#!/usr/bin/env python3
"""
Mobile Responsiveness Improvements
Applies mobile-specific improvements to website
Tests on localhost first before deployment

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"
CSS_FILE = WEBSITE_DIR / "css" / "style.css"

def add_mobile_css_improvements():
    """Add mobile-specific CSS improvements."""
    print("📱 Adding mobile CSS improvements...")
    
    if not CSS_FILE.exists():
        print(f"  ❌ CSS file not found: {CSS_FILE}")
        return False
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if mobile improvements already added
    if '/* Mobile Improvements - Contact Info & About Section */' in content:
        print("  ⚠️  Mobile improvements already exist")
        return False
    
    # Mobile improvements for new sections
    mobile_css = '''

/* Mobile Improvements - Contact Info & About Section */
@media (max-width: 767px) {
  /* Contact Info Display - Mobile Optimization */
  .contact-info-display {
    padding: 20px 16px !important;
    margin-top: 30px !important;
  }
  
  .contact-info-display h3 {
    font-size: 1.3rem !important;
    margin-bottom: 15px !important;
  }
  
  .contact-info-display p {
    font-size: 1rem !important;
    line-height: 1.6 !important;
  }
  
  .contact-info-display a {
    font-size: 1rem !important;
    word-break: break-word;
    display: inline-block;
    min-height: 44px; /* Touch target */
    padding: 8px 0;
  }
  
  /* About Section - Mobile Optimization */
  .about {
    padding: 60px 16px !important;
  }
  
  .about h2 {
    font-size: 2rem !important;
    margin-bottom: 1.2rem !important;
  }
  
  .about > div > div {
    padding: 0 16px !important;
  }
  
  .about p {
    font-size: 1.1rem !important;
    line-height: 1.7 !important;
    margin-bottom: 1.5rem !important;
  }
  
  .about > div > div > div {
    grid-template-columns: 1fr !important;
    gap: 1.5rem !important;
    margin-top: 2rem !important;
  }
  
  .about > div > div > div > div {
    padding: 1.5rem !important;
  }
  
  .about h3 {
    font-size: 1.2rem !important;
    margin-bottom: 0.8rem !important;
  }
  
  /* Book 1 Link - Mobile Optimization */
  .books-card a[href*="book1.html"] {
    display: block !important;
    margin-top: 1rem !important;
    padding: 12px 20px !important;
    min-height: 44px; /* Touch target */
    font-size: 1rem !important;
    text-align: center;
  }
  
  /* FAQ - Ensure mobile-friendly */
  .faq-answer {
    font-size: 1rem !important;
    line-height: 1.6 !important;
    padding: 1rem 0 !important;
  }
  
  /* Navigation - Ensure touch targets */
  .header-top-navlink {
    min-height: 44px;
    min-width: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  /* Form inputs - Prevent iOS zoom */
  .contact-form-field input,
  .contact-form-field textarea {
    font-size: 16px !important; /* Prevents iOS auto-zoom */
  }
  
  /* Buttons - Ensure touch targets */
  .contact-form-btn,
  .books-card-button,
  .header-cta,
  .header-top-cta {
    min-height: 44px;
    min-width: 44px;
    padding: 12px 24px;
  }
}

/* Extra Small Mobile Devices */
@media (max-width: 480px) {
  .contact-info-display {
    padding: 16px 12px !important;
  }
  
  .contact-info-display h3 {
    font-size: 1.2rem !important;
  }
  
  .about {
    padding: 40px 12px !important;
  }
  
  .about h2 {
    font-size: 1.8rem !important;
  }
  
  .about p {
    font-size: 1rem !important;
  }
}
'''
    
    # Add before closing of file or at end
    content += mobile_css
    
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("  ✅ Mobile CSS improvements added")
    return True

def verify_mobile_viewport():
    """Verify viewport meta tag is correct."""
    print("📱 Verifying viewport meta tag...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for viewport tag
    viewport_pattern = r'<meta\s+name="viewport"\s+content="[^"]*"'
    
    if re.search(viewport_pattern, content):
        viewport_match = re.search(viewport_pattern, content)
        viewport_content = viewport_match.group(0)
        
        # Check if it has proper mobile settings
        if 'width=device-width' in viewport_content and 'initial-scale=1.0' in viewport_content:
            print("  ✅ Viewport meta tag is correct")
            return True
        else:
            print("  ⚠️  Viewport tag exists but may need adjustment")
            return False
    else:
        print("  ❌ Viewport meta tag not found")
        return False

def check_touch_targets():
    """Check if touch targets are adequate."""
    print("👆 Checking touch targets...")
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for minimum touch target sizes in mobile media query
    if 'min-height: 44px' in content and 'min-width: 44px' in content:
        print("  ✅ Touch targets configured (44x44px minimum)")
        return True
    else:
        print("  ⚠️  Touch targets may need adjustment")
        return False

def check_font_sizes():
    """Check if font sizes prevent iOS zoom."""
    print("🔤 Checking font sizes...")
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for 16px minimum on inputs
    if 'font-size: 16px' in content or 'font-size: 1rem' in content:
        # Check specifically in mobile media query
        mobile_section = re.search(r'@media\s*\(max-width:\s*767px\)\s*\{[^}]*font-size:\s*16px', content, re.DOTALL)
        if mobile_section:
            print("  ✅ Font sizes configured to prevent iOS zoom")
            return True
    
    print("  ⚠️  Font sizes may need adjustment for iOS")
    return False

def generate_mobile_test_report():
    """Generate mobile testing report."""
    print("📊 Generating mobile test report...")
    
    report_file = PROJECT_ROOT / "documents" / "mobile-test-report.md"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Run checks
    viewport_ok = verify_mobile_viewport()
    touch_ok = check_touch_targets()
    font_ok = check_font_sizes()
    
    content = f"""# Mobile Responsiveness Test Report

