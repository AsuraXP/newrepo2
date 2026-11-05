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
- status: ancient_travel_video/ STATE 5 - frame batches in progress (40/182
  done, batches 1-5; anchor B locked, script approved 1,210 words ~6.5 min).
  Brief confirmed (6 min+, default voice, 2nd person, style-only refs, no
  captions, 16:9, YouTube). Phase 0 preflight still awaiting user's Kaggle run

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

- Gate 0 (calibration): PENDING - awaiting user's Kaggle run
- Gate 1 (script): not started (topic not selected)
- Gate 2 (anchors): not started
- Gate 3 (frames / style): not started - MANDATORY STOP for user style selection
- Gate 4 (verify + measure): not started
- Gate 5 (render): not started
- Gate 6 (publish assets): not started
