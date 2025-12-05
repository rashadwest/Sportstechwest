#!/bin/bash

# Copy GitHub Actions Workflow to Unity Repository
# Purpose: Copy unity-webgl-build.yml to BTEBallCODE repository

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Copying GitHub Actions Workflow to Unity Repository${NC}"
echo "=========================================================="
echo ""

# Source file
SOURCE_FILE=".github/workflows/unity-webgl-build.yml"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if source file exists
if [ ! -f "$SOURCE_DIR/$SOURCE_FILE" ]; then
    echo -e "${RED}Error: Source file not found: $SOURCE_FILE${NC}"
    exit 1
fi

# Unity repository path (adjust as needed)
UNITY_REPO_PATH="${1:-$HOME/Projects/BTEBallCODE}"

# Check if Unity repo exists
if [ ! -d "$UNITY_REPO_PATH" ]; then
    echo -e "${YELLOW}Unity repository not found at: $UNITY_REPO_PATH${NC}"
    echo ""
    echo "Please provide the path to your BTEBallCODE repository:"
    read -p "Path: " UNITY_REPO_PATH
    
    if [ ! -d "$UNITY_REPO_PATH" ]; then
        echo -e "${RED}Error: Directory does not exist: $UNITY_REPO_PATH${NC}"
        exit 1
    fi
fi

echo "Source: $SOURCE_DIR/$SOURCE_FILE"
echo "Destination: $UNITY_REPO_PATH/.github/workflows/unity-webgl-build.yml"
echo ""

# Create .github/workflows directory if it doesn't exist
mkdir -p "$UNITY_REPO_PATH/.github/workflows"

# Copy workflow file
cp "$SOURCE_DIR/$SOURCE_FILE" "$UNITY_REPO_PATH/.github/workflows/unity-webgl-build.yml"

echo -e "${GREEN}✓ Workflow file copied successfully!${NC}"
echo ""
echo "Next steps:"
echo "1. cd $UNITY_REPO_PATH"
echo "2. git add .github/workflows/unity-webgl-build.yml"
echo "3. git commit -m 'Add Unity WebGL build and deploy workflow'"
echo "4. git push origin main"
echo ""

