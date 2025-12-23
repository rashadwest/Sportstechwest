#!/usr/bin/env python3
"""
Garvis Push Command - Natural Language Interface
Handles "website push", "game push", "push all" commands
"""

import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
GARVIS_PUSH = SCRIPT_DIR / "garvis-push.py"

def main():
    """Handle natural language push commands"""
    if len(sys.argv) < 2:
        # Default to all
        subprocess.run([sys.executable, str(GARVIS_PUSH), "--all"])
        return
    
    command = sys.argv[1].lower()
    
    if command in ['website', 'web', 'site']:
        subprocess.run([sys.executable, str(GARVIS_PUSH), "--website"])
    elif command in ['game', 'games', 'unity']:
        subprocess.run([sys.executable, str(GARVIS_PUSH), "--game"])
    elif command in ['all', 'everything', 'both']:
        subprocess.run([sys.executable, str(GARVIS_PUSH), "--all"])
    else:
        print("Usage: python scripts/garvis-push-command.py [website|game|all]")
        print("\nCommands:")
        print("  website  - Push website only")
        print("  game     - Push game levels only")
        print("  all      - Push everything (default)")
        print("\nExamples:")
        print("  python scripts/garvis-push-command.py website")
        print("  python scripts/garvis-push-command.py game")
        print("  python scripts/garvis-push-command.py all")

if __name__ == "__main__":
    main()

