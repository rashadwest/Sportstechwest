#!/bin/bash
# Launch Automation Master Script
# Automates as much as possible for tomorrow's launch
#
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

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Launch Automation Master Script${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Add Contact Information
echo -e "${YELLOW}Step 1: Adding Contact Information...${NC}"
cd "$PROJECT_ROOT"
python3 scripts/automate-website-phase1-updates.py
echo ""

# Step 2: Test All Webhooks
echo -e "${YELLOW}Step 2: Testing All Webhooks...${NC}"
bash scripts/test-all-webhooks.sh
echo ""

# Step 3: Update Dashboard
echo -e "${YELLOW}Step 3: Updating Dashboard...${NC}"
python3 scripts/update-dashboard.py
echo ""

# Step 4: Generate Launch Prep Materials
echo -e "${YELLOW}Step 4: Generating Launch Prep Materials...${NC}"
python3 scripts/generate-launch-prep-materials.py
echo ""

# Step 5: Run Integration Flow Tests
echo -e "${YELLOW}Step 5: Testing Integration Flow...${NC}"
python3 scripts/test-integration-flow.py
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Launch Automation Complete!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${YELLOW}📋 Next Steps (Manual):${NC}"
echo "  1. Generate visual assets (2-3 hours) - Use prompts in documents/visual-assets/"
echo "  2. Add visuals to Book 1 page (30 min)"
echo "  3. Test complete user journey manually"
echo "  4. Review launch prep materials"
echo "  5. Deploy website changes"
echo ""

