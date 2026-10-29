# Continuity

## User-supplied style references
- `refs/style_ref_01.png`
- `refs/style_ref_02.png`
- `refs/style_ref_03.png`

These establish the requested hand-drawn stick-figure look. They are not generated character/location anchors.


## Narrative design cues — pending visual anchor approval
- Protagonist: green windbreaker, cheap enamel anchor pin, red backpack, yellow muster wristband.
- Lina: thirteen years old, small build, two dark braids, purple hoodie; carries flashlight and spare radio during the rescue.
- Mara: young deck officer, cropped black braid, white uniform, silver radio, brass key ring.
- Meridian: fourteen decks, glass atrium elevators, orange lifeboats, blue crew doors, forward observation lounge with steel shutters.

These are script details, not yet approved visual invariants.

## Approved anchors
- **Winning style/reference anchor: B** — `refs/test_02_atrium.png`, explicitly selected by the user.
- Character reference derived from B: `refs/anchor_characters.png` (crop only; no new image content).
- Atrium location reference: `refs/anchor_atrium.png` (exact copy of B).
- Terminal location reference: `refs/anchor_terminal.png`, generated from B and visually QC-approved before batch 1.
- Promenade location reference: `refs/anchor_promenade.png`, generated from B with terminal port geography and visually QC-approved before batch 6's departure frames.
- Additional location anchors may be generated with B as the style reference before their first scene; they never replace B's style or character rules.
- Anchor recipe for every episode frame: `images=[refs/anchor_characters.png, refs/anchor_<location>.png, optional_prior_approved_frame]`.
- Exact B generation prompt is preserved below under `Style-test candidate prompts`.

## Invariants
- Palette: warm off-white paper, uneven black ink, muted teal-gray architecture, green windbreaker, purple hoodie, white uniform, blue crew doors, restrained blue water, and desaturated gray infected.
- Line weight: thick uneven black outer contours; very thin black stick limbs; flat muted fills; subtle dry-paper texture; no photorealism or 3D.
- Protagonist: gender-neutral young stick figure, oversized white round head, tiny oval eyes, green windbreaker, small enamel anchor pin, red backpack, yellow muster wristband.
- Lina: small thirteen-year-old stick figure, oversized white round head, two dark braids, purple hoodie. Flashlight and spare radio appear only after Mara gives them to her.
- Mara: oversized white round head, cropped black hair with a single dark over-shoulder braid, white deck-officer uniform, silver radio, brass key ring. One sleeve is torn only after the rescue.
- Props: red backpack, yellow wristband, anchor pin, blue crew doors, orange lifeboats, steel shutters, flashlight, silver radios, brass keys, and wheeled drinks cart must keep their established shapes and colors.
- Creature rules: desaturated gray-green round heads, cloudy pale dot eyes, uneven posture, torn muted clothing, non-graphic action, no blood or wound detail.
- Visual SFX: hand-drawn motion lines, abstract impact bursts, smoke, sea spray, flickering light, and dramatic shadows only when motivated by the exact micro-beat; no comic-book captions or onomatopoeia text.
- Glass/barrier composition: camera on the viewer's side; figures seen from behind; hands on the viewer's side of the surface; interior visible through it.
- Story state: every frame prompt must state the current location, door/shutter state, available props, character wardrobe state, and pursuit state. Never show a later action early.
- Set dressing is lower priority than character, prop, palette, line-weight, and story-state fidelity.

## Moderation substitutions
- `test_03_pool_action.png`, first block: exact triggering token was not reported; blocked action clause `swings a red backpack into the chest of` replaced with `braces a red backpack between himself and`. No other prompt clause changed.
- `test_03_pool_action.png`, second block: exact triggering token was not reported; negative phrase `no blood or wounds` replaced with `flat muted color shapes and no injury detail`.
- `test_03_pool_action.png`, third block: direct-contact backpack action with Lina beside the threat replaced by a non-contact drinks-cart evasion composition; Lina and Mara are safely inside the lounge doorway and distant gray figures replace the close infected passenger.

## Style-test QC
- `test_03_pool_action.png`: `Mara dark round head vs test_02_atrium white round head`; rejected character drift and changed only the Mara appearance clause, adding `test_02_atrium.png` as her visual reference. Original preserved as `test_03_pool_action_reject.png`.


## Style-test candidate prompts — pending user selection

### A — `refs/test_01_gangway.png`
Reference images: `refs/style_ref_01.png`, `refs/style_ref_02.png`, `refs/style_ref_03.png`.

