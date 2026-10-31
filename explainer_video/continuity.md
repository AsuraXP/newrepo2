# Continuity ledger

Status: user selected a hand-drawn stick-figure look and explicitly approved character and location tests as anchors.

Observed visual direction: round white or pale faces with simple expressive eyes and mouths; slender black stick limbs and hand-drawn contours; flat muted colors with restrained shading; simple compositions and sparse detail. Exact reusable tokens remain pending reference tests and approval.

## Invariants to freeze after approval

- Exact style and negative-prompt blocks, copied verbatim into every frame prompt.
- Palette, line weight, rendering texture, and aspect ratio.
- Character face, silhouette, hair, garments, and identifying props.
- Creature design and movement rules, if applicable.
- Location layout and explicit story state in every prompt.
- Set dressing is lower priority than subject and style continuity.

## Anchor recipe

Use `images=[character_ref, location_ref, optional_prior_approved_frame]` where applicable. Create the required anchors before sequence frames. Log each reference's exact prompt and path here. Never silently rephrase frozen blocks.

## Barrier composition

For figures pressing against glass, windows, or other transparent barriers: camera on the viewer's side; figures seen from behind; hands on the viewer's side of the surface; interior visible through it.

## Moderation substitutions

None yet. On the first block, record the blocked wording and the exact replacement before retrying.

## Approved references and drift checks

None yet. Compare specific quoted attributes against the approved anchor, not vague impressions.

## Reference-test attempt — image service unavailable

Both tests were attempted on 2026-10-30 using the user-supplied images `Screenshot Capture - 2026-10-28 - 08-14-25.png` and `Screenshot Capture - 2026-10-28 - 08-14-55.png`. The image service returned HTTP 403 with an account access/terms-of-use restriction for both calls; no test image was produced. This is an access error, not a content-moderation block, so no blocked word or replacement is recorded. Neither reference is approved. Do not generate sequence frames or claim an anchor exists until tests are successfully generated and explicitly approved.

Common provisional style block (not frozen):

> hand-drawn 2D stick-figure illustration, slightly irregular bold black ink contours, large round white face, simple black dot eyes and expressive small mouth, thin black stick limbs, flat muted colors, minimal soft paper texture, simple uncluttered forms.

Character test exact prompt:

> Create ONE landscape 16:9 character style reference, not a video frame or contact sheet. Match the visual language of the attached user-provided style references: hand-drawn 2D stick-figure illustration, slightly irregular bold black ink contours, large round white face, simple black dot eyes and expressive small mouth, thin black stick limbs, flat muted colors, minimal soft paper texture, simple uncluttered forms. Show one original Victorian construction worker, full body, standing in an easy-to-read three-quarter pose, wearing a dark charcoal flat cap and muted slate-blue work waistcoat; white round face and thin black arms and legs remain clearly visible. The worker holds one oversized iron bolt in one hand and a hexagonal nut in the other, looking curious. Warm cream plain background, no scenery. Consistent human anatomy: two arms, two hands, two legs. No lettering, no labels, no logos, no watermark, no gradients, no photorealism.

Location test exact prompt:

> Create ONE landscape 16:9 location style reference, not a video frame or contact sheet. Match the visual language of the attached user-provided style references: hand-drawn 2D stick-figure illustration, slightly irregular bold black ink contours, large round white face, simple black dot eyes and expressive small mouth, thin black stick limbs, flat muted colors, minimal soft paper texture, simple uncluttered forms. Show a wide architectural view of the Crystal Palace under construction in 1851 London: a long, low Victorian iron-and-glass exhibition hall with a prominent arched central transept, repeated dark iron columns and pale teal glass panels. The structure remains intact; a few tiny builders in charcoal caps and muted slate-blue waistcoats work nearby to show scale, with clearly separated limbs. Ground muted warm brown, sky warm cream, uncluttered atmosphere; no modern skyline. No lettering, no labels, no logos, no watermark, no gradients, no photorealism.

Retry: both character and location tests were retried with the exact same prompts and reference inputs; both again returned HTTP 403 account-access restriction. No images were produced.

Second user-requested retry: both reference generation calls again failed with HTTP 403 account restriction; no images generated.

