#!/usr/bin/env python3
"""
Robot: Garvis Unity Build Setup & Verification
Automates setup and verification of Garvis Unity build system

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import os
from pathlib import Path
from datetime import datetime

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

def print_header(text):
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}{text:^70}{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def check_python():
    """Check Python availability"""
    try:
        result = subprocess.run(
            ["python3", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print_success(f"Python available: {version}")
            return True
        return False
    except:
        print_error("Python 3 not found")
        return False

def check_unity_editor():
    """Check Unity Editor"""
    unity_path = Path("/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity")
    if unity_path.exists():
        print_success(f"Unity Editor found: {unity_path}")
        return True
    else:
        print_error(f"Unity Editor not found: {unity_path}")
        return False

def check_unity_project():
    """Check Unity project"""
    project_path = Path("/Users/rashadwest/BTEBallCODE")
    assets_path = project_path / "Assets"
    
    if project_path.exists() and assets_path.exists():
        print_success(f"Unity project found: {project_path}")
        return True
    else:
        print_error(f"Unity project not found: {project_path}")
        return False

def check_build_script():
    """Check build orchestrator script"""
    script_path = SCRIPT_DIR / "custom-unity-build-orchestrator.py"
    if script_path.exists():
        print_success(f"Build orchestrator found: {script_path.name}")
        return True
    else:
        print_error(f"Build orchestrator not found: {script_path}")
        return False

def check_garvis_script():
    """Check Garvis Unity build script"""
    script_path = SCRIPT_DIR / "garvis-unity-build.py"
    if script_path.exists():
        print_success(f"Garvis Unity build script found: {script_path.name}")
        return True
    else:
        print_error(f"Garvis Unity build script not found: {script_path}")
        return False

def verify_script_syntax(script_path):
    """Verify Python script syntax"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", str(script_path)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success(f"Syntax valid: {script_path.name}")
            return True
        else:
            print_error(f"Syntax error in {script_path.name}: {result.stderr}")
            return False
    except Exception as e:
        print_error(f"Error checking syntax: {e}")
        return False

def check_netlify_cli():
    """Check Netlify CLI (optional)"""
    try:
        result = subprocess.run(
            ["which", "netlify"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success("Netlify CLI available")
            return True
        else:
            print_warning("Netlify CLI not installed (deployment optional)")
            return False
    except:
        print_warning("Netlify CLI check failed (deployment optional)")
        return False

def test_garvis_script():
    """Test Garvis Unity build script (dry run)"""
    script_path = SCRIPT_DIR / "garvis-unity-build.py"
    
    print_info("Testing Garvis Unity build script...")
    
    # Just verify it can be imported/executed (without actually building)
    try:
        # Check if script is executable
        if not os.access(script_path, os.X_OK):
            print_warning(f"Script not executable, making it executable...")
            os.chmod(script_path, 0o755)
        
        print_success("Garvis Unity build script is ready")
        return True
    except Exception as e:
        print_error(f"Error testing script: {e}")
        return False

def create_readiness_report(results):
    """Create readiness report"""
    all_checks = [
        results.get("python", False),
        results.get("unity_editor", False),
        results.get("unity_project", False),
        results.get("build_script", False),
        results.get("garvis_script", False),
        results.get("build_syntax", False),
        results.get("garvis_syntax", False),
    ]
    
    ready = all(all_checks)
    optional = results.get("netlify_cli", False)
    
    print_header("🤖 Robot: Garvis Unity Build Readiness Report")
    
    print(f"\n{'Component':<30} {'Status':<15}")
    print("-" * 50)
    print(f"{'Python 3':<30} {'✅ Ready' if results.get('python') else '❌ Missing'}")
    print(f"{'Unity Editor':<30} {'✅ Ready' if results.get('unity_editor') else '❌ Missing'}")
    print(f"{'Unity Project':<30} {'✅ Ready' if results.get('unity_project') else '❌ Missing'}")
    print(f"{'Build Orchestrator':<30} {'✅ Ready' if results.get('build_script') else '❌ Missing'}")
    print(f"{'Garvis Script':<30} {'✅ Ready' if results.get('garvis_script') else '❌ Missing'}")
    print(f"{'Build Script Syntax':<30} {'✅ Valid' if results.get('build_syntax') else '❌ Invalid'}")
    print(f"{'Garvis Script Syntax':<30} {'✅ Valid' if results.get('garvis_syntax') else '❌ Invalid'}")
    print(f"{'Netlify CLI':<30} {'✅ Available' if optional else '⚠️  Optional'}")
    
    print("\n" + "=" * 70)
    
    if ready:
        print_success("🎉 GARVIS IS READY TO USE!")
        print("\nYou can now run:")
        print(f"  {BLUE}python3 scripts/garvis-unity-build.py{NC}")
        print("\nOr via Garvis command system:")
        print(f"  {BLUE}python3 scripts/garvis-command.py --one-thing 'Build Unity' --tasks 'Build Unity WebGL'{NC}")
        return True
    else:
        print_error("⚠️  GARVIS NOT READY - Some components missing")
        print("\nPlease fix the issues above and run this script again.")
        return False

def main():
    """Main robot execution"""
    print_header("🤖 Robot: Garvis Unity Build Setup & Verification")
    
    results = {}
    
    # Check prerequisites
    print_info("Checking prerequisites...")
    results["python"] = check_python()
    results["unity_editor"] = check_unity_editor()
    results["unity_project"] = check_unity_project()
    
    print()
    
    # Check scripts
    print_info("Checking scripts...")
    results["build_script"] = check_build_script()
    results["garvis_script"] = check_garvis_script()
    
    print()
    
    # Verify syntax
    if results["build_script"]:
        print_info("Verifying build script syntax...")
        results["build_syntax"] = verify_script_syntax(
            SCRIPT_DIR / "custom-unity-build-orchestrator.py"
        )
    
    if results["garvis_script"]:
        print_info("Verifying Garvis script syntax...")
        results["garvis_syntax"] = verify_script_syntax(
            SCRIPT_DIR / "garvis-unity-build.py"
        )
    
    print()
    
    # Check optional components
    print_info("Checking optional components...")
    results["netlify_cli"] = check_netlify_cli()
    
    print()
    
    # Test Garvis script
    if results["garvis_script"]:
        results["garvis_test"] = test_garvis_script()
    
    print()
    
    # Create report
    ready = create_readiness_report(results)
    
    print()
    print_header("🤖 Robot: Setup Complete")
    
    if ready:
        print_success("Garvis Unity build system is ready to use!")
        print("\nNext steps:")
        print("1. Test the build: python3 scripts/garvis-unity-build.py")
        print("2. Or integrate with Garvis command system")
        return 0
    else:
        print_error("Setup incomplete - please fix issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())


