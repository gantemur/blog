#!/usr/bin/env python3
"""Export selected blog posts into a combined Markdown/Pandoc LaTeX source."""

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src" / "posts"
MEDIA_DIR = ROOT / "src" / "assets" / "wp-media"


def new_diagnostics():
    return {
        "images_copied": 0,
        "image_links_rewritten": 0,
        "linked_image_wrappers_simplified": 0,
        "captions_inferred": 0,
        "images_with_explicit_width_preserved": 0,
        "unresolved_images": 0,
    }


def split_front_matter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    front = text[4:end]
    body = text[end + 5 :]
    return parse_simple_yaml(front), body.lstrip("\n")


def parse_simple_yaml(text):
    data = {}
    current_key = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_key:
            data.setdefault(current_key, []).append(parse_scalar(list_match.group(1)))
            continue
        key_match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not key_match:
            continue
        key, value = key_match.groups()
        current_key = key
        value = (value or "").strip()
        if value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(value)
    return data


def parse_scalar(value):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in split_csv(inner)]
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def split_csv(value):
    parts = []
    current = []
    quote = None
    for char in value:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            current.append(char)
            quote = char
        elif char == ",":
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
    parts.append("".join(current))
    return parts


def yaml_quote(value):
    return json.dumps(str(value), ensure_ascii=False)


def latex_escape_text(value):
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


def resolve_latex_names(manifest, args):
    language = str(manifest.get("language") or manifest.get("lang") or "").casefold()
    figure_name = args.figure_name if args.figure_name is not None else manifest.get("figureName")
    table_name = args.table_name if args.table_name is not None else manifest.get("tableName")
    toc_title = args.toc_title if args.toc_title is not None else manifest.get("tocTitle")
    if language in {"mn", "mongolian"}:
        figure_name = figure_name or "Зураг"
        table_name = table_name or "Хүснэгт"
        toc_title = toc_title or "Гарчиг"
    return figure_name, table_name, toc_title


def latex_name_header_include(figure_name, table_name, toc_title):
    if not figure_name and not table_name and not toc_title:
        return []

    commands = []
    if toc_title:
        commands.append(rf"\renewcommand{{\contentsname}}{{{latex_escape_text(toc_title)}}}%")
    if figure_name:
        commands.append(rf"\renewcommand{{\figurename}}{{{latex_escape_text(figure_name)}}}%")
    if table_name:
        commands.append(rf"\renewcommand{{\tablename}}{{{latex_escape_text(table_name)}}}%")

    lines = [
        "header-includes:",
        "  - |",
        "    \\makeatletter",
        "    \\@ifundefined{captionsmongolian}{}{%",
        "      \\addto\\captionsmongolian{%",
    ]
    lines.extend(f"        {command}" for command in commands)
    lines.extend(
        [
            "      }%",
            "    }",
            "    \\@ifundefined{captionsmn}{}{%",
            "      \\addto\\captionsmn{%",
        ]
    )
    lines.extend(f"        {command}" for command in commands)
    lines.extend(
        [
            "      }%",
            "    }",
            "    \\AtBeginDocument{%",
        ]
    )
    lines.extend(f"      {command}" for command in commands)
    lines.extend(
        [
            "    }",
            "    \\makeatother",
        ]
    )
    return lines


def resolve_toc_options(manifest, args):
    toc = args.toc if args.toc is not None else bool(manifest.get("toc", False))
    toc_depth = args.toc_depth if args.toc_depth is not None else manifest.get("tocDepth")
    if toc_depth is not None:
        try:
            toc_depth = int(toc_depth)
        except (TypeError, ValueError) as error:
            raise SystemExit("tocDepth / --toc-depth must be an integer") from error
        if toc_depth < 1:
            raise SystemExit("tocDepth / --toc-depth must be at least 1")
    return toc, toc_depth


def resolve_existing_option_path(value, option_name):
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        raise SystemExit(f"{option_name} file not found: {path}")
    return path


def resolve_pandoc_options(manifest, args):
    template = args.template if args.template is not None else manifest.get("template")
    include_header = args.include_header if args.include_header is not None else manifest.get("includeHeader")
    return {
        "template": resolve_existing_option_path(template, "--template"),
        "include_header": resolve_existing_option_path(include_header, "--include-header"),
    }


