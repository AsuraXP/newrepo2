# lost_week_video

Second-person horror short, ~10 minutes. Working title: **"The Week You Lost"**.

You were bitten in a stairwell by a man who looked almost normal. You went home, bandaged it, slept.
You wake to a phone that says seven days are gone, a bite mark that has healed too well, and a hunger
that gets you out of bed before you have looked at a single notification.

Not a "don't get bitten" story. You never had stage one. You are the thing that walked through the
week you lost.

## Status

| Step | State | Notes |
|---|---|---|
| Brief | done | `brief.md` (includes director's critique + act timings) |
| Script | **awaiting approval** | `script.md` — 1,917 words ≈ 10:18 projected |
| Spine (`visuals.csv`) | not started | micro-beat split happens after script approval |
| Style anchors (`refs/`) | blocked | waiting on the user's art-style reference image |
| Frames | not started | `frames/beat{slide:02d}m{moment:02d}.png` |
| Thumbnail | not started | `thumbnail.jpg` |
| Kaggle runner | not started | `../run_lost_week_kaggle.sh` |

## Contents

```
script.md       narration only (lines starting with ## are act markers, not read aloud)
brief.md        logline, hard rules, critique of the opening, act timings, hook ladder
visuals.csv     slide_id, moment, moment_text, visual_prompt (word-reactive spine)
continuity.md   locked style + character blocks, verbatim prompt text, moderation log
refs/           style anchor images + winning-prompt records
frames/         one PNG per micro-beat, named beat{slide:02d}m{moment:02d}.png
metadata.json   upload metadata (title, description, tags)
youtube.txt     paste-ready YouTube title / description / tags
STATE.md        state-machine log, QC exceptions, declared exceptions
```

## Rules for this project

- No TTS, no audio, no FFmpeg in this workspace. Frames and text only.
- Frame count and durations are outputs. The Kaggle word-boundary timestamps decide every cut.
- Reference images are art style and character inspiration only — never a spatial template.
