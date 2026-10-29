# STATE — Apocalypse Survival Video

| File | Status | Notes |
|---|---|---|
| README.md | ✅ Created | |
| brief.md | ✅ Created | |
| script.md | ✅ Approved | 842 words, ~4.5 min |
| visuals.csv | ✅ Approved | 68 frames (s01–s68), word-reactive |
| metadata.json | ✅ Created | |
| youtube.txt | ✅ Created | Chapters TBD post-render |
| STATE.md | ✅ Complete | |
| frames/ | ✅ 68/68 | All generated and committed |
| refs/ | ✅ Created | 3 anchors + continuity.md |
| continuity.md | ✅ Created | Style tokens locked |
| run_apocalypse_survival_kaggle.sh | ✅ Created | Kaggle runner script |

## Kaggle Handoff

```bash
!rm -rf newrepo2
!git clone --depth 1 --branch arena/138cc5e0-newrepo2 https://github.com/AsuraXP/newrepo2.git
!bash newrepo2/run_apocalypse_survival_kaggle.sh
```

## Frame Summary
- 68 frames covering: hook → shock → water → shelter → food → security → mental test → checklist → groups → closer
- Style: stick-figure cartoon (user-provided references)
- All frames word-reactive: each illustrates the exact phrase being narrated
