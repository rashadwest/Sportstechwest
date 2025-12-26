#!/usr/bin/env python3
"""
End-to-End Website Test
Comprehensive test of website functionality, mobile responsiveness, and bugs

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import requests
from pathlib import Path
from typing import Dict, List
import json

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
WEBSITE_PATH = PROJECT_ROOT / "BallCode"

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

def test_website_structure() -> Dict:
    """Test 1: Verify website file structure"""
    print_header("TEST 1: Website File Structure")
    
    required_files = [
        "index.html",
        "books/book1.html",
        "books/book2.html",
        "books/book3.html"
    ]
    
    results = {}
    for file_path in required_files:
        full_path = WEBSITE_PATH / file_path
        if full_path.exists():
            print_success(f"{file_path}: Exists")
            results[file_path] = True
        else:
            print_error(f"{file_path}: Missing")
            results[file_path] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '❌ FAIL'}")
    
    return {"passed": all_passed, "results": results}

def test_html_validation() -> Dict:
    """Test 2: Basic HTML validation"""
    print_header("TEST 2: HTML Validation")
    
    html_files = [
        "index.html",
        "books/book1.html",
        "books/book2.html",
        "books/book3.html"
    ]
    
    results = {}
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic validation
            has_doctype = '<!DOCTYPE' in content or '<!doctype' in content
            has_html = '<html' in content.lower()
            has_head = '<head' in content.lower()
            has_body = '<body' in content.lower()
            has_closing_tags = '</html>' in content.lower()
            
            if has_doctype and has_html and has_head and has_body and has_closing_tags:
                print_success(f"{html_file}: Valid HTML structure")
                results[html_file] = True
            else:
                missing = []
                if not has_doctype: missing.append("DOCTYPE")
                if not has_html: missing.append("html tag")
                if not has_head: missing.append("head tag")
                if not has_body: missing.append("body tag")
                if not has_closing_tags: missing.append("closing html tag")
                print_warning(f"{html_file}: Missing {', '.join(missing)}")
                results[html_file] = False
                
        except Exception as e:
            print_error(f"{html_file}: Error reading - {e}")
            results[html_file] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '⚠️  WARNINGS'}")
    
    return {"passed": all_passed, "results": results}

def test_links() -> Dict:
    """Test 3: Check for broken links"""
    print_header("TEST 3: Link Validation")
    
    html_files = [
        "index.html",
        "books/book1.html",
        "books/book2.html",
        "books/book3.html"
    ]
    
    broken_links = []
    working_links = []
    
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all links
            import re
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            for link in links:
                # Skip mailto, tel, javascript, anchors
                if link.startswith(('mailto:', 'tel:', 'javascript:', '#')):
                    continue
                
                # Check if it's a local file
                if link.startswith('/'):
                    link_path = WEBSITE_PATH / link.lstrip('/')
                elif not link.startswith('http'):
                    link_path = WEBSITE_PATH / Path(html_file).parent / link
                else:
                    # External link - check if accessible
                    try:
                        response = requests.head(link, timeout=5, allow_redirects=True)
                        if response.status_code == 200:
                            working_links.append(link)
                        else:
                            broken_links.append(f"{html_file}: {link} (HTTP {response.status_code})")
                    except:
                        broken_links.append(f"{html_file}: {link} (Connection failed)")
                    continue
                
                if link_path.exists():
                    working_links.append(link)
                else:
                    broken_links.append(f"{html_file}: {link}")
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
    
    if broken_links:
        print_warning(f"Found {len(broken_links)} broken links:")
        for link in broken_links[:10]:  # Show first 10
            print(f"  - {link}")
        if len(broken_links) > 10:
            print(f"  ... and {len(broken_links) - 10} more")
    else:
        print_success(f"All {len(working_links)} links working")
    
    print(f"\n{'Result:':<20} {'✅ PASS' if not broken_links else '⚠️  BROKEN LINKS'}")
    
    return {"passed": len(broken_links) == 0, "broken": broken_links, "working": working_links}

def test_mobile_responsiveness() -> Dict:
    """Test 4: Check mobile responsiveness"""
    print_header("TEST 4: Mobile Responsiveness")
    
    html_files = [
        "index.html",
        "books/book1.html"
    ]
    
    results = {}
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for viewport meta tag
            has_viewport = 'viewport' in content.lower() or 'meta name="viewport"' in content.lower()
            
            # Check for responsive CSS
            has_responsive_css = any(term in content.lower() for term in [
                '@media',
                'max-width',
                'min-width',
                'responsive',
                'mobile'
            ])
            
            # Check for mobile-friendly elements
            has_flexible_images = 'max-width: 100%' in content or 'width: 100%' in content
            
            checks = {
                "viewport": has_viewport,
                "responsive_css": has_responsive_css,
                "flexible_images": has_flexible_images
            }
            
            passed = sum(checks.values())
            total = len(checks)
            
            if passed == total:
                print_success(f"{html_file}: Mobile responsive ({passed}/{total})")
                results[html_file] = True
            else:
                missing = [k for k, v in checks.items() if not v]
                print_warning(f"{html_file}: Missing {', '.join(missing)} ({passed}/{total})")
                results[html_file] = False
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
            results[html_file] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '⚠️  NEEDS IMPROVEMENT'}")
    
    return {"passed": all_passed, "results": results}

def test_images() -> Dict:
    """Test 5: Check for missing images"""
    print_header("TEST 5: Image Validation")
    
    html_files = [
        "index.html",
        "books/book1.html",
        "books/book2.html",
        "books/book3.html"
    ]
    
    missing_images = []
    found_images = []
    
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image references
            import re
            images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
            images += re.findall(r'background-image:\s*url\(["\']?([^"\']+)["\']?\)', content, re.IGNORECASE)
            
            for img_path in images:
                # Skip external images
                if img_path.startswith('http'):
                    found_images.append(img_path)
                    continue
                
                # Check local path
                if img_path.startswith('/'):
                    img_file = WEBSITE_PATH / img_path.lstrip('/')
                else:
                    img_file = WEBSITE_PATH / Path(html_file).parent / img_path
                
                if img_file.exists():
                    found_images.append(img_path)
                else:
                    missing_images.append(f"{html_file}: {img_path}")
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
    
    if missing_images:
        print_warning(f"Found {len(missing_images)} missing images:")
        for img in missing_images[:10]:  # Show first 10
            print(f"  - {img}")
        if len(missing_images) > 10:
            print(f"  ... and {len(missing_images) - 10} more")
    else:
        print_success(f"All {len(found_images)} images found")
    
    print(f"\n{'Result:':<20} {'✅ PASS' if not missing_images else '⚠️  MISSING IMAGES'}")
    
    return {"passed": len(missing_images) == 0, "missing": missing_images, "found": found_images}

def test_javascript() -> Dict:
    """Test 6: Check JavaScript files"""
    print_header("TEST 6: JavaScript Validation")
    
    html_files = [
        "index.html",
        "books/book1.html"
    ]
    
    results = {}
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all script references
            import re
            scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
            
            missing_scripts = []
            for script_path in scripts:
                if script_path.startswith('http'):
                    continue  # External script
                
                if script_path.startswith('/'):
                    script_file = WEBSITE_PATH / script_path.lstrip('/')
                else:
                    script_file = WEBSITE_PATH / Path(html_file).parent / script_path
                
                if not script_file.exists():
                    missing_scripts.append(script_path)
            
            if missing_scripts:
                print_warning(f"{html_file}: Missing scripts: {', '.join(missing_scripts)}")
                results[html_file] = False
            else:
                print_success(f"{html_file}: All scripts found")
                results[html_file] = True
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
            results[html_file] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '⚠️  MISSING SCRIPTS'}")
    
    return {"passed": all_passed, "results": results}

def test_css() -> Dict:
    """Test 7: Check CSS files"""
    print_header("TEST 7: CSS Validation")
    
    html_files = [
        "index.html",
        "books/book1.html"
    ]
    
    results = {}
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all CSS references
            import re
            css_files = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)
            
            missing_css = []
            for css_path in css_files:
                if css_path.startswith('http'):
                    continue  # External CSS
                
                if css_path.startswith('/'):
                    css_file = WEBSITE_PATH / css_path.lstrip('/')
                else:
                    css_file = WEBSITE_PATH / Path(html_file).parent / css_path
                
                if not css_file.exists():
                    missing_css.append(css_path)
            
            if missing_css:
                print_warning(f"{html_file}: Missing CSS: {', '.join(missing_css)}")
                results[html_file] = False
            else:
                print_success(f"{html_file}: All CSS found")
                results[html_file] = True
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
            results[html_file] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '⚠️  MISSING CSS'}")
    
    return {"passed": all_passed, "results": results}

def test_accessibility() -> Dict:
    """Test 8: Basic accessibility checks"""
    print_header("TEST 8: Accessibility Checks")
    
    html_files = [
        "index.html",
        "books/book1.html"
    ]
    
    results = {}
    for html_file in html_files:
        file_path = WEBSITE_PATH / html_file
        if not file_path.exists():
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic accessibility checks
            has_title = '<title>' in content.lower()
            has_alt_text = 'alt=' in content.lower() or 'alt =' in content.lower()
            has_headings = '<h1' in content.lower() or '<h2' in content.lower()
            has_lang = 'lang=' in content.lower() or '<html lang' in content.lower()
            
            checks = {
                "title": has_title,
                "alt_text": has_alt_text,
                "headings": has_headings,
                "language": has_lang
            }
            
            passed = sum(checks.values())
            total = len(checks)
            
            if passed == total:
                print_success(f"{html_file}: Accessibility good ({passed}/{total})")
                results[html_file] = True
            else:
                missing = [k for k, v in checks.items() if not v]
                print_warning(f"{html_file}: Missing {', '.join(missing)} ({passed}/{total})")
                results[html_file] = False
        
        except Exception as e:
            print_error(f"Error checking {html_file}: {e}")
            results[html_file] = False
    
    all_passed = all(results.values())
    print(f"\n{'Result:':<20} {'✅ PASS' if all_passed else '⚠️  NEEDS IMPROVEMENT'}")
    
    return {"passed": all_passed, "results": results}

def generate_test_report(all_results: Dict):
    """Generate comprehensive test report"""
    print_header("📊 END-TO-END WEBSITE TEST REPORT")
    
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
        print_success("🎉 ALL TESTS PASSED - WEBSITE IS READY!")
    else:
        print_warning(f"⚠️  {failed_tests} TEST(S) NEED ATTENTION")
        print("\nRecommendations:")
        if "Links" in all_results and not all_results["Links"].get("passed"):
            print("  - Fix broken links")
        if "Images" in all_results and not all_results["Images"].get("passed"):
            print("  - Add missing images")
        if "Mobile" in all_results and not all_results["Mobile"].get("passed"):
            print("  - Improve mobile responsiveness")
    
    print("=" * 70)

def main():
    """Run all website tests"""
    print_header("🧪 END-TO-END WEBSITE TEST")
    
    print_info("Testing website functionality, mobile responsiveness, and bugs...")
    print_info("This will verify all components are working correctly.\n")
    
    all_results = {}
    
    # Run all tests
    all_results["Structure"] = test_website_structure()
    all_results["HTML"] = test_html_validation()
    all_results["Links"] = test_links()
    all_results["Images"] = test_images()
    all_results["Mobile"] = test_mobile_responsiveness()
    all_results["JavaScript"] = test_javascript()
    all_results["CSS"] = test_css()
    all_results["Accessibility"] = test_accessibility()
    
    # Generate report
    generate_test_report(all_results)
    
    # Return exit code
    all_passed = all(r.get("passed", False) for r in all_results.values())
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

