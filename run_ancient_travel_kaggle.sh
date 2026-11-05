#!/usr/bin/env bash
# STATE 6 Kaggle runner — ancient_travel_video
#
# Run INSIDE a Kaggle notebook (internet ON). The workspace never runs TTS;
# kaggle/preflight.py and kaggle/run.py enforce that themselves.
#
#   bash run_ancient_travel_kaggle.sh preflight   # Phase 0 calibration only
#   bash run_ancient_travel_kaggle.sh dry         # Phase 4 measure + verify
#   bash run_ancient_travel_kaggle.sh render      # Phase 5 render (reuses Phase 4)
#   bash run_ancient_travel_kaggle.sh package     # ZIP deliverable (after Gate 6)
#
# Extra flags after `render` are passed to kaggle/run.py, e.g.
#   bash run_ancient_travel_kaggle.sh render --allow-reduced-precision
# Only pass approval flags after the measured timings have been reviewed.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO"
MODE="${1:-help}"
shift || true

install_deps() {
  pip install -q --upgrade --force-reinstall edge-tts pyyaml pillow imageio-ffmpeg
  python -c "import edge_tts; print('edge-tts', edge_tts.__version__)"
}

prepare_frames() {
  # Bridge the committed quantized PNG spine into the reusable prep tool.
  # assets/frames/source is gitignored; JPGs are derived on Kaggle, not committed.
  mkdir -p assets/frames
  if [ ! -e assets/frames/source ]; then
    ln -s ../../ancient_travel_video/frames assets/frames/source
  fi
  python tools/prep_frames.py --repo "$REPO" --strict
}

case "$MODE" in
  preflight)
    install_deps
    python kaggle/preflight.py
    ;;
  dry)
    install_deps
    prepare_frames
    python kaggle/run.py --dry-run --repo "$REPO"
    ;;
  render)
    prepare_frames
    python kaggle/run.py --out "$REPO/ancient_travel_FINAL.mp4" --repo "$REPO" "$@"
    ;;
  all)
    # ONE-SHOT (user-approved): measure -> render -> measured youtube.txt -> ZIP.
    # Carries explicit approval flags end-to-end:
    #   --allow-reduced-precision : dry-run rc=5 means a handful of words were
    #     interpolated (engine chunking); all frame anchors must still be
    #     'exact/measured' - check the printed table.
    #   --allow-transition-overlap: micro-beat holds shorter than the 1.0 s
    #     fade overlap their neighbours instead of aborting the render.
    # All numbers still come from measured Phase 4 timing (build/timings.csv).
    install_deps
    prepare_frames
    run_dry_tolerant() {
      set +e
      python kaggle/run.py --dry-run --repo "$REPO"
      local rc=$?
      set -e
      case "$rc" in
        0) ;;
        5) echo "NOTE: Gate 4 rc=5 (diagnostics flagged, e.g. interpolated words)." \
               "Proceeding under explicit --allow-reduced-precision approval." ;;
        *) exit "$rc" ;;
      esac
    }
    if [ ! -f "$REPO/build/manifest.json" ]; then
      run_dry_tolerant
    fi
    set +e
    python kaggle/run.py --out "$REPO/ancient_travel_FINAL.mp4" --repo "$REPO" \
      --allow-transition-overlap --allow-reduced-precision
    RENDER_RC=$?
    set -e
    if [ "$RENDER_RC" -ne 0 ]; then
      echo "render failed (rc=$RENDER_RC) - re-measuring once, then retrying render"
      run_dry_tolerant
      python kaggle/run.py --out "$REPO/ancient_travel_FINAL.mp4" --repo "$REPO" \
        --allow-transition-overlap --allow-reduced-precision
    fi
    python ancient_travel_video/make_youtube_txt.py
    bash "${BASH_SOURCE[0]}" package
    ;;
  package)
    python - <<'PY'
from pathlib import Path
import zipfile, sys
repo = Path.cwd()
video = repo / "ancient_travel_FINAL.mp4"
youtube = repo / "ancient_travel_video" / "youtube.txt"
if not video.exists():
    sys.exit("package: ancient_travel_FINAL.mp4 missing — render first")
if "PENDING" in youtube.read_text(encoding="utf-8"):
    sys.exit("package: youtube.txt still PENDING — write measured publish copy first")
out = repo / "ancient_travel_DELIVERABLE.zip"
files = [
    video,
    repo / "ancient_travel_video" / "thumbnail.jpg",
    youtube,
    repo / "ancient_travel_video" / "script.md",
    repo / "ancient_travel_video" / "metadata.json",
    repo / "build" / "timings.csv",
    repo / "build" / "timing.json",
    repo / "build" / "manifest.json",
]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        if not f.exists():
            sys.exit(f"package: missing {f}")
        z.write(f, f.relative_to(repo))
print("package:", out, f"{out.stat().st_size/1e6:.1f} MB")
PY
    ;;
  *)
    sed -n '2,18p' "${BASH_SOURCE[0]}"
    exit 2
    ;;
esac
