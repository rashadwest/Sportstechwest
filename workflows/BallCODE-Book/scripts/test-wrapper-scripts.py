#!/usr/bin/env python3
"""
Test Full Integration Wrapper Scripts
Quick test to verify all wrapper scripts execute correctly.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

def test_script(script_name: str, test_input: dict) -> dict:
    """Test a wrapper script with test input."""
    script_path = SCRIPTS_DIR / script_name
    
    if not script_path.exists():
        return {
            "status": "error",
            "error": f"Script not found: {script_path}"
        }
    
    try:
        # Convert test input to JSON string
        input_json = json.dumps(test_input)
        
        # Execute script
        process = subprocess.run(
            [sys.executable, str(script_path)],
            input=input_json,
            capture_output=True,
            text=True,
            timeout=30,
            encoding='utf-8'
        )
        
        # Try to parse output as JSON
        try:
            output = json.loads(process.stdout)
        except json.JSONDecodeError:
            output = {
                "status": "error",
                "error": "Could not parse output as JSON",
                "raw_output": process.stdout,
                "stderr": process.stderr
            }
        
        return {
            "status": "success" if process.returncode == 0 else "error",
            "exit_code": process.returncode,
            "output": output,
            "stderr": process.stderr
        }
        
    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "error": "Script execution timeout"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

def main():
    """Run tests for all wrapper scripts."""
    print("🧪 Testing Full Integration Wrapper Scripts\n")
    
    results = {
        "game": None,
        "curriculum": None,
        "book": None,
        "website": None
    }
    
    # Test Game Script
    print("1️⃣ Testing full-integration-apply-game.py...")
    game_test = {
        "unityScripts": [],
        "levelFiles": [],
        "exerciseConfig": {},
        "integrationData": {}
    }
    results["game"] = test_script("full-integration-apply-game.py", game_test)
    if results["game"]["status"] == "success":
        print("   ✅ Game script test passed\n")
    else:
        print(f"   ❌ Game script test failed: {results['game'].get('error', 'Unknown error')}\n")
    
    # Test Curriculum Script
    print("2️⃣ Testing full-integration-apply-curriculum.py...")
    curriculum_test = {
        "curriculumUpdates": [],
        "schemaUpdates": {}
    }
    results["curriculum"] = test_script("full-integration-apply-curriculum.py", curriculum_test)
    if results["curriculum"]["status"] == "success":
        print("   ✅ Curriculum script test passed\n")
    else:
        print(f"   ❌ Curriculum script test failed: {results['curriculum'].get('error', 'Unknown error')}\n")
    
    # Test Book Script
    print("3️⃣ Testing full-integration-apply-book.py...")
    book_test = {
        "bookUpdates": [],
        "contentUpdates": []
    }
    results["book"] = test_script("full-integration-apply-book.py", book_test)
    if results["book"]["status"] == "success":
        print("   ✅ Book script test passed\n")
    else:
        print(f"   ❌ Book script test failed: {results['book'].get('error', 'Unknown error')}\n")
    
    # Test Website Script
    print("4️⃣ Testing full-integration-apply-website.py...")
    website_test = {
        "htmlFiles": [],
        "cssUpdates": [],
        "jsUpdates": []
    }
    results["website"] = test_script("full-integration-apply-website.py", website_test)
    if results["website"]["status"] == "success":
        print("   ✅ Website script test passed\n")
    else:
        print(f"   ❌ Website script test failed: {results['website'].get('error', 'Unknown error')}\n")
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for r in results.values() if r and r.get("status") == "success")
    total = len([r for r in results.values() if r])
    
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! Scripts are ready for n8n integration.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Review errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

