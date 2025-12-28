#!/bin/bash
# Create Pre-MVP Checkpoint
# Creates a safety checkpoint before MVP push

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║        CREATE PRE-MVP CHECKPOINT (SAFETY TAG)             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Get current date for tagging
DATE_TAG=$(date +%Y%m%d)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TAG_NAME="v-pre-mvp-$DATE_TAG"

# Check if tag already exists
if git rev-parse "$TAG_NAME" >/dev/null 2>&1; then
    echo "⚠️  Tag $TAG_NAME already exists!"
    read -p "   Create new tag with timestamp? (yes/no): " CREATE_NEW
    if [ "$CREATE_NEW" = "yes" ]; then
        TAG_NAME="v-pre-mvp-$TIMESTAMP"
    else
        echo "❌ Checkpoint creation cancelled."
        exit 0
    fi
fi

# Get current branch and commit
CURRENT_BRANCH=$(git branch --show-current)
CURRENT_COMMIT=$(git rev-parse --short HEAD)
CURRENT_COMMIT_FULL=$(git rev-parse HEAD)

echo "📋 Checkpoint Information:"
echo "   Tag Name: $TAG_NAME"
echo "   Current Branch: $CURRENT_BRANCH"
echo "   Current Commit: $CURRENT_COMMIT"
echo "   Commit Message: $(git log -1 --pretty=%B)"
echo ""

# Confirm checkpoint creation
read -p "✅ Create checkpoint tag $TAG_NAME? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Checkpoint creation cancelled."
    exit 0
fi

echo ""
echo "🔄 Creating checkpoint..."
echo ""

# Create annotated tag
git tag -a "$TAG_NAME" -m "Pre-MVP checkpoint - Safe to revert to

Created: $(date)
Branch: $CURRENT_BRANCH
Commit: $CURRENT_COMMIT
Commit Message: $(git log -1 --pretty=%B)

This tag marks a safe checkpoint before MVP push.
Use rollback-mvp.sh to return to this state if needed."

# Push tag to remote
echo "📤 Pushing tag to remote..."
git push origin "$TAG_NAME"

echo ""
echo "✅ Checkpoint created successfully!"
echo ""
echo "📋 Checkpoint Details:"
echo "   Tag: $TAG_NAME"
echo "   Commit: $CURRENT_COMMIT"
echo "   Branch: $CURRENT_BRANCH"
echo ""
echo "💡 To return to this checkpoint:"
echo "   git checkout $TAG_NAME"
echo "   OR"
echo "   ./scripts/rollback-mvp.sh"
echo ""


