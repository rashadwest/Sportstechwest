#!/bin/bash
# Quick helper script to run robot scripts from anywhere

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ "$1" == "env-vars" ] || [ "$1" == "hardcode" ]; then
    echo "Running: robot-hardcode-env-vars.py"
    python scripts/robot-hardcode-env-vars.py
elif [ "$1" == "verify" ]; then
    echo "Running: verify-garvis-unity-integration.py"
    python scripts/verify-garvis-unity-integration.py
elif [ "$1" == "test" ]; then
    echo "Running: garvis-command.py"
    python scripts/garvis-command.py --one-thing "Test Unity build integration" --tasks "Build Unity game"
else
    echo "Usage: ./run-robot.sh [command]"
    echo ""
    echo "Commands:"
    echo "  env-vars  or  hardcode  - Set environment variables (hardcode in workflow)"
    echo "  verify                  - Verify integration setup"
    echo "  test                    - Test full integration"
    echo ""
    echo "Or run from anywhere:"
    echo "  cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
    echo "  python scripts/robot-hardcode-env-vars.py"
fi


