# WORKER ASSIGNMENT 1 — The Rewilding

- Branch: `git checkout -b rewilding-worker-1` (from arena/c251d7fe-newrepo2)
- Target CSV: `rewilding_video/visuals.csv` — **Assigned rows 1 to 112** (112 frames to generate)
- Slides covered: 1, 2, 3, 4, 5
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

## ASSIGNED FRAMES — 112 prompts

| # | frame file | moment_text | visual_prompt |
|---|---|---|---|
| 1 | beat01m01.png | You wake before the radio does, | close-up: dark ranger bunk, round white head of a stick-figure ranger on a pillow, eyes opening in dim pre-dawn gloom |
| 2 | beat01m02.png | the way you always do, | same bed, figure lying still, listening, eyes half open, first gray light through cracked blinds |
| 3 | beat01m03.png | to the sound of wind moving through a forest that used to be a suburb. | wide establishing: station window framing foggy evergreen forest, faint vine-choked suburban overgrowth deep in frame — rusted car roofs under vines |
| 4 | beat01m04.png | You lie in the bunk | figure lying motionless in the bunk, blanket to the chin, staring upward |
| 5 | beat01m05.png | and listen to it. | figure tilts head, ear toward the wall, savoring the familiar quiet |
| 6 | beat01m06.png | Pine. | close-up: fog-swaddled pine trunks outside the window, needles beaded with moisture |
| 7 | beat01m07.png | Oak. | close-up: old oak limbs reaching over a mossy ruin of a mailbox row |
| 8 | beat01m08.png | Wind in the power lines that stopped carrying power forty years before you were born. | low angle: leaning power pole, drooping wires, a nest on the crossarm, ferns swallowing the lane |
| 9 | beat01m09.png | Somewhere below the ridge, | wide from high ridge: valley below, a ruined highway unspooling under moss and wild grape |
| 10 | beat01m10.png | a highway unspools under moss | closer: torn highway segment emerging from vines, grape dripping off broken overpass girders |
| 11 | beat01m11.png | and wild grape, | close-up: wild grape tendrils and leaves drooping over a rusted guardrail |
| 12 | beat01m12.png | straight as a scar that healed crooked. | wide: the crooked healed scar of the highway curving through solid green forest |
| 13 | beat01m13.png | You know every sound this station makes at dawn. | interior wide: ranger station at dawn, figure facing a wall of maps and shelves, knowing every sound |
| 14 | beat01m14.png | The settling beams. | close-up: ancient ceiling beams, thin blades of light through gaps, drifting dust |
| 15 | beat01m15.png | The water pump. | close-up: hand-crank water pump by the door, swaying faintly on its mount |
| 16 | beat01m16.png | The long, | close-up: close-up sliver: antenna mast base and guy wires through the window, gray dawn |
| 17 | beat01m17.png | low groan of the antenna mast, | low angle: full antenna mast against gray morning sky, a slight forward lean |
| 18 | beat01m18.png | leaning a degree further every year into the gray morning. | top-of-mast close-up: weathered tip and insulator, wires humming, clouds streaming past |
| 19 | beat01m19.png | Then the radio hisses, | erasing-paced wide: dim interior, figure still in the bunk, static whispering from the radio |
| 20 | beat01m20.png | and the day begins the way every day begins. | wide: same room, morning ritual beginning, rafters dusty in light shafts |
| 21 | beat01m21.png | "Sector Seven, | close-up: radio speaker grille, warm dial glow, sound waves implied |
| 22 | beat01m22.png | this is Base." A woman's voice, | medium: figure sits up, flat calm expression, listening to the voice |
| 23 | beat01m23.png | flat with coffee | medium: figure rubs face with both hands, unimpressed, morning face |
| 24 | beat01m24.png | and distance. | close-up: untouched coffee pot on stove, thin steam, flat gray light through window |
| 25 | beat01m25.png | "Say your count." | medium: figure inhales, steadying for the ritual |
| 26 | beat01m26.png | You lift the handset from its hook. | close-up: hand lifts the handset off the wall phone hook |
| 27 | beat01m27.png | "Sector Seven. | medium: figure speaks into handset, steady ranger posture, dawn-lit room |
| 28 | beat01m28.png | Morning one, | wide: station interior, map wall, radio desk, dusty sunbeam through doorway |
| 29 | beat01m29.png | in position. | medium: boots planted, spine straight — Morning one report |
| 30 | beat01m30.png | Cameras armed on the crossing. | close-up: trail camera strapped to a pine at the creek crossing, sensor eye dark |
| 31 | beat01m31.png | I'll do the foot count at midday." | wide: creek crossing, gray water, camera traps armed on both banks |
| 32 | beat01m32.png | "Log it," Base says, | close-up: notebook page grid for midday count, blank, pen resting |
| 33 | beat01m33.png | "and remember, | close-up: ledger open on desk, header SECTOR SEVEN in stamped letters |
| 34 | beat01m34.png | if you lose visual, | medium: handset pressed to ear, listening hard, jaw set |
| 35 | beat01m35.png | you do not pursue. | close-up: radio dial, waveform glow, red standby light |
| 36 | beat01m36.png | You log | close-up: brass tally counter clicking once in a gloved palm — the log |
| 37 | beat01m37.png | and you withdraw." | medium: figure turns from the desk, already withdrawing |
| 38 | beat01m38.png | "Copy," you say, | close-up: one finger raised in flat acknowledgment |
| 39 | beat01m39.png | the way you always say it, | close-up: handset tag worn smooth by years of the same call |
| 40 | beat01m40.png | and Base clicks off, | close-up: handset settling onto the cradle, dial light dying to standby |
| 41 | beat01m41.png | and you lie there one second longer, | wide: room, figure motionless at the desk, long dusty light shaft |
| 42 | beat01m42.png | because there is something you have not told Base yet. | close-up: figure's face half in shadow, holding the unsaid calf-secret |
| 43 | beat02m01.png | There is a calf. | medium: figure turns slowly toward a pinned photograph on the wall |
| 44 | beat02m02.png | You found the tracks two days ago, | close-up: muddy creekbank prints among reeds, two-day-old rain texture |
| 45 | beat02m03.png | in the mud by the creek crossing. | close-up: prints at the waterline, faint ripple rings crossing them |
| 46 | beat02m04.png | Small. | macro: toddler-size bare print, staggered heel-toe |
| 47 | beat02m05.png | Bare. | macro: tiny bare footprint, toes spread, never known a shoe |
| 48 | beat02m06.png | The gait of a toddler who never learned to walk | close-up: short stuttering print sequence zig-zagging through mud |
| 49 | beat02m07.png | and somehow did. | close-up: prints leveling into steadier, more deliberate steps |
| 50 | beat02m08.png | And beside them, | close-up: tiny print beside a long adult drag-smear, paired in mud |
| 51 | beat02m09.png | in the same mud, | macro: adult long-toed print filling the frame, toe-claw strokes |
| 52 | beat02m10.png | the long-toed, | close-up: toe-claw impressions held in raking light |
| 53 | beat02m11.png | dragging print of an adult. | wide: single wavering drag-track line hesitating into fog |
| 54 | beat02m12.png | One adult. | wide: mud spacing — wide patient strides heading valleyward |
| 55 | beat02m13.png | Walking slow. | close-up: unbroken heel-drag smear, one continuous line in mud |
| 56 | beat02m14.png | Bleeding nothing, | close-up: dried flat dark splotch in old mud — matte, dry, impersonal |
| 57 | beat02m15.png | because they do not bleed anymore. | macro: still air above the prints, no flies, only settling dust |
| 58 | beat02m16.png | Going somewhere with terrible patience. | wide: the track line climbing out of the creek onto the valley floor |
| 59 | beat02m17.png | You logged the adult prints. | close-up: gloved hand writing in the log: ADULT — DRAG — EAST |
| 60 | beat02m18.png | You did not log the small ones. | close-up: same logbook, a second line pointedly left blank |
| 61 | beat02m19.png | You told yourself it was a rounding error. | close-up: crumpled scrap of paper, tally marks crossed out twice |
| 62 | beat02m20.png | You told yourself a lot of things, | close-up: hand scribbling, crossing out again, charcoal fingers |
| 63 | beat02m21.png | those two days. | wide: dusk two days ago, figure on the porch staring at rain-dark boards |
| 64 | beat03m01.png | The Collapse was fifty years ago, | wide memory frame: enclave walls on the coast at sunset, towers and antennas, smoke columns far inland |
| 65 | beat03m02.png | and nobody alive remembers the world that ended. | close-up: old field manual page, finger tracing cream paper, headline THE COLLAPSE |
| 66 | beat03m03.png | You know it the way you know scripture: | close-up: same manual, a candle flame steady at its spine |
| 67 | beat03m04.png | the fever that was never quite a fever, | close-up: manual illustration — an empty main street, cars under drifting leaves, one distant figure |
| 68 | beat03m05.png | the streets that filled in a single bad month, | close-up: manual illustration — city skyline emptying, smoke columns, tiny evacuees on a bridge |
| 69 | beat03m06.png | the long years when the cities emptied | close-up: manual illustration — a patrol line of soldiers thinning into fog |
| 70 | beat03m07.png | and the Army walked patrols that came back fewer every time. | wide memory frame: coastal enclave gate at dusk, clinic flag, a queue of tiny figures |
| 71 | beat03m08.png | You know the enclaves on the coasts, | wide: coastal enclave gate at dusk, walls running into the surf, watchtowers |
| 72 | beat03m09.png | with their walls | close-up: enclave wall concrete and rebar scars, a clinic flag snapping |
| 73 | beat03m10.png | and their clinics | close-up: worn clinic door, red cross flaked to pink paint |
| 74 | beat03m11.png | and their rules. | close-up: gate signage AUTHORITY TRANSIT — RESIDENTS ONLY, riveted plate |
| 75 | beat03m12.png | You know the Authority. | wide: AUTHORITY brochure cover left open, heron emblem — REWILDING |
| 76 | beat03m13.png | And you know the thing the Authority does not say on the brochures: | close-up: brochure inside page — THREE MERIDIANS — ONE WILD |
| 77 | beat03m14.png | the turned did not burn out. | close-up: manual page THE TURNED — a simple diagram of the dragging gait |
| 78 | beat03m15.png | They adapted. | close-up: manual illustration — herd spacing like deer in a meadow |
| 79 | beat03m16.png | They thinned. | close-up: range maps in the manual — contour lines and drift arrows |
| 80 | beat03m17.png | They settled into the deep green like deer into a meadow, | wide: herd backs at dawn clearing like deer, far away, unhurried |
| 81 | beat03m18.png | and they move through it on a path older than roads. | wide: single-file herd along a vine-drowned highway interchange |
| 82 | beat03m19.png | They call it the Drift. | close-up: hand-drawn wall map labeled THE DRIFT, red arrows crossing contours |
| 83 | beat03m20.png | The herds follow water | wide: herd following the river through morning mist |
| 84 | beat03m21.png | and season, | wide: herd on a ridge in wind, bracken waves rolling around them |
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
