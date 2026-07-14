#!/usr/bin/env python3
"""Safely optimize large still images imported from WordPress."""

import argparse
import datetime as dt
import shutil
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:  # pragma: no cover - depends on local environment
    Image = None
    ImageOps = None


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_PARTS = {"_site", "exports", "_private", "source", "_import", "node_modules"}
STILL_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
REPORT_PATH = ROOT / "IMAGE_OPTIMIZATION_REPORT.md"


def parse_size(value):
    text = str(value).strip().lower()
    units = {"k": 1024, "kb": 1024, "m": 1024 * 1024, "mb": 1024 * 1024}
    for suffix, multiplier in units.items():
        if text.endswith(suffix):
            return int(float(text[: -len(suffix)]) * multiplier)
    return int(text)


def human_size(size):
    units = ["B", "K", "M", "G"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f}{unit}" if unit != "B" else f"{int(value)}B"
        value /= 1024
    return f"{value:.1f}G"


def safe_relative(path):
    resolved = path.resolve()
    try:
        rel = resolved.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit(f"Refusing path outside repo: {path}") from error
    if any(part in PROTECTED_PARTS for part in rel.parts):
        raise SystemExit(f"Refusing protected path: {rel}")
    return rel


def iter_media_files(target):
    for path in sorted(target.rglob("*")):
        if not path.is_file():
            continue
        rel = path.resolve().relative_to(ROOT)
        if any(part in PROTECTED_PARTS for part in rel.parts):
            continue
        yield path


def dimensions(path):
    with Image.open(path) as image:
        return image.size


def resize_dimensions(width, height, max_long_edge):
    long_edge = max(width, height)
    if long_edge <= max_long_edge:
        return width, height
    scale = max_long_edge / long_edge
    return max(1, round(width * scale)), max(1, round(height * scale))


def save_optimized(source, output, args):
    ext = source.suffix.lower()
    with Image.open(source) as raw:
        original_size = raw.size
        image = ImageOps.exif_transpose(raw)
        width, height = image.size
        new_size = resize_dimensions(width, height, args.max_long_edge)
        if new_size != image.size:
            image = image.resize(new_size, Image.Resampling.LANCZOS)

        save_kwargs = {}
        icc_profile = raw.info.get("icc_profile")
        if icc_profile:
            save_kwargs["icc_profile"] = icc_profile

        if ext in {".jpg", ".jpeg"}:
            if image.mode not in {"RGB", "L"}:
                image = image.convert("RGB")
            save_kwargs.update({"quality": args.jpeg_quality, "optimize": True, "progressive": True})
            image.save(output, "JPEG", **save_kwargs)
        elif ext == ".png":
            image.save(output, "PNG", optimize=True, **save_kwargs)
        elif ext == ".webp":
            image.save(output, "WEBP", quality=args.jpeg_quality, method=6, **save_kwargs)
        else:
            raise ValueError(f"Unsupported still image extension: {ext}")
    return original_size, new_size


def analyze_file(path, args):
    ext = path.suffix.lower()
    size = path.stat().st_size
    rel = path.relative_to(ROOT)

    if size < args.min_size:
        return {"kind": "small", "path": rel, "size": size}
    if ext == ".gif":
        return {"kind": "skipped-gif", "path": rel, "size": size}
    if ext in {".pdf", ".svg"}:
        return {"kind": "skipped-format", "path": rel, "size": size, "reason": ext}
    if ext not in STILL_EXTENSIONS:
        return {"kind": "skipped-format", "path": rel, "size": size, "reason": ext or "no extension"}

    with Image.open(path) as image:
        width, height = image.size
    new_width, new_height = resize_dimensions(width, height, args.max_long_edge)

    if ext == ".png" and (new_width, new_height) == (width, height):
        return {
            "kind": "skipped-png",
            "path": rel,
            "size": size,
            "before": (width, height),
            "reason": "large PNG has no resize opportunity; not converting PNG to JPEG",
        }
    if ext == ".webp" and (new_width, new_height) == (width, height):
        return {
            "kind": "skipped-webp",
            "path": rel,
            "size": size,
            "before": (width, height),
            "reason": "large WEBP has no resize opportunity",
        }

    with tempfile.TemporaryDirectory(prefix="blog-media-opt-") as tmpdir:
        tmp_output = Path(tmpdir) / path.name
        before_dims, after_dims = save_optimized(path, tmp_output, args)
        new_size = tmp_output.stat().st_size
        if new_size >= size:
            return {
                "kind": "skipped-not-smaller",
                "path": rel,
                "size": size,
                "new_size": new_size,
                "before": before_dims,
                "after": after_dims,
                "reason": "optimized file was not smaller",
            }
        if args.apply:
            backup = args.backup_dir / rel
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copy2(path, backup)
            shutil.copy2(tmp_output, path)
        return {
            "kind": "optimized",
            "path": rel,
            "size": size,
            "new_size": new_size,
            "before": before_dims,
            "after": after_dims,
        }


