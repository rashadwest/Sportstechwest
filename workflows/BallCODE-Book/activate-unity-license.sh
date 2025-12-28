#!/bin/bash
# Unity License Activation Script
# Replace YOUR-EMAIL and YOUR-PASSWORD before running!

UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity"
UNITY_EMAIL="rashadlwest@gmail.com"  # ← REPLACE THIS
UNITY_PASSWORD="$TWu#1ty365"         # ← REPLACE THIS

echo "🎮 Activating Unity License..."
echo ""

if [ ! -f "$UNITY_PATH" ]; then
    echo "❌ Unity Editor not found at: $UNITY_PATH"
    exit 1
fi

if [ "$UNITY_EMAIL" = "YOUR-EMAIL@example.com" ] || [ "$UNITY_PASSWORD" = "YOUR-PASSWORD" ]; then
    echo "❌ Please edit this script and replace YOUR-EMAIL and YOUR-PASSWORD!"
    echo ""
    echo "Open this file and edit:"
    echo "  $0"
    exit 1
fi

echo "✅ Unity Editor found"
echo "📧 Email: $UNITY_EMAIL"
echo "⏳ Activating license (this may take 10-30 seconds)..."
echo ""

"$UNITY_PATH" -quit -batchmode -serial -username "$UNITY_EMAIL" -password "$UNITY_PASSWORD"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ License activation completed!"
    echo "   Check Unity Hub → Licenses to verify"
else
    echo ""
    echo "❌ License activation failed"
    echo "   Check the error message above"
    exit 1
fi
