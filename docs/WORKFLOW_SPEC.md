# Narration-First Explainer Video — Production Spec

This is the universal workflow specification. Episode-specific topics,
styles, settings, measurements and production progress live in the episode
files and PRODUCTION.md — never here.

====================================================================
0. CORE PRINCIPLE
====================================================================

Narration is the master timeline. Frames react to the words and their meaning.

- Frame count = the number of anchors in frames.json. Decided at authoring time.
- Frame duration = measured time between anchor timestamps. Derived, never hand-set.
- Audio = one continuous narration, synthesized in a single request. Never chunked per scene, per beat, or per paragraph.
- Runtime is an output, not an input. Never trim or pad the script to hit a target length.
- Visual anchors follow changes in narrated subject, action, location or explanation.
  They are not restricted to sentence boundaries or fixed-duration slots.

Nothing downstream may silently change the frame count. If anchors are added, removed or
moved during an approved revision, the frame count is re-derived from frames.json, not
adjusted by hand. Reopen affected gates and re-review affected artwork.

====================================================================
1. THREE LOCATIONS
====================================================================

WORKSPACE : research, script, anchors, frame generation + visual QC, all code and config.
            Must NEVER run TTS.

GITHUB    : source of truth. Everything the render needs, cloneable without auth.
            Must NEVER hold large binaries.

KAGGLE    : TTS + measured timing, and stitching.
            Must NEVER author content, edit prompts, or regenerate frames.

Kaggle never authors. The workspace never synthesizes. Keep that boundary absolute.

The assistant creates and pushes the required scripts before asking the user to run them.
The user must not be asked to upload a dataset, upload a ZIP, or manually copy source files
into Kaggle. Supply public GitHub clone/pull instructions instead.

Keep generated source images, audio, video and other large outputs out of Git. Reviewed,
compressed frame JPGs may be included within the repository's size budget. If approved
assets require external storage, provide an automated retrieval step, not a manual upload.

====================================================================
PHASE 0 — PREFLIGHT CALIBRATION (Kaggle, before any authoring)
====================================================================

PURPOSE: replace assumptions about the TTS engine with measurements. This phase runs before
a single word of episode narration is written. Test the engine's actual timing metadata
and speaking rate instead of assuming either.

DO:

1. Create narration/preflight.md containing roughly 60 words of plain prose with several
   sentences, wrapped in <!-- TTS:START --> and <!-- TTS:END --> markers.

2. Create the preflight test script and all supporting code/config in the workspace.

   Provide a dedicated entry point:

   python kaggle/preflight.py

   It must:
   - resolve repository paths from its own location
   - refuse to synthesize outside Kaggle
   - synthesize only the marked preflight passage, in one request
   - explicitly request WordBoundary rather than relying on an engine default
   - print installed edge-tts version, voice, rate, requested and returned boundary types
   - print boundary-event count, words per event, source-word recovery and word coverage
   - validate timestamp order and correspondence to the source text
   - print non-zero audio duration and suggested sec_per_word
   - print sync_source and distinguish measured timestamps from interpolation

   Test syntax and offline logic in the workspace. NEVER run synthesis there.

3. Push the test script, preflight passage, dependencies and supporting code/config to the
   public GitHub working branch BEFORE asking the user to run anything.

   Verify that the repository can be cloned without authentication. Do not require a
   Kaggle dataset, ZIP upload or manual copying of source files.

4. Give the user ready-to-run Kaggle cells with the actual repository URL and branch
   filled in. Internet must be enabled.

   For a new notebook:

   !git clone --branch <WORKING_BRANCH> <PUBLIC_REPO_URL> /kaggle/working/video-repo

   For an existing clone, use this instead of cloning again:

   !git -C /kaggle/working/video-repo pull --ff-only

   Then run:

   !pip install -q --upgrade --force-reinstall edge-tts pyyaml
   !python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
   !python /kaggle/working/video-repo/kaggle/preflight.py

   The placeholders above describe this reusable workflow. In the actual cells delivered
   to the user, replace them with the real public URL and working branch.

   Use the same absolute repository path throughout all later Kaggle instructions.
   Install any additional declared dependencies required by the implementation.