Latest retry succeeded: `refs/character_test.png` and `refs/location_test.png` were generated with the exact logged prompts above and inspected. Candidate character: round white face, charcoal cap, slate-blue vest, thin black limbs, brown shoes; candidate location: intact teal-glass palace with repeated black iron arches on a warm brown ground. Both await user approval; these are not approved anchors yet.

## Approved anchors and frozen prompt blocks

User explicitly approved both reference tests. Character anchor: `refs/character_test.png`. Location anchor: `refs/location_test.png`. Exact prompts are recorded above. Both anchors must be passed as images for every frame; an optional previously approved frame may be added. The blocks below are copied verbatim to each `visuals.csv` prompt.

> STYLE: hand-drawn 2D stick-figure illustration, slightly irregular bold black ink contours, large round white face, simple black dot eyes and expressive small mouth, thin black stick limbs, flat muted colors, minimal soft paper texture, simple uncluttered forms.

> CHARACTER: Victorian construction worker with round white face, black dot eyes, charcoal flat cap, muted slate-blue waistcoat over a cream shirt, slender black arms and legs, brown shoes; match character reference exactly.

> LOCATION: 1851 Crystal Palace, long low iron-and-glass hall with central arched transept, repeated dark iron columns and pale teal glass panels; warm cream sky and muted warm brown ground; match location reference exactly.

> NEGATIVES: no lettering, captions, labels, logos, watermark, photorealism, extra limbs, merged faces, visual clutter, gradients, or modern objects.

First batch shot prompts: `visuals.csv`, rows 1–8. Explicit story state: the palace is intact and unfinished throughout batch 1; the jammed bolt is a visual metaphor, not a documented collapse. Later rows remain provisional until their shots are individually refined before generation.

## Batch 1 QC and repair attempts

- `beat01m01` attempt 0 rejected: nut surrounds the bolt as if fitted, so the selected mismatched-bolt hook is not visibly clear. Repair changes only the bolt/nut relationship clause to make the bolt end visibly wider than the nut opening.
- `beat01m03` attempt 0 rejected: the large hexagon reads as a bolt head, with no visibly separate nut being threaded. Repair changes only the bolt/nut relationship clause to require a separate nut with visible hole too small for the bolt end.
- Both rejected images retained in `refs/rejects/` for the batch contact sheet. Other six frames reviewed visually; slate-blue waistcoat, charcoal cap, white face and teal palace are consistent with anchors.

- `beat01m01` repair 1 accepted: oversized bolt end meets visibly separate smaller nut; distressed worker and intact palace match hook and anchors. Prompt changed only bolt/nut relationship clause.
- `beat01m03` repair 1 rejected: nut appears aligned around the bolt and incompatibility is not clearly visible; worried expression alone does not show the narrated failure. Attempt retained in `refs/rejects/`. The frame remains pending; one of three permitted re-rolls failed and the two-image repair budget for this turn is exhausted.
- Drift check: `beat01m01` cap charcoal and waistcoat slate blue vs `character_test.png` cap charcoal and waistcoat slate blue; `beat02m02` palace glass pale teal and arches black vs `location_test.png` pale teal glass and black arches. No new anchors.
- Contact sheet contains all seven accepted images and three rejected attempts: `refs/reviews/batch01_contact.png`.

## Batch 2 plan

- `beat01m03` repair 2 changes only the nut/bolt relationship clause: the bolt end is twice the diameter of the nut hole and cannot enter it. Prior attempt 1 rejected because the connection appeared to fit.
- Seven new shots: `beat02m05` through `beat02m10` and `beat03m01`. Construction scenes are intact and unfinished; exhibition scenes explicitly depict the intact completed venue as a future visualization.

## Batch 2 QC

- `beat01m03` repair 2 accepted: worker holds a clearly smaller nut apart from an oversized bolt, alarmed; the visibly incompatible sizes communicate the narrated failure. The changed clause specified that the bolt end was twice the diameter of the nut hole. No new rejection this turn.
- `beat02m05`–`beat02m10` and `beat03m01` inspected and accepted. The two exhibition interiors depict the future, completed Crystal Palace, not the under-construction state.
- Drift check: `beat02m07` worker cap charcoal and waistcoat slate blue vs `character_test.png` charcoal cap and slate-blue waistcoat; `beat03m01` facade pale teal glass and dark iron arches vs `location_test.png` pale teal glass and dark iron arches. No new anchors.
- Review sheet: `refs/reviews/batch02_contact.png` (accepted images and earlier rejects for the repaired shot).
- Reviewed PNG frames and rejects were converted to 256-color indexed PNG without changing pixel dimensions to keep the repository compact; `beat02m07` was visually rechecked after conversion. All future frames must be reviewed after any compression.

