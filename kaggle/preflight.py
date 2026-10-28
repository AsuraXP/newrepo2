#!/usr/bin/env python3
"""Kaggle-only entry point for the existing single-request calibration test."""
import subprocess
import sys
from pathlib import Path


def main():
    if not Path('/kaggle/working').is_dir():
        raise SystemExit('Run this TTS preflight on Kaggle, not in the workspace.')
    repo = Path(__file__).resolve().parents[1]
    return subprocess.call([
        sys.executable, str(repo / 'kaggle/run.py'), '--repo', str(repo),
        '--dry-run', '--tts-debug', '--preflight',
    ])


if __name__ == '__main__':
    raise SystemExit(main())