5. Read the actual report and record:

   - installed edge-tts version, voice and rate
     -> PRODUCTION.md
   - requested and observed boundary type, words per event and word coverage
     -> PRODUCTION.md
   - sync_source, source-word recovery and audio duration
     -> PRODUCTION.md
   - measured seconds per word
     -> kaggle/config.yaml -> estimate.sec_per_word

   Do not infer word accuracy from event count alone. Verify that event text corresponds
   to the source words and that the required timestamps are present.

6. If the engine returns sentence-only or incomplete word metadata, correct the requested
   mode or provide verified word-level alignment and repeat the test on Kaggle.

   Do not automatically change the creative workflow to one frame per sentence. If
   word-accurate timing remains unavailable, explain the limitation and obtain explicit
   approval of reduced precision before proceeding.

RECORD in PRODUCTION.md at repo root:

   ## Calibration
   - edge-tts: <actual installed version>
   - voice and rate: <actual settings>
   - requested boundary type: <requested type>
   - observed boundary type: <returned type>
   - granularity and coverage: <actual measured result>
   - sync_source: <measured metadata/alignment or explicit approximation>
   - sec_per_word: <actual measured value>
   - audio duration: <actual measured duration>
   - source-word recovery: <recovered count>/<expected count>
   - measured with: preflight.md
   - limitations: <any unresolved limitations>

Never copy example measurements into the calibration record as if they were observed.
Recheck calibration applicability when the engine, version, voice, rate or boundary mode
changes.

GATE 0:
[ ] Test script and required source/config pushed and publicly cloneable without auth
[ ] User can clone/pull and run the supplied cells without uploading a dataset
[ ] Actual Kaggle preflight completed; no TTS ran in the workspace
[ ] sync_source is printed and understood
[ ] Engine version, settings, observed granularity and word coverage recorded
[ ] estimate.sec_per_word in config.yaml matches the measured value
[ ] Audio duration is non-zero and recovered source words match the preflight text
[ ] Word-reactive timing supported, or reduced precision explicitly explained and approved

====================================================================
PHASE 1 — RESEARCH AND SCRIPT
====================================================================

DO:

1. Research the topic. Collect sources as you go, with URLs.

2. Write narration/narration.md:
   - Speakable text only between <!-- TTS:START --> and <!-- TTS:END -->
   - No headings, bullets, links, markdown emphasis, or parenthetical stage directions
     inside the markers
   - A "## Sources" section after the end marker — it is stripped before synthesis

3. Write for the ear, not the page: short sentences, concrete nouns, one idea per sentence.
   A sentence break is a natural breath, not a mandatory frame boundary. Visual anchors
   follow changes in meaning and action, including within a sentence.

4. State estimates as estimates ("perhaps one person in a hundred"). Never invent a precise
   figure to sound authoritative.

5. Let the runtime be whatever the script honestly takes. Do not pad, do not compress.

GATE 1:
[ ] Script contains no markdown characters that TTS would read aloud
[ ] Every factual claim has a source in "## Sources"
[ ] Estimated duration is reported, and is treated as an estimate only
[ ] Read it aloud once. Any sentence you stumble over is rewritten, not kept

====================================================================
PHASE 2 — ANCHORS (frames.json)
====================================================================

This is where timing is won or lost. Anchor placement decides whether the final video is
word-accurate or approximately right.

THE GRANULARITY RULE (read Gate 0 before this):

Author visual beats from the narration's meaning. Timing support must serve those beats;
an engine default must not dictate the script's sentence structure or visual count.

Use what the engine actually reported in Phase 0, and verify it again in Phase 4.

  one event per WORD, with verified source correspondence and coverage
    -> every covered word has a measured timestamp
    -> anchors may sit anywhere; word-accurate sync is achievable

  one event per SENTENCE, or incomplete word coverage
    -> only the supplied boundaries are measured
    -> unmeasured word positions are approximate unless accurately aligned separately
    -> do not silently call interpolation word-accurate
    -> obtain word-level metadata/alignment, or explicit approval of reduced precision

