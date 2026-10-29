# Apocalypse Survival — Animated Story Video

**Slug:** `apocalypse_survival`
**Branch:** `arena/138cc5e0-newrepo2`
**Status:** Script drafted — awaiting approval

## Project Files

| File | Purpose |
|---|---|
| `brief.md` | Topic, runtime, POV, style, rules |
| `script.md` | Full narration text (Phase 2) |
| `visuals.csv` | Spine: slide_id, moment, moment_text, visual_prompt |
| `metadata.json` | Episode metadata |
| `youtube.txt` | Title, description, chapters (filled post-render) |
| `STATE.md` | Per-file state tracker |
| `frames/` | Accepted frame JPGs |
| `refs/` | Style anchors + continuity docs |

## Art Style

Stick-figure cartoon: white round head, bold black line body, simple expressive face. Colored flat-shaded environments. Minimal shading, no gradients. Bold outlines. Expressive character poses carry the emotion.

## Kaggle Handoff

```bash
!rm -rf newrepo2
!git clone --depth 1 --branch arena/138cc5e0-newrepo2 https://github.com/AsuraXP/newrepo2.git
!bash newrepo2/run_apocalypse_survival_kaggle.sh
```
