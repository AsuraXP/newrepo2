# CONTINUITY — ONE OF THEM Ep.1

Status: MASTER ANCHOR LOCKED 2026-11-01 (user picked winner, option 1 of 2).

## MASTER ANCHOR — exact prompt (logged VERBATIM; copy never rephrased)
Ref file: refs/style_test_winner.png (character+style anchor).
Style source refs: refs/style_user_01..03.png (user-supplied look).
Unselected candidate: "Unselected files" (rejected 2026-11-01).

WINNING PROMPT (verbatim):
"A hand-drawn stick figure storytime scene in the exact style of the reference
images: a white-headed stick figure with simple dot eyes and thin black stick
limbs walks calmly down a city sidewalk while gray-green zombie stick figures
with droopy half-lidded eyes shuffle past in both directions, one zombie's
shoulder bumping the walker's arm. Bold wobbly black outlines, flat muted
colors, warm cream background, simple everyday objects, cartoon doodle energy,
tense but humorous mood. One single full-frame scene, no text, no watermark,
no lettering anywhere."

## STYLE BLOCK — append VERBATIM to every frame prompt (never rephrase)
"Hand-drawn stick figure storytime style exactly like the master anchor refs:
white round heads, minimal dot-eye faces with expressive eyebrows, thin black
stick limbs, bold wobbly black outlines, flat muted colors, warm cream/beige
backgrounds, simple everyday props, no gradients, no text or lettering
anywhere, no watermarks. Single clear scene per frame."

## NEGATIVE BLOCK — identical on every prompt
"text, letters, watermark, signature, photorealism, 3D render, gradients, gore,
blood splatter, extra limbs, merged faces, gibberish signs"

## ANCHOR RECIPE (every frame)
images=[refs/style_test_winner.png (master anchor), optional prior approved
frame from your own batch]. Scene content = the row's visual_prompt from
visuals.csv. STYLE BLOCK + NEGATIVE BLOCK copied verbatim. Explicit story-state
rules appended every time (sleeve state, wound stage, zombie behavior).

## Composition rule
Shots of figures pressing against glass/windows/barriers: camera on the
viewer's side, figures seen from behind, hands on the viewer's side of the
surface, interior visible through it.

## Content moderation log (pre-logged at STATE 3; finalized at STATE 4)
Risky narration -> prompt-safe replacements (already applied in visuals.csv):
- "teeth went into your forearm" / "bone" -> "jaw clamped on forearm, flat dark
  red splotch, no blood detail" / "thin pale glint in wound, stylized, no gore"
- "hit it until it stopped moving" -> "impact shown as a flat dark splotch, no gore"
- "knife into the base of her skull" -> "knife swung at back of head, impact
  shown as a flat dark splotch, no gore"
- "screamed", cage beat -> "caged figure with an open mouth, flat style"
- blood drops/scratches -> "flat red drop", "flat red scratch mark" (graphic, minimal)
- guns -> "simple stick rifle shapes, flat muzzle-flash doodles"

## Story-state invariants (every frame must obey)
- Protagonist: white round head, dot eyes, thin black stick limbs, long sleeves.
  Sleeve covers the forearm ALWAYS except explicit wound/scar close-ups
  (slides 03, 05, 08m21, 10m14-15, 12m19/22/24/25).
- Wound continuity: fresh bite+wrap (slide 02) -> red ring (03m17) -> purple
  (03m18) -> black edges (03m19) -> closing crescents (03m28) -> healed twin
  crescents (05m03-04) -> scarred crescents persist (12).
- Zombies: gray-green tint, droopy half-lidded eyes. They NEVER bite, chase,
  or react to the protagonist (sole exceptions: slide 02 flashback attack;
  slide 10 green-coat grab that slides off).
- Recurring: green-coat zombie woman (10m07-25, 12m10-14), Hector (big hands,
  quiet face), June (medic armband), Ollie (small kid, big dot eyes).
- Flashbacks/thought bubbles: desaturated memory tone / doodle bubbles. USER STYLE REFS RECEIVED
2026-11-01: refs/style_user_01.png (stick figure on couch, living room),
refs/style_user_02.png (stick figure, white void, finger up),
refs/style_user_03.png (stick figure by campfire in cave, night).

## Style analysis from user refs (target look for test refs)
- Hand-drawn stick figures: round white/cream heads, minimal faces (dot eyes,
  small line mouth), thin black stick limbs, occasional simple hair tufts.
- Bold black outlines, slightly wobbly hand-drawn line weight, closed shapes.
- Flat muted colors: warm cream/beige backgrounds, muted blue-gray, browns,
  soft simple shadows; slightly desaturated palette; no gradients.
- Simple everyday props, clean composition, one readable scene per frame.
- Face acting must read at thumbnail size (eyebrows do the heavy lifting).
This file is written only after style test refs are generated and the winning
anchor is approved. Contents when locked:

- Master style anchor: exact winning prompt + ref path (VERBATIM source block)
- Character look: face, silhouette, garments (protagonist sleeve always down)
- Palette + line weight invariants
- Props + creature rules (zombies never bite/react to protagonist)
- Content moderation log: blocked words and replacements (violence verbs →
  softer equivalents, gore → flat color-splotch language)
- Composition rule: shots of figures pressing against glass/barriers are shot
  from the viewer's side — figures from behind, hands on viewer's side of the
  surface, interior visible through it.
- Story-state rules per shot (sleeve up/down, wound stage, door open/closed)