def format_file_list(items, include_new=False, limit=None):
    if not items:
        return "- None\n"
    lines = []
    selected = items if limit is None else items[:limit]
    for item in selected:
        if include_new:
            before = f"{item['before'][0]}x{item['before'][1]}"
            after = f"{item['after'][0]}x{item['after'][1]}"
            saved = item["size"] - item["new_size"]
            lines.append(
                f"- `{item['path']}`: {human_size(item['size'])} -> {human_size(item['new_size'])} "
                f"({before} -> {after}, saved {human_size(saved)})"
            )
        else:
            detail = f" ({item.get('reason')})" if item.get("reason") else ""
            lines.append(f"- `{item['path']}`: {human_size(item['size'])}{detail}")
    if limit is not None and len(items) > limit:
        lines.append(f"- ... {len(items) - limit} more")
    return "\n".join(lines) + "\n"


def write_report(args, results, command):
    optimized = [item for item in results if item["kind"] == "optimized"]
    skipped = [item for item in results if item["kind"].startswith("skipped")]
    skipped_gifs = [item for item in results if item["kind"] == "skipped-gif"]
    skipped_pngs = [item for item in results if item["kind"] == "skipped-png"]
    skipped_webps = [item for item in results if item["kind"] == "skipped-webp"]
    candidates = [item for item in results if item["kind"] not in {"small"}]
    original_total = sum(item["size"] for item in optimized)
    new_total = sum(item["new_size"] for item in optimized)
    savings = original_total - new_total
    mode = "apply" if args.apply else "dry-run"
    target_size = sum(path.stat().st_size for path in iter_media_files(args.target))

    text = [
        "# Image Optimization Report",
        "",
        f"- Date: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- Mode: `{mode}`",
        f"- Command: `{command}`",
        f"- Target: `{args.target.relative_to(ROOT)}`",
        f"- Backup directory: `{args.backup_dir.relative_to(ROOT)}`",
        f"- Minimum size: `{human_size(args.min_size)}`",
        f"- Max long edge: `{args.max_long_edge}`",
        f"- JPEG quality: `{args.jpeg_quality}`",
        f"- Current target size: `{human_size(target_size)}`",
        "",
        "## Summary",
        "",
        f"- Candidates considered: {len(candidates)}",
        f"- Optimized files: {len(optimized)}",
        f"- Skipped files: {len(skipped)}",
        f"- Original total size of optimized files: {human_size(original_total)}",
        f"- New total size of optimized files: {human_size(new_total)}",
        f"- Estimated/actual savings: {human_size(savings)}",
        "",
        "Normal commits reduce current and future checkout size, but they do not shrink already-pushed Git history.",
        "",
        "## Optimized Files",
        "",
        format_file_list(optimized, include_new=True),
        "## Skipped Large GIFs",
        "",
        format_file_list(skipped_gifs, limit=80),
        "## Skipped Large PNGs",
        "",
        format_file_list(skipped_pngs, limit=80),
        "## Skipped Large WEBPs",
        "",
        format_file_list(skipped_webps, limit=80),
        "## Other Skipped Large Files",
        "",
        format_file_list(
            [
                item
                for item in skipped
                if item["kind"] not in {"skipped-gif", "skipped-png", "skipped-webp"}
            ],
            limit=80,
        ),
    ]
    REPORT_PATH.write_text("\n".join(text), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default="src/assets/wp-media", type=Path)
    parser.add_argument("--backup-dir", default="_private/media-originals", type=Path)
    parser.add_argument("--min-size", default="1500K")
    parser.add_argument("--max-long-edge", default=2200, type=int)
    parser.add_argument("--jpeg-quality", default=88, type=int)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if Image is None:
        raise SystemExit("Pillow is not installed. Install Pillow or run on a machine with PIL available.")
    if not args.dry_run and not args.apply:
        args.dry_run = True

    args.target = (ROOT / args.target).resolve() if not args.target.is_absolute() else args.target.resolve()
    args.backup_dir = (ROOT / args.backup_dir).resolve() if not args.backup_dir.is_absolute() else args.backup_dir.resolve()
    args.min_size = parse_size(args.min_size)
    safe_relative(args.target)
    if not args.target.exists():
        raise SystemExit(f"Target does not exist: {args.target}")
    try:
        args.backup_dir.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit(f"Backup directory must stay inside repo: {args.backup_dir}") from error
    if "_private" not in args.backup_dir.relative_to(ROOT).parts:
        raise SystemExit(f"Backup directory must be under ignored _private/: {args.backup_dir.relative_to(ROOT)}")

    results = []
    for path in iter_media_files(args.target):
        try:
            results.append(analyze_file(path, args))
        except Exception as error:  # keep scanning and report the problem
            results.append(
                {
                    "kind": "skipped-format",
                    "path": path.relative_to(ROOT),
                    "size": path.stat().st_size,
                    "reason": f"error: {error}",
                }
            )

    command = "python3 scripts/optimize-media.py " + ("--apply" if args.apply else "--dry-run")
    write_report(args, results, command)

    optimized = [item for item in results if item["kind"] == "optimized"]
    skipped_gifs = [item for item in results if item["kind"] == "skipped-gif"]
    savings = sum(item["size"] - item["new_size"] for item in optimized)
    print(f"Mode: {'apply' if args.apply else 'dry-run'}")
    print(f"Target: {args.target.relative_to(ROOT)}")
    print(f"Optimized candidates: {len(optimized)}")
    print(f"Estimated/actual savings: {human_size(savings)}")
    print(f"Skipped large GIFs: {len(skipped_gifs)}")
    print(f"Wrote {REPORT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
