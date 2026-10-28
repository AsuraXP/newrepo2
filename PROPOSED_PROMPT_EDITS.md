# Proposed targeted edits to your original production spec

These are proposed replacements/additions only, not a rewritten spec. All text not identified below stays exactly as supplied. No episode-specific details are added.

## 1. Replace PHASE 0 only

```text
====================================================================
PHASE 0 — PREFLIGHT CALIBRATION (Kaggle, before any authoring)
====================================================================

PURPOSE: replace assumptions about the TTS engine with measurements. Run an actual
Kaggle preflight before authoring. The assistant prepares and publishes the test;
the user only runs the supplied notebook cells. No manual dataset upload.

DO:

1. In the workspace, create narration/preflight.md containing roughly 60 words of plain
   prose with several sentences, wrapped in <!-- TTS:START --> and <!-- TTS:END -->.

2. Create kaggle/preflight.py and the supporting pipeline/config/dependency files.
   The test must synthesize only the marked preflight passage in one request, request
   WordBoundary explicitly, and print:
   - installed engine version, voice, rate, requested and returned boundary types
   - boundary-event count and words per event
   - recovered versus expected source words, timestamp order and word coverage
   - non-zero audio duration and suggested seconds per word
   - sync_source and whether timing is measured or interpolated

   Make the script resolve repository paths from its own location. Add a Kaggle-only
   guard so it cannot accidentally run TTS in the workspace. Test syntax and offline
   logic here; NEVER execute synthesis here.

3. Push the test script and all required source/config files to the public GitHub working
   branch before asking the user to run it. Verify public unauthenticated clone access.
   Keep large binaries and generated test outputs out of Git. Do not request a Kaggle
   dataset upload, ZIP upload, or manual copying of source files.

4. Supply runnable Kaggle cells with the actual public repository URL and working branch
   filled in. Internet must be enabled. Use clone for a new notebook and pull for an
   existing clone; retain one consistent absolute repository path in every command:

   # New clone (assistant supplies the real URL and branch):
   !git clone --branch <WORKING_BRANCH> <PUBLIC_REPO_URL> /kaggle/working/video-repo

   # Existing clone — use instead of cloning again:
   !git -C /kaggle/working/video-repo pull --ff-only

   !pip install -q --upgrade --force-reinstall edge-tts pyyaml
   !python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
   !python /kaggle/working/video-repo/kaggle/preflight.py

   Placeholders above describe the universal template only. The delivered cells must
   contain real values, not placeholders. Request only the output report needed for
   verification; do not ask the user to discover technical settings manually.

5. Read the actual report and record in PRODUCTION.md:
   - engine version, voice and rate
   - requested and observed boundary granularity, word coverage and sync_source
   - measured seconds per word, source-word recovery and audio duration
   - passage used and any limitations

   Copy measured seconds per word into kaggle/config.yaml -> estimate.sec_per_word.
   Example numbers are never calibration evidence. Do not assume a rate or confuse
   sentence-boundary interpolation with word-accurate timestamps.

6. If the service returns sentence-only or incomplete word metadata, fix the requested
   mode or provide verified word-level alignment and repeat the test on Kaggle. Do not
   automatically restrict the creative workflow to sentence-start anchors. If exact
   timing remains unavailable, explain the limitation and obtain explicit approval of
   reduced precision before proceeding.

GATE 0:
[ ] Test script and required source/config pushed and publicly cloneable without auth
[ ] User can clone/pull and run the supplied cells without uploading a dataset
[ ] Actual Kaggle test completed; no TTS ran in the workspace
[ ] sync_source, engine version and observed timestamp granularity recorded
[ ] Word coverage and source recovery verified; audio duration is non-zero
[ ] estimate.sec_per_word matches the actual measured value
[ ] Word-reactive timing supported, or reduced precision explicitly explained and approved
```

## 2. PHASE 1, step 3: replace only its second sentence

Replace:
```text
   A sentence break is a natural breath and a good place for a frame anchor.
```
With:
```text
   A sentence break is a natural breath, not a mandatory frame boundary. Visual anchors
   follow changes in meaning and action, including within a sentence.
```

## 3. PHASE 2: replace THE GRANULARITY RULE block, up to ANCHOR RULES

