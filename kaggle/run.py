#!/usr/bin/env python3
"""
narration-first video renderer
==============================

One continuous narration track is the master timeline. Frames react to words.

    PASS 1  edge-tts(whole script, one request) -> WordBoundary stream
            -> match every frame anchor (anchor_phrase + occurrence)
            -> exact start/end per frame -> validate holds -> timings.csv
    PASS 2  ffmpeg places each frame at its measured offset, transitions
            complete on the anchor word, narration muxed on top -> final.mp4

Modes
    --estimate   no internet, no TTS. Runs the authoring estimator
                 (~0.33 s/word + punctuation pauses) over the script and
                 writes estimated timings for pacing QC.
    --dry-run    real TTS + real timings, stop before rendering.

Usage (Kaggle)
    python run.py --repo . --out final.mp4
Usage (authoring QC, anywhere)
    python run.py --repo . --estimate
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

TICKS = 10_000_000  # edge-tts WordBoundary offset/duration unit = 100 ns

TTS_START = "<!-- TTS:START -->"
TTS_END = "<!-- TTS:END -->"

SOURCES_HEADING = re.compile(
    r"^#{1,6}\s*(sources|source list|references|further reading|sources\s*&\s*further reading)\b",
    re.IGNORECASE,
)

# ffmpeg xfade transition names we accept (anything else falls back to fade)
XFADE_TRANSITIONS = {
    "fade", "fadeblack", "fadewhite", "fadegrays", "dissolve", "distance",
    "wipeleft", "wiperight", "wipeup", "wipedown", "wipetl", "wipetr",
    "wipebl", "wipebr", "slideleft", "slideright", "slideup", "slidedown",
    "smoothleft", "smoothright", "smoothup", "smoothdown",
    "circleopen", "circleclose", "circlecrop", "rectcrop",
    "vertopen", "vertclose", "horzopen", "horzclose",
    "diagtl", "diagtr", "diagbl", "diagbr",
    "hlslice", "hrslice", "vuslice", "vdslice", "hblur",
    "pixelize", "radial", "zoomin", "squeezeh", "squeezev",
}


# ---------------------------------------------------------------------------
# config / inputs
# ---------------------------------------------------------------------------

def load_config(path: Path) -> dict:
    try:
        import yaml
    except ImportError:  # pragma: no cover
        sys.exit("PyYAML is required: pip install -q pyyaml")
    with open(path, "r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}
    for key in ("tts", "video", "timing", "paths", "estimate", "transitions"):
        cfg.setdefault(key, {})
    cfg["video"].setdefault("width", 1280)
    cfg["video"].setdefault("height", 720)
    cfg["video"].setdefault("fps", 30)
    cfg["video"].setdefault("crf", 20)
    cfg["video"].setdefault("preset", "medium")
    cfg["video"].setdefault("pix_fmt", "yuv420p")
    cfg["video"].setdefault("audio_bitrate", "192k")
    cfg["video"].setdefault("ken_burns", True)
    cfg["video"].setdefault("ken_burns_zoom", 1.10)
    cfg["video"].setdefault("ken_burns_rate", 0.0006)
    cfg["transitions"].setdefault("default", "fade:0.5")
    cfg["transitions"].setdefault("cut_frames", 2)
    cfg["timing"].setdefault("min_hold_s", 1.2)
    cfg["timing"].setdefault("max_hold_s", 12.0)
    cfg["timing"].setdefault("under_min_policy", "merge")
    cfg["timing"].setdefault("over_max_policy", "warn")
    cfg["timing"].setdefault("lead_in_max_s", 0.6)
    cfg["timing"].setdefault("tail_end_s", 0.8)
    cfg["estimate"].setdefault("sec_per_word", 0.33)
    cfg["estimate"].setdefault("pauses", {})
    cfg["render"] = cfg.get("render") or {}
    cfg["render"].setdefault("fade_in_s", 0.4)
    cfg["render"].setdefault("fade_out_s", 0.5)
    return cfg


def read_narration(path: Path) -> str:
    """Extract the speakable text. Markers win; heading heuristic as fallback."""
    raw = path.read_text(encoding="utf-8")

    if TTS_START in raw:
        body = raw.split(TTS_START, 1)[1]
        if TTS_END in body:
            body = body.split(TTS_END, 1)[0]
    else:
        lines = raw.splitlines()
        # drop YAML front matter
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    lines = lines[i + 1:]
                    break
        kept: list[str] = []
        for line in lines:
            if SOURCES_HEADING.match(line.strip()):
                break
            if line.lstrip().startswith(("#", ">", "|", "<!--")):
                continue
            kept.append(line)
        body = "\n".join(kept)

    # strip light markdown emphasis / links / backticks so TTS never reads syntax
    body = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", body)
    body = body.replace("**", "").replace("__", "").replace("`", "")
    body = re.sub(r"(?<!\w)\*(?!\s)([^*\n]+)(?<!\s)\*(?!\w)", r"\1", body)

    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", body)]
    text = "\n\n".join(p for p in paragraphs if p)
    if not text.strip():
        sys.exit(f"no speakable text found in {path}")
    if re.search(r"[#*_`\[\]]", text):
        print("  ! narration still contains markdown-ish characters - check TTS text")
    return text


def load_frames(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as fh:
        frames = json.load(fh)
    if isinstance(frames, dict):
        frames = frames.get("frames", [])
    if not frames:
        sys.exit(f"{path} has no frames")

    seen = set()
    for i, fr in enumerate(frames):
        # `transition` is optional: omit it and the config default applies. That
        # keeps one global look instead of 40 hand-written durations drifting.
        for key in ("id", "anchor_phrase", "image_prompt", "negative_prompt"):
            if key not in fr:
                sys.exit(f"frames[{i}] missing required key '{key}'")
        if fr["id"] in seen:
            sys.exit(f"duplicate frame id '{fr['id']}'")
        seen.add(fr["id"])
        fr.setdefault("occurrence", 1)
        if not isinstance(fr["occurrence"], int) or fr["occurrence"] == 0:
            sys.exit(f"frame '{fr['id']}' occurrence must be a non-zero integer")
    return frames


# ---------------------------------------------------------------------------
# tokenising + anchor matching
# ---------------------------------------------------------------------------

def norm_tokens(text: str) -> list[str]:
    """Lowercase, punctuation-free tokens. Hyphens/slashes split words."""
    text = text.lower().replace("\u2019", "'")
    out: list[str] = []
    for part in re.split(r"[\s\-/\u2013\u2014]+", text):
        part = re.sub(r"[^a-z0-9']", "", part).strip("'")
        if part:
            out.append(part)
    return out


def stream_tokens(words: list[dict]) -> tuple[list[str], list[int]]:
    """Expand word boundaries into matchable tokens, keeping the parent word index."""
    toks: list[str] = []
    owner: list[int] = []
    for wi, word in enumerate(words):
        for tok in norm_tokens(word["text"]):
            toks.append(tok)
            owner.append(wi)
    return toks, owner


def _tok_match(a: str, b: str) -> bool:
    if a == b:
        return True
    if len(a) >= 3 and len(b) >= 3 and (a.startswith(b) or b.startswith(a)):
        return True
    return False


def find_anchor(anchor_tokens: list[str], toks: list[str], occurrence: int,
                words: list[dict], owner: list[int]) -> tuple[int, str, int]:
    """Locate the `occurrence`-th match of an anchor phrase in the word stream."""
    n = len(anchor_tokens)
    if n == 0:
        raise ValueError("empty anchor")
    span = len(toks) - n + 1
    exact = [i for i in range(span) if toks[i:i + n] == anchor_tokens]
    matches = exact
    quality = "exact"
    if not exact:
        loose = [i for i in range(span)
                 if all(_tok_match(a, b) for a, b in zip(anchor_tokens, toks[i:i + n]))]
        matches = loose
        quality = "loose"

    if not matches:
        preview = " ".join(toks[:14]) + (" ..." if span > 14 else "")
        raise LookupError(
            f"anchor phrase not found: \"{' '.join(anchor_tokens)}\"\n"
            f"    narration starts with: {preview}\n"
            f"    anchors must be copied verbatim from the narration script")

    idx_list = matches
    if occurrence > 0:
        if occurrence > len(idx_list):
            raise LookupError(
                f"anchor \"{' '.join(anchor_tokens)}\" occurs {len(idx_list)} time(s), "
                f"frame asked for occurrence {occurrence}")
        pick = idx_list[occurrence - 1]
    else:
        if abs(occurrence) > len(idx_list):
            raise LookupError(
                f"anchor \"{' '.join(anchor_tokens)}\" occurs {len(idx_list)} time(s), "
                f"frame asked for occurrence {occurrence}")
        pick = idx_list[occurrence]

    return pick, quality, len(idx_list)


# ---------------------------------------------------------------------------
# estimator (authoring QC only - never used for the final timeline)
# ---------------------------------------------------------------------------

def pause_for(word: str, pauses: dict) -> float:
    clean = word.strip("\"'\u201d\u2019)]}*")
    if not clean:
        return 0.0
    return float(pauses.get(clean[-1], 0.0))


def estimate_words(text: str, est_cfg: dict) -> list[dict]:
    """Approximate a word-boundary stream from raw text. Workspace QC only."""
    spw = float(est_cfg["sec_per_word"])
    pauses = est_cfg.get("pauses") or {}
    words: list[dict] = []
    t = 0.0
    for raw in text.split():
        words.append({"text": raw, "start": t, "end": t + spw})
        t += spw + pause_for(raw, pauses)
    return words


def estimate_seconds(text: str, est_cfg: dict) -> float:
    words = estimate_words(text, est_cfg)
    return words[-1]["end"] if words else 0.0


# ---------------------------------------------------------------------------
# TTS - one request, one continuous track
# ---------------------------------------------------------------------------

def _chunk_kind(raw: object) -> str:
    """edge-tts has renamed chunk types across versions - match generously."""
    if not isinstance(raw, dict):
        return ""
    return str(raw.get("type", "")).strip().lower()


async def _synth_async(text: str, tts_cfg: dict, mp3_path: Path,
                       debug: bool = False) -> tuple[list[dict], dict]:
    """One request, one continuous track. Returns (word boundaries, diagnostics)."""
    try:
        import edge_tts
    except ImportError:
        sys.exit("edge-tts is required for PASS 1: pip install -q edge-tts")

    version = getattr(edge_tts, "__version__", "unknown")
    stats = {"version": version, "kinds": {}, "audio_bytes": 0,
             "error": None, "attempts": 0}

    communicate = edge_tts.Communicate(
        text,
        voice=tts_cfg["voice"],
        rate=tts_cfg.get("rate", "+0%"),
        volume=tts_cfg.get("volume", "+0%"),
        pitch=tts_cfg.get("pitch", "+0Hz"),
    )

    chunks: list[dict] = []
    try:
        with open(mp3_path, "wb") as fh:
            async for chunk in communicate.stream():
                kind = _chunk_kind(chunk)
                stats["kinds"][kind or "?"] = stats["kinds"].get(kind or "?", 0) + 1
                if debug:
                    print(f"        chunk: {kind} {list(chunk.keys())[:5]}")
                if kind == "audio":
                    data = chunk.get("data") or b""
                    fh.write(data)
                    stats["audio_bytes"] += len(data)
                elif "boundary" in kind:
                    offset = float(chunk.get("offset", 0)) / TICKS
                    duration = float(chunk.get("duration", 0)) / TICKS
                    label = str(chunk.get("text", "")).strip()
                    if label:
                        chunks.append({"text": label, "start": offset,
                                       "duration": duration, "kind": kind})
    except Exception as exc:  # noqa: BLE001 - surface the real reason, never mask it
        stats["error"] = f"{type(exc).__name__}: {exc}"
        if debug:
            import traceback
            traceback.print_exc()

    stats["chunks"] = len(chunks)
    return chunks, stats


def _word_cost(token: str, pauses: dict) -> float:
    """Rough share of a sentence a single word should occupy."""
    letters = len(re.sub(r"[^A-Za-z0-9']", "", token))
    speak = max(letters, 1) / 5.0
    return speak + pause_for(token, pauses) / 0.33


def expand_boundaries(chunks: list[dict], audio_dur: float,
                      est_cfg: dict) -> tuple[list[dict], str, float]:
    """Turn boundary chunks into per-word timings.

    edge-tts is not consistent about granularity: some builds emit one event per
    WORD, newer ones emit one per SENTENCE (or per phrase). Both are useful, but
    they must not be treated the same way - a sentence event used as if it were a
    word collapses every anchor inside that sentence onto a single instant.

    For multi-word chunks only the chunk's own start/end are measured; the words
    inside are distributed by length and punctuation. Sentence-level events are
    therefore "sentence-anchored": real spans, inferred interior.
    """
    pauses = est_cfg.get("pauses") or {}
    words: list[dict] = []
    multi = 0

    for i, ch in enumerate(chunks):
        tokens = ch["text"].split()
        if not tokens:
            continue
        # chunk end: its own duration if trustworthy, else the next chunk's start
        end = ch["start"] + ch["duration"]
        if ch["duration"] <= 0:
            end = chunks[i + 1]["start"] if i + 1 < len(chunks) else audio_dur
        span = max(end - ch["start"], 0.001)
        if len(tokens) > 1:
            multi += 1

        costs = [_word_cost(t, pauses) for t in tokens]
        total = sum(costs) or 1.0
        t = ch["start"]
        for k, (token, cost) in enumerate(zip(tokens, costs)):
            share = span * cost / total
            words.append({"text": token, "start": round(t, 4),
                          "end": round(t + share, 4),
                          # the first word of a chunk sits on a measured timestamp;
                          # anything after it is interpolated inside a real span
                          "event_start": k == 0})
            t += share

    words.sort(key=lambda w: w["start"])
    granularity = "measured" if multi == 0 else (
        "sentence-anchored" if multi > len(chunks) * 0.5 else "mixed")
    avg_tokens = (sum(len(c["text"].split()) for c in chunks) / len(chunks)) if chunks else 0
    return words, granularity, round(avg_tokens, 2)


def _proportional_words(text: str, audio_dur: float, est_cfg: dict) -> list[dict]:
    """Last-resort timing when the boundary stream is unavailable.

    The narration audio is real and correctly measured; only the per-word
    timestamps are inferred, by weighting the estimator with word length and
    scaling the whole thing to the measured audio duration.
    """
    raw = text.split()
    if not raw or audio_dur <= 0:
        return []
    pauses = est_cfg.get("pauses") or {}
    spw = float(est_cfg["sec_per_word"])
    weights = []
    for w in raw:
        weight = max(len(re.sub(r"[^A-Za-z0-9']", "", w)), 1) / 5.0
        weights.append(weight * spw + pause_for(w, pauses))
    total = sum(weights) or 1.0
    scale = audio_dur / total
    words: list[dict] = []
    t = 0.0
    for w, weight in zip(raw, weights):
        span = weight * scale
        words.append({"text": w, "start": t, "end": t + span})
        t += span
    return words


def synth(text: str, tts_cfg: dict, mp3_path: Path, est_cfg: dict,
          debug: bool = False) -> tuple[list[dict], str]:
    """Run PASS 1, retrying a bare connection failure. Returns (words, sync_source)."""
    attempts = max(int(tts_cfg.get("retries", 3)), 1)
    last: dict = {}
    for attempt in range(1, attempts + 1):
        chunks, stats = asyncio.run(
            _synth_async(text, tts_cfg, mp3_path, debug=debug))
        stats["attempts"] = attempt
        last = stats
        if chunks and stats["audio_bytes"]:
            audio_dur = probe_duration(mp3_path) or chunks[-1]["start"]
            words, granularity, avg_tokens = expand_boundaries(
                chunks, audio_dur, est_cfg)
            print(f"        edge-tts {stats['version']} | "
                  f"audio {stats['audio_bytes'] / 1024:.0f} KiB | "
                  f"{len(chunks)} boundary events ({avg_tokens} words each) "
                  f"-> {len(words)} word timings | attempt {attempt}")
            if granularity != "measured":
                print(f"        this build reports {granularity.upper()} events, not "
                      f"per-word ones.")
                print("        sentence spans are measured; word positions inside a "
                      "sentence are inferred")
                print("        from word length and punctuation. Anchor starts are "
                      "accurate to the sentence.")
            script_words = len(text.split())
            if len(words) < script_words * 0.75:
                print(f"        ! only {len(words)} words recovered from "
                      f"{script_words} in the script - check the audio is complete")
            return words, granularity
        kinds = ", ".join(f"{k}={v}" for k, v in stats["kinds"].items()) or "none"
        reason = stats["error"] or f"stream ended (chunk types seen: {kinds})"
        print(f"        attempt {attempt}/{attempts} incomplete: {reason}")
        if stats["audio_bytes"]:
            print(f"        audio WAS received ({stats['audio_bytes'] / 1024:.0f} KiB) "
                  f"but no word boundaries came with it")
            break
        if attempt < attempts:
            print("        retrying in 3s ...")
            time.sleep(3)

    audio_dur = probe_duration(mp3_path)
    if last.get("audio_bytes") and audio_dur:
        if not tts_cfg.get("allow_estimated_fallback", True):
            sys.exit(
                "edge-tts returned audio but no word boundaries.\n"
                "  Fix: pip install -q --upgrade --force-reinstall edge-tts\n"
                "  Then re-run. Set tts.allow_estimated_fallback: false to keep\n"
                "  this a hard failure.")
        print("\n  ! FALLBACK: audio is real and measured, but the boundary stream\n"
              "    is unavailable on this edge-tts build. Frame timings will be\n"
              "    inferred proportionally across the measured audio length.\n"
              "    The video will be watchable but NOT word-accurate.\n"
              "    Nothing in the repo changes - fix edge-tts and re-run to get\n"
              "    exact sync.")
        words = _proportional_words(text, audio_dur, est_cfg)
        return words, "estimated"

    hint = ""
    if last.get("error") and ("403" in str(last["error"]) or "401" in str(last["error"])):
        hint = ("\n  This is an Azure auth rejection. Upgrade edge-tts:\n"
                "    pip install -q --upgrade --force-reinstall edge-tts")
    sys.exit(
        "PASS 1 failed: no audio and no word boundaries.\n"
        f"  edge-tts version: {last.get('version', 'unknown')}\n"
        f"  last error: {last.get('error') or 'stream produced nothing'}{hint}\n"
        "  Check: is Internet enabled in the Kaggle sidebar?")


def probe_duration(path: Path) -> float | None:
    """Duration in seconds via ffprobe, else by parsing `ffmpeg -i`."""
    if shutil.which("ffprobe"):
        try:
            out = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=nw=1:nk=1", str(path)],
                capture_output=True, text=True, check=True).stdout.strip()
            return float(out)
        except Exception:
            pass
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        return None
    try:
        proc = subprocess.run([ffmpeg, "-i", str(path)], capture_output=True, text=True)
        match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", proc.stderr)
        if match:
            h, m, s = match.groups()
            return int(h) * 3600 + int(m) * 60 + float(s)
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# timeline: anchors -> exact starts/ends -> hold validation
# ---------------------------------------------------------------------------

def assign_timings(frames: list[dict], words: list[dict], audio_dur: float,
                   cfg: dict) -> list[dict]:
    """Match every anchor into the word stream and derive frame start/end."""
    toks, owner = stream_tokens(words)
    est_cfg = cfg["estimate"]
    spw = float(est_cfg["sec_per_word"])
    pauses = est_cfg.get("pauses") or {}

    segments: list[dict] = []
    last_word_idx = -1
    for fi, fr in enumerate(frames):
        anchor_tokens = norm_tokens(fr["anchor_phrase"])
        try:
            tok_idx, quality, n_matches = find_anchor(
                anchor_tokens, toks, int(fr["occurrence"]), words, owner)
        except LookupError as exc:
            sys.exit(f"frame #{fi + 1} ({fr['id']}): {exc}")

        word_idx = owner[tok_idx]
        anchor_end_word = owner[tok_idx + len(anchor_tokens) - 1]
        if word_idx <= last_word_idx:
            sys.exit(
                f"frame #{fi + 1} ({fr['id']}) anchor lands on word {word_idx}, "
                f"which is not after the previous frame (word {last_word_idx}).\n"
                f"    frames.json must be in narration order.")
        last_word_idx = word_idx

        precision = ("exact" if words[word_idx].get("event_start")
                     else "in-sentence")

        segments.append({
            "frame_index": fi + 1,
            "id": fr["id"],
            "anchor_precision": precision,
            "anchor_phrase": fr["anchor_phrase"],
            "occurrence": int(fr["occurrence"]),
            "matched_text": " ".join(w["text"] for w in
                                     words[word_idx:anchor_end_word + 1]),
            "match_quality": quality,
            "n_anchor_matches": n_matches,
            "anchor_word_index": word_idx,
            "anchor_word_start_s": words[word_idx]["start"],
            "anchor_word_end_s": words[anchor_end_word]["end"],
            "image": fr.get("image") or f"{fr['id']}.jpg",
            "transition": fr.get("transition") or cfg["transitions"]["default"],
            "status": "ok",
            "effective": True,
            "est_words": 0,
        })

    # a frame starts on its anchor word; frame 1 owns the lead-in from 0.0s
    for i, seg in enumerate(segments):
        seg["start_s"] = 0.0 if i == 0 else round(seg["anchor_word_start_s"], 4)
    # ends = next anchor start; the last frame runs to the end of the audio
    for i, seg in enumerate(segments):
        seg["end_s"] = round(segments[i + 1]["start_s"], 4) if i + 1 < len(segments) \
            else round(audio_dur, 4)

    if segments[0]["anchor_word_start_s"] > float(cfg["timing"]["lead_in_max_s"]):
        segments[0]["status"] = "warn_lead_in"

    # estimated hold per frame, from the words that actually live in that slice
    for seg in segments:
        seg_words = [w for w in words
                     if seg["start_s"] - 1e-6 <= w["start"] < seg["end_s"] - 1e-6]
        seg["est_words"] = len(seg_words)
        seg["est_hold_s"] = round(len(seg_words) * spw
                                  + sum(pause_for(w["text"], pauses) for w in seg_words), 4)

    return segments


def validate_holds(segments: list[dict], cfg: dict) -> list[dict]:
    """Under-min frames merge into a neighbour; over-max ones are flagged."""
    timing = cfg["timing"]
    min_hold = float(timing["min_hold_s"])
    max_hold = float(timing["max_hold_s"])
    under_policy = str(timing["under_min_policy"]).lower()

    def holds(seg):
        return round(seg["end_s"] - seg["start_s"], 4)

    changed = True
    while changed:
        changed = False
        active = [s for s in segments if s["effective"]]
        for seg in active:
            if holds(seg) >= min_hold - 1e-9:
                continue
            if under_policy != "merge" or len(active) == 1:
                seg["status"] = "warn_under_min"
                continue

            pos = active.index(seg)
            if pos == 0:
                # first frame too short: it just becomes lead-in for the next frame
                nxt = active[1]
                seg["effective"] = False
                seg["status"] = f"merged_into:{nxt['id']}"
                nxt["start_s"] = 0.0
                changed = True
                break
            prev = active[pos - 1]
            seg["effective"] = False
            seg["status"] = f"merged_into:{prev['id']}"
            prev["end_s"] = seg["end_s"]
            changed = True
            break

    for seg in segments:
        if not seg["effective"]:
            continue
        if holds(seg) > max_hold + 1e-9:
            seg["status"] = ("warn_over_max" if seg["status"] == "ok"
                             else seg["status"] + "+warn_over_max")
    return segments


def refresh_estimates(segments: list[dict], words: list[dict], cfg: dict) -> None:
    """Recompute per-frame estimator holds after merging changed the spans."""
    pauses = cfg["estimate"].get("pauses") or {}
    spw = float(cfg["estimate"]["sec_per_word"])
    for seg in segments:
        seg_words = [w for w in words
                     if seg["start_s"] - 1e-6 <= w["start"] < seg["end_s"] - 1e-6]
        seg["est_words"] = len(seg_words)
        seg["est_hold_s"] = round(len(seg_words) * spw
                                  + sum(pause_for(w["text"], pauses) for w in seg_words), 4)


# ---------------------------------------------------------------------------
# ffmpeg
# ---------------------------------------------------------------------------

def parse_transition(spec: str | None, cfg: dict) -> tuple[str, float, str]:
    fps = float(cfg["video"]["fps"])
    default = cfg["transitions"]["default"]
    cut_frames = float(cfg["transitions"]["cut_frames"])
    spec = (spec or default)
    spec = str(spec).strip().lower()

    if spec in ("cut", "hardcut", "none", ""):
        return "fade", max(cut_frames / fps, 1.0 / fps), "cut"

    if ":" in spec:
        name, _, dur = spec.partition(":")
        try:
            seconds = float(dur)
        except ValueError:
            name, seconds = spec, 0.5
    else:
        name, seconds = spec, 0.5

    name = name.strip() or "fade"
    if name not in XFADE_TRANSITIONS:
        print(f"  ! unknown transition '{name}' - using 'fade'")
        name = "fade"
    return name, max(min(seconds, 2.0), 1.0 / fps), spec


def plan_render(segments: list[dict], cfg: dict) -> dict:
    """Clip durations, xfade offsets and total length - the timing math."""
    active = [s for s in segments if s["effective"]]
    fps = float(cfg["video"]["fps"])
    tail = float(cfg["timing"]["tail_end_s"])

    trans = [parse_transition(s["transition"], cfg) for s in active]
    n = len(active)
    pad = 1.0 / fps  # one spare frame so an xfade always has material to blend

    # A frame's `transition` is how it ENTERS. Its clip must therefore carry
    # (hold + own transition) seconds: xfade maps B's own timestamps onto the
    # output timeline, so B's length sets the cumulative cursor:
    #     cursor(i) = offset(i) + len(clip_i) = start_(i+1)
    durs: list[float] = []
    for i, seg in enumerate(active):
        hold = seg["end_s"] - seg["start_s"]
        enter = trans[i][1] if i > 0 else 0.0
        extra = tail if i == n - 1 else 0.0
        durs.append(round(hold + enter + extra + pad, 4))

    offsets: list[float] = []
    for i in range(1, n):
        offset = active[i]["start_s"] - trans[i][1]
        if offset < 0:
            raise SystemExit(
                f"frame '{active[i]['id']}' is only {active[i]['start_s']:.3f}s in, "
                f"shorter than its {trans[i][1]:.2f}s transition")
        offsets.append(round(offset, 4))

    total = round(active[-1]["end_s"] + tail, 4)
    return {"segments": active, "durations": durs, "offsets": offsets,
            "transitions": trans, "total_s": total, "fps": fps}


def build_filtergraph(plan: dict, cfg: dict, with_audio: bool) -> tuple[str, str, str]:
    video = cfg["video"]
    W, H, fps = int(video["width"]), int(video["height"]), float(video["fps"])
    pix_fmt = video["pix_fmt"]
    segs = plan["segments"]
    durs, offsets, trans = plan["durations"], plan["offsets"], plan["transitions"]
    n = len(segs)

    kb = bool(video["ken_burns"])
    zmax = float(video["ken_burns_zoom"])
    rate = float(video["ken_burns_rate"])

    parts: list[str] = []
    for i, seg in enumerate(segs):
        frames_in_clip = max(int(durs[i] * fps), 2)
        chain = []
        if kb:
            z_end = 1.0 + rate * frames_in_clip
            zmax_local = max(zmax, z_end)
            if i % 2 == 0:  # push in
                zexpr = f"min(1+{rate:.6f}*on,{zmax_local:.4f})"
            else:           # pull out
                zexpr = f"max({zmax_local:.4f}-{rate:.6f}*on,1)"
            chain += [
                f"scale={int(W * 1.2)}:{int(H * 1.2)}:force_original_aspect_ratio=increase",
                f"crop={int(W * 1.2)}:{int(H * 1.2)}",
                "setsar=1",
                f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                f":d=1:s={W}x{H}:fps={fps:g}",
            ]
        else:
            chain += [
                f"scale={W}:{H}:force_original_aspect_ratio=increase",
                f"crop={W}:{H}",
                "setsar=1",
            ]
        chain += [f"fps={fps:g}", "settb=AVTB", f"format={pix_fmt}"]
        parts.append(f"[{i}:v]" + ",".join(chain) + f"[v{i}]")

    cur = "v0"
    for i in range(1, n):
        name, dur, _spec = trans[i]
        out = f"x{i}"
        parts.append(
            f"[{cur}][v{i}]xfade=transition={name}:duration={dur:.3f}"
            f":offset={offsets[i - 1]:.3f}[{out}]")
        cur = out

    total = plan["total_s"]
    fade_in = float(cfg["render"]["fade_in_s"])
    fade_out = min(float(cfg["render"]["fade_out_s"]), max(total / 4, 0.1))
    post = []
    if fade_in > 0:
        post.append(f"fade=t=in:st=0:d={fade_in:.3f}")
    if fade_out > 0 and total > fade_out + 0.2:
        post.append(f"fade=t=out:st={total - fade_out:.3f}:d={fade_out:.3f}")
    post.append(f"format={pix_fmt}")
    parts.append(f"[{cur}]" + ",".join(post) + "[vout]")

    if with_audio:
        parts.append(f"[{n}:a]apad,atrim=0:{total:.3f},asetpts=N/SR/TB[aout]")
    return ";".join(parts), "vout", "aout"


def build_ffmpeg_cmd(plan: dict, images: list[Path], cfg: dict,
                     out_path: Path, audio: Path | None) -> list[str]:
    video = cfg["video"]
    fps = plan["fps"]
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats"]
    for img, dur in zip(images, plan["durations"]):
        cmd += ["-loop", "1", "-framerate", f"{fps:g}", "-t", f"{dur:.3f}", "-i", str(img)]
    n = len(images)
    if audio:
        cmd += ["-i", str(audio)]

    graph, vlabel, alabel = build_filtergraph(plan, cfg, with_audio=bool(audio))
    cmd += ["-filter_complex", graph, "-map", f"[{vlabel}]"]
    if audio:
        cmd += ["-map", f"[{alabel}]", "-c:a", "aac", "-b:a", video["audio_bitrate"]]
    cmd += [
        "-t", f"{plan['total_s']:.3f}",
        "-c:v", "libx264",
        "-preset", str(video["preset"]),
        "-crf", str(video["crf"]),
        "-pix_fmt", video["pix_fmt"],
        "-r", f"{fps:g}",
        "-movflags", "+faststart",
        str(out_path),
    ]
    return cmd


def resolve_images(segments: list[dict], cfg: dict, repo: Path) -> list[Path]:
    """Every rendered frame must exist - never ship a video with a hole in it."""
    frames_dir = repo / cfg["paths"]["frames_dir"]
    images: list[Path] = []
    missing: list[str] = []
    for seg in segments:
        if not seg["effective"]:
            continue
        img = Path(seg["image"])
        img = img if img.is_absolute() else frames_dir / img
        if not img.is_file():
            missing.append(str(img))
        images.append(img)
    if missing:
        sys.exit("missing frame images:\n  " + "\n  ".join(missing)
                 + "\n  generate + verify every frame before rendering")
    return images


def find_ffmpeg() -> str | None:
    """PATH first, then an explicit FFMPEG_BIN override."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    override = os.environ.get("FFMPEG_BIN")
    if override and Path(override).is_file():
        return override
    return None


