#!/usr/bin/env bash
# mentalIQ — Assemble 1-hour video: Brain loop + voice + music
# Usage: ./scripts/ship-mentalIQ-assemble.sh

set -e

VIDEO="/Users/rashadwest/Desktop/Brain Videos/MentalIQ_brain.mp4"
AUDIO="/Users/rashadwest/Desktop/SportsTechWest_visualizeIQ/MentalIQ_1hour_focus.m4a"
MUSIC="/Users/rashadwest/Sportstechwest/output/music/background-manifestation-60min/track-a.mp3"
OUT="/Users/rashadwest/Sportstechwest/output/video/mentalIQ-1hour-focus.mp4"

# Ensure paths exist
[[ -f "$VIDEO" ]] || { echo "❌ Video not found: $VIDEO"; exit 1; }
[[ -f "$AUDIO" ]] || { echo "❌ Audio not found: $AUDIO"; exit 1; }
[[ -f "$MUSIC" ]] || { echo "❌ Music not found: $MUSIC"; exit 1; }

echo "🎬 Assembling mentalIQ 1-hour..."
echo "   Video: MentalIQ_brain.mp4 (looped)"
echo "   Audio: MentalIQ_1hour_focus.m4a"
echo "   Music: track-a.mp3 (35%)"
echo "   Out:   $OUT"
echo ""

ffmpeg -y \
  -stream_loop -1 -i "$VIDEO" \
  -stream_loop -1 -i "$AUDIO" \
  -i "$MUSIC" \
  -t 3600 \
  -filter_complex "[1:a]volume=1[a1];[2:a]volume=0.35[a2];[a1][a2]amix=inputs=2:duration=first:dropout_transition=2[aout]" \
  -map 0:v -map "[aout]" \
  -c:v libx264 -preset fast -crf 23 \
  -c:a aac -b:a 192k \
  "$OUT"

echo ""
echo "✅ Wrote: $OUT"
echo ""
echo "Next: youtube-upload or see docs/MENTALIQ-POST-PLAN.md"