```text
Create one standalone 16:9 style-test frame for an animated story. Use the three supplied images only as visual style references, not as scenes to copy. Scene: outside a cruise terminal on the gangway of the immense white cruise ship Meridian. A gender-neutral young stick-figure protagonist wears a green windbreaker with a tiny enamel anchor pin, a red backpack, and a yellow wristband. Beside them is their small thirteen-year-old sister Lina with two dark braids and a purple hoodie. They look up at the ship while distant emergency smoke and subtle hand-drawn siren-ray marks create tension on land. Full-body, clean character silhouettes, gangway and ship scale clearly readable. Hand-drawn 2D stick-figure animation matching the supplied user references: oversized round white heads, thick uneven black ink contours, tiny oval eyes, minimal expressive mouths, thin black stick limbs, simple flat muted colors, sparse hand-inked environments, subtle dry-paper texture, expressive silhouettes, wide 16:9 composition; no photorealism, no 3D, no glossy shading, no readable text, no logos, no watermarks, no gore. Visual SFX are hand-drawn within the artwork when the action calls for them: motion lines, impact bursts, smoke, sea spray, flickering light, and dramatic shadows; never use comic-book captions or onomatopoeia text.
```

### B — `refs/test_02_atrium.png`
Reference images: `refs/style_ref_01.png`, `refs/style_ref_02.png`, `refs/style_ref_03.png`.

```text
Create one standalone 16:9 style-test frame for an animated story. Use the three supplied images only as visual style references, not as scenes to copy. Scene: inside the Meridian's luxurious multi-level cruise atrium during the first panic. Glass elevators, curved staircases, a piano, and an abstract sculpture surround a clearly visible blue crew door. Mara, a young deck officer with a cropped black braid, white uniform, silver radio, and brass key ring, blows a whistle and points toward the door. The green-windbreaker protagonist with red backpack and their purple-hoodie sister Lina with two dark braids follow her. Background passengers rush in opposing directions. Use restrained hand-drawn motion lines and flickering-light marks, with no graphic injury. Hand-drawn 2D stick-figure animation matching the supplied user references: oversized round white heads, thick uneven black ink contours, tiny oval eyes, minimal expressive mouths, thin black stick limbs, simple flat muted colors, sparse hand-inked environments, subtle dry-paper texture, expressive silhouettes, wide 16:9 composition; no photorealism, no 3D, no glossy shading, no readable text, no logos, no watermarks, no gore. Visual SFX are hand-drawn within the artwork when the action calls for them: motion lines, impact bursts, smoke, sea spray, flickering light, and dramatic shadows; never use comic-book captions or onomatopoeia text.
```

### C — `refs/test_03_pool_action.png`
Reference images: `refs/test_02_atrium.png`, `refs/style_ref_01.png`, `refs/style_ref_02.png`, `refs/style_ref_03.png`.

```text
Create one standalone 16:9 style-test frame for an animated story. Use the supplied images only as visual style references, not as scenes to copy. Scene: on the Meridian's wet pool deck beside a white canopy and scattered loungers, with blue ocean beyond the railing. The green-windbreaker protagonist, wearing a yellow wristband and red backpack, kicks an empty wheeled drinks cart across the wet tiles toward an unoccupied lounger. The cart tips the lounger sideways with a small abstract hand-drawn impact burst and motion lines. Lina, small with two dark braids and a purple hoodie, and Mara, with the same white oversized round head and cropped black braid as the supplied atrium character reference, wearing a white deck-officer uniform, wait safely inside the open observation-lounge doorway and wave the protagonist forward. Two fully clothed, desaturated gray stick figures are distant background silhouettes with uneven posture, separated from the protagonists by deck furniture. Add light hand-drawn sea spray and keep every silhouette simple and readable. Hand-drawn 2D stick-figure animation matching the supplied user references: oversized round white heads, thick uneven black ink contours, tiny oval eyes, minimal expressive mouths, thin black stick limbs, simple flat muted colors, sparse hand-inked environments, subtle dry-paper texture, expressive silhouettes, wide 16:9 composition; no photorealism, no 3D, no glossy shading, no readable text, no logos, no watermarks, no gore. Visual SFX are hand-drawn within the artwork when the action calls for them: motion lines, impact bursts, smoke, sea spray, flickering light, and dramatic shadows; never use comic-book captions or onomatopoeia text.
```

## Additional approved location-anchor prompts

### Terminal — `refs/anchor_terminal.png`
Reference image: `refs/anchor_atrium.png`.