def render(plan: dict, images: list[Path], cfg: dict, out_path: Path,
           audio: Path | None, work: Path) -> Path:
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        sys.exit("ffmpeg not found on PATH (or set FFMPEG_BIN)")
    cmd = build_ffmpeg_cmd(plan, images, cfg, out_path, audio)
    cmd[0] = ffmpeg
    (work / "ffmpeg_cmd.txt").write_text(" \\\n  ".join(cmd) + "\n", encoding="utf-8")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  rendering {len(images)} frames -> {out_path}  ({plan['total_s']:.1f}s)")
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        sys.exit(f"ffmpeg failed ({proc.returncode}) - see {work / 'ffmpeg_cmd.txt'}")
    return out_path


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------

CSV_FIELDS = [
    "frame_index", "frame_id", "status", "sync_source", "anchor_phrase", "occurrence",
    "matched_text", "match_quality", "anchor_precision",
    "anchor_word_start_s", "anchor_word_end_s",
    "start_s", "end_s", "hold_s", "est_hold_s", "hold_delta_s", "est_words",
    "image", "transition", "transition_dur_s",
]


def write_csv(segments: list[dict], path: Path, cfg: dict,
              sync_source: str = "estimated") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for seg in segments:
            name, dur, _ = parse_transition(seg["transition"], cfg)
            writer.writerow({
                "frame_index": seg["frame_index"],
                "frame_id": seg["id"],
                "status": seg["status"],
                "sync_source": sync_source,
                "anchor_phrase": seg["anchor_phrase"],
                "occurrence": seg["occurrence"],
                "matched_text": seg["matched_text"],
                "match_quality": seg["match_quality"],
                "anchor_precision": seg.get("anchor_precision", "estimated"),
                "anchor_word_start_s": f"{seg['anchor_word_start_s']:.3f}",
                "anchor_word_end_s": f"{seg['anchor_word_end_s']:.3f}",
                "start_s": f"{seg['start_s']:.3f}",
                "end_s": f"{seg['end_s']:.3f}",
                "hold_s": f"{seg['end_s'] - seg['start_s']:.3f}",
                "est_hold_s": f"{seg['est_hold_s']:.3f}",
                "hold_delta_s": f"{(seg['end_s'] - seg['start_s']) - seg['est_hold_s']:+.3f}",
                "est_words": seg["est_words"],
                "image": seg["image"],
                "transition": name,
                "transition_dur_s": f"{dur:.3f}",
            })


