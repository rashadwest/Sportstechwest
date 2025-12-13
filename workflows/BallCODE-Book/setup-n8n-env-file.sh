#!/bin/bash

# Setup .env file for local n8n installation
# Creates .env file with required environment variables

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🔧 Setting up .env file for local n8n${NC}"
echo ""

# Find n8n directory
N8N_DIR=""

# Check common locations
if [ -d ~/.n8n ]; then
  N8N_DIR="$HOME/.n8n"
  echo -e "${GREEN}✅ Found n8n directory: ${N8N_DIR}${NC}"
elif [ -d ~/n8n ]; then
  N8N_DIR="$HOME/n8n"
  echo -e "${GREEN}✅ Found n8n directory: ${N8N_DIR}${NC}"
else
  echo -e "${YELLOW}⚠️  n8n directory not found in common locations${NC}"
  echo ""
  read -p "Enter the path to your n8n project directory (where you run 'n8n start'): " N8N_DIR
  
  if [ ! -d "$N8N_DIR" ]; then
    echo -e "${RED}❌ Directory not found: ${N8N_DIR}${NC}"
    exit 1
  fi
fi

echo ""
echo -e "${BLUE}Creating .env file in: ${N8N_DIR}${NC}"
echo ""

# Create .env file
ENV_FILE="${N8N_DIR}/.env"

# Check if .env already exists
if [ -f "$ENV_FILE" ]; then
  echo -e "${YELLOW}⚠️  .env file already exists${NC}"
  echo ""
  read -p "Backup existing .env and create new one? (y/n): " backup_choice
  
  if [ "$backup_choice" = "y" ] || [ "$backup_choice" = "Y" ]; then
    cp "$ENV_FILE" "${ENV_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
    echo -e "${GREEN}✅ Backed up to: ${ENV_FILE}.backup.*${NC}"
  else
    echo -e "${YELLOW}⚠️  Appending to existing .env file${NC}"
    echo "" >> "$ENV_FILE"
    echo "# Added by setup script on $(date)" >> "$ENV_FILE"
  fi
fi

# Add environment variables
echo -e "${BLUE}Adding environment variables...${NC}"

# Check if variables already exist
if grep -q "UNITY_REPO_URL" "$ENV_FILE" 2>/dev/null; then
  echo -e "${YELLOW}⚠️  UNITY_REPO_URL already exists in .env${NC}"
  read -p "Overwrite? (y/n): " overwrite
  if [ "$overwrite" = "y" ] || [ "$overwrite" = "Y" ]; then
    # Remove existing lines
    sed -i.bak '/^UNITY_REPO_URL=/d' "$ENV_FILE" 2>/dev/null || sed -i '' '/^UNITY_REPO_URL=/d' "$ENV_FILE" 2>/dev/null
    sed -i.bak '/^UNITY_PROJECT_PATH=/d' "$ENV_FILE" 2>/dev/null || sed -i '' '/^UNITY_PROJECT_PATH=/d' "$ENV_FILE" 2>/dev/null
    sed -i.bak '/^WORKFLOW_PATH=/d' "$ENV_FILE" 2>/dev/null || sed -i '' '/^WORKFLOW_PATH=/d' "$ENV_FILE" 2>/dev/null
  fi
fi

# Append variables to .env file
cat >> "$ENV_FILE" << EOF

# Unity Automation Environment Variables
# Added on $(date)
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF

echo -e "${GREEN}✅ Added environment variables to .env${NC}"
echo ""

# Show what was added
echo -e "${BLUE}📋 Variables added:${NC}"
echo "  UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git"
echo "  UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE"
echo "  WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
echo ""

# Show .env file location
echo -e "${BLUE}📁 .env file location:${NC}"
echo "  ${ENV_FILE}"
echo ""

# Security reminder
echo -e "${YELLOW}🔒 Security Reminder:${NC}"
echo "  - Don't commit .env to Git"
echo "  - Keep .env file secure"
echo "  - Add .env to .gitignore"
echo ""

# Next steps
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "  1. Restart n8n:"
echo "     - If running in terminal: Stop (Ctrl+C) and run 'n8n start'"
echo "     - If running as service: 'n8n stop' then 'n8n start'"
echo ""
echo "  2. Test in n8n workflow:"
echo "     - Add a Code node"
echo "     - Type: {{ \$env.UNITY_REPO_URL }}"
echo "     - Should show: https://github.com/rashadwest/BallCode.git"
echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"