def normalize_path(value):
    if not value:
        return None
    value = html.unescape(str(value)).strip()
    value = value.split("#", 1)[0].split("?", 1)[0]
    parsed = urlparse(value)
    path = parsed.path if parsed.scheme or parsed.netloc else value
    path = unquote(path)
    if not path:
        return None
    if not path.startswith("/"):
        path = "/" + path
    if not PurePosixPath(path).suffix and not path.endswith("/"):
        path += "/"
    return path


def path_variants(value):
    path = normalize_path(value)
    if not path:
        return []
    variants = {path, path.rstrip("/")}
    if path.startswith("/blog/"):
        short = path[len("/blog") :]
        variants.update({short, short.rstrip("/")})
    else:
        blog = "/blog" + path
        variants.update({blog, blog.rstrip("/")})
    return [variant for variant in variants if variant]


def add_mapping(mapping, key, post):
    for variant in path_variants(key):
        mapping.setdefault(variant, post)


def build_post_index():
    mapping = {}
    posts = []
    slug_counts = {}
    for path in sorted(POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        front, body = split_front_matter(text)
        post = {"path": path, "front": front, "body": body}
        posts.append(post)
        add_mapping(mapping, front.get("permalink"), post)
        add_mapping(mapping, front.get("wordpress_url"), post)
        slug = front.get("slug")
        if slug:
            slug_counts[slug] = slug_counts.get(slug, 0) + 1
    for post in posts:
        slug = post["front"].get("slug")
        if slug and slug_counts.get(slug) == 1:
            mapping.setdefault(slug, post)
            mapping.setdefault("/" + slug + "/", post)
    return mapping, posts


def load_manifest(path):
    manifest = parse_simple_yaml(path.read_text(encoding="utf-8"))
    if not isinstance(manifest.get("posts"), list):
        raise SystemExit(f"Manifest must include a posts list: {path}")
    manifest.setdefault("division", "chapter")
    manifest.setdefault("language", "mn")
    return manifest


def section_title(line):
    stripped = line.strip()
    heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", stripped)
    if heading:
        return heading.group(2).strip()
    bold = re.match(r"^\*\*(.+?)\*\*\s*$", stripped)
    if bold:
        return bold.group(1).strip()
    return None


def extract_section(markdown, requested):
    if not requested:
        return markdown
    lines = markdown.splitlines()
    selected = []
    in_section = False
    requested_norm = requested.strip().casefold()
    for line in lines:
        title = section_title(line)
        if title:
            if in_section:
                break
            if title.casefold() == requested_norm:
                in_section = True
                continue
        elif in_section:
            selected.append(line)
    if not in_section:
        raise SystemExit(f"Section not found: {requested}")
    return "\n".join(selected)


def links_from_markdown(markdown):
    links = []
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", markdown):
        links.append(match.group(1))
    return links


def resolve_refs(refs, mapping):
    resolved = []
    unresolved = []
    seen = set()
    for ref in refs:
        post = None
        for variant in path_variants(ref):
            post = mapping.get(variant)
            if post:
                break
        if not post:
            unresolved.append(ref)
            continue
        key = str(post["path"])
        if key in seen:
            continue
        seen.add(key)
        resolved.append({"ref": ref, "post": post})
    return resolved, unresolved


def media_path_from_url(value):
    value = html.unescape(str(value))
    parsed = urlparse(value)
    path = unquote(parsed.path)
    if path.startswith("/blog/assets/wp-media/"):
        return path.split("/blog/assets/wp-media/", 1)[1]
    if path.startswith("/assets/wp-media/"):
        return path.split("/assets/wp-media/", 1)[1]
    for marker in ("/wp-content/uploads/", "/files/"):
        if marker in path:
            tail = path.split(marker, 1)[1]
            parts = PurePosixPath(tail).parts
            for index in range(len(parts) - 2):
                if re.fullmatch(r"\d{4}", parts[index]) and re.fullmatch(r"\d{2}", parts[index + 1]):
                    return "/".join(parts[index:])
    return None


def rewrite_asset_url(value, out_dir, copied, unresolved_images, diagnostics):
    media_path = media_path_from_url(value)
    if not media_path:
        return value
    source = MEDIA_DIR / media_path
    if not source.exists():
        unresolved_images.append(value)
        diagnostics["unresolved_images"] += 1
        return value
    destination = out_dir / "assets" / "wp-media" / media_path
    if source not in copied:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.add(source)
        diagnostics["images_copied"] += 1
    rewritten = PurePosixPath("assets/wp-media") / media_path
    if str(rewritten) != str(value):
        diagnostics["image_links_rewritten"] += 1
    return rewritten


def rewrite_assets(markdown, out_dir, copied, unresolved_images, diagnostics):
    def md_image(match):
        alt, url, title = match.groups()
        rewritten = rewrite_asset_url(url, out_dir, copied, unresolved_images, diagnostics)
        suffix = f' "{title}"' if title else ""
        return f"![{alt}]({rewritten}{suffix})"

    def linked_md_image(match):
        image, url, title = match.groups()
        rewritten = rewrite_asset_url(url, out_dir, copied, unresolved_images, diagnostics)
        suffix = f' "{title}"' if title else ""
        return f"[{image}]({rewritten}{suffix})"

    def html_attr(match):
        attr, quote, url = match.groups()
        rewritten = rewrite_asset_url(url, out_dir, copied, unresolved_images, diagnostics)
        return f"{attr}={quote}{rewritten}{quote}"

    markdown = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)", md_image, markdown)
    markdown = re.sub(r"\[(!\[[^\]]*\]\([^)]+\))\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)", linked_md_image, markdown)
    markdown = re.sub(r"\b(src|href)=(['\"])([^'\"]+)\2", html_attr, markdown)
    return markdown


