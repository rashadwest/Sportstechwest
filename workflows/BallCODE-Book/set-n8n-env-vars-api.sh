#!/bin/bash

# Set n8n Environment Variables via API
# Works for remote n8n instances

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# n8n URL (Raspberry Pi)
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

# Environment variables to set
VARS=(
  "UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git"
  "UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE"
  "WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
)

echo -e "${BLUE}🔧 Setting n8n Environment Variables via API${NC}"
echo "n8n URL: ${N8N_URL}"
echo ""

# Check if n8n is accessible
if ! curl -s "${N8N_URL}/healthz" > /dev/null 2>&1; then
  echo -e "${RED}❌ Cannot connect to n8n at ${N8N_URL}${NC}"
  echo ""
  echo "Please check:"
  echo "  1. n8n is running"
  echo "  2. URL is correct: ${N8N_URL}"
  echo "  3. Network connectivity"
  exit 1
fi

echo -e "${GREEN}✅ n8n is accessible${NC}"
echo ""

# Note: n8n API requires authentication for setting env vars
# This script shows the manual steps needed

echo -e "${YELLOW}⚠️  Note: n8n API requires authentication to set environment variables${NC}"
echo ""
echo "You have two options:"
echo ""
echo "Option 1: Set via n8n UI (if accessible):"
echo "  1. Go to: ${N8N_URL}/settings/environment-variables"
echo "  2. Add each variable manually"
echo ""
echo "Option 2: Use the Python script on the Raspberry Pi:"
echo "  1. SSH into Raspberry Pi: ssh pi@192.168.1.226"
echo "  2. Copy robot-set-n8n-env-vars.py to the Pi"
echo "  3. Run: python3 robot-set-n8n-env-vars.py"
echo ""
echo "Variables to set:"
for var in "${VARS[@]}"; do
  echo "  ${var}"
done
echo ""

# If API key is available, try to set via API
if [ -n "$N8N_API_KEY" ]; then
  echo -e "${BLUE}Attempting to set via API...${NC}"
  
  for var in "${VARS[@]}"; do
    KEY="${var%%=*}"
    VALUE="${var#*=}"
    
    echo "Setting ${KEY}..."
    
    # Note: This endpoint may vary by n8n version
    RESPONSE=$(curl -s -X POST "${N8N_URL}/api/v1/settings" \
      -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"key\":\"${KEY}\",\"value\":\"${VALUE}\"}")
    
    if [ $? -eq 0 ]; then
      echo -e "${GREEN}  ✅ Set ${KEY}${NC}"
    else
      echo -e "${RED}  ❌ Failed to set ${KEY}${NC}"
    fi
  done
else
  echo -e "${YELLOW}No API key set. Using manual method.${NC}"
fi

echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "  1. Set variables (using one of the methods above)"
echo "  2. Restart n8n on Raspberry Pi"
echo "  3. Test workflow again"
echo ""


