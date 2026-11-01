# ONE OF THEM — Episode 1: "The Bite"

Animated story series produced with the word-reactive frame pipeline.
Premise: you were bitten by a zombie and survived, uninfected. The dead see
you as one of their own. Every survivor would be a threat if they knew.

## Folder map

```
README.md        this file
brief.md         locked brief (STATE 1)
script.md        full narration, second-person (STATE 2) — source of all words
visuals.csv      word-reactive spine (STATE 3): slide_id, moment, moment_text, visual_prompt
metadata.json    delivery metadata (final values from measured output at STATE 6)
youtube.txt      title + description draft (final values from measured output)
frames/          beat{NN}m{NN}.png — one per visuals.csv row
refs/            style test refs + winning master anchors (STATE 4)
continuity.md    anchor invariants, palette, moderation replacements (STATE 4)
STATE.md         state-machine log — read this first
```

## Hard boundary
This workspace NEVER runs TTS, FFmpeg, or voice audition. All audio, timing
measurement, and encoding happen on Kaggle via `run_one_of_them_kaggle.sh`.
