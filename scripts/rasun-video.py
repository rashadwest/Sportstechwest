#!/usr/bin/env python3
"""
RaSun Video: turn Sportstechwest blog posts into narrated YouTube videos
using the RaSun voice in ElevenLabs, published every other day.

One "episode" = one folder in video-packages/rasun/<slug>/:
  script.txt     What RaSun reads (edit this before it ships)
  youtube.txt    Line 1 title, then description, then "TAGS:" + comma list
  package.json   Source post, post URL, visual, status
  visual.*       Optional override (png/jpg/mp4/mov); otherwise the post's hero image

Commands:
  new      Create an episode from a blog post (drafts script + YouTube copy)
  schedule Give unscheduled episodes publish dates, every other day
  build    Generate RaSun audio (ElevenLabs) and render the MP4 (ffmpeg)
  status   Show every episode, its date, and what's still missing

The upload itself is done by scripts/stw-iq-dispatcher.py (job "rasun-every-other-day"
in stw-publish-schedule.json), which reads _data/rasun_queue.csv and builds the
video on the spot if it isn't rendered yet.

Typical flow:
  python3 scripts/rasun-video.py new --post _posts/2026-11-09-Practicing-Is-Not-Pressure-Beasley-vs-Stephenson.md
  # read/edit video-packages/rasun/<slug>/script.txt, set "approved": true in package.json
  python3 scripts/rasun-video.py schedule
  python3 scripts/rasun-video.py build --upcoming 2     # optional; dispatcher builds if missing
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO = Path(__file__).resolve().parents[1]
PKG_ROOT = REPO / "video-packages" / "rasun"
QUEUE_CSV = REPO / "_data" / "rasun_queue.csv"
AUDIO_DIR = REPO / "output" / "audio"
VIDEO_DIR = REPO / "output" / "video"
SITE_URL = "https://sportstechwest.com"
FALLBACK_VISUAL = REPO / "assets" / "images" / "blog-img" / "teaching-greatest-teacher-hero.png"
DEFAULT_GAP_DAYS = 2  # every other day

TARGET_WORDS = (380, 520)  # ~2.5–3.5 minutes at a natural pace

CHANNEL_FOOTER = (
    "Read the full breakdown: {url}\n\n"
    "Sportstechwest: sports, technology, and the systems behind performance.\n"
    "Subscribe for a new RaSun breakdown every other day."
)


# ---------------------------------------------------------------- helpers

def load_dotenv() -> None:
    env = REPO / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").lstrip("﻿").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if " #" in v:
            v = v.split(" #")[0].strip()
        if v and k not in os.environ:
            os.environ[k] = v


def parse_front_matter(text: str) -> Tuple[Dict[str, str], str]:
    """Minimal Jekyll front matter parser (flat key: value, plus [a, b] lists)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end]
    body = text[end + 4:]
    fm: Dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def fm_list(value: str) -> List[str]:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [v.strip().strip('"').strip("'") for v in value.split(",") if v.strip()]


def markdown_to_plain(body: str) -> str:
    """Strip HTML, Liquid, images, link URLs and markdown syntax; keep headings as lines."""
    t = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", "", body, flags=re.S)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"^\s{0,3}>\s?", "", t, flags=re.M)
    t = re.sub(r"[*_`]{1,3}", "", t)
    t = re.sub(r"^\s*[-*+]\s+", "", t, flags=re.M)
    t = re.sub(r"^\s*\|.*\|\s*$", "", t, flags=re.M)  # tables
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def slug_from_post(post: Path, fm: Dict[str, str]) -> str:
    permalink = fm.get("permalink", "").strip("/")
    if permalink:
        s = permalink.split("/")[-1]
    else:
        s = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60].strip("-")


def post_url(fm: Dict[str, str], post: Path) -> str:
    permalink = fm.get("permalink", "")
    if permalink:
        return SITE_URL + "/" + permalink.lstrip("/")
    return SITE_URL + "/blog/"


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'’-]+\b", text))


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


# ---------------------------------------------------------------- script drafting

