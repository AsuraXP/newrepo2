# STATE — ancient_travel_video

Machine: STATE 0 → 7 (single-agent producer spec).
**Current: STATE 5 — FRAME GENERATION (batch 1 in progress).**

| State | Status |
|---|---|
| 0 — Repo discovery & init | DONE 2026-11-05 (folder renamed ship_outbreak_video → ancient_travel_video on topic pivot) |
| 1 — Brief | DONE 2026-11-05 — user confirmed: 6 min (can be longer), default voice, 2nd person, style-only refs, no hard rules, no captions, 16:9, YouTube |
| 2 — Script | DONE 2026-11-05 — user approved ("apprive"). 1,210 words ≈ 6.5 min (estimate). |
| 3 — visuals.csv spine | DONE 2026-11-05 — N=182 rows, 42 slides, 23 batches; moment_text concatenation verified == narration word-for-word (build_visuals.py). |
| 4 — Master anchor lock | DONE 2026-11-05 — user picked **B (cinematic)**. Verbatim style/character/negative blocks frozen in continuity.md + build_visuals.py, injected into all 182 prompts. anchor_B reused as beat01m01. |
| 5 — Frame batches | IN PROGRESS — batches 1–21 DONE. 168/182 frames done, 14 remain. |
| 5.5 — Thumbnail | pending |
| 6 — Kaggle runner | pending (`run_ancient_travel_kaggle.sh`) |
| 7 — Handoff cell | pending |

## Standing notes
- All git ops on `arena/1cbb32ec-newrepo2` (session-pinned; no other branch).
- NO AUDIO in this workspace. TTS / mix / FFmpeg / ZIP only on Kaggle.
- User refs are STYLE ONLY: reuse the style continuously, never the literal
  scenes/props (logged in continuity.md).
- Title hook: "It took them ___ days…" → 2,000 walking-days vs 50,000 years
  (42,000 km Out of Eden route ÷ ~20 km/day; sources in script.md).
- Repo Gate 0 calibration still PENDING (`sec_per_word: null`); Kaggle run
  measures word-level timing. Workspace numbers are labelled estimates.
- Reuse at STATE 6: `vidsync/` (tts, timing, stitch, media), `kaggle/run.py`,
  `tools/prep_frames.py` where compatible with the CSV spine.

## Frame storage pipeline (decided batch 1)
Native generated PNGs (~2.3 MB each) would exceed the ~128 MB patchset cap at 182
frames (~387 MB). Pipeline: resize to 1280×720 (render target) + quantize to
256-color PNG (optimize=True) → ~550 KB/frame, ~98 MB projected total. Keeps the
spec's `.png` naming and stays under cap. QC confirmed grain/gradients/character
survive quantization (contact_batch01.jpg). Contact sheets in sheets/ (~380px
thumbs) are QC-only; the STATE 6 runner globs frames/beat*.png only.

## Batch log
- Batch 1 (2026-11-05): beat01m01–beat02m04. 8/8 accepted, 0 rejects, 0 repairs.
  beat01m01 = reused approved anchor B. Location shifts (beach → S. headland →
  map) generated fresh in locked style. Contact sheet: sheets/contact_batch01.jpg.
  Next: batch 2 = beat03m01–beat05m02.
- Batch 2 (2026-11-05): beat03m01–beat05m02. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch02.jpg (incl. rejects). Rejects:
  beat03m01_r0 (paved cobblestone path + forest → changed path clause to dirt
  footpath on open grassland); beat05m02_r0 (Stonehenge-like megalith → changed
  environment clause to natural rocky ledge, no standing stones). Both repairs
  passed first re-roll. Next: batch 3 = beat05m03–beat07m05.
- Batch 3 (2026-11-05): beat05m03–beat07m05. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch03.jpg (incl. rejects). Rejects:
  beat06m02_r0 (tan boot-like feet → bare black stick feet, no shoes);
  beat07m01_r0 (extra corner limb-lines → exactly two legs, nothing else).
  Both repairs passed first re-roll. New location: savanna (acacia). Kudu
  design established (spiral horns, white-striped tan coat) for slide 9.
  Next: batch 4 = beat07m06–beat08m04.
- Batch 4 (2026-11-05): beat07m06–beat08m04. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch04.jpg (incl. rejects). Rejects:
  beat08m01_r0 (baked-in letterbox bars → full-bleed 16:9); beat08m02_r0
  (gibberish pseudo-text annotations → wordless coil, no labels/arrows).
  Both repairs passed first re-roll. Anatomy-diagram beats use amber glow
  highlights, no text. Next: batch 5 = beat08m05–beat09m07.
