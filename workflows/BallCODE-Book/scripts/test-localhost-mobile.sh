#!/bin/bash
# Localhost Mobile Testing Script
# Starts local server and provides mobile testing instructions

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WEBSITE_DIR="$PROJECT_ROOT/BallCode"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📱 Localhost Mobile Testing Setup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "$WEBSITE_DIR/index.html" ]; then
    echo -e "${RED}❌ Error: index.html not found in $WEBSITE_DIR${NC}"
    exit 1
fi

# Get local IP address
LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

if [ -z "$LOCAL_IP" ]; then
    LOCAL_IP="localhost"
fi

echo -e "${YELLOW}Starting local server...${NC}"
echo ""

cd "$WEBSITE_DIR"

# Start Python HTTP server in background
PORT=8000
python3 -m http.server $PORT > /tmp/ballcode-server.log 2>&1 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

# Check if server started successfully
if ps -p $SERVER_PID > /dev/null; then
    echo -e "${GREEN}✅ Server started on port $PORT${NC}"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}🌐 Access URLs:${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "Desktop: ${GREEN}http://localhost:$PORT${NC}"
    echo -e "Mobile (same network): ${GREEN}http://$LOCAL_IP:$PORT${NC}"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}📱 Mobile Testing Instructions:${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "1. Make sure your phone is on the same Wi-Fi network"
    echo "2. Open browser on your phone"
    echo "3. Navigate to: http://$LOCAL_IP:$PORT"
    echo ""
    echo -e "${YELLOW}Alternative: Use Chrome DevTools${NC}"
    echo "1. Open Chrome on desktop"
    echo "2. Press F12 (or Cmd+Option+I on Mac)"
    echo "3. Click device toolbar icon (or Cmd+Shift+M)"
    echo "4. Select device (iPhone, iPad, etc.)"
    echo "5. Navigate to: http://localhost:$PORT"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}🧪 Test Checklist:${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "□ Navigation menu works (hamburger on mobile)"
    echo "□ All text is readable (no overflow)"
    echo "□ Buttons are tappable (good touch targets)"
    echo "□ Images scale properly"
    echo "□ Contact form is usable"
    echo "□ Book cards display correctly"
    echo "□ About section is readable"
    echo "□ FAQ accordion works"
    echo "□ Social media links work"
    echo "□ Book 1 page link works"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    # Wait for user to stop
    trap "kill $SERVER_PID 2>/dev/null; echo ''; echo 'Server stopped.'; exit 0" INT TERM
    
    # Keep script running
    wait $SERVER_PID
else
    echo -e "${RED}❌ Failed to start server${NC}"
    echo "Check /tmp/ballcode-server.log for errors"
    exit 1
fi