RASUN_SYSTEM = """You write voiceover scripts for RaSun, the narrator of the Sportstechwest YouTube channel.
Sportstechwest is Rashad West's lane: basketball, player development, sports science, analytics, and the
systems behind performance, explained by a practitioner who translates research into what coaches,
players and parents can use.

Write a script RaSun will read out loud with an ElevenLabs voice. Rules:
- {lo}-{hi} words. Plain spoken English, short sentences, no lists, no headings, no stage directions,
  no emoji, no markdown, no URLs read aloud.
- Open with a one or two sentence hook that makes a viewer stay. No "Hey guys", no "In this video".
- Carry the post's argument and its best concrete details (names, numbers, dates) faithfully.
  Never add facts, stats or quotes that are not in the post.
- Write numbers the way they should be spoken when it helps the voice ("one twenty-six", "twenty twenty-six").
- Use a paragraph break where RaSun should pause.
- End with one takeaway line, then: "The full breakdown is on Sportstechwest dot com. I'm RaSun. See you in two days."
Return only the script text."""


def draft_with_claude(title: str, plain: str) -> Optional[str]:
    """Use the Claude API if the SDK and a credential are available; otherwise return None."""
    try:
        import anthropic  # type: ignore
    except ImportError:
        return None
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        return None
    client = anthropic.Anthropic()
    lo, hi = TARGET_WORDS
    try:
        resp = client.beta.messages.create(
            model="claude-opus-5-5",
            max_tokens=16000,
            output_config={"effort": "medium"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            system=RASUN_SYSTEM.format(lo=lo, hi=hi),
            messages=[{
                "role": "user",
                "content": f"Blog post title: {title}\n\nBlog post:\n\n{plain}",
            }],
        )
    except anthropic.APIStatusError as e:
        print(f"Claude API error {e.status_code}; falling back to the outline draft.", file=sys.stderr)
        return None
    except anthropic.APIConnectionError:
        print("Could not reach the Claude API; falling back to the outline draft.", file=sys.stderr)
        return None
    if resp.stop_reason == "refusal":
        print("Claude declined this post; falling back to the outline draft.", file=sys.stderr)
        return None
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    return text or None


def draft_outline(title: str, description: str, plain: str) -> str:
    """No-API fallback: hook from the description, first lines of each section, standard close."""
    sections: List[Tuple[str, List[str]]] = []
    current: Tuple[str, List[str]] = ("", [])
    for para in [p.strip() for p in plain.split("\n\n") if p.strip()]:
        if para.startswith("#"):
            if current[1]:
                sections.append(current)
            current = (para.lstrip("# ").strip(), [])
        else:
            current[1].append(" ".join(para.split()))
    if current[1]:
        sections.append(current)

    lo, hi = TARGET_WORDS
    out: List[str] = [description or title]
    budget = hi - word_count(out[0]) - 40
    skip = re.compile(r"^(sources?|references?|further reading|related)", re.I)
    for heading, paras in sections:
        if skip.match(heading):
            continue
        for p in paras[:2]:
            if budget <= 0:
                break
            if word_count(p) > budget:
                continue
            out.append(p)
            budget -= word_count(p)
    out.append(
        "The full breakdown is on Sportstechwest dot com. I'm RaSun. See you in two days."
    )
    return "\n\n".join(out)


# ---------------------------------------------------------------- packages

def load_pkg(slug: str) -> Dict:
    p = PKG_ROOT / slug / "package.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_pkg(slug: str, data: Dict) -> None:
    p = PKG_ROOT / slug / "package.json"
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def all_slugs() -> List[str]:
    if not PKG_ROOT.exists():
        return []
    return sorted(d.name for d in PKG_ROOT.iterdir() if (d / "package.json").exists())


def choose_visual(slug: str) -> Optional[Path]:
    d = PKG_ROOT / slug
    for name in ("visual.mp4", "visual.mov", "visual.png", "visual.jpg", "visual.jpeg", "visual.webp"):
        if (d / name).exists():
            return d / name
    v = load_pkg(slug).get("visual") or ""
    if v:
        p = REPO / v.lstrip("/")
        if p.exists():
            return p
    return FALLBACK_VISUAL if FALLBACK_VISUAL.exists() else None


def cmd_new(args: argparse.Namespace) -> int:
    post = Path(args.post)
    if not post.is_absolute():
        post = REPO / post
    if not post.exists():
        print(f"Post not found: {post}", file=sys.stderr)
        return 1
    fm, body = parse_front_matter(post.read_text(encoding="utf-8"))
    title = fm.get("title", post.stem)
    description = fm.get("description", "")
    slug = args.slug or slug_from_post(post, fm)
    d = PKG_ROOT / slug
    if d.exists() and not args.force:
        print(f"Episode already exists: {rel(d)} (use --force to redraft)", file=sys.stderr)
        return 1
    d.mkdir(parents=True, exist_ok=True)

    plain = markdown_to_plain(body)
    url = post_url(fm, post)

    script = None if args.no_ai else draft_with_claude(title, plain)
    drafted_by = "claude" if script else "outline"
    if not script:
        script = draft_outline(title, description, plain)
    (d / "script.txt").write_text(script.strip() + "\n", encoding="utf-8")

    yt_title = title if len(title) <= 85 else title[:82].rstrip() + "…"
    yt_title = f"{yt_title} | RaSun"
    if len(yt_title) > 100:
        yt_title = yt_title[:100]
    tags = [t for t in fm_list(fm.get("tags", "")) if t] + ["RaSun", "Sportstechwest"]
    seen, uniq = set(), []
    for t in tags:
        key = t.lower()
        if key not in seen:
            seen.add(key)
            uniq.append(t.replace("-", " "))
    desc = (description + "\n\n" if description else "") + CHANNEL_FOOTER.format(url=url)
    (d / "youtube.txt").write_text(
        f"{yt_title}\n\n{desc}\n\nTAGS:\n{', '.join(uniq)}\n", encoding="utf-8"
    )

    save_pkg(slug, {
        "slug": slug,
        "title": title,
        "source_post": rel(post),
        "post_url": url,
        "visual": fm.get("thumbnail", "").lstrip("/"),
        "drafted_by": drafted_by,
        "approved": False,
        "publish_date": "",
        "youtube_video_id": "",
    })

    wc = word_count(script)
    print(f"Created {rel(d)}/  (script drafted by {drafted_by}, {wc} words ≈ {wc / 150:.1f} min)")
    print(f"  1. Read and edit {rel(d / 'script.txt')}")
    print(f"  2. Check {rel(d / 'youtube.txt')}")
    print(f"  3. Set \"approved\": true in {rel(d / 'package.json')}, then run: rasun-video.py schedule")
    return 0


# ---------------------------------------------------------------- queue

def read_queue() -> List[Tuple[date, str]]:
    rows: List[Tuple[date, str]] = []
    if not QUEUE_CSV.exists():
        return rows
    with QUEUE_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                rows.append((date.fromisoformat((r.get("date") or "").strip()), (r.get("story") or "").strip()))
            except ValueError:
                continue
    return sorted(rows)


def write_queue(rows: List[Tuple[date, str]]) -> None:
    QUEUE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with QUEUE_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "story"])
        for d, s in sorted(rows):
            w.writerow([d.isoformat(), s])


