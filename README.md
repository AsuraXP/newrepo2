# Narration-first explainer pipeline

A gated workflow for one explainer episode. Narration is the master timeline: the number of entries in `frames.json` determines the frame count, and frame holds are measured from narration timestamps rather than authored by hand.

## Repository map

- `narration/preflight.md` — calibration passage; run on Kaggle before writing episode narration.
- `narration/narration.md` — episode script, with speakable prose only inside the TTS markers.
- `frames.json` — the single source of truth for frame count and anchor placement.
- `assets/STYLE.md` — fixed style and negative-prompt token blocks.
- `assets/frames/` — reviewed, compressed 1280×720 JPGs only.
- `kaggle/config.yaml` — voice, measured rate, and transition defaults.
- `kaggle/run.py` — offline estimate, single-request Edge TTS timing, and measured render.
- `tools/prep_frames.py` — strict frame validation/compression/contact sheet.
- `tools/selftest.py` — offline renderer and sync regression test.
- `PRODUCTION.md` — phase gates and calibration record.

## Absolute location boundary

Workspace work is research, writing, anchors, frame generation/QC, code and config. **Do not run TTS in the workspace.** Kaggle is for TTS, measured timing and stitching only; never author there or regenerate frames there. GitHub contains cloneable source/config but no large binary sources. Do not upload unreviewed images.

## Start here

1. Complete Phase 0 on Kaggle using `narration/preflight.md`; record the measured values in `PRODUCTION.md` and `kaggle/config.yaml`. Do not use an assumed rate.
2. Research and write the episode script and sources, then pass Gate 1.
3. Author sentence-start anchors in `frames.json`. Run `python kaggle/run.py --estimate --repo .` and pass Gate 2.
4. Fix and review the style/reference frame, generate and inspect every image, then run `python tools/prep_frames.py --repo . --sheet --strict`.
5. Run `python tools/selftest.py` before trusting the Kaggle render.
6. On Kaggle, install/force-reinstall dependencies and run a dry pass; inspect `timings.csv`. Only then render and review the final video.
7. Write publish assets only after the measured render passes Gate 5.

The repository begins intentionally uncalibrated and has no episode topic or authored episode. Phase 0 must be completed before estimate timings are meaningful. See `PRODUCTION.md` for the Kaggle commands and gate checklist.
