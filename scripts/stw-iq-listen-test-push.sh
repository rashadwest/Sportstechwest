#!/usr/bin/env bash
# Phase 1b: upload one (or all) listen-test drops as unlisted and append Morning Report queue.
# Usage:
#   ./scripts/stw-iq-listen-test-push.sh bikeiq-breathe-every-5-pedals
#   ./scripts/stw-iq-listen-test-push.sh --all
# Does NOT flip videos public. Manual Studio publish after you listen.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="${STW_LISTEN_MANIFEST:-$ROOT/stw-iq-test-listen.manifest.json}"
PYTHON="${PYTHON_BIN:-$ROOT/.venv/bin/python}"
[[ -x "$PYTHON" ]] || PYTHON="python3"
QUEUE_DEFAULT="$ROOT/output/stw-iq-listen-queue.json"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Missing manifest: $MANIFEST" >&2
  exit 1
fi

IDS=("$@")
if [[ ${#IDS[@]} -eq 0 ]]; then
  echo "Usage: $0 <drop-id>|--all" >&2
  exit 2
fi

export MANIFEST QUEUE_DEFAULT
"$PYTHON" - "$ROOT" "${IDS[@]}" <<'PY'
import json, os, subprocess, sys
from pathlib import Path

root = Path(sys.argv[1])
want = sys.argv[2:]
manifest = json.loads(Path(os.environ["MANIFEST"]).read_text(encoding="utf-8"))
queue = Path(manifest.get("listen_queue") or os.environ["QUEUE_DEFAULT"])
if not queue.is_absolute():
    queue = root / queue
drops = manifest.get("drops") or []
if want == ["--all"]:
    selected = drops
else:
    ids = set(want)
    selected = [d for d in drops if d.get("id") in ids]
    missing = ids - {d.get("id") for d in selected}
    if missing:
        print("Unknown drop id(s):", ", ".join(sorted(missing)), file=sys.stderr)
        sys.exit(2)

py = os.environ.get("PYTHON_BIN") or sys.executable
for d in selected:
    mp4 = root / d["mp4"]
    meta = root / d["metadata_txt"]
    if not mp4.exists():
        print(f"SKIP {d['id']}: missing {mp4}", file=sys.stderr)
        continue
    if not meta.exists():
        print(f"SKIP {d['id']}: missing {meta}", file=sys.stderr)
        continue
    cmd = [
        py, str(root / "scripts" / "youtube-upload.py"),
        "--mp4", str(mp4),
        "--metadata-file", str(meta),
        "--title", d.get("title") or "LISTEN TEST",
        "--privacy", d.get("privacy") or "unlisted",
        "--write-listen-queue", str(queue),
        "--listen-id", d["id"],
        "--confirm",
    ]
    thumb = d.get("thumbnail") or ""
    if thumb:
        tp = root / thumb
        if tp.exists():
            cmd.extend(["--thumbnail", str(tp)])
    if d.get("synthetic_media"):
        cmd.append("--synthetic-media")
    print("RUN:", " ".join(cmd))
    rc = subprocess.run(cmd, cwd=str(root)).returncode
    if rc != 0:
        sys.exit(rc)
print("Done. Sync Morning Report with: scripts/stw-sync-listen-checklist.sh")
PY
