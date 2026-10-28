# Brief — THE LIST

## One line
A man and his dog walk four blocks of open ground across a dead city to answer a
radio that reads the names of the living, one at a time, every night.

## Locked parameters

| Field | Value |
|---|---|
| Slug | `zombie_survival_video` |
| Working title | THE LIST |
| Runtime target | 300 s (5 min) — draft 3 projects 293 s |
| POV | **Second person, present tense, male lead, held throughout** |
| Voice | Deep male, measured — edge-tts `en-US-ChristopherNeural`, rate `-10%` |
| Pace basis | ~3.1 wps for runtime projection |
| Style / look | **LOCKED** — flat 2D hand-drawn stick-figure cartoon (owner refs in `refs/`) |
| Hard rules | None beyond the house defaults |
| Captions | None (silent-safe frames, no burned subs) |
| Aspect | 16:9 — 1920×1080 native |
| Platform | YouTube |
| Frame rate | 30 fps |
| Audio (Kaggle only) | AAC 192k, −14 LUFS loudnorm |

## Voice rationale
Owner deferred the voice choice; the lead is male, so a male read. Survival narration wants weight, not
energy: the story is a countdown of small decisions, and a brisk read would turn
it into an action recap. `en-US-ChristopherNeural` at `-10%` gives a low, even,
documentary cadence with room between sentences. The runner preflights the voice
against `edge-tts --list-voices` and dies if it does not resolve — no silent
substitution.

## Format engine (from the owner reference)
1. Cold open on a blunt fact that turns. 2. "First problem, the X."
3. Real arithmetic on real quantities. 4. A house-rule refrain, amended
on the final line. 5. "Here is the thing nobody tells you about the dead."
6. Inventory ledger before the ending. 7. End on a knock.

## Tone locks
- Second person, present tense, held for the entire script. No POV switches.
- Procedural voice, modelled on the owner's reference video: numbered problems,
  day markers, costed arithmetic, flat statements, no lyrical simile.
- Short declaratives. Facts, not adjectives. The horror is in the arithmetic.
- No explanation of the outbreak's origin. Ever.
- The dog is a partner, never a victim and never comic relief.
- Ends on a door left unlocked, not on a rescue.

## Hard rules
- Nothing gory. Violence is implied by framing and aftermath, never shown.
- No named real people, no real places, no real events. Fictional throughout.
- The radio numbers are consistent: 841 last month, 794 tonight, 796 after the
  broadcast. If the script changes, these change together.
- The protagonist is male and unnamed until the transmission. He gives his name and
  the dog's, and that is the only name-drop in the film.

## Audio boundary
This workspace produces frames, text, CSV, and the Kaggle runner. It never calls
TTS, never mixes, never encodes. Runtime figures quoted here are word-count
projections only (words ÷ 3.1), not measurements.
