# PRODUCTION RECORD

Episode-specific progress and measurements. The universal workflow lives in
docs/WORKFLOW_SPEC.md. Never copy example numbers into this file as if they
were observed - every value below must come from an actual run.

## Episode

- topic: PENDING (awaiting user selection)
- narrator voice: PENDING (awaiting user selection; config default until then: en-US-EmmaMultilingualNeural / +0%)
- working branch: arena/99202f8c-newrepo2
- status: Phase 0 tooling prepared; awaiting topic/voice selection, then Kaggle preflight run

## Calibration

Filled ONLY from an actual Kaggle preflight run of narration/preflight.md.
Until then every field reads PENDING - nothing here is measured yet.

- edge-tts: PENDING
- voice and rate: PENDING (current config default: en-US-EmmaMultilingualNeural / +0%)
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
