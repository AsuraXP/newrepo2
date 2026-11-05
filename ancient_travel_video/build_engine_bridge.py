#!/usr/bin/env python3
"""Bridge the approved 182-beat CSV spine into the tested vidsync engine inputs.

Writes:
  - narration/narration.md  (TTS:START/END markers around the approved script)
  - frames.json             (182 entries; id == frames/beatNNmMM.png stem)

The engine requires anchor_phrase to be 3-8 verbatim narration words. Many
micro-beats are shorter than 3 words, so for those rows the anchor window is
extended forward to the minimum 3 significant words; the anchor START remains
the first word of the micro-beat, so frame timing still lands on the beat.
Long beats are anchored on their first 8 significant words. Occurrence is set
explicitly whenever the chosen phrase repeats.

No durations are written. No tooling is rebuilt; this only emits engine inputs.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from vidsync.textnorm import tokenize, find_phrase_occurrences  # noqa: E402

PROJECT = ROOT / "ancient_travel_video"
NEG = (
    "No text, no letters, no numbers, no watermark, no signature, no extra limbs, "
    "no melted faces, no photorealism, no 3D render."
)


def sig_count(tokens):
    return sum(1 for t in tokens if t.norm)


def main() -> int:
    script = (PROJECT / "script.md").read_text(encoding="utf-8")
    parts = script.split("\n---\n")
    if len(parts) < 3:
        print("ERROR: script.md must have narration between --- dividers", file=sys.stderr)
        return 2
    narration = parts[1].strip()
    normalized = " ".join(narration.split())
    words = tokenize(normalized)

    rows = list(csv.DictReader(open(PROJECT / "visuals.csv", encoding="utf-8")))
    joined = " ".join(" ".join(r["moment_text"].split()) for r in rows)
    if joined != normalized:
        print("ERROR: CSV moment_text concatenation != script narration", file=sys.stderr)
        return 2

    # Token start index for each row.
    starts = []
    cursor = 0
    for r in rows:
        starts.append(cursor)
        cursor += len(tokenize(r["moment_text"]))
    if cursor != len(words):
        print(f"ERROR: token count mismatch {cursor} != {len(words)}", file=sys.stderr)
        return 2

    entries = []
    prev_start = -1
    extended = 0
    truncated = 0
    for i, r in enumerate(rows):
        start = starts[i]
        row_len = len(tokenize(r["moment_text"]))
        row_tokens = words[start : start + row_len]
        n_sig = sig_count(row_tokens)

        if 3 <= n_sig <= 8:
            window = row_tokens
        elif n_sig > 8:
            window = []
            seen = 0
            for t in row_tokens:
                window.append(t)
                if t.norm:
                    seen += 1
                if seen == 8:
                    break
            truncated += 1
        else:
            window = []
            seen = 0
            j = start
            while j < len(words) and seen < 3:
                t = words[j]
                window.append(t)
                if t.norm:
                    seen += 1
                j += 1
            extended += 1

        phrase = " ".join(t.text for t in window)
        first_sig = next(t.index for t in window if t.norm)
        if first_sig <= prev_start:
            print(f"ERROR: anchor start not increasing at row {i}", file=sys.stderr)
            return 2
        prev_start = first_sig

        hits = find_phrase_occurrences(words, phrase)
        if first_sig not in hits:
            print(f"ERROR: phrase does not match at expected start row {i}: {phrase!r}", file=sys.stderr)
            return 2
        entry = {
            "id": f"beat{int(r['slide_id']):02d}m{int(r['moment']):02d}",
            "anchor_phrase": phrase,
            "image_prompt": r["visual_prompt"],
            "negative_prompt": NEG,
        }
        if len(hits) > 1:
            entry["occurrence"] = hits.index(first_sig) + 1
        entries.append(entry)

    (ROOT / "frames.json").write_text(json.dumps({"frames": entries}, indent=2) + "\n", encoding="utf-8")

    narr_md = (
        "# Narration — ancient_travel_video\n\n"
        "Approved second-person script. Sources live in ancient_travel_video/script.md.\n\n"
        "<!-- TTS:START -->\n"
        f"{narration}\n"
        "<!-- TTS:END -->\n"
    )
    (ROOT / "narration").mkdir(exist_ok=True)
    (ROOT / "narration" / "narration.md").write_text(narr_md, encoding="utf-8")

    print(f"frames.json entries : {len(entries)}")
    print(f"anchors extended    : {extended} (short beats padded to 3-word minimum)")
    print(f"anchors truncated   : {truncated} (long beats anchored on first 8 words)")
    print(f"narration words     : {sum(1 for w in words if w.norm)}")
    print("bridge: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
