#!/bin/bash
# Unity License Setup - Quick Commands
# Run these commands one by one

echo "=========================================="
echo "Unity License Setup - Step by Step"
echo "=========================================="
echo ""

echo "STEP 1: Open activation file location"
echo "File: Unity_v2021.3.10f1.alf"
open /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/
echo "✅ Opened folder with activation file"
echo ""

echo "STEP 2: Open Unity license website"
open https://license.unity3d.com/
echo "✅ Opened Unity license website"
echo ""

echo "STEP 3: After you upload and get license/serial, run:"
echo "  cd /Users/rashadwest/BTEBallCODE"
echo "  git add .github/workflows/unity-webgl-build.yml"
echo "  git commit -m 'Add UNITY_LICENSE and UNITY_SERIAL support'"
echo "  git push origin main"
echo ""

echo "=========================================="
echo "Next: Upload the .alf file to Unity website"
echo "Then add UNITY_LICENSE or UNITY_SERIAL to GitHub Secrets"
echo "=========================================="
