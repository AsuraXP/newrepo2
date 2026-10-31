#!/usr/bin/env python3
"""Kaggle-only narration and rendering for the story video.

--preflight is deliberately offline and safe in the workspace. Rendering,
including TTS, audio processing and encoding, is refused outside Kaggle.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import math
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'story_video'
sys.path.insert(0, str(ROOT))
from vidsync.textnorm import tokenize
from vidsync.timing import recover_word_times
from vidsync.tts import RealEdgeTTS, is_kaggle

VOICE = 'en-US-AndrewNeural'
RATE = '+10%'


def preflight():
    from PIL import Image
    for name in ('script.md', 'visuals.csv', 'metadata.json', 'youtube.txt'):
        path = PROJECT / name
        if not path.is_file() or not path.stat().st_size:
            raise ValueError(f'Missing or empty required file: {path}')
    json.loads((PROJECT / 'metadata.json').read_text(encoding='utf-8'))
    text = (PROJECT / 'script.md').read_text(encoding='utf-8').strip()
    with (PROJECT / 'visuals.csv').open(encoding='utf-8', newline='') as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != ['slide_id', 'moment', 'moment_text', 'visual_prompt']:
            raise ValueError('Unexpected visuals.csv columns')
        rows = list(reader)
    if not rows:
        raise ValueError('No visual moments')
    if re.sub(r'\s+', ' ', ' '.join(r['moment_text'] for r in rows)).strip() != re.sub(r'\s+', ' ', text).strip():
        raise ValueError('Visual moments do not reconstruct the narration exactly')
    cursor, starts, files, seen = 0, [], [], set()
    for row in rows:
        if not row['slide_id'].isdigit() or not row['moment'].isdigit() or not row['moment_text'].strip():
            raise ValueError(f'Invalid moment: {row}')
        name = f"beat{int(row['slide_id']):02d}m{int(row['moment']):02d}.png"
        if name in seen:
            raise ValueError(f'Duplicate frame {name}')
        seen.add(name)
        frame = PROJECT / 'frames' / name
        if not frame.is_file():
            raise ValueError(f'Missing frame: {frame}')
        with Image.open(frame) as im:
            im.verify()
        starts.append(cursor)
        tokens = tokenize(row['moment_text'])
        if not tokens or any(not token.norm for token in tokens):
            raise ValueError(f'Empty or punctuation-only token in {name}')
        cursor += len(tokens)
        files.append(frame)
    if cursor != len(tokenize(text)):
        raise ValueError('Moment word counts do not match script')
    print(f'Preflight OK: {len(rows)} frames, {cursor} narration tokens.', flush=True)
    return text, rows, files, starts


def render():
    if not is_kaggle():
        raise RuntimeError('Rendering and synthesis are only permitted on Kaggle')
    from PIL import Image
    import edge_tts

    text, rows, files, starts = preflight()
    voices = asyncio.run(edge_tts.list_voices())
    if not any(v.get('ShortName') == VOICE for v in voices):
        raise RuntimeError(f'Voice cannot be resolved: {VOICE}')
    out = Path('/kaggle/working/story_video_build')
    out.mkdir(parents=True, exist_ok=True)
    padded = out / 'padded'
    padded.mkdir(exist_ok=True)

    # No rescaling: pad every source to the same maximum even canvas in PIL.
    sizes = []
    for path in files:
        with Image.open(path) as im:
            sizes.append(im.size)
    width = math.ceil(max(w for w, _ in sizes) / 2) * 2
    height = math.ceil(max(h for _, h in sizes) / 2) * 2
    frame_paths = []
    for index, path in enumerate(files):
        with Image.open(path) as im:
            canvas = Image.new('RGB', (width, height), 'black')
            canvas.paste(im.convert('RGB'), (0, 0))
            target = padded / f'{index:04d}.png'
            canvas.save(target, format='PNG', optimize=False, compress_level=6)
            frame_paths.append(target)

    # One continuous Edge-TTS stream with explicit word boundaries.
    audio = out / 'narration.mp3'
    result = RealEdgeTTS(VOICE, rate=RATE).synthesize(text, audio, boundary='WordBoundary')
    if result.returned_boundary_types != ['WordBoundary']:
        raise RuntimeError(f'Word-boundary timestamps unavailable: {result.returned_boundary_types}')
    times, report = recover_word_times(text, result.events)
    print(report.summary(), flush=True)
    if not report.correspondence_ok or report.interpolated_words or report.unrecovered_words:
        raise RuntimeError('Cannot map every narration word to a measured timestamp; refusing approximate cuts')
    if not report.timestamps_monotonic or any(times[i].source != 'measured' for i in starts):
        raise RuntimeError('Invalid or unmeasured frame-start timestamps')
    cuts = [0.0] + [times[i].t_start for i in starts[1:]] + [result.audio_duration_s]
    if any(x is None for x in cuts) or any(b <= a for a, b in zip(cuts, cuts[1:])):
        raise RuntimeError('Invalid or non-increasing frame cut times')
    (out / 'word_events.json').write_text(result.to_json(), encoding='utf-8')
    concat = out / 'frames.ffconcat'
    with concat.open('w', encoding='utf-8') as fh:
        fh.write('ffconcat version 1.0\n')
        for i, path in enumerate(frame_paths):
            # All paths are generated locally; escape single quotes for ffconcat.
            escaped = str(path).replace("'", "'\\''")
            fh.write(f"file '{escaped}'\noption framerate 1000\nduration {cuts[i+1] - cuts[i]:.9f}\n")
        escaped = str(frame_paths[-1]).replace("'", "'\\''")
        fh.write(f"file '{escaped}'\noption framerate 1000\n")
    video = out / 'VIDEO.mp4'
    subprocess.run([
        'ffmpeg', '-hide_banner', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat),
        '-i', str(audio), '-map', '0:v:0', '-map', '1:a:0', '-r', '30',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
        '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-t', f'{result.audio_duration_s:.9f}',
        '-movflags', '+faststart', str(video),
    ], check=True)
    thumbnail = out / 'thumbnail.jpg'
    with Image.open(frame_paths[0]) as im:
        im.convert('RGB').save(thumbnail, 'JPEG', quality=90)
    archive = Path('/kaggle/working/story_DELIVERABLE.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for path in (video, thumbnail, PROJECT / 'metadata.json', PROJECT / 'script.md', PROJECT / 'youtube.txt'):
            z.write(path, path.name)
    print(f'Deliverable ready: {archive}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--preflight', action='store_true', help='offline source/frame check only')
    args = parser.parse_args()
    try:
        preflight() if args.preflight else render()
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
