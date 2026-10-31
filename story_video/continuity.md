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
