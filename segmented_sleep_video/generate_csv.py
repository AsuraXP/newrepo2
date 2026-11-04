import csv
import re

with open('segmented_sleep_video/script.md') as f:
    lines = [l.strip() for l in f if l.strip()]

rows = []
# We will create visual prompts that strictly maintain the Ink Explainer stickman aesthetic
# Style anchor constant:
STYLE = "Ink Explainer style, minimalist stick figure with smooth circular white head, bold expressive black ink facial features and thin stick limbs, warm cozy textured parchment background, cinematic warm lighting"

# We map each beat into slide_id, moment, moment_text, visual_prompt
slide_id = 1
moment_id = 1

for line in lines:
    parts = re.split(r'(?<=,)|(?<=;)|(?<=—)', line)
    clean_parts = [p.strip() for p in parts if p.strip()]
    for p in clean_parts:
        # Generate appropriate reactive visual prompt based on content
        txt = p.lower()
        if "3:15" in txt or "digital clock" in txt:
            desc = "a glowing red digital alarm clock on a wooden nightstand reading 03:15 in a pitch dark bedroom, minimalist ink lines"
        elif "wake up" in txt or "eyes snapping open" in txt:
            desc = "stick figure in bed with duvet, wide shocked eyes snapping open in the dark, startled comic expression"
        elif "completely silent" in txt or "room is" in txt:
            desc = "wide shot of dark quiet bedroom, lonely stick figure sitting up in bed under dim ambient window glow"
        elif "roll onto" in txt:
            desc = "stick figure lying sideways on blue mattress, tossing and turning restlessly"
        elif "punch your pillow" in txt:
            desc = "stick figure angrily punching fluffy white pillow with cartoon action lines, frustrated frown"
        elif "squeeze your eyes shut" in txt:
            desc = "close-up of stick figure face tightly squeezing eyes shut with squint marks, trying desperately to sleep"
        elif "five minutes pass" in txt or "ten minutes pass" in txt:
            desc = "stick figure lying flat on back staring blankly straight up at bedroom ceiling, bored expression"
        elif "mind begins racing" in txt:
            desc = "stick figure with spiraling swirling comic thought bubbles, tangled scribble lines over head depicting racing thoughts"
        elif "worry about your morning alarm" in txt:
            desc = "stick figure looking terrified at an imaginary ringing alarm clock icon hovering in the air"
        elif "meetings at work" in txt:
            desc = "stick figure picturing stressful office calendars, spreadsheet charts, and work deadlines hovering overhead"
        elif "brain is hopelessly broken" in txt:
            desc = "stick figure clutching circular head with cartoon question marks, looking defeated and broken"
        elif "pick up your phone" in txt or "squinting against" in txt:
            desc = "stick figure in dark illuminated by blinding bright blue smartphone screen glare, squinting and wincing"
        elif "wondering why" in txt or "normal human being" in txt:
            desc = "stick figure with droopy tired eyes staring at phone screen on couch, slouching in utter exhaustion"
        elif "astonishing truth" in txt or "not broken" in txt:
            desc = "stick figure standing proudly with a glowing lightbulb star idea above head, confident smirk, warm golden halo circle"
        elif "body is doing exactly" in txt or "evolved to do" in txt:
            desc = "stick figure silhouette transitioning into an ancient human hunter-gatherer silhouette, evolutionary timeline line"
        elif "hundreds of thousands of years" in txt or "virtually all of human existence" in txt:
            desc = "vast prehistoric landscape timeline stretching back through thousands of years, sun and moon cycling"
        elif "eight uninterrupted hours" in txt or "not normal" in txt:
            desc = "stick figure pointing sceptically at a modern 8-hour clock schedule crossed out with a red X"
        elif "even considered desirable" in txt:
            desc = "antique scroll illustration showing that 8 hours uninterrupted sleep did not exist in old eras"
        elif "segmented sleep" in txt or "biphasic sleep" in txt:
            desc = "graphic diagram showing First Sleep, an awake midnight window, and Second Sleep marked with moon and sun icons"
        elif "two distinct shifts" in txt:
            desc = "two separate cozy sleeping stick figures separated by an awake figure enjoying peaceful midnight tea"
        elif "magical" in txt or "peaceful window of wakefulness" in txt:
            desc = "stick figure sitting serenely under starry midnight sky, peaceful gentle smile, calm tranquil aura"
        elif "journey back" in txt or "world before lightbulbs" in txt:
            desc = "time vortex portal opening from modern city apartment into a prehistoric wilderness mountain valley"
        elif "prehistoric cave" in txt or "outside a prehistoric cave" in txt:
            desc = "primitive stickman dressed in ragged fur pelt sitting near mouth of ancient rock cave under twinkling starry sky"
        elif "sun dips below" in txt or "pitch-black stillness" in txt:
            desc = "ancient landscape sunset, orange sun sinking beneath mountain ridge leaving starry deep indigo night sky"
        elif "without electricity" in txt or "street lamps" in txt:
            desc = "dark prehistoric forest and mountains with complete absence of modern artificial light, pristine dark wilderness"
        elif "gather around the dying embers" in txt or "campfire" in txt:
            desc = "group of cute primitive stick figures in fur clothes warming hands around crackling orange campfire"
        elif "floods with melatonin" in txt:
            desc = "stylized diagram of stick figure brain releasing glowing calming blue melatonin particles in the dark"
        elif "crawl into your bedding" in txt or "dry grasses" in txt:
            desc = "primitive stick figure curling up cozily inside cave on soft pile of dried grasses and warm animal fur pelt"
        elif "first sleep" in txt:
            desc = "primitive stick figure soundly asleep in cave with floating 'Zzz' notes, labeled 'FIRST SLEEP', serene smile"
        elif "four hours" in txt or "deep slow-wave" in txt:
            desc = "smooth slow brainwave graph drawn across starry cave wall, restorative deep delta sleep waves"
        elif "repairing tissues" in txt or "restoring cellular" in txt:
            desc = "close-up of stick figure body glowing with soft healing golden light, battery recharging icon filling up"
        elif "long day of hunting" in txt:
            desc = "ancient stick figure carrying a simple wooden spear across grassy prehistoric plains under the afternoon sun"
        elif "around midnight" in txt or "something remarkable" in txt:
            desc = "cave entrance under full moon and bright constellations at exact midnight, mystical quiet atmosphere"
        elif "wake up gently" in txt or "not with a jolt" in txt:
            desc = "ancient stick figure opening eyes slowly in cave bed, calm peaceful expression, resting chin on hands"
        elif "feeling remarkably calm" in txt or "alert" in txt:
            desc = "ancient stick figure sitting up smoothly, feeling refreshed, clear-eyed, stretching arms contentedly"
        elif "clan members stir" in txt or "around you" in txt:
            desc = "multiple cave stick figures gently stretching and sitting up together in the warm amber cave glow"
        elif "no one panics" in txt or "curses their insomnia" in txt:
            desc = "modern stick figure stressing vs ancient cave stick figure smiling peacefully side by side contrast"
        elif "anticipated" in txt or "deeply valued" in txt:
            desc = "ancient stick figure looking up at night stars through cave opening with sense of wonder and deep gratitude"
        elif "prolactin" in txt or "hormone" in txt:
            desc = "scientific diagram showing gentle hormone molecules labeled Prolactin creating a soothing golden aura around stick figure"
        elif "twilight state" in txt or "dreaming and reality" in txt:
            desc = "ethereal dream clouds floating softly between stick figure head and starry cosmos, half-awake bliss"
        elif "anything they wanted" in txt or "waking hour" in txt:
            desc = "panoramic view of cave interior showing different primitive stick figures doing relaxed quiet midnight activities"
        elif "tended the embers" in txt or "fresh logs" in txt:
            desc = "ancient stick figure placing a small dry log onto cozy campfire, warm yellow sparks dancing upward"
        elif "keep predators away" in txt:
            desc = "distant glowing animal eyes outside dark cave edge staying back from the safe bright campfire perimeter"
        elif "reflecting on dreams" in txt:
            desc = "ancient stick figure sitting cross-legged by fire gazing pensively into flames with soft dream bubble above"
        elif "elders shared quiet stories" in txt or "ancestral lore" in txt:
            desc = "wise elder stick figure with simple walking stick whispering ancient tales to listening young stick figure by fire"
        elif "canopy of starlight" in txt:
            desc = "wide breathtaking view looking out from cave archway at majestic Milky Way galaxy glowing across dark sky"
        elif "intimacy" in txt or "couples" in txt:
            desc = "two affectionate stick figures wrapped together under warm fur pelt in secluded quiet cave alcove"
        elif "philosophers and storytellers" in txt or "creative hour" in txt:
            desc = "ancient stick figure drawing expressive charcoal cave art of running bison on rocky stone wall by firelight"
        elif "conscious ego was soft" in txt or "imaginations ran wild" in txt:
            desc = "creative spark burst illuminating stick figure face with wondrous colorful swirling shapes and wild inspiration"
        elif "ancient greece" in txt or "medieval europe" in txt or "historical records" in txt:
            desc = "antique historical manuscript parchment showing classical Greek figures and medieval villagers resting"
        elif "roger ekirch" in txt:
            desc = "modern stickman historian wearing glasses examining a giant dusty leather-bound historical archive book with magnifying glass"
        elif "hundreds of routine references" in txt:
            desc = "stack of old yellowed books and diary pages highlighting printed words 'First Sleep' and 'Second Sleep'"
        elif "sixteenth-century england" in txt:
            desc = "cozy 16th century timber cottage bedroom, stickman in nightcap waking up by gentle candle glow"
        elif "warm herbal broth" in txt or "smoke a pipe" in txt:
            desc = "stickman in nightshirt sipping steaming mug of herbal tea by stone fireplace, warm cozy cottage vibes"
        elif "chat with their neighbors" in txt:
            desc = "two friendly neighbor stickmen leaning over low wooden garden fence talking quietly in lantern light"
        elif "read by candlelight" in txt:
            desc = "stickman in nightcap reading an open parchment book illuminated by a single warm flickering wax candle"
        elif "medicines taken" in txt or "twice as effective" in txt:
            desc = "antique apothecary bottle and spoon labeled midnight herbal tonic glowing with healing restorative sparks"
        elif "pleasantly drowsy" in txt or "settled back" in txt:
            desc = "stickman yawning peacefully, setting candle aside, and pulling cozy patchwork quilt up to shoulders"
        elif "second sleep" in txt or "morning sleep" in txt:
            desc = "stick figure deep asleep under cozy blanket, labeled 'SECOND SLEEP', dreaming blissfully"
        elif "morning sun crested" in txt:
            desc = "golden sunrise glowing through quaint bedroom window, dawn birds chirping, gentle waking light"
        elif "destroyed this ancient" in txt or "what destroyed" in txt:
            desc = "dramatic stormy shadow dividing ancient tranquil starlight and modern blinding artificial factory glare"
        elif "artificial illumination" in txt or "one single invention" in txt:
            desc = "first gas street lamp flaring to life on a cobblestone street, casting harsh unnatural yellow glow"
        elif "gas street lighting" in txt or "london and paris" in txt:
            desc = "19th century London cobblestone boulevard lined with glowing gas street lanterns, crowds walking at night"
        elif "bustling economic frontier" in txt or "taverns" in txt:
            desc = "busy bustling Victorian nighttime street with brightly lit tavern windows, theater signs, and noisy horse carriages"
        elif "thomas edison" in txt or "electric bulb" in txt:
            desc = "stick figure inventor holding up a brilliantly glowing modern incandescent tungsten lightbulb"
        elif "darkness was eradicated" in txt:
            desc = "modern city skyline illuminated by thousands of electric windows, billboards, and streetlamps erasing the night stars"
        elif "fooled the human pineal gland" in txt or "melatonin production" in txt:
            desc = "diagram of human eye bombarded by blue light rays blocking melatonin droplet production, pineal gland confused"
        elif "bedtimes hours later" in txt:
            desc = "stick figure sitting awake under bright overhead electric chandelier at midnight looking exhausted and drained"
        elif "industrial revolution" in txt or "factory clock" in txt:
            desc = "imposing Victorian industrial brick factory with smoking chimneys and a giant ticking mechanical pocket watch"
        elif "rigid schedule" in txt or "workers could no longer" in txt:
            desc = "line of weary stick figure factory workers marching under the shadow of a giant ticking clock tower"
        elif "compress their biological recovery" in txt or "eight-hour block" in txt:
            desc = "mechanical metal vice clamp squeezing a clock schedule down into a rigid 8-hour block labeled 'SLEEP SHIFT'"
        elif "early twentieth century" in txt or "vanished from public" in txt:
            desc = "old vintage poster of segmented sleep fading into dust and vanishing into thin air"
        elif "brings us right back to you" in txt or "lying wide awake" in txt:
            desc = "modern stick figure lying awake in bedroom at 3:00 AM, glowing clock softly visible, looking thoughtful"
        elif "ancient biology is simply remembering" in txt:
            desc = "stick figure in modern bed overlaid with ghostly transparent silhouette of ancient cave ancestor smiling beside them"
        elif "glowing phone in frustration" in txt:
            desc = "stick figure deliberately putting glowing smartphone face down on wooden nightstand, choosing calm stillness"
        elif "do not panic" in txt or "tomorrow is ruined" in txt:
            desc = "stick figure releasing a deep breath with gentle musical calm waves floating across quiet dark bedroom"
        elif "welcome the ancient intermission" in txt or "ancestors treasured" in txt:
            desc = "stick figure smiling serenely by dark window looking out at peaceful midnight stars, feeling connected to ancestors"
        else:
            desc = f"stick figure illustrating {p.lower()}"

        full_prompt = f"{STYLE}, {desc}"
        rows.append({
            "slide_id": slide_id,
            "moment": moment_id,
            "moment_text": p,
            "visual_prompt": full_prompt
        })
        moment_id += 1
    slide_id += 1

with open('segmented_sleep_video/visuals.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["slide_id", "moment", "moment_text", "visual_prompt"])
    writer.writeheader()
    writer.writerows(rows)

print(f"visuals.csv successfully created with {len(rows)} micro-beat rows across {slide_id-1} slides!")
