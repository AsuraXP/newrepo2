# last_awake_video

Animated narrated YouTube episode — **"You're the Only One Awake (Sleep Is Rationed)"**.

Second-person sci-fi explainer: you are the last human awake aboard a station where sleep is a
scheduled, rationed resource. Story spine with a real sleep-science backbone.

- Target runtime: 10 min (~1,860 words @ 3.1 wps)
- Voice: `en-US-AndrewNeural` @ `+10%` (Edge-TTS — **Kaggle only**)
- 16:9, no burned captions, hard cuts only
- Style anchor: see `continuity.md` (populated at STATE 4 from `refs/`)

## Files

| Path | Written at | Purpose |
|---|---|---|
| `brief.md` | STATE 1 | Locked production parameters |
| `script.md` | STATE 2 | Plain-text second-person narration |
| `visuals.csv` | STATE 3 | The spine: `slide_id, moment, moment_text, visual_prompt` |
| `refs/` | STATE 4 | Style/character reference images — ARTSTYLE ONLY, never spatial templates |
| `continuity.md` | STATE 4 | Verbatim style tokens, character invariants, moderation substitutions |
| `frames/` | STATE 5 | `beat{slide:02d}m{moment:02d}.png` |
| `thumbnail.jpg` | STATE 5.5 | High-CTR thumbnail, legible at mobile size |
| `metadata.json` | STATE 6 | Title/description/tags for upload |
| `youtube.txt` | STATE 6 | Paste-ready YouTube title + description + chapters |
| `STATE.md` | all | State machine position, decisions, declared exceptions |

Render runner lives at repo root: `run_last_awake_kaggle.sh` (STATE 6).

## Boundary

This folder holds scripts, CSVs, frames, and state only. **No audio, no TTS, no FFmpeg here.**
Synthesis, mixing, encoding, and the deliverable ZIP happen exclusively on Kaggle.
