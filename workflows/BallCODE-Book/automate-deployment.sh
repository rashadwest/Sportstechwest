#!/bin/bash

# Automated Deployment Script
# Commits and pushes changes to GitHub, triggers auto-deployment

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="$SCRIPT_DIR/BallCode"
DEPLOY_REMOTE="${BALLCODE_DEPLOY_REMOTE:-origin}"

echo -e "${BLUE}=== Automated Deployment ===${NC}\n"

cd "$WEBSITE_DIR"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo -e "${RED}Error: Git not initialized${NC}"
    echo "Initialize git first: git init"
    exit 1
fi

# Check for changes
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo -e "${BLUE}No changes to deploy${NC}"
    exit 0
fi

# Show status
echo -e "${BLUE}Changes detected:${NC}"
git status --short
echo ""

# Stage all changes
echo -e "${BLUE}Staging changes...${NC}"
git add -A

# Get commit message
COMMIT_MSG=${1:-"Update website: $(date +'%Y-%m-%d %H:%M:%S')"}

# Commit
echo -e "${BLUE}Committing changes...${NC}"
git commit -m "$COMMIT_MSG"

# Check remote
if ! git remote | grep -q "^${DEPLOY_REMOTE}$"; then
    echo -e "${YELLOW}⚠${NC} No remote '${DEPLOY_REMOTE}' configured"
    echo "Add remote: git remote add ${DEPLOY_REMOTE} <your-repo-url>"
    exit 0
fi

# Push
echo -e "${BLUE}Pushing to GitHub...${NC}"
REMOTE_URL="$(git remote get-url "$DEPLOY_REMOTE" 2>/dev/null || echo "")"
if echo "$REMOTE_URL" | grep -q "CourtXLabs/BallCODE-Website"; then
    echo -e "${RED}Error: remote '${DEPLOY_REMOTE}' points to CourtXLabs/BallCODE-Website (known broken/404).${NC}"
    echo "Fix: git remote set-url ${DEPLOY_REMOTE} https://github.com/JuddCMelvin/BallCode.git (or your correct repo)"
    exit 1
fi

if git push "$DEPLOY_REMOTE" main 2>&1; then
    echo -e "${GREEN}✓${NC} Successfully pushed to GitHub"
    echo ""
    echo -e "${BLUE}Deployment Status:${NC}"
    echo "  - Changes committed: ✓"
    echo "  - Pushed to GitHub: ✓"
    echo "  - Auto-deploy: Check your hosting platform (Netlify/Vercel/etc.)"
    echo ""
    echo -e "${BLUE}Next:${NC} Verify deployment on live site"
else
    echo -e "${RED}Error: Failed to push${NC}"
    echo "Check your git credentials and permissions"
    exit 1
fi


