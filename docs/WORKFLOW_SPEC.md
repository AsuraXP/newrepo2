# NARRATION-FIRST EXPLAINER VIDEO — WORKFLOW (v2)

One episode: research → script → anchors → frames → measured render. Narration is the master timeline. Every phase ends with a GATE; do not start the next phase until it passes.

## FIRST ACTIONS (every session)

1. Read PRODUCTION.md and `git log --oneline -5`. Establish what is already done. NEVER rebuild existing tooling (`vidsync/`, `kaggle/`, `tools/` are built and tested — run them, do not rewrite them), never redo completed phases, never re-test validated code unless something changed.
2. Record the episode parameters in PRODUCTION.md before starting: topic, narrator voice.
3. Response style: one status line, the results, and exactly what the user must do next. No activity narration ("I did this, then this happened"), no long reports of your own work, no re-explaining completed phases.

## HARD RULES

1. Calibrate the engine on Kaggle before authoring. Never author against an assumed rate.
2. One continuous narration request per video. Never chunk TTS. Reuse verified audio for stitching.
3. Never hand-set a frame duration. Durations are measured.
4. Never generate a frame before its anchor exists (sole exception: the style reference, after the user selects the style).
5. Anchors follow narrated meaning, not sentence count or cadence. Word-accurate sync requires verified word-level timing; reduced precision requires explicit approval.
6. Every frame is looked at before it is pushed, and checked against its narrated subject/action.
7. The style token block is copied VERBATIM into every prompt. Same negative block every time.
8. Camera locked off. No ken burns, no zoom, no drift.
9. Transitions at least 0.8 s (default 1.0 s), ending exactly at the incoming frame's anchor.
10. Kaggle measures and stitches; it never authors. Workspace never runs TTS. GitHub holds no large binaries.
11. frames.json is the only source of truth for frame count.
12. Publish assets are written from measured output, never from predictions.
13. Never choose the art style automatically. Stop for the user's explicit selection, then for reference-frame approval.

## THREE LOCATIONS

- WORKSPACE: research, script, anchors, frame generation + visual QC, code/config. NEVER runs TTS.
- GITHUB: source of truth, cloneable without auth. NO large binaries (reviewed compressed frame JPGs only).
- KAGGLE: TTS + measured timing + stitching. NEVER authors content, edits prompts, or regenerates frames.

The assistant supplies ready-to-run Kaggle cells with the real URL and branch filled in. Never ask the user to upload a dataset, a ZIP, or copy source files manually.

## PHASE 0 — CALIBRATION (skip if PRODUCTION.md already records it)

Tooling exists. Do not rebuild it. If calibration is missing or the engine, version, voice, rate or boundary mode changed, the user runs on Kaggle (internet on):

```
!git clone --branch <current-branch> https://github.com/AsuraXP/newrepo2.git /kaggle/working/video-repo
```
(existing clone instead: `!git -C /kaggle/working/video-repo pull --ff-only`)
```
!pip install -q --upgrade --force-reinstall edge-tts pyyaml
!python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
!python /kaggle/working/video-repo/kaggle/preflight.py
```

User pastes the report. Record it in PRODUCTION.md `## Calibration` and set `kaggle/config.yaml -> estimate.sec_per_word` to the measured value.

GATE 0: report recorded; sec_per_word matches the measurement; word coverage and source-word recovery verified (or reduced precision explained and approved); sync_source understood.

## PHASE 1 — SCRIPT

- Research with URLs. Write `narration/narration.md`: plain speakable text only between `<!-- TTS:START -->` and `<!-- TTS:END -->`; no markdown, links, or parenthetical stage directions inside; `## Sources` after the end marker (stripped before synthesis).
- Short sentences, concrete nouns, one idea per sentence. Estimates stated as estimates. Runtime = whatever the script honestly takes.

GATE 1: no markdown TTS would read aloud; every factual claim sourced; duration reported as estimate only; read aloud once — rewrite anything stumbled over.

## PHASE 2 — ANCHORS (frames.json)

