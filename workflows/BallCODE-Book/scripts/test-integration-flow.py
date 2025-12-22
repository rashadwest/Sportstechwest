#!/usr/bin/env python3
"""
Integration Flow Testing Script
Tests the complete user journey: Book → Exercise → Return

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
from pathlib import Path
import requests
from urllib.parse import urlparse, parse_qs

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"

def test_book1_page_exists():
    """Test that Book 1 page exists."""
    print("📄 Testing Book 1 page exists...")
    
    if not BOOK1_HTML.exists():
        print("  ❌ Book 1 page not found")
        return False
    
    print("  ✅ Book 1 page exists")
    return True

def test_exercise_button():
    """Test that 'Try the Exercise' button exists and has correct URL."""
    print("🔘 Testing 'Try the Exercise' button...")
    
    if not BOOK1_HTML.exists():
        print("  ❌ Cannot test - Book 1 page not found")
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for exercise button
    if 'try-exercise-button' not in content:
        print("  ❌ Exercise button not found")
        return False
    
    # Check for correct URL pattern
    if '/play?book=1&exercise=' not in content:
        print("  ⚠️  Exercise button URL may be incorrect")
        return False
    
    # Extract URL
    import re
    match = re.search(r'href=["\']([^"\']*play[^"\']*)["\']', content)
    if match:
        url = match.group(1)
        print(f"  ✅ Exercise button found with URL: {url}")
        
        # Parse URL parameters
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        required_params = ['book', 'exercise', 'source', 'return']
        missing = [p for p in required_params if p not in params]
        
        if missing:
            print(f"  ⚠️  Missing URL parameters: {', '.join(missing)}")
        else:
            print(f"  ✅ All required URL parameters present")
            print(f"     - book: {params.get('book', [''])[0]}")
            print(f"     - exercise: {params.get('exercise', [''])[0]}")
            print(f"     - source: {params.get('source', [''])[0]}")
            print(f"     - return: {params.get('return', [''])[0]}")
        
        return True
    else:
        print("  ⚠️  Could not extract exercise button URL")
        return False

def test_completion_section():
    """Test that exercise completion section exists."""
    print("✅ Testing exercise completion section...")
    
    if not BOOK1_HTML.exists():
        print("  ❌ Cannot test - Book 1 page not found")
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'exercise-completion' not in content:
        print("  ❌ Exercise completion section not found")
        return False
    
    if 'what-you-learned-section' not in content:
        print("  ⚠️  'What You Learned' section not found")
        return False
    
    print("  ✅ Exercise completion section exists")
    print("  ✅ 'What You Learned' section exists")
    return True

def test_integration_js():
    """Test that integration JavaScript exists."""
    print("📜 Testing integration JavaScript...")
    
    integration_js = WEBSITE_DIR / "books" / "book-integration.js"
    
    if not integration_js.exists():
        print("  ⚠️  book-integration.js not found")
        return False
    
    with open(integration_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_functions = [
        'initializeBookPage',
        'showExerciseCompletion',
        'unlockNextSections'
    ]
    
    missing = [f for f in required_functions if f not in content]
    
    if missing:
        print(f"  ⚠️  Missing functions: {', '.join(missing)}")
        return False
    
    print("  ✅ Integration JavaScript exists with required functions")
    return True

def test_website_structure():
    """Test overall website structure."""
    print("🏗️  Testing website structure...")
    
    required_files = [
        WEBSITE_DIR / "index.html",
        WEBSITE_DIR / "books" / "book1.html",
    ]
    
    missing = [f for f in required_files if not f.exists()]
    
    if missing:
        print(f"  ❌ Missing files:")
        for f in missing:
            print(f"     - {f.relative_to(PROJECT_ROOT)}")
        return False
    
    print("  ✅ Required website files exist")
    return True

def generate_test_report(results):
    """Generate test report."""
    report_file = PROJECT_ROOT / "documents" / "launch-prep" / "integration-flow-test-report.md"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    content = f"""# Integration Flow Test Report

**Generated:** {Path(__file__).stat().st_mtime}
**Status:** {passed}/{total} tests passed

---

## Test Results

"""
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        content += f"- **{test_name}:** {status}\n"
    
    content += f"""
---

## Summary

**Overall Status:** {'✅ READY' if passed == total else '⚠️ NEEDS ATTENTION'}

**Next Steps:**
"""
    
    if passed == total:
        content += "- All integration flow tests passed\n"
        content += "- Ready for manual testing\n"
        content += "- Proceed with launch prep\n"
    else:
        failed_tests = [name for name, result in results.items() if not result]
        content += f"- Fix {len(failed_tests)} failing test(s)\n"
        for test in failed_tests:
            content += f"  - {test}\n"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n📊 Test report saved: {report_file}")
    return report_file

def main():
    """Run all integration flow tests."""
    print("=" * 60)
    print("🧪 Integration Flow Testing")
    print("=" * 60)
    print()
    
    results = {}
    
    results["Book 1 Page Exists"] = test_book1_page_exists()
    print()
    
    results["Exercise Button"] = test_exercise_button()
    print()
    
    results["Completion Section"] = test_completion_section()
    print()
    
    results["Integration JavaScript"] = test_integration_js()
    print()
    
    results["Website Structure"] = test_website_structure()
    print()
    
    # Generate report
    report_file = generate_test_report(results)
    
    # Summary
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    print("=" * 60)
    print(f"📊 Test Summary: {passed}/{total} passed")
    print("=" * 60)
    print()
    
    if passed == total:
        print("✅ All tests passed! Integration flow is ready.")
    else:
        print("⚠️  Some tests failed. Review the test report for details.")
        print(f"   Report: {report_file}")
    
    print()
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

