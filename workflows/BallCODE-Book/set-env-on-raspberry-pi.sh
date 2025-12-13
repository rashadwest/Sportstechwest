#!/bin/bash

# Set .env file on Raspberry Pi for n8n
# This sets environment variables on the remote Pi instance

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

PI_HOST="pi@192.168.1.226"
N8N_DIR="~/.n8n"  # Default n8n directory on Pi

echo -e "${BLUE}🔧 Setting .env file on Raspberry Pi n8n${NC}"
echo "Host: ${PI_HOST}"
echo "n8n URL: http://192.168.1.226:5678"
echo ""

# Test SSH connection
echo -e "${BLUE}Testing SSH connection...${NC}"
if ! ssh -o ConnectTimeout=5 "${PI_HOST}" "echo 'Connected'" > /dev/null 2>&1; then
  echo -e "${RED}❌ Cannot connect to Raspberry Pi${NC}"
  echo ""
  echo "Please check:"
  echo "  1. Raspberry Pi is on and accessible"
  echo "  2. SSH is enabled on Pi"
  echo "  3. You can SSH manually: ssh ${PI_HOST}"
  exit 1
fi

echo -e "${GREEN}✅ Connected to Raspberry Pi${NC}"
echo ""

# Find n8n directory on Pi
echo -e "${BLUE}Finding n8n directory on Pi...${NC}"
N8N_DIR=$(ssh "${PI_HOST}" "if [ -d ~/.n8n ]; then echo ~/.n8n; elif [ -d ~/n8n ]; then echo ~/n8n; else echo 'not_found'; fi")

if [ "$N8N_DIR" = "not_found" ]; then
  echo -e "${YELLOW}⚠️  n8n directory not found in common locations${NC}"
  echo ""
  read -p "Enter n8n directory path on Pi (or press Enter to use ~/.n8n): " custom_dir
  N8N_DIR="${custom_dir:-~/.n8n}"
fi

echo -e "${GREEN}✅ Using n8n directory: ${N8N_DIR}${NC}"
echo ""

# Create .env file on Pi
echo -e "${BLUE}Creating .env file on Raspberry Pi...${NC}"

# Check if .env exists
ENV_EXISTS=$(ssh "${PI_HOST}" "if [ -f ${N8N_DIR}/.env ]; then echo 'yes'; else echo 'no'; fi")

if [ "$ENV_EXISTS" = "yes" ]; then
  echo -e "${YELLOW}⚠️  .env file already exists${NC}"
  read -p "Backup and overwrite? (y/n): " overwrite
  
  if [ "$overwrite" = "y" ] || [ "$overwrite" = "Y" ]; then
    ssh "${PI_HOST}" "cp ${N8N_DIR}/.env ${N8N_DIR}/.env.backup.\$(date +%Y%m%d_%H%M%S)"
    echo -e "${GREEN}✅ Backed up existing .env${NC}"
  fi
fi

# Create .env file with variables
ssh "${PI_HOST}" "cat > ${N8N_DIR}/.env << 'EOF'
# Unity Automation Environment Variables
# Set on $(date)
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# n8n cookie configuration
# Avoids the 'secure cookie' warning when accessing n8n over HTTP (common on LAN/Pi)
N8N_SECURE_COOKIE=false
EOF
"

if [ $? -eq 0 ]; then
  echo -e "${GREEN}✅ .env file created on Raspberry Pi${NC}"
else
  echo -e "${RED}❌ Failed to create .env file${NC}"
  exit 1
fi

echo ""

# Show what was created
echo -e "${BLUE}📋 Variables set on Pi:${NC}"
ssh "${PI_HOST}" "cat ${N8N_DIR}/.env"
echo ""

# Restart n8n on Pi
echo -e "${BLUE}Restarting n8n on Raspberry Pi...${NC}"
echo "Choose restart method:"
echo "  1) systemctl (if n8n is a service)"
echo "  2) PM2 (if using PM2)"
echo "  3) Manual (you'll restart it yourself)"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
  1)
    echo "Restarting via systemctl..."
    echo "Ensuring systemd service has N8N_SECURE_COOKIE=false..."
    ssh "${PI_HOST}" "sudo mkdir -p /etc/systemd/system/n8n.service.d && sudo bash -lc 'cat > /etc/systemd/system/n8n.service.d/override.conf << \"EOF\"\n[Service]\nEnvironment=\"N8N_SECURE_COOKIE=false\"\nEOF\n' && sudo systemctl daemon-reload" \
      && echo -e "${GREEN}✅ systemd override applied${NC}" \
      || echo -e "${YELLOW}⚠️  Could not apply systemd override (continuing)${NC}"
    ssh "${PI_HOST}" "sudo systemctl restart n8n" && echo -e "${GREEN}✅ n8n restarted${NC}"
    ;;
  2)
    echo "Restarting via PM2..."
    ssh "${PI_HOST}" "export N8N_SECURE_COOKIE=false && pm2 restart n8n --update-env" && echo -e "${GREEN}✅ n8n restarted${NC}"
    ;;
  3)
    echo -e "${YELLOW}⚠️  Manual restart required${NC}"
    echo ""
    echo "SSH into Pi and restart n8n:"
    echo "  ssh ${PI_HOST}"
    echo "  sudo systemctl restart n8n"
    echo "  # OR"
    echo "  pm2 restart n8n"
    ;;
  *)
    echo -e "${YELLOW}⚠️  Invalid choice - skipping restart${NC}"
    ;;
esac

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "📋 Next steps:"
echo "  1. Wait a few seconds for n8n to restart"
echo "  2. Test workflow at: http://192.168.1.226:5678"
echo "  3. Execute 'Get Git Variables' node"
echo "  4. Should show: repoUrlSet: true, projectPathSet: true"
echo ""

