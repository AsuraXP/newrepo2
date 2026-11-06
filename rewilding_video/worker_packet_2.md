# WORKER ASSIGNMENT 2 — The Rewilding

- Worker: branch `rewilding-worker-2`
- Target CSV: `rewilding_video/visuals.csv` — **Assigned rows 85 to 168** (84 frames to generate)
- Slides covered: 3, 4, 5, 6, 7
- Output dir: `rewilding_video/frames/` — filename `beat{slide:02d}m{moment:02d}.png` (already encoded in the table below)
- Batch: **6 frames per turn**, repair budget **R=2 per turn** (re-roll changing ONE clause only)
- QC each frame: shows its moment_text? invariants intact? no melted limbs/merged faces/gibberish text? Reject → name the fault, re-roll, ≤3 tries then ship closest as DECLARED EXCEPTION (log in STATE.md).
- Contact sheet of every batch (~380px thumbs, rejects included). Commit + push branch after EVERY batch.
- Pacing: each frame holds for the exact spoken duration of its moment_text; word-level TTS timestamps place cuts — never hand-place durations

## LOCKED STYLE & CHARACTER (copy/paste VERBATIM into every prompt)

**Style & Medium:**
Hand-drawn 2D stick-figure cartoon — thick wobbly black ink outlines, round white head, dot eyes with expressive black brows, thin black stick body and limbs with small oval hands and simple stick feet, painterly gouache-style brush shading with subtle film grain, warm-cool color separation (amber practical light vs cold blue-gray mist), muted earthy palette, high-contrast readable silhouettes, no photorealism, no 3D render, no anime.

**Protagonist
round white head, three-strand hair sprig under a weathered olive wide-brim hat, heavy-lidded tired dot eyes under straight brows; thin black oval torso; STICK arms and legs with oval hands and flat stick feet; olive-green ranger vest over charcoal shirt, olive trousers, small olive backpack, chest tag reading SECTOR SEVEN, brass tally counter on belt; dart gun holstered, ALWAYS with the red UNFIRED tape intact; dark boots.

**The calf
round white head, smaller than adult hands, single hair sprig, huge bright dot eyes, enormous brave smile; oversized red flannel work jacket with painted-on check/plaid, sleeves rolled and cupped over her hands; tiny stick limbs; barefoot. NEVER shown older than two. NEVER harmed.

**The turned
round pale blue-gray heads, blank soft-white dot eyes (never red), tattered layered coats in ash gray, slate and bark brown, hunched posture, heels dragging toe-clawing gait; move ONLY at a slow walk; NEVER run, NEVER speak, NEVER attack. No wounds, no blood, no rot — always weathered and dry.

## INSTRUCTIONS
1. Pull branch, open `visuals.csv` (rows pre-numbered in the table below for convenience), load `refs/`.
2. For EVERY assigned row: image prompt = [visual_prompt] + [LOCKED STYLE & CHARACTER verbatim above]. Attach character_ref whenever ranger/calf/herd appears.
3. Attach location_ref ONLY while the beat occurs in the same continuous setting. When the setting changes (see Slides column), DROP location_ref and generate a fresh background in the locked style.
4. Camera LOCKED OFF — no Ken Burns/zoom/drift. Fire/candle = warm light only. No text beyond diegetic signage ≤5 words. Wanderers never run, never red-eye, never glow.

## ASSIGNED FRAMES — 84 prompts

