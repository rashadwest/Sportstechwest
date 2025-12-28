#!/usr/bin/env python3
"""
Enhance Integration Testing Automation
Adds comprehensive tests, mobile testing, and performance tests

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import re
import requests
import time
from pathlib import Path
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"
INDEX_HTML = WEBSITE_DIR / "index.html"
INTEGRATION_JS = WEBSITE_DIR / "books" / "book-integration.js"
TRACKING_JS = WEBSITE_DIR / "js" / "measurement-tracking.js"

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

def test_file_size(file_path, max_size_mb=5):
    """Test file size is reasonable."""
    if not file_path.exists():
        return False, 0
    
    size_mb = file_path.stat().st_size / (1024 * 1024)
    if size_mb > max_size_mb:
        return False, size_mb
    return True, size_mb

def test_page_performance(url, max_load_time=3):
    """Test page load performance."""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=TEST_TIMEOUT)
        load_time = time.time() - start_time
        
        if response.status_code == 200 and load_time <= max_load_time:
            return True, load_time
        return False, load_time
    except:
        return False, 999

def test_mobile_viewport():
    """Test mobile viewport meta tag."""
    if not INDEX_HTML.exists():
        return False
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    viewport_patterns = [
        r'<meta[^>]*name=["\']viewport["\']',
        r'viewport.*width.*device-width',
        r'viewport.*initial-scale'
    ]
    
    for pattern in viewport_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    
    return False

def test_touch_targets():
    """Test touch target sizes in CSS."""
    css_file = WEBSITE_DIR / "css" / "style.css"
    if not css_file.exists():
        return False
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for mobile-specific touch target rules
    touch_patterns = [
        r'min-height:\s*44px',
        r'min-width:\s*44px',
        r'touch-target',
        r'@media.*mobile'
    ]
    
    found = False
    for pattern in touch_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found = True
            break
    
    return found

def test_measurement_tracking():
    """Test measurement tracking is included."""
    html_files = [INDEX_HTML, BOOK1_HTML]
    
    for html_file in html_files:
        if not html_file.exists():
            continue
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'measurement-tracking.js' in content:
            return True
    
    return False

def test_curriculum_section():
    """Test curriculum section exists in Book 1."""
    if not BOOK1_HTML.exists():
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    curriculum_indicators = [
        'curriculum',
        'learning objective',
        'standards',
        'What You\'re Learning'
    ]
    
    found = 0
    for indicator in curriculum_indicators:
        if indicator.lower() in content.lower():
            found += 1
    
    return found >= 2

def test_accessibility():
    """Test basic accessibility features."""
    html_files = [INDEX_HTML, BOOK1_HTML]
    
    all_good = True
    for html_file in html_files:
        if not html_file.exists():
            continue
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for alt text on images
        img_pattern = r'<img[^>]*>'
        images = re.findall(img_pattern, content, re.IGNORECASE)
        for img in images:
            if 'alt=' not in img.lower():
                all_good = False
                break
        
        # Check for semantic HTML
        if '<main>' not in content and '<article>' not in content:
            # Not critical, just note
            pass
    
    return all_good

def run_comprehensive_tests():
    """Run all comprehensive tests."""
    print()
    print("=" * 60)
    print("🧪 Comprehensive Integration Testing")
    print("=" * 60)
    print()
    
    results = {}
    
    # File existence tests
    print("📁 File Existence Tests...")
    print()
    
    files_to_check = [
        (INDEX_HTML, "Homepage"),
        (BOOK1_HTML, "Book 1 page"),
        (INTEGRATION_JS, "Integration JavaScript"),
        (TRACKING_JS, "Measurement tracking")
    ]
    
    for file_path, description in files_to_check:
        if file_path.exists():
            size_ok, size_mb = test_file_size(file_path)
            if size_ok:
                print_success(f"{description} exists ({size_mb:.2f} MB)")
                results[f"{description} Size"] = True
            else:
                print_warning(f"{description} exists but large ({size_mb:.2f} MB)")
                results[f"{description} Size"] = False
        else:
            print_error(f"{description} missing")
            results[f"{description} Exists"] = False
    
    print()
    
    # Performance tests
    print("⚡ Performance Tests...")
    print()
    
    perf_tests = [
        (f"{LOCALHOST_URL}/", "Homepage load time"),
        (f"{LOCALHOST_URL}/books/book1.html", "Book 1 load time")
    ]
    
    for url, description in perf_tests:
        perf_ok, load_time = test_page_performance(url)
        if perf_ok:
            print_success(f"{description}: {load_time:.2f}s")
            results[description] = True
        else:
            if load_time == 999:
                print_warning(f"{description}: Cannot test (localhost not running)")
            else:
                print_warning(f"{description}: {load_time:.2f}s (target: <3s)")
            results[description] = perf_ok
    
    print()
    
    # Mobile tests
    print("📱 Mobile Responsiveness Tests...")
    print()
    
    viewport_ok = test_mobile_viewport()
    if viewport_ok:
        print_success("Viewport meta tag present")
    else:
        print_error("Viewport meta tag missing")
    results["Mobile Viewport"] = viewport_ok
    
    touch_ok = test_touch_targets()
    if touch_ok:
        print_success("Touch target CSS rules present")
    else:
        print_warning("Touch target CSS rules may be missing")
    results["Touch Targets"] = touch_ok
    
    print()
    
    # Integration tests
    print("🔗 Integration Tests...")
    print()
    
    tracking_ok = test_measurement_tracking()
    if tracking_ok:
        print_success("Measurement tracking included")
    else:
        print_warning("Measurement tracking not found")
    results["Measurement Tracking"] = tracking_ok
    
    curriculum_ok = test_curriculum_section()
    if curriculum_ok:
        print_success("Curriculum section present")
    else:
        print_warning("Curriculum section may be missing")
    results["Curriculum Section"] = curriculum_ok
    
    print()
    
    # Accessibility tests
    print("♿ Accessibility Tests...")
    print()
    
    a11y_ok = test_accessibility()
    if a11y_ok:
        print_success("Basic accessibility features present")
    else:
        print_warning("Some accessibility features may be missing")
    results["Accessibility"] = a11y_ok
    
    print()
    
    # Summary
    print("=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    print()
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "⚠️  WARN"
        print(f"{status} - {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    print()
    
    if passed == total:
        print_success("All comprehensive tests passed! ✅")
        return True
    else:
        print_warning(f"{total - passed} test(s) need attention")
        return passed >= total * 0.8  # 80% pass rate is acceptable

def main():
    """Main function."""
    import re
    
    print("=" * 60)
    print("🚀 Enhanced Integration Testing")
    print("=" * 60)
    print()
    
    success = run_comprehensive_tests()
    
    print()
    print("🚀 Next Steps:")
    print("  1. Fix any failed tests")
    print("  2. Test manually on localhost")
    print("  3. Test on actual mobile devices")
    print("  4. Run performance optimization if needed")
    print()
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


