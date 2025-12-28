#!/bin/bash
# Create Unity 2021.3.45f2 activation file

echo "============================================================"
echo "  Create Unity 2021.3.45f2 Activation File"
echo "============================================================"

UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"
OUTPUT_DIR="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"

if [ ! -f "$UNITY_PATH" ]; then
    echo "❌ Unity 2021.3.45f2 not found at: $UNITY_PATH"
    echo "   Please install it in Unity Hub first"
    exit 1
fi

echo "✅ Found Unity 2021.3.45f2"
echo "📝 Creating activation file..."

cd "$OUTPUT_DIR"

"$UNITY_PATH" -quit -batchmode -createManualActivationFile

if [ -f "Unity_v2021.3.45f2.alf" ]; then
    echo "✅ Activation file created: Unity_v2021.3.45f2.alf"
    echo "📁 Location: $OUTPUT_DIR/Unity_v2021.3.45f2.alf"
    echo ""
    echo "Next steps:"
    echo "1. Upload this file to: https://license.unity3d.com/"
    echo "2. Get license file or serial number"
    echo "3. Add to GitHub Secrets"
else
    echo "❌ Activation file not created"
    echo "   Try opening Unity Editor manually and use Help → Manage License"
    exit 1
fi
