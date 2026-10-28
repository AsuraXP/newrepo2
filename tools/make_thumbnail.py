#!/usr/bin/env python3
"""Composite the channel thumbnail: crop, then draw type over the empty plate.

Type is drawn here, not generated - image models mangle lettering, and the
thumbnail is the one asset where wording must be exact.

    python tools/make_thumbnail.py --src assets/thumb_base.png
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CREAM = (247, 243, 233)
INK = (26, 24, 22)
RUST = (193, 84, 43)
MUSTARD = (214, 160, 48)
GREY = (183, 190, 186)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fit(draw, text, font_path, max_w, start, min_size=28):
    size = start
    while size > min_size:
        f = ImageFont.truetype(font_path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f, size
        size -= 2
    return ImageFont.truetype(font_path, min_size), min_size


def crop_16_9(img: Image.Image, bias_x: float = 0.55) -> Image.Image:
    """Take the widest 16:9 window, biased toward the subject."""
    w, h = img.size
    target_h = int(w * 9 / 16)
    if target_h <= h:
        left = int((w - w) * 0)
        top = int((h - target_h) * 0.45)
        return img.crop((left, top, w, top + target_h))
    target_w = int(h * 16 / 9)
    left = int((w - target_w) * bias_x)
    return img.crop((left, 0, left + target_w, h))


def panel(draw, box, radius=26, fill=CREAM, outline=INK, width=7):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="assets/thumb_base.png")
    ap.add_argument("--out", default="assets/thumbnail.png")
    ap.add_argument("--width", type=int, default=1280)
    args = ap.parse_args()

    src = Image.open(args.src).convert("RGB")
    # the plate has a wide empty margin on the left: take a 16:9 window that
    # keeps the hero and most of the flat wall for type
    w, h = src.size
    target_h = int(w * 9 / 16)
    if target_h > h:
        target_w = int(h * 16 / 9)
        left = int((w - target_w) * 0.62)
        src = src.crop((left, 0, left + target_w, h))
    else:
        top = int((h - target_h) * 0.4)
        src = src.crop((0, top, w, top + target_h))

    W = args.width
    H = int(W * 9 / 16)
    img = src.resize((W, H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    # --- text plate, top-left, flat with an ink outline -------------------
    pad = int(W * 0.028)
    box = (pad, pad, int(W * 0.60), int(W * 0.315))
    panel(draw, box, radius=22, width=6)

    inner_x = box[0] + int(W * 0.030)
    line1 = "YOU WAKE UP"
    line2 = "5,000 YEARS"
    line3 = "AGO"
    avail = (box[2] - box[0]) - int(W * 0.060)

    f1, s1 = fit(draw, line1, FONT_BOLD, avail, int(W * 0.085))
    f2, s2 = fit(draw, line2, FONT_BOLD, avail - int(W * 0.02), int(W * 0.105))
    f3, s3 = fit(draw, line3, FONT_BOLD, avail, int(W * 0.105))

    y = box[1] + int(H * 0.030)
    draw.text((inner_x, y), line1, font=f1, fill=INK)
    y += s1 + int(H * 0.022)

    # second line: the number carries the colour so the eye lands on it first
    head, tail = "5,000", " YEARS"
    draw.text((inner_x, y), head, font=f2, fill=RUST)
    hw = draw.textlength(head, font=f2)
    draw.text((inner_x + hw, y), tail, font=f2, fill=INK)
    y += s2 + int(H * 0.018)

    draw.text((inner_x, y), line3, font=f3, fill=INK)
    y += s3 + int(H * 0.026)

    # --- bottom strap: the promise ---------------------------------------
    strap_text = "COULD YOU SURVIVE?"
    fs, ss = fit(draw, strap_text, FONT_BOLD, int(W * 0.46), int(W * 0.048))
    sw = draw.textlength(strap_text, font=fs)
    sh = ss + int(H * 0.032)
    sx, sy = pad, H - pad - sh
    draw.rounded_rectangle((sx, sy, sx + sw + int(W * 0.036), sy + sh),
                           radius=14, fill=INK)
    draw.text((sx + int(W * 0.018), sy + int(H * 0.016)), strap_text,
              font=fs, fill=CREAM)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    img.save(out.with_suffix(".jpg"), "JPEG", quality=90, optimize=True)
    # downscaled proof: what it looks like in a phone feed
    img.resize((320, 180), Image.LANCZOS).save("/tmp/thumb_small.png")
    print(f"wrote {out} and {out.with_suffix('.jpg')} ({W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
