#!/bin/bash

# Set n8n Environment Variables via Terminal
# Works remotely - no SSH needed if n8n API is accessible

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# n8n URL
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo -e "${BLUE}🔧 Setting n8n Environment Variables via Terminal${NC}"
echo "n8n URL: ${N8N_URL}"
echo ""

# Check if n8n is accessible
echo -e "${BLUE}Checking n8n connection...${NC}"
if curl -s "${N8N_URL}/healthz" > /dev/null 2>&1; then
  echo -e "${GREEN}✅ n8n is accessible${NC}"
else
  echo -e "${RED}❌ Cannot connect to n8n${NC}"
  exit 1
fi
echo ""

# Method 1: Try via n8n API (if API key available)
if [ -n "$N8N_API_KEY" ]; then
  echo -e "${BLUE}Method 1: Using n8n API${NC}"
  
  VARS=(
    "UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git"
    "UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE"
    "WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
  )
  
  for var in "${VARS[@]}"; do
    KEY="${var%%=*}"
    VALUE="${var#*=}"
    
    echo "Setting ${KEY}..."
    RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${N8N_URL}/api/v1/settings" \
      -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"key\":\"${KEY}\",\"value\":\"${VALUE}\"}")
    
    HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
    BODY=$(echo "$RESPONSE" | sed '$d')
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
      echo -e "${GREEN}  ✅ Set ${KEY}${NC}"
    else
      echo -e "${YELLOW}  ⚠️  API method failed (HTTP ${HTTP_CODE})${NC}"
      echo "  Response: $BODY"
    fi
  done
  echo ""
fi

# Method 2: Direct database access (if on same machine or mounted)
echo -e "${BLUE}Method 2: Direct database access${NC}"
echo "Checking for n8n database..."

# Common n8n database locations
DB_PATHS=(
  "$HOME/.n8n/database.sqlite"
  "/root/.n8n/database.sqlite"
  "/home/pi/.n8n/database.sqlite"
  "/var/lib/n8n/database.sqlite"
)

DB_FOUND=""
for db_path in "${DB_PATHS[@]}"; do
  if [ -f "$db_path" ]; then
    DB_FOUND="$db_path"
    break
  fi
done

if [ -n "$DB_FOUND" ]; then
  echo -e "${GREEN}✅ Found database: ${DB_FOUND}${NC}"
  echo ""
  
  # Use Python script if available
  if command -v python3 &> /dev/null; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -f "${SCRIPT_DIR}/robot-set-n8n-env-vars.py" ]; then
      echo "Running Python script..."
      python3 "${SCRIPT_DIR}/robot-set-n8n-env-vars.py"
      if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Variables set via database!${NC}"
        echo ""
        echo -e "${YELLOW}⚠️  Restart n8n for changes to take effect:${NC}"
        echo "  ssh pi@192.168.1.226 'sudo systemctl restart n8n'"
        exit 0
      fi
    fi
  fi
else
  echo -e "${YELLOW}⚠️  Database not found locally${NC}"
  echo "n8n is running on remote server - need to set there"
fi
echo ""

# Method 3: SSH and run script remotely
echo -e "${BLUE}Method 3: SSH into Raspberry Pi and set remotely${NC}"
echo ""
echo "Run these commands:"
echo ""
echo "  # Copy script to Pi"
echo "  scp robot-set-n8n-env-vars.py pi@192.168.1.226:~/"
echo ""
echo "  # SSH and run"
echo "  ssh pi@192.168.1.226 'python3 ~/robot-set-n8n-env-vars.py'"
echo ""
echo "  # Restart n8n"
echo "  ssh pi@192.168.1.226 'sudo systemctl restart n8n'"
echo ""

# Method 4: Check if n8n UI has environment variables page
echo -e "${BLUE}Method 4: Check n8n UI${NC}"
echo ""
echo "Try accessing:"
echo "  ${N8N_URL}/settings/environment-variables"
echo ""
echo "If that page exists, you can set variables there manually."
echo ""

echo -e "${YELLOW}📋 Variables to set:${NC}"
echo "  UNITY_REPO_URL = https://github.com/rashadwest/BallCode.git"
echo "  UNITY_PROJECT_PATH = /Users/rashadwest/BTEBallCODE"
echo "  WORKFLOW_PATH = /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
echo ""



