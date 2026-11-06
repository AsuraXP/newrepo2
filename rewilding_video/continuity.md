# Continuity — The Rewilding

Status: ANCHOR LOCK DRAFT 2026-11-06 — awaiting user approval of winning anchor + worker deployment (STATE 4 STOP).

## LOCKED STYLE & CHARACTER (copy/paste VERBATIM into every prompt)

**Style & Medium:**
Hand-drawn 2D stick-figure cartoon — thick wobbly black ink outlines, round white head, dot eyes with expressive black brows, thin black stick body and limbs with small oval hands and simple stick feet, painterly gouache-style brush shading with subtle film grain, warm-cool color separation (amber practical light vs cold blue-gray mist), muted earthy palette, high-contrast readable silhouettes, no photorealism, no 3D render, no anime.

**Protagonist ("You" — the ranger):**
round white head, three-strand hair sprig under a weathered olive wide-brim hat, heavy-lidded tired dot eyes under straight brows; thin black oval torso; STICK arms and legs with oval hands and flat stick feet; olive-green ranger vest over charcoal shirt, olive trousers, small olive backpack, chest tag reading SECTOR SEVEN, brass tally counter on belt; dart gun holstered, ALWAYS with the red UNFIRED tape intact; dark boots.

**The calf ("she"):**
round white head, smaller than adult hands, single hair sprig, huge bright dot eyes, enormous brave smile; oversized red flannel work jacket with painted-on check/plaid, sleeves rolled and cupped over her hands; tiny stick limbs; barefoot. NEVER shown older than two. NEVER harmed.

**The turned ("the herd"):**
round pale blue-gray heads, blank soft-white dot eyes (never red), tattered layered coats in ash gray, slate and bark brown, hunched posture, heels dragging toe-clawing gait; move ONLY at a slow walk; NEVER run, NEVER speak, NEVER attack. No wounds, no blood, no rot — always weathered and dry.

## INVARIANTS
- Palette anchors: cream/ivory heads; ink black lines; olive ranger gear; red flannel for the calf (ONLY warm small note in herd shots); fog blue-gray; moss and pine green; firelight/porch amber for warm scenes.
- Line weight: thick, wobbly, hand-inked (approx 4–8 px at 1280px wide). No ruler-straight vectors.
- Characters are stick figures with ROUND heads — no necks, no noses, no mouths except simple curved smiling/frowning strokes. No fingers (oval mitten hands only).
- Wanderers NEVER glow, NEVER bite, NEVER chase. Tension = stillness and numbers, never pursuit.
- Cameras: LOCKED OFF per repo Rule 8. No Ken Burns, no zoom, no drift. Word-reactive cuts come from editing; every frame is a still composition.
- Text in frame: diegetic signage/ledger/manual pages only, SHOUTY block type, UK-spelling free, max ~5 words per surface. Never invent story-breaking text (no names of the calf, ever).
- Fire and candlelight ONLY as warm light sources; flames never harm anyone.
- The calf's origin is NEVER shown or explained. No flashbacks to her birth. No pregnant turned figure. Ever.

## LOCATION REFERENCE SCOPE
- `character_ref` (anchor): attach whenever the ranger, the calf, or the herd is framed. Non-negotiable.
- `location_ref`: attach ONLY while the beat occurs in that continuous setting:
  - ranger station interior/porch (slides 1, 14, 15)
  - creek crossing (slides 2, 5, 6)
  - upper valley / ridge (slides 8, 9, 10, 11, 12)
  When the story cuts to a NEW environment (e.g., fog line above timberline slide 13), do NOT attach the previous location_ref — generate a fresh background in the locked style instead.

## CONTENT MODERATION LOG (blocked → replacement)
| Blocked in prompts | Replacement |
|---|---|
| zombie / undead / corpse | the turned / wanderers / hollow-eyed figures / the slow ones |
| blood / gore / wound / mutilation | nothing; or "flat dark splotch, dry and matte" (used once at chunk 055) |
| kill / attack / bite / lunge | guard / press close / converge / herd around / walk with |
| mass grave / body pile | the resting fields (unused) |
| murder / violence spectacle | dread via stillness, distance, counting |
| baby / infant (photoreal weight) | toddler / the calf / small shape (always stylized stick figure) |
| "pregnant turned woman" | NEVER GENERATED — story forbids it |
| fire that harms | warm light only |
| red glowing eyes | blank soft-white dot eyes |
| chase / run (wanderers) | slow walk, tidal gait |

## COMPOSITION RULE (barriers/glass)
Rare in this story (window beats only): camera on the viewer's side, figures seen from behind or in profile, hands on the viewer's side of the surface, interior visible through it. Never compose figures pressing faces/hands against the camera-side of glass.

## ANCHORS (winning candidates 2026-11-06, user's style refs + 3 test generations)
- test_anchor_ranger_dawn.png — station porch at dawn, radio in hand, ruined highway in mist (used in response; user approval pending)
- test_anchor_herd_crossing.png — creek-bed crossing, adult stooped over flannel bundle (the "04:17" photo made flesh)
- test_anchor_calf_smile.png — toddler in oversized red flannel smiling up, wanderers fog-blurred behind
- User style refs (verbatim anchors of look): refs/ref-couch.png (couch mood, warm interior), refs/ref-campfire.png (fire-warm night blues, cave), refs/ref-mark.png (pure mark-making, yellow sun disc)

## DECLARED EXCEPTIONS
(none yet — worker phase will log here and in STATE.md)

## USER DECISIONS 2026-11-06
- All three test anchors APPROVED as style/character anchors: test_anchor_ranger_dawn.png, test_anchor_herd_crossing.png, test_anchor_calf_smile.png. (NOT location anchors — locations change per scene.)
- Location handling: each NEW continuous environment = fresh background generated in the locked style; location_ref attached ONLY within its own continuous setting (station porch/interior; creek crossing; upper valley/ridge; Hawk's Back; fog line above timberline). character_ref always.
- Worker packets must assign the actual prompts + counts to each worker (not just row ranges). See rewilding_video/worker_packet_1.md .. worker_packet_3.md.
