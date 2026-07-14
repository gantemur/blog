#!/usr/bin/env python3
"""Generate post PDFs locally, but validate only in CI or when skipped."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script):
    subprocess.run([sys.executable, str(ROOT / "scripts" / script)], cwd=ROOT, check=True)


def main():
    if os.environ.get("CI", "").lower() == "true":
        print("CI=true: skipping Pandoc post PDF generation; validating committed PDFs only.", flush=True)
        run("check-post-pdfs.py")
        return

    if os.environ.get("BLOG_SKIP_PDF") == "1":
        print("BLOG_SKIP_PDF=1: skipping post PDF generation; validating existing PDFs only.", flush=True)
        run("check-post-pdfs.py")
        return

    run("export-post-pdfs.py")
    run("check-post-pdfs.py")


if __name__ == "__main__":
    main()
