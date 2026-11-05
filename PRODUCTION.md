# PRODUCTION RECORD

Episode-specific progress and measurements. The universal workflow lives in
docs/WORKFLOW_SPEC.md. Never copy example numbers into this file as if they
were observed - every value below must come from an actual run.

## Episode

- topic: How ancient humans traveled such long distances — second-person walk from
  East Africa (~60 ka) to Tierra del Fuego (~11 ka); hook "It Took Them 2,000 Days
  to Walk to the End of the World" (topic pivot by user 2026-11-05; project folder
  ancient_travel_video/).
- narrator voice: en-US-AndrewNeural @ +10% (user-selected 2026-10-28; calibrate with this)
- working branch: arena/1cbb32ec-newrepo2
- status: ancient_travel_video/ STATE 5.5 DONE + STATE 6 READY (182/182 frames
  accepted, batches 1-23; anchor B locked, script approved 1,210 words;
  104.6 MB quantized 1280x720 PNG, 23 contact sheets, 14 QC rejects all
  repaired + 2 moderation re-words, 0 unresolved). Thumbnail baked
  (thumbnail.jpg, 4-word hook, legible at 336 px). Engine bridge committed:
  frames.json 182 entries + narration/narration.md; offline Gate 2 PASS
  (UNCALIBRATED fallback estimate only); selftest 43/43 PASS. Kaggle runner
  run_ancient_travel_kaggle.sh + KAGGLE_CELLS.md ready. Next: user runs Kaggle
  Phase 0 preflight (Gate 0), then Phase 4 dry-run. No TTS/audio in workspace.

## Calibration

Filled ONLY from an actual Kaggle preflight run of narration/preflight.md.
Measured on Kaggle 2026-11-05 (Gate 0 PASS, user-pasted report, verbatim values).

- edge-tts: 7.3.1
- voice and rate: en-US-AndrewNeural / +10% (volume +0%, pitch +0Hz) — measured, matches config
- requested boundary type: WordBoundary (explicit, never engine default)
- observed boundary type: WordBoundary
- granularity and coverage: WORD-LEVEL — 57 boundary events, 57/57 events carried
  exactly 1 word (min 1 / max 1 / mean 1.00); every covered word has a measured timestamp
- sync_source: measured: word-boundary event timestamps (verified word correspondence);
  timestamp order monotonically non-decreasing; event text corresponds to source words in order
- sec_per_word: 0.3381 (audio: 19.272 s / 57 words) — recorded in kaggle/config.yaml
  estimate.sec_per_word; events-based value 0.3319 (last event end / words) noted for reference
- audio duration: 19.272 s (measured from file)
- source-word recovery: 57/57 (100.0% coverage), interpolated: 0, unrecovered: 0;
  timestamp provenance: 57 words backed by measured event timestamps, 0 interpolated
- measured with: narration/preflight.md (57 words, target ~60)
- limitations: calibration passage is 57 words — sec_per_word for the full 1,210-word
  narration may drift slightly; Gate 4 dry-run holds are the authoritative measurement.
  Gate 0 measurement checks: PASS.

## Progress log

- 2026-11-05: Gate 0 PASS. User ran Kaggle preflight (Cell 1): edge-tts 7.3.1,
  WordBoundary observed, 57 events / 57 words (100% recovery, 0 interpolated),
  audio 19.272 s, sec_per_word 0.3381. Recorded verbatim in Calibration above;
  kaggle/config.yaml estimate.sec_per_word set to 0.3381. Next: Phase 4 dry-run.

- 2026-11-05: STATE 5.5 + STATE 6 prep. Thumbnail: textless anchor-B art +
  baked 4-word hook "50,000 YEARS / 2,000 DAYS" (thumbnail.jpg 1280x720;
  thumbnail_336.jpg legibility QC PASS). Bridge: build_engine_bridge.py emits
  frames.json (182 entries; verbatim anchors, 15 short beats forward-extended
  to 3-word minimum, 50 long beats first-8-word anchors, 4 explicit
  occurrences, no durations) + narration/narration.md (approved script between
  TTS markers). kaggle/run.py --estimate: GATE 2 offline PASS; estimated
  runtime 484.0 s / 8.07 min using UNCALIBRATED fallback 0.4000 s/word —
  diagnostics only, NOT measured. tools/selftest.py 43/43 PASS. Runner:
  run_ancient_travel_kaggle.sh (preflight/dry/render/package) + KAGGLE_CELLS.md;
  Kaggle derives render JPGs from committed PNG spine via prep_frames --strict.
  Phase 0 preflight still awaiting user's Kaggle run.