def same_image_path(left, right):
    left_path = normalize_path(str(left))
    right_path = normalize_path(str(right))
    if not left_path or not right_path:
        return str(left) == str(right)
    return left_path == right_path


def clean_caption(value):
    value = re.sub(r"<[^>]+>", "", value or "")
    return html.unescape(value).strip()


def parse_html_attrs(attrs):
    parsed = {}
    for match in re.finditer(r"([A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*(['\"])(.*?)\2", attrs or "", flags=re.S):
        parsed[match.group(1).lower()] = html.unescape(match.group(3).strip())
    return parsed


def width_attribute(attrs):
    width = attrs.get("width")
    style = attrs.get("style", "")
    classes = set((attrs.get("class") or "").split())
    if width:
        width = width.strip()
        if re.fullmatch(r"\d+", width):
            return f"{{width={width}px}}", True
        if re.fullmatch(r"\d+(?:\.\d+)?px", width):
            return f"{{width={width}}}", True
        if re.fullmatch(r"\d+(?:\.\d+)?%", width):
            return f"{{width={width}}}", True
    style_width = re.search(r"(?:^|;)\s*width\s*:\s*([^;]+)", style)
    if style_width:
        value = style_width.group(1).strip()
        if re.fullmatch(r"\d+(?:\.\d+)?px", value) or re.fullmatch(r"\d+(?:\.\d+)?%", value):
            return f"{{width={value}}}", True
    if "size-medium" in classes:
        return "{width=60%}", False
    if "size-large" in classes:
        return "{width=90%}", False
    return "", False


def markdown_image(alt, path, attr=""):
    return f"![{alt}]({path}){attr}"


def html_img_to_markdown(img_tag, caption, diagnostics):
    attrs = parse_html_attrs(img_tag)
    src = attrs.get("src")
    if not src:
        return img_tag
    alt = clean_caption(caption) or attrs.get("alt", "")
    attr, explicit_width = width_attribute(attrs)
    if explicit_width:
        diagnostics["images_with_explicit_width_preserved"] += 1
    if alt:
        diagnostics["captions_inferred"] += 1
    return markdown_image(alt, src, attr)


def convert_html_figures(markdown, diagnostics):
    def figure_repl(match):
        img_tag = match.group(1)
        caption = match.group(2) or ""
        return html_img_to_markdown(img_tag, caption, diagnostics)

    markdown = re.sub(
        r"<figure\b[^>]*>\s*(?:<a\b[^>]*>\s*)?(<img\b[^>]*>)\s*(?:</a>\s*)?(?:<figcaption\b[^>]*>(.*?)</figcaption>\s*)?</figure>",
        figure_repl,
        markdown,
        flags=re.I | re.S,
    )
    return re.sub(r"<img\b([^>]*?)\/?>", lambda match: html_img_to_markdown(match.group(0), "", diagnostics), markdown, flags=re.I | re.S)


