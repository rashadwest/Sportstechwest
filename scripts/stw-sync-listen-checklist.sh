#!/usr/bin/env bash
# Sync output/stw-iq-listen-queue.json into ~/personal-os/docs/checklist.md YouTube rows.
# Idempotent: refreshes matching "Listen unlisted <id>" lines; adds if missing.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
QUEUE="${1:-$ROOT/output/stw-iq-listen-queue.json}"
CHECKLIST="${CHECKLIST_FILE:-$HOME/personal-os/docs/checklist.md}"
ADD="$HOME/personal-os/tools/checklist-add.sh"

if [[ ! -f "$QUEUE" ]]; then
  echo "No listen queue yet: $QUEUE"
  exit 0
fi
if [[ ! -f "$CHECKLIST" ]]; then
  echo "Missing checklist: $CHECKLIST" >&2
  exit 1
fi

python3 - "$QUEUE" "$CHECKLIST" "$ADD" <<'PY'
import json, re, subprocess, sys
from pathlib import Path

queue_path, checklist_path, add_sh = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
data = json.loads(queue_path.read_text(encoding="utf-8"))
drops = data.get("drops") or []
if not drops:
    print("Listen queue empty.")
    sys.exit(0)

text = checklist_path.read_text(encoding="utf-8")
lines = text.splitlines()
# Drop prior auto listen rows for these ids so we can re-add fresh URLs.
id_pat = re.compile(r"Listen unlisted ([a-z0-9-]+)", re.I)
keep = []
for ln in lines:
    m = id_pat.search(ln)
    if m and any(m.group(1) == d.get("id") for d in drops):
        continue
    keep.append(ln)
checklist_path.write_text("\n".join(keep) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")

for d in drops:
    did = d.get("id") or "unknown"
    url = d.get("watch_url") or ""
    title = (d.get("title") or did)[:60]
    task = f"Listen unlisted {did} ({title}) {url} — full listen, then Public in Studio when ready {{8}}"
    subprocess.run([str(add_sh), "YouTube", task], check=True)
    print("checklist:", did, url)
PY
