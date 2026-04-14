#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def queue_story_for_date(queue_path: Path, day: date) -> str:
    if not queue_path.exists():
        return ""
    with queue_path.open("r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("date") or "").strip() == day.isoformat():
                return (row.get("story") or "").strip()
    return ""


def upcoming_stories_from_queue(queue_path: Path, start: date, end: date) -> List[str]:
    """Stories in queue CSV whose publish date falls in [start, end], calendar order, deduped."""
    rows: List[tuple[date, str]] = []
    if not queue_path.exists():
        return []
    with queue_path.open("r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ds = (row.get("date") or "").strip()
            if not ds:
                continue
            try:
                d = date.fromisoformat(ds)
            except ValueError:
                continue
            if start <= d <= end:
                s = (row.get("story") or "").strip()
                if s:
                    rows.append((d, s))
    rows.sort(key=lambda x: x[0])
    out: List[str] = []
    seen: set[str] = set()
    for _, s in rows:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def run_cmd(cmd: List[str], log_lines: List[str], dry_run: bool) -> int:
    log_lines.append(f"RUN: {' '.join(cmd)}")
    if dry_run:
        return 0
    proc = subprocess.run(cmd)
    return int(proc.returncode)


def choose_visual(story_dir: Path, fallback_visual: Path | None) -> Path | None:
    candidates = [
        story_dir / "visual.mp4",
        story_dir / "visual.mov",
        story_dir / "visual.png",
        story_dir / "visual.jpg",
        story_dir / "stw-news-opener.png",
    ]
    for p in candidates:
        if p.exists():
            return p
    if fallback_visual and fallback_visual.exists():
        return fallback_visual
    return None


def resolve_fallback_visual(repo: Path, configured_path: str) -> Path | None:
    configured = repo / configured_path if configured_path else None
    candidates: List[Path] = []
    if configured:
        candidates.append(configured)
    candidates.append(repo / "assets" / "images" / "blog-img" / "teaching-greatest-teacher-hero.png")
    for p in candidates:
        if p.exists():
            return p
    return configured


def build_story_video(
    repo: Path,
    story_dir: Path,
    out_video: Path,
    voice_mp3: Path,
    fallback_visual: Path | None,
    dry_run: bool,
    log_lines: List[str],
) -> int:
    visual = choose_visual(story_dir, fallback_visual)
    if visual is None:
        log_lines.append(f"SKIP: no visual asset for {story_dir.name}")
        return -2

    out_video.parent.mkdir(parents=True, exist_ok=True)
    if visual.suffix.lower() in (".mp4", ".mov"):
        cmd = [
            "ffmpeg",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(visual),
            "-i",
            str(voice_mp3),
            "-shortest",
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "23",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(out_video),
        ]
    else:
        cmd = [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(visual),
            "-i",
            str(voice_mp3),
            "-shortest",
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "23",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(out_video),
        ]
    return run_cmd(cmd, log_lines, dry_run=dry_run)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build STW recordings/videos for queued stories and enabled IQ jobs")
    ap.add_argument("--config", default="stw-publish-schedule.json")
    ap.add_argument("--queue-csv", default="_data/stw_news_queue.csv")
    ap.add_argument("--story-root", default="shorts-packages/stw-news-2026-01")
    ap.add_argument("--lookahead-days", type=int, default=2)
    ap.add_argument(
        "--from-queue-upcoming-days",
        type=int,
        default=None,
        metavar="N",
        help="Build every queue story whose date is between today and today+N days (inclusive). Overrides --lookahead-days.",
    )
    ap.add_argument("--fallback-visual", default="output/assets/stw-news-opener.png")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--log", default="output/stw-recording-build.log")
    args = ap.parse_args()

    repo = repo_root()
    log_lines: List[str] = []
    schedule = load_json(repo / args.config, default={})

    queue_csv = repo / args.queue_csv
    story_root = repo / args.story_root
    fallback_visual = resolve_fallback_visual(repo, args.fallback_visual)

    today = date.today()
    due_stories: List[str] = []
    if args.from_queue_upcoming_days is not None:
        end = today + timedelta(days=max(0, args.from_queue_upcoming_days))
        due_stories = upcoming_stories_from_queue(queue_csv, today, end)
    else:
        for i in range(max(1, args.lookahead_days + 1)):
            slug = queue_story_for_date(queue_csv, today + timedelta(days=i - 1))
            if slug and slug not in due_stories:
                due_stories.append(slug)

    any_fail = False

    for story in due_stories:
        story_dir = story_root / story
        script_txt = story_dir / "script-elevenlabs.txt"
        voice_mp3 = repo / "output" / "audio" / f"stw-news-{story}.mp3"
        out_video = repo / "output" / "video" / f"stw-news-{story}-ready.mp4"

        if not script_txt.exists():
            any_fail = True
            log_lines.append(f"FAIL: missing script for {story}: {script_txt}")
            continue

        rc = run_cmd(
            [
                sys.executable,
                str(repo / "scripts" / "voice-generate.py"),
                "--in",
                str(script_txt),
                "--out",
                str(voice_mp3),
                "--preset",
                "stw-news",
            ],
            log_lines=log_lines,
            dry_run=args.dry_run,
        )
        if rc != 0:
            any_fail = True
            log_lines.append(f"FAIL: voice generation failed for {story}")
            continue

        rc = build_story_video(
            repo=repo,
            story_dir=story_dir,
            out_video=out_video,
            voice_mp3=voice_mp3,
            fallback_visual=fallback_visual,
            dry_run=args.dry_run,
            log_lines=log_lines,
        )
        if rc not in (0, -2):
            any_fail = True
            log_lines.append(f"FAIL: video assembly failed for {story}")
        elif rc == -2:
            any_fail = True

    # Assemble selected IQ jobs when enabled.
    enabled_ids = [str(j.get("id", "")) for j in schedule.get("jobs", []) if bool(j.get("enabled", False))]
    if "goalIQ-3min-visualization" in enabled_ids:
        rc = run_cmd([str(repo / "scripts" / "ship-goalIQ-assemble.sh")], log_lines=log_lines, dry_run=args.dry_run)
        if rc != 0:
            any_fail = True
    if "mentalIQ-1hour-focus" in enabled_ids:
        rc = run_cmd([str(repo / "scripts" / "ship-mentalIQ-assemble.sh")], log_lines=log_lines, dry_run=args.dry_run)
        if rc != 0:
            any_fail = True

    log_path = repo / args.log
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    if any_fail:
        print("Recording build completed with issues. See log.")
        sys.exit(1)
    print("Recording build completed OK.")


if __name__ == "__main__":
    main()
