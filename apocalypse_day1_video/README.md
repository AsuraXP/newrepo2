# Can You Survive Day One of the Zombie Apocalypse? (`apocalypse_day1_video`)

Second-person (`"you"`) survival story following Day One of a zombie outbreak from `7:12 AM` on the apartment couch through `12:00 AM` midnight inside a 30-foot stilt forestry fire-lookout cabin.

## Production Summary
- **Narration (`script.md`)**: `1,518` words (`~8m 10s` projected at `3.1 wps`; exact duration measured via Edge-TTS on Kaggle)
- **Visual Spine (`visuals.csv`)**: `162` micro-beat frames across `9` story beats (`frames/beat01m01.png` .. `frames/beat09m15.png`)
- **Art Style**: Minimalist 2D pure-white circle-head stick-figure cartoon strictly matching `refs/user_style_ref_01..03.png`
- **Thumbnail**: `thumbnail.jpg` (`16:9` high-contrast YouTube thumbnail)
- **Voice**: `en-US-AndrewNeural` at `+10%` rate (ONE continuous Edge-TTS take with `WordBoundary` alignment)
- **Render & Packaging (`../run_apocalypse_day1_kaggle.sh`)**: Executes on Kaggle (Internet ON) to synthesize audio, normalize to `-14 LUFS`, PIL pre-pad frames onto an even-dimension black RGB canvas, stitch `30fps` `libx264` `yuv420p` + `AAC 192k`, and output `/kaggle/working/apocalypse_day1_DELIVERABLE.zip`.
