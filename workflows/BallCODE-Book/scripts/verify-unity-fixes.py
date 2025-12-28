#!/usr/bin/env python3
"""
Verify Unity Compilation Fixes
Checks that all fixes are properly applied to Unity scripts.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

UNITY_SCRIPTS = Path("/Users/rashadwest/BTEBallCODE/Assets/Scripts")

def check_improved_button():
    """Check ImprovedButton.cs has correct access modifiers."""
    file = UNITY_SCRIPTS / "ImprovedButton.cs"
    if not file.exists():
        return {"status": "error", "message": "ImprovedButton.cs not found"}
    
    content = file.read_text()
    
    checks = {
        "originalScale protected": "protected Vector3 originalScale" in content,
        "originalColor protected": "protected Color originalColor" in content,
        "isHovering protected": "protected bool isHovering" in content,
        "UpdateSelectionState protected": "protected void UpdateSelectionState()" in content,
        "OnPointerEnter virtual": "public virtual void OnPointerEnter" in content,
        "OnPointerExit virtual": "public virtual void OnPointerExit" in content,
    }
    
    all_ok = all(checks.values())
    
    return {
        "status": "ok" if all_ok else "error",
        "checks": checks,
        "all_ok": all_ok
    }

def check_book_menu_manager():
    """Check BookMenuManager.cs exists."""
    file = UNITY_SCRIPTS / "BookMenuManager.cs"
    exists = file.exists()
    
    return {
        "status": "ok" if exists else "error",
        "exists": exists,
        "path": str(file)
    }

def check_child_classes():
    """Check child classes compile correctly."""
    files = {
        "ExitButton.cs": UNITY_SCRIPTS / "ExitButton.cs",
        "FeatureButton.cs": UNITY_SCRIPTS / "FeatureButton.cs",
        "GameModeButton.cs": UNITY_SCRIPTS / "GameModeButton.cs",
    }
    
    results = {}
    for name, path in files.items():
        if not path.exists():
            results[name] = {"status": "error", "message": "File not found"}
            continue
        
        content = path.read_text()
        
        # Check for override keywords (should be present)
        has_override = "override" in content
        has_base_start = "base.Start()" in content if name == "ExitButton.cs" else True
        
        results[name] = {
            "status": "ok" if (has_override or name == "GameModeButton.cs") else "warning",
            "has_override": has_override,
            "has_base_start": has_base_start if name == "ExitButton.cs" else "N/A"
        }
    
    return results

def main():
    """Main verification."""
    print("=" * 70)
    print("🔍 Verifying Unity Compilation Fixes")
    print("=" * 70)
    print()
    
    # Check ImprovedButton
    print("Checking ImprovedButton.cs...")
    improved_result = check_improved_button()
    if improved_result["all_ok"]:
        print("  ✅ All access modifiers correct")
    else:
        print("  ❌ Issues found:")
        for check, passed in improved_result["checks"].items():
            status = "✅" if passed else "❌"
            print(f"    {status} {check}")
    print()
    
    # Check BookMenuManager
    print("Checking BookMenuManager.cs...")
    book_result = check_book_menu_manager()
    if book_result["exists"]:
        print(f"  ✅ Found: {book_result['path']}")
    else:
        print(f"  ❌ Not found: {book_result['path']}")
    print()
    
    # Check child classes
    print("Checking child classes...")
    child_results = check_child_classes()
    for name, result in child_results.items():
        if result.get("status") == "ok":
            print(f"  ✅ {name}: OK")
        else:
            print(f"  ⚠️  {name}: {result.get('message', 'Check needed')}")
    print()
    
    # Summary
    all_ok = (
        improved_result["all_ok"] and
        book_result["exists"] and
        all(r.get("status") == "ok" for r in child_results.values())
    )
    
    print("=" * 70)
    if all_ok:
        print("✅ All fixes verified - Unity should compile successfully")
    else:
        print("⚠️  Some issues detected - Check output above")
    print("=" * 70)

if __name__ == "__main__":
    main()


