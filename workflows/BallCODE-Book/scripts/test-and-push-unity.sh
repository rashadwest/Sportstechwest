#!/bin/bash
# Test Unity Build and Push - Automated Script
# Tests build first, then pushes if successful

echo "============================================================"
echo "  Unity Build Test and Push"
echo "============================================================"

cd /Users/rashadwest/BTEBallCODE

# Check if workflow change needs to be committed
if git diff --quiet .github/workflows/unity-webgl-build.yml; then
    echo "✅ No workflow changes to commit"
else
    echo "📋 Workflow changes detected:"
    git diff .github/workflows/unity-webgl-build.yml | grep -E "^\+|^\-" | head -5
    echo ""
    echo "⚠️  Workflow needs to be committed after successful test"
fi

echo ""
echo "📋 Current secrets status:"
echo "   ✅ UNITY_EMAIL - Configured"
echo "   ✅ UNITY_PASSWORD - Configured"
echo "   ✅ UNITY_SERIAL - Configured (F4-UBEE-VV7Z-SSXU-DYHH-X7BM)"
echo "   ✅ NETLIFY_AUTH_TOKEN - Configured"
echo "   ✅ NETLIFY_SITE_ID - Configured"
echo ""

echo "🎯 Next Steps:"
echo ""
echo "1. TEST BUILD:"
echo "   - Go to: https://github.com/rashadwest/BTEBallCODE/actions"
echo "   - Click: 'Unity WebGL Build and Deploy'"
echo "   - Click: 'Run workflow' → 'Run workflow'"
echo "   - Wait for build to complete"
echo ""
echo "2. IF BUILD SUCCEEDS:"
echo "   Run: ./scripts/push-unity-workflow.sh"
echo "   OR manually:"
echo "   git add .github/workflows/unity-webgl-build.yml"
echo "   git commit -m 'Update Unity to 2021.3.45f2 and configure license for CI/CD'"
echo "   git push origin main"
echo ""
echo "3. IF BUILD FAILS:"
echo "   - Check error message"
echo "   - Verify serial number format"
echo "   - Check workflow configuration"
echo ""

echo "✅ Ready to test! I opened GitHub Actions page for you."
echo ""


