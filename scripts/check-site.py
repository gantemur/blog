#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []


def require(condition, message):
    if not condition:
        errors.append(message)


gitignore = ROOT.joinpath(".gitignore").read_text(encoding="utf-8")
for required in ["source/", "_import/", "_tmp/", "_site/", "node_modules/", "_private/", ".DS_Store"]:
    require(required in gitignore.splitlines(), f".gitignore is missing {required}")

require('pathPrefix: "/blog/"' in ROOT.joinpath(".eleventy.js").read_text(encoding="utf-8"), "Eleventy pathPrefix is not /blog/.")

site_data = json.loads(ROOT.joinpath("src/_data/site.json").read_text(encoding="utf-8"))
comments = site_data.get("comments", {})
require(comments.get("provider") == "giscus", "Site comments provider is not giscus.")
require(comments.get("enabled") is False, "Giscus comments should stay disabled by default.")

report_path = ROOT / "_import" / "wordpress-import-report.json"
if report_path.exists():
    report = json.loads(report_path.read_text(encoding="utf-8"))
    require(report.get("imported", {}).get("post", 0) > 0, "No imported posts found in importer report.")
    require(report.get("media_copied", 0) == report.get("media_files", -1), "Not all media files were copied.")
else:
    warnings.append("Importer report not found; run npm run import:wordpress before final checks.")

unpublished = ROOT / "_private" / "unpublished"
if unpublished.exists():
    private_posts = [path for path in unpublished.glob("*.md") if path.name != "INDEX.md"]
    require(len(private_posts) == 22, f"Expected 22 private unpublished exports, found {len(private_posts)}.")
else:
    warnings.append("_private/unpublished not found; run npm run import:wordpress to preserve unpublished WordPress content.")

comment_review = ROOT / "_import" / "comments-sanitized.jsonl"
if comment_review.exists():
    allowed_keys = {"post_id", "post_slug", "comment_id", "author", "author_url", "date", "content"}
    private_keys = re.compile(r"(email|ip|user_agent|user-agent|agent)", re.I)
    for line_number, line in enumerate(comment_review.read_text(encoding="utf-8").splitlines(), 1):
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON in sanitized review at line {line_number}.")
            continue
        extra_keys = set(record) - allowed_keys
        if extra_keys:
            errors.append(f"Unexpected comment review keys at line {line_number}: {sorted(extra_keys)}")
        for key in record:
            if private_keys.search(key):
                errors.append(f"Private comment metadata key detected in sanitized review at line {line_number}: {key}")

site = ROOT / "_site"
if site.exists():
    forbidden = [site / "source", site / "_import", site / "_tmp", site / "_private"]
    for path in forbidden:
        require(not path.exists(), f"Private directory appeared in build output: {path.relative_to(ROOT)}")
    html_files = list(site.rglob("*.html"))
    require(html_files, "No HTML files found in _site.")
    bad_links = []
    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for attr, url in re.findall(r'(href|src)="(/(?!blog/|/|#)[^"]*)"', text):
            bad_links.append(f"{path.relative_to(ROOT)}: {attr}={url}")
    if bad_links:
        errors.append("Found root-relative links without /blog/ prefix:\n" + "\n".join(bad_links[:20]))
else:
    warnings.append("_site not found; run npm run build to verify generated links.")

draft_count = 0
for path in ROOT.joinpath("src/posts").glob("*.md"):
    text = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"(?m)^draft:\s*true\s*$", text):
        draft_count += 1

print(f"Draft posts in public source: {draft_count}")

if warnings:
    for warning in warnings:
        print(f"warning: {warning}")

if errors:
    for error in errors:
        print(f"error: {error}")
    raise SystemExit(1)

print("Migration checks passed.")
