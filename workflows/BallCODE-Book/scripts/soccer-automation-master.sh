#!/bin/bash
# Soccer Automation Master Script
# Runs all soccer automation tasks in sequence

set -e  # Exit on error

echo "⚽ Soccer Version - Automation Master Script"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}Step 1: Creating Soccer Route Structure...${NC}"
python3 create-soccer-routes.py
echo ""

echo -e "${BLUE}Step 2: Adapting Basketball Content to Soccer...${NC}"
python3 adapt-basketball-to-soccer.py
echo ""

echo -e "${BLUE}Step 3: Generating Soccer Book Pages...${NC}"
python3 generate-soccer-book-pages.py
echo ""

echo -e "${GREEN}✅ All automation tasks completed!${NC}"
echo ""
echo "Next steps:"
echo "1. Review generated content"
echo "2. Customize as needed"
echo "3. Deploy to ballcode.co"

