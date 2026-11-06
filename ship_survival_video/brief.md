# BRIEF — ship_survival

Status: **proposed from `PRODUCTION.md`, awaiting user confirmation.**
Nothing in this file is approved until the user says so. Fields marked
PROPOSED are carried over from the recorded 2026-10-28 session; fields marked
PENDING have no recorded answer.

| Field | Value | Source |
|---|---|---|
| Topic / logline | Apocalypse survival aboard a ship you just boarded: crowds onboard, a few infections among passengers, still safer than land — no shore contact, and far more zombies on land than on the ship. | PROPOSED (`PRODUCTION.md`) |
| Target runtime | PENDING | no record |
| Voice + pace | `en-US-AndrewNeural`, `+10%` (Edge-TTS) | PROPOSED + spec default (`kaggle/config.yaml`) |
| Narration POV | Second person ("you open the door…") | PENDING (spec default for stories) |
| Style / look | PENDING | user must choose (hard rule: never auto-chosen) |
| Hard rules — must appear | PENDING | - |
| Hard rules — must never appear | PENDING | - |
| Captions | None | spec default |
| Aspect ratio | 16:9 (1280x720 per `kaggle/config.yaml`) | spec default |
| Platform | YouTube | PENDING |

## Fictional framing

The premise is explicitly fictional and must be narrated as such (no
real-world instructions presented as advice). Recorded with the topic.

## Pipeline note

This episode runs on the existing `vidsync/` + `kaggle/` tooling. That tooling
already implements measured, word-reactive timing; `visuals.csv` here is the
swarm-spec front end for micro-beat granularity and is converted into the
pipeline's frame manifest at the spine stage. Existing code is used, not
rewritten.