def normalize_markdown_image_lines(markdown, diagnostics):
    linked_pattern = re.compile(
        r"^\s*\[!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)(\{[^}\n]*\})?\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)([^\n]*)$"
    )
    plain_pattern = re.compile(r"^\s*!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)(\{[^}\n]*\})?([^\n]*)$")
    lines = []
    for line in markdown.splitlines():
        linked = linked_pattern.match(line)
        if linked and same_image_path(linked.group(2), linked.group(4)):
            alt = linked.group(1)
            path = linked.group(2)
            attr = linked.group(3) or ""
            caption = linked.group(5).strip()
            diagnostics["linked_image_wrappers_simplified"] += 1
            if caption:
                diagnostics["captions_inferred"] += 1
                alt = alt or caption
            lines.append(markdown_image(alt, path, attr))
            continue
        plain = plain_pattern.match(line)
        if plain:
            alt = plain.group(1)
            path = plain.group(2)
            attr = plain.group(3) or ""
            caption = plain.group(4).strip()
            if caption:
                diagnostics["captions_inferred"] += 1
                alt = alt or caption
                lines.append(markdown_image(alt, path, attr))
            else:
                lines.append(line.strip())
            continue
        lines.append(line)
    return "\n".join(lines)


def normalize_figure_spacing(markdown):
    image_line = re.compile(r"^\s*!\[[^\]]*\]\([^)]+\)(?:\{[^}]+\})?\s*$")
    output = []
    for line in markdown.splitlines():
        if image_line.match(line):
            if output and output[-1] != "":
                output.append("")
            output.append(line.strip())
            output.append("")
        else:
            output.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(output)).strip() + "\n"


def post_process_images(markdown, diagnostics):
    markdown = convert_html_figures(markdown, diagnostics)
    markdown = normalize_markdown_image_lines(markdown, diagnostics)
    return normalize_figure_spacing(markdown)


def normalize_math_delimiters(markdown):
    return (
        markdown.replace(r"\\(", r"\(")
        .replace(r"\\)", r"\)")
        .replace(r"\\[", r"\[")
        .replace(r"\\]", r"\]")
    )


def adjust_headings(markdown, inserted_level):
    minimum = inserted_level + 1

    def repl(match):
        hashes, title = match.groups()
        level = max(len(hashes), minimum)
        return "#" * min(level, 6) + " " + title

    return re.sub(r"^(#{1,6})\s+(.+)$", repl, markdown, flags=re.M)


def post_heading_level(division):
    if division == "section":
        return 2
    if division != "chapter":
        raise SystemExit("division must be either 'chapter' or 'section'")
    return 1


def pandoc_command(pandoc_path, book_md, out_dir, output_path, args, output_kind, toc, toc_depth, pandoc_options):
    command = [
        pandoc_path,
        str(book_md),
        "--resource-path",
        str(out_dir),
        "-f",
        "markdown+raw_tex+tex_math_single_backslash",
    ]
    if toc:
        command.append("--toc")
    if toc_depth is not None:
        command.append(f"--toc-depth={toc_depth}")
    if pandoc_options["template"]:
        command.append(f"--template={pandoc_options['template']}")
    if pandoc_options["include_header"]:
        command.append(f"--include-in-header={pandoc_options['include_header']}")
    if args.mainfont:
        command.extend(["-V", f"mainfont={args.mainfont}"])
    if output_kind == "tex":
        command.extend(["-s", "-t", "latex"])
    elif output_kind == "pdf":
        command.extend(["--pdf-engine", args.pdf_engine])
    else:
        raise ValueError(f"Unknown Pandoc output kind: {output_kind}")
    command.extend(["-o", str(output_path)])
    return command


def run_pandoc(command):
    result = {"command": command, "ok": False, "error": None}
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        result["ok"] = True
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or error.stdout or str(error)).strip()
        result["error"] = detail
    return result


