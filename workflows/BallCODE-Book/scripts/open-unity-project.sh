#!/bin/bash
# Open Unity Project in Unity Editor
# Correct way to open Unity project (not just Finder)

UNITY_PROJECT="/Users/rashadwest/BTEBallCODE"
UNITY_EDITOR="/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity"

echo "🎮 Opening Unity project in Unity Editor..."
echo "   Project: $UNITY_PROJECT"
echo ""

# Method 1: Try Unity Hub first (if available)
if [ -d "/Applications/Unity Hub.app" ]; then
    echo "📦 Opening via Unity Hub..."
    open -a "Unity Hub" "$UNITY_PROJECT"
    echo "✅ Unity Hub should open - select the project from the list"
    exit 0
fi

# Method 2: Direct Unity Editor
if [ -f "$UNITY_EDITOR" ]; then
    echo "🚀 Opening directly in Unity Editor..."
    "$UNITY_EDITOR" -projectPath "$UNITY_PROJECT" &
    echo "✅ Unity Editor is starting..."
    echo "   (This may take 30-60 seconds to load)"
    exit 0
fi

# Method 3: Find any Unity Editor
UNITY_EDITORS=$(find /Applications -name "Unity" -type f 2>/dev/null | head -1)
if [ -n "$UNITY_EDITORS" ]; then
    echo "🔍 Found Unity Editor: $UNITY_EDITORS"
    "$UNITY_EDITORS" -projectPath "$UNITY_PROJECT" &
    echo "✅ Unity Editor is starting..."
    exit 0
fi

echo "❌ Unity Editor not found!"
echo ""
echo "Please:"
echo "1. Install Unity Hub from: https://unity.com/download"
echo "2. Or install Unity Editor directly"
echo "3. Then run this script again"

exit 1


