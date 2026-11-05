#!/usr/bin/env python3
"""Write ancient_travel_video/youtube.txt from MEASURED Kaggle output only.

Runs on Kaggle AFTER render. Refuses to run unless both the rendered video
and build/timings.csv exist. Every number in the output is measured:
  - runtime      : ffprobe of ancient_travel_FINAL.mp4
  - chapters     : hold_start_s of each section's first beat in build/timings.csv
Never run this from estimates.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from vidsync.media import probe_duration  # measured, never estimated

VIDEO = REPO / "ancient_travel_FINAL.mp4"
TIMINGS = REPO / "build" / "timings.csv"
OUT = REPO / "ancient_travel_video" / "youtube.txt"

TITLE = "It Took Them 2,000 Days to Walk to the End of the World"

# Section-start beats -> chapter titles (slide map locked in STATE 5)
CHAPTERS = [
    ("beat01m01", "The beach where it started"),
    ("beat07m01", "Born to outrun everything"),
    ("beat11m01", "Life at walking speed"),
    ("beat17m01", "Maps made of songs"),
    ("beat21m01", "Crossing the open sea"),
    ("beat26m01", "Beringia and the kelp highway"),
    ("beat32m01", "Into the Americas"),
    ("beat37m01", "The man still walking it"),
]

DESCRIPTION = """Your ancestors walked out of Africa and didn't stop until they hit the end of the world — Tierra del Fuego, 42,000 km away. The actual walking? About 2,000 days. The journey? 50,000 years. This is the story of the greatest walk in history, and why your body is still built for it.

No one alive has finished it on foot — except one man, who is trying right now.
"""

TAGS = (
    "human migration, out of africa, prehistory, walking, persistence hunting, "
    "songlines, beringia, white sands footprints, paul salopek, out of eden walk, "
    "tierra del fuego, ancient humans, history documentary"
)

SOURCES = """Sources:
1. Out of Africa main dispersal ~60-70 ka - sciencedaily.com/releases/2017/12/171207141724.htm
2. Endurance anatomy - Bramble & Lieberman, Nature 2004 (doi:10.1038/nature03052)
3. Persistence hunting in the Kalahari - Liebenberg, Current Anthropology 2006 (doi:10.1086/508695)
4. Hadza daily travel distances - nature.com/articles/s41562-020-01002-7
5. Camp relocation distances - Marlowe 2010 / O'Connell 1988
6. Songlines as oral maps - walkingoncountry.com.au/what-is-a-songline/
7. Sahul sea crossing + Madjedbebe ~65 ka - australiangeographic.com.au (2017)
8. Beringia and the kelp highway - scienceinsights.org/what-was-beringia-the-land-bridge-to-the-americas/
9. White Sands footprints 23-21 ka - npr.org/2021/09/24/1040381802
10. Longest prehistoric migration >20,000 km - NTU/GenomeAsia100K, Science 2025
11. Tierra del Fuego earliest occupation ~11 ka (Tres Arroyos)
12. Paul Salopek, Out of Eden Walk - outofedenwalk.nationalgeographic.org
"""


def mmss(t: float) -> str:
    t = int(round(t))
    return f"{t // 60:02d}:{t % 60:02d}"


def main() -> int:
    if not VIDEO.exists():
        print("make_youtube_txt: ancient_travel_FINAL.mp4 missing - render first", file=sys.stderr)
        return 2
    if not TIMINGS.exists():
        print("make_youtube_txt: build/timings.csv missing - dry-run first", file=sys.stderr)
        return 2

    starts = {}
    with TIMINGS.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            starts[row["id"]] = float(row["hold_start_s"])

    missing = [bid for bid, _ in CHAPTERS if bid not in starts]
    if missing:
        print(f"make_youtube_txt: beats missing from timings.csv: {missing}", file=sys.stderr)
        return 2

    runtime = probe_duration(VIDEO)  # measured from the rendered file

    chapter_lines = []
    prev = -10.0
    for i, (bid, label) in enumerate(CHAPTERS):
        t = 0.0 if i == 0 else starts[bid]
        if i > 0 and t - prev < 10.0:
            print(f"make_youtube_txt: chapter '{label}' starts <10s after previous "
                  f"({t:.1f}s) - YouTube requires >=10s; aborting", file=sys.stderr)
            return 3
        prev = t
        chapter_lines.append(f"{mmss(t)} {label}")

    body = (
        f"TITLE\n{TITLE}\n\n"
        f"RUNTIME (measured from rendered file)\n{mmss(runtime)} ({runtime:.2f} s)\n\n"
        f"DESCRIPTION\n{DESCRIPTION}\n"
        f"Chapters:\n" + "\n".join(chapter_lines) + "\n\n"
        f"{SOURCES}\n"
        f"TAGS\n{TAGS}\n\n"
        f"THUMBNAIL\nancient_travel_video/thumbnail.jpg (baked text: 50,000 YEARS / 2,000 DAYS / ON FOOT.)\n\n"
        f"PROVENANCE\nRuntime measured by ffprobe on ancient_travel_FINAL.mp4; chapter times are\n"
        f"hold_start_s values from build/timings.csv (measured word-boundary sync, Phase 4).\n"
    )
    OUT.write_text(body, encoding="utf-8")
    print(f"youtube.txt written: runtime {mmss(runtime)}, {len(CHAPTERS)} chapters")
    for line in chapter_lines:
        print(" ", line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
