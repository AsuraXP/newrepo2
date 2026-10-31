# zombie_72h_video — 72 Hours After the Zombie Breakout

Self-contained episode package. It does not modify the shared explainer
pipeline in `vidsync/`, `kaggle/`, or `tools/`; it borrows nothing at runtime
and can be cloned and built on Kaggle from this folder alone.

```
zombie_72h_video/
  README.md          this file — how the folder is used
  brief.md           locked episode parameters (POV, runtime, rules)
  script.md          narration between TTS markers + sources
  visuals.csv        THE SPINE: one row per beat (slide_id, moment, moment_text, visual_prompt)
  continuity.md      frozen style tokens, character invariants, moderation log
  STATE.md           state machine position, batch log, declared exceptions
  metadata.json      publish metadata, written from measured output
  youtube.txt        title, description, chapters, tags
  frames/            beatNNmMM.png, final frames only
  refs/              style test references and approved anchors
run_zombie_72h_kaggle.sh   (repo root) Kaggle-only build: TTS, timing, render, ZIP
```

## Hard boundary

- **Here (workspace):** script, CSV, frames, commits. Never TTS, never FFmpeg
  previews, never audio mixing.
- **Kaggle:** the only place `edge-tts`, `ffmpeg`, `loudnorm`, and the ZIP
  deliverable exist.

## Frame naming

`frames/beat{slide:02d}m{moment:02d}.png`, matching the `slide_id` and
`moment` columns of `visuals.csv`. A row with `slide_id=03, moment=07`
becomes `frames/beat03m07.png`.

## Duration model

Each row's `moment_text` is spoken by one continuous TTS take. The row holds
from the start of its first word to the start of the next row's first word.
Zero durations are hand-set.

## Rebuild

See `STATE.md` for the current phase and `run_zombie_72h_kaggle.sh` for the
one-command Kaggle build.
