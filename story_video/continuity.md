# Continuity

Status: user approved both generated character and location references as production anchors. User-supplied images in this directory remain visual inspiration.

## Candidate invariant blocks

Copy these verbatim into production prompts after approval; revise if the user requests changes.

**Style:** Warm textured hand-inked 2D illustration, expressive simple round-headed stick figures, irregular charcoal outlines, muted blue and amber palette, cinematic soft lighting, 16:9, no captions, no legible text, no watermark.

**Main character:** Main character: an adult, gender-neutral stick figure with a large round ivory face, two small black oval eyes, expressive brows, a tiny three-stroke black hair tuft, a thin charcoal stick body and limbs, and a distinctive muted teal scarf.

**Waiting room state:** Muted blue sofa, warm cream walls, honey-colored wooden floor, side table with lit amber lamp, three waiting chairs, and a closed dark-wood door. Door remains closed unless the scene explicitly requires otherwise. The waiting room is an imaginary metaphor, not a literal brain interior.

**Task visitors:** Small, distinct round-headed stick figures representing unfinished tasks, each with two thin legs, separate limbs, and a simple task prop. Queue tickets may carry one or two dots as visual number markers, but no written digits. `frames/beat03m01.png` is the accepted visitor design reference; use it as the optional prior frame when useful. Never represent the waiting room as established neuroscience.

**Drift to correct in subsequent prompts:** `beat02m05` visitors wear small white tunic-like torsos, whereas the `beat03m01` visitor anchor has an unfilled stick-line torso. Prefer the anchor's unfilled stick-line torso. `beat02m06` has an extra cup on the side table while the protagonist also holds a cup; the `character_test.png` anchor shows a single held cup. Keep only one cup in future frames.

**Reference recipe:** provide both `refs/character_test.png` and `refs/location_test.png` to frame generation; optionally add a prior approved frame where continuity benefits. Rework each draft CSV prompt before generation to include the applicable invariant blocks verbatim and explicit scene state.

## Character test: `refs/character_test.png`

Exact prompt:

> Create one standalone 16:9 character reference for an original educational explainer, using the attached images only as visual style inspiration. Warm textured hand-inked 2D illustration, expressive simple round-headed stick figures, irregular charcoal outlines, muted blue and amber palette, cinematic soft lighting, 16:9, no captions, no legible text, no watermark. Main character: an adult, gender-neutral stick figure with a large round ivory face, two small black oval eyes, expressive brows, a tiny three-stroke black hair tuft, a thin charcoal stick body and limbs, and a distinctive muted teal scarf. Show this one character sitting in three-quarter view on a muted blue sofa, holding a warm tea cup, with a slightly worried but gentle expression. Keep anatomy clean, hands simple, silhouette immediately readable, textured cream wall and restrained warm lamplight. No other people, no text, no logos.

## Location test: `refs/location_test.png`

Exact prompt:

> Create one standalone 16:9 location reference for an original educational explainer, using the attached images only as visual style inspiration. Warm textured hand-inked 2D illustration, expressive simple round-headed stick figures, irregular charcoal outlines, muted blue and amber palette, cinematic soft lighting, 16:9, no captions, no legible text, no watermark. Show an inviting, slightly surreal waiting room representing unfinished tasks: muted blue sofa, warm cream plaster walls, honey-colored wooden floor, a small side table with a lit amber lamp and a tea cup, three simple empty waiting chairs, and a closed dark-wood door. Camera at eye level in a wide view, clear spatial layout, cozy yet gently mysterious. A few blank paper tickets and an envelope sit on a small table; no people or characters, no writing, numbers, symbols, logos or watermarks.

Inputs to both tests: `refs/cozy-textured.png`, `refs/cinematic-storytime.png`, `refs/expressive-comic.png`.

## Moderation and exceptions

No moderation blocks or declared exceptions.
