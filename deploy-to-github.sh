#!/bin/bash

# BallCODE Website Deployment System
# Copyright © 2025 Rashad West. All Rights Reserved.
#
# This script performs a complete end-to-end deployment test and push
# to GitHub, including all images and content.

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_PATH="/Users/rashadwest/Sportstechwest"
REPORT_FILE="$REPO_PATH/deployment-report-$(date +%Y%m%d-%H%M%S).md"
LOG_FILE="$REPO_PATH/deployment-log-$(date +%Y%m%d-%H%M%S).txt"

# Initialize report
echo "# Deployment Report - $(date)" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Copyright © 2025 Rashad West. All Rights Reserved.**" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Log function
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
    echo "- $1" >> "$REPORT_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
    echo "❌ **ERROR:** $1" >> "$REPORT_FILE"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$LOG_FILE"
    echo "✅ **SUCCESS:** $1" >> "$REPORT_FILE"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
    echo "⚠️ **WARNING:** $1" >> "$REPORT_FILE"
}

# Step 1: Navigate to repository
log "Step 1: Navigating to repository directory..."
cd "$REPO_PATH" || { error "Failed to navigate to $REPO_PATH"; exit 1; }
success "Repository directory found"

# Step 2: Check git status
log "Step 2: Checking git status..."
if ! git status &>/dev/null; then
    error "Not a git repository or git not initialized"
    exit 1
fi
success "Git repository detected"

# Step 3: Check for uncommitted changes
log "Step 3: Checking for uncommitted changes..."
CHANGED_FILES=$(git status --short | wc -l | tr -d ' ')
if [ "$CHANGED_FILES" -eq 0 ]; then
    warning "No changes detected. Repository is up to date."
    echo "✅ **STATUS:** No changes to deploy" >> "$REPORT_FILE"
    exit 0
fi
success "Found $CHANGED_FILES files with changes"

# Step 4: Count images
log "Step 4: Counting images to be deployed..."
IMAGE_COUNT=$(find assets/images/blog-img -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" \) 2>/dev/null | wc -l | tr -d ' ')
log "Found $IMAGE_COUNT images in assets/images/blog-img"

# Step 5: Count blog posts
log "Step 5: Counting blog posts..."
POST_COUNT=$(find _posts -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
log "Found $POST_COUNT blog posts in _posts"

# Step 6: Check remote connection
log "Step 6: Checking remote repository connection..."
if ! git remote get-url origin &>/dev/null; then
    error "No remote 'origin' configured"
    exit 1
fi
REMOTE_URL=$(git remote get-url origin)
success "Remote configured: $REMOTE_URL"

# Step 7: Add all changes (including images)
log "Step 7: Staging all changes (including images)..."
git add -A
STAGED_FILES=$(git diff --cached --name-only | wc -l | tr -d ' ')
success "Staged $STAGED_FILES files for commit"

# List staged files by category
echo "" >> "$REPORT_FILE"
echo "## Files Staged for Deployment" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

BLOG_POSTS=$(git diff --cached --name-only | grep "^_posts/" | wc -l | tr -d ' ')
IMAGES=$(git diff --cached --name-only | grep "^assets/images/" | wc -l | tr -d ' ')
OTHER=$(git diff --cached --name-only | grep -v "^_posts/" | grep -v "^assets/images/" | wc -l | tr -d ' ')

echo "- **Blog Posts:** $BLOG_POSTS files" >> "$REPORT_FILE"
echo "- **Images:** $IMAGES files" >> "$REPORT_FILE"
echo "- **Other Files:** $OTHER files" >> "$REPORT_FILE"
echo "- **Total:** $STAGED_FILES files" >> "$REPORT_FILE"

# Step 8: Create commit
log "Step 8: Creating commit..."
COMMIT_MESSAGE="Deploy website updates: $(date +'%Y-%m-%d %H:%M:%S') - $BLOG_POSTS posts, $IMAGES images"
if git commit -m "$COMMIT_MESSAGE"; then
    success "Commit created successfully"
    echo "**Commit Message:** $COMMIT_MESSAGE" >> "$REPORT_FILE"
else
    error "Failed to create commit"
    exit 1
fi

# Step 9: Get commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)
log "Commit hash: $COMMIT_HASH"
echo "**Commit Hash:** $COMMIT_HASH" >> "$REPORT_FILE"

# Step 10: Push to GitHub
log "Step 10: Pushing to GitHub..."
echo "" >> "$REPORT_FILE"
echo "## Push Results" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
    success "Successfully pushed to GitHub"
    echo "✅ **Status:** Successfully pushed to origin/main" >> "$REPORT_FILE"
    echo "✅ **Commit:** $COMMIT_HASH" >> "$REPORT_FILE"
else
    error "Failed to push to GitHub"
    echo "❌ **Status:** Push failed. Check logs for details." >> "$REPORT_FILE"
    exit 1
fi

# Step 11: Verify push
log "Step 11: Verifying push..."
sleep 2
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git ls-remote origin main | cut -f1)

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
    success "Push verified: Local and remote commits match"
    echo "✅ **Verification:** Local and remote commits match" >> "$REPORT_FILE"
else
    warning "Push verification: Commits don't match (may need to wait for sync)"
    echo "⚠️ **Verification:** Commits may not be synced yet" >> "$REPORT_FILE"
fi

# Step 12: Generate summary
echo "" >> "$REPORT_FILE"
echo "## Deployment Summary" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Date:** $(date)" >> "$REPORT_FILE"
echo "**Repository:** $REMOTE_URL" >> "$REPORT_FILE"
echo "**Branch:** main" >> "$REPORT_FILE"
echo "**Commit:** $COMMIT_HASH" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Files Deployed:**" >> "$REPORT_FILE"
echo "- Blog Posts: $BLOG_POSTS" >> "$REPORT_FILE"
echo "- Images: $IMAGES" >> "$REPORT_FILE"
echo "- Other Files: $OTHER" >> "$REPORT_FILE"
echo "- Total: $STAGED_FILES" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Status:** ✅ Deployment Complete" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**Next Steps:**" >> "$REPORT_FILE"
echo "1. Wait 2-5 minutes for GitHub Pages to rebuild" >> "$REPORT_FILE"
echo "2. Check https://sportstechwest.com/blogs" >> "$REPORT_FILE"
echo "3. Hard refresh (Cmd+Shift+R) to see changes" >> "$REPORT_FILE"

# Final success message
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ DEPLOYMENT COMPLETE${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Report saved to: $REPORT_FILE"
echo "Log saved to: $LOG_FILE"
echo ""
echo "Files deployed:"
echo "  - Blog Posts: $BLOG_POSTS"
echo "  - Images: $IMAGES"
echo "  - Other: $OTHER"
echo "  - Total: $STAGED_FILES"
echo ""
echo "Commit: $COMMIT_HASH"
echo ""
echo "Next: Wait 2-5 minutes, then check https://sportstechwest.com/blogs"


