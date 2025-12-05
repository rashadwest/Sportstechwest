#!/bin/bash

# Unity Story Mode Setup Automation Script
# Purpose: Copy Story Mode scripts from local to Unity project and create folder structure
# Usage: ./automate-unity-setup.sh <unity-project-path>

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory (where this script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNITY_SCRIPTS_DIR="${SCRIPT_DIR}/Unity-Scripts"
TARGET_SCRIPTS_DIR=""

# Check if Unity project path is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Unity project path not provided${NC}"
    echo "Usage: ./automate-unity-setup.sh <unity-project-path>"
    echo "Example: ./automate-unity-setup.sh ~/Projects/BTEBallCODE"
    exit 1
fi

UNITY_PROJECT_PATH="$1"
TARGET_SCRIPTS_DIR="${UNITY_PROJECT_PATH}/Assets/Scripts/StoryMode"

# Validate Unity project path
if [ ! -d "$UNITY_PROJECT_PATH" ]; then
    echo -e "${RED}Error: Unity project path does not exist: ${UNITY_PROJECT_PATH}${NC}"
    exit 1
fi

# Validate Unity project structure
if [ ! -d "${UNITY_PROJECT_PATH}/Assets" ]; then
    echo -e "${RED}Error: Not a valid Unity project (Assets folder not found)${NC}"
    exit 1
fi

# Validate source scripts directory
if [ ! -d "$UNITY_SCRIPTS_DIR" ]; then
    echo -e "${RED}Error: Unity-Scripts directory not found: ${UNITY_SCRIPTS_DIR}${NC}"
    exit 1
fi

echo -e "${GREEN}Unity Story Mode Setup Automation${NC}"
echo "=================================="
echo "Source: ${UNITY_SCRIPTS_DIR}"
echo "Target: ${TARGET_SCRIPTS_DIR}"
echo ""

# Create target directory structure
echo -e "${YELLOW}Creating folder structure...${NC}"
mkdir -p "${TARGET_SCRIPTS_DIR}"

# List of scripts to copy
SCRIPTS=(
    "StoryModeManager.cs"
    "StoryData.cs"
    "GameModeManager.cs"
    "StoryEpisodeCreator.cs"
    "BallCODEStarter.cs"
    "MetricsCollector.cs"
    "LevelData.cs"
    "LevelDataManager.cs"
    "AIMCODELevelGenerator.cs"
    "TestStoryDataHelper.cs"
)

# Copy scripts
echo -e "${YELLOW}Copying scripts...${NC}"
COPIED_COUNT=0
MISSING_COUNT=0

for script in "${SCRIPTS[@]}"; do
    SOURCE_FILE="${UNITY_SCRIPTS_DIR}/${script}"
    TARGET_FILE="${TARGET_SCRIPTS_DIR}/${script}"
    
    if [ -f "$SOURCE_FILE" ]; then
        cp "$SOURCE_FILE" "$TARGET_FILE"
        echo -e "  ${GREEN}✓${NC} Copied: ${script}"
        ((COPIED_COUNT++))
    else
        echo -e "  ${YELLOW}⚠${NC} Missing: ${script} (skipping)"
        ((MISSING_COUNT++))
    fi
done

echo ""
echo -e "${GREEN}Summary:${NC}"
echo "  Copied: ${COPIED_COUNT} scripts"
if [ $MISSING_COUNT -gt 0 ]; then
    echo -e "  ${YELLOW}Missing: ${MISSING_COUNT} scripts${NC}"
fi

# Create additional folders for story content
echo ""
echo -e "${YELLOW}Creating story content folders...${NC}"
mkdir -p "${UNITY_PROJECT_PATH}/Assets/StoryContent/Episodes"
mkdir -p "${UNITY_PROJECT_PATH}/Assets/StoryContent/Audio/Episode1"
mkdir -p "${UNITY_PROJECT_PATH}/Assets/StoryContent/Audio/Episode2"
mkdir -p "${UNITY_PROJECT_PATH}/Assets/StoryContent/Audio/Episode3"

echo -e "  ${GREEN}✓${NC} Created: Assets/StoryContent/Episodes"
echo -e "  ${GREEN}✓${NC} Created: Assets/StoryContent/Audio/Episode1"
echo -e "  ${GREEN}✓${NC} Created: Assets/StoryContent/Audio/Episode2"
echo -e "  ${GREEN}✓${NC} Created: Assets/StoryContent/Audio/Episode3"

# Create .meta file template (Unity will generate these, but we can note it)
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Open Unity project in Unity Editor"
echo "2. Unity will automatically compile the scripts"
echo "3. Check Unity Console for any compilation errors"
echo "4. Follow UNITY-SETUP-GUIDE.md for scene setup"
echo ""
echo -e "${GREEN}Setup complete!${NC}"


