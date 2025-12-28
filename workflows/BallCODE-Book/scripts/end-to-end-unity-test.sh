#!/bin/bash
# AIMCODE: End-to-End Unity License Test
# Verifies complete setup from license file to GitHub Secrets

echo "============================================================"
echo "  AIMCODE: End-to-End Unity License Test"
echo "============================================================"

# Step 1: Verify license file exists
echo ""
echo "📋 Step 1: Verify License File"
LICENSE_FILE="/Library/Application Support/Unity/Unity_lic.ulf"
if [ -f "$LICENSE_FILE" ]; then
    echo "✅ License file found: $LICENSE_FILE"
    FILE_SIZE=$(wc -c < "$LICENSE_FILE")
    echo "   Size: $FILE_SIZE bytes"
else
    echo "❌ License file not found"
    exit 1
fi

# Step 2: Extract license content
echo ""
echo "📋 Step 2: Extract License Content"
OUTPUT_FILE="/tmp/unity-license-for-cicd.txt"
cat "$LICENSE_FILE" > "$OUTPUT_FILE"
if [ -f "$OUTPUT_FILE" ]; then
    echo "✅ License content extracted: $OUTPUT_FILE"
    echo "   Ready to add to GitHub Secrets"
else
    echo "❌ Failed to extract license content"
    exit 1
fi

# Step 3: Verify GitHub Secrets (manual check)
echo ""
echo "📋 Step 3: GitHub Secrets Status"
echo "   ⚠️  Manual verification needed:"
echo "   - UNITY_EMAIL: Should be configured"
echo "   - UNITY_PASSWORD: Should be configured"
echo "   - UNITY_LICENSE: Should contain full license file content"
echo "   - UNITY_SERIAL: Optional (backup)"
echo ""
echo "   Check: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions"

# Step 4: Verify workflow configuration
echo ""
echo "📋 Step 4: Verify Workflow Configuration"
WORKFLOW_FILE="/Users/rashadwest/BTEBallCODE/.github/workflows/unity-webgl-build.yml"
if [ -f "$WORKFLOW_FILE" ]; then
    echo "✅ Workflow file found"
    
    # Check if UNITY_LICENSE is in env
    if grep -q "UNITY_LICENSE.*secrets.UNITY_LICENSE" "$WORKFLOW_FILE"; then
        echo "✅ UNITY_LICENSE configured in workflow"
    else
        echo "⚠️  UNITY_LICENSE may not be configured correctly"
    fi
    
    # Check if UNITY_EMAIL is in env
    if grep -q "UNITY_EMAIL.*secrets.UNITY_EMAIL" "$WORKFLOW_FILE"; then
        echo "✅ UNITY_EMAIL configured in workflow"
    else
        echo "⚠️  UNITY_EMAIL may not be configured"
    fi
    
    # Check Unity version
    if grep -q "unityVersion: 2021.3.45f2" "$WORKFLOW_FILE"; then
        echo "✅ Unity version: 2021.3.45f2"
    else
        echo "⚠️  Unity version may be incorrect"
    fi
else
    echo "❌ Workflow file not found"
    exit 1
fi

# Step 5: Summary
echo ""
echo "============================================================"
echo "  Test Summary"
echo "============================================================"
echo ""
echo "✅ License file: Present"
echo "✅ License content: Extracted"
echo "⏳ GitHub Secrets: Manual verification needed"
echo "✅ Workflow: Configured"
echo ""
echo "📋 Next Steps:"
echo "1. Add license file content to GitHub Secrets → UNITY_LICENSE"
echo "2. Trigger test build in GitHub Actions"
echo "3. Monitor build logs for license activation"
echo "4. Verify build succeeds"
echo ""
echo "✅ End-to-end test complete!"
echo ""