def cmd_schedule(args: argparse.Namespace) -> int:
    rows = read_queue()
    queued = {s for _, s in rows}
    pending = [s for s in all_slugs() if s not in queued and (args.include_unapproved or load_pkg(s).get("approved"))]
    if not pending:
        unapproved = [s for s in all_slugs() if s not in queued and not load_pkg(s).get("approved")]
        print("Nothing to schedule." + (f" Not approved yet: {', '.join(unapproved)}" if unapproved else ""))
        return 0

    today = date.today()
    if args.start:
        nxt = date.fromisoformat(args.start)
    else:
        future = [d for d, _ in rows if d >= today]
        nxt = (max(future) + timedelta(days=args.gap)) if future else today + timedelta(days=1)

    # Episodes with a "planned_date" in package.json go on that date; the rest fill
    # every-other-day slots after the last queued date.
    planned = sorted((s for s in pending if load_pkg(s).get("planned_date")), key=lambda s: load_pkg(s)["planned_date"])
    for slug in planned:
        when = date.fromisoformat(load_pkg(slug)["planned_date"])
        if when < today:
            print(f"SKIP {slug}: planned date {when} has passed; set a new planned_date")
            continue
        clash = [s for d, s in rows if d == when]
        if clash:
            print(f"SKIP {slug}: {when} already has {clash[0]}")
            continue
        rows.append((when, slug))
        pkg = load_pkg(slug)
        pkg["publish_date"] = when.isoformat()
        save_pkg(slug, pkg)
        print(f"{when.isoformat()}  {slug}  (planned)")
    pending = [s for s in pending if s not in planned]

    for slug in pending:
        while any(d == nxt for d, _ in rows):
            nxt += timedelta(days=1)
        rows.append((nxt, slug))
        pkg = load_pkg(slug)
        pkg["publish_date"] = nxt.isoformat()
        save_pkg(slug, pkg)
        print(f"{nxt.isoformat()}  {slug}")
        nxt += timedelta(days=args.gap)

    if not args.dry_run:
        write_queue(rows)
        print(f"Updated {rel(QUEUE_CSV)}")
    return 0


