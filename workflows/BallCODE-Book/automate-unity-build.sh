#!/bin/bash

# Unity WebGL Build Automation Script
# Purpose: Build Unity project as WebGL using Unity CLI
# Usage: ./automate-unity-build.sh <unity-project-path> [build-output-path]

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Unity project path is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Unity project path not provided${NC}"
    echo "Usage: ./automate-unity-build.sh <unity-project-path> [build-output-path]"
    echo "Example: ./automate-unity-build.sh ~/Projects/BTEBallCODE ~/Builds/WebGL"
    exit 1
fi

UNITY_PROJECT_PATH="$1"
BUILD_OUTPUT_PATH="${2:-${UNITY_PROJECT_PATH}/Builds/WebGL}"

# Validate Unity project path
if [ ! -d "$UNITY_PROJECT_PATH" ]; then
    echo -e "${RED}Error: Unity project path does not exist: ${UNITY_PROJECT_PATH}${NC}"
    exit 1
fi

# Find Unity executable
UNITY_EXECUTABLE=""
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    UNITY_EXECUTABLE="/Applications/Unity/Hub/Editor/*/Unity.app/Contents/MacOS/Unity"
    UNITY_EXECUTABLE=$(ls -d $UNITY_EXECUTABLE 2>/dev/null | head -1)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    UNITY_EXECUTABLE="/opt/unity/Editor/Unity"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    UNITY_EXECUTABLE="C:/Program Files/Unity/Hub/Editor/*/Editor/Unity.exe"
    UNITY_EXECUTABLE=$(ls -d $UNITY_EXECUTABLE 2>/dev/null | head -1)
fi

if [ -z "$UNITY_EXECUTABLE" ] || [ ! -f "$UNITY_EXECUTABLE" ]; then
    echo -e "${YELLOW}Warning: Unity executable not found automatically${NC}"
    echo "Please provide Unity executable path:"
    read -p "Unity path: " UNITY_EXECUTABLE
    
    if [ ! -f "$UNITY_EXECUTABLE" ]; then
        echo -e "${RED}Error: Unity executable not found: ${UNITY_EXECUTABLE}${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Unity WebGL Build Automation${NC}"
echo "=================================="
echo "Project: ${UNITY_PROJECT_PATH}"
echo "Output: ${BUILD_OUTPUT_PATH}"
echo "Unity: ${UNITY_EXECUTABLE}"
echo ""

# Create build output directory
mkdir -p "$BUILD_OUTPUT_PATH"

# Create build script for Unity
BUILD_SCRIPT="${UNITY_PROJECT_PATH}/BuildScript.cs"
cat > "$BUILD_SCRIPT" << 'EOF'
using UnityEngine;
using UnityEditor;
using System.IO;

public class BuildScript
{
    [MenuItem("BallCODE/Build WebGL")]
    public static void BuildWebGL()
    {
        string[] scenes = {
            "Assets/Scenes/StoryModeScene.unity"
        };
        
        string buildPath = Path.Combine(Application.dataPath, "../Builds/WebGL");
        
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions
        {
            scenes = scenes,
            locationPathName = buildPath,
            target = BuildTarget.WebGL,
            options = BuildOptions.None
        };
        
        Debug.Log($"Building WebGL to: {buildPath}");
        BuildPipeline.BuildPlayer(buildPlayerOptions);
        Debug.Log("WebGL build complete!");
    }
}
EOF

echo -e "${YELLOW}Building WebGL...${NC}"
echo "This may take several minutes..."

# Build using Unity CLI
"$UNITY_EXECUTABLE" \
    -batchmode \
    -quit \
    -projectPath "$UNITY_PROJECT_PATH" \
    -executeMethod BuildScript.BuildWebGL \
    -logFile "${BUILD_OUTPUT_PATH}/build.log"

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}Build successful!${NC}"
    echo ""
    echo -e "${BLUE}Build Output:${NC} ${BUILD_OUTPUT_PATH}"
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo "1. Test build locally:"
    echo "   cd ${BUILD_OUTPUT_PATH}"
    echo "   python3 -m http.server 8000"
    echo "   Open http://localhost:8000 in browser"
    echo ""
    echo "2. Deploy to Netlify:"
    echo "   ./automate-netlify-deploy.sh ${BUILD_OUTPUT_PATH}"
    echo ""
    
    # Clean up build script
    rm -f "$BUILD_SCRIPT"
    
else
    echo ""
    echo -e "${RED}Build failed!${NC}"
    echo "Check build log: ${BUILD_OUTPUT_PATH}/build.log"
    exit 1
fi


