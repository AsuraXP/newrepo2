# PRODUCTION RECORD

Episode-specific progress and measurements. The universal workflow lives in
docs/WORKFLOW_SPEC.md. Never copy example numbers into this file as if they
were observed - every value below must come from an actual run.

## Episode

- topic: Apocalypse survival aboard a ship you just boarded — crowds onboard, a few
  infections among passengers, but safer than land: no contact with shore, and far
  more zombies on land than on the ship (second person, explicitly fictional).
- narrator voice: en-US-AndrewNeural @ +10% (user-selected 2026-10-28; calibrate with this)
- working branch: arena/99202f8c-newrepo2
- status: Topic + voice recorded; Phase 0 preflight awaiting user's Kaggle run

## Calibration

Filled ONLY from an actual Kaggle preflight run of narration/preflight.md.
Until then every field reads PENDING - nothing here is measured yet.

- edge-tts: PENDING
- voice and rate: PENDING measurement (config set to user choice: en-US-AndrewNeural / +10%)
- requested boundary type: PENDING (config requests WordBoundary explicitly)
- observed boundary type: PENDING
- granularity and coverage: PENDING
- sync_source: PENDING
- sec_per_word: PENDING (kaggle/config.yaml estimate.sec_per_word is still null)
- audio duration: PENDING
- source-word recovery: PENDING
- measured with: narration/preflight.md
- limitations: PENDING

## Progress log

- 2026-10-30: State 1 Step A ✅ — new premise (user's original: bite ignored,
  1-week gap, immunity twist), 10–12 min, YouTube long-form 16:9, POV second
  person (user-confirmed). 3 style refs received into
  `apocalypse_ship_video/refs/` (minimal 2D stick-figure storytime style).
  Step B v2 (hook + thumbnail pick) awaiting user.
- 2026-10-30: Animated-story master-spec session started on branch
  arena/c93850c6-newrepo2. Project folder `apocalypse_ship_video/`
  initialized (State 0 done; State 1 Step A pending: runtime, platform,
  visual style). Voice remains en-US-AndrewNeural @ +10%. No TTS in
  workspace.
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

- Gate 0 (calibration): PENDING - awaiting user's Kaggle run
- Gate 1 (script): not started (topic not selected)
- Gate 2 (anchors): not started
- Gate 3 (frames / style): not started - MANDATORY STOP for user style selection
- Gate 4 (verify + measure): not started
- Gate 5 (render): not started
- Gate 6 (publish assets): not started
