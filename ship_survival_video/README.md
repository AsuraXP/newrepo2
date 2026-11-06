# ship_survival — episode project

Swarm-spec v3.0 project folder for the ship-survival episode. The repository's
existing `vidsync/` + `kaggle/` pipeline is the render engine for this episode;
this folder supplies the brief, the narration, the word-reactive spine and the
frames. Do not rebuild tooling that already exists (docs/WORKFLOW_SPEC.md).

## Contents

```
README.md        this file
brief.md         State 1 record (awaits user confirmation)
script.md        State 2 narration (empty until the brief is confirmed)
visuals.csv      State 3 spine: beat-level rows, durations are outputs
continuity.md    State 4 style/character anchor lock + moderation log
metadata.json    machine-readable episode record (measured fields null)
youtube.txt      State 6 publish assets (stub until rendered)
frames/          beat{slide:02d}m{moment:02d}.png
refs/            style test refs + winning anchors
STATE.md         state-machine ledger (append-only)
```

## Boundaries

- **Workspace (here):** script, CSV, frame generation, QC, commits. No TTS, no
  voice audition, no FFmpeg preview.
- **Kaggle:** the only place TTS, mixes, encodes and the ZIP deliverable exist.
- **Git:** source of truth; reviewed compressed frames only, no large binaries.

Silent estimate only: `frame_count` comes from `visuals.csv`; projected runtime
is `words / 3.1` and is always labelled an estimate.

## Naming

Frames: `frames/beat{slide:02d}m{moment:02d}.png`, matching assigned CSV rows.

## Current state

State 1 — brief issued, awaiting the user's answers. See `STATE.md`.
