#!/bin/bash
# Setup Soccer Unity Foundation - Automated Setup Script
# Creates folder structure and initial files

set -e  # Exit on error

echo "⚽ Setting Up Soccer Unity Foundation"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Unity project path is provided
if [ -z "$1" ]; then
    echo -e "${YELLOW}Usage: ./setup-soccer-unity-foundation.sh <UnityProjectPath>${NC}"
    echo ""
    echo "Example:"
    echo "  ./setup-soccer-unity-foundation.sh ~/UnityProjects/BallCODE"
    echo ""
    echo "Or set UNITY_PROJECT_PATH environment variable:"
    echo "  export UNITY_PROJECT_PATH=~/UnityProjects/BallCODE"
    echo "  ./setup-soccer-unity-foundation.sh"
    exit 1
fi

UNITY_PROJECT_PATH="$1"
if [ -z "$UNITY_PROJECT_PATH" ]; then
    UNITY_PROJECT_PATH="${UNITY_PROJECT_PATH:-$1}"
fi

# Verify Unity project exists
if [ ! -d "$UNITY_PROJECT_PATH" ]; then
    echo -e "${YELLOW}⚠️  Unity project not found at: $UNITY_PROJECT_PATH${NC}"
    echo "Please provide correct path to Unity project"
    exit 1
fi

ASSETS_DIR="$UNITY_PROJECT_PATH/Assets"
SCRIPTS_DIR="$ASSETS_DIR/Scripts"

# Check if Assets folder exists
if [ ! -d "$ASSETS_DIR" ]; then
    echo -e "${YELLOW}⚠️  Assets folder not found. Is this a Unity project?${NC}"
    exit 1
fi

echo -e "${BLUE}Unity Project: $UNITY_PROJECT_PATH${NC}"
echo ""

# Create folder structure
echo -e "${BLUE}Creating folder structure...${NC}"

mkdir -p "$SCRIPTS_DIR/Sport"
mkdir -p "$SCRIPTS_DIR/Soccer"
mkdir -p "$ASSETS_DIR/Scenes/Soccer"
mkdir -p "$ASSETS_DIR/Prefabs/Soccer"

echo -e "${GREEN}✅ Folder structure created${NC}"
echo ""

# Create README files
echo -e "${BLUE}Creating README files...${NC}"

# Sport folder README
cat > "$SCRIPTS_DIR/Sport/README.md" << 'EOF'
# Sport-Agnostic Framework

This folder contains sport-agnostic base classes and interfaces.

## Files:
- `SportGameManager.cs` - Abstract base class for sport managers
- `ISportCommand.cs` - Interface for sport-specific commands
- `SportLevelData.cs` - Base class for level data

## Usage:
Both Basketball and Soccer implementations inherit from these base classes.
EOF

# Soccer folder README
cat > "$SCRIPTS_DIR/Soccer/README.md" << 'EOF'
# Soccer Module

Soccer-specific implementation of BallCODE game.

## Files:
- `SoccerGameManager.cs` - Soccer game manager
- `SoccerCommands.cs` - Soccer-specific commands
- `SoccerField.cs` - Soccer field environment
- `SoccerBall.cs` - Soccer ball physics
- `SoccerPlayer.cs` - Soccer player movement

## Status:
In development - Week 1 foundation setup
EOF

echo -e "${GREEN}✅ README files created${NC}"
echo ""

# Create template files
echo -e "${BLUE}Creating template files...${NC}"

# SportGameManager template
cat > "$SCRIPTS_DIR/Sport/SportGameManager.cs.template" << 'EOF'
using UnityEngine;

/// <summary>
/// Abstract base class for sport-specific game managers
/// </summary>
public abstract class SportGameManager : MonoBehaviour
{
    public string sportName;
    
    public abstract void InitializeSport();
    public abstract void HandleSportSpecificMechanics();
    public abstract void LoadLevel(string levelId);
    public abstract void ExecuteCommand(string command, params object[] args);
}
EOF

# SoccerGameManager template
cat > "$SCRIPTS_DIR/Soccer/SoccerGameManager.cs.template" << 'EOF'
using UnityEngine;

/// <summary>
/// Soccer-specific game manager
/// </summary>
public class SoccerGameManager : SportGameManager
{
    public SoccerField field;
    public SoccerBall ball;
    public SoccerPlayer player;
    
    public override void InitializeSport()
    {
        sportName = "soccer";
        // TODO: Initialize soccer-specific components
        field = FindObjectOfType<SoccerField>();
        ball = FindObjectOfType<SoccerBall>();
        player = FindObjectOfType<SoccerPlayer>();
    }
    
    public override void HandleSportSpecificMechanics()
    {
        // TODO: Implement soccer-specific game logic
    }
    
    public override void LoadLevel(string levelId)
    {
        // TODO: Load soccer level
        Debug.Log($"Loading soccer level: {levelId}");
    }
    
    public override void ExecuteCommand(string command, params object[] args)
    {
        // TODO: Execute soccer command
        Debug.Log($"Executing soccer command: {command}");
    }
}
EOF

echo -e "${GREEN}✅ Template files created${NC}"
echo ""

# Summary
echo -e "${GREEN}✅ Soccer Unity Foundation Setup Complete!${NC}"
echo ""
echo "Created:"
echo "  📁 $SCRIPTS_DIR/Sport/"
echo "  📁 $SCRIPTS_DIR/Soccer/"
echo "  📁 $ASSETS_DIR/Scenes/Soccer/"
echo "  📁 $ASSETS_DIR/Prefabs/Soccer/"
echo ""
echo "Next steps:"
echo "  1. Open Unity project"
echo "  2. Review template files"
echo "  3. Create actual C# scripts from templates"
echo "  4. Follow SOCCER-UNITY-FOUNDATION-SETUP.md guide"
echo ""


