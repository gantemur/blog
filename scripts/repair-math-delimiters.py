#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "src" / "posts", ROOT / "src" / "pages"]

OPEN_INLINE = re.compile(r"(?<!\\)\\\(")
CLOSE_INLINE = re.compile(r"(?<!\\)\\\)")
OPEN_DISPLAY = re.compile(r"(?<!\\)\\\[")
CLOSE_DISPLAY = re.compile(r"(?<!\\)\\\]")


def split_front_matter(text):
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :]


def repair_body(body):
    body = OPEN_INLINE.sub(r"\\\\(", body)
    body = CLOSE_INLINE.sub(r"\\\\)", body)
    body = OPEN_DISPLAY.sub(r"\\\\[", body)
    body = CLOSE_DISPLAY.sub(r"\\\\]", body)
    return body


def main():
    changed = 0
    for root in TARGETS:
        for path in root.glob("*.md"):
            original = path.read_text(encoding="utf-8")
            front, body = split_front_matter(original)
            repaired = front + repair_body(body)
            if repaired != original:
                path.write_text(repaired, encoding="utf-8")
                changed += 1
    print(f"Repaired math delimiters in {changed} files.")


if __name__ == "__main__":
    main()