## Batch 3 QC — repairs

- `beat03m03` original rejected: two large foreground workers overlap so their heads and bodies merge. Repair changes only the visitor-count clause to one small visitor standing alone.
- `beat03m07` original rejected: visible shattered panes on the central transept contradict the explicit intact-palace state. Repair changes only the palace condition clause to say every pane is unbroken.

- `beat03m03` repair 1 accepted: a single isolated visitor under the arched roof replaces the merged foreground figures.
- `beat03m07` repair 1 accepted: incomplete roof is under construction but panes are not shattered; beam and watch illustrate rapid construction.
- Drift check: `beat03m03` worker cap charcoal and vest slate blue vs `character_test.png` charcoal cap and slate-blue vest; `beat03m05` pale teal glass and dark iron arches vs `location_test.png` pale teal glass and dark iron arches. No new anchors.
- All 8 accepted frame files and 2 rejected attempts compressed to 256-color indexed PNG at unchanged native dimensions; batch contact sheet `refs/reviews/batch03_contact.png` shows each, including rejects.

## Batch 4 QC — repairs

- `beat05m04` original rejected: closed hand forms a tangled swirl of fingers instead of the anchor's simple white hand. Repair changes only the closed-hand clause to an uncomplicated white mitten shape.
- `beat06m01` original rejected: peach-colored, anatomically detailed palm drifts from the anchor's simple white cartoon hands. Repair changes only the open-palm clause to a white oval cartoon mitten.

- `beat05m04` repair 1 accepted: clean white mitten replaces tangled fingers and conceals the object.
- `beat06m01` repair 1 accepted: white cartoon mitten replaces peach anatomically detailed palm; nut and bolt remain distinct.
- Drift check: `beat05m04` cap charcoal, waistcoat slate-blue and hand white vs `character_test.png` charcoal cap, slate-blue waistcoat and white hands; `beat04m03` glass pale teal and arches dark vs `location_test.png` pale teal glass and dark arches. No new anchors.
- All eight accepted frames and both rejected attempts converted to indexed PNG at unchanged native dimensions; `refs/reviews/batch04_contact.png` shows all attempts.

## Batch 5 QC — repair

- `beat07m03` original rejected: the archival book contains illegible pseudo-writing despite the no-text invariant. Repair changes only the book-page clause to make the pages blank except for a palace drawing.

- `beat07m03` repair 1 accepted: the book pages are blank apart from the palace image; illegible pseudo-writing removed.
- Drift check: `beat07m01` cap charcoal and waistcoat slate blue vs `character_test.png` charcoal cap and slate-blue waistcoat; `beat07m02` palace glass pale teal and iron dark vs `location_test.png` pale teal glass and dark iron. No new anchors.
- Eight accepted frames and the rejected attempt converted to 256-color indexed PNG at unchanged native dimensions; contact sheet `refs/reviews/batch05_contact.png` shows all accepted frames and the reject.

## Batch 6 QC — repair

- `beat08m02` original rejected: the bolt is shown end-on like a solid hexagon, so its threaded shaft is not visible; the cropped worker also has black hands rather than the approved white hands. Repair changes the bolt-view clause to a clear side-on view of its entire threaded shaft.

- `beat08m02` repair 1 accepted: side-on bolt displays the full ridged shaft; the worker’s hands are no longer visible.
- Drift check: `beat08m01` cap charcoal and waistcoat slate blue vs `character_test.png` charcoal cap and slate-blue waistcoat; `beat08m04` pale teal glass and dark iron vs `location_test.png` pale teal glass and dark iron. No new anchors.
- All eight accepted frames and the rejected attempt converted to 256-color indexed PNG at unchanged native dimensions. Contact sheet `refs/reviews/batch06_contact.png` includes accepted frames and the rejected original.
