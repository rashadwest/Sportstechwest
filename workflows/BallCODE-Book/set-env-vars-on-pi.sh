#!/bin/bash

# Set n8n Environment Variables on Raspberry Pi via SSH
# One-command solution

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

PI_HOST="pi@192.168.1.226"
SCRIPT_NAME="robot-set-n8n-env-vars.py"

echo -e "${BLUE}🚀 Setting n8n Environment Variables on Raspberry Pi${NC}"
echo "Host: ${PI_HOST}"
echo ""

# Check if script exists locally
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="${SCRIPT_DIR}/${SCRIPT_NAME}"

if [ ! -f "$SCRIPT_PATH" ]; then
  echo -e "${RED}❌ Script not found: ${SCRIPT_PATH}${NC}"
  exit 1
fi

echo -e "${BLUE}Step 1: Copying script to Raspberry Pi...${NC}"
scp "$SCRIPT_PATH" "${PI_HOST}:~/" || {
  echo -e "${RED}❌ Failed to copy script${NC}"
  echo "Make sure you can SSH into the Pi:"
  echo "  ssh ${PI_HOST}"
  echo ""
  echo -e "${YELLOW}⚡ FASTEST FIX (run these commands ON THE PI):${NC}"
  echo ""
  echo "Option A) systemd (most common):"
  echo "  sudo mkdir -p /etc/systemd/system/n8n.service.d"
  echo "  sudo tee /etc/systemd/system/n8n.service.d/override.conf >/dev/null <<'EOF'"
  echo "  [Service]"
  echo "  Environment=\"N8N_SECURE_COOKIE=false\""
  echo "  EOF"
  echo "  sudo systemctl daemon-reload"
  echo "  sudo systemctl restart n8n"
  echo ""
  echo "Option B) PM2:"
  echo "  export N8N_SECURE_COOKIE=false"
  echo "  pm2 restart n8n --update-env"
  exit 1
}
echo -e "${GREEN}✅ Script copied${NC}"
echo ""

echo -e "${BLUE}Step 2: Running script on Raspberry Pi...${NC}"
ssh "${PI_HOST}" "python3 ~/${SCRIPT_NAME}" || {
  echo -e "${RED}❌ Failed to run script${NC}"
  exit 1
}
echo ""

echo -e "${BLUE}Step 2.5: Ensuring N8N_SECURE_COOKIE=false on Pi...${NC}"
# Put it in ~/.n8n/.env (common) and keep it consistent even if file already exists
ssh "${PI_HOST}" "mkdir -p ~/.n8n && touch ~/.n8n/.env && (grep -q '^N8N_SECURE_COOKIE=' ~/.n8n/.env && sed -i.bak 's/^N8N_SECURE_COOKIE=.*/N8N_SECURE_COOKIE=false/' ~/.n8n/.env) || echo 'N8N_SECURE_COOKIE=false' >> ~/.n8n/.env" \
  && echo -e "${GREEN}✅ N8N_SECURE_COOKIE set in ~/.n8n/.env${NC}" \
  || echo -e "${YELLOW}⚠️  Could not update ~/.n8n/.env (continuing)${NC}"
echo ""

echo -e "${BLUE}Step 3: Restarting n8n...${NC}"
echo "Choose restart method:"
echo "  1) systemctl (if n8n is a service)"
echo "  2) PM2 (if using PM2)"
echo "  3) Skip (restart manually)"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
  1)
    echo "Ensuring systemd service has N8N_SECURE_COOKIE=false..."
    ssh "${PI_HOST}" "sudo mkdir -p /etc/systemd/system/n8n.service.d && sudo bash -lc 'cat > /etc/systemd/system/n8n.service.d/override.conf << \"EOF\"\n[Service]\nEnvironment=\"N8N_SECURE_COOKIE=false\"\nEOF\n' && sudo systemctl daemon-reload" \
      && echo -e "${GREEN}✅ systemd override applied${NC}" \
      || echo -e "${YELLOW}⚠️  Could not apply systemd override (continuing)${NC}"
    ssh "${PI_HOST}" "sudo systemctl restart n8n" && echo -e "${GREEN}✅ n8n restarted${NC}"
    ;;
  2)
    ssh "${PI_HOST}" "export N8N_SECURE_COOKIE=false && pm2 restart n8n --update-env" && echo -e "${GREEN}✅ n8n restarted${NC}"
    ;;
  3)
    echo -e "${YELLOW}⚠️  Skipping restart - restart manually:${NC}"
    echo "  ssh ${PI_HOST}"
    echo "  sudo systemctl restart n8n"
    ;;
  *)
    echo -e "${YELLOW}⚠️  Invalid choice - skipping restart${NC}"
    ;;
esac

echo ""
echo -e "${GREEN}✅ Done!${NC}"
echo ""
echo "Variables set:"
echo "  ✅ UNITY_REPO_URL = https://github.com/rashadwest/BallCode.git"
echo "  ✅ UNITY_PROJECT_PATH = /Users/rashadwest/BTEBallCODE"
echo "  ✅ WORKFLOW_PATH = /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
echo ""
echo "Test your workflow now!"

