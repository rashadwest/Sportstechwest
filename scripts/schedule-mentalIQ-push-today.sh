#!/usr/bin/env bash
# Schedule mentalIQ push for later today without needing macOS `at` (which often fails until atrun is enabled).
#
# Usage:
#   ./scripts/schedule-mentalIQ-push-today.sh --delay-minutes 90    # run push in 90 minutes (recommended if `at` fails)
#   ./scripts/schedule-mentalIQ-push-today.sh 6pm                  # uses `at` (needs: sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist)
#
# List at jobs: atq   |   Cancel: atrm <id>

set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
PUSH="$REPO/scripts/ship-mentalIQ-push.sh"

usage() {
  echo "Usage:"
  echo "  $0 --delay-minutes N   Schedule push in N minutes (works without \`at\`; runs in background)"
  echo "  $0 TIME                Schedule via \`at\` (e.g. 6pm, 21:00) — enable atrun first if you see lockfile errors"
  exit 1
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
fi

if [[ "${1:-}" == "--delay-minutes" ]]; then
  MINS="${2:-}"
  if ! [[ "$MINS" =~ ^[0-9]+$ ]] || [[ "$MINS" -lt 1 ]]; then
    echo "❌ Need positive integer minutes after --delay-minutes"
    usage
  fi
  SEC=$((MINS * 60))
  LOG="$REPO/output/mentalIQ-scheduled-push.log"
  mkdir -p "$(dirname "$LOG")"
  echo "Scheduling mentalIQ push in $MINS minutes ($SEC s). Log: $LOG"
  (
    sleep "$SEC"
    echo "=== $(date '+%Y-%m-%dT%H:%M:%S') ===" >>"$LOG"
    cd "$REPO" && "$PUSH" >>"$LOG" 2>&1
    echo "=== done $(date '+%Y-%m-%dT%H:%M:%S') ===" >>"$LOG"
  ) &
  BG_PID=$!
  echo "✅ Background job started (PID $BG_PID). Push will run in ~$MINS min."
  echo "   Tail log: tail -f $LOG"
  echo "   Kill job: kill $BG_PID"
  exit 0
fi

TIME="${1:-6pm}"

if ! command -v at >/dev/null 2>&1; then
  echo "❌ 'at' not installed. Use:"
  echo "   $0 --delay-minutes 120"
  exit 1
fi

OUT=$(mktemp)
set +e
set -o pipefail
printf 'export PATH="%s"\ncd "%s" && ./scripts/ship-mentalIQ-push.sh\n' "$PATH" "$REPO" | at "$TIME" 2>"$OUT"
AT_EXIT=$?
set +o pipefail
set -e
if [[ "$AT_EXIT" -eq 0 ]]; then
  rm -f "$OUT"
  echo "✅ mentalIQ push scheduled with \`at\` for $TIME (local time)."
  echo "   List: atq   |   Cancel: atrm <id>"
  exit 0
else
  ERR=$(cat "$OUT" 2>/dev/null || true)
  rm -f "$OUT"
  echo "❌ \`at\` failed (exit $AT_EXIT):"
  echo "$ERR"
  echo ""
  echo "Fix on macOS (one-time, then retry):"
  echo "   sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist"
  echo ""
  echo "Or skip \`at\` and delay in minutes instead:"
  echo "   $0 --delay-minutes 120"
  exit 1
fi
