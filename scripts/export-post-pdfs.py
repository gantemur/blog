#!/usr/bin/env python3
"""Generate selected per-post PDFs from source Markdown."""

import argparse
import os
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

from post_pdf_provenance import asset_hashes, digest, source_record

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src" / "posts"
POST_PDF_DIR = ROOT / "src" / "assets" / "pdf" / "posts"
POST_PDF_DATA = ROOT / "src" / "_data" / "post_pdfs.json"
PROVENANCE = ROOT / "src" / "_data" / "post_pdf_provenance.json"


def parse_scalar(value):
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return value


def parse_front_matter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    data = {}
    front = text[4:end]
    body = text[end + 5 :].lstrip("\n")
    current_map = None
    current_list = None
    for raw_line in front.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        child = re.match(r"^\s{2,}([A-Za-z0-9_-]+):(?:\s*(.*))?$", raw_line)
        if child and current_map:
            key, value = child.groups()
            data[current_map][key] = parse_scalar((value or "").strip()) if (value or "").strip() else {}
            continue
        item = re.match(r"^\s*-\s+(.*)$", raw_line)
        if item and current_list:
            data[current_list].append(parse_scalar(item.group(1)))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", raw_line)
        if not match:
            current_map = None
            current_list = None
            continue
        key, value = match.groups()
        value = (value or "").strip()
        current_map = None
        current_list = None
        if value == "":
            data[key] = {}
            current_map = key
        else:
            data[key] = parse_scalar(value)
            if isinstance(data[key], list):
                current_list = key
    return data, body


def split_post(path):
    text = path.read_text(encoding="utf-8")
    front, body = parse_front_matter(text)
    return front, body


def pdf_config(front):
    pdf = front.get("pdf")
    if pdf is True:
        return {"enabled": True, "source": "generated"}
    if not pdf or pdf is False or not isinstance(pdf, dict):
        return {"enabled": False}
    config = dict(pdf)
    config["enabled"] = config.get("enabled", True) is not False
    config["source"] = config.get("source") or ("external" if config.get("url") else "generated")
    return config


def should_generate(front):
    config = pdf_config(front)
    if not config.get("enabled"):
        return False
    if config.get("url") or config.get("source") == "external":
        return False
    return True


def post_slug(front):
    if front.get("slug"):
        return str(front["slug"])
    permalink = str(front.get("permalink") or "").strip("/")
    if permalink:
        return PurePosixPath(permalink).name
    raise SystemExit(f"Post has no slug or permalink: {front.get('title', '[untitled]')}")


def post_date_parts(front):
    date = str(front.get("date") or "")
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", date)
    if not match:
        raise SystemExit(f"Post has no YYYY-MM-DD date: {front.get('title', '[untitled]')}")
    return match.groups()


def normalize_math_delimiters(markdown):
    return (
        markdown.replace(r"\\(", r"\(")
        .replace(r"\\)", r"\)")
        .replace(r"\\[", r"\[")
        .replace(r"\\]", r"\]")
    )


def rewrite_asset_paths(markdown):
    markdown = markdown.replace("(/blog/assets/", "(src/assets/")
    markdown = markdown.replace('"/blog/assets/', '"src/assets/')
    markdown = markdown.replace("'/blog/assets/", "'src/assets/")
    markdown = markdown.replace("(/assets/", "(src/assets/")
    markdown = markdown.replace('"/assets/', '"src/assets/')
    markdown = markdown.replace("'/assets/", "'src/assets/")
    return markdown


def latex_escape(value):
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in str(value))


def toc_options(front, config):
    toc = config.get("toc", front.get("pdfToc", False))
    depth = config.get("tocDepth", front.get("pdfTocDepth"))
    return bool(toc), int(depth) if depth is not None else None


def layout_options(front, config, args):
    papersize = config.get("papersize") or front.get("pdfPapersize") or args.papersize or "a4"
    margin = config.get("margin") or front.get("pdfMargin") or args.margin or "25mm"
    return str(papersize), str(margin)


