# Continuity

## Reference candidates — awaiting approval

- `refs/character_test.png`: "Create one clean character reference frame for a zombie apocalypse survival story. Match the supplied references closely: hand-drawn 2D stick figure with a round white head, black dot eyes, simple expressive face, uneven bold black outlines, thin black limbs, flat muted colors. Show one young adult survivor, gender-neutral, with a muted olive jacket and dark backpack, standing full body, anxious but determined, on a simple pale warm background. No text, no watermark. Landscape 16:9."
- `refs/farm_test.png`: "Create one establishing reference frame for a self-sufficient family farm in a zombie apocalypse story. Match the supplied references closely: hand-drawn 2D animation, uneven bold black outlines, flat muted colors, simple storybook backgrounds. A modest farmhouse and barn, closed wooden gate and fence, solar panels, a water well, vegetable rows, a chicken enclosure and a goat; distant windmill, dusk sky. Clear readable composition, no people, no text, no watermark. Landscape 16:9."

## Proposed invariants

- Style block: "hand-drawn 2D stick figure with a round white head, black dot eyes, simple expressive face, uneven bold black outlines, thin black limbs, flat muted colors."
- Survivor block: "one young adult survivor, gender-neutral, with a muted olive jacket and dark backpack" (jacket and backpack only after packing, as story requires).
- Farm: cream farmhouse, red barn, closed wooden gate and fence on arrival, solar panels, well, vegetable rows, chickens, goat, distant windmill. Gate opens when protagonist enters; house door closes after the encounter.
- Palette: warm beige and subdued olive, brown, gray, red and dusk blue; black outlines.
- Infected: recognizable as people with vacant expressions and unsteady movement; grandfather remains recognizable as an older family member. Avoid incidental gore and illegible text.
- Reference inputs for frame generation: approved character and relevant location anchor, plus optional prior approved frame. Spell out story state in each prompt. Set dressing is secondary to character and story continuity.

## Moderation substitutions

None so far.

## Approved anchors

User approved `character_test.png` and `farm_test.png` as character and farm anchors. No new anchors in batch 1. Bedroom location reference remains to be established.

## Batch 1 QC

- `beat02m02` initial rejected: protagonist ran away from the farm; changed camera clause to rear view running toward gate. Replacement accepted with minor drift: "beat02m02 hair tufts vs character anchor bald round head".
- `beat04m01` initial rejected: jacket and backpack appeared in the room despite the earlier story state; changed visibility clause. Replacement remains pending: "beat04m01 farm windmill and barn visible through bedroom window vs script's town home before journey". Repair on next turn; do not accept this candidate.
- Bedroom background varies between `beat03m01` and `beat04m02` (window/bed layout); create a consistent town bedroom reference for later frames. No moderation blocks.

## Batch 2 QC

- `beat04m01`: Previous pending candidate rejected because farm buildings appeared outside the town bedroom; changed the window clause to show town apartments and added `beat03m01` as prior reference. Replacement accepted. The earlier candidate remains visible on the batch 1 contact sheet.
- `beat09m01` initial rejected: "beat09m01 olive jacket worn before departure vs morning story state bare torso in beat07m03". Changed the clothing clause to require a plain black stick-figure torso. Replacement accepted.
- Minor drift noted: "beat07m01 gray shirt vs beat07m03 bare black stick torso"; clothing was not specified for this early scene. "beat06m02 survivor present in foreground vs requested empty street"; the nightfall beat is still clear.
- No new anchors; no moderation blocks.

## Batch 3 QC

- `beat11m02` initial rejected: "beat11m02 survivor wears olive jacket and backpack during news at home vs beat09m01 bare stick torso before departure". Changed camera clause to show broadcast only; replacement accepted.
- `beat12m01` initial rejected: "beat12m01 survivor wears jacket and backpack and farm windmill appears through window vs town apartment before journey". Changed camera clause to broadcast only; replacement accepted.
- `beat11m01` pending: "beat11m01 olive sleeve and backpack visible vs beat09m01 bare stick torso before departure". Needs repair.
- `beat12m02` and `beat13m01` pending: "survivor appears in street footage vs script survivor watching TV at home". Need repairs without foreground survivor.
- No new anchors or moderation blocks. Candidate and rejected frames are retained in `refs/pending` and `refs/rejects`.

## News corrections after user feedback

The survivor does not wear a jacket or backpack at home during the news; departure clothing and packed backpack appear only later, after packing (except the opening foreshadowing shots). The three previously pending shots were repaired and accepted: `beat11m01` now shows the broadcast only; `beat12m02` shows the smoky street with no foreground survivor; `beat13m01` shows fleeing civilians rather than the survivor in the street. Prior rejects remain in `refs/pending`. No new anchors.