A sentence may need multiple frames. A continuing visual idea may span multiple sentences.
Do not move meaningful anchors to sentence starts merely to satisfy a metadata limitation.

ANCHOR RULES:

- anchor_phrase is copied VERBATIM from the narration — 3 to 8 words
- Anchor where the narrated subject, action, location, explanation or visual idea changes
- Multiple anchors may sit inside the same sentence when the meaning calls for them
- A continuing idea may keep the same frame across sentence boundaries
- Frame count emerges from authored visual beats, never from dividing runtime into slots
- No fixed cadence or uniform holds. Do not force frames to last 5–10 seconds, or any other
  predetermined interval
- Estimated holds are diagnostics only. Short holds, long holds and transition conflicts
  require review, not automatic merging, padding or removal of meaningful beats
- Frames appear in narration order; anchor start positions must be distinct and increasing
- occurrence selects which appearance of a repeated phrase (1-based, negative counts from the
  end). Use it whenever a phrase repeats — never rely on the first match by accident
- transition is OPTIONAL. Omit it and the config default applies. Only override when a
  specific beat needs a different move
- Never add a hand-set duration to a frame entry

FRAME ENTRY:

  {
    "id": "07_no_year",
    "anchor_phrase": "Nobody here will tell you the year",
    "occurrence": 1,
    "image_prompt": "<subject>, <verbatim style token block>",
    "negative_prompt": "<verbatim negative token block>"
  }

During this phase, author the scene content and anchors. Do not invent or freeze an art
style to fill the style placeholders. Complete those blocks only after the STYLE GATE
in Phase 3 passes.

GATE 2:

Run the offline check — no network, no Azure:

  python kaggle/run.py --estimate --repo .

[ ] Every anchor matched; no MISSING, ambiguity or order errors
[ ] Authored frame count equals the number of entries in frames.json — nothing merged
[ ] Short/long estimated holds and transition risks reviewed without forcing a cadence
[ ] Runtime estimate and its basis reported, not treated as a required range
[ ] Visual beats follow narrated meaning; no artificial one-anchor-per-sentence restriction

====================================================================
PHASE 3 — FRAMES AND VISUAL QC (workspace)
====================================================================

MANDATORY STOP — USER CHOOSES THE ART STYLE

Do not choose an art style automatically. Do not infer approval from the topic, an example
in this specification, a previous episode, or the assistant's own preference.

Before generating the reference frame or any episode frames:

1. Ask the user to choose an art style. They may provide reference images, describe a style,
   or request suggestions.

2. If the user requests suggestions, present clearly distinct options for approval.
   Suggestions are not a selection. STOP and wait for the user's explicit choice.

3. Summarize the selected style and record it in assets/STYLE.md. Preserve any supplied
   references and identify the visual properties to match.

4. Generate a reference frame in the selected style and STOP again for user approval.
   Do not generate episode frames until the reference is explicitly approved.
   If rejected, revise the reference and repeat this approval step.

If the user already explicitly selected a style for this episode, confirm that selection
rather than asking them to choose again. Reference-frame approval is still required.

STYLE GATE:
[ ] User explicitly selected the art style for this episode
[ ] Selected style and references recorded in assets/STYLE.md
[ ] User explicitly approved the generated reference frame
[ ] No episode frames generated before these approvals

Only after this gate passes may the remaining Phase 3 steps begin.

DO:

1. Freeze the approved style token set in assets/STYLE.md and use the approved reference
   frame for all subsequent visual QC.

2. Append the style token block VERBATIM to every prompt. Same negative block every time.
   Consistency across the episode is the channel's identity; unapproved per-frame style
   changes break it. Scene content and composition must still match each narrated beat.

3. Generate in small batches. OPEN EVERY IMAGE AND LOOK AT IT. Reject and regenerate on:
   - wrong subject or action
   - missing or unrecognizable defining subject/object: a generic scene or crowd is not a
     substitute for the specific thing the narration names
   - off-model character (face, hands, proportions)
   - palette drift
   - text, watermarks, extra limbs
   - anything that reads as a different film