- 2026-11-05: STATE 5 COMPLETE. All 182/182 frames accepted (batches 1-23),
  verified vs visuals.csv (0 missing / 0 extra), 104.6 MB quantized 1280x720
  PNG. 23 contact sheets with reject audit trail; 14 cumulative QC rejects
  (all repaired) + 2 moderation re-words; 0 unresolved. Closing montage +
  ancient/modern blended final horizon locked. Next: STATE 5.5 thumbnail /
  STATE 6 Kaggle runner (TTS/mix/FFmpeg/ZIP on Kaggle only; no audio here).
- 2026-11-05: STATE 3-5. visuals.csv locked (182 micro-beats / 42 slides,
  verbatim invariant check PASS). Anchor B (cinematic) approved + locked.
  Frame batches 1-5 done: 40/182 quantized 1280x720 PNGs, contact sheets with
  reject audit trail, 6 QC rejects repaired + 2 moderation re-words, all
  accepted. Locations locked: beach/coast, savanna, Kalahari. Next: batch 6.
- 2026-11-05: Topic pivot to ancient human long-distance travel (user brief).
  Folder renamed ancient_travel_video/; user style refs copied to refs/
  (STYLE ONLY). Script written: 1,210 words, second person, sourced; STATE 2
  stop for approval.
- 2026-11-05: Single-agent producer spec adopted; project folder
  ancient_travel_video/ initialized (STATE 0). Existing vidsync/kaggle/tools
  pipeline retained for reuse. STATE 1 brief questions issued; awaiting user.
- 2026-10-28: Preflight crash fixed: edge-tts 7.3.1 stores `Communicate.texts`
  as a generator consumed by the stream; chunk counting now tees instead of
  len()-ing. Selftest 43/43 PASS. Re-run Phase 0 on Kaggle.
- 2026-10-28: Built v2 tooling imported unchanged from branch
  arena/d8370f31-newrepo2 into this session's branch (run, never rebuild).
  Awaiting user: topic + narrator voice.
- 2026-10-28: Workflow spec streamlined to v2 (docs/WORKFLOW_SPEC.md): tooling
  marked as built (never rebuild), activity-narration banned, remaining steps
  only.
- 2026-10-28: Workflow tooling created (vidsync library, kaggle/preflight.py,
  kaggle/run.py, tools/prep_frames.py, tools/selftest.py, config, preflight
  passage). Offline validation and selftest run in the workspace; no TTS run
  in the workspace (per spec). Pushed to the working branch; awaiting the
  user's Kaggle preflight run for Gate 0 measurements.

## Gate status

- Gate 0 (calibration): PASS 2026-11-05 - Kaggle preflight measured: edge-tts
  7.3.1, WordBoundary observed, 57/57 words word-level (100% recovery, 0
  interpolated), audio 19.272 s, sec_per_word 0.3381 recorded in config
- Gate 1 (script): PASS - approved 1,210-word second-person script; speakable
  marker passage checks clean (no markdown/URLs/parentheses)
- Gate 2 (anchors): PASS offline - 182/182 anchors matched, no ambiguity/order
  errors; runtime estimate UNCALIBRATED (fallback 0.4000 s/word), measured
  timing still pending Phase 4
- Gate 3 (frames / style): PASS - anchor B user-selected + approved; 182/182
  frames accepted vs locked prompts; strict frame set verified (0 missing/extra)
- Gate 4 (verify + measure): MEASURED 2026-11-05 (Kaggle dry-run, user-pasted
  report): audio 375.168 s, 1207 WordBoundary events, recovery 1206/1210
  (99.7%, 4 interpolated, 0 unrecovered - engine split text into 2 internal
  chunks), timestamps monotonic, all 182 anchors exact/measured, 22
  transition conflicts (holds < 1.0 s fade on micro-beats). User requested
  one-shot delivery -> render proceeds with explicit --allow-reduced-precision
  + --allow-transition-overlap (recorded approval)
- Gate 5 (render): PENDING
- Gate 6 (publish assets): thumbnail PASS (336 px legible); title/description/
  chapters/runtime PENDING measured render