| # | frame file | moment_text | visual_prompt |
|---|---|---|---|
| 85 | beat03m22.png | the way elk do. | close-up: far-off elk in a meadow echoing the same spacing |
| 86 | beat03m23.png | They do not hunt anymore. | close-up: matte pale eyes of one turned figure — blank, enormous, still |
| 87 | beat03m24.png | They do not seek. | wide: herd drifting past an overturned fruit truck, uninterested |
| 88 | beat03m25.png | They migrate, | side tracking wide: herd cresting a hill and vanishing, endless patience |
| 89 | beat03m26.png | generation after silent generation, | wide time-feel: faint echo figures walking the same path, generations deep |
| 90 | beat03m27.png | and nobody can fully explain how they persist, | close-up: manual page THE PERSISTENCE OF THE DRIFT — only diagrams, no answers |
| 91 | beat03m28.png | only that they do, | close-up: tally sheet grid filled with years of silent ticks |
| 92 | beat03m29.png | because they always have. | wide: a dusk valley, the herd trail worn into ferns, ancient |
| 93 | beat03m30.png | Your job is to count them. | wide: ranger tiny on the ridge, valley vast, herd a slow river |
| 94 | beat04m01.png | You are a ranger of the Rewilding Authority, | medium: figure pulls on olive ranger vest at the door, clipboard under arm |
| 95 | beat04m02.png | Third Meridian, | close-up: shoulder patch REWILDING AUTHORITY — THIRD MERIDIAN |
| 96 | beat04m03.png | Sector Seven. | close-up: chest tag SECTOR SEVEN and a brass tally counter |
| 97 | beat04m04.png | You carry a dart gun you have never fired in anger, | close-up: dart gun on the table, red UNFIRED tape across the trigger guard |
| 98 | beat04m05.png | a pair of binoculars older than your parents, | close-up: binoculars on a nail, brass worn bright, strap sun-faded |
| 99 | beat04m06.png | and a manual with more addenda than rules. | close-up: manual stack with a dozen addenda tabs fanned out |
| 100 | beat04m07.png | You collar nothing. | close-up: an open collar case on the table — empty, never used |
| 101 | beat04m08.png | You tag nothing permanent. | close-up: dart gun re-hung on the wall rack |
| 102 | beat04m09.png | You count, | close-up: gloved hand over a tally grid, counting heads |
| 103 | beat04m10.png | you photograph, | close-up: figure lining up a shot through the spotting scope tripod |
| 104 | beat04m11.png | you note condition | close-up: notebook line — CONDITION: THIN, steady column |
| 105 | beat04m12.png | and direction, | close-up: notebook line — DIRECTION: NE, arrow scratched hard |
| 106 | beat04m13.png | and every month Base flies a drone over the crossing | wide: a small survey drone high above the creek crossing, drifting low |
| 107 | beat04m14.png | and checks your numbers, | close-up: drone's shadow sliding across the gray ford water |
| 108 | beat04m15.png | and the numbers go into a ledger | close-up: a monthly ledger, columns of counts in neat block script |
| 109 | beat04m16.png | in a tower in a walled city by the sea, | wide: walled city far across the water, one tall tower, antenna blinking |
| 110 | beat04m17.png | because knowing where the herds are is the difference between a safe world | close-up: ledger page stamped SAFETY IS KNOWING in block letters |
| 111 | beat04m18.png | and a lucky one. | close-up: the last page of the ledger closing over a fresh count |
| 112 | beat05m01.png | You make coffee on the camp stove. | interior: propane camp stove ablaze, coffee pot steaming, figure waiting |
| 113 | beat05m02.png | You check the camera traps, | medium: figure crouches at the creekbank, checking the trap strap |
| 114 | beat05m03.png | one by one, | close-up: camera strap buckle and mud-caked boot toe |
| 115 | beat05m04.png | spooling the film in the dry little dark of your pack. | close-up: film cartridge spooling into a belt pouch in the dark pack |
| 116 | beat05m05.png | You tell yourself what you always tell yourself. | close-up: figure's eye reflected in the curved camera lens glass |
| 117 | beat05m06.png | You are a clerk. | medium: figure alone with coffee on the porch, thinking |
| 118 | beat05m07.png | A clerk of the wilderness. | close-up: ink-black fingertips on ledger paper — a clerk's hands |
| 119 | beat05m08.png | Clerks do not interfere. | close-up: a rubber stamp coming down — LOGGED |
| 120 | beat05m09.png | At the second camera, | medium: figure at the second camera on a bent oak, going suddenly still |
| 121 | beat05m10.png | you find the thing you feared. | close-up: printed photo strip lying across a lap, red 04:17 in the corner |
| 122 | beat06m01.png | The frame is timestamped 04:17. | close-up: photo corner INFRARED — 04:17 in hot red type |
| 123 | beat06m02.png | Night grain, | close-up: grainy infrared photo, white figures against green-black wash |
| 124 | beat06m03.png | infrared white | close-up: photo zoomed, a band of white backs across the frame |
| 125 | beat06m04.png | and green. | same photo, green flare tint deepening, sprocket grain visible |
| 126 | beat06m05.png | In it, | medium: figure staring at the photo, eyes widening under hat brim |
| 127 | beat06m06.png | the herd crosses the creek bed — | photo close-up: herd frozen mid creek crossing, water flung in stars |
| 128 | beat06m07.png | eleven adults, | photo close-up: eleven adult backs in a hitching tide formation |
| 129 | beat06m08.png | unmistakable even at that distance, | photo close-up: gait detail — heels dragging, toes clawing |
| 130 | beat06m09.png | that hitching, | photo close-up: the wave of motion rippling down the line |
| 131 | beat06m10.png | tidelike gait — | same photo widened — the ripple line crossing the whole frame |
| 132 | beat06m11.png | and behind the last of them, | photo close-up: the farthest back — low, small, and dragging |
| 133 | beat06m12.png | so low to the ground she is nearly a shadow, | photo close-up: near-shadow fold pressed against the dark |
| 134 | beat06m13.png | the adult you logged two days ago. | photo close-up: the long-toed adult recognized from the mud |
| 135 | beat06m14.png | And under her chest, | photo close-up: under her chest, a small bright bundle-shape |
| 136 | beat06m15.png | tucked against her, | photo close-up: the bundle tucked high and held tight to the torso |
| 137 | beat06m16.png | a small bright shape. | macro: the bright knot of the sling, centered in the frame |
| 138 | beat06m17.png | Wrapped in something. | photo close-up: sling knot visible at the figure's back |
| 139 | beat06m18.png | A tarp scrap. | photo close-up: tarp scrap corner — gray-blue weave, sun-bleached |
| 140 | beat06m19.png | A jacket. | photo close-up: flannel check pattern inside the sling |
| 141 | beat06m20.png | A piece of the old world, | photo close-up: jacket sleeve stripe — old-world red plaid, decades old |
| 142 | beat06m21.png | remade into a sling. | photo close-up: loose sling strap dangling, sway frozen mid-frame |
| 143 | beat06m22.png | The calf. | macro: the bundle centered in the photo — THE CALF in harsh contrast |
| 144 | beat06m23.png | You sit down in the leaf mold with the photograph in your hands, | wide: figure seated on the forest floor, photo in both hands, gold leaf-light |
| 145 | beat06m24.png | and for a long time you do not move. | long hold: figure unmoving, ferns swaying, creek light crawling |
| 146 | beat07m01.png | The manual has a page for a turned animal found dead. | close-up: manual page TURNED — DECEASED PROTOCOL — numbered steps one to six |
| 147 | beat07m02.png | It has a page for a new settlement found in the Drift. | close-up: manual page SETTLEMENTS FOUND IN THE DRIFT — shack illustration |
| 148 | beat07m03.png | It does not have a page for this, | close-up: manual page — THIS PAGE INTENTIONALLY BLANK |
| 149 | beat07m04.png | because this has never happened, | close-up: a finger hovering an inch above the blank paper |
| 150 | beat07m05.png | because this cannot happen, | close-up: figure's face going cold and calculating |
| 151 | beat07m06.png | because turners do not have children, | macro: the photo burning in the reflection of one close eye |
| 152 | beat07m07.png | because the world that ended took the children first, | close-up: manual foreword plate — the evacuation-era city at dusk, storybook flat |
| 153 | beat07m08.png | and because — and your mind keeps returning to this, | medium: over-shoulder — figure reading a torn evacuation poster: ROUTE 9 arrow |
| 154 | beat07m09.png | over and over — | close-up: the same blank page again, close in |
| 155 | beat07m10.png | someone had to carry that baby into the deep woods | wide: the deep woods under untouched canopy, a game trail vanishing east |
| 156 | beat07m11.png | and leave it there, | photo close-up: the adult from behind, bundle hugged to the chest |
| 157 | beat07m12.png | or lose it, | photo close-up: same frame held tighter to the face |
| 158 | beat07m13.png | or die, | photo close-up: the herd from behind, spacing like geese in flight |
| 159 | beat07m14.png | and the herd found it, | photo close-up: the bundle centered — the herd gathered around a lost gosling |
| 160 | beat07m15.png | and the herd kept it. | wide: the creek crossing at dusk, abandoned, reeds bowing in wind |
| 161 | beat07m16.png | You zoom the photo until the pixels break. | macro: a jeweler's loupe over the photo resting on a flat palm |
| 162 | beat07m17.png | The adult's head is bowed. | photo close-up: the adult's head bowed against her chest |
| 163 | beat07m18.png | Not browsing. | same photo — hanging lower, grazing silhouette denied |
| 164 | beat07m19.png | Bowed. | same photo — the bow unmistakable, a different posture entirely |
| 165 | beat07m20.png | The posture of something standing guard over warmth. | photo close-up: shoulders rounded protectively — a sentry over warmth |
| 166 | beat07m21.png | You do not radio Base. | medium: figure at the radio desk, hand hovering above the handset |
| 167 | beat07m22.png | You tell yourself it is | close-up: fingers stopped mid-air above the telephone hook |
| 168 | beat07m23.png | because Base would send a team, | close-up: radio dial glow, red, waiting |
