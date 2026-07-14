#!/usr/bin/env python3
"""Validate optional per-post PDF download configuration."""

import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src" / "posts"
POST_PDF_DIR = ROOT / "src" / "assets" / "pdf" / "posts"
POST_PDF_DATA = ROOT / "src" / "_data" / "post_pdfs.json"


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
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data = {}
    front = text[4:end]
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
    return data


def read_front_matter(path):
    return parse_front_matter(path.read_text(encoding="utf-8"))


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


def is_generated(config):
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
    return None


def post_date_parts(front):
    date = str(front.get("date") or "")
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", date)
    if not match:
        return None
    return match.groups()


def generated_pdf_paths(front):
    date_parts = post_date_parts(front)
    slug = post_slug(front)
    permalink = front.get("permalink")
    if not date_parts or not slug or not permalink:
        return None, None, None
    year, month, day = date_parts
    pdf_path = POST_PDF_DIR / year / month / day / f"{slug}.pdf"
    url = f"/blog/assets/pdf/posts/{year}/{month}/{day}/{slug}.pdf"
    return str(permalink), pdf_path, url


def local_url_path(url):
    if url.startswith("/blog/assets/"):
        return ROOT / "src" / "assets" / url.removeprefix("/blog/assets/")
    if url.startswith("/assets/"):
        return ROOT / "src" / "assets" / url.removeprefix("/assets/")
    return None


def data_url_to_path(url):
    return local_url_path(url)


def main():
    errors = []
    warnings = []
    checked = 0
    generated_expected = 0
    generated_found = 0
    local_static_expected = 0
    local_static_found = 0
    remote_static = 0

    if POST_PDF_DATA.exists():
        try:
            post_pdf_map = json.loads(POST_PDF_DATA.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"Invalid JSON in {POST_PDF_DATA.relative_to(ROOT)}: {error}")
            post_pdf_map = {}
    else:
        post_pdf_map = {}

    generated_permalinks = set()

    for path in sorted(POSTS_DIR.glob("*.md")):
        checked += 1
        front = read_front_matter(path)
        config = pdf_config(front)
        if not config.get("enabled"):
            continue

        rel = path.relative_to(ROOT)
        if is_generated(config):
            generated_expected += 1
            permalink, pdf_path, expected_url = generated_pdf_paths(front)
            if not permalink or not pdf_path or not expected_url:
                errors.append(f"{rel}: generated PDF needs date, slug/permalink, and permalink front matter")
                continue
            generated_permalinks.add(permalink)
            if pdf_path.exists():
                generated_found += 1
                if pdf_path.stat().st_mtime < path.stat().st_mtime:
                    warnings.append(f"{rel}: generated PDF may be stale: {pdf_path.relative_to(ROOT)}")
            else:
                errors.append(f"{rel}: missing generated PDF {pdf_path.relative_to(ROOT)}")

            mapped_url = post_pdf_map.get(permalink)
            if mapped_url != expected_url:
                errors.append(f"{rel}: {POST_PDF_DATA.relative_to(ROOT)} maps {permalink!r} to {mapped_url!r}, expected {expected_url!r}")
                continue
            mapped_path = data_url_to_path(mapped_url)
            if not mapped_path or not mapped_path.exists():
                errors.append(f"{rel}: generated map URL points to missing local file: {mapped_url}")
            continue

        url = str(config.get("url") or "")
        if url.startswith(("http://", "https://")):
            remote_static += 1
            warnings.append(f"{rel}: remote PDF URL not checked locally: {url}")
            continue

        local_path = local_url_path(url)
        if local_path:
            local_static_expected += 1
            if local_path.exists():
                local_static_found += 1
            else:
                errors.append(f"{rel}: missing local static PDF {local_path.relative_to(ROOT)} for {url}")
        else:
            errors.append(f"{rel}: unsupported pdf.url for local validation: {url!r}")

    extra_generated_entries = sorted(set(post_pdf_map) - generated_permalinks)
    for permalink in extra_generated_entries:
        errors.append(f"{POST_PDF_DATA.relative_to(ROOT)} has an entry for a post without generated pdf enabled: {permalink}")

    print(f"Post PDFs checked: {checked} posts")
    print(f"Generated PDFs: {generated_found}/{generated_expected} found")
    print(f"Local static PDFs: {local_static_found}/{local_static_expected} found")
    print(f"Remote PDF URLs: {remote_static} noted")

    if warnings:
        for warning in warnings:
            print(f"warning: {warning}")

    if errors:
        for error in errors:
            print(f"error: {error}")
        raise SystemExit(1)

    print("Post PDF checks passed.")


if __name__ == "__main__":
    main()
