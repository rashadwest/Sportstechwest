#!/usr/bin/env bash
# Nightly RaSun prebuild (C4): voice + assemble approved episodes for today..today+2
# so 11:17 uploads do not wait on a cold ElevenLabs + hour-long encode.
# Invoked by launchd com.sportstechwest.rasun-prebuild at 02:13 local.
set -euo pipefail

ROOT="${STW_REPO_ROOT:-/Users/rashadwest/Sportstechwest}"
PYTHON_BIN="${PYTHON_BIN:-$ROOT/.venv/bin/python}"
if [[ ! -x "$PYTHON_BIN" ]]; then
  PYTHON_BIN="/usr/bin/python3"
fi
LOG_DIR="$ROOT/output/automation"
LOG="$ROOT/output/rasun-prebuild.log"

mkdir -p "$LOG_DIR" "$(dirname "$LOG")"
cd "$ROOT"
{
  echo "=== $(date '+%Y-%m-%dT%H:%M:%S%z') rasun-prebuild start ==="
  "$PYTHON_BIN" scripts/rasun-video.py build --upcoming 2
  echo "=== $(date '+%Y-%m-%dT%H:%M:%S%z') rasun-prebuild end rc=$? ==="
} >>"$LOG" 2>&1
