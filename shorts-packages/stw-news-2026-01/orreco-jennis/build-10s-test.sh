#!/usr/bin/env bash
#
# Build a 10-second test MP4 for STW News (Orreco/Jennis).
# Uses: one image (STW News opener) + one audio file (first ~10s of voice from ElevenLabs).
#
# Usage:
#   1. Create STW News opener image (e.g. stw-news-opener.png) — black/deep blue + "STW News" + logo.
#   2. In ElevenLabs, paste only: "An Olympic champion's app just became core infrastructure for pro women's sports."
#      Generate and save as voice-10s.mp3 (or trim full script to 10s).
#   3. Run: ./build-10s-test.sh [path/to/opener.png] [path/to/voice-10s.mp3]
#      Defaults: opener = stw-news-opener.png in this folder; audio = voice-10s.mp3 in this folder.
#   4. Upload: see README in parent folder or run the upload command below.
#
# Requires: ffmpeg

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
OUT_DIR="${REPO_ROOT}/output/video"
mkdir -p "$OUT_DIR"

IMAGE="${1:-$SCRIPT_DIR/stw-news-opener.png}"
AUDIO="${2:-$SCRIPT_DIR/voice-10s.mp3}"
OUT="${OUT_DIR}/stw-news-orreco-jennis-10s-test.mp4"

if [[ ! -f "$IMAGE" ]]; then
  echo "❌ Image not found: $IMAGE"
  echo "   Create an STW News opener (black/deep blue + 'STW News' + logo) and save as stw-news-opener.png in this folder."
  exit 1
fi
if [[ ! -f "$AUDIO" ]]; then
  echo "❌ Audio not found: $AUDIO"
  echo "   Generate ~10s of voice in ElevenLabs (first line of script) and save as voice-10s.mp3 in this folder."
  exit 1
fi

echo "Building 10s test: image=$IMAGE, audio=$AUDIO"
ffmpeg -y -loop 1 -i "$IMAGE" -i "$AUDIO" -c:v libx264 -t 10 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -shortest -c:a aac "$OUT"
echo "✅ Output: $OUT"
echo ""
echo "Upload unlisted:"
echo "  python $REPO_ROOT/scripts/youtube-upload.py --mp4 $OUT --metadata-file $SCRIPT_DIR/youtube-test.txt --privacy unlisted --confirm"
echo ""
