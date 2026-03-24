#!/usr/bin/env bash
# mentalIQ — Full automated push: assemble + YouTube upload
# Usage: ./scripts/ship-mentalIQ-push.sh [--skip-assemble] [--no-upload]

set -e

REPO="$(cd "$(dirname "$0")/.." && pwd)"
MP4="$REPO/output/video/mentalIQ-1hour-focus.mp4"
METADATA="$REPO/audio-scripts/youtube-mentalIQ-1hour-focus.txt"
SKIP_ASSEMBLE=false
NO_UPLOAD=false

for arg in "$@"; do
  case "$arg" in
    --skip-assemble) SKIP_ASSEMBLE=true ;;
    --no-upload)    NO_UPLOAD=true ;;
  esac
done

echo "🧠 mentalIQ Push"
echo "   Repo: $REPO"
echo ""

# 1. Assemble
if [[ "$SKIP_ASSEMBLE" != "true" ]]; then
  echo "📦 Step 1: Assemble video..."
  "$REPO/scripts/ship-mentalIQ-assemble.sh"
  echo ""
else
  echo "📦 Step 1: Skip assemble (--skip-assemble)"
  if [[ ! -f "$MP4" ]]; then
    echo "❌ Video not found. Run without --skip-assemble first."
    exit 1
  fi
  echo ""
fi

# 2. YouTube upload
if [[ "$NO_UPLOAD" != "true" ]]; then
  echo "📤 Step 2: YouTube upload..."
  python3 "$REPO/scripts/youtube-upload.py" \
    --mp4 "$MP4" \
    --metadata-file "$METADATA" \
    --title "1 Hour Mental Focus for Sports | mentalIQ | Sportstechwest" \
    --privacy public \
    --confirm
  echo ""
  echo "✅ mentalIQ pushed to YouTube."
else
  echo "📤 Step 2: Skip upload (--no-upload)"
  echo ""
  echo "To upload manually:"
  echo "  python3 scripts/youtube-upload.py --mp4 $MP4 --metadata-file $METADATA --title \"1 Hour Mental Focus for Sports | mentalIQ | Sportstechwest\" --privacy public --confirm"
fi

echo ""
echo "📱 Social posts: see docs/MENTALIQ-POST-PLAN.md (LinkedIn, Instagram, X)"
