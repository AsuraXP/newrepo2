# apocalypse_ship_video — Animated Story Video Project

State-machine production folder (MASTER SPEC: States 0–7).

- Slug: `apocalypse_ship`
- Branch: `arena/c93850c6-newrepo2`
- Hard boundary: NO audio in this workspace. TTS, mixing, encoding, and the
  final ZIP happen ONLY on Kaggle (State 6 runner script).

## Files

| File | Purpose | State |
|---|---|---|
| `brief.md` | concept, hooks, thumbnail pitch, defaults | 1 |
| `script.md` | plain-text narration (POV, word count, runtime) | 2 |
| `visuals.csv` | word-reactive spine (`slide_id,moment,moment_text,visual_prompt`) | 3 |
| `refs/` + `continuity.md` | style anchors + invariants log | 4 |
| `frames/` | accepted frames `beat{slide:02d}m{moment:02d}.png` | 5 |
| `metadata.json`, `youtube.txt` | publish assets | 5/7 |
| `STATE.md` | state-machine position + declared exceptions | all |

## Repo relationship

Existing tooling (`vidsync/`, `kaggle/`, `tools/`) is built and tested —
run it, never rebuild it. The State 6 Kaggle runner
(`run_apocalypse_ship_kaggle.sh`) is modeled on the existing repo scripts.