4. Keep the reference frame open beside each batch and compare directly.

   Check each frame against its exact narrated beat as well as the style reference.
   Re-review affected artwork whenever narration or anchors change.

5. Compress to 1280x720 JPG and build a contact sheet:

   python tools/prep_frames.py --repo . --sheet --strict

6. Review the contact sheet as one document. Any frame that stands out is regenerated.

Never push a frame you have not looked at. Compressed JPGs only; source PNGs stay out of
the repo.

GATE 3:
[ ] STYLE GATE passed before episode-frame generation
[ ] Approved style and negative blocks copied verbatim into every frame prompt
[ ] prep_frames.py --strict reports every frame present
[ ] Contact sheet reviewed end-to-end in one pass
[ ] Every frame on-model: same character, same palette, same line weight
[ ] Every frame clearly depicts the subject/action required by its narrated beat
[ ] Repo weight is reasonable (target: well under 5 MB of frames)

====================================================================
PHASE 4 — VERIFY THE PIPELINE, THEN MEASURE
====================================================================

DO:

1. Run the selftest BEFORE trusting a render. It uses a stand-in TTS backend and synthetic
   frames, so it needs no network:

   python tools/selftest.py

   It asserts: sync at every anchor, multiple distinct anchors within one sentence,
   uneven timestamp-driven holds, a genuinely static picture, transitions that actually
   blend, correct duration, audio muxed, and that missing or out-of-order anchors fail loudly.

   It must also distinguish sentence-only/incomplete metadata from word-accurate timing.
   Synthetic tests verify pipeline logic, not actual engine behavior.

2. Push all approved source/config and reviewed frames before asking for a Kaggle run.
   Supply the exact pull and execution cells. No dataset upload:

   !git -C /kaggle/working/video-repo pull --ff-only
   !python /kaggle/working/video-repo/kaggle/run.py --repo /kaggle/working/video-repo --dry-run

   Verify the actual engine version, voice/rate, returned boundary type, source-word
   recovery, timestamp coverage and non-zero audio duration for the full narration.

   Generate the full video narration in one continuous request. Preserve its audio and
   timing artifacts for Phase 5; do not synthesize it again merely to stitch the video.

3. Read timings.csv and check:
   - status           : no merged_*; every warning explicitly investigated and resolved
   - anchor_precision : exact for word-reactive anchors, backed by verified word timestamps
                        or alignment; reduced precision requires informed approval
   - hold_s vs est_hold_s : if these drift systematically, update sec_per_word
   - matched_text     : confirms which words the anchor actually landed on

   Holds come from successive measured anchor timestamps. The final hold ends at the
   measured narration end. Ensure picture coverage from time zero.

   Do not move anchors to sentence starts, merge frames or replace measured timing with
   fixed-duration slots merely to make validation pass.

GATE 4:
[ ] Selftest passes
[ ] Actual boundary type, word coverage, source recovery and non-zero duration verified
[ ] Measured frame count equals the number of entries in frames.json
[ ] No merged frames; timing and transition warnings explicitly resolved
[ ] Word-reactive anchors are exact; reduced precision explicitly explained and approved
[ ] Calibration updated in config.yaml if the estimator drifted
[ ] Verified narration audio and timing artifacts saved for reuse in Phase 5

====================================================================
PHASE 5 — RENDER
====================================================================

  !python /kaggle/working/video-repo/kaggle/run.py --repo /kaggle/working/video-repo --out final.mp4

This command must reuse Phase 4's verified audio and timing artifacts. If the implementation
requires an explicit reuse option, implement it and include it in the supplied command.
Do not synthesize the narration again just to stitch the final video.

Static camera. No zoom, no drift, ever — a slow zoom on a still image steps in whole-pixel
jumps and reads as shake. Transitions are long enough to be seen: 0.8 s MINIMUM, 1.0 s
DEFAULT for flat 2D art, which has no motion cues to imply a gradual change.