def print_table(segments: list[dict], limit: int = 60) -> None:
    print(f"  {'#':>3} {'frame_id':<26} {'start':>7} {'end':>7} {'hold':>6} "
          f"{'est':>6} {'d':>6}  status")
    for seg in segments[:limit]:
        hold = seg["end_s"] - seg["start_s"]
        print(f"  {seg['frame_index']:>3} {seg['id'][:26]:<26} {seg['start_s']:>7.2f} "
              f"{seg['end_s']:>7.2f} {hold:>6.2f} {seg['est_hold_s']:>6.2f} "
              f"{hold - seg['est_hold_s']:>+6.2f}  {seg['status']}")
    if len(segments) > limit:
        print(f"  ... {len(segments) - limit} more rows")


def report(segments: list[dict], cfg: dict, audio_dur: float | None,
           estimate_total: float) -> dict:
    active = [s for s in segments if s["effective"]]
    dropped = [s for s in segments if not s["effective"]]
    warnings: list[str] = []

    for seg in segments:
        if seg["match_quality"] == "loose":
            warnings.append(
                f"anchor \"{seg['anchor_phrase']}\" matched loosely - "
                f"copy the phrase verbatim from the script")
        if seg["status"].startswith("warn_lead_in"):
            warnings.append(
                f"frame 1 anchor starts at {seg['anchor_word_start_s']:.2f}s "
                f"(> lead_in_max_s) - it holds from 0.0s")
        if "warn_under_min" in seg["status"]:
            warnings.append(
                f"frame '{seg['id']}' holds {seg['end_s'] - seg['start_s']:.2f}s "
                f"(< min_hold_s) and was NOT merged")
        if "warn_over_max" in seg["status"]:
            warnings.append(
                f"frame '{seg['id']}' holds {seg['end_s'] - seg['start_s']:.2f}s "
                f"(> max_hold_s) - add an anchor to split it")
    for seg in dropped:
        warnings.append(f"frame '{seg['id']}' merged ({seg['status']}) - "
                        f"too short on its own")

    calib = {}
    if audio_dur:
        calib = {
            "measured_audio_s": round(audio_dur, 3),
            "estimated_s": round(estimate_total, 3),
            "estimate_ratio": round(audio_dur / estimate_total, 4) if estimate_total else None,
            "current_sec_per_word": cfg["estimate"]["sec_per_word"],
            "suggested_sec_per_word": None,
        }
    print()
    print(f"  frames authored : {len(segments)}")
    print(f"  frames rendered : {len(active)}"
          + (f"  (merged: {', '.join(s['id'] for s in dropped)})" if dropped else ""))
    if audio_dur:
        print(f"  narration length: {audio_dur:.2f}s")
    print(f"  estimated length: {estimate_total:.2f}s")
    exact = sum(1 for s in active if s.get("anchor_precision") == "exact")
    if active and exact < len(active):
        est = len(active) - exact
        print(f"  anchor precision : {exact}/{len(active)} exact, "
              f"{est} inferred inside a measured sentence")

    if warnings:
        print(f"\n  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"    ! {w}")
    else:
        print("\n  no timing warnings")
    return {"calibration": calib, "warnings": warnings}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="narration-first renderer (edge-tts word boundaries -> ffmpeg)")
    ap.add_argument("--repo", default=".", help="repo root (default: .)")
    ap.add_argument("--config", default=None, help="default: <repo>/kaggle/config.yaml")
    ap.add_argument("--out", default="final.mp4", help="output video (default final.mp4)")
    ap.add_argument("--workdir", default=None,
                    help="scratch + timings dir (default /kaggle/working if present)")
    ap.add_argument("--dry-run", action="store_true",
                    help="PASS 1 only: real TTS + timings.csv, no render")
    ap.add_argument("--estimate", action="store_true",
                    help="no TTS: authoring estimator only (works offline)")
    ap.add_argument("--draft", action="store_true",
                    help="render a SILENT draft from estimated timings "
                         "(no TTS, no network - pacing preview only)")
    ap.add_argument("--tts-debug", action="store_true",
                    help="print every edge-tts chunk type (diagnose missing word boundaries)")
    ap.add_argument("--narration", default=None, help="override narration path")
    ap.add_argument("--frames", default=None, help="override frames.json path")
    args = ap.parse_args(argv)

    repo = Path(args.repo).resolve()
    cfg_path = Path(args.config) if args.config else repo / "kaggle" / "config.yaml"
    cfg = load_config(cfg_path)

    if args.workdir:
        work = Path(args.workdir).resolve()
    elif Path("/kaggle/working").is_dir():
        work = Path("/kaggle/working")
    else:
        work = repo / cfg["paths"]["out_dir"]
    work.mkdir(parents=True, exist_ok=True)

    narration_path = Path(args.narration) if args.narration else \
        repo / cfg["paths"]["narration"]
    frames_path = Path(args.frames) if args.frames else repo / cfg["paths"]["frames"]

    print(f"repo    : {repo}")
    print(f"config  : {cfg_path}")
    print(f"workdir : {work}")

    text = read_narration(narration_path)
    frames = load_frames(frames_path)
    est_total = estimate_seconds(text, cfg["estimate"])
    print(f"script  : {len(text.split())} words, ~{est_total:.1f}s estimated"
          f" | {len(frames)} frames\n")

    # ---------------- estimate mode (workspace QC, no internet) -------------
    if args.estimate:
        words = estimate_words(text, cfg["estimate"])
        audio_dur = words[-1]["end"] if words else 0.0
        segments = assign_timings(frames, words, audio_dur, cfg)
        segments = validate_holds(segments, cfg)
        refresh_estimates(segments, words, cfg)
        print_table(segments)
        write_csv(segments, work / "estimates.csv", cfg)
        write_csv(segments, repo / cfg["paths"]["out_dir"] / "estimates.csv", cfg)
        report(segments, cfg, None, est_total)
        print(f"\n  wrote {work / 'estimates.csv'}")
        if not args.draft:
            print("  estimator is QC only - final sync always comes from Kaggle word boundaries")
            return 0
        # silent pacing draft: same render path, estimated timings, no audio
        print("\n  DRAFT  rendering silent pacing preview from estimated timings")
        images = resolve_images(segments, cfg, repo)
        plan = plan_render(segments, cfg)
        stem = Path(args.out).stem
        if not stem.endswith("_draft"):
            stem += "_draft"
        out_path = Path(args.out) if Path(args.out).is_absolute() else work / (stem + ".mp4")
        render(plan, images, cfg, out_path, audio=None, work=work)
        print(f"\n  draft: {out_path}  ({plan['total_s']:.1f}s, no audio)")
        print("  timing is estimated - the real sync always comes from Kaggle")
        return 0

    # ---------------- PASS 1: one continuous narration ----------------------
    mp3 = work / "narration.mp3"
    print("PASS 1  synthesising narration (single request, whole script)")
    words, sync_source = synth(text, cfg["tts"], mp3, cfg["estimate"],
                               debug=bool(args.tts_debug))
    audio_dur = probe_duration(mp3) or words[-1]["end"]
    label = {"measured": "measured word boundaries",
             "sentence-anchored": "word timings from measured sentence spans",
             "mixed": "word timings from mixed-granularity events"}.get(
                 sync_source, "inferred word timings")
    print(f"        {len(words)} {label}, {audio_dur:.2f}s audio -> {mp3}")
    print(f"        sync_source={sync_source}")

    segments = assign_timings(frames, words, audio_dur, cfg)
    segments = validate_holds(segments, cfg)
    refresh_estimates(segments, words, cfg)

    print("\n  measured timeline")
    print_table(segments)

    write_csv(segments, work / "timings.csv", cfg, sync_source)
    write_csv(segments, repo / cfg["paths"]["out_dir"] / "timings.csv", cfg, sync_source)
    info = report(segments, cfg, audio_dur, est_total)

    if audio_dur and est_total:
        suggested = None
        # refine the estimator constant: measured time minus punctuation pauses
        pause_total = 0.0
        n_words = 0
        for raw in text.split():
            n_words += 1
            pause_total += pause_for(raw, cfg["estimate"].get("pauses") or {})
        if n_words:
            suggested = round(max(audio_dur - pause_total, 0.0) / n_words, 4)
        info["calibration"]["suggested_sec_per_word"] = suggested
        info["calibration"]["word_count"] = n_words
        info["calibration"]["punctuation_pause_s"] = round(pause_total, 3)
        print(f"  calibration: est {est_total:.1f}s vs measured {audio_dur:.1f}s "
              f"-> suggested sec_per_word {suggested}")

    (work / "calibration.json").write_text(
        json.dumps(info, indent=2), encoding="utf-8")
    print(f"  wrote {work / 'timings.csv'}")

    if args.dry_run:
        print("\n  --dry-run: stopping before render.")
        print("  review timings.csv, fix anchors if a frame is misplaced or short,")
        print("  then re-run without --dry-run.")
        return 0

    # ---------------- PASS 2: stitch ---------------------------------------
    images = resolve_images(segments, cfg, repo)
    plan = plan_render(segments, cfg)
    out_path = Path(args.out)
    if not out_path.is_absolute() and out_path.parent == Path("."):
        out_path = work / out_path.name

    print(f"\nPASS 2  rendering {len(images)} frames, {plan['total_s']:.2f}s total")
    manifest = {
        "total_s": plan["total_s"],
        "fps": plan["fps"],
        "voice": cfg["tts"]["voice"],
        "rate": cfg["tts"]["rate"],
        "narration_s": round(audio_dur, 3),
        "frames": [
            {"id": s["id"], "start_s": s["start_s"], "end_s": s["end_s"],
             "image": s["image"], "transition": s["transition"]}
            for s in plan["segments"]
        ],
    }
    (work / "render_manifest.json").write_text(json.dumps(manifest, indent=2),
                                               encoding="utf-8")
    render(plan, images, cfg, out_path, audio=mp3, work=work)

    size_mb = out_path.stat().st_size / 1e6
    print(f"\n  done: {out_path}  ({size_mb:.1f} MB, {plan['total_s']:.1f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
