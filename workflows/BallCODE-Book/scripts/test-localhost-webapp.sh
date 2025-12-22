#!/bin/bash
# Localhost Testing Script for BallCODE
# Tests website on localhost with mobile/desktop preview

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEBSITE_DIR="$PROJECT_ROOT/BallCode"

cd "$WEBSITE_DIR"

echo "============================================================"
echo "🌐 BallCODE Localhost Testing"
echo "============================================================"
echo ""

# Get local IP address
LOCAL_IP=$(ipconfig getifaddr en0 2>/dev/null || ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

if [ -z "$LOCAL_IP" ]; then
    LOCAL_IP="localhost"
fi

echo "📱 Testing Instructions:"
echo ""
echo "1. Desktop Testing:"
echo "   Open: http://localhost:8000"
echo "   Or:   http://$LOCAL_IP:8000"
echo ""
echo "2. Mobile Testing (Same Network):"
echo "   Open on your phone: http://$LOCAL_IP:8000"
echo ""
echo "3. Chrome DevTools Mobile:"
echo "   - Press F12 or Cmd+Option+I"
echo "   - Click device toolbar icon"
echo "   - Test different device sizes"
echo ""
echo "4. Testing Checklist:"
echo "   [ ] Homepage loads correctly"
echo "   [ ] Navigation works"
echo "   [ ] Book 1 page accessible"
echo "   [ ] Exercise button works"
echo "   [ ] Mobile menu works"
echo "   [ ] Forms work on mobile"
echo "   [ ] Touch targets are 44px+"
echo "   [ ] No horizontal scroll"
echo "   [ ] Text is readable"
echo "   [ ] Images load properly"
echo ""

echo "🚀 Starting local server..."
echo "   Press Ctrl+C to stop"
echo ""

# Start Python HTTP server
python3 -m http.server 8000
