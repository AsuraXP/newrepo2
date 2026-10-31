# CONTINUITY — zombie_72h

The single source of truth for how this episode must look. Every prompt is
built by pasting the TOKEN BLOCK verbatim, then the scene line, then the
anchor images.

## 1. Style tokens

Master copy: `../assets/STYLE.md` (user's three reference images, palette
sampled). The block below is the episode copy. It must match that file; if the
two ever disagree, `assets/STYLE.md` wins and this file is corrected.

```
STYLE: 2D hand-drawn digital cartoon, deadpan stick-figure animation still.
Line: single uniform-weight black ink contour, ~4px at 1280px wide, slightly
wobbly hand-drawn edges, no line tapering, no cross-hatching, no sketch texture.
Fill: flat opaque color areas only, no gradients, no airbrush, no soft shadow,
no bloom; one flat shadow tone per surface at most.
Face: perfect circle head, blank off-white fill, two small solid black dot eyes,
one simple curved black mouth line; no nose, no ears, no eyebrows unless the
beat needs them; expression carried by mouth curve and eye placement alone.
Body: pure black stick limbs of even thickness with solid black round dot hands
and dot feet; torso is a single line unless clothing is specified.
Color: restrained flat palette — paper #F8F8F8, cream #F0E0C8, sand #E0D0B8,
floor brown #705038, cave rock #585050 / #403838, navy #182850, slate #788090,
with at most two warm accents from #D8A838 / #F08018 / #A85038 / #6B7A44.
Composition: wide 16:9 locked-off camera, eye-level or slightly above, figure
composed off-center with generous empty background, background furniture and
props drawn as simple flat blocks with black outlines.
Mood: dry, calm, matter-of-fact; comedy from understatement, never from
cartoon squash-and-stretch.
NEGATIVE: photorealistic, 3D render, CGI, painterly brushwork, oil paint,
watercolor wash, gradient mesh, lens flare, bokeh, depth-of-field blur, film
grain, motion blur, anime, manga speed lines, chibi, caricature, oversized
googly eyes, extra limbs, extra fingers, malformed hands, melted features,
duplicate heads, text, letters, captions, watermark, signature, UI chrome,
busy detail, ornate background, dramatic chiaroscuro, gore, blood spatter.
```

## 2. Invariants (drift is measured against these)

- PALETTE: flat fills only, from the hex list above. No new hues per frame.
- LINE: one uniform black contour weight everywhere. No thin/thick variation.
- HEAD: perfect circle, off-white `#F8F8F8`, fixed diameter relative to frame.
- EYES: exactly two solid black dots. Never three, never any whites.
- MOUTH: one curved stroke. Neutral flat, worry down-arc, conviction up-arc.
- LIMBS: uniform black strokes, dot hands, dot feet. Two arms, two legs, always.
- YOU (the viewer character): plain stick figure, white circle head, no hair,
  no clothing unless the beat specifies outerwear. Beard, hat or coat must be
  identical across every frame that has it.
- THREAT: flat matte silhouette figures, no detail, no gore, no visible
  wounds, same dot eyes. Never shown biting.
- SET DRESSING: lowest priority. Furniture and props as flat blocks only.

## 3. Story-state rules that must appear in every prompt

- Hour 0–3: street daylight, ordinary world still standing, no damage yet.
- Hour 3–12: interior bathroom and kitchen, tap still running, water levels rising.
- Hour 12–24: night, interior, curtains closed, one low warm light only, no fire.
- Hour 24–48: interior daylight and dusk, doors blocked with one heavy object.
- Hour 48–72: exterior street, small groups at a distance, aid point crowd.
- Closing beats: dawn light, quiet interior, no threat on screen.
- Time cannot move backwards in a scene without a stated beat that says so.

## 4. Anchor recipe

Every generation call:

1. `images=[refs/anchor_character.png, refs/anchor_location_<loc>.png, optional prior approved frame]`
2. TOKEN BLOCK above, byte-identical.
3. One scene line, written as a camera instruction, not a story summary.
4. The story-state rule for that hour range.
5. The same NEGATIVE block, byte-identical.

Never paraphrase the token block. Never add style adjectives to a scene line.

## 5. Moderation log

First block: record the blocked word and the replacement used, then keep using
the replacement for the rest of the episode.

| Date | Frame | Blocked input | Replacement | Result |
|---|---|---|---|---|
| — | — | none yet | — | — |

Known risky vocabulary and the safe swap already adopted: bite -> contact /
the moment of contact; blood -> flat color-splotch; corpse -> figure; attack
-> approached; gore -> never named.

## 6. Approved anchors

| Anchor | File | Prompt (verbatim) | Approved |
|---|---|---|---|
| Character | `refs/anchor_character.png` | pending | — |
| Location A | `refs/anchor_location_room.png` | pending | — |
| Location B | `refs/anchor_location_street.png` | pending | — |
