# STATE — last_awake_video

## Current state: STATE 1 (BRIEF) — BLOCKED on 2 user inputs

| State | Name | Status |
|---|---|---|
| 0 | Repo discovery & init | DONE — `docs/WORKFLOW_SPEC.md`, `vidsync/`, `kaggle/`, `tools/` present; run, never rebuild |
| 0.5 | Resume check | DONE — no pre-existing `<slug>_video/` folders; user chose "start fresh" |
| 1 | Brief | IN PROGRESS — 8/10 fields locked; awaiting hard rules + art-style ref |
| 2 | Scripting (`script.md`, ~1,860 words, 2nd person) | NOT STARTED |
| 3 | Spine (`visuals.csv`, word-reactive micro-beats) | NOT STARTED |
| 4 | Master anchor lock (style refs → `continuity.md`) | NOT STARTED |
| 5 | Frame generation loop (batches of 8, R=2) | NOT STARTED |
| 5.5 | Thumbnail (`thumbnail.jpg`) | NOT STARTED |
| 6 | Kaggle runner (`run_last_awake_kaggle.sh`) | NOT STARTED |
| 7 | Handoff cell | NOT STARTED |

## Locked decisions
- Runtime target: 10 min → ~1,860 words @ 3.1 wps.
- Voice/rate: `en-US-AndrewNeural` @ `+10%` (Edge-TTS, Kaggle-only).
- POV: second person ("you").
- Captions: none. Aspect: 16:9. Platform: YouTube long-form.
- Hard cuts only at render time: zero crossfades, dissolves, or fades between frames.

## Open questions
1. Hard rules — must appear / must never appear.
2. Art-style reference image (user will paste) → saved to `refs/`.

## Declared exceptions
(none)

## Log
- 2026-11-06: Scaffold created. STATE 0 + 0.5 complete. Brief fields collected via user prompts.
