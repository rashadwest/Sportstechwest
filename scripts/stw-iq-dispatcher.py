#!/usr/bin/env python3
"""
STW / IQ 24-7 dispatcher.

This script is designed to be run periodically (e.g., via n8n scheduleTrigger).
It reads `stw-publish-schedule.json` and uploads due jobs using `scripts/youtube-upload.py`.

Key behaviors:
- Runs idempotently using a JSON state file to avoid duplicate uploads per day.
- Supports daily schedules with a small grace window.
- Jobs are controlled by `enabled` in the JSON config.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, time as dt_time
from pathlib import Path
from typing import Any, Dict, List, Optional


def repo_root() -> Path:
    # scripts/<this_file>.py -> repo root is parent directory of scripts/
    return Path(__file__).resolve().parents[1]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def parse_hhmm(s: str) -> dt_time:
    # Accept "HH:MM" 24-hour format
    parts = s.strip().split(":")
    if len(parts) != 2:
        raise ValueError(f"Invalid time format: {s} (expected HH:MM)")
    hh = int(parts[0])
    mm = int(parts[1])
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        raise ValueError(f"Invalid time: {s}")
    return dt_time(hour=hh, minute=mm)


def weekday_allowed(days: Optional[List[str]], weekday: int) -> bool:
    # weekday: Monday=0 ... Sunday=6
    if not days:
        return True
    norm = {d.strip().lower() for d in days}
    mapping = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return mapping[weekday] in norm


@dataclass(frozen=True)
class DueDecision:
    due: bool
    reason: str


def compute_due(job: Dict[str, Any], now: datetime, state: Dict[str, Any], grace_minutes: int) -> DueDecision:
    enabled = bool(job.get("enabled", False))
    if not enabled:
        return DueDecision(due=False, reason="job disabled")

    job_id = str(job.get("id") or "")
    schedule = job.get("schedule") or {}
    sched_type = str(schedule.get("type") or "daily").lower()

    last_run_date = (state.get(job_id, {}) or {}).get("last_run_date")
    today = now.date().isoformat()

    if last_run_date == today:
        return DueDecision(due=False, reason="already ran today")

    if sched_type != "daily":
        return DueDecision(due=False, reason=f"unsupported schedule type: {sched_type}")

    time_str = str(schedule.get("time") or "")
    if not time_str:
        return DueDecision(due=False, reason="missing schedule.time")

    try:
        scheduled_local_time = parse_hhmm(time_str)
    except Exception as e:
        return DueDecision(due=False, reason=f"bad schedule.time: {e}")

    scheduled_dt = datetime.combine(now.date(), scheduled_local_time, tzinfo=now.tzinfo)
    grace_delta = timedelta(minutes=grace_minutes)
    window_end = scheduled_dt + grace_delta

    allowed_days = schedule.get("daysOfWeek") or schedule.get("days") or None
    if not weekday_allowed(allowed_days, now.weekday()):
        return DueDecision(due=False, reason="weekday not allowed")

    if now < scheduled_dt:
        return DueDecision(due=False, reason="not reached scheduled time yet")

    if now > window_end:
        return DueDecision(due=False, reason="outside grace window")

    return DueDecision(due=True, reason="within grace window and not run today")


def derive_title_from_filename(mp4_path: Path) -> str:
    # Basic fallback: "output/video/bikeiq-leisure.mp4" -> "bikeiq leisure"
    stem = mp4_path.stem
    cleaned = stem.replace("stw-news-", "").replace("-", " ")
    return cleaned.strip().title()


def parse_metadata_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    title = lines[0].strip() if lines else ""
    desc_lines: List[str] = []
    tags: List[str] = []
    i = 1
    while i < len(lines):
        line = lines[i]
        if re.match(r"^TAGS\s*[:(]", line, re.I):
            if i + 1 < len(lines):
                tags = [t.strip() for t in lines[i + 1].split(",") if t.strip()]
            break
        desc_lines.append(line)
        i += 1
    return {"title": title, "description": "\n".join(desc_lines).strip(), "tags": tags}


def queue_story_for_date(queue_path: Path, date_iso: str) -> str:
    if not queue_path.exists():
        return ""
    with queue_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row.get("date") or "").strip() == date_iso:
                return (row.get("story") or "").strip()
    return ""


def resolve_queue_job(job: Dict[str, Any], repo: Path, now: datetime, log_lines: List[str]) -> Dict[str, Any] | None:
    queue_csv = Path(str(job.get("queue_csv") or "_data/stw_news_queue.csv"))
    if not queue_csv.is_absolute():
        queue_csv = repo / queue_csv
    story = queue_story_for_date(queue_csv, now.date().isoformat())
    if not story:
        log_lines.append(f"JOB {job.get('id')}: no queue story for {now.date().isoformat()}")
        return None

    story_dir = Path(str(job.get("story_dir") or "shorts-packages/stw-news-2026-01"))
    if not story_dir.is_absolute():
        story_dir = repo / story_dir
    video_template = str(job.get("video_template") or "output/video/stw-news-{story}-ready.mp4")
    metadata_template = str(job.get("metadata_template") or "shorts-packages/stw-news-2026-01/{story}/youtube-test.txt")
    mp4_path = Path(video_template.format(story=story))
    if not mp4_path.is_absolute():
        mp4_path = repo / mp4_path
    metadata_path = Path(metadata_template.format(story=story))
    if not metadata_path.is_absolute():
        metadata_path = repo / metadata_path
    if not mp4_path.exists():
        log_lines.append(f"JOB {job.get('id')}: queued story '{story}' missing mp4 {mp4_path}")
        return None
    if not metadata_path.exists():
        log_lines.append(f"JOB {job.get('id')}: queued story '{story}' missing metadata {metadata_path}")
        return None

    parsed = parse_metadata_file(metadata_path)
    return {
        "id": f"{job.get('id')}:{story}",
        "action": "youtube_upload",
        "mp4": str(mp4_path),
        "privacy": str(job.get("privacy") or "unlisted"),
        "title": parsed.get("title") or derive_title_from_filename(mp4_path),
        "description": parsed.get("description") or str(job.get("description") or ""),
        "tags": parsed.get("tags") or job.get("tags") or [],
        "thumbnail": str(job.get("thumbnail") or ""),
    }


def run_youtube_upload(job: Dict[str, Any], repo: Path, dry_run: bool, log_lines: List[str], now: datetime) -> int:
    action = str(job.get("action") or "youtube_upload").lower()
    if action == "stw_news_queue_upload":
        resolved = resolve_queue_job(job, repo, now, log_lines)
        if resolved is None:
            return -2
        job = resolved
        action = "youtube_upload"
    if action != "youtube_upload":
        raise ValueError(f"Unsupported action: {action}")

    mp4_rel = job.get("mp4") or job.get("video") or ""
    if not mp4_rel:
        raise ValueError(f"Job {job.get('id')} missing mp4")

    mp4_path = Path(str(mp4_rel))
    if not mp4_path.is_absolute():
        mp4_path = repo / mp4_path

    title = str(job.get("title") or "").strip() or derive_title_from_filename(mp4_path)
    description = str(job.get("description") or "").strip()
    tags = job.get("tags") or []
    privacy = str(job.get("privacy") or "unlisted").strip()

    cmd: List[str] = [
        sys.executable,
        str(repo / "scripts" / "youtube-upload.py"),
        "--mp4",
        str(mp4_path),
        "--privacy",
        privacy,
        "--title",
        title,
        "--description",
        description,
        "--confirm",
    ]

    if tags:
        if isinstance(tags, str):
            # allow "a,b,c"
            cmd.extend(["--tags", tags])
        elif isinstance(tags, list):
            cmd.extend(["--tags", ",".join([str(t).strip() for t in tags if str(t).strip()])])
        else:
            raise ValueError(f"Job {job.get('id')} tags must be string or list")

    # thumbnail optional
    thumb = job.get("thumbnail") or job.get("thumb") or ""
    if thumb:
        thumb_path = Path(str(thumb))
        if not thumb_path.is_absolute():
            thumb_path = repo / thumb_path
        cmd.extend(["--thumbnail", str(thumb_path)])

    log_lines.append(f"RUN: {' '.join(cmd)}")
    if dry_run:
        return 0

    proc = subprocess.run(cmd, cwd=str(repo))
    return int(proc.returncode)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="stw-publish-schedule.json", help="Path to schedule JSON (relative to repo root by default)")
    ap.add_argument("--state", default="output/stw-iq-scheduler-state.json", help="State JSON to track last runs (relative to repo root by default)")
    ap.add_argument("--grace-minutes", type=int, default=20, help="How long after scheduled time to still run")
    ap.add_argument("--dry-run", action="store_true", help="Print actions but do not execute uploads")
    ap.add_argument(
        "--pause-uploads-until",
        default=None,
        help="Optional ISO datetime (local or with timezone) to pause all uploads until; overrides config pauseUploadsUntil",
    )
    ap.add_argument("--log", default="output/stw-iq-dispatcher.log", help="Log file (relative to repo root by default)")
    ap.add_argument(
        "--run-now",
        default="",
        help="Comma-separated job ids to upload immediately (ignores schedule and enabled; still respects pauseUploadsUntil unless you clear it)",
    )
    args = ap.parse_args()

    repo = repo_root()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = repo / config_path

    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = repo / state_path

    log_path = Path(args.log)
    if not log_path.is_absolute():
        log_path = repo / log_path

    config = load_json(config_path, default={})
    jobs = config.get("jobs") or []

    if not isinstance(jobs, list):
        raise SystemExit("Config error: jobs must be a list")

    state = load_json(state_path, default={})
    state_changed = False

    now = datetime.now().astimezone()
    log_lines: List[str] = []
    log_lines.append(f"=== dispatch start {now.isoformat()} ===")
    log_lines.append(f"config={config_path} state={state_path} dry_run={args.dry_run}")

    # Global safety guard:
    # If uploads are paused for the next N days, avoid any external API calls.
    pause_until_raw = args.pause_uploads_until or config.get("pauseUploadsUntil") or config.get("pausedUntil")
    if pause_until_raw:
        pause_until_raw = str(pause_until_raw).strip()
        try:
            # datetime.fromisoformat handles local datetimes and timezone offsets.
            pause_dt = datetime.fromisoformat(pause_until_raw.replace("Z", "+00:00"))
            if pause_dt.tzinfo is None:
                # Interpret "naive" ISO timestamp as local time.
                pause_dt = pause_dt.replace(tzinfo=now.tzinfo)
            if now < pause_dt:
                log_lines.append(f"GLOBAL PAUSE: skipping all uploads until {pause_dt.isoformat()}")
                log_path.parent.mkdir(parents=True, exist_ok=True)
                log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
                # n8n will treat this as success; no uploads happen.
                return
        except Exception as e:
            log_lines.append(f"GLOBAL PAUSE parse failed; ignoring: {e}")

    any_fail = False

    run_now_ids = [s.strip() for s in str(args.run_now or "").split(",") if s.strip()]
    jobs_by_id = {str(j.get("id") or ""): j for j in jobs if j.get("id")}

    if run_now_ids:
        log_lines.append(f"RUN-NOW mode: {run_now_ids}")
        for job_id in run_now_ids:
            job = jobs_by_id.get(job_id)
            if not job:
                any_fail = True
                log_lines.append(f"JOB {job_id}: UNKNOWN JOB ID (not in config)")
                continue
            try:
                log_lines.append(f"JOB {job_id}: run-now upload (schedule ignored)")
                rc = run_youtube_upload(job, repo=repo, dry_run=args.dry_run, log_lines=log_lines, now=now)
                if rc != 0:
                    if rc == -2:
                        log_lines.append(f"JOB {job_id}: skipped (no queue story or missing artifacts)")
                        continue
                    any_fail = True
                    log_lines.append(f"JOB {job_id}: FAILED rc={rc}")
                    continue
                state.setdefault(job_id, {})
                state[job_id]["last_run_date"] = now.date().isoformat()
                state[job_id]["last_run_at"] = now.isoformat()
                state_changed = True
                log_lines.append(f"JOB {job_id}: SUCCESS")
            except Exception as e:
                any_fail = True
                log_lines.append(f"JOB {job_id}: EXCEPTION: {e}")
    else:
        for job in jobs:
            job_id = str(job.get("id") or "")
            if not job_id:
                log_lines.append("SKIP: job missing id")
                continue

            decision = compute_due(job, now=now, state=state, grace_minutes=args.grace_minutes)
            log_lines.append(f"JOB {job_id}: enabled={job.get('enabled')} due={decision.due} reason={decision.reason}")

            if not decision.due:
                continue

            try:
                rc = run_youtube_upload(job, repo=repo, dry_run=args.dry_run, log_lines=log_lines, now=now)
                if rc != 0:
                    if rc == -2:
                        log_lines.append(f"JOB {job_id}: skipped (no queue story or missing artifacts)")
                        continue
                    any_fail = True
                    log_lines.append(f"JOB {job_id}: FAILED rc={rc}")
                    continue

                state.setdefault(job_id, {})
                state[job_id]["last_run_date"] = now.date().isoformat()
                state[job_id]["last_run_at"] = now.isoformat()
                state_changed = True
                log_lines.append(f"JOB {job_id}: SUCCESS")
            except Exception as e:
                any_fail = True
                log_lines.append(f"JOB {job_id}: EXCEPTION: {e}")

    if state_changed and not args.dry_run:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    # n8n executeCommand marks failure if exit code non-zero; we keep it 0 so the workflow doesn't get stuck.
    # The log captures failures.
    if any_fail:
        print("Dispatcher completed with failures (see log).")
    else:
        print("Dispatcher completed OK.")


if __name__ == "__main__":
    main()