# ---------------------------------------------------------------- build

def audio_path(slug: str) -> Path:
    return AUDIO_DIR / f"rasun-{slug}.mp3"


def video_path(slug: str) -> Path:
    return VIDEO_DIR / f"rasun-{slug}.mp4"


def render_video(visual: Path, audio: Path, out: Path) -> int:
    out.parent.mkdir(parents=True, exist_ok=True)
    encode = [
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",  # YouTube loudness target
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out),
    ]
    if visual.suffix.lower() in (".mp4", ".mov"):
        vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1"
        cmd = ["ffmpeg", "-y", "-stream_loop", "-1", "-i", str(visual), "-i", str(audio), "-vf", vf,
               "-map", "0:v:0", "-map", "1:a:0", "-shortest", "-r", "30"] + encode
    else:
        # Still image: blurred full-bleed background + sharp centered image + slow push-in.
        fc = (
            "[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=30:2,setsar=1[bg];"
            "[0:v]scale=1720:960:force_original_aspect_ratio=decrease,setsar=1[fg];"
            "[bg][fg]overlay=(W-w)/2:(H-h)/2,scale=2880:1620,"
            "zoompan=z='1+0.06*min(in/5400\\,1)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30[v]"
        )
        cmd = ["ffmpeg", "-y", "-loop", "1", "-framerate", "30", "-i", str(visual), "-i", str(audio),
               "-filter_complex", fc, "-map", "[v]", "-map", "1:a:0", "-shortest"] + encode
    print("RUN:", " ".join(cmd))
    return subprocess.run(cmd).returncode


# ---------------------------------------------------------------- IQ sessions (bikeIQ, walkingIQ style)
#
# package.json "format": "iq-session" switches build to this path. Same structure as the
# walking/mentalIQ sessions: one spoken segment per paragraph, 5 seconds of quiet after each,
# music bed at 35%, looped visual, fixed total length. A "[ride N]" line after a segment
# replaces the 5-second gap with ~N seconds of music-only time; ride blocks are scaled so the
# session lands exactly on the target length.

DEFAULT_MUSIC = "output/music/background-manifestation-60min/track-a.mp3"
SEGMENT_GAP = 5.0


def parse_session(text: str) -> List[Tuple[str, Optional[float]]]:
    """Return [(segment_text, ride_seconds or None)]. None means the standard 5-second gap."""
    segments: List[Tuple[str, Optional[float]]] = []
    for block in re.split(r"\n\s*\n", text):
        lines = [l.strip() for l in block.splitlines() if l.strip() and not l.strip().startswith("#")]
        ride: Optional[float] = None
        spoken: List[str] = []
        for l in lines:
            m = re.fullmatch(r"\[(?:ride|walk|hike|run|quiet)\s+(\d+(?:\.\d+)?)\]", l, re.I)
            if m:
                ride = float(m.group(1))
            else:
                spoken.append(l)
        if spoken:
            segments.append((" ".join(spoken), ride))
        elif ride is not None and segments:
            t, _ = segments[-1]
            segments[-1] = (t, ride)
    return segments


