#!/usr/bin/env python3
"""
Schedule RaSun private drafts to go public on their queue date.

Every RaSun episode is uploaded as a private draft for the listen check, and the
dispatcher then skips it on its date because it already has a video ID. Without
this script, nothing goes public unless someone flips each video in Studio.

This sets YouTube's scheduled publish (status.publishAt) on each approved,
already-uploaded episode in _data/rasun_queue.csv, so it stays private until its
date and then publishes on its own. To stop one, set it back to private in
Studio or delete its queue row and run this again with --clear.

Usage:
  python3 scripts/rasun-schedule-publish.py --dry-run
  python3 scripts/rasun-schedule-publish.py
  python3 scripts/rasun-schedule-publish.py --time 05:47
  python3 scripts/rasun-schedule-publish.py --only walkingiq-5-4-3-2-1-senses

Changing a video's status needs the "youtube" scope, which the upload token does
not have, so this keeps its own token at secrets/youtube-token-manage.json and
asks for consent once in the browser on first real run.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime, time as dt_time
from pathlib import Path
from typing import Any, Dict, List

REPO = Path(__file__).resolve().parents[1]
QUEUE = REPO / "_data" / "rasun_queue.csv"
PACKAGES = REPO / "video-packages" / "rasun"
SECRETS = REPO / "secrets"
TOKEN_PATH = SECRETS / "youtube-token-manage.json"
SECRETS_NAMES = ("client_secrets.json", "client_secret.json", "youtube_client_secrets.json")
SCOPES = ["https://www.googleapis.com/auth/youtube"]

# The only status fields videos.update accepts; anything left out is reset.
WRITABLE_STATUS = (
    "privacyStatus",
    "publishAt",
    "license",
    "embeddable",
    "publicStatsViewable",
    "selfDeclaredMadeForKids",
    "containsSyntheticMedia",
)


def load_queue(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [
            {"date": (r.get("date") or "").strip(), "story": (r.get("story") or "").strip()}
            for r in csv.DictReader(f)
            if (r.get("date") or "").strip() and (r.get("story") or "").strip()
        ]


def publish_at_iso(day: str, at: dt_time) -> str:
    local = datetime.combine(date.fromisoformat(day), at).astimezone()
    return local.isoformat(timespec="seconds")


def plan(queue: List[Dict[str, str]], at: dt_time, now: datetime, only: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for item in queue:
        slug = item["story"]
        if only and slug != only:
            continue
        pkg_path = PACKAGES / slug / "package.json"
        row: Dict[str, Any] = {"date": item["date"], "slug": slug, "pkg_path": pkg_path}
        if not pkg_path.exists():
            row["action"], row["why"] = "skip", "no package.json"
            rows.append(row)
            continue
        pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
        row["pkg"] = pkg
        video_id = str(pkg.get("youtube_video_id") or "").strip()
        row["video_id"] = video_id
        when = publish_at_iso(item["date"], at)
        row["publish_at"] = when
        if not pkg.get("approved"):
            row["action"], row["why"] = "skip", "not approved"
        elif not video_id:
            row["action"], row["why"] = "skip", "not uploaded yet (dispatcher uploads it on its date)"
        elif datetime.fromisoformat(when) <= now:
            row["action"], row["why"] = "overdue", "date has passed; publish it in Studio or run with --publish-overdue"
        elif pkg.get("scheduled_publish_at") == when:
            row["action"], row["why"] = "skip", "already scheduled"
        else:
            row["action"], row["why"] = "schedule", ""
        rows.append(row)
    return rows


def get_service():
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        sys.exit("Missing dependencies. Run: pip install -r requirements-youtube.txt")

    secrets = next((SECRETS / n for n in SECRETS_NAMES if (SECRETS / n).exists()), None)
    if secrets is None:
        sys.exit("No client_secrets.json in secrets/ (same file the uploader uses).")

    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Opening the browser once to allow managing video visibility (youtube scope)...")
            creds = InstalledAppFlow.from_client_secrets_file(str(secrets), SCOPES).run_local_server(port=0)
        TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds)


def current_status(youtube, video_id: str) -> Dict[str, Any] | None:
    items = youtube.videos().list(part="status", id=video_id).execute().get("items") or []
    return items[0]["status"] if items else None


def update_status(youtube, video_id: str, status: Dict[str, Any], changes: Dict[str, Any]) -> None:
    body = {k: status[k] for k in WRITABLE_STATUS if k in status}
    body.update(changes)
    if body.get("privacyStatus") == "public":
        body.pop("publishAt", None)
    youtube.videos().update(part="status", body={"id": video_id, "status": body}).execute()


def save_pkg(row: Dict[str, Any], **fields: Any) -> None:
    pkg = row["pkg"]
    for k, v in fields.items():
        if v is None:
            pkg.pop(k, None)
        else:
            pkg[k] = v
    row["pkg_path"].write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--time", default="06:07", help="Local publish time on the queue date (HH:MM, default 06:07)")
    ap.add_argument("--only", default="", help="Only this slug")
    ap.add_argument("--dry-run", action="store_true", help="Show the plan; no YouTube calls")
    ap.add_argument("--publish-overdue", action="store_true", help="Make overdue private drafts public now")
    ap.add_argument("--clear", action="store_true", help="Remove scheduled publish from episodes no longer in the queue")
    args = ap.parse_args()

    hh, mm = (int(x) for x in args.time.split(":"))
    at = dt_time(hh, mm)
    now = datetime.now().astimezone()
    queue = load_queue(QUEUE)
    rows = plan(queue, at, now, args.only)

    stale: List[Dict[str, Any]] = []
    if args.clear:
        queued = {q["story"] for q in queue}
        for pkg_path in sorted(PACKAGES.glob("*/package.json")):
            slug = pkg_path.parent.name
            pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
            if slug not in queued and pkg.get("scheduled_publish_at") and pkg.get("youtube_video_id"):
                stale.append({"slug": slug, "pkg_path": pkg_path, "pkg": pkg, "video_id": pkg["youtube_video_id"]})

    for r in rows:
        when = r.get("publish_at", "")
        print(f"{r['date']}  {r['slug']:<42} {r['action']:<9} {when if r['action'] == 'schedule' else r['why']}")
    for s in stale:
        print(f"{'':10}  {s['slug']:<42} {'clear':<9} not in queue; remove scheduled publish")

    todo = [r for r in rows if r["action"] == "schedule" or (r["action"] == "overdue" and args.publish_overdue)]
    if args.dry_run or not (todo or stale):
        if not args.dry_run:
            print("Nothing to change.")
        return

    youtube = get_service()
    for r in todo:
        status = current_status(youtube, r["video_id"])
        if status is None:
            print(f"  {r['slug']}: video {r['video_id']} not found on the channel; skipped")
            continue
        if status.get("privacyStatus") == "public":
            print(f"  {r['slug']}: already public; recording that")
            save_pkg(r, scheduled_publish_at=None)
            continue
        if r["action"] == "overdue":
            update_status(youtube, r["video_id"], status, {"privacyStatus": "public"})
            save_pkg(r, scheduled_publish_at=None)
            print(f"  {r['slug']}: published now")
        else:
            update_status(youtube, r["video_id"], status, {"privacyStatus": "private", "publishAt": r["publish_at"]})
            save_pkg(r, scheduled_publish_at=r["publish_at"])
            print(f"  {r['slug']}: scheduled for {r['publish_at']}")
    for s in stale:
        status = current_status(youtube, s["video_id"])
        if status and status.get("privacyStatus") == "private":
            status.pop("publishAt", None)
            update_status(youtube, s["video_id"], status, {"privacyStatus": "private"})
        save_pkg(s, scheduled_publish_at=None)
        print(f"  {s['slug']}: scheduled publish removed")


if __name__ == "__main__":
    main()
