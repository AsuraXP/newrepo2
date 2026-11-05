# Kaggle cells — ancient_travel_video

Run in a Kaggle notebook with **Internet ON**. Stop at each STOP and paste the
output back here. Do not add approval flags until the measured timings have
been reviewed.

Repo: `https://github.com/AsuraXP/newrepo2.git`
Branch: `arena/1cbb32ec-newrepo2`

## Cell 1 — clone/pull + Phase 0 preflight (Gate 0)

```python
!git clone --branch arena/1cbb32ec-newrepo2 https://github.com/AsuraXP/newrepo2.git /kaggle/working/video-repo || git -C /kaggle/working/video-repo pull --ff-only
!bash /kaggle/working/video-repo/run_ancient_travel_kaggle.sh preflight
```

STOP: paste the full PREFLIGHT CALIBRATION REPORT. I will record it in
PRODUCTION.md and set `kaggle/config.yaml -> estimate.sec_per_word` from the
measured value before Phase 4.

## Cell 2 — Phase 4 dry-run (Gate 4, after Gate 0 is recorded)

```python
!git -C /kaggle/working/video-repo pull --ff-only
!bash /kaggle/working/video-repo/run_ancient_travel_kaggle.sh dry
```

STOP: paste the full output and attach `/kaggle/working/video-repo/build/timings.csv`.
If it reports TRANSITION CONFLICTS or REDUCED PRECISION, do not force flags;
share the output for review.

## Cell 3 — Phase 5 render (Gate 5, after timings approved)

```python
!git -C /kaggle/working/video-repo pull --ff-only
!bash /kaggle/working/video-repo/run_ancient_travel_kaggle.sh render
```

Only if explicitly approved after review:
`... render --allow-reduced-precision` and/or `... render --allow-transition-overlap`.

STOP: review `ancient_travel_FINAL.mp4` end to end. Paste the render summary.

## Cell 4 — package (after measured publish copy is written)

```python
!git -C /kaggle/working/video-repo pull --ff-only
!bash /kaggle/working/video-repo/run_ancient_travel_kaggle.sh package
```

Deliverable: `ancient_travel_DELIVERABLE.zip` (video, thumbnail, youtube.txt,
script, metadata, measured timings/manifest).
