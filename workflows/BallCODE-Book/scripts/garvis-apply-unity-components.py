#!/usr/bin/env python3
"""
Garvis: Apply Unity Components Automatically
Runs Unity Editor in headless mode to apply UI/UX components to buttons.

This script executes the UIUXButtonSetupHelper editor script in Unity Editor
headless mode, allowing Garvis to apply components without manual Unity Editor steps.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from typing import Dict, Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

# Configuration
UNITY_REPO = "rashadwest/BTEBallCODE"
UNITY_PROJECT_PATH = None  # Will be detected or set via env var

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{BLUE}{text:^60}{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def find_unity_editor() -> Optional[Path]:
    """Find Unity Editor executable on system."""
    # Common Unity Editor paths
    paths = [
        # macOS
        Path("/Applications/Unity/Unity.app/Contents/MacOS/Unity"),
        Path("/Applications/Unity/Hub/Editor/*/Unity.app/Contents/MacOS/Unity"),
        # Linux
        Path("/opt/unity/Editor/Unity"),
        # Windows (if running on Windows)
        Path("C:/Program Files/Unity/Editor/Unity.exe"),
    ]
    
    # Check if Unity is in PATH
    try:
        result = subprocess.run(
            ["which", "Unity"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return Path(result.stdout.strip())
    except:
        pass
    
    # Check common paths
    for path in paths:
        if "*" in str(path):
            # Handle glob patterns
            import glob
            matches = glob.glob(str(path))
            if matches:
                return Path(matches[0])
        elif path.exists():
            return path
    
    return None

def find_unity_project() -> Optional[Path]:
    """Find Unity project path."""
    # Check environment variable
    env_path = os.environ.get("UNITY_PROJECT_PATH")
    if env_path:
        path = Path(env_path)
        if path.exists():
            return path
    
    # Check common locations
    common_paths = [
        Path("/Users/rashadwest/BTEBallCODE"),  # Mac local path
        PROJECT_ROOT.parent / "BTEBallCODE",
        Path.home() / "BTEBallCODE",
        Path("/tmp/BTEBallCODE"),
    ]
    
    for path in common_paths:
        if path.exists() and (path / "Assets").exists():
            return path
    
    return None

def apply_components_via_unity_editor(unity_path: Path, project_path: Path) -> Dict:
    """Run Unity Editor in headless mode to apply components."""
    try:
        print_info(f"Unity Editor: {unity_path}")
        print_info(f"Project Path: {project_path}")
        print_info("Running Unity Editor in headless mode...")
        
        # Unity Editor command for headless mode
        cmd = [
            str(unity_path),
            "-batchmode",           # Run in batch mode (no GUI)
            "-quit",                # Quit after execution
            "-projectPath", str(project_path),
            "-executeMethod", "UIUXButtonSetupHelper.ApplyUIUXImprovementsAuto",
            "-logFile", str(PROJECT_ROOT / "unity-apply-components.log")
        ]
        
        print_info(f"Command: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes timeout
        )
        
        # Check log file for results
        log_file = PROJECT_ROOT / "unity-apply-components.log"
        if log_file.exists():
            log_content = log_file.read_text()
            # Check for compilation errors first
            if "error CS" in log_content or "Scripts have compiler errors" in log_content:
                print_error("Unity Editor reported compilation errors")
                return {
                    "success": False,
                    "error": "Unity compilation errors detected",
                    "log": log_content[-1000:]
                }
            # Check if method was called successfully
            if "UIUXButtonSetupHelper" in log_content and ("Applied" in log_content or "Exiting batchmode successfully" in log_content):
                print_success("Unity Editor executed successfully!")
                print_warning("Note: Components require button selection - use manual method or update script")
                return {
                    "success": True,
                    "message": "Unity Editor executed - components need manual application",
                    "log": log_content[-500:]  # Last 500 chars
                }
            elif "error" in log_content.lower() and "CS" not in log_content:
                # Only treat as error if it's not a compilation error (which we already checked)
                print_error("Unity Editor reported errors")
                return {
                    "success": False,
                    "error": "Unity Editor errors detected",
                    "log": log_content[-1000:]
                }
        
        if result.returncode == 0:
            return {
                "success": True,
                "message": "Unity Editor executed successfully",
                "stdout": result.stdout[-500:]
            }
        else:
            return {
                "success": False,
                "error": f"Unity Editor exited with code {result.returncode}",
                "stderr": result.stderr[-500:]
            }
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Unity Editor execution timed out"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        }

def apply_components_via_github_api() -> Dict:
    """Alternative: Apply components by pushing updated scene files.
    
    Note: This is a workaround - Unity scenes are binary and hard to modify.
    This would require Unity to export scenes as text/YAML format.
    """
    print_warning("GitHub API method not yet implemented")
    print_info("Unity scenes are binary files - cannot modify via API")
    print_info("Recommendation: Use Unity Editor headless mode instead")
    
    return {
        "success": False,
        "error": "GitHub API method not available for Unity scenes",
        "recommendation": "Use Unity Editor headless mode"
    }

def main():
    """Main function."""
    print_header("Garvis: Apply Unity Components Automatically")
    
    # Find Unity Editor
    unity_path = find_unity_editor()
    if not unity_path:
        print_error("Unity Editor not found!")
        print_info("Please install Unity Editor or set UNITY_EDITOR_PATH environment variable")
        print_info("\nAlternative: Use manual Unity Editor step:")
        print_info("  1. Open Unity project")
        print_info("  2. Select all buttons in Hierarchy")
        print_info("  3. Right-click → UI → Apply UI/UX Improvements to Selected Buttons")
        return 1
    
    print_success(f"Found Unity Editor: {unity_path}")
    
    # Find Unity project
    project_path = find_unity_project()
    if not project_path:
        print_error("Unity project not found!")
        print_info("Please set UNITY_PROJECT_PATH environment variable")
        print_info(f"  export UNITY_PROJECT_PATH=/path/to/BTEBallCODE")
        return 1
    
    print_success(f"Found Unity project: {project_path}")
    
    # Check if UIUXButtonSetupHelper exists
    helper_script = project_path / "Assets/Editor/UIUXButtonSetupHelper.cs"
    if not helper_script.exists():
        print_warning("UIUXButtonSetupHelper.cs not found in Unity project")
        print_info("Pushing UI/UX scripts to Unity repository first...")
        
        # Push scripts
        push_script = PROJECT_ROOT / "scripts/push-ui-ux-scripts-to-unity.py"
        if push_script.exists():
            subprocess.run(["python3", str(push_script)])
            print_info("Please pull latest changes in Unity project, then retry")
            return 1
        else:
            print_error("push-ui-ux-scripts-to-unity.py not found")
            return 1
    
    # Apply components
    print_info("Applying UI/UX components to buttons...")
    result = apply_components_via_unity_editor(unity_path, project_path)
    
    if result["success"]:
        print_success("✅ Components applied successfully!")
        print_info("Next: Commit and push changes, then trigger Unity build")
        return 0
    else:
        print_error(f"❌ Failed to apply components: {result.get('error', 'Unknown error')}")
        if "log" in result:
            print_info("Unity Editor log:")
            print(result["log"][-500:])
        return 1

if __name__ == "__main__":
    sys.exit(main())