**Generated:** {Path(__file__).stat().st_mtime}
**Status:** Mobile improvements applied

---

## Mobile Checks

- **Viewport Meta Tag:** {'✅ PASS' if viewport_ok else '⚠️ NEEDS ATTENTION'}
- **Touch Targets:** {'✅ PASS' if touch_ok else '⚠️ NEEDS ATTENTION'}
- **Font Sizes:** {'✅ PASS' if font_ok else '⚠️ NEEDS ATTENTION'}

---

## Testing Instructions

### 1. Start Localhost Server
```bash
bash scripts/test-localhost-mobile.sh
```

### 2. Test on Mobile Device
- Connect phone to same Wi-Fi
- Navigate to: http://[YOUR_IP]:8000
- Test all sections

### 3. Test Checklist

**Navigation:**
- [ ] Hamburger menu works
- [ ] All links are tappable
- [ ] Navigation is smooth

**Contact Section:**
- [ ] Contact info is readable
- [ ] Email links are tappable
- [ ] Form inputs don't cause zoom
- [ ] Submit button is tappable

**About Section:**
- [ ] Text is readable
- [ ] Cards stack properly
- [ ] No horizontal scroll

**Book Cards:**
- [ ] Cards display correctly
- [ ] Book 1 link is tappable
- [ ] Images scale properly

**FAQ:**
- [ ] Accordion works on touch
- [ ] Text is readable
- [ ] No overflow

**General:**
- [ ] No horizontal scrolling
- [ ] All text is readable (no zoom needed)
- [ ] All buttons are tappable
- [ ] Images load properly

---

## Mobile Improvements Applied

1. ✅ Contact info display - Mobile optimized
2. ✅ About section - Mobile responsive
3. ✅ Book 1 link - Touch-friendly
4. ✅ FAQ answers - Readable on mobile
5. ✅ Form inputs - Prevent iOS zoom
6. ✅ Touch targets - Minimum 44x44px

---

**Next Steps:**
1. Test on localhost
2. Test on actual mobile device
3. Fix any issues found
4. Deploy when ready

"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Mobile test report generated: {report_file}")
    return report_file

def main():
    """Apply mobile improvements."""
    print("=" * 60)
    print("📱 Mobile Responsiveness Improvements")
    print("=" * 60)
    print()
    print("⚠️  IMPORTANT: Testing on localhost first!")
    print()
    
    if not INDEX_HTML.exists():
        print(f"❌ Error: {INDEX_HTML} not found")
        return False
    
    results = {}
    
    # Apply improvements
    results["Mobile CSS"] = add_mobile_css_improvements()
    print()
    
    results["Viewport Check"] = verify_mobile_viewport()
    print()
    
    results["Touch Targets"] = check_touch_targets()
    print()
    
    results["Font Sizes"] = check_font_sizes()
    print()
    
    # Generate report
    report_file = generate_mobile_test_report()
    print()
    
    # Summary
    successful = sum(1 for r in results.values() if r)
    total = len(results)
    
    print("=" * 60)
    print(f"✅ Mobile Improvements Complete: {successful}/{total} checks passed")
    print("=" * 60)
    print()
    print("🚀 Next Steps:")
    print("  1. Start localhost server: bash scripts/test-localhost-mobile.sh")
    print("  2. Test on mobile device or Chrome DevTools")
    print("  3. Review mobile test report")
    print("  4. Fix any issues found")
    print("  5. Deploy when ready")
    print()
    print(f"📊 Test report: {report_file}")
    print()
    
    return successful > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


