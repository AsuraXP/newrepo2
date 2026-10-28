#!/usr/bin/env python3
"""
Frame prep for the repo: compress generated frames to 1280x720 JPG and build a
contact sheet for the style-consistency pass.

Run after frames are generated and visually verified in the workspace.

    python tools/prep_frames.py --repo .            # compress + report
    python tools/prep_frames.py --repo . --sheet    # also build QC contact sheet
    python tools/prep_frames.py --repo . --strict   # fail if any frame is missing

Source images are read from --src (default: the frame files' own directory) and
written back under assets/frames/ with the exact names referenced by frames.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install -q pillow")


def load_frames(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as fh:
        frames = json.load(fh)
    if isinstance(frames, dict):
        frames = frames.get("frames", [])
    return frames


def fit_720(img: Image.Image, width: int, height: int) -> Image.Image:
    """Cover-fit: preserve aspect, crop centre, no letterbox bars."""
    src_ratio = img.width / img.height
    dst_ratio = width / height
    if src_ratio > dst_ratio:
        new_h = height
        new_w = round(height * src_ratio)
    else:
        new_w = width
        new_h = round(width / src_ratio)
    img = img.convert("RGB").resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - width) // 2
    top = (new_h - height) // 2
    return img.crop((left, top, left + width, top + height))


def contact_sheet(images: list[tuple[str, Image.Image]], out: Path,
                  cols: int = 4, cell: int = 320) -> None:
    rows = (len(images) + cols - 1) // cols
    pad = 8
    label_h = 18
    W = cols * cell + (cols + 1) * pad
    H = rows * (cell + label_h) + (rows + 1) * pad
    sheet = Image.new("RGB", (W, H), (18, 18, 20))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(sheet)
    for i, (name, img) in enumerate(images):
        r, c = divmod(i, cols)
        x = pad + c * (cell + pad)
        y = pad + r * (cell + label_h + pad)
        sheet.paste(img.resize((cell, cell), Image.LANCZOS), (x, y))
        draw.text((x + 2, y + cell + 3), f"{i + 1:02d} {name}", fill=(210, 210, 210))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "JPEG", quality=88, optimize=True)
    print(f"  contact sheet -> {out}  ({W}x{H})")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--config", default=None)
    ap.add_argument("--src", default=None, help="dir with source images")
    ap.add_argument("--outdir", default=None, help="default assets/frames")
    ap.add_argument("--quality", type=int, default=86)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--sheet", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    import yaml
    cfg_path = Path(args.config) if args.config else repo / "kaggle" / "config.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    paths = cfg.get("paths", {})
    frames_path = repo / paths.get("frames", "narration/frames.json")
    outdir = Path(args.outdir) if args.outdir else repo / paths.get("frames_dir",
                                                                   "assets/frames")
    outdir.mkdir(parents=True, exist_ok=True)

    frames = load_frames(frames_path)
    print(f"  {len(frames)} frames in {frames_path.name}")

    sheet_items: list[tuple[str, Image.Image]] = []
    missing, total_before, total_after = [], 0, 0
    for fr in frames:
        name = Path(fr.get("image") or f"{fr['id']}.jpg").name
        stem = Path(name).stem
        out = outdir / (stem + ".jpg")
        candidates = []
        if args.src:
            src_dir = Path(args.src)
            candidates += [src_dir / name, src_dir / (stem + ".png"),
                           src_dir / (stem + ".jpg")]
        candidates += [outdir / (stem + ".png"), outdir / name]
        src = next((c for c in candidates if c.is_file()), None)
        if src is None:
            missing.append(fr["id"])
            continue
        total_before += src.stat().st_size
        with Image.open(src) as img:
            processed = fit_720(img, args.width, args.height)
        processed.save(out, "JPEG", quality=args.quality, optimize=True,
                       progressive=True)
        total_after += out.stat().st_size
        sheet_items.append((fr["id"], processed))
        # drop the oversized png source so it never lands in git
        if src.suffix.lower() == ".png" and src.parent == outdir:
            src.unlink()

    print(f"  prepared {len(sheet_items)}/{len(frames)} frames "
          f"-> {outdir}")
    if total_before:
        print(f"  size: {total_before / 1e6:.1f} MB -> {total_after / 1e6:.1f} MB")
    if missing:
        print(f"  ! missing frames: {', '.join(missing)}")
        if args.strict:
            return 1
    if args.sheet and sheet_items:
        contact_sheet(sheet_items, repo / "output" / "contact_sheet.jpg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
