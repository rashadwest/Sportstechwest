#!/bin/bash
# Emergency Local Build and Deploy
# Ready to Push Solution #3
# Builds locally and deploys to Netlify

set -e

UNITY_PROJECT="/Users/rashadwest/BTEBallCODE"
UNITY_VERSION="2021.3.15f1"
UNITY_PATH="/Applications/Unity/Hub/Editor/${UNITY_VERSION}/Unity.app/Contents/MacOS/Unity"
BUILD_PATH="${UNITY_PROJECT}/Builds/WebGL"

echo "🚨 Emergency Local Build and Deploy"
echo ""

# Check Unity installation
if [ ! -f "$UNITY_PATH" ]; then
    echo "❌ Unity not found at: $UNITY_PATH"
    echo "   Please check Unity installation"
    exit 1
fi

# Check project directory
if [ ! -d "$UNITY_PROJECT" ]; then
    echo "❌ Unity project not found at: $UNITY_PROJECT"
    exit 1
fi

cd "$UNITY_PROJECT"

echo "🔨 Building Unity WebGL..."
"$UNITY_PATH" \
  -batchmode \
  -quit \
  -projectPath "$UNITY_PROJECT" \
  -buildTarget WebGL \
  -buildPath "$BUILD_PATH" \
  -logFile build.log

if [ $? -ne 0 ]; then
    echo "❌ Unity build failed"
    echo "📋 Check build.log for errors"
    exit 1
fi

# Verify build output
if [ ! -d "$BUILD_PATH" ] || [ ! -f "$BUILD_PATH/index.html" ]; then
    echo "❌ Build output not found or invalid"
    exit 1
fi

echo "✅ Build complete: $BUILD_PATH"
BUILD_SIZE=$(du -sh "$BUILD_PATH" | cut -f1)
echo "📦 Build size: $BUILD_SIZE"

# Deploy to Netlify
echo ""
echo "🚀 Deploying to Netlify..."

if command -v netlify &> /dev/null; then
    netlify deploy --prod --dir="$BUILD_PATH"
    echo "✅ Deployment complete!"
    echo "🌐 Game should be live at: https://ballcode.netlify.app"
else
    echo "⚠️  Netlify CLI not installed"
    echo "   Install: npm install -g netlify-cli"
    echo "   Or deploy manually via Netlify dashboard"
fi

echo ""
echo "✅ Emergency build and deployment complete!"

