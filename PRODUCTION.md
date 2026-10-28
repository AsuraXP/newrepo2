# Production log

Calibration is measured per episode. Never assume a value from a previous episode
carries over — voices, rates and edge-tts builds all drift.

## Episode 1 — "I Woke Up 5,000 Years Ago"

| field | value |
| --- | --- |
| voice / rate | en-US-AndrewNeural @ +10% |
| edge-tts | 7.3.1 |
| boundary granularity | ~10.2 words per event (sentence-level) |
| `sec_per_word` | 0.246 |
| narration | 835 words |
| measured runtime | 243.89 s (4:04) |
| frames | 40 |
| anchor precision | 32 exact / 8 in-sentence |
| video | 1280×720, 30 fps, locked-off camera, 1.0 s dissolves |

### Notes carried into episode 2

- This build reports **sentence-level** boundaries, so anchors are placed at sentence
  starts, one per sentence. That keeps every anchor on a measured timestamp.
- `sec_per_word` was 0.246, not the 0.33 the estimator shipped with. Always re-measure
  in Phase 0 rather than reusing this number.
- A force-reinstall of edge-tts is required on Kaggle; a cached wheel produces no audio.
