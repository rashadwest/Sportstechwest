#!/usr/bin/env python3
"""
Generate MP3 from plain text using ElevenLabs TTS.
Loads .env from repo root: ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, ELEVENLABS_VOICE_ID_STW_NEWS.

Usage:
  python scripts/voice-generate.py --in shorts-packages/.../script-elevenlabs.txt \\
    --out output/audio/stw-news-strava-runna.mp3 --preset stw-news
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Install requests: pip install requests", file=sys.stderr)
    sys.exit(1)


def _load_dotenv() -> None:
    root = Path(__file__).resolve().parents[1]
    env = root / ".env"
    if not env.exists():
        return
    raw = env.read_text(encoding="utf-8").lstrip("\ufeff")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip().lstrip("\ufeff")
        v = v.strip().strip('"').strip("'").strip("\r")
        if " #" in v:
            v = v.split(" #")[0].strip()
        if k.startswith("ELEVENLABS_") and v:
            os.environ[k] = v


def _strip_broll(text: str) -> str:
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("[B-ROLL") or s.startswith("**[B-ROLL"):
            continue
        if s.startswith("— Sportstechwest"):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _read_input(path: Path) -> str:
    body = path.read_text(encoding="utf-8")
    return _strip_broll(body)


def _resolve_voice_id(preset: str | None, out_path: str, voice_id_arg: str | None) -> str:
    if voice_id_arg:
        return voice_id_arg
    out_lower = out_path.lower()
    use_stw = preset == "stw-news" or "stw-news" in out_lower
    if use_stw:
        vid = os.environ.get("ELEVENLABS_VOICE_ID_STW_NEWS", "").strip()
        if not vid:
            print(
                "STW News voice: set ELEVENLABS_VOICE_ID_STW_NEWS in .env (British lady ID).",
                file=sys.stderr,
            )
            sys.exit(1)
        return vid
    vid = os.environ.get("ELEVENLABS_VOICE_ID", "").strip()
    if not vid:
        print("Set ELEVENLABS_VOICE_ID in .env or pass --voice-id.", file=sys.stderr)
        sys.exit(1)
    return vid


def _tts(api_key: str, voice_id: str, text: str, out_path: Path) -> None:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
        },
    }
    r = requests.post(
        url,
        headers={"xi-api-key": api_key, "Accept": "audio/mpeg", "Content-Type": "application/json"},
        json=payload,
        timeout=120,
    )
    if r.status_code != 200:
        print(f"ElevenLabs error {r.status_code}: {r.text[:500]}", file=sys.stderr)
        sys.exit(1)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(r.content)
    print(f"Wrote {out_path} ({len(r.content)} bytes)")


def main() -> None:
    _load_dotenv()
    p = argparse.ArgumentParser(description="ElevenLabs TTS to MP3")
    p.add_argument("--in", dest="in_path", required=True, help="Input text file")
    p.add_argument("--out", dest="out_path", required=True, help="Output .mp3 path")
    p.add_argument("--preset", choices=["stw-news"], default=None)
    p.add_argument("--voice-id", default=None)
    p.add_argument("--dry-run", action="store_true", help="Print text only, no API call")
    p.add_argument("--show-voice-id", action="store_true", help="Show resolved voice id and exit")
    args = p.parse_args()

    in_path = Path(args.in_path)
    out_path = Path(args.out_path)
    if not in_path.is_file():
        print(f"Missing input: {in_path}", file=sys.stderr)
        sys.exit(1)

    text = _read_input(in_path)
    if not text:
        print("No text after stripping B-roll lines.", file=sys.stderr)
        sys.exit(1)

    voice_id = _resolve_voice_id(args.preset, str(out_path), args.voice_id)

    if args.show_voice_id:
        masked = voice_id[:4] + "…" + voice_id[-4:] if len(voice_id) > 8 else "(short)"
        print(f"Voice ID: {masked} (preset={args.preset})")
        sys.exit(0)

    if args.dry_run:
        print(text)
        sys.exit(0)

    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("Set ELEVENLABS_API_KEY in .env", file=sys.stderr)
        sys.exit(1)

    _tts(api_key, voice_id, text, out_path)


if __name__ == "__main__":
    main()
