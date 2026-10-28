# Continuity — THE LIST

Style authority: owner's three reference frames, copied into `refs/`.
Everything below is measured off those images, not invented.

---

## 1. STYLE BLOCK — copy VERBATIM into every prompt. Never rephrase, never abbreviate.

```
Flat 2D cartoon illustration in hand-drawn stick-figure animation style: solid
black outlines of uniform weight with a slightly wobbly hand-drawn edge, flat
muted fills, no gradients, no texture, no shading, no cast shadows, no highlights.
Characters are simple stick figures with a round white head, two small black dot
eyes, a thin straight mouth line, and single-stroke black limbs with rounded ends.
Clean empty background planes, minimal detail, wide 16:9 composition with generous
negative space.
```

## 2. Measured invariants

| Invariant | Value | Measured from |
|---|---|---|
| Outline weight | uniform 5 px at 1192 px image width = **0.42% of frame width** | stroke histogram, both refs peak at 4–5 px |
| Head diameter | **13.9% of frame width** | figure ref, 166 px / 1192 px |
| Limb stroke | same weight as outline, **5 px**, rounded cap | figure ref |
| Ink colour | `#010101` | couch ref sample |
| Head fill | `#f8f3dc` ivory, bleaches toward `#ffffff` on bright grounds | both refs |
| Eyes | two solid black dots, no whites, no brows except when emoting | figure ref |
| Mouth | one thin line; curve up = calm, straight = flat, small o = speaking | figure ref |
| Perspective | flat elevation, no vanishing point, camera square to the plane | all three refs |
| Line wobble | gentle, ~1–2 px, never jittery or sketchy-scratchy | all three refs |

## 3. PALETTE LOCK

| Role | Hex | Notes |
|---|---|---|
| Ink | `#010101` | all outlines, all limbs, all hair |
| Head / paper | `#f8f3dc` | heads, and any paper prop |
| Wall, dawn | `#e5d3ba` | interior + exterior planes, warm beige |
| Wall, night | `#5e5653` | same planes, stone grey after dark |
| Floor / wood | `#75503b` | boards, road, bridge deck |
| Furniture grey | `#6b767f` | sofas, cars, metal, tower equipment |
| Accent yellow | `#f0c667` | cloth, laundry, the blanket |
| Dog brown | `#473425` | Ash's back patch, Ash's ears |
| **Warm accent orange** | `#ff8421` | **reserved:** fire, the tower lamp, the record light. The only saturated colour in the film. |
| Night sky | `#1e2d50` | windows, sky, open water |

**Rule:** orange appears exactly where something is still *powered or burning*.
It is the film's only saturated colour. Nothing else may use it.

## 4. CHARACTER — THE SURVIVOR

```
the survivor: a male stick figure, round white head, two black dot eyes, thin
straight mouth, six short black hair strokes on top of the head, single-stroke
black limbs with rounded ends, wearing a flat charcoal-grey hooded jacket worn
open over a black torso stroke, flat olive-brown trousers on the leg strokes,
dark boots, one shoulder-strap line across the chest. No other detail.
```

Male is carried by the flat chest, the broad shoulder line, the short hair
strokes, and the jacket — never by muscle, jaw, or facial features. He has no
nose, no eyebrows at rest, and no iris.

He is **never named in prompts or filenames.** In narration he is "you". His name
is spoken once, in the last eight beats, and is never written down here.

## 5. CHARACTER — ASH

```
Ash: a small stick-figure dog, round white head, two black dot eyes, single-stroke
black legs and tail with rounded ends, two flat brown #473425 floppy ear shapes,
one flat brown #473425 patch across the back, thin straight mouth line. No collar.
```

Ash is roughly **half the survivor's height at the shoulder**. He is a partner:
never injured, never comic, never carried.

## 6. LOCATION — THE THIRD FLOOR (home)

```
a bare third-floor apartment room: flat beige #e5d3ba wall planes, a tall window
with flat #1e2d50 night behind it, a bare mattress on a brown #75503b floorboard
plane, hand-scratched pencil rules on the wall beside the window. Nothing else.
```

## 7. LOCATION — THE TOWER (destination)

```
a small radio transmitter room: flat grey #6b767f equipment boxes on a low shelf,
a desk with a microphone on a short stand, a cassette deck, a bare hanging bulb,
one small orange #ff8421 record light. Flat #5e5653 walls, one tall window.
```

## 8. RECURRING PROPS — locked

