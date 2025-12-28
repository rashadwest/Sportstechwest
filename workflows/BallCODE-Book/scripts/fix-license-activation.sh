#!/bin/bash
# Fix License Activation - Ready to Push Solution #1
# Uses game-ci/unity-activate action

set -e

WORKFLOW_FILE=".github/workflows/unity-webgl-build.yml"
BACKUP_FILE="${WORKFLOW_FILE}.backup.$(date +%Y%m%d_%H%M%S)"

echo "🔧 Fixing license activation with game-ci/unity-activate..."

# Check if in correct directory
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Workflow file not found: $WORKFLOW_FILE"
    echo "   Run this script from the Unity project root"
    exit 1
fi

# Backup workflow
cp "$WORKFLOW_FILE" "$BACKUP_FILE"
echo "✅ Backup created: $BACKUP_FILE"

# Check if game-ci/unity-activate step already exists
if grep -q "game-ci/unity-activate" "$WORKFLOW_FILE"; then
    echo "⚠️  game-ci/unity-activate already in workflow"
    echo "   Skipping update"
    exit 0
fi

echo "📋 Updating workflow to use game-ci/unity-activate..."
echo ""
echo "⚠️  MANUAL STEP REQUIRED:"
echo "   1. Open: $WORKFLOW_FILE"
echo "   2. Find: 'Activate Unity License' step"
echo "   3. Replace with:"
echo ""
echo "   - name: Activate Unity License"
echo "     uses: game-ci/unity-activate@v1"
echo "     with:"
echo "       unityEmail: \${{ secrets.UNITY_EMAIL }}"
echo "       unityPassword: \${{ secrets.UNITY_PASSWORD }}"
echo "       unityLicense: \${{ secrets.UNITY_LICENSE || '' }}"
echo "       unitySerial: \${{ secrets.UNITY_SERIAL || '' }}"
echo ""
echo "   4. Save and commit"
echo "   5. Push to trigger build"
echo ""
echo "✅ Backup saved. Ready to update workflow manually."

