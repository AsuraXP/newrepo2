# BRIEF — last_awake_video

**Working title:** You're the Only One Awake (Sleep Is Rationed)

| Field | Value |
|---|---|
| Slug | `last_awake_video` |
| Topic / logline | Sci-fi explainer: you are the last human awake aboard a station where sleep has become a scheduled, rationed resource. A second-person story with a real sleep-science backbone (circadian rhythm, sleep pressure/adenosine, sleep debt, microsleep, and what a rationed-sleep society does to a human body). |
| Format | Ink-explainer-style narrated episode (story + explainer hybrid) |
| Target runtime | 10 minutes |
| Target word count | ~1,860 words (10 × 60 × 3.1 wps) |
| Voice | `en-US-AndrewNeural` via Edge-TTS |
| Rate | `--rate=+10%` |
| Narration POV | Second person ("you") — immersive direct address, consistent throughout |
| Style / look | PENDING — user will paste an art-style reference into `refs/`. Reference is ARTSTYLE + CHARACTER ONLY, never a spatial background template. |
| Hard rules | PENDING — user to specify must-appear / must-never-appear |
| Captions | None (no burn-in) |
| Aspect ratio | 16:9 |
| Platform | YouTube (long-form) |
| Branch | `arena/94231213-newrepo2` |

## Repo conventions inherited from `docs/WORKFLOW_SPEC.md`
- Workspace never runs TTS, never mixes audio, never encodes video. Kaggle only.
- Frame count and durations are OUTPUTS of the script, measured on Kaggle from word-level
  TTS timestamps. Never hand-set a duration.
- Existing repo tooling (`vidsync/`, `kaggle/`, `tools/`) is run, never rebuilt.

## Blocking inputs
1. Hard rules (must appear / must never appear).
2. Art-style reference image → `refs/`.