| Prop | Rule |
|---|---|
| Pencil | short stub, ivory `#f8f3dc` barrel, black point. Never long. |
| Rifle | drawn as a plain black single-stroke silhouette, slung, never aimed |
| Pry bar | one black line, no detail, always at his right side |
| Rules on wall | scratched lines, illegible — **never render readable text** |
| The list / logbook | open paper `#f8f3dc`, ruled columns, no readable names |
| Tower lamp | orange `#ff8421`, always mid-rotation (motion lines, 2 short arcs) |

**Text rule:** no frame may contain legible writing. Every written surface is
scratches, ruled lines, or shapes. This kills gibberish-text defects at the source.

## 9. TIME OF DAY

Fixed progression, monotonic. Never jumps backwards.

| Act | Beats | Light |
|---|---|---|
| 1 — waking | 1–15 | pre-dawn, wall `#e5d3ba`, sky `#1e2d50` still dark |
| 2 — the number | 16–29 | dawn, wall `#e5d3ba`, sky lifting to `#8d8378` |
| 3 — Calder St | 30–59 | overcast day, flat `#e5d3ba` sky, no sun disc |
| 4 — the bridge | 60–71 | dusk, wall/plane `#75503b`, sky `#1e2d50` |
| 5 — the tower | 72–91 | night, wall `#5e5653`, sky `#1e2d50`, orange lamp on |

## 10. ANCHORS

| Anchor file | Made from | Coverage |
|---|---|---|
| `refs/style_indoor_couch.png` | owner ref — flat interior + full figure | style authority |
| `refs/style_figure_gesture.png` | owner ref — full figure, proportions | style authority |
| `refs/style_night_cave.png` | owner ref — night palette, hair strokes | style authority |
| ✅ `refs/anchor_survivor.png` | test 1, accepted first pass | all survivor beats |
| ✅ `refs/anchor_ash.png` | test 2b, accepted on repair r1 | all Ash beats |
| ✅ `refs/anchor_tower.png` | test 3, accepted first pass | all tower beats |
| ✅ `refs/anchor_thirdfloor.png` | test 4, accepted first pass | all home beats |

### Style test log

| Test | Result | Diagnosis |
|---|---|---|
| test 1 — survivor, empty street | **ACCEPT** | Six hair strokes, 5 px uniform ink, strap, olive trousers, boots, pry bar. Palette exact. |
| test 2 — survivor + Ash walking | **REJECT** | The brown back-patch migrated onto Ash's skull and face as a mask. Reads as injury. Violates "Ash is never injured." |
| test 2b — Ash repair r1 | **ACCEPT** | Brown confined to two ear shapes + one back patch. Head clean white. |
| test 3 — tower room | **ACCEPT** | Mic, deck, ruled notebook (no legible writing), exactly one orange light, unlit bulb. |
| test 4 — third floor | **ACCEPT** | Scratches read as tally marks, illegible. Full-bleed. |

**Permanent clause added after test 3:** `Full-bleed: the artwork fills the entire
frame edge to edge, no border, no frame line, no vignette.` Test 3 and test 4's
first attempts framed the art with a cream border, which would bake a letterbox
into every video frame. It is now welded into the style block for all 89 prompts.

## 11. MODERATION SUBSTITUTIONS

First block recorded. The trigger was **stacked negation about a body** ("never on
the head, never on the face… no splotches, no markings, no injury") applied to a
dog's head — describing an injury even in order to forbid it. The fix is not a
softer word, it is **positive phrasing**: state where the colour *is*, drop the
list of where it isn't.

| Blocked phrasing | Working replacement | First seen |
|---|---|---|
| "the head stays entirely white apart from the two dot eyes and the mouth line, no splotches, no markings, no injury" | "The dog is a simple stick-figure cartoon: perfectly round smooth white head, two small black dot eyes, one thin straight mouth line… Colourful and friendly, like a children's book mascot." | test 2b attempt 1 |

Standing guidance: violent impact verbs also tend to block in this style. Keep the
beat with "pressed against with impact burst lines", "the shape tips past the rail",
"flat colour splotch". Nothing gory is scripted. **Never** describe a wound in order
to prohibit it — describe the intact shape instead.

## 12. DELIBERATE COMPOSITIONS

- **Figures behind glass** (tower window, laundromat glass, shop fronts): camera on
  the *viewer's* side, figures seen from behind, hands on the near side of the
  surface, interior visible through it.
- **Crowd beats** (41, 47): figures mid-ground only, backs turned, no faces.
  Faces cost the most and drift the fastest.
- **The bridge** (60–67): deck as a flat brown band, water flat `#1e2d50`, horizon
  raised, no perspective lines.
