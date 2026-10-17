#!/usr/bin/env python3
"""Ordinary checks/builds validate committed PDFs; rendering is always explicit."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    print("Validating committed PDFs; use export:post-pdfs -- --post PATH to render.", flush=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/check-post-pdfs.py")], cwd=ROOT, check=True)
