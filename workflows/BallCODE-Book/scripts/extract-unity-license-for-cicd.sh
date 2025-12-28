#!/bin/bash
# AIMCODE: Extract Unity License File for CI/CD
# End-to-end solution for Unity Personal license activation

echo "============================================================"
echo "  AIMCODE: Extract Unity License for CI/CD"
echo "============================================================"

# Find license file
LICENSE_FILE="/Library/Application Support/Unity/Unity_lic.ulf"
OUTPUT_FILE="/tmp/unity-license-for-cicd.txt"

if [ ! -f "$LICENSE_FILE" ]; then
    echo "❌ License file not found at: $LICENSE_FILE"
    exit 1
fi

echo "✅ Found license file: $LICENSE_FILE"
echo ""

# Extract full content
echo "📝 Extracting license file content..."
cat "$LICENSE_FILE" > "$OUTPUT_FILE"

# Get file info
FILE_SIZE=$(wc -c < "$OUTPUT_FILE")
FILE_LINES=$(wc -l < "$OUTPUT_FILE")

echo "✅ License file extracted:"
echo "   Size: $FILE_SIZE bytes"
echo "   Lines: $FILE_LINES"
echo "   Location: $OUTPUT_FILE"
echo ""

# Display first few lines (for verification)
echo "📋 First 10 lines (for verification):"
head -10 "$OUTPUT_FILE"
echo ""
echo "---"
echo ""

# Instructions
echo "📋 NEXT STEPS:"
echo ""
echo "1. Copy the license file content:"
echo "   cat $OUTPUT_FILE | pbcopy"
echo "   OR"
echo "   Open: $OUTPUT_FILE"
echo "   Select All → Copy"
echo ""
echo "2. Add to GitHub Secrets:"
echo "   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions"
echo "   - Click: 'New repository secret' (or edit existing UNITY_LICENSE)"
echo "   - Name: UNITY_LICENSE"
echo "   - Value: Paste entire license file content"
echo "   - Click: 'Add secret'"
echo ""
echo "3. Test build:"
echo "   - Trigger GitHub Actions build"
echo "   - Should work with full license file content"
echo ""
echo "✅ License file ready for CI/CD!"
echo ""