- Batch 5 (2026-11-05): beat08m05–beat09m07. 8/8 accepted, 0 QC rejects.
  Contact sheet: sheets/contact_batch05.jpg. 2 moderation blocks re-worded
  (not QC rejects): beat09m02 "hunters jogging after"→"figures jogging behind
  a running kudu"; beat09m07 "hunter toward exhausted kudu, relentless"→
  "figure toward a kudu lying down resting". Both accepted first try. New
  location locked: Kalahari (red sand, dry scrub, blazing white sun, mesas).
  Kudu design consistent across all hunt beats. Next: batch 6 =
  beat09m08–beat12m02.
- Batch 6 (2026-11-05): beat09m08–beat12m02. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks (neutral hunt phrasing per continuity.md
  worked). Contact sheet: sheets/contact_batch06.jpg. Hunt resolved respectfully
  (lying kudu, calm approach, no gore). New location locked: camp (A-frame hide
  lean-tos with crossed poles, central fire, savanna edge, acacia silhouettes).
  Next: batch 7 = beat12m03–beat13m06.
- Batch 7 (2026-11-05): beat12m03–beat13m06. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch07.jpg.
  Camp design held (A-frame hide lean-tos, crossed poles); sparse-possessions
  prop set established (folded hide, digging stick, woven basket, fire drill).
  Distance contrast m02 (short path, both camps in frame) vs m03 (long aerial
  path, camp at horizon) reads clearly. Next: batch 8 = beat14m01–beat15m06.
- Batch 8 (2026-11-05): beat14m01–beat15m06. 8/8 accepted after 2 repairs (R=2
  used). Contact sheet: sheets/contact_batch08.jpg (incl. rejects). Rejects:
  beat15m01_r0 + beat15m06_r0 (both conifer/pine-forest background drift →
  explicit "flat savanna horizon with acacia silhouettes and no forest").
  Both repairs passed first re-roll. "Again/And again" beats use intentional
  compositional repetition with dusk→morning→wet-season light shifts; lifetime
  beat = child→adult→grey elder silhouettes. Next: batch 9 = beat15m07–beat16m05.
- Batch 9 (2026-11-05): beat15m07–beat16m05. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch09.jpg.
  Drift lesson applied: all savanna/camp beats carry acacia + no-forest clause.
  Drift-math beats (stylized map w/ tiny amber arrow; tiny camp vs enormous
  Earth) wordless. Elder = distinct secondary character (grey hair/robe),
  protagonist child on-model. Next: batch 10 = beat16m06–beat18m06.
- Batch 10 (2026-11-05): beat16m06–beat18m06. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch10.jpg.
  Navigation section: seasonal bands, fork-in-path, glowing amber landmarks
  (wordless), east-west sun arc, circular star-trail vortex, river, mountains,
  coastline-as-road (shifts to coast setting). Acacia/no-forest held throughout.
  Next: batch 11 = beat18m07–beat19m06.
- Batch 11 (2026-11-05): beat18m07–beat19m06. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch11.jpg.
  Beach foraging (tide pools, seal/fish/shellfish, peaceful) → featureless
  desert memory → Australian outback songlines. Musical-note symbols rendered
  clean (treble clef + notes), not gibberish — accepted as intentional metaphor.
  New location locked: Australian outback (red sand, spinifex, monoliths,
  glowing amber songlines). Next: batch 12 = beat19m07–beat21m01.
- Batch 12 (2026-11-05): beat19m07–beat21m01. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch12.jpg.
  Songlines payoff: confident crossing, song-as-map, map-as-song (beat19m09
  musical notation = intentional clean subject, accepted), continent-spanning
  song-path network (standout). "No paper / No GPS" = empty hands, no device.
  Melody-to-waterhole. New location locked: lush Asian coastline (tropical
  palms, jungle, open sea) for Sahul section. Next: batch 13 = beat21m02–beat22m06.
- Batch 13 (2026-11-05): beat21m02–beat22m06. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch13.jpg.
  Sahul problem setup: concerned pause, ultra-wide daunting ocean, faint land
  hint, squint at empty horizon, subtle sign, seabirds, stationary cloud over
  unseen land, vast open ocean. Lush Asian coast + deep-blue/amber palette held.
  Next: batch 14 = beat22m07–beat23m04.
- Batch 14 (2026-11-05): beat22m07–beat23m04. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch14.jpg.
  No-land-bridge wordless cross-sections (deep trench persists at low sea
  level); bamboo raft build → cordage close → founding-group boarding → paddle
  out, home shore shrinking. Next: batch 15 = beat24m01–beat26m02.
- Batch 15 (2026-11-05): beat24m01–beat26m02. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch15.jpg.
  Voyage payoff (awe, deliberate paddling, decisive point), thriving Australian
  camp (monolith backdrop), Madjedbebe rock shelter (tools + ochre, no
  paintings), pre-wheel raft, turn-north warm→cold transition, advancing ice
  sheets. New location locked: ice-age north (cold blue). Next: batch 16 =
  beat27m01–beat29m02.