Check transition placement against the anchor timestamps. Transitions must not obscure
critical beats or cause silent frame loss. Resolve conflicts explicitly.

GATE 5:
[ ] Duration matches the measured narration length within a second
[ ] Rendered frame count equals the number of entries in frames.json
[ ] Picture is static when the frame is static
[ ] Every cut is visible as a transition, not a snap
[ ] Audio present and synchronised
[ ] Actual video reviewed end-to-end, not accepted from logs alone

====================================================================
PHASE 6 — PUBLISH ASSETS (only after Gate 5)
====================================================================

Order matters: title, thumbnail and chapter timestamps are all downstream of the MEASURED
runtime. Writing them earlier means rewriting them.

1. THUMBNAIL — generate the art with any text baked in; never composite text afterwards.
   Keep overlay wording to three or four words. Proof it at 336 px wide: if the words are not
   legible there, they do not exist.
2. TITLE — concrete, first person, matches the channel's voice.
3. DESCRIPTION — hook, honest summary, then chapters cut directly from timings.csv
   (not from estimates), then sources.
4. CHAPTERS — verified against timings.csv line by line.

GATE 6:
[ ] Thumbnail legible at 336 px
[ ] Chapter timestamps derived from timings.csv, not estimated
[ ] Runtime in the description matches the rendered file

====================================================================
HARD RULES
====================================================================

1.  Calibrate the engine on Kaggle before authoring. The assistant creates and pushes the
    test script and supplies clone/pull/run cells. No manual dataset upload. Never author
    against an assumed rate.
2.  One continuous narration request per video. Never chunk TTS. Reuse verified audio for
    stitching; a calibration passage is separate from the video narration.
3.  Never hand-set a frame duration. Durations are measured.
4.  Never generate a frame before its anchor exists. The separate style reference is the
    only exception and requires the user's prior style selection.
5.  Anchors follow narrated meaning, not sentence count or fixed cadence. Word-reactive
    anchors require verified word-level timing; reduced precision needs informed approval.
6.  Every frame is viewed before it is pushed, and checked against its narrated subject/action.
7.  The style token block is copied, never paraphrased.
8.  The camera is locked off. No ken burns.
9.  Transitions are at least 0.8 s.
10. Kaggle measures and stitches; it never authors.
11. frames.json is the only source of truth for frame count.
12. Publish assets are written from measured output, never from predictions.
13. Never choose the art style automatically. Stop for the user's explicit style selection,
    then stop for reference-frame approval before generating episode frames.

====================================================================
DIVISION OF RESPONSIBILITY
====================================================================

ASSISTANT: research, script, anchors, frame generation and visual QC, all code and config,
           creating and pushing the preflight test, ready-to-run Kaggle clone/pull/run
           cells, interpretation of test results, verification of every gate.

USER: run the Kaggle cells, share the requested output, choose the art style, approve the
      reference frame, review timings.csv when asked, review the render, ship.

The user is not responsible for manually uploading datasets or discovering engine properties.
The assistant prepares the tests and interprets the evidence.

The assistant must stop for required user decisions instead of treating its own suggestions
or generated examples as approval.

Keep this universal specification separate from episode-specific topics, styles, settings,
measurements and production progress. Record those in the episode files and PRODUCTION.md.

====================================================================
ACCEPTANCE SUMMARY
====================================================================

A finished episode satisfies all of these at once:

  preflight         | actual Kaggle measurement, delivered through GitHub clone/pull/run
  manual uploads    | none required
  art style         | explicitly selected by the user
  reference frame   | explicitly approved before episode-frame generation
  frames rendered   | equals frame count in frames.json
  merged frames     | zero
  timing warnings   | explicitly resolved, never hidden by dropping meaningful frames
  holds             | measured; readability and transition risks resolved
  anchor precision  | word-accurate, or reduced precision by explicit informed choice
  visual accuracy   | every frame depicts its narrated subject/action
  selftest          | passing, including word-reactive, static-frame and blend assertions
  runtime           | measured, and quoted in the description
  thumbnail         | text legible at 336 px
