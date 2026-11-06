# ULTRA-LEAN WORKER PACKETS — broken_leg

200 rows in `visuals.csv`, 3 non-overlapping chunks. Each packet is fully
self-contained: copy the whole block into its own worker chat.

Shared branch base: `arena/c25b4281-newrepo2` (workers PR back into it, not into
`main` — `main` does not carry this session's branch).

---

## WORKER 1 — rows 1-67 (slides 01-09, starts slide 10)

```markdown
WORKER ASSIGNMENT:
- Branch: git checkout -b broken-leg-worker-1 origin/arena/c25b4281-newrepo2
- Target CSV: broken_leg_video/visuals.csv (Assigned Rows 1 to 67)
- Output Dir: broken_leg_video/frames/  (files: beat{slide:02d}m{moment:02d}.jpg, 1280x720, quality 90)

LOCKED STYLE (copy/paste verbatim into every prompt):
Hand-inked 2D animation still on warm cream paper, thick slightly wobbly dark-brown outlines, flat gouache fills with soft paper grain, limited earthy palette of mustard ochre, sage blue-grey, warm sand, deep navy and one brick-red accent, halftone dot shading only in contact shadows, simple round-headed figures with dot eyes and thin expressive brows, soft daylight or firelight bloom, muted film grain, locked-off camera, 16:9 widescreen.
LOCKED NEGATIVE (verbatim): photorealistic, 3D render, CGI, gradients, airbrush, anime, chibi, detailed anatomy, gore, blood, open wounds, broken skin, text, letters, numbers, captions, watermark, logo, signature, frame border, extra limbs, melted faces, deformed hands, motion blur, lens flare, neon colours, dense background detail
PROTAGONIST ("YOU"): round white head, two black dot eyes, thin arched brows, small ink tuft of hair at the crown, one ink-stroke body, fringed hide tunic to mid-thigh, simple three-finger hands, thick dark-brown mitten boots. Never a wound, cast, splint or blood.
BAND: same design language, darker shaggy hair, hides in sage grey or warm sand, emotion carried by brows and posture only.

INSTRUCTIONS:
1. Pull the branch, read ONLY rows 1-67 of visuals.csv, load broken_leg_video/refs/ and continuity.md.
2. Generate 6 frames per turn matching each moment_text; attach refs/<WINNING_ANCHOR>.jpg as the style reference every time. No location_ref yet - build fresh backgrounds in the locked style.
3. QC each frame against its moment_text and the anchor; re-roll max 2 per turn, changing ONE clause each time. After 3 failed rolls, ship the closest and append a DECLARED EXCEPTION line to broken_leg_video/STATE.md.
4. Save, commit and push after every batch of 6. Never touch rows outside 1-67, never edit visuals.csv.
```

---

## WORKER 2 — rows 68-134 (slide 10 mid to slide 22)

```markdown
WORKER ASSIGNMENT:
- Branch: git checkout -b broken-leg-worker-2 origin/arena/c25b4281-newrepo2
- Target CSV: broken_leg_video/visuals.csv (Assigned Rows 68 to 134)
- Output Dir: broken_leg_video/frames/  (files: beat{slide:02d}m{moment:02d}.jpg, 1280x720, quality 90)

LOCKED STYLE (copy/paste verbatim into every prompt):
Hand-inked 2D animation still on warm cream paper, thick slightly wobbly dark-brown outlines, flat gouache fills with soft paper grain, limited earthy palette of mustard ochre, sage blue-grey, warm sand, deep navy and one brick-red accent, halftone dot shading only in contact shadows, simple round-headed figures with dot eyes and thin expressive brows, soft daylight or firelight bloom, muted film grain, locked-off camera, 16:9 widescreen.
LOCKED NEGATIVE (verbatim): photorealistic, 3D render, CGI, gradients, airbrush, anime, chibi, detailed anatomy, gore, blood, open wounds, broken skin, text, letters, numbers, captions, watermark, logo, signature, frame border, extra limbs, melted faces, deformed hands, motion blur, lens flare, neon colours, dense background detail
PROTAGONIST ("YOU"): round white head, two black dot eyes, thin arched brows, small ink tuft of hair at the crown, one ink-stroke body, fringed hide tunic to mid-thigh, simple three-finger hands, thick dark-brown mitten boots. Never a wound, cast, splint or blood.
BAND: same design language, darker shaggy hair, hides in sage grey or warm sand, emotion carried by brows and posture only.
ELDER (Shanidar 1): grey-streaked hair, heavy brow, hide across the shoulders, right forearm ended smooth below the elbow, left eye socket flattened.

INSTRUCTIONS:
1. Pull the branch, read ONLY rows 68-134 of visuals.csv, load broken_leg_video/refs/ and continuity.md.
2. Generate 6 frames per turn matching each moment_text; attach refs/<WINNING_ANCHOR>.jpg as the style reference every time. No location_ref yet - build fresh backgrounds; museum and lab beats use the cold-light key, cave beats the firelight key.
3. QC each frame against its moment_text and the anchor; re-roll max 2 per turn, changing ONE clause each time. After 3 failed rolls, ship the closest and append a DECLARED EXCEPTION line to broken_leg_video/STATE.md.
4. Save, commit and push after every batch of 6. Never touch rows outside 68-134, never edit visuals.csv.
```

---

## WORKER 3 — rows 135-200 (slide 22 mid to end)

```markdown
WORKER ASSIGNMENT:
- Branch: git checkout -b broken-leg-worker-3 origin/arena/c25b4281-newrepo2
- Target CSV: broken_leg_video/visuals.csv (Assigned Rows 135 to 200)
- Output Dir: broken_leg_video/frames/  (files: beat{slide:02d}m{moment:02d}.jpg, 1280x720, quality 90)

LOCKED STYLE (copy/paste verbatim into every prompt):
Hand-inked 2D animation still on warm cream paper, thick slightly wobbly dark-brown outlines, flat gouache fills with soft paper grain, limited earthy palette of mustard ochre, sage blue-grey, warm sand, deep navy and one brick-red accent, halftone dot shading only in contact shadows, simple round-headed figures with dot eyes and thin expressive brows, soft daylight or firelight bloom, muted film grain, locked-off camera, 16:9 widescreen.
LOCKED NEGATIVE (verbatim): photorealistic, 3D render, CGI, gradients, airbrush, anime, chibi, detailed anatomy, gore, blood, open wounds, broken skin, text, letters, numbers, captions, watermark, logo, signature, frame border, extra limbs, melted faces, deformed hands, motion blur, lens flare, neon colours, dense background detail
PROTAGONIST ("YOU"): round white head, two black dot eyes, thin arched brows, small ink tuft of hair at the crown, one ink-stroke body, fringed hide tunic to mid-thigh, simple three-finger hands, thick dark-brown mitten boots. Never a wound, cast, splint or blood.
BAND: same design language, darker shaggy hair, hides in sage grey or warm sand, emotion carried by brows and posture only.
ELDER (Shanidar 1): grey-streaked hair, heavy brow, hide across the shoulders, right forearm ended smooth below the elbow, left eye socket flattened.

INSTRUCTIONS:
1. Pull the branch, read ONLY rows 135-200 of visuals.csv, load broken_leg_video/refs/ and continuity.md.
2. Generate 6 frames per turn matching each moment_text; attach refs/<WINNING_ANCHOR>.jpg as the style reference every time. No location_ref yet - build fresh backgrounds; hillside beats warm dusk, museum beats cold white.
3. QC each frame against its moment_text and the anchor; re-roll max 2 per turn, changing ONE clause each time. After 3 failed rolls, ship the closest and append a DECLARED EXCEPTION line to broken_leg_video/STATE.md.
4. Save, commit and push after every batch of 6. Never touch rows outside 135-200, never edit visuals.csv.
```

---

## Frame naming examples

`beat01m03.jpg`, `beat09m17.jpg`, `beat32m09.jpg` — slide is 2 digits, moment is
2 digits, matching the `slide_id` / `moment` columns exactly. No zero rows, no
renames, no renumbering.