- Batch 16 (2026-11-05): beat27m01–beat29m02. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch16.jpg.
  Glacier freeze, sea drop (exposed seabed, tall cliff band), building-silhouette
  scale metaphor (intentional, wordless), broad Beringia emergence (waterfalls
  off rising plain), mammoth-steppe reveal (mammoths + bison design locked in
  continuity.md), crossed-out rope-bridge misconception (X mark + thought
  bubble, no text). Next: batch 17 = beat29m03–beat30m03.
- Batch 17 (2026-11-05): beat29m03–beat30m03. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch17.jpg.
  Beringia-as-country aerials (tiny family for scale), mammoth/horse/river
  steppe, settled camp (camp design + elder reused, generations), hidden-ocean
  cutaway (unaware camp above, fish below), family standing in America,
  unbroken land (no crossing), walking east behind bison/mammoths with packs.
  Wild horses added to Beringia fauna set. Next: batch 18 = beat31m01–beat32m02.
- Batch 18 (2026-11-05): beat31m01–beat32m02. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch18.jpg.
  Twin ice walls block south, open coast, kelp-forest underwater (all four
  foods), aerial food highway (no road), skin boats hugging coast (new design
  locked in continuity.md), corridor waiters at ice gap, wind/light-break
  change beat, sprint with motion streaks. Next: batch 19 = beat33m01–beat34m05.
- Batch 19 (2026-11-05): beat33m01–beat34m05. 8/8 accepted first pass, 0 QC
  rejects, 0 moderation blocks. Contact sheet: sheets/contact_batch19.jpg.
  White Sands kids' footprints in mud → teens splashing by the lake →
  fossilized trackway payoff (no people, raking light) → tropical Panama →
  pour-south river-of-people (crowd stylization accepted) → rainforest
  threading → Andes pass (breath puffs, condor) → continental-spine aerial.
  Locations locked: White Sands, tropical Panama/rainforest, Andes, Tierra del
  Fuego (pre-logged); bamboo-raft design row added (backlog cleared).
  Next: batch 20 = beat35m01–beat36m03.
- Batch 20 (2026-11-05): beat35m01–beat36m03. 7/8 first pass + 1 repair PASS
  (1 QC reject: beat36m02 map had modern political borders → re-rolled with
  plain-silhouette/no-internal-lines clause, PASS; 0 moderation blocks).
  Contact sheet: sheets/contact_batch20.jpg. Tierra del Fuego arrival → last
  headland → Antarctica ice line across the sea → empty ocean "no more land"
  → quiet bookend (lone figure from behind, footprint trail, mirrors opening
  beach) → wordless glowing-path map (ice→tip) → crawl-vs-sprint world map →
  rich-land payoff (bison + guanacos, family upright). Map-border drift lesson
  logged in continuity.md. Next: batch 21 = beat36m04–beat38m01.
- Batch 21 (2026-11-05): beat36m04–beat38m01. 6/8 first pass + 2 repair PASS
  (2 QC rejects: beat37m02 full-body landscape → close bust portrait;
  beat38m01 route confined to Africa → full faint Africa→TdF route with short
  bright lifetime segment; 0 moderation blocks). Contact sheet:
  sheets/contact_batch21.jpg. "It runs" ancient sprint; modern walker introduced
  (design locked in continuity.md: olive shirt, dark trousers, boots, small
  pack, stick, beard — separate from ancient protagonist); Ethiopia departure;
  wordless 42,000 km route map; seasons-passing; still not done; one-lifetime
  map. Portrait + lifetime-map drift lessons logged. Next: batch 22 =
  beat38m02–beat39m06.

## Declared exceptions / reject log
- beat03m01_r0: REJECTED (anachronistic paving + forest drift). Fixed r1, accepted.
- beat05m02_r0: REJECTED (anachronistic megalith monument). Fixed r1, accepted.
- beat06m02_r0: REJECTED (feet drifted to tan boot-like shapes). Fixed r1, accepted.
- beat07m01_r0: REJECTED (extra limb-like lines in frame corners). Fixed r1, accepted.
- beat08m01_r0: REJECTED (baked-in black letterbox bars). Fixed r1, accepted.
- beat08m02_r0: REJECTED (gibberish pseudo-text annotations/arrows). Fixed r1, accepted.
- beat15m01_r0: REJECTED (conifer/pine-forest background drift). Fixed r1, accepted.
- beat15m06_r0: REJECTED (conifer/pine-forest background drift). Fixed r1, accepted.
- Reject sources kept locally in frames/rejects/ (gitignored); audit trail in
  contact sheets. No DECLARED EXCEPTIONS (all frames eventually passed).
