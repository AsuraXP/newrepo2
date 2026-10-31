# Explainer video — production workspace

**Status:** State 4, reference tests await user approval. Topic: how standardized screw threads helped build the Crystal Palace; five-minute YouTube explainer, second-person narration. The user's own visual-style reference images are in `refs/`; generated anchors and sequence frames do not yet exist. The folder slug is provisional. Hook 1, thumbnail A, defaults and narration approved. The 177-row visual spine is provisional. Character and location style tests have been generated after earlier HTTP 403 errors; no anchors have been approved and no sequence frames exist.

## Governing workflow

Concept → hook/thumbnail selection → script approval → word-reactive visuals → reference approval → frame batches and thumbnail → Kaggle runner → handoff. Stop at every approval gate. AUTOPILOT is off.

- `brief.md`: concept and creative decisions.
- `script.md`: approved narration, written only after the brief gates.
- `visuals.csv`: `slide_id,moment,moment_text,visual_prompt`; the source of frame count after scripting.
- `frames/`: reviewed sequence PNGs, named `beatNNmNN.png`.
- `refs/`: style tests and approved character/location anchors.
- `continuity.md`: exact anchor prompts, invariants, and moderation substitutions.
- `metadata.json`: machine-readable production settings.
- `youtube.txt`: publishing copy, finalized after the concept and script gates.
- `STATE.md`: current gate, decisions, and next action.

## Reuse and environment boundary

The repository already contains `vidsync/`, `kaggle/run.py`, and `tools/`. Reuse working components where compatible; do not replace the existing pipeline merely to rename its inputs. State 6 will add the project-specific Kaggle shell runner and any necessary adapter, with offline tests only in this workspace.

Workspace: writing, silent estimates, image generation/QC, and Git operations only. Kaggle: all speech synthesis, audio mixing, encoding, and deliverable packaging. No audio generation or FFmpeg preview in this workspace.

Planning estimate: spoken words ÷ 3.1 words/second. Final duration comes from Kaggle's continuous-take word timestamps, never a frame budget or manually assigned holds.
