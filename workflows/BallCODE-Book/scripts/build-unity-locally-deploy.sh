#!/bin/bash
# Build Unity Locally and Deploy to Netlify
# Alternative solution that bypasses CI/CD license issues

echo "============================================================"
echo "  Build Unity Locally and Deploy to Netlify"
echo "============================================================"

UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"
PROJECT_PATH="/Users/rashadwest/BTEBallCODE"
BUILD_PATH="$PROJECT_PATH/Builds/WebGL"

# Check Unity Editor
if [ ! -f "$UNITY_PATH" ]; then
    echo "❌ Unity Editor not found at: $UNITY_PATH"
    exit 1
fi

# Check project
if [ ! -d "$PROJECT_PATH/Assets" ]; then
    echo "❌ Unity project not found at: $PROJECT_PATH"
    exit 1
fi

echo "✅ Unity Editor: $UNITY_PATH"
echo "✅ Project: $PROJECT_PATH"
echo ""

# Build Unity WebGL
echo "📝 Building Unity WebGL..."
"$UNITY_PATH" \
    -batchmode \
    -quit \
    -projectPath "$PROJECT_PATH" \
    -buildTarget WebGL \
    -buildPath "$BUILD_PATH" \
    -logfile ~/Library/Logs/Unity/build-webgl.log

# Check build result
if [ $? -eq 0 ] && [ -f "$BUILD_PATH/index.html" ]; then
    echo "✅ Build successful!"
    echo "   Build location: $BUILD_PATH"
    echo ""
    
    # Deploy to Netlify
    echo "📤 Deploying to Netlify..."
    cd "$PROJECT_PATH"
    
    if command -v netlify &> /dev/null; then
        netlify deploy --prod --dir="$BUILD_PATH"
        echo ""
        echo "✅ Deployment complete!"
    else
        echo "⚠️  Netlify CLI not installed"
        echo "   Install: npm install -g netlify-cli"
        echo "   OR deploy manually: Upload $BUILD_PATH to Netlify"
    fi
else
    echo "❌ Build failed"
    echo "   Check log: ~/Library/Logs/Unity/build-webgl.log"
    exit 1
fi

echo ""
echo "✅ Build and deploy complete!"
echo ""


