# PRODUCTION RECORD

Episode-specific progress and measurements. The universal workflow lives in
docs/WORKFLOW_SPEC.md. Never copy example numbers into this file as if they
were observed - every value below must come from an actual run.

## Episode

- topic: 72 Hours After the Zombie Breakout — second person, fictional
  outbreak, real survival logic hour by hour. Package: `zombie_72h_video/`.
  The earlier ship/cruise premise is SCRAPPED (user, 2026-10-31).
- narrator voice: en-US-AndrewNeural @ +10% (user-selected 2026-10-28; calibrate with this)
- working branch: arena/c1b41521-newrepo2
- status: Brief locked and script written (1,513 words, 8.13 min projected).
  Awaiting user approval of the script before the visuals.csv spine. Phase 0
  preflight still awaiting user's Kaggle run.

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

- 2026-10-31: Episode switched to "72 Hours After the Zombie Breakout".
  Ship/cruise premise scrapped at user's request. Created self-contained
  `zombie_72h_video/` package (brief, script, continuity, STATE, metadata,
  youtube draft) and sourced the factual claims. Script awaiting approval.

- 2026-10-31: User supplied three art-style reference images (stick-figure
  deadpan cartoon: cave/campfire, white-field figure, couch prop shot). Stored
  read-only in `style_refs/`; sampled palette + frozen token block written to
  `assets/STYLE.md`. Style is user-selected; a generated anchor frame still
  needs explicit approval (Gate 3). Topic still open.

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
- Gate 1 (script): WRITTEN, awaiting user approval
- Gate 2 (anchors): blocked on script approval
- Gate 3 (frames / style): style SELECTED by user (stick-figure deadpan, `assets/STYLE.md`); anchor frame not yet generated or approved
- Gate 4 (verify + measure): not started
- Gate 5 (render): not started
- Gate 6 (publish assets): not started
