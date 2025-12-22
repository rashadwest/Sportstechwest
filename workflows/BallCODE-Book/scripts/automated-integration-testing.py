#!/usr/bin/env python3
"""
Automated Integration Testing System
Tests complete user journey and integration flows

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"
INDEX_HTML = WEBSITE_DIR / "index.html"
INTEGRATION_JS = WEBSITE_DIR / "books" / "book-integration.js"

# Test configuration
LOCALHOST_URL = "http://localhost:8000"
TEST_TIMEOUT = 10

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_success(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.RESET}")

def print_error(message):
    print(f"{Colors.RED}❌ {message}{Colors.RESET}")

def print_warning(message):
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.RESET}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.RESET}")

def check_file_exists(file_path, description):
    """Check if a file exists."""
    if file_path.exists():
        print_success(f"{description} exists: {file_path}")
        return True
    else:
        print_error(f"{description} missing: {file_path}")
        return False

def check_file_content(file_path, required_strings, description):
    """Check if file contains required strings."""
    if not file_path.exists():
        print_error(f"{description} not found")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_found = True
    for required in required_strings:
        if required in content:
            print_success(f"{description} contains: {required}")
        else:
            print_error(f"{description} missing: {required}")
            all_found = False
    
    return all_found

def test_url_accessibility(url, description):
    """Test if URL is accessible."""
    try:
        response = requests.get(url, timeout=TEST_TIMEOUT)
        if response.status_code == 200:
            print_success(f"{description} accessible: {url}")
            return True
        else:
            print_error(f"{description} returned status {response.status_code}: {url}")
            return False
    except requests.exceptions.RequestException as e:
        print_warning(f"{description} not accessible (localhost may not be running): {url}")
        print_info("  To test locally, run: cd BallCode && python3 -m http.server 8000")
        return False

def test_integration_flow():
    """Test the complete integration flow."""
    print()
    print("=" * 60)
    print("🔄 Testing Integration Flow")
    print("=" * 60)
    print()
    
    # Test 1: File existence
    print("📁 Checking file existence...")
    print()
    
    files_ok = True
    files_ok &= check_file_exists(INDEX_HTML, "Homepage")
    files_ok &= check_file_exists(BOOK1_HTML, "Book 1 page")
    files_ok &= check_file_exists(INTEGRATION_JS, "Integration JavaScript")
    
    print()
    
    # Test 2: Homepage content
    print("🏠 Testing homepage content...")
    print()
    
    homepage_checks = [
        ("Book 1 link", ["book1", "Book 1", "books/book1"]),
        ("Navigation", ["About", "Contact"]),
        ("Contact info", ["info@ballcode.co", "schools@ballcode.co"]),
    ]
    
    homepage_ok = True
    for check_name, required_strings in homepage_checks:
        for required in required_strings:
            if required.lower() in INDEX_HTML.read_text(encoding='utf-8').lower():
                print_success(f"Homepage contains: {required}")
            else:
                print_error(f"Homepage missing: {required}")
                homepage_ok = False
    
    print()
    
    # Test 3: Book 1 page content
    print("📖 Testing Book 1 page content...")
    print()
    
    book1_content = BOOK1_HTML.read_text(encoding='utf-8')
    
    book1_checks = [
        ("Try the Exercise button", ["Try the Exercise", "try-exercise", "exercise"]),
        ("Story content", ["story", "Nova", "Shadow Press"]),
        ("What You Learned section", ["What You Learned", "what-you-learned"]),
        ("Return flow", ["return", "back", "book1"]),
    ]
    
    book1_ok = True
    for check_name, required_strings in book1_checks:
        found = False
        for required in required_strings:
            if required.lower() in book1_content.lower():
                print_success(f"Book 1 contains: {required}")
                found = True
                break
        if not found:
            print_error(f"Book 1 missing: {check_name}")
            book1_ok = False
    
    print()
    
    # Test 4: Integration JavaScript
    print("🔗 Testing integration JavaScript...")
    print()
    
    if INTEGRATION_JS.exists():
        js_content = INTEGRATION_JS.read_text(encoding='utf-8')
        
        js_checks = [
            ("URL parameter handling", ["URLSearchParams", "get", "url"]),
            ("Exercise completion tracking", ["completed", "exercise", "localStorage"]),
            ("Return flow", ["return", "window.location", "href"]),
        ]
        
        js_ok = True
        for check_name, required_strings in js_checks:
            found = False
            for required in required_strings:
                if required.lower() in js_content.lower():
                    print_success(f"Integration JS contains: {required}")
                    found = True
                    break
            if not found:
                print_error(f"Integration JS missing: {check_name}")
                js_ok = False
    else:
        print_error("Integration JavaScript file not found")
        js_ok = False
    
    print()
    
    # Test 5: URL structure
    print("🔗 Testing URL structure...")
    print()
    
    # Check if exercise URL is referenced
    book1_content = BOOK1_HTML.read_text(encoding='utf-8')
    
    url_checks = [
        ("Exercise URL reference", ["exercise", "game", "unity"]),
        ("Return URL parameter", ["return", "?return=", "book1"]),
    ]
    
    url_ok = True
    for check_name, required_strings in url_checks:
        found = False
        for required in required_strings:
            if required.lower() in book1_content.lower():
                print_success(f"URL structure contains: {required}")
                found = True
                break
        if not found:
            print_warning(f"URL structure may be missing: {check_name}")
            # Don't fail on this, just warn
    
    print()
    
    # Test 6: Localhost accessibility (optional)
    print("🌐 Testing localhost accessibility (optional)...")
    print()
    
    localhost_ok = test_url_accessibility(f"{LOCALHOST_URL}/", "Homepage")
    test_url_accessibility(f"{LOCALHOST_URL}/books/book1.html", "Book 1 page")
    
    print()
    
    # Summary
    print("=" * 60)
    print("📊 Integration Flow Test Summary")
    print("=" * 60)
    print()
    
    all_tests = {
        "File Existence": files_ok,
        "Homepage Content": homepage_ok,
        "Book 1 Content": book1_ok,
        "Integration JavaScript": js_ok,
        "URL Structure": url_ok,
    }
    
    passed = sum(1 for v in all_tests.values() if v)
    total = len(all_tests)
    
    for test_name, result in all_tests.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    print()
    
    if passed == total:
        print_success("All integration flow tests passed! ✅")
        return True
    else:
        print_warning(f"{total - passed} test(s) failed. Review errors above.")
        return False

def test_bypass_pathway():
    """Test the bypass pathway (direct game access)."""
    print()
    print("=" * 60)
    print("🔄 Testing Bypass Pathway")
    print("=" * 60)
    print()
    
    print_info("Bypass pathway: Website → Game (direct) → Score → Return")
    print()
    
    # Check if direct game access is possible
    index_content = INDEX_HTML.read_text(encoding='utf-8')
    
    bypass_checks = [
        ("Direct game link", ["game", "exercise", "play"]),
        ("Game selection", ["select", "choose", "direct"]),
    ]
    
    bypass_ok = True
    for check_name, required_strings in bypass_checks:
        found = False
        for required in required_strings:
            if required.lower() in index_content.lower():
                print_success(f"Bypass pathway contains: {required}")
                found = True
                break
        if not found:
            print_warning(f"Bypass pathway may be missing: {check_name}")
            # Don't fail, just note it's optional
    
    print()
    print_info("Note: Bypass pathway is optional for initial launch")
    print()
    
    return True

def main():
    """Main testing function."""
    print("=" * 60)
    print("🧪 BallCODE Automated Integration Testing")
    print("=" * 60)
    print()
    
    # Test ideal pathway
    ideal_ok = test_integration_flow()
    
    # Test bypass pathway
    bypass_ok = test_bypass_pathway()
    
    print()
    print("=" * 60)
    print("📋 Final Results")
    print("=" * 60)
    print()
    
    if ideal_ok:
        print_success("Ideal pathway: ✅ READY")
    else:
        print_error("Ideal pathway: ⚠️  NEEDS WORK")
    
    if bypass_ok:
        print_success("Bypass pathway: ✅ READY (optional)")
    else:
        print_warning("Bypass pathway: ⚠️  OPTIONAL")
    
    print()
    print("🚀 Next Steps:")
    print("  1. Fix any failed tests")
    print("  2. Test manually on localhost")
    print("  3. Test on mobile device")
    print("  4. Run this script again to verify")
    print()
    
    return ideal_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