```text
Create one standalone 16:9 location-reference image for the same animated story, using the supplied approved atrium anchor only for its visual style. Location: exterior cruise-terminal gangway beside the immense white hull of the cruise ship Meridian. Show the open gangway door, metal railings, luggage barriers, abstract emergency-screen shapes with no legible writing, the distant pier and abandoned cars, and restrained hand-drawn black smoke rising far beyond the terminal. No named characters in the foreground; keep the location clear for later character placement. Hand-drawn 2D stick-figure animation matching the supplied user references: oversized round white heads, thick uneven black ink contours, tiny oval eyes, minimal expressive mouths, thin black stick limbs, simple flat muted colors, sparse hand-inked environments, subtle dry-paper texture, expressive silhouettes, wide 16:9 composition; no photorealism, no 3D, no glossy shading, no readable text, no logos, no watermarks, no gore. Visual SFX are hand-drawn within the artwork when the action calls for them: motion lines, impact bursts, smoke, sea spray, flickering light, and dramatic shadows; never use comic-book captions or onomatopoeia text.
```

### Promenade — `refs/anchor_promenade.png`
Reference images: `refs/anchor_atrium.png`, `refs/anchor_terminal.png`.

```text
Create one standalone 16:9 location-reference image for the same animated story. Use the first image only for its approved hand-drawn style, palette, and line work, and the second only for distant port geography; do not copy either image's characters or action. Location: the Meridian's open exterior promenade deck while still near port. A warm cream deck runs beside a muted teal-gray ship wall on the left and a long white metal railing on the right. Beyond the railing are restrained blue water, a receding concrete pier with a few tiny abandoned cars, and a distant coastal city skyline. Include two orange lifeboats suspended below the outer railing and one closed cream life-jacket storage locker set into the ship wall, marked only with a simple icon-only life-jacket shape and no writing. Add one thin distant black smoke plume far above the city, keeping the deck itself calm and safe. No named characters, no passengers, no infected, no motion, no cheering, and no foreground props; keep the location clear for later character placement. Wide maritime geography must make the strip of water between ship and pier unmistakable. Hand-drawn 2D stick-figure animation matching the supplied user references: oversized round white heads, thick uneven black ink contours, tiny oval eyes, minimal expressive mouths, thin black stick limbs, simple flat muted colors, sparse hand-inked environments, subtle dry-paper texture, expressive silhouettes, wide 16:9 composition; no photorealism, no 3D, no glossy shading, no readable text, no logos, no watermarks, no gore. Visual SFX are hand-drawn within the artwork when the action calls for them; here only the distant smoke and a few restrained hand-inked water lines, never comic-book captions or onomatopoeia text.
```

## Batch 1 QC — 8 accepted
- Accepted: `beat01m01`, `beat01m02`, `beat01m03`, `beat01m04`, `beat01m05`, `beat01m06`, `beat01m07`, `beat02m01`.
- Reject: `beat01m04_r1` — readable `BOARDING PASS` and `SAVINGS` plus pseudo-writing violated the no-readable-text/gibberish floor. Changed only the close-up prop clause to a plain glass coin jar and completely blank cream cards; replacement `beat01m04` passed.
- Contact sheet: `frames/contact_sheets/batch01.jpg` includes all eight accepted frames and the reject.
- New anchor: `refs/anchor_terminal.png`.
- Declared exceptions: none.

## Batch 2 QC — 8 accepted
- Accepted: `beat02m02`, `beat02m03`, `beat02m04`, `beat02m05`, `beat02m06`, `beat02m07`, `beat02m08`, `beat02m09`.
- Rejects: none; repair budget 0 / 2 used.
- Prop checks: `beat02m08` shows exactly two water bottles and one flashlight, with no snacks or radio; `beat02m09` adds exactly three blank snack packets while retaining the two bottles and flashlight.
- Contact sheet: `frames/contact_sheets/batch02.jpg`.
- New anchors: none.
- Declared exceptions: none.

## Batch 3 QC — 8 accepted
- Accepted: `beat02m10`, `beat02m11`, `beat02m12`, `beat02m13`, `beat02m14`, `beat02m15`, `beat02m16`, `beat02m17`.
- Reject: `beat02m17_r1` — `protagonist and crew hands realistic skin-toned vs anchor B solid black mitten silhouettes`. Changed only the hand-style clause to require solid black mitten hands for every visible person; replacement `beat02m17` passed.
- Contact sheet: `frames/contact_sheets/batch03.jpg` includes the reject.
- New anchors: none.
- Declared exceptions: none.

## Post-checkpoint user review — `beat02m16` repaired
- Reject: `beat02m16_r1` — the user flagged the cars-and-smoke terminal background as confusing in the playful sailor-memory shot. The original is preserved under `frames/rejects/`.
- Changed only the location clause to a plain cream sky and clean ship hull, explicitly excluding the terminal, cars, smoke, and disaster effects. Character blocking, anchors, action, and all other prompt language stayed unchanged.
- Replacement `beat02m16` passed: sailor pose and Lina's thumbs-up remain clear against the clean hull; style, palette, costumes, and solid black mitten hands match the anchors.
- Updated `frames/contact_sheets/batch03.jpg` now includes both `beat02m16_r1` and `beat02m17_r1` rejects.