def spoken_text(text: str) -> str:
    return "\n\n".join(t for t, _ in parse_session(text))


def media_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def build_session(slug: str, force: bool, dry_run: bool) -> int:
    import hashlib

    d = PKG_ROOT / slug
    pkg = load_pkg(slug)
    target = float(pkg.get("duration_seconds") or 3600)
    segments = parse_session((d / "script.txt").read_text(encoding="utf-8"))
    if not segments:
        print(f"{slug}: script has no segments", file=sys.stderr)
        return 1

    seg_dir = AUDIO_DIR / f"rasun-{slug}-segments"
    seg_dir.mkdir(parents=True, exist_ok=True)
    mp4 = video_path(slug)

    # 1) Voice each segment (cached by text, so editing one line re-voices only that line).
    seg_files: List[Path] = []
    for i, (text, _) in enumerate(segments):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
        out = seg_dir / f"{i:03d}-{h}.mp3"
        seg_files.append(out)
        if out.exists() and not force:
            continue
        txt = seg_dir / f"{i:03d}-{h}.txt"
        txt.write_text(text + "\n", encoding="utf-8")
        cmd = [sys.executable, str(REPO / "scripts" / "voice-generate.py"),
               "--in", str(txt), "--out", str(out), "--preset", "rasun"]
        if dry_run:
            print("RUN:", " ".join(cmd[1:3]), f"... segment {i + 1}/{len(segments)}")
            continue
        rc = subprocess.run(cmd).returncode
        if rc != 0:
            return rc
    if dry_run:
        print(f"would assemble {len(segments)} segments into {target / 60:.0f} minutes → {rel(mp4)}")
        return 0

    if mp4.exists() and not force and all(mp4.stat().st_mtime > f.stat().st_mtime for f in seg_files):
        print(f"{slug}: ready → {rel(mp4)}")
        return 0
    if shutil.which("ffmpeg") is None:
        print("ffmpeg not installed", file=sys.stderr)
        return 1

    # 2) Fit ride blocks to the target length.
    durs = [media_duration(f) for f in seg_files]
    speech = sum(durs)
    fixed_gaps = sum(SEGMENT_GAP for _, r in segments if r is None)
    ride_base = sum(r for _, r in segments if r is not None)
    room = target - speech - fixed_gaps
    scale = max(0.3, room / ride_base) if ride_base else 1.0
    print(f"speech {speech / 60:.1f} min, gaps {fixed_gaps:.0f}s, ride blocks {ride_base:.0f}s × {scale:.2f}")

    # 3) Voice timeline: segment, gap, segment, gap ... as one WAV padded/trimmed to target.
    work = seg_dir / "assemble"
    work.mkdir(exist_ok=True)
    concat_list = work / "list.txt"
    lines: List[str] = []
    silence_cache: Dict[int, Path] = {}
    for f, (_, ride) in zip(seg_files, segments):
        wav = work / (f.stem + ".wav")
        if not wav.exists() or wav.stat().st_mtime < f.stat().st_mtime:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(f), "-ar", "44100", "-ac", "2", str(wav)], check=True)
        gap_ms = int(round((SEGMENT_GAP if ride is None else ride * scale) * 1000))
        if gap_ms not in silence_cache:
            sil = work / f"silence-{gap_ms}.wav"
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                            "anullsrc=r=44100:cl=stereo", "-t", f"{gap_ms / 1000:.3f}", str(sil)], check=True)
            silence_cache[gap_ms] = sil
        lines.append(f"file '{wav}'")
        lines.append(f"file '{silence_cache[gap_ms]}'")
    concat_list.write_text("\n".join(lines) + "\n", encoding="utf-8")
    voice = work / "voice.wav"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
                    "-af", f"apad=whole_dur={target}", "-t", str(target), str(voice)], check=True)

    # 4) Music bed at 35% (looped), voice on top. Music is optional.
    music = REPO / (pkg.get("music") or DEFAULT_MUSIC)
    mix = work / "mix.m4a"
    if music.exists():
        vol = float(pkg.get("music_volume") or 0.35)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(voice), "-stream_loop", "-1", "-i", str(music),
                        "-filter_complex",
                        f"[1:a]volume={vol},afade=t=in:d=3,afade=t=out:st={target - 8}:d=8[m];"
                        f"[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0,"
                        f"loudnorm=I=-16:TP=-1.5:LRA=11[a]",
                        "-map", "[a]", "-t", str(target), "-c:a", "aac", "-b:a", "192k", str(mix)], check=True)
    else:
        print(f"WARNING: music not found at {rel(music)}; rendering voice only.", file=sys.stderr)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(voice), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                        "-t", str(target), "-c:a", "aac", "-b:a", "192k", str(mix)], check=True)

    # 5) Video: looped clip or still card, cheap to encode for an hour.
    visual = choose_visual(slug)
    if visual is None:
        print(f"{slug}: no visual found", file=sys.stderr)
        return 1
    tmp = mp4.with_name(mp4.stem + ".partial.mp4")
    mp4.parent.mkdir(parents=True, exist_ok=True)
    scale_vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1"
    if visual.suffix.lower() in (".mp4", ".mov"):
        vin = ["-stream_loop", "-1", "-i", str(visual)]
        venc = ["-vf", scale_vf + ",fps=30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23"]
    else:
        vin = ["-loop", "1", "-framerate", "6", "-i", str(visual)]
        venc = ["-vf", scale_vf, "-r", "6", "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-crf", "22"]
    cmd = ["ffmpeg", "-loglevel", "error", "-stats", "-y"] + vin + ["-i", str(mix), "-map", "0:v:0", "-map", "1:a:0",
           "-t", str(target)] + venc + ["-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", str(tmp)]
    print("RUN:", " ".join(cmd))
    rc = subprocess.run(cmd).returncode
    if rc != 0:
        tmp.unlink(missing_ok=True)
        return rc
    tmp.replace(mp4)
    print(f"{slug}: ready → {rel(mp4)} ({media_duration(mp4) / 60:.1f} min)")
    return 0


