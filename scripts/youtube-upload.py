#!/usr/bin/env python3
"""
YouTube video upload via Google API.
Requires: pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
One-time: Get client_secrets.json from Google Cloud Console (YouTube Data API v3).
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Optional deps - fail with clear message if missing
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE = "youtube"
API_VERSION = "v3"
VALID_PRIVACY = ("public", "private", "unlisted")
TOKEN_PATH = Path(__file__).parent.parent / "secrets" / "youtube-token.json"
SECRETS_PATHS = [
    Path(__file__).parent.parent / "secrets" / "client_secrets.json",
    Path(__file__).parent.parent / "secrets" / "client_secret.json",
    Path(__file__).parent.parent / "secrets" / "youtube_client_secrets.json",
]


def get_secrets_path():
    for p in SECRETS_PATHS:
        if p.exists():
            return str(p)
    return None


def parse_metadata_file(path: str) -> dict:
    """Parse metadata file. Format:
    Line 1: title
    Blank line
    Description (multiline until TAGS line)
    TAGS (paste...): optional
    tag1, tag2, tag3
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")

    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    title = lines[0].strip() if lines else ""
    desc_lines = []
    tags = []

    i = 1
    while i < len(lines):
        line = lines[i]
        if re.match(r"^TAGS\s*[:(]", line, re.I):
            if i + 1 < len(lines):
                tags = [t.strip() for t in lines[i + 1].split(",") if t.strip()]
            break
        desc_lines.append(line)
        i += 1

    description = "\n".join(desc_lines).strip()
    return {"title": title, "description": description, "tags": tags}


def get_authenticated_service():
    creds = None
    token_p = TOKEN_PATH
    secrets_p = get_secrets_path()

    if not secrets_p:
        print("No client_secrets.json found. Place in secrets/ folder.")
        print("  Get from: https://console.cloud.google.com/apis/credentials")
        print("  Enable YouTube Data API v3 for your project.")
        sys.exit(1)

    if token_p.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(token_p), SCOPES)
        except Exception:
            pass

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(secrets_p, SCOPES)
            creds = flow.run_local_server(port=0)
        token_p.parent.mkdir(parents=True, exist_ok=True)
        with open(token_p, "w") as f:
            f.write(creds.to_json())

    return build(API_SERVICE, API_VERSION, credentials=creds)


def upload(youtube, mp4_path: str, metadata: dict, privacy: str, thumbnail_path: str = None):
    body = {
        "snippet": {
            "title": metadata["title"],
            "description": metadata["description"],
            "tags": metadata.get("tags", []),
            "categoryId": "17",  # 17 = Sports
        },
        "status": {"privacyStatus": privacy},
    }

    media = MediaFileUpload(mp4_path, mimetype="video/mp4", resumable=True, chunksize=8 * 1024 * 1024)

    request = youtube.videos().insert(part=",".join(body.keys()), body=body, media_body=media)
    response = None

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  Uploaded {int(status.progress() * 100)}%")

    video_id = response.get("id")
    print(f"Uploaded. Video ID: {video_id}")

    if thumbnail_path and Path(thumbnail_path).exists():
        try:
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_path, mimetype="image/jpeg", resumable=False),
            ).execute()
            print("Thumbnail set.")
        except HttpError as e:
            print(f"Thumbnail failed: {e}")

    return video_id


def main():
    ap = argparse.ArgumentParser(description="Upload video to YouTube")
    ap.add_argument("--mp4", required=True, help="Path to MP4 file")
    ap.add_argument("--metadata-file", help="Path to metadata file (title, description, tags)")
    ap.add_argument("--title", help="Override title")
    ap.add_argument("--description", help="Override description")
    ap.add_argument("--tags", help="Comma-separated tags (override)")
    ap.add_argument("--privacy", default="public", choices=VALID_PRIVACY)
    ap.add_argument("--thumbnail", help="Path to thumbnail image")
    ap.add_argument("--confirm", action="store_true", help="Skip confirmation prompt")
    args = ap.parse_args()

    mp4_path = Path(args.mp4).resolve()
    if not mp4_path.exists():
        print(f"Video not found: {mp4_path}")
        sys.exit(1)

    if args.metadata_file:
        metadata = parse_metadata_file(args.metadata_file)
    else:
        metadata = {"title": "Untitled", "description": "", "tags": []}

    if args.title:
        metadata["title"] = args.title
    if args.description:
        metadata["description"] = args.description
    if args.tags:
        metadata["tags"] = [t.strip() for t in args.tags.split(",")]

    print(f"Title: {metadata['title']}")
    print(f"Privacy: {args.privacy}")
    if not args.confirm:
        r = input("Upload? [y/N]: ")
        if r.lower() != "y":
            print("Aborted.")
            sys.exit(0)

    youtube = get_authenticated_service()
    try:
        vid = upload(youtube, str(mp4_path), metadata, args.privacy, args.thumbnail)
        print(f"URL: https://youtube.com/watch?v={vid}")
    except HttpError as e:
        print(f"HTTP error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
