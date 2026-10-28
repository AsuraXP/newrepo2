#!/usr/bin/env python3
"""Validate, compress, and contact-sheet episode frames."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps, ImageDraw
except ImportError:
    print("Pillow is required: python -m pip install pillow", file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--sheet", action="store_true", help="build a labeled contact sheet")
    parser.add_argument("--strict", action="store_true", help="fail if any expected frame is absent or invalid")
    args = parser.parse_args()
    repo = args.repo.resolve()
    entries = json.loads((repo / "frames.json").read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        print("ERROR: frames.json must contain at least one frame", file=sys.stderr)
        return 1
    output = repo / "assets" / "frames"
    sources = repo / "assets" / "source_frames"
    output.mkdir(parents=True, exist_ok=True)
    missing: list[str] = []
    images: list[tuple[str, Image.Image]] = []
    for entry in entries:
        fid = str(entry.get("id", ""))
        if not fid or Path(fid).name != fid:
            missing.append(f"invalid frame id: {fid!r}")
            continue
        jpg = output / f"{fid}.jpg"
        candidates = [sources / f"{fid}.png", sources / f"{fid}.jpg", output / f"{fid}.png", jpg]
        source = next((p for p in candidates if p.is_file()), None)
        if source is None:
            missing.append(f"{fid}: no source image in assets/source_frames/ or assets/frames/")
            continue
        try:
            with Image.open(source) as original:
                converted = ImageOps.fit(original.convert("RGB"), (1280, 720), method=Image.Resampling.LANCZOS)
                converted.save(jpg, "JPEG", quality=88, optimize=True, progressive=True)
            with Image.open(jpg) as ready:
                if ready.size != (1280, 720) or ready.format != "JPEG":
                    missing.append(f"{fid}: compressed output failed 1280x720 JPG validation")
                    continue
                images.append((fid, ready.copy()))
            print(f"OK {fid}: {jpg.stat().st_size / 1024:.1f} KB")
        except Exception as exc:
            missing.append(f"{fid}: could not process {source}: {exc}")
    if args.sheet and images:
        thumb_w, thumb_h, label_h, cols = 320, 180, 32, 3
        rows = (len(images) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "#eeeeee")
        draw = ImageDraw.Draw(sheet)
        for i, (fid, image) in enumerate(images):
            x, y = (i % cols) * thumb_w, (i // cols) * (thumb_h + label_h)
            sheet.paste(image.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS), (x, y))
            draw.text((x + 6, y + thumb_h + 7), fid, fill="#111111")
        target = repo / "assets" / "contact_sheet.jpg"
        sheet.save(target, "JPEG", quality=90, optimize=True)
        print(f"Contact sheet: {target.relative_to(repo)}")
    if missing:
        for message in missing:
            print(f"MISSING/INVALID {message}", file=sys.stderr)
        return 1 if args.strict else 0
    if len(images) != len(entries):
        print(f"ERROR: prepared {len(images)} frames, expected {len(entries)}", file=sys.stderr)
        return 1
    total = sum((output / f"{entry['id']}.jpg").stat().st_size for entry in entries)
    print(f"Prepared {len(entries)} / {len(entries)} frames; total {total / (1024 * 1024):.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