def build_one(slug: str, force: bool, dry_run: bool) -> int:
    d = PKG_ROOT / slug
    script = d / "script.txt"
    if not script.exists():
        print(f"{slug}: missing {rel(script)}", file=sys.stderr)
        return 1
    if not load_pkg(slug).get("approved"):
        print(f"{slug}: not approved (set \"approved\": true in package.json)", file=sys.stderr)
        return 1
    if load_pkg(slug).get("format") == "iq-session":
        return build_session(slug, force=force, dry_run=dry_run)
    mp3, mp4 = audio_path(slug), video_path(slug)

    # Re-voice when the script changed after the last render.
    stale = mp3.exists() and script.stat().st_mtime > mp3.stat().st_mtime
    if force or stale or not mp3.exists():
        cmd = [sys.executable, str(REPO / "scripts" / "voice-generate.py"),
               "--in", str(script), "--out", str(mp3), "--preset", "rasun"]
        print("RUN:", " ".join(cmd))
        if not dry_run:
            rc = subprocess.run(cmd).returncode
            if rc != 0:
                return rc
        stale = True

    if force or stale or not mp4.exists():
        visual = choose_visual(slug)
        if visual is None:
            print(f"{slug}: no visual found", file=sys.stderr)
            return 1
        if dry_run:
            print(f"would render {rel(mp4)} from {rel(visual)} + {rel(mp3)}")
            return 0
        if shutil.which("ffmpeg") is None:
            print("ffmpeg not installed", file=sys.stderr)
            return 1
        # Render to a temp name and rename at the end, so a half-written file is never uploaded.
        tmp = mp4.with_name(mp4.stem + ".partial.mp4")
        rc = render_video(visual, mp3, tmp)
        if rc != 0:
            tmp.unlink(missing_ok=True)
            return rc
        tmp.replace(mp4)
    print(f"{slug}: ready → {rel(mp4)}")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    load_dotenv()
    if args.slug:
        slugs = [args.slug]
    else:
        today = date.today()
        end = today + timedelta(days=args.upcoming)
        slugs = [s for d, s in read_queue() if today <= d <= end]
        if not slugs:
            print(f"No RaSun episodes queued between {today} and {end}.")
            return 0
    rc_all = 0
    for s in slugs:
        rc = build_one(s, force=args.force, dry_run=args.dry_run)
        rc_all = rc_all or rc
    return rc_all


