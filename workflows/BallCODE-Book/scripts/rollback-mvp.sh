#!/bin/bash
# MVP Rollback Script
# Safely rollback MVP push to pre-MVP state

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║          MVP ROLLBACK SCRIPT - USE WITH CAUTION           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Get current date for tagging
DATE_TAG=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Find pre-MVP tag
PRE_MVP_TAG=$(git tag -l "v-pre-mvp-*" | sort -r | head -1)

if [ -z "$PRE_MVP_TAG" ]; then
    echo "❌ ERROR: No pre-MVP tag found!"
    echo "   Looking for tags matching: v-pre-mvp-*"
    echo ""
    echo "Available tags:"
    git tag -l | head -10
    exit 1
fi

echo "📋 Rollback Information:"
echo "   Pre-MVP Tag: $PRE_MVP_TAG"
echo "   Current Branch: $(git branch --show-current)"
echo "   Current Commit: $(git rev-parse --short HEAD)"
echo ""

# Confirm rollback
read -p "⚠️  Are you sure you want to rollback to $PRE_MVP_TAG? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Rollback cancelled."
    exit 0
fi

echo ""
echo "🔄 Starting rollback process..."
echo ""

# Create rollback branch
ROLLBACK_BRANCH="rollback-$TIMESTAMP"
echo "1️⃣  Creating rollback branch: $ROLLBACK_BRANCH"
git checkout -b "$ROLLBACK_BRANCH" "$PRE_MVP_TAG"

echo ""
echo "2️⃣  Rollback branch created successfully!"
echo ""
echo "📋 Next Steps:"
echo "   1. Review the rollback branch:"
echo "      git log --oneline -10"
echo ""
echo "   2. Test the rollback branch locally"
echo ""
echo "   3. If satisfied, merge to main:"
echo "      git checkout main"
echo "      git merge $ROLLBACK_BRANCH"
echo "      git push origin main"
echo ""
echo "   4. Or push rollback branch for review:"
echo "      git push origin $ROLLBACK_BRANCH"
echo ""
echo "✅ Rollback branch created: $ROLLBACK_BRANCH"
echo "   Current state: Pre-MVP checkpoint ($PRE_MVP_TAG)"
echo ""

