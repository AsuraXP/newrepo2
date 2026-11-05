#!/usr/bin/env python3
"""Contact sheet for a frame batch (~380px thumbs). Usage: make_sheet.py <batch>."""
import csv, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PER_BATCH = 8

def fname(s, m): return f"beat{s:02d}m{m:02d}.png"

def main(batch):
    rows = list(csv.DictReader(open(ROOT / 'visuals.csv')))
    chunk = rows[(batch - 1) * PER_BATCH : batch * PER_BATCH]
    items = [(fname(int(r['slide_id']), int(r['moment'])), r['moment_text']) for r in chunk]
    tw, th, pad, label_h, cols = 380, 214, 10, 42, 4
    nrows = (len(items) + cols - 1) // cols
    W = pad + cols * (tw + pad); H = pad + nrows * (th + label_h + pad)
    sheet = Image.new('RGB', (W, H), (20, 18, 16)); d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
        bold = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
    except OSError:
        font = bold = ImageFont.load_default()
    for i, (name, text) in enumerate(items):
        cx, cy = i % cols, i // cols
        x = pad + cx * (tw + pad); y = pad + cy * (th + label_h + pad)
        p = ROOT / 'frames' / name
        if p.exists():
            im = Image.open(p).convert('RGB'); im.thumbnail((tw, th))
            sheet.paste(im, (x + (tw - im.width) // 2, y + (th - im.height) // 2))
        d.text((x, y + th + 4), name, fill=(240, 235, 225), font=bold)
        d.text((x, y + th + 22), text if len(text) <= 54 else text[:52] + '…', fill=(180, 175, 165), font=font)
    outdir = ROOT / 'sheets'; outdir.mkdir(exist_ok=True)
    out = outdir / f'contact_batch{batch:02d}.jpg'
    sheet.save(out, quality=88)
    print('wrote', out, sheet.size)

if __name__ == '__main__':
    main(int(sys.argv[1]))
