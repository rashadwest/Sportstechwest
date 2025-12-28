#!/usr/bin/env python3
"""
Garvis Unity Build Automation
Autonomous Unity build execution via Garvis system

Purpose: Execute Unity builds autonomously without human intervention
Cost: FREE (uses local Mac + existing Unity license)
"""

import subprocess
import sys
import os
from pathlib import Path

# Garvis integration
SCRIPT_DIR = Path(__file__).parent
BUILD_SCRIPT = SCRIPT_DIR / "custom-unity-build-orchestrator.py"

def execute_unity_build():
    """Execute Unity build via Garvis"""
    print("=" * 60)
    print("Garvis: Unity Build Automation")
    print("=" * 60)
    print(f"Build Script: {BUILD_SCRIPT}")
    print(f"Script Exists: {BUILD_SCRIPT.exists()}")
    print("=" * 60)
    print()
    
    if not BUILD_SCRIPT.exists():
        print(f"❌ Build script not found: {BUILD_SCRIPT}")
        return False
    
    print("🚀 Starting Unity build...")
    print()
    
    # Execute build script
    result = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT)],
        cwd=SCRIPT_DIR.parent,
        capture_output=False  # Show output in real-time
    )
    
    if result.returncode == 0:
        print()
        print("=" * 60)
        print("✅ Garvis: Unity build completed successfully!")
        print("=" * 60)
        return True
    else:
        print()
        print("=" * 60)
        print(f"❌ Garvis: Unity build failed (exit code: {result.returncode})")
        print("=" * 60)
        return False

if __name__ == "__main__":
    success = execute_unity_build()
    sys.exit(0 if success else 1)