# ---------------------------------------------------------------- status

def cmd_approve(args: argparse.Namespace) -> int:
    """Mark episodes approved and put them on the calendar (planned_date, else next open slot)."""
    for slug in args.slugs:
        if not (PKG_ROOT / slug / "package.json").exists():
            print(f"No episode named {slug}", file=sys.stderr)
            return 1
        pkg = load_pkg(slug)
        pkg["approved"] = True
        save_pkg(slug, pkg)
        print(f"approved {slug}")
    return cmd_schedule(argparse.Namespace(start=None, gap=DEFAULT_GAP_DAYS, include_unapproved=False, dry_run=False))


def cmd_status(_: argparse.Namespace) -> int:
    dates = {s: d for d, s in read_queue()}
    slugs = all_slugs()
    if not slugs:
        print("No RaSun episodes yet. Start one with: rasun-video.py new --post _posts/<post>.md")
        return 0
    today = date.today()
    def sort_key(x: str):
        planned = load_pkg(x).get("planned_date")
        return (dates.get(x) or (date.fromisoformat(planned) if planned else date.max), x)

    for s in sorted(slugs, key=sort_key):
        pkg = load_pkg(s)
        d = dates.get(s)
        when = d.isoformat() if d else (f"planned {pkg['planned_date']}" if pkg.get("planned_date") else "unscheduled")
        if d and d < today:
            when += " (past)"
        flags = []
        flags.append("approved" if pkg.get("approved") else "NEEDS REVIEW")
        flags.append("audio" if audio_path(s).exists() else "no audio")
        flags.append("video" if video_path(s).exists() else "no video")
        if pkg.get("youtube_video_id"):
            flags.append(f"youtu.be/{pkg['youtube_video_id']}")
        sp = PKG_ROOT / s / "script.txt"
        wc = word_count(spoken_text(sp.read_text(encoding="utf-8"))) if sp.exists() else 0
        if pkg.get("format") == "iq-session" and any((AUDIO_DIR / f"rasun-{s}-segments").glob("*.mp3")):
            flags[1] = "audio"
        print(f"{when:<20} {s:<50} {wc:>4}w  {' · '.join(flags)}")
    return 0


# ---------------------------------------------------------------- main

def main() -> None:
    load_dotenv()
    ap = argparse.ArgumentParser(description="RaSun Video: blog post → RaSun-narrated YouTube video, every other day")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("new", help="Create an episode from a blog post")
    p.add_argument("--post", required=True, help="Path to a _posts/*.md file")
    p.add_argument("--slug", help="Override the episode slug")
    p.add_argument("--no-ai", action="store_true", help="Skip Claude; build an outline draft from the post")
    p.add_argument("--force", action="store_true", help="Overwrite an existing episode's drafts")
    p.set_defaults(fn=cmd_new)

    p = sub.add_parser("schedule", help="Assign every-other-day dates to approved, unscheduled episodes")
    p.add_argument("--start", help="First date to use (YYYY-MM-DD); default: 2 days after the last queued date, or tomorrow")
    p.add_argument("--gap", type=int, default=DEFAULT_GAP_DAYS, help="Days between videos (default 2)")
    p.add_argument("--include-unapproved", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(fn=cmd_schedule)

    p = sub.add_parser("build", help="Voice + render episodes")
    p.add_argument("--slug", help="Build one episode")
    p.add_argument("--upcoming", type=int, default=2, help="Build episodes queued from today through today+N (default 2)")
    p.add_argument("--force", action="store_true", help="Re-voice and re-render even if files exist")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(fn=cmd_build)

    p = sub.add_parser("approve", help="Approve episodes and schedule them")
    p.add_argument("slugs", nargs="+")
    p.set_defaults(fn=cmd_approve)

    p = sub.add_parser("status", help="List episodes")
    p.set_defaults(fn=cmd_status)

    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
