#!/bin/bash
# Push Unity Workflow Update - After Successful Test
# Commits and pushes the workflow update to Unity 2021.3.45f2

echo "============================================================"
echo "  Push Unity Workflow Update"
echo "============================================================"

cd /Users/rashadwest/BTEBallCODE

# Check if there are changes to commit
if git diff --quiet .github/workflows/unity-webgl-build.yml; then
    echo "✅ No changes to commit - workflow already up to date"
    exit 0
fi

echo "📋 Changes to commit:"
git diff .github/workflows/unity-webgl-build.yml | grep -E "^\+|^\-" | head -10
echo ""

# Confirm before pushing
read -p "Commit and push workflow update? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 1
fi

# Add and commit
echo "📝 Committing workflow update..."
git add .github/workflows/unity-webgl-build.yml
git commit -m "Update Unity to 2021.3.45f2 and configure license for CI/CD

- Switch to Unity 2021.3.45f2 (secure LTS version)
- Configure UNITY_SERIAL for Personal license activation
- All secrets configured: UNITY_EMAIL, UNITY_PASSWORD, UNITY_SERIAL"

# Push
echo "📤 Pushing to repository..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Workflow update pushed successfully!"
    echo ""
    echo "📋 This will trigger a new build automatically"
    echo "   Monitor at: https://github.com/rashadwest/BTEBallCODE/actions"
    echo ""
else
    echo ""
    echo "❌ Push failed - check error message above"
    exit 1
fi