def export_book(manifest, resolved, unresolved_refs, out_dir, args):
    out_dir.mkdir(parents=True, exist_ok=True)
    copied = set()
    unresolved_images = []
    diagnostics = new_diagnostics()
    division = manifest.get("division", "chapter")
    figure_name, table_name, toc_title = resolve_latex_names(manifest, args)
    toc, toc_depth = resolve_toc_options(manifest, args)
    pandoc_options = resolve_pandoc_options(manifest, args)
    heading_level = post_heading_level(division)
    lines = [
        "---",
        f"title: {yaml_quote(manifest.get('title', 'Blog export'))}",
        f"author: {yaml_quote(manifest.get('author', ''))}",
        f"lang: {yaml_quote(manifest.get('language', 'mn'))}",
        *latex_name_header_include(figure_name, table_name, toc_title),
        "---",
        "",
    ]
    resolved_posts = []
    for item in resolved:
        post = item["post"]
        front = post["front"]
        title = front.get("title") or front.get("slug") or post["path"].stem
        date = front.get("date", "")
        permalink = front.get("permalink", "")
        body = normalize_math_delimiters(post["body"])
        body = rewrite_assets(body, out_dir, copied, unresolved_images, diagnostics).strip()
        body = post_process_images(body, diagnostics).strip()
        body = adjust_headings(body, heading_level)
        lines.append("#" * heading_level + f" {title}")
        lines.append("")
        if date or permalink:
            meta = " · ".join(str(part) for part in [date, permalink] if part)
            lines.append(f"*{meta}*")
            lines.append("")
        lines.append(body)
        lines.append("")
        lines.append("")
        resolved_posts.append(
            {
                "ref": item["ref"],
                "title": title,
                "date": date,
                "permalink": permalink,
                "source": str(post["path"].relative_to(ROOT)),
            }
        )
    book_md = out_dir / "book.md"
    book_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    pandoc_path = shutil.which("pandoc")
    book_tex = out_dir / "book.tex"
    book_pdf = out_dir / "book.pdf"
    pandoc_report = {
        "found": bool(pandoc_path),
        "path": pandoc_path,
        "wrote_tex": False,
        "wrote_pdf": False,
        "tex_command": None,
        "pdf_command": None,
        "tex_error": None,
        "pdf_error": None,
    }
    if pandoc_path:
        tex_result = run_pandoc(pandoc_command(pandoc_path, book_md, out_dir, book_tex, args, "tex", toc, toc_depth, pandoc_options))
        pandoc_report["tex_command"] = tex_result["command"]
        pandoc_report["wrote_tex"] = tex_result["ok"]
        pandoc_report["tex_error"] = tex_result["error"]
        if args.pdf:
            pdf_result = run_pandoc(pandoc_command(pandoc_path, book_md, out_dir, book_pdf, args, "pdf", toc, toc_depth, pandoc_options))
            pandoc_report["pdf_command"] = pdf_result["command"]
            pandoc_report["wrote_pdf"] = pdf_result["ok"]
            pandoc_report["pdf_error"] = pdf_result["error"]
    manifest_resolved = {
        "title": manifest.get("title"),
        "author": manifest.get("author"),
        "language": manifest.get("language", "mn"),
        "division": division,
        "posts": resolved_posts,
        "unresolved_refs": unresolved_refs,
        "unresolved_images": sorted(set(unresolved_images)),
        "diagnostics": diagnostics,
        "latex_names": {"contents": toc_title, "figure": figure_name, "table": table_name},
        "toc": {"enabled": toc, "depth": toc_depth, "title": toc_title},
        "pandoc_options": {
            "template": str(pandoc_options["template"].relative_to(ROOT)) if pandoc_options["template"] else None,
            "include_header": str(pandoc_options["include_header"].relative_to(ROOT)) if pandoc_options["include_header"] else None,
        },
        "caption_names": {"figure": figure_name, "table": table_name},
        "pandoc": pandoc_report,
    }
    (out_dir / "manifest-resolved.json").write_text(
        json.dumps(manifest_resolved, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return book_md, book_tex if pandoc_report["wrote_tex"] else None, book_pdf if pandoc_report["wrote_pdf"] else None, manifest_resolved


def manifest_from_contents(args, mapping):
    contents_path = ROOT / args.contents
    front, body = split_front_matter(contents_path.read_text(encoding="utf-8"))
    selected = extract_section(body, args.section)
    refs = links_from_markdown(selected)
    resolved, unresolved = resolve_refs(refs, mapping)
    title = front.get("title") or contents_path.stem
    if args.section:
        title = f"{title}: {args.section}"
    return {
        "title": title,
        "author": "",
        "language": "mn",
        "division": "chapter",
        "posts": [item["ref"] for item in resolved],
    }, resolved, unresolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--manifest", type=Path, help="YAML manifest listing posts to export")
    mode.add_argument("--contents", help="Contents/topic Markdown page to scan for post links")
    parser.add_argument("--section", help="Section title to export from a contents/topic page")
    parser.add_argument("--out", required=True, type=Path, help="Output directory, e.g. exports/example")
    parser.add_argument("--pdf", action="store_true", help="Also generate book.pdf with Pandoc")
    parser.add_argument("--pdf-engine", default="xelatex", help="Pandoc PDF engine to use with --pdf")
    parser.add_argument("--mainfont", help="Main font passed to Pandoc, e.g. Times New Roman")
    parser.add_argument("--figure-name", help="LaTeX figure caption name, e.g. Зураг")
    parser.add_argument("--table-name", help="LaTeX table caption name, e.g. Хүснэгт")
    parser.add_argument("--toc", action="store_true", default=None, help="Include a table of contents in Pandoc TeX/PDF output")
    parser.add_argument("--toc-depth", type=int, help="Pandoc table-of-contents depth")
    parser.add_argument("--toc-title", help="LaTeX table-of-contents title, e.g. Гарчиг")
    parser.add_argument("--template", help="Pandoc LaTeX template path")
    parser.add_argument("--include-header", help="Extra LaTeX header file passed to Pandoc")
    args = parser.parse_args()

    mapping, _posts = build_post_index()
    if args.manifest:
        manifest_path = ROOT / args.manifest
        manifest = load_manifest(manifest_path)
        resolved, unresolved = resolve_refs(manifest["posts"], mapping)
    else:
        manifest, resolved, unresolved = manifest_from_contents(args, mapping)
    if not resolved:
        raise SystemExit("No posts resolved for export.")

    out_dir = ROOT / args.out
    book_md, book_tex, book_pdf, report = export_book(manifest, resolved, unresolved, out_dir, args)
    print(f"Wrote {book_md.relative_to(ROOT)}")
    print(f"Wrote {(out_dir / 'manifest-resolved.json').relative_to(ROOT)}")
    if book_tex:
        print(f"Wrote {book_tex.relative_to(ROOT)}")
    elif report["pandoc"]["tex_error"]:
        print("Pandoc could not generate book.tex.", file=sys.stderr)
        print(f"Command: {' '.join(report['pandoc']['tex_command'])}", file=sys.stderr)
        print(report["pandoc"]["tex_error"], file=sys.stderr)
    else:
        print("Pandoc was not found; book.tex was not generated.")
        print(f"To generate LaTeX later: pandoc {book_md.relative_to(ROOT)} --resource-path={out_dir.relative_to(ROOT)} -s -f markdown+raw_tex -t latex -o {(out_dir / 'book.tex').relative_to(ROOT)}")
    if args.pdf:
        if book_pdf:
            print(f"Wrote {book_pdf.relative_to(ROOT)}")
        elif report["pandoc"]["pdf_error"]:
            print("Pandoc could not generate book.pdf.", file=sys.stderr)
            print(f"Command: {' '.join(report['pandoc']['pdf_command'])}", file=sys.stderr)
            print(report["pandoc"]["pdf_error"], file=sys.stderr)
        elif not report["pandoc"]["found"]:
            print(f"To generate PDF later: pandoc {book_md.relative_to(ROOT)} --resource-path={out_dir.relative_to(ROOT)} --pdf-engine={args.pdf_engine} -o {(out_dir / 'book.pdf').relative_to(ROOT)}")
    if report["unresolved_refs"]:
        print(f"Unresolved post links: {len(report['unresolved_refs'])}", file=sys.stderr)
    if report["unresolved_images"]:
        print(f"Unresolved images: {len(report['unresolved_images'])}", file=sys.stderr)


if __name__ == "__main__":
    main()
