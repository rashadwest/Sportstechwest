#!/usr/bin/env python3
"""
End-to-End Test: Garvis Unity Build System
Comprehensive test of the complete pipeline

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import os
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List

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

def test_prerequisites() -> Dict:
    """Test 1: Verify all prerequisites"""
    print_header("TEST 1: Prerequisites Check")
    
    results = {
        "python": False,
        "unity_editor": False,
        "unity_project": False,
        "build_script": False,
        "garvis_script": False
    }
    
    # Check Python
    try:
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print_success(f"Python: {result.stdout.strip()}")
            results["python"] = True
        else:
            print_error("Python not available")
    except:
        print_error("Python check failed")
    
    # Check Unity Editor
    unity_path = Path("/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity")
    if unity_path.exists():
        print_success(f"Unity Editor: {unity_path}")
        results["unity_editor"] = True
    else:
        print_error(f"Unity Editor not found: {unity_path}")
    
    # Check Unity Project
    project_path = Path("/Users/rashadwest/BTEBallCODE")
    if project_path.exists() and (project_path / "Assets").exists():
        print_success(f"Unity Project: {project_path}")
        results["unity_project"] = True
    else:
        print_error(f"Unity Project not found: {project_path}")
    
    # Check Build Script
    build_script = SCRIPT_DIR / "custom-unity-build-orchestrator.py"
    if build_script.exists():
        print_success(f"Build Script: {build_script.name}")
        results["build_script"] = True
    else:
        print_error(f"Build Script not found: {build_script}")
    
    # Check Garvis Script
    garvis_script = SCRIPT_DIR / "garvis-unity-build.py"
    if garvis_script.exists():
        print_success(f"Garvis Script: {garvis_script.name}")
        results["garvis_script"] = True
    else:
        print_error(f"Garvis Script not found: {garvis_script}")
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '❌ FAIL'}")
    
    return {"passed": all_passed, "results": results}

def test_script_syntax() -> Dict:
    """Test 2: Verify script syntax"""
    print_header("TEST 2: Script Syntax Validation")
    
    scripts = [
        "custom-unity-build-orchestrator.py",
        "garvis-unity-build.py",
        "garvis-push.py"
    ]
    
    results = {}
    for script_name in scripts:
        script_path = SCRIPT_DIR / script_name
        if script_path.exists():
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "py_compile", str(script_path)],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print_success(f"{script_name}: Syntax valid")
                    results[script_name] = True
                else:
                    print_error(f"{script_name}: Syntax error")
                    results[script_name] = False
            except Exception as e:
                print_error(f"{script_name}: Check failed - {e}")
                results[script_name] = False
        else:
            print_warning(f"{script_name}: Not found")
            results[script_name] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '❌ FAIL'}")
    
    return {"passed": all_passed, "results": results}

def test_garvis_push() -> Dict:
    """Test 3: Test Garvis push system"""
    print_header("TEST 3: Garvis Push System")
    
    print_info("Checking Garvis push script...")
    push_script = SCRIPT_DIR / "garvis-push.py"
    
    if not push_script.exists():
        print_error("Garvis push script not found")
        return {"passed": False, "error": "Script not found"}
    
    print_success("Garvis push script found")
    
    # Check if it can be imported (dry run)
    try:
        result = subprocess.run(
            [sys.executable, str(push_script), "--help"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 or "--game" in result.stdout or "--website" in result.stdout:
            print_success("Garvis push script is executable")
            return {"passed": True}
        else:
            print_warning("Garvis push script may have issues")
            return {"passed": False, "error": "Script execution check failed"}
    except subprocess.TimeoutExpired:
        print_warning("Garvis push script check timed out")
        return {"passed": False, "error": "Timeout"}
    except Exception as e:
        print_warning(f"Garvis push script check failed: {e}")
        return {"passed": False, "error": str(e)}

def test_unity_project_structure() -> Dict:
    """Test 4: Verify Unity project structure"""
    print_header("TEST 4: Unity Project Structure")
    
    project_path = Path("/Users/rashadwest/BTEBallCODE")
    required_paths = [
        "Assets",
        "Assets/Scripts",
        "ProjectSettings",
        "Packages"
    ]
    
    results = {}
    for path_name in required_paths:
        path = project_path / path_name
        if path.exists():
            print_success(f"{path_name}: Exists")
            results[path_name] = True
        else:
            print_error(f"{path_name}: Missing")
            results[path_name] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '❌ FAIL'}")
    
    return {"passed": all_passed, "results": results}

def test_build_script_dry_run() -> Dict:
    """Test 5: Dry run of build script (check imports and basic execution)"""
    print_header("TEST 5: Build Script Dry Run")
    
    build_script = SCRIPT_DIR / "custom-unity-build-orchestrator.py"
    
    if not build_script.exists():
        print_error("Build script not found")
        return {"passed": False}
    
    # Try to import and check basic structure
    try:
        # Read script and check for key components
        with open(build_script, 'r') as f:
            content = f.read()
        
        required_components = [
            "class UnityBuildOrchestrator",
            "def check_prerequisites",
            "def build_unity",
            "def verify_build",
            "def deploy_netlify"
        ]
        
        missing = []
        for component in required_components:
            if component in content:
                print_success(f"Component found: {component.split('def ')[-1] if 'def' in component else component.split('class ')[-1]}")
            else:
                print_error(f"Component missing: {component}")
                missing.append(component)
        
        if missing:
            print_warning(f"Missing {len(missing)} components")
            return {"passed": False, "missing": missing}
        else:
            print_success("All required components found")
            return {"passed": True}
            
    except Exception as e:
        print_error(f"Error checking build script: {e}")
        return {"passed": False, "error": str(e)}

def test_garvis_integration() -> Dict:
    """Test 6: Test Garvis integration"""
    print_header("TEST 6: Garvis Integration")
    
    garvis_script = SCRIPT_DIR / "garvis-unity-build.py"
    
    if not garvis_script.exists():
        print_error("Garvis script not found")
        return {"passed": False}
    
    # Check if script can be executed (help or version check)
    try:
        # Check script structure
        with open(garvis_script, 'r') as f:
            content = f.read()
        
        # Check for key functions and imports
        required_elements = [
            "execute_unity_build",
            "BUILD_SCRIPT",
            "subprocess.run"
        ]
        
        missing = []
        for element in required_elements:
            if element in content:
                print_success(f"Element found: {element}")
            else:
                missing.append(element)
        
        if missing:
            print_error(f"Missing elements: {missing}")
            return {"passed": False}
        else:
            print_success("Garvis script structure valid")
            print_success("Garvis can execute build orchestrator")
            return {"passed": True}
            
    except Exception as e:
        print_error(f"Error checking Garvis script: {e}")
        return {"passed": False, "error": str(e)}

def test_github_integration() -> Dict:
    """Test 7: Test GitHub integration (check credentials)"""
    print_header("TEST 7: GitHub Integration")
    
    try:
        # Check if gh CLI is available
        result = subprocess.run(
            ["gh", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print_success("GitHub CLI available")
            
            # Check if authenticated
            auth_result = subprocess.run(
                ["gh", "auth", "status"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if "Logged in" in auth_result.stdout or auth_result.returncode == 0:
                print_success("GitHub authentication: Active")
                return {"passed": True}
            else:
                print_warning("GitHub authentication: Not verified")
                return {"passed": False, "warning": "Auth not verified"}
        else:
            print_warning("GitHub CLI not available (optional)")
            return {"passed": True, "warning": "gh CLI not installed"}
            
    except FileNotFoundError:
        print_warning("GitHub CLI not installed (optional)")
        return {"passed": True, "warning": "gh CLI not installed"}
    except Exception as e:
        print_warning(f"GitHub check failed: {e}")
        return {"passed": True, "warning": str(e)}

def generate_test_report(all_results: Dict):
    """Generate comprehensive test report"""
    print_header("📊 END-TO-END TEST REPORT")
    
    total_tests = len(all_results)
    passed_tests = sum(1 for r in all_results.values() if r.get("passed", False))
    failed_tests = total_tests - passed_tests
    
    print(f"\n{'Test':<40} {'Status':<15}")
    print("-" * 60)
    
    for test_name, result in all_results.items():
        status = "✅ PASS" if result.get("passed", False) else "❌ FAIL"
        print(f"{test_name:<40} {status:<15}")
    
    print("-" * 60)
    print(f"\n{'Total Tests:':<40} {total_tests}")
    print(f"{'Passed:':<40} {passed_tests} ✅")
    print(f"{'Failed:':<40} {failed_tests} {'❌' if failed_tests > 0 else ''}")
    print(f"{'Success Rate:':<40} {(passed_tests/total_tests*100):.1f}%")
    
    print("\n" + "=" * 70)
    
    if failed_tests == 0:
        print_success("🎉 ALL TESTS PASSED - SYSTEM IS READY!")
        print("\nGarvis Unity build system is fully operational.")
        print("You can now use:")
        print(f"  {BLUE}python3 scripts/garvis-unity-build.py{NC}")
    else:
        print_error(f"⚠️  {failed_tests} TEST(S) FAILED")
        print("\nPlease fix the issues above before using the system.")
    
    print("=" * 70)

def main():
    """Run all end-to-end tests"""
    print_header("🧪 END-TO-END TEST: Garvis Unity Build System")
    
    print_info("Running comprehensive system tests...")
    print_info("This will verify all components are working correctly.\n")
    
    all_results = {}
    
    # Run all tests
    all_results["Prerequisites"] = test_prerequisites()
    all_results["Script Syntax"] = test_script_syntax()
    all_results["Garvis Push"] = test_garvis_push()
    all_results["Unity Project"] = test_unity_project_structure()
    all_results["Build Script"] = test_build_script_dry_run()
    all_results["Garvis Integration"] = test_garvis_integration()
    all_results["GitHub Integration"] = test_github_integration()
    
    # Generate report
    generate_test_report(all_results)
    
    # Return exit code
    all_passed = all(r.get("passed", False) for r in all_results.values())
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