## Batch 4 QC

- `beat15m01` initial rejected: "beat15m01 survivor wears olive jacket during news at home vs beat09m01 bare torso before departure". Changed composition clause to broadcast only; replacement accepted.
- `beat15m02` initial rejected: "beat15m02 TV news ticker contains gibberish vs no text rule". Changed TV clause to prohibit captions and tickers; replacement accepted. Minor drift: "beat15m02 beige shirt and gray trousers vs beat09m01 bare stick torso"; no jacket or backpack is worn.
- `beat15m03` pending: "beat15m03 two televisions in room vs beat09m01 one TV"; repair next turn with exactly one television. No new anchors or moderation blocks.

## Batch 5 QC

- `beat15m03`: initial rejected in batch 4 for two TVs; changed the TV-count clause to exactly one. Replacement accepted, no backpack worn.
- `beat21m03`: initial rejected: the bodies were not discernible on a distant TV in a room. Changed composition clause to footage-only. Retry still pending: "beat21m03 retry has LIVE/GNN logos and news ticker vs no text rule". Two candidate versions retained; retry next turn with a single-clause ban on broadcast graphics. One re-roll has failed for this shot.
- `beat20m02`: blank ticker rectangle, no legible text; monitor for broadcast overlay drift. No new anchors; no moderation blocks.

## Batch 6 QC

- `beat21m03`: second retry accepted; changed broadcast graphics clause to prohibit all text and used street footage reference. Smoke and motionless figures are visible without logos.
- `beat26m01` initial rejected: floating, disconnected arm vs body. Changed composition clause to connected arm in medium full-body view. Retry remains pending: "beat26m01 backpack on couch before packing vs no visible packed bag during news". One failed re-roll.
- `beat24m01` and `beat27m02` pending: "backpack sitting in living room during news vs no visible packed bag during news". Neither was re-rolled this turn.
- Story-state refinement: Before the decision to leave and packing, do not depict a packed backpack anywhere in the room; never wear the jacket or backpack until departure. Earlier accepted `beat08m01` and `beat10m01` also show a backpack in the room and must be reviewed/repaired for this stronger rule.
- No new anchors or moderation blocks.

## Batch 7 QC and moderation

- `beat08m01`, `beat10m01`, `beat24m01`, `beat26m01`, and `beat27m02` regenerated without the prematurely visible backpack. `beat26m01` now has connected limbs. All accepted.
- `beat28m01` initial rejected: "beat28m01 detached foreground hand holding a can vs survivor's hands at sides". Changed action clause to hands at sides; replacement accepted.
- `beat29m01` first generation was blocked by moderation; the service did not identify a blocked word, so none can be reported. Changed "half a loaf of bread" to "a small piece of bread"; retry succeeded and was accepted.
- Minor clothing drift: "beat26m01 white shirt vs beat09m01 bare stick torso"; no jacket or backpack appears. `beat28m01` and `beat29m01` show a gray shirt matching the earlier kitchen frame `beat07m01`. No new anchors.

## Batch 8 QC

- `beat34m01` initial rejected: "beat34m01 food packets replace the cans and bread established in beat32m02". Changed the food description to specify the same cans, half loaf and bottles; used the previous accepted inventory frame as reference. Replacement accepted.
- Minor continuity drift: quantities and grouping of cans and bottles vary across `beat30m01`–`beat34m01`; no backpack or jacket appears. New anchor: none. No moderation blocks.

## Batch 9 QC

- `beat37m01` initial rejected: "beat37m01 static appears before emergency alert vs beat39m01 alert then beat39m02 static". Changed TV screen clause to an empty news studio; replacement accepted.
- Minor drift: "beat37m01 blue news studio vs beat38m01 muted green studio"; both show an empty desk, and set dressing is secondary. `beat39m01` represents the emergency message as a text-free alert icon so no illegible text appears. No new anchors or moderation blocks.

## Batch 10 QC

- `beat44m01` initial rejected: "beat44m01 arm stretches beyond top of image vs anchor's normal short stick-figure limbs". Changed close-up clause to medium full-body view with two natural arms; replacement accepted.
- `beat45m01` combines the isolated conjunction "And" with the following phrase into one meaningful beat. This reduced the CSV total from 196 to 195; no narration was removed.
- `beat46m01` shows the farm in a distant imagined view; actual location remains the approved farm reference. No new anchors or moderation blocks.

## Batch 11 QC

