#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d /kaggle/working && -z "${KAGGLE_KERNEL_RUN_TYPE:-}" ]]; then
  echo 'ERROR: This runner may only execute on Kaggle.' >&2
  exit 1
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
BRANCH='arena/bca6e311-newrepo2'
if [[ "$(git branch --show-current)" != "$BRANCH" ]]; then
  echo "ERROR: clone and run branch $BRANCH" >&2
  exit 1
fi
# Update only by fast-forward; refuse rather than overwrite local Kaggle edits.
git fetch origin "$BRANCH"
git merge --ff-only FETCH_HEAD
if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  if [[ $(id -u) -eq 0 ]]; then
    apt-get update -qq && apt-get install -y ffmpeg
  else
    sudo apt-get update -qq && sudo apt-get install -y ffmpeg
  fi
fi
python -m pip install 'edge-tts>=7.0,<8' 'pillow>=10.0'
python story_video/kaggle_render.py --preflight
python story_video/kaggle_render.py
