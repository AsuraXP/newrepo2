# Story video: zombie apocalypse farm

187 word-reactive frames and a second-person narration. Source material and
visuals live here; all TTS, audio mixing and encoding run **only on Kaggle**.

The offline source check is `python story_video/kaggle_render.py --preflight`
(requires Pillow). It checks CSV/script continuity and all frame files without
generating audio. On Kaggle, run `bash run_story_kaggle.sh` from the repository
clone with internet enabled. The runner fast-forwards the session branch,
installs dependencies, verifies the voice and frames, synthesizes one narration
stream with word timestamps, pads frames before concatenation, and writes
`/kaggle/working/story_DELIVERABLE.zip`. It refuses approximate timing if
word-boundary recovery is incomplete. Cuts are based on the next spoken word's
start; natural gaps between words are held on the preceding frame. Output is
30 fps, so cuts are quantized to the video frame grid.