- `beat48m02` initial rejected: "beat48m02 grandfather lacked gray hair and mustache vs beat48m01 gray side hair and gray mustache". Changed grandfather clause to match `beat48m01` and used it as prior approved frame; replacement accepted.
- `beat50m01` initial rejected: "beat50m01 disconnected floating lightbulb diagram vs solar panels powering farmhouse lights". Changed illustration clause to illuminated farmhouse windows; replacement accepted.
- Recurring grandfather reference: `beat48m01` (gray side hair, gray mustache, brown vest over pale shirt); use alongside approved character and farm anchors for later grandfather scenes. Minor drift: `beat47m01` vest is lighter than `beat48m01`; both retain gray side hair and mustache. No moderation blocks.

## Batch 12 QC

- `beat53m04` initial rejected: "beat53m04 survivor wears olive jacket and backpack during pre-packing thought vs beat49m01 still at home before packing". Changed composition clause to stormy farm only, no person or thought bubble; replacement accepted.
- Minor set-dressing drift: "beat53m04 barn roof lacks solar panels vs farm anchor roof panels"; focus is the sturdy barn during an imagined storm, not the system detail. `beat54m01` introduces the backpack only at the scripted grab; `beat55m01` packs it without wearing it. No new anchors or moderation blocks.

## Batch 13 QC

- `beat55m04` initial rejected: "beat55m04 two olive jackets vs single jacket in packing sequence". Changed the held jacket clause to specify the only jacket in the room. Retry pending: "beat55m04 retry olive pullover has no zipper vs character anchor olive zip-front jacket". One failed re-roll.
- `beat57m02` initial rejected: "beat57m02 curtains open vs beat27m02 curtains closed". Changed story-state clause to fully shut curtains; replacement accepted.
- Grandmother proposed recurring appearance in `beat58m01`: gray hair bun, muted lavender cardigan, round white face. No other new anchor or moderation blocks.

## Batch 14 QC

- `beat55m04` repaired: changed garment clause to specify an open zip-front jacket and collar. Replacement matches olive jacket anchor and is accepted.
- `beat59m01` first generation produced no image (service error, no moderation block). Simplified the two-thought-bubble clause to a survivor lowering a silent phone; retry accepted.
- `beat60m01` pending: "beat60m01 white filled arms with five-finger hands vs beat57m02 black stick limbs and mitten-like hands". No repair budget remains this turn.
- `beat63m01` begins outdoor sequence: survivor now wears olive jacket and dark backpack as departure has occurred. No new anchors or moderation blocks.

## Batch 15 QC

- `beat60m01` repaired: specified solid black stick arms and mitten hands instead of the prior filled white arms. Accepted.
- `beat67m03` initial rejected: "beat67m03 white five-fingered hand vs anchor black mitten hands". Changed hand clause to solid black mitten shape; replacement accepted.
- `beat66m03` has a distant gray swarm behind fleeing civilians, though individual expressions are indistinct at this distance. No new anchors or moderation blocks.

## Batch 16 QC

- `beat70m02` initial rejected: "beat70m02 driver door open vs story state shut before pulling away in beat70m03". Changed door clause to fully shut with window visible; replacement accepted.
- Vehicle anchor: `beat70m01`, dark slate-blue compact hatchback, rounded body and five doors. The driver's door is open only while entering, then closed while driving. Survivor wears olive jacket; dark backpack travels with them.
- Minor drift: "beat71m01 car looks sedan-like from the front vs beat70m01 hatchback side profile"; subsequent shots should match the accepted vehicle anchor. No moderation blocks.

## Batch 17 QC

- `beat76m01` initial rejected: "beat76m01 tiny storefront lettering vs no text rule". Changed storefront clause to blank facades, no signage; replacement accepted.
- `beat77m02` initial rejected: "beat77m02 car faces lone person rather than clearly steering past". Changed action/composition clause to an elevated view showing the car passing with a safe gap; replacement accepted.
- `beat77m01` pending: "beat77m01 dusk purple sky vs beat76m01 and beat77m02 pale daytime sky"; repair next turn for matching daylight. Both repair slots used.
- Merged isolated "Once," with the following phrase (now `beat77m01`), reducing total moments from 195 to 194 without omitting narration. No new anchors or moderation blocks.

## Batch 18 QC

- `beat77m01` repaired: changed sky clause to pale daytime for consistency with `beat77m02`; replacement accepted.
- `beat82m01` initial rejected: "beat82m01 car appears ahead of walker despite being left behind". Changed composition clause to keep car and farm out of view; replacement accepted.
- `beat81m01` pending: "beat81m01 farm and windmill clearly visible before the scripted windmill reveal vs later story beat". Both repair slots used; repair next turn with the farm and windmill out of frame.
- `beat80m03` has tiny indistinct distant buildings, but the farm is not clearly established there. No new anchors or moderation blocks.
