#!/usr/bin/env python3
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
POSTS = SRC / "posts"
PAGES = SRC / "pages"
ALIASES = SRC / "aliases"
REPORT = ROOT / "URL_AUDIT.md"


def split_front_matter(text):
    if not text.startswith("---\n"):
        return {}, "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, "", text
    raw = text[4:end]
    front = text[: end + 5]
    body = text[end + 5 :]
    data = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = ""
        else:
            try:
                data[key] = json.loads(value)
            except json.JSONDecodeError:
                data[key] = value.strip('"')
    return data, front, body


def front_matter_and_body(path):
    text = path.read_text(encoding="utf-8")
    data, front, body = split_front_matter(text)
    return text, data, front, body


def ensure_trailing(path):
    if not path:
        return "/"
    return path if path.endswith("/") else path + "/"


def old_path(url):
    parsed = urlparse(url)
    if parsed.netloc.lower() != "t8m8r.wordpress.com":
        return ""
    return ensure_trailing(parsed.path)


def alias_filename(path):
    name = unquote(path.strip("/")).replace("/", "__") or "home"
    name = re.sub(r"[^\w.-]+", "-", name, flags=re.UNICODE).strip("-")
    return name[:140] + ".njk"


def collect_entries():
    entries = []
    for path in sorted(list(POSTS.glob("*.md")) + list(PAGES.glob("*.md"))):
        _, data, _, _ = front_matter_and_body(path)
        permalink = ensure_trailing(str(data.get("permalink", "")))
        wordpress_url = str(data.get("wordpress_url", ""))
        if not permalink or not wordpress_url:
            continue
        entries.append({
            "file": path,
            "title": str(data.get("title", "")),
            "permalink": permalink,
            "wordpress_url": wordpress_url,
            "old_path": old_path(wordpress_url),
        })
    return entries


def build_mapping(entries):
    mapping = {}
    for entry in entries:
        if entry["old_path"]:
            mapping[entry["old_path"]] = entry["permalink"]
        slug = entry["permalink"].strip("/")
        if entry["file"].parent == PAGES:
            mapping[f"/contents/{slug}/"] = entry["permalink"]
            mapping[f"/{slug}/"] = entry["permalink"]
    return mapping


def rewrite_wordpress_links(mapping):
    url_pattern = re.compile(r"https?://t8m8r\.wordpress\.com(/[^\s)\"'<]+)")
    changed = 0
    unresolved = {}

    for path in sorted(list(POSTS.glob("*.md")) + list(PAGES.glob("*.md"))):
        text = path.read_text(encoding="utf-8")
        _, front, body = split_front_matter(text)

        def repl(match):
            raw_path = ensure_trailing(match.group(1).split("#", 1)[0])
            suffix = ""
            if "#" in match.group(1):
                suffix = "#" + match.group(1).split("#", 1)[1]
            if raw_path.startswith("/wp-content/uploads/"):
                unresolved[match.group(0)] = unresolved.get(match.group(0), 0) + 1
                return match.group(0)
            target = mapping.get(raw_path)
            if not target:
                unresolved[match.group(0)] = unresolved.get(match.group(0), 0) + 1
                return match.group(0)
            return "/blog" + target.rstrip("/") + "/" + suffix

        updated_body = url_pattern.sub(repl, body)
        updated = front + updated_body
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed, unresolved


def write_aliases(entries):
    if ALIASES.exists():
        shutil.rmtree(ALIASES)
    ALIASES.mkdir(parents=True, exist_ok=True)
    current = {entry["permalink"] for entry in entries}
    aliases = []
    for entry in entries:
        old = entry["old_path"]
        new = entry["permalink"]
        if not old or old == new or old in current:
            continue
        aliases.append({**entry, "alias_path": old})
        target = new
        content = f"""---
permalink: "{old}"
eleventyExcludeFromCollections: true
target: "{target}"
---
<!doctype html>
<html lang="{{{{ site.language }}}}">
  <head>
    <meta charset="utf-8">
    <title>Redirecting to {{{{ title or site.title }}}}</title>
    <link rel="canonical" href="{{{{ site.url }}}}{{{{ target | url }}}}">
    <meta http-equiv="refresh" content="0; url={{{{ target | url }}}}">
  </head>
  <body>
    <p>Redirecting to <a href="{{{{ target | url }}}}">{{{{ target | url }}}}</a>.</p>
  </body>
</html>
"""
        (ALIASES / alias_filename(old)).write_text(content, encoding="utf-8")
    return aliases


def write_report(entries, aliases, unresolved, rewritten_count):
    texas = [entry for entry in entries if "Техас" in entry["title"] or "Texas" in entry["title"] or "техас" in entry["file"].name.lower()]
    mismatches = [entry for entry in entries if entry["old_path"] and entry["old_path"] != entry["permalink"]]
    lines = [
        "# URL Audit",
        "",
        "This report compares migrated WordPress URLs with generated Eleventy permalinks.",
        "",
        "## Summary",
        "",
        f"- Posts/pages with WordPress URLs: {len(entries)}",
        f"- Old path/new permalink mismatches: {len(mismatches)}",
        f"- Alias pages generated: {len(aliases)}",
        f"- Source files with WordPress links rewritten: {rewritten_count}",
        f"- Unresolved WordPress links left in Markdown: {sum(unresolved.values())}",
        "",
        "## Texas Name Post",
        "",
    ]
    if texas:
        for entry in texas:
            lines.extend([
                f"- Title: {entry['title']}",
                f"- Source: `{entry['file'].relative_to(ROOT)}`",
                f"- Generated URL: `/blog{entry['permalink']}`",
                f"- Original WordPress URL: {entry['wordpress_url']}",
                f"- Old path and generated path match: {'yes' if entry['old_path'] == entry['permalink'] else 'no'}",
            ])
    else:
        lines.append("- Not found.")

    lines.extend(["", "## Alias Pages", ""])
    if aliases:
        lines.append("| Old path | New path | Source |")
        lines.append("| --- | --- | --- |")
        for entry in aliases:
            lines.append(f"| `{entry['alias_path']}` | `{entry['permalink']}` | `{entry['file'].relative_to(ROOT)}` |")
    else:
        lines.append("- No aliases needed.")

    lines.extend(["", "## Unresolved WordPress Links", ""])
    if unresolved:
        for url, count in sorted(unresolved.items()):
            lines.append(f"- {url} ({count})")
    else:
        lines.append("- None.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    entries = collect_entries()
    mapping = build_mapping(entries)
    rewritten_count, unresolved = rewrite_wordpress_links(mapping)
    aliases = write_aliases(entries)
    write_report(entries, aliases, unresolved, rewritten_count)
    print(f"Rewrote WordPress links in {rewritten_count} source files.")
    print(f"Generated {len(aliases)} alias pages.")
    print(f"Wrote {REPORT.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