def post_markdown(front, body):
    title = front.get("title") or post_slug(front)
    body = rewrite_asset_paths(normalize_math_delimiters(body)).strip()
    header = [
        "---",
        f"title: {json.dumps(str(title), ensure_ascii=False)}",
        'lang: "mn"',
        "header-includes:",
        "  - |",
        "    \\AtBeginDocument{%",
        "      \\renewcommand{\\contentsname}{Гарчиг}%",
        "      \\renewcommand{\\figurename}{Зураг}%",
        "      \\renewcommand{\\tablename}{Хүснэгт}%",
        "    }",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if front.get("date") or front.get("permalink"):
        meta = " · ".join(str(part) for part in [front.get("date"), front.get("permalink")] if part)
        header.extend([f"*{meta}*", ""])
    return "\n".join(header) + body + "\n"


def pandoc_command(pandoc, source_md, staged_pdf, args, toc, toc_depth, papersize, margin):
    command = [
        pandoc,
        str(source_md),
        "--resource-path",
        str(ROOT),
        "-f",
        "markdown+raw_tex+tex_math_single_backslash",
        "--pdf-engine",
        args.pdf_engine,
        "-V",
        f"mainfont={args.mainfont}",
        "-V",
        f"papersize={papersize}",
        "-V",
        f"geometry:margin={margin}",
        "-V",
        "colorlinks=true",
        "-V",
        "linkcolor=blue",
        "-V",
        "urlcolor=blue",
        "-V",
        "toccolor=blue",
        "-o",
        str(staged_pdf),
    ]
    if toc:
        command.insert(1, "--toc")
    if toc_depth is not None:
        command.insert(1, f"--toc-depth={toc_depth}")
    return command


def export_post(path, pandoc, args, staging):
    source_hash = digest(path)
    images = asset_hashes(ROOT, path)
    front, body = split_post(path)
    config = pdf_config(front)
    if not should_generate(front):
        return None
    year, month, day = post_date_parts(front)
    slug = post_slug(front)
    output_dir = POST_PDF_DIR / year / month / day
    output_pdf = output_dir / f"{slug}.pdf"
    staged_pdf = staging / f"{year}-{month}-{day}-{slug}.pdf"
    toc, toc_depth = toc_options(front, config)
    papersize, margin = layout_options(front, config, args)
    with tempfile.TemporaryDirectory(prefix="blog-post-pdf-") as tmp:
        source_md = Path(tmp) / f"{slug}.md"
        source_md.write_text(post_markdown(front, body), encoding="utf-8")
        command = pandoc_command(pandoc, source_md, staged_pdf, args, toc, toc_depth, papersize, margin)
        try:
            rendered = subprocess.run(command, check=True, capture_output=True, text=True)
            if "Missing character:" in (rendered.stderr + rendered.stdout):
                raise SystemExit("PDF font is missing required glyphs; staged output was not installed")
        except subprocess.CalledProcessError as error:
            print(f"Pandoc failed for {path}", file=sys.stderr)
            print("Command: " + " ".join(command), file=sys.stderr)
            print((error.stderr or error.stdout or str(error)).strip(), file=sys.stderr)
            raise SystemExit(1) from error
    permalink = front.get("permalink")
    if not permalink:
        raise SystemExit(f"Post has no permalink: {path}")
    url = f"/blog/assets/pdf/posts/{year}/{month}/{day}/{slug}.pdf"
    provenance = source_record(ROOT, path, staged_pdf, {
        "engine": args.pdf_engine, "mainfont": args.mainfont,
        "papersize": papersize, "margin": margin,
        "pandoc": subprocess.check_output([pandoc, "--version"], text=True).splitlines()[0],
    })
    if provenance["source_sha256"] != source_hash or provenance["assets"] != images:
        raise SystemExit("Source or image changed during rendering; staged output was not installed")
    return {
        "staged": staged_pdf,
        "provenance": provenance,
        "source": str(path.relative_to(ROOT)),
        "title": front.get("title"),
        "permalink": permalink,
        "url": url,
        "output": str(output_pdf.relative_to(ROOT)),
        "toc": toc,
        "tocDepth": toc_depth,
        "papersize": papersize,
        "margin": margin,
    }


def selected_posts(args):
    if args.post:
        return [ROOT / value for value in args.post]
    return sorted(POSTS_DIR.glob("*.md"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all-enabled", action="store_true", help="Generate PDFs for all posts with generated PDF enabled")
    parser.add_argument("--post", action="append", help="Generate only a specific post source path; can be repeated")
    parser.add_argument("--pdf-engine", default="xelatex", help="Pandoc PDF engine")
    parser.add_argument("--mainfont", default="Times New Roman", help="Main font passed to Pandoc")
    parser.add_argument("--papersize", default="a4", help="Pandoc/LaTeX paper size, default: a4")
    parser.add_argument("--margin", default="25mm", help="Pandoc/LaTeX page margin, default: 25mm")
    args = parser.parse_args()

    if bool(args.all_enabled) == bool(args.post):
        parser.error("Select --post PATH (repeatable) or explicitly --all-enabled")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("Pandoc was not found. Install Pandoc before generating post PDFs.")
    if not shutil.which(args.pdf_engine):
        raise SystemExit(f"PDF engine was not found on PATH: {args.pdf_engine}")

    paths = selected_posts(args)
    # Resolve and validate the complete selection before any PDF output is touched.
    posts = []
    targets = set()
    mapping = json.loads(POST_PDF_DATA.read_text()) if POST_PDF_DATA.exists() else {}
    provenance = json.loads(PROVENANCE.read_text()) if PROVENANCE.exists() else {}
    known = {}
    for candidate in POSTS_DIR.glob("*.md"):
        front, _ = split_post(candidate)
        if should_generate(front):
            permalink = front.get("permalink")
            if permalink in known:
                raise SystemExit("Generated posts must have unique permalinks")
            known[permalink] = candidate.resolve()
    for path in paths:
        path = path.resolve()
        if path.parent != POSTS_DIR.resolve() or path.suffix != ".md" or not path.is_file():
            raise SystemExit("--post must name a Markdown file directly in src/posts/")
        front, _ = split_post(path)
        if not should_generate(front):
            if args.post:
                raise SystemExit(f"Selected post does not enable generated PDFs: {path.name}")
            continue
        year, month, day = post_date_parts(front)
        slug = post_slug(front)
        if slug in {".", ".."} or re.search(r"[/\\]", slug):
            raise SystemExit("PDF slug must be a single safe filename component")
        permalink = front.get("permalink")
        if not isinstance(permalink, str) or not permalink.startswith('/'):
            raise SystemExit("Generated PDF needs an absolute post permalink")
        url = f"/blog/assets/pdf/posts/{year}/{month}/{day}/{slug}.pdf"
        if url in targets or any(k != permalink and v == url for k, v in mapping.items()):
            raise SystemExit("Two selected posts or mappings would share one PDF output")
        targets.add(url)
        # Validate image availability before invoking Pandoc.
        asset_hashes(ROOT, path)
        posts.append(path)
    generated = []
    # Stage the entire selection first: a renderer failure leaves existing PDFs/maps intact.
    with tempfile.TemporaryDirectory(prefix="blog-pdf-stage-", dir=ROOT) as tmp:
        for path in posts:
            generated.append(export_post(path, pandoc, args, Path(tmp)))
        for item in generated:
            mapping[item['permalink']] = item['url']
            provenance[item['permalink']] = item['provenance']
        for item in generated:
            output = ROOT / item['output']
            output.parent.mkdir(parents=True, exist_ok=True)
            os.replace(item['staged'], output)
        for path, data in [(POST_PDF_DATA, mapping), (PROVENANCE, provenance)]:
            path.parent.mkdir(parents=True, exist_ok=True)
            staged = Path(tmp) / path.name
            staged.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            os.replace(staged, path)

    for item in generated:
        toc = " with ToC" if item["toc"] else ""
        print(f"Wrote {item['output']} for {item['permalink']}{toc}, {item['papersize']} paper, {item['margin']} margin")
    print(f"Wrote {POST_PDF_DATA.relative_to(ROOT)} with {len(mapping)} entries")


if __name__ == "__main__":
    main()