```text
THE GRANULARITY RULE (read Gate 0 before this):

Author visual beats from the narration's meaning. Choose timestamp support to serve those
beats; do not reshape the narration or restrict every beat to a sentence because of an
engine default.

Use what the engine actually reported in Phase 0, and verify it again in Phase 4.

  one event per WORD, with complete verified coverage
    -> every word has a measured timestamp
    -> anchors may sit anywhere; word-accurate sync is achievable

  one event per SENTENCE, or incomplete word coverage
    -> words inside unmeasured spans are approximate unless accurately aligned separately
    -> do not silently force anchors to sentence starts or call interpolation word-accurate
    -> stop timing acceptance; obtain word-level metadata/alignment, or ask for explicit
       approval of reduced precision and explain its effect on the authored beats

The actual Kaggle preflight verifies the engine contract before authoring. Recheck that
contract against the full narration in Phase 4.
```

## 4. PHASE 2, ANCHOR RULES: replace the three sentence/cadence bullets only

Replace the bullets beginning “One anchor per sentence”, “Anchor on the first words”, and
“Anchor cadence”, including their continuation lines, with:

```text
- Anchor where the narrated subject, action, location, explanation or visual idea changes.
  Multiple anchors may sit inside one sentence; a continuing idea may span sentences
- Frame count emerges from these authored beats, never from dividing runtime into slots
- No fixed cadence or hand-set holds. Estimated holds are diagnostics only. Short holds,
  long holds and transition conflicts require review, not automatic merging, padding or
  removal of meaningful beats
```

Keep all other anchor rules and the FRAME ENTRY example unchanged.

## 5. PHASE 2, GATE 2: retain the command and first checkbox; replace the rest

```text
[ ] Authored frame count equals the number of entries in frames.json — nothing merged
[ ] Short/long estimated holds and transition risks reviewed without forcing a cadence
[ ] Runtime estimate and its basis/uncertainty reported, not treated as a required range
[ ] Visual beats follow narrated meaning; no artificial one-anchor-per-sentence restriction
```

## 6. PHASE 3, step 3: add one rejection criterion

After “wrong subject or action”, add:

```text
   - missing or unrecognizable defining subject/object: a generic scene or crowd is not a
     substitute for the specific thing the narration names
```

After step 4, add:

```text
   Check each frame against its exact narrated beat as well as the style reference.
   Re-review affected artwork whenever narration or anchors change.
```

Add to GATE 3:

```text
[ ] Every frame clearly depicts the subject/action required by its narrated beat
```

## 7. PHASE 4: add live verification before step 2

```text
   Before the live pass, supply public GitHub clone/pull cells and dependency installation
   instructions. Do not require a manual dataset upload. Inspect the installed engine
   version; reinstall if needed to obtain the required version, rather than assuming a
   cached package is always defective.

   The live pass must report engine version, requested and returned boundary types,
   recovered source words, timestamp order/coverage, non-zero audio duration, and measured
   seconds per word. Record these in PRODUCTION.md and update the planning estimate only
   from measured evidence. Exact anchor claims require verified metadata text alignment,
   not merely a boundary-event count.

   One continuous video narration request only. Preserve its audio and timing artifacts
   for Phase 5; do not synthesize the same narration again just to stitch the final video.
```

In step 3, replace the anchor_precision item with:

```text
   - anchor_precision : "exact" for word-reactive anchors, backed by verified word-level
                        timestamps/alignment; approximation requires informed approval,
                        not automatic movement to a sentence start
```

Replace the GATE 4 checkbox about moving in-sentence anchors with:

```text
[ ] Actual boundary type, word coverage, source recovery and non-zero duration verified
[ ] Word-reactive anchors are exact; any reduced precision explicitly explained and approved
```

## 8. PHASE 5: add after the render command

```text
The render command must reuse Phase 4's verified audio and timing artifacts. If the current
implementation synthesizes again, add an explicit reuse mode before passing this phase.
```

## 9. HARD RULES: replace rules 1 and 5 only

```text
1.  Calibrate the engine on Kaggle before authoring using the published test script.
    Never treat an assumed rate as measured; no manual dataset upload is required.
5.  Anchors follow visual meaning, not sentence count or fixed cadence. Word-reactive
    anchors require verified word-level timing; reduced precision needs informed approval.
```

## 10. ACCEPTANCE SUMMARY: replace these two rows only

```text
  holds             | derived from measured timestamps; readability/transition risks resolved
  anchor precision  | word-accurate, or reduced precision by explicit informed choice
```

The existing “merged/warned | zero” acceptance still applies: diagnostic warnings must be
resolved explicitly in the implementation/report, not hidden or bypassed by dropping frames.

---

Everything else in your original prompt stays unchanged, including its title, numbered
sections, locations, examples, frame preparation, static-camera rule, transition minimum,
publishing requirements and division of responsibility.
