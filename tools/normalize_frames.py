#!/usr/bin/env python3
"""Normalise frames to a single 1280x720 canvas before the Kaggle pad step.

Centre-crops each frame to 16:9, resizes to 1280x720, rewrites as JPEG q90.
Run it in the worker chat right before committing a batch, so the Kaggle canvas
pad never has to reconcile mixed aspect ratios.

    python tools/normalize_frames.py --dir broken_leg_video/frames
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

TARGET = (1280, 720)


def normalise(path: Path) -> tuple[int, int, int, int]:
    im = Image.open(path).convert("RGB")
    w, h = im.size
    want = TARGET[0] / TARGET[1]
    have = w / h
    if have > want:                      # too wide -> crop sides
        new_w = int(round(h * want))
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    elif have < want:                    # too tall -> crop top/bottom
        new_h = int(round(w / want))
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    im = im.resize(TARGET, Image.LANCZOS)
    im.save(path, quality=90, optimize=True)
    return (w, h, *im.size)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="broken_leg_video/frames")
    ap.add_argument("--glob", default="*.jpg")
    a = ap.parse_args()
    root = Path(a.dir)
    files = sorted(root.glob(a.glob))
    if not files:
        print(f"no files in {root}")
        return 1
    for f in files:
        before = f.stat().st_size
        ow, oh, nw, nh = normalise(f)
        print(f"{f.name:18s} {ow}x{oh} -> {nw}x{nh}  {before/1024:.0f}kB -> {f.stat().st_size/1024:.0f}kB")
    print(f"normalised {len(files)} frame(s) to {TARGET[0]}x{TARGET[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
