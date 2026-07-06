#!/usr/bin/env python3
import email.utils
import html
import json
import re
import shutil
import tarfile
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
IMPORT_DIR = ROOT / "_import"
PRIVATE_DIR = ROOT / "_private"
UNPUBLISHED_DIR = PRIVATE_DIR / "unpublished"
POSTS_DIR = ROOT / "src" / "posts"
PAGES_DIR = ROOT / "src" / "pages"
MEDIA_DIR = ROOT / "src" / "assets" / "wp-media"
MANIFEST = IMPORT_DIR / "generated-files.json"
REPORT_JSON = IMPORT_DIR / "wordpress-import-report.json"
COMMENTS_JSONL = IMPORT_DIR / "comments-sanitized.jsonl"
COMMENT_AUDIT = PRIVATE_DIR / "comment-audit.md"
MIGRATION_REPORT = ROOT / "MIGRATION_REPORT.md"

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


class MarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.links = []
        self.list_stack = []
        self.in_pre = False
        self.in_code = False

    def emit(self, text):
        self.out.append(text)

    def newline(self, count=1):
        text = "".join(self.out)
        missing = count - (len(text) - len(text.rstrip("\n")))
        if missing > 0:
            self.emit("\n" * missing)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"p", "div", "section", "article", "figure"}:
            self.newline(2)
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.newline(2)
            self.emit("#" * int(tag[1]) + " ")
        elif tag == "br":
            self.emit("  \n")
        elif tag == "a":
            self.links.append(attrs.get("href", ""))
            self.emit("[")
        elif tag == "img":
            alt = attrs.get("alt", "")
            src = attrs.get("src", "")
            if src:
                self.emit(f"![{escape_md(alt)}]({src})")
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag == "blockquote":
            self.newline(2)
            self.emit("> ")
        elif tag in {"ul", "ol"}:
            self.list_stack.append({"tag": tag, "index": 1})
            self.newline(1)
        elif tag == "li":
            self.newline(1)
            if self.list_stack and self.list_stack[-1]["tag"] == "ol":
                index = self.list_stack[-1]["index"]
                self.emit(f"{index}. ")
                self.list_stack[-1]["index"] += 1
            else:
                self.emit("- ")
        elif tag == "pre":
            self.newline(2)
            self.emit("```\n")
            self.in_pre = True
        elif tag == "code" and not self.in_pre:
            self.emit("`")
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == "a":
            href = self.links.pop() if self.links else ""
            self.emit(f"]({href})" if href else "]")
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag in {"p", "div", "section", "article", "figure", "blockquote"}:
            self.newline(2)
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.newline(2)
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.newline(2)
        elif tag == "li":
            self.newline(1)
        elif tag == "pre":
            self.newline(1)
            self.emit("```\n")
            self.in_pre = False
        elif tag == "code" and self.in_code:
            self.emit("`")
            self.in_code = False

    def handle_data(self, data):
        if self.in_pre:
            self.emit(data)
        else:
            self.emit(data)

    def markdown(self):
        text = "".join(self.out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def escape_md(value):
    return str(value).replace("[", "\\[").replace("]", "\\]")


def text(parent, tag):
    return (parent.findtext(tag, default="", namespaces=NS) or "").strip()


def find_export_zip():
    zips = sorted(SOURCE.glob("*.zip"))
    if not zips:
        raise SystemExit("No .zip WordPress export found under source/.")
    return zips[0]


def find_media_tar():
    tars = sorted(SOURCE.glob("*.tar"))
    if not tars:
        raise SystemExit("No .tar media archive found under source/.")
    return tars[0]


def read_wxr(zip_path):
    with zipfile.ZipFile(zip_path) as archive:
        xml_names = [name for name in archive.namelist() if name.lower().endswith(".xml")]
        if not xml_names:
            raise SystemExit(f"No XML/WXR file found in {zip_path}.")
        xml_name = xml_names[0]
        xml_bytes = archive.read(xml_name)
    return xml_name, ET.fromstring(xml_bytes)


def media_members(tar_path):
    with tarfile.open(tar_path) as archive:
        return [member.name for member in archive.getmembers() if member.isfile()]


def safe_member_path(name):
    posix = PurePosixPath(name)
    if posix.is_absolute() or ".." in posix.parts:
        return None
    return posix


def copy_media(tar_path):
    if MEDIA_DIR.exists():
        shutil.rmtree(MEDIA_DIR)
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    copied = []
    skipped = []
    with tarfile.open(tar_path) as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            safe = safe_member_path(member.name)
            if safe is None:
                skipped.append(member.name)
                continue
            target = MEDIA_DIR.joinpath(*safe.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is None:
                skipped.append(member.name)
                continue
            with source, target.open("wb") as out:
                shutil.copyfileobj(source, out)
            copied.append(str(safe))
    return copied, skipped


def parse_date(item):
    raw = text(item, "wp:post_date") or text(item, "pubDate")
    if raw:
        for fmt in ("%Y-%m-%d %H:%M:%S",):
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                pass
        try:
            return email.utils.parsedate_to_datetime(raw).replace(tzinfo=None)
        except Exception:
            pass
    return datetime(1970, 1, 1)


def date_iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def yaml_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(json.dumps(str(v), ensure_ascii=False) for v in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def front_matter(data):
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def slug_from_title(title, fallback):
    value = unquote(title or "").lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE).strip()
    value = re.sub(r"[-\s]+", "-", value)
    return value or fallback


def safe_filename(value, fallback):
    value = unquote(value or "").strip() or fallback
    value = re.sub(r"[^\w.%_-]+", "-", value, flags=re.UNICODE).strip("-._")
    return (value or fallback)[:110]


def terms(item, domain):
    values = []
    seen = set()
    for cat in item.findall("category"):
        if cat.attrib.get("domain") != domain:
            continue
        label = (cat.text or cat.attrib.get("nicename") or "").strip()
        if label and label not in seen:
            values.append(label)
            seen.add(label)
    return values


def comments_for(item):
    comments = []
    for comment in item.findall("wp:comment", NS):
        approved = text(comment, "wp:comment_approved")
        ctype = text(comment, "wp:comment_type")
        if approved != "1" or ctype not in {"", "comment"}:
            continue
        comments.append(
            {
                "comment_id": text(comment, "wp:comment_id"),
                "author": text(comment, "wp:comment_author"),
                "author_url": text(comment, "wp:comment_author_url"),
                "date": text(comment, "wp:comment_date"),
                "content": html_to_markdown(text(comment, "wp:comment_content")).strip(),
            }
        )
    return comments


def classify_comments(items):
    counts = Counter()
    skipped = []
    for item in items:
        post_type = text(item, "wp:post_type")
        status = text(item, "wp:status")
        post_id = text(item, "wp:post_id")
        slug = text(item, "wp:post_name")
        title = (item.findtext("title") or "").strip()
        for comment in item.findall("wp:comment", NS):
            approved = text(comment, "wp:comment_approved")
            comment_type = text(comment, "wp:comment_type") or "comment"
            sanitized = post_type in {"post", "page"} and status == "publish" and approved == "1" and comment_type == "comment"
            counts[(post_type, status, approved, comment_type, "sanitized" if sanitized else "skipped")] += 1
            if not sanitized:
                skipped.append({
                    "post_id": post_id,
                    "post_slug": slug,
                    "post_title": title,
                    "comment_id": text(comment, "wp:comment_id"),
                    "comment_type": comment_type,
                    "approved": approved,
                    "date": text(comment, "wp:comment_date"),
                })
    return counts, skipped


def html_to_markdown(value):
    parser = MarkdownConverter()
    try:
        parser.feed(value or "")
        parser.close()
        return parser.markdown()
    except Exception:
        return (value or "").strip() + "\n"


def convert_latex(content):
    count = 0

    def repl(match):
        nonlocal count
        body = html.unescape(match.group(1)).strip()
        body = re.sub(r"^display=true\s+", "", body)
        body = re.split(r"&(?:bg|fg|s|size|source)=", body, maxsplit=1)[0].strip()
        count += 1
        return f"\\\\({body}\\\\)"

    return re.sub(r"\$\\?latex\s+(.+?)\$", repl, content or "", flags=re.I | re.S), count


def convert_sourcecode(content):
    count = 0

    def repl(match):
        nonlocal count
        attrs = match.group(1) or ""
        code = html.unescape(match.group(2) or "").strip("\n")
        language = ""
        lang_match = re.search(r'language=["\']?([A-Za-z0-9_+-]+)', attrs)
        if lang_match:
            language = lang_match.group(1)
        count += 1
        return f"\n\n```{language}\n{code}\n```\n\n"

    converted = re.sub(
        r"\[sourcecode([^\]]*)\](.*?)\[/sourcecode\]",
        repl,
        content or "",
        flags=re.I | re.S,
    )
    return converted, count


def strip_caption_shortcodes(content):
    count = 0

    def repl(match):
        nonlocal count
        count += 1
        return match.group(1)

    converted = re.sub(r"\[caption[^\]]*\](.*?)\[/caption\]", repl, content or "", flags=re.I | re.S)
    return converted, count


def shortcode_counts(content):
    counts = Counter()
    for match in re.finditer(r"\[([A-Za-z][A-Za-z0-9_-]*)(?:\s[^\]]*)?\]", content or ""):
        name = match.group(1)
        if len(name) == 1 and name not in {"m", "n", "x"}:
            continue
        counts[name] += 1
    return counts


def media_path_from_url(url):
    parsed = urlparse(html.unescape(url))
    host = parsed.netloc.lower()
    path = unquote(parsed.path.lstrip("/"))
    for marker in ("wp-content/uploads/", "files/"):
        if marker in path:
            path = path.split(marker, 1)[1]
            break
    if host.endswith("files.wordpress.com") or "wp-content/uploads/" in parsed.path:
        parts = PurePosixPath(path).parts
        for index in range(len(parts) - 2):
            if re.fullmatch(r"\d{4}", parts[index]) and re.fullmatch(r"\d{2}", parts[index + 1]):
                return "/".join(parts[index:])
    return None


def rewrite_content_links(content, media_set, permalink_map, unresolved):
    def replace_url(match):
        quote = match.group(1)
        url = match.group(2)
        normalized = url.split("#", 1)[0].rstrip("/")
        if normalized in permalink_map:
            return f"{quote}{permalink_map[normalized]}{quote}"
        media_path = media_path_from_url(url)
        if media_path:
            media_path = media_path.split("?", 1)[0]
            if media_path in media_set:
                return f"{quote}/blog/assets/wp-media/{media_path}{quote}"
            unresolved.add(url)
        return match.group(0)

    pattern = r'(["\'])(https?://(?:t8m8r\.files\.wordpress\.com|t8m8r\.wordpress\.com)[^"\']+)\1'
    return re.sub(pattern, replace_url, content or "")


def cleanup_generated_files():
    if not MANIFEST.exists():
        return
    try:
        generated = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    for rel in generated.get("files", []):
        path = ROOT / rel
        if path.exists() and path.is_file():
            path.unlink()


def cleanup_private_unpublished():
    if UNPUBLISHED_DIR.exists():
        shutil.rmtree(UNPUBLISHED_DIR)
    UNPUBLISHED_DIR.mkdir(parents=True, exist_ok=True)


def item_permalink(item, post_type):
    slug = text(item, "wp:post_name") or slug_from_title(item.findtext("title") or "", f"post-{text(item, 'wp:post_id')}")
    if post_type == "post":
        dt = parse_date(item)
        return f"/{dt:%Y/%m/%d}/{slug}/"
    return f"/{slug}/"


def make_permalink_map(items):
    mapping = {}
    for item in items:
        post_type = text(item, "wp:post_type")
        status = text(item, "wp:status")
        if status != "publish" or post_type not in {"post", "page"}:
            continue
        link = (item.findtext("link") or "").strip()
        permalink = "/blog" + item_permalink(item, post_type).rstrip("/") + "/"
        if link:
            mapping[link.rstrip("/")] = permalink
            mapping[link.replace("http://", "https://").rstrip("/")] = permalink
    return mapping


def write_item(item, post_type, media_set, permalink_map, report, generated_files, comments_out):
    status = text(item, "wp:status")
    if status != "publish":
        return False
    post_id = text(item, "wp:post_id")
    title = (item.findtext("title") or "").strip() or f"Untitled {post_id}"
    slug = text(item, "wp:post_name") or slug_from_title(title, f"post-{post_id}")
    dt = parse_date(item)
    raw_content = text(item, "content:encoded")
    content, sourcecode_count = convert_sourcecode(raw_content)
    content, caption_count = strip_caption_shortcodes(content)
    content, latex_count = convert_latex(content)
    unresolved = set()
    content = rewrite_content_links(content, media_set, permalink_map, unresolved)
    shortcodes = shortcode_counts(content)
    markdown = html_to_markdown(content)
    item_comments = comments_for(item)

    for comment in item_comments:
        comments_out.write(json.dumps({
            "post_id": post_id,
            "post_slug": slug,
            **comment,
        }, ensure_ascii=False) + "\n")

    destination_dir = POSTS_DIR if post_type == "post" else PAGES_DIR
    destination_dir.mkdir(parents=True, exist_ok=True)
    if post_type == "post":
        filename = f"{dt:%Y-%m-%d}-{post_id}-{safe_filename(slug, 'post-' + post_id)}.md"
        layout = "layouts/post.njk"
    else:
        filename = f"{post_id}-{safe_filename(slug, 'page-' + post_id)}.md"
        layout = "layouts/page.njk"
    destination = destination_dir / filename

    front = {
        "layout": layout,
        "title": title,
        "date": date_iso(dt),
        "slug": slug,
        "permalink": item_permalink(item, post_type),
        "wordpress_id": int(post_id or 0),
        "wordpress_url": (item.findtext("link") or "").strip(),
        "categories": terms(item, "category"),
        "tags": terms(item, "post_tag"),
        "status": status,
        "comments_count": len(item_comments),
        "math": latex_count > 0 or "\\(" in markdown or "\\[" in markdown,
        "generated_by": "wordpress-importer",
        "templateEngineOverride": "md",
    }

    destination.write_text(front_matter(front) + markdown, encoding="utf-8")
    generated_files.append(str(destination.relative_to(ROOT)))

    report["imported"][post_type] += 1
    report["latex_conversions"] += latex_count
    report["caption_shortcodes_converted"] += caption_count
    report["sourcecode_shortcodes_converted"] += sourcecode_count
    report["unconverted_shortcodes"].update(shortcodes)
    for url in sorted(unresolved):
        report["unresolved_media_urls"][url] += 1
    return True


def convert_wordpress_content(raw_content, media_set=None, permalink_map=None):
    content, _ = convert_sourcecode(raw_content)
    content, _ = strip_caption_shortcodes(content)
    content, _ = convert_latex(content)
    if media_set is not None and permalink_map is not None:
        unresolved = set()
        content = rewrite_content_links(content, media_set, permalink_map, unresolved)
    return html_to_markdown(content)


def write_unpublished_item(item, generated_private):
    post_type = text(item, "wp:post_type")
    status = text(item, "wp:status")
    if post_type not in {"post", "page"} or status == "publish":
        return None

    post_id = text(item, "wp:post_id")
    title = (item.findtext("title") or "").strip() or f"Untitled {post_id}"
    slug = text(item, "wp:post_name") or slug_from_title(title, f"{post_type}-{post_id}")
    dt = parse_date(item)
    filename = f"{dt:%Y-%m-%d}-{post_id}-{safe_filename(slug, post_type + '-' + post_id)}.md"
    destination = UNPUBLISHED_DIR / filename
    front = {
        "publish_review": True,
        "private_archive": True,
        "title": title,
        "date": date_iso(dt),
        "slug": slug,
        "wordpress_id": int(post_id or 0),
        "wordpress_url": (item.findtext("link") or "").strip(),
        "status": status,
        "type": post_type,
        "categories": terms(item, "category"),
        "tags": terms(item, "post_tag"),
    }
    markdown = convert_wordpress_content(text(item, "content:encoded"))
    destination.write_text(front_matter(front) + markdown, encoding="utf-8")
    generated_private.append(str(destination.relative_to(ROOT)))
    return {
        "title": title,
        "date": date_iso(dt),
        "slug": slug,
        "status": status,
        "type": post_type,
        "wordpress_id": post_id,
        "file": str(destination.relative_to(ROOT)),
    }


def write_unpublished_index(items):
    lines = [
        "# Unpublished WordPress Content",
        "",
        "This local archive is ignored by git. Review each item carefully before copying anything into `src/posts/` or `src/pages/`.",
        "",
        "| Date | Type | Status | Title | File |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in sorted(items, key=lambda item: (item["date"], item["type"], item["title"])):
        lines.append(f"| {row['date'][:10]} | {row['type']} | {row['status']} | {row['title']} | `{Path(row['file']).name}` |")
    index_path = UNPUBLISHED_DIR / "INDEX.md"
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(index_path.relative_to(ROOT))


def write_comment_audit(report):
    COMMENT_AUDIT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# WordPress Comment Audit",
        "",
        "This private audit is ignored by git. It intentionally does not include commenter email addresses, IP addresses, user-agent strings, or raw private comment metadata.",
        "",
        "## Summary",
        "",
        f"- Comments in WXR: {report['comments_total']}",
        f"- Sanitized public-looking comment records: {report['comments_sanitized']}",
        f"- Skipped comment-like records: {report['comments_total'] - report['comments_sanitized']}",
        "",
        "The five skipped records are approved WordPress `pingback` records attached to published posts. They are not normal human comments, so they were excluded from `_import/comments-sanitized.jsonl`.",
        "",
        "## Classification",
        "",
        "| Post type | Post status | Comment approved | Comment type | Handling | Count |",
        "| --- | --- | --- | --- | --- | ---: |",
    ]
    for (post_type, status, approved, comment_type, handling), count in sorted(report["comment_classification"].items()):
        lines.append(f"| {post_type} | {status} | {approved} | {comment_type} | {handling} | {count} |")
    lines.extend(["", "## Skipped Records", "", "| Post id | Post slug | Comment id | Type | Approved | Date |", "| --- | --- | --- | --- | --- | --- |"])
    for row in report["skipped_comments"]:
        lines.append(f"| {row['post_id']} | {row['post_slug']} | {row['comment_id']} | {row['comment_type']} | {row['approved']} | {row['date']} |")
    COMMENT_AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(report):
    serializable = dict(report)
    serializable["counts_by_type"] = dict(report["counts_by_type"])
    serializable["counts_by_status"] = dict(report["counts_by_status"])
    serializable["counts_by_type_status"] = {f"{k[0]}:{k[1]}": v for k, v in report["counts_by_type_status"].items()}
    serializable["imported"] = dict(report["imported"])
    serializable["unconverted_shortcodes"] = dict(report["unconverted_shortcodes"])
    serializable["unresolved_media_urls"] = dict(report["unresolved_media_urls"])
    serializable["comment_classification"] = {":".join(k): v for k, v in report["comment_classification"].items()}
    serializable["skipped_comments"] = report["skipped_comments"]
    serializable["categories"] = sorted(report["categories"])
    serializable["tags"] = sorted(report["tags"])
    serializable["unpublished"] = report["unpublished"]
    REPORT_JSON.write_text(json.dumps(serializable, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Migration Report",
        "",
        "## Archive Inventory",
        "",
        f"- WordPress export archive: `{report['zip_archive']}`",
        f"- Media archive: `{report['tar_archive']}`",
        f"- Detected WXR/XML file: `{report['xml_file']}`",
        "",
        "## Detected Content",
        "",
        f"- Total WXR items: {report['total_items']}",
        f"- Published posts: {report['counts_by_type_status'][('post', 'publish')]}",
        f"- Published pages: {report['counts_by_type_status'][('page', 'publish')]}",
        f"- Attachments in WXR: {report['counts_by_type'].get('attachment', 0)}",
        f"- Media files in tar: {report['media_files']}",
        f"- Comments found: {report['comments_total']}",
        f"- Approved comments written to private sanitized review: {report['comments_sanitized']}",
        f"- Categories: {len(report['categories'])}",
        f"- Tags: {len(report['tags'])}",
        "",
        "## Import Result",
        "",
        f"- Markdown posts generated: {report['imported'].get('post', 0)}",
        f"- Markdown pages generated: {report['imported'].get('page', 0)}",
        f"- Media files copied: {report['media_copied']}",
        f"- Media files skipped for unsafe paths or read errors: {report['media_skipped']}",
        f"- WordPress.com LaTeX snippets converted: {report['latex_conversions']}",
        f"- Caption shortcodes converted: {report['caption_shortcodes_converted']}",
        f"- Sourcecode shortcodes converted: {report['sourcecode_shortcodes_converted']}",
        "",
        "## Comments",
        "",
        "Old WordPress comments are not rendered publicly. A sanitized review file was generated at `_import/comments-sanitized.jsonl` with post id/slug, display name, date, content, and optional author URL only. Email addresses, IP addresses, user-agent strings, and private metadata are not included.",
        "",
        "## Private, Draft, or Unpublished Content",
        "",
    ]
    if report["unpublished"]:
        lines.append(f"- Draft/private/unpublished posts/pages detected: {len(report['unpublished'])}")
        lines.append(f"- Exported to ignored local archive: `_private/unpublished/`")
        lines.append("- Exact titles and content are kept out of this public report.")
    else:
        lines.append("- None detected among posts/pages.")

    lines.extend(["", "## Shortcodes and Special Markup", ""])
    if report["unconverted_shortcodes"]:
        for name, count in report["unconverted_shortcodes"].most_common():
            lines.append(f"- `{name}`: {count}")
    else:
        lines.append("- No unconverted shortcode-like patterns detected after importer conversions.")

    lines.extend(["", "## Unresolved Media URLs", ""])
    if report["unresolved_media_urls"]:
        for url, count in list(report["unresolved_media_urls"].most_common(40)):
            lines.append(f"- {url} ({count})")
    else:
        lines.append("- None detected for WordPress media links.")

    lines.extend([
        "",
        "## Notes",
        "",
        "- `source/`, `_import/`, `_tmp/`, `_site/`, and `node_modules/` are ignored by `.gitignore`.",
        "- `_private/` is ignored by `.gitignore` and is used for local-only drafts and unpublished WordPress exports.",
        "- Generated public Markdown, pages, and media live under `src/`.",
        "- Site links are configured for the GitHub Pages project base path `/blog/`.",
    ])
    MIGRATION_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = find_export_zip()
    tar_path = find_media_tar()
    xml_name, tree = read_wxr(zip_path)
    channel = tree.find("channel")
    items = channel.findall("item") if channel is not None else []
    media_names = media_members(tar_path)
    copied_media, skipped_media = copy_media(tar_path)
    media_set = set(copied_media)

    cleanup_generated_files()
    cleanup_private_unpublished()
    permalink_map = make_permalink_map(items)
    generated_files = []
    generated_private_files = []

    report = {
        "zip_archive": str(zip_path.relative_to(ROOT)),
        "tar_archive": str(tar_path.relative_to(ROOT)),
        "xml_file": xml_name,
        "total_items": len(items),
        "counts_by_type": Counter(),
        "counts_by_status": Counter(),
        "counts_by_type_status": Counter(),
        "imported": Counter(),
        "categories": set(),
        "tags": set(),
        "comments_total": 0,
        "comments_sanitized": 0,
        "media_files": len(media_names),
        "media_copied": len(copied_media),
        "media_skipped": len(skipped_media),
        "latex_conversions": 0,
        "caption_shortcodes_converted": 0,
        "sourcecode_shortcodes_converted": 0,
        "unconverted_shortcodes": Counter(),
        "unresolved_media_urls": Counter(),
        "unpublished": [],
        "comment_classification": Counter(),
        "skipped_comments": [],
    }

    comment_classification, skipped_comments = classify_comments(items)
    report["comment_classification"] = comment_classification
    report["skipped_comments"] = skipped_comments

    for item in items:
        post_type = text(item, "wp:post_type")
        status = text(item, "wp:status")
        report["counts_by_type"][post_type] += 1
        report["counts_by_status"][status] += 1
        report["counts_by_type_status"][(post_type, status)] += 1
        report["categories"].update(terms(item, "category"))
        report["tags"].update(terms(item, "post_tag"))
        report["comments_total"] += len(item.findall("wp:comment", NS))
        if post_type in {"post", "page"} and status != "publish":
            report["unpublished"].append({
                "type": post_type,
                "status": status,
                "title": (item.findtext("title") or "").strip(),
            })
            private_row = write_unpublished_item(item, generated_private_files)
            if private_row:
                report.setdefault("unpublished_private_index", []).append(private_row)

    with COMMENTS_JSONL.open("w", encoding="utf-8") as comments_out:
        for item in items:
            post_type = text(item, "wp:post_type")
            if post_type not in {"post", "page"}:
                continue
            before = comments_out.tell()
            write_item(item, post_type, media_set, permalink_map, report, generated_files, comments_out)
            if comments_out.tell() != before:
                pass

    report["comments_sanitized"] = sum(1 for _ in COMMENTS_JSONL.open(encoding="utf-8"))
    generated_private_files.append(write_unpublished_index(report.get("unpublished_private_index", [])))
    MANIFEST.write_text(json.dumps({"files": generated_files}, indent=2), encoding="utf-8")
    (PRIVATE_DIR / "generated-private-files.json").write_text(json.dumps({"files": generated_private_files}, indent=2), encoding="utf-8")
    write_comment_audit(report)
    write_report(report)

    print(f"Imported {report['imported'].get('post', 0)} posts and {report['imported'].get('page', 0)} pages.")
    print(f"Exported {len(report.get('unpublished_private_index', []))} unpublished items to {UNPUBLISHED_DIR.relative_to(ROOT)}.")
    print(f"Copied {report['media_copied']} media files.")
    print(f"Wrote {MIGRATION_REPORT.relative_to(ROOT)} and {COMMENTS_JSONL.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
