#!/bin/bash
# Set ALL n8n Environment Variables on Pi - Complete Configuration
# This script sets all required environment variables for all workflows

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Complete Pi n8n Environment Variables Setup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

PI_USER="rw3hampton"
PI_IP="192.168.1.226"
PI_N8N_URL="http://192.168.1.226:5678"

echo -e "${YELLOW}📋 Configuration:${NC}"
echo "  Pi IP: $PI_IP"
echo "  n8n URL: $PI_N8N_URL"
echo ""

# Check if container exists
echo -e "${YELLOW}🔍 Checking current n8n container...${NC}"
CONTAINER_EXISTS=$(ssh ${PI_USER}@${PI_IP} "docker ps -a | grep -q n8n && echo 'yes' || echo 'no'")

if [ "$CONTAINER_EXISTS" = "yes" ]; then
    echo -e "${GREEN}✅ n8n container found${NC}"
    echo -e "${YELLOW}🛑 Stopping container...${NC}"
    ssh ${PI_USER}@${PI_IP} "docker stop n8n" || true
    echo -e "${YELLOW}🗑️  Removing container...${NC}"
    ssh ${PI_USER}@${PI_IP} "docker rm n8n" || true
    echo -e "${GREEN}✅ Old container removed${NC}"
else
    echo -e "${YELLOW}ℹ️  No existing container found, will create new one${NC}"
fi

echo ""
echo -e "${YELLOW}🚀 Starting n8n with ALL environment variables...${NC}"
echo ""

# Start container with ALL environment variables (single line command)
ssh ${PI_USER}@${PI_IP} "docker run -d --name n8n --restart unless-stopped -p 5678:5678 -e WEBHOOK_URL=http://192.168.1.226:5678/ -e N8N_HOST=192.168.1.226 -e N8N_PROTOCOL=http -e N8N_PORT=5678 -e N8N_SECURE_COOKIE=false -e N8N_INSTANCE_ROLE=prod -e GITHUB_REPO_OWNER=rashadwest -e GITHUB_REPO_NAME=BallCode -e GITHUB_WORKFLOW_FILE=unity-webgl-build.yml -e NETLIFY_SITE_NAME=ballcode-game -e NETLIFY_SITE_ID=REPLACE_ME_NETLIFY_SITE_ID -e UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git -e UNITY_PROJECT_PATH=/home/rw3hampton/Projects/BTEBallCODE -e WORKFLOW_PATH=/home/rw3hampton/workflows/BallCODE-Book n8nio/n8n:latest"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ n8n container started with ALL environment variables${NC}"
    echo ""
    echo -e "${YELLOW}⏳ Waiting for n8n to start...${NC}"
    sleep 8
    
    # Verify it's running
    if ssh ${PI_USER}@${PI_IP} "docker ps | grep -q n8n"; then
        echo -e "${GREEN}✅ n8n is running${NC}"
        echo ""
        
        # Verify environment variables
        echo -e "${YELLOW}🔍 Verifying environment variables...${NC}"
        ssh ${PI_USER}@${PI_IP} "docker exec n8n env | grep -E 'WEBHOOK_URL|N8N_HOST|GITHUB_|NETLIFY_|UNITY_|WORKFLOW_PATH|N8N_INSTANCE_ROLE' | sort"
        
        echo ""
        echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${GREEN}✅ SUCCESS! All environment variables configured${NC}"
        echo ""
        echo -e "${YELLOW}📝 Environment Variables Set:${NC}"
        echo "  ✅ WEBHOOK_URL=http://192.168.1.226:5678/"
        echo "  ✅ N8N_HOST=192.168.1.226"
        echo "  ✅ N8N_PROTOCOL=http"
        echo "  ✅ N8N_PORT=5678"
        echo "  ✅ N8N_SECURE_COOKIE=false"
        echo "  ✅ N8N_INSTANCE_ROLE=prod"
        echo "  ✅ GITHUB_REPO_OWNER=rashadwest"
        echo "  ✅ GITHUB_REPO_NAME=BallCode"
        echo "  ✅ GITHUB_WORKFLOW_FILE=unity-webgl-build.yml"
        echo "  ✅ NETLIFY_SITE_NAME=ballcode-game"
        echo "  ✅ NETLIFY_SITE_ID=REPLACE_ME_NETLIFY_SITE_ID"
        echo "  ✅ UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git"
        echo "  ✅ UNITY_PROJECT_PATH=/home/rw3hampton/Projects/BTEBallCODE"
        echo "  ✅ WORKFLOW_PATH=/home/rw3hampton/workflows/BallCODE-Book"
        echo ""
        echo -e "${YELLOW}📝 Next Steps:${NC}"
        echo "  1. Open n8n: $PI_N8N_URL"
        echo "  2. Refresh the page"
        echo "  3. Open any workflow with a webhook"
        echo "  4. Check webhook URL - should now show $PI_IP instead of localhost"
        echo "  5. Verify all workflows can access environment variables"
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