## Batch 4 QC — 8 accepted
- Accepted: `beat02m18`, `beat02m19`, `beat02m20`, `beat02m21`, `beat02m22`, `beat02m23`, `beat02m24`, `beat02m25`.
- Reject: `beat02m19_r1` — duplicated the green-windbreaker/red-backpack protagonist in the refused-entry cutaway. Changed only the camera clause to a family-and-security cutaway with both siblings entirely out of frame and no green windbreaker, red backpack, yellow wristband, anchor pin, or purple hoodie visible; replacement `beat02m19` passed.
- Action/prop checks: `beat02m20` uses an abstract red-triangle medical alert without readable text; `beat02m23` uses wristband icons without readable text or numbers; `beat02m24` shows an icon-only emergency route on the phone.
- Contact sheet: `frames/contact_sheets/batch04.jpg` includes all eight accepted frames and the reject.
- Repair budget this turn: 2 / 2 used across the `beat02m16` and `beat02m19` repairs.
- New anchors: none.
- Declared exceptions: none.

## Batch 5 QC — 8 accepted
- Accepted: `beat02m26`, `beat03m01`, `beat03m02`, `beat03m03`, `beat03m04`, `beat03m05`, `beat03m06`, `beat03m07`.
- `beat03m01` is the approved calm-atrium prior frame for the batch. It retains the established geography without copying anchor B's panic action or Mara.
- Reject: `beat03m05_r1` — pseudo-lettering on the yellow wristband violated the no-readable-text/gibberish floor. Changed only the wristband clause to require a completely blank band; replacement `beat03m05` passed.
- Rejects: `beat03m06_r1` and `beat03m06_r2` — both scale-shot attempts retained pseudo-lettering on the yellow wristband despite a wristband-clause-only repair. Both originals are preserved. With a fresh repair allowance, changed only the wristband visibility clause: the left-wrist band is occluded by the torso/backpack and the visible right cuff is plain green. Replacement `beat03m06` passed with no lettering and the required atrium scale.
- `beat03m07` passed as a single continuous restaurant-and-theater architectural view with icon-only plaques, no siblings, and no clinic or cabins shown early.
- Contact sheet: `frames/contact_sheets/batch05.jpg` includes all eight accepted frames and all three rejects.
- Repair budget final turn: 1 / 2 used; the batch required two turns because the earlier image and repair caps were reached.
- New anchors: none.
- Declared exceptions: none.

## Batch 6 QC — 8 accepted
- Accepted: `beat03m08`, `beat03m09`, `beat03m10`, `beat04m01`, `beat04m02`, `beat04m03`, `beat04m04`, `beat04m05`.
- New location anchor: `refs/anchor_promenade.png`, QC-approved before `beat04m01`. It establishes the cream promenade, white railing, two orange lifeboats, icon-only locker, blue water gap, receding pier, and distant city without characters or readable text; exact prompt and references are logged above.
- `beat03m09` is an explicitly unpopulated storybook metaphor of the city-like ship floating, not a new physical event. `beat03m10` introduces the horn only through offscreen resonance curves, glass jitter marks, and the siblings' reactions.
- Departure timing checks: no cheering occurs through `beat04m05`; `beat04m03` shows exactly three abandoned cars and five distant runners; `beat04m04` is a non-graphic city-smoke cutaway; `beat04m05` emphasizes the widening water before the next moment's cheering.
- Rejects: none; repair budget 0 / 2 used. Nine of ten image slots used, including the new location anchor.
- Contact sheet: `frames/contact_sheets/batch06.jpg`.
- Declared exceptions: none.

## Batch 7 QC — 8 accepted
- Accepted: `beat04m06`, `beat04m07`, `beat04m08`, `beat04m09`, `beat04m10`, `beat04m11`, `beat04m12`, `beat04m13`.
- Reject: `beat04m11_r1` — the open locker contained extra jackets instead of the established six, and both siblings smiled instead of remaining solemn. Changed only the jacket-count/arrangement and expression clauses; replacement `beat04m11` passed with exactly six jackets in two rows of three, flat mouths, and the pool secondary to the safety equipment.
- Prop/timing checks: `beat04m07` shows eight hanging boats in two staggered rows; `beat04m08` keeps the safety card inside a thought cloud with exactly three pictograms and no writing; `beat04m09` shows exactly six jackets and no removal; `beat04m13` keeps the coastline individually readable and does not show the next moment's thin burning line.
- `beat04m12` first returned a no-image generation response with no artifact; the identical prompt retry succeeded and passed, consuming no QC repair.
- Contact sheet: `frames/contact_sheets/batch07.jpg` includes all eight accepted frames and the reject.
- Repair budget: 1 / 2 used; nine successful image slots used.
- New anchors: none.
- Declared exceptions: none.
