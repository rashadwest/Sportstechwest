#!/usr/bin/env python3
"""
RaSun Video — turn Sportstechwest blog posts into narrated YouTube videos
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
    "Sportstechwest — sports, technology, and the systems behind performance.\n"
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


def build_one(slug: str, force: bool, dry_run: bool) -> int:
    d = PKG_ROOT / slug
    script = d / "script.txt"
    if not script.exists():
        print(f"{slug}: missing {rel(script)}", file=sys.stderr)
        return 1
    if not load_pkg(slug).get("approved"):
        print(f"{slug}: not approved (set \"approved\": true in package.json)", file=sys.stderr)
        return 1
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

def cmd_status(_: argparse.Namespace) -> int:
    dates = {s: d for d, s in read_queue()}
    slugs = all_slugs()
    if not slugs:
        print("No RaSun episodes yet. Start one with: rasun-video.py new --post _posts/<post>.md")
        return 0
    today = date.today()
    for s in sorted(slugs, key=lambda x: (dates.get(x) or date.max, x)):
        pkg = load_pkg(s)
        d = dates.get(s)
        when = d.isoformat() if d else "unscheduled"
        if d and d < today:
            when += " (past)"
        flags = []
        flags.append("approved" if pkg.get("approved") else "NEEDS REVIEW")
        flags.append("audio" if audio_path(s).exists() else "no audio")
        flags.append("video" if video_path(s).exists() else "no video")
        if pkg.get("youtube_video_id"):
            flags.append(f"youtu.be/{pkg['youtube_video_id']}")
        wc = word_count((PKG_ROOT / s / "script.txt").read_text(encoding="utf-8")) if (PKG_ROOT / s / "script.txt").exists() else 0
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

    p = sub.add_parser("status", help="List episodes")
    p.set_defaults(fn=cmd_status)

    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
