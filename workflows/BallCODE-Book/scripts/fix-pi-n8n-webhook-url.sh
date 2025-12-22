#!/bin/bash
# Fix Pi n8n Webhook URL - Add environment variables to Docker container
# This will restart the n8n container with correct webhook URL settings

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Fix Pi n8n Webhook URL${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

PI_USER="rw3hampton"
PI_IP="192.168.1.226"
PI_N8N_URL="http://192.168.1.226:5678"

echo -e "${YELLOW}📋 Current Configuration:${NC}"
echo "  Pi IP: $PI_IP"
echo "  n8n URL: $PI_N8N_URL"
echo ""

echo -e "${YELLOW}🔄 Stopping n8n container...${NC}"
ssh ${PI_USER}@${PI_IP} "docker stop n8n" || {
    echo -e "${RED}❌ Failed to stop container${NC}"
    exit 1
}

echo -e "${GREEN}✅ Container stopped${NC}"
echo ""

echo -e "${YELLOW}🗑️  Removing old container...${NC}"
ssh ${PI_USER}@${PI_IP} "docker rm n8n" || {
    echo -e "${YELLOW}⚠️  Container already removed or doesn't exist${NC}"
}

echo -e "${GREEN}✅ Old container removed${NC}"
echo ""

echo -e "${YELLOW}🚀 Starting n8n with correct webhook URL...${NC}"

# Start container with all existing env vars + new webhook vars
ssh ${PI_USER}@${PI_IP} << 'EOF'
docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -e UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git \
  -e UNITY_PROJECT_PATH=/home/rw3hampton/Projects/BTEBallCODE \
  -e WORKFLOW_PATH=/home/rw3hampton/workflows/BallCODE-Book \
  -e N8N_SECURE_COOKIE=false \
  -e GITHUB_REPO_OWNER=rashadwest \
  -e GITHUB_REPO_NAME=BallCode \
  -e GITHUB_WORKFLOW_FILE=unity-webgl-build.yml \
  -e NETLIFY_SITE_NAME=ballcode-game \
  -e NETLIFY_SITE_ID=REPLACE_ME_NETLIFY_SITE_ID \
  -e WEBHOOK_URL=http://192.168.1.226:5678/ \
  -e N8N_HOST=192.168.1.226 \
  -e N8N_PROTOCOL=http \
  -e N8N_PORT=5678 \
  n8nio/n8n:latest
EOF

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ n8n container started with correct webhook URL${NC}"
    echo ""
    echo -e "${YELLOW}⏳ Waiting for n8n to start...${NC}"
    sleep 5
    
    # Verify it's running
    if ssh ${PI_USER}@${PI_IP} "docker ps | grep -q n8n"; then
        echo -e "${GREEN}✅ n8n is running${NC}"
        echo ""
        echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${GREEN}✅ SUCCESS!${NC}"
        echo ""
        echo -e "${YELLOW}📝 Next Steps:${NC}"
        echo "  1. Open n8n: $PI_N8N_URL"
        echo "  2. Refresh the page"
        echo "  3. Open any workflow with a webhook"
        echo "  4. Check webhook URL - should now show $PI_IP instead of localhost"
        echo ""
        echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    else
        echo -e "${RED}❌ Container failed to start${NC}"
        echo "Check logs: ssh ${PI_USER}@${PI_IP} 'docker logs n8n'"
        exit 1
    fi
else
    echo -e "${RED}❌ Failed to start container${NC}"
    exit 1
fi