- anchor_phrase copied VERBATIM from the narration, 3–8 words. Anchor where subject, action, location, explanation or visual idea changes. Multiple anchors per sentence allowed; one idea may span sentences. `occurrence` for any repeated phrase (1-based, negative from end). `transition` optional (config default otherwise). NEVER a duration field.
- Entry: `{ "id", "anchor_phrase", "occurrence"?, "image_prompt", "negative_prompt"?, "transition"? }`. Before the style gate, image_prompt carries scene content with a style placeholder only — do not invent a style.

GATE 2: `python kaggle/run.py --estimate --repo .` passes — every anchor matched, no MISSING/ambiguity/order errors, frame count equals frames.json entries, short/long holds reviewed as diagnostics only, runtime estimate reported with its basis (never a target).

## PHASE 3 — FRAMES + VISUAL QC (MANDATORY STOPS)

1. STOP: the user selects the art style (their own choice; suggestions only on request; not a selection until they say so). Record it in `assets/STYLE.md`.
2. Generate ONE reference frame in that style. STOP: the user approves it. Revise and repeat on rejection.
   Style gate: explicit style selection AND explicit reference approval before any episode frame.
3. Then: freeze the style tokens; append the token block VERBATIM to every prompt, same negatives. Generate in small batches. Open every image. Reject: wrong subject/action, missing or unrecognizable named subject, off-model character, palette drift, text/watermarks/extra limbs, anything reading as a different film. Compare each batch against the reference frame and its exact narrated beat.
4. `python tools/prep_frames.py --repo . --sheet --strict`. Review the contact sheet end to end in one pass; regenerate stand-outs. Push only looked-at compressed JPGs; source images stay out of Git.

GATE 3: style gate passed first; strict prep reports every frame present; every frame on-model and beat-accurate; frames well under 5 MB.

## PHASE 4 — MEASURE

1. `python tools/selftest.py` must pass (already implemented; do not extend or rewrite without cause).
2. Push all reviewed frames and config. User runs:
```
!git -C /kaggle/working/video-repo pull --ff-only
!python /kaggle/working/video-repo/kaggle/run.py --repo /kaggle/working/video-repo --dry-run
```
3. User shares the output and `build/timings.csv`. Verify: no merged frames; every warning investigated and resolved; anchor_precision exact (reduced precision only with explicit approval); hold_s vs est_hold_s drift (systematic drift → update sec_per_word); matched_text correct. Holds are measured anchor-to-anchor; picture covers from time zero; final hold ends at the measured narration end. Never move anchors to sentence starts or merge frames to make validation pass.

GATE 4: engine verified on the full narration (boundary type, coverage, recovery, non-zero duration); frame count equals frames.json; artifacts preserved in `build/` for reuse.

## PHASE 5 — RENDER

```
!python /kaggle/working/video-repo/kaggle/run.py --repo /kaggle/working/video-repo --out final.mp4
```

This reuses Phase 4 artifacts automatically and refuses to synthesize again. Reduced precision requires `--allow-reduced-precision` (explicit informed approval).

GATE 5: duration within 1 s of the measured narration; rendered frame count equals frames.json; static picture static; every cut a visible transition; audio present and synced; the actual video reviewed end to end.

## PHASE 6 — PUBLISH (only after Gate 5)

Order: thumbnail (text baked into the art, 3–4 words, legible at 336 px) → title (concrete, first person) → description (hook, honest summary, chapters cut from timings.csv, sources) → chapters verified line by line against timings.csv. Runtime in the description = rendered runtime.

GATE 6: thumbnail legible at 336 px; chapter timestamps from timings.csv, not estimates; runtime matches the file.

## RESPONSIBILITIES

ASSISTANT: research, script, anchors, frames + QC, code/config, ready-to-run cells, result interpretation, gate verification. Stop for required user decisions (topic, style, reference approval, reduced-precision approval) — never treat suggestions or examples as approval.

USER: run the Kaggle cells, share output, choose the style, approve the reference, review timings.csv and the render, ship.

## ACCEPTANCE (all at once)

preflight measured via clone/pull/run · no manual uploads · style explicitly user-selected · reference explicitly approved · frames rendered == frames.json · zero merged frames · timing warnings resolved · holds measured · anchor precision exact or explicitly approved · every frame shows its narrated beat · selftest passing · runtime measured and quoted · thumbnail legible at 336 px
