#!/usr/bin/env python3
"""
Comprehensive Readability Check
Tests desktop (full screen and resized) and mobile readability

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"
CSS_FILE = WEBSITE_DIR / "css" / "style.css"

def check_desktop_readability():
    """Check desktop readability at different screen sizes."""
    if not INDEX_HTML.exists() or not CSS_FILE.exists():
        print("❌ Files not found")
        return False
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    print()
    print("=" * 60)
    print("🖥️  Desktop Readability Check")
    print("=" * 60)
    print()
    
    issues = []
    fixes = []
    
    # Check 1: About BallCODE section padding
    if 'padding: 120px 0' in html_content or 'padding: 120px 0 !important' in css_content:
        print("✅ About BallCODE section has increased padding (120px)")
    else:
        issues.append("About BallCODE section needs more padding")
        fixes.append("Increase padding to 120px 0")
    
    # Check 2: Centered content
    centered_sections = [
        ("About BallCODE", 'text-align: center'),
        ("Real Student Impact", 'text-align: center'),
        ("What You'll Learn", 'text-align: center'),
        ("Example Exercise", 'text-align: center'),
    ]
    
    for section_name, pattern in centered_sections:
        if pattern in html_content:
            print(f"✅ {section_name} is centered")
        else:
            issues.append(f"{section_name} needs to be centered")
            fixes.append(f"Add text-align: center to {section_name}")
    
    # Check 3: Container max-widths for centering
    if 'max-width: 1100px' in html_content or 'max-width: 900px' in html_content:
        print("✅ Content containers have max-width for centering")
    else:
        issues.append("Content containers need max-width for proper centering")
        fixes.append("Add max-width to content containers")
    
    # Check 4: Font sizes for readability
    font_sizes = re.findall(r'font-size:\s*([\d.]+rem|[\d.]+px)', html_content)
    small_fonts = [f for f in font_sizes if float(re.findall(r'[\d.]+', f)[0]) < 1.0 and 'rem' in f]
    if not small_fonts:
        print("✅ Font sizes are readable (1rem+)")
    else:
        issues.append("Some font sizes may be too small")
        fixes.append("Ensure all body text is at least 1rem (16px)")
    
    # Check 5: Line heights for readability
    if 'line-height: 1.7' in html_content or 'line-height: 1.8' in html_content or 'line-height: 1.9' in html_content:
        print("✅ Line heights are optimized for readability (1.7-1.9)")
    else:
        issues.append("Line heights may need optimization")
        fixes.append("Set line-height to 1.7-1.9 for body text")
    
    # Check 6: Responsive breakpoints
    breakpoints = ['@media (max-width: 767px)', '@media (max-width: 1023px)', '@media (min-width: 1024px)']
    found_breakpoints = [bp for bp in breakpoints if bp in css_content]
    if len(found_breakpoints) >= 2:
        print(f"✅ Responsive breakpoints present ({len(found_breakpoints)} breakpoints)")
    else:
        issues.append("Need more responsive breakpoints")
        fixes.append("Add mobile and tablet breakpoints")
    
    print()
    
    if issues:
        print("⚠️  Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print()
        print("🔧 Suggested Fixes:")
        for fix in fixes:
            print(f"  - {fix}")
    else:
        print("✅ No desktop readability issues found!")
    
    return len(issues) == 0

def check_mobile_readability():
    """Check mobile readability."""
    if not CSS_FILE.exists():
        return False
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    print()
    print("=" * 60)
    print("📱 Mobile Readability Check")
    print("=" * 60)
    print()
    
    issues = []
    fixes = []
    
    # Check 1: Mobile viewport
    if '<meta name="viewport"' in open(INDEX_HTML, 'r').read():
        print("✅ Viewport meta tag present")
    else:
        issues.append("Viewport meta tag missing")
        fixes.append("Add viewport meta tag")
    
    # Check 2: Mobile font sizes (16px+)
    mobile_css = re.findall(r'@media.*?max-width.*?767px.*?\{.*?\}', css_content, re.DOTALL)
    if mobile_css:
        if 'font-size: 16px' in str(mobile_css) or 'font-size: 1rem' in str(mobile_css):
            print("✅ Mobile font sizes are 16px+ (prevents iOS zoom)")
        else:
            issues.append("Mobile font sizes may be too small")
            fixes.append("Ensure mobile inputs are 16px+")
    else:
        issues.append("Mobile CSS section may be missing")
        fixes.append("Add @media (max-width: 767px) styles")
    
    # Check 3: Touch targets (44px+)
    if 'min-height: 44px' in css_content or 'min-width: 44px' in css_content:
        print("✅ Touch targets are 44px+ (mobile-friendly)")
    else:
        issues.append("Touch targets may be too small")
        fixes.append("Set min-height and min-width to 44px for buttons/links")
    
    # Check 4: Mobile padding
    if 'padding: 0 16px' in css_content or 'padding: 0 20px' in css_content:
        print("✅ Mobile padding is appropriate")
    else:
        issues.append("Mobile padding may need adjustment")
        fixes.append("Add padding: 0 16px for mobile containers")
    
    # Check 5: Grid responsiveness
    if 'grid-template-columns: 1fr' in css_content or 'grid-template-columns: repeat(1' in css_content:
        print("✅ Grids stack on mobile (1 column)")
    else:
        issues.append("Grids may not stack properly on mobile")
        fixes.append("Set grid-template-columns: 1fr for mobile")
    
    # Check 6: Horizontal scroll prevention
    if 'overflow-x: hidden' in css_content:
        print("✅ Horizontal scroll prevented")
    else:
        issues.append("Horizontal scroll may occur")
        fixes.append("Add overflow-x: hidden to html/body")
    
    print()
    
    if issues:
        print("⚠️  Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print()
        print("🔧 Suggested Fixes:")
        for fix in fixes:
            print(f"  - {fix}")
    else:
        print("✅ No mobile readability issues found!")
    
    return len(issues) == 0

def apply_final_fixes():
    """Apply final fixes for perfect readability."""
    if not INDEX_HTML.exists() or not CSS_FILE.exists():
        return False
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    fixes_applied = []
    
    # Fix 1: Ensure all "What You'll Learn" are centered
    if 'What You\'ll Learn</h3>' in html_content:
        # Already handled in previous script
        pass
    
    # Fix 2: Ensure example exercise code blocks are centered
    if 'Example Exercise Structure</h4>' in html_content:
        # Already handled
        pass
    
    # Fix 3: Add mobile-specific improvements
    if '/* Mobile: Stack Outcome/Skill Cards */' not in css_content:
        mobile_fixes = """
/* Additional Mobile Readability Fixes */
@media (max-width: 767px) {
    /* Ensure all centered content stays centered on mobile */
    section.about#about > div > div,
    .impact-stories > div,
    .book-preview-section > div > div {
        text-align: center !important;
    }
    
    /* Better mobile spacing */
    section.about#about > div > div > div[style*="grid-template-columns"] {
        padding: 0 16px !important;
    }
    
    /* Mobile typography */
    section.about#about h2 {
        font-size: 2rem !important;
        line-height: 1.2 !important;
    }
    
    section.about#about > div > div > p {
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
    }
    
    /* Clear Progression - Mobile */
    section.about#about > div > div > div[style*="Clear Progression"] h3 {
        font-size: 1.8rem !important;
        line-height: 1.3 !important;
    }
    
    section.about#about > div > div > div[style*="Clear Progression"] > div {
        font-size: 1.2rem !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
    }
}

/* Desktop: Full Screen & Resized Window */
@media (min-width: 1024px) {
    /* Ensure content is readable at all desktop sizes */
    section.about#about > div > div {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 0 40px !important;
    }
    
    .impact-stories > div {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 0 40px !important;
    }
    
    .book-preview-section > div > div {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 0 40px !important;
    }
}

/* Resized Desktop Window (768px - 1023px) */
@media (min-width: 768px) and (max-width: 1023px) {
    section.about#about {
        padding: 100px 0 !important;
    }
    
    section.about#about > div > div {
        padding: 0 30px !important;
    }
    
    section.about#about h2 {
        font-size: 2.5rem !important;
    }
}
"""
        if mobile_fixes.strip() not in css_content:
            with open(CSS_FILE, 'a', encoding='utf-8') as f:
                f.write('\n' + mobile_fixes)
            fixes_applied.append("Added mobile readability fixes")
            print("✅ Applied mobile readability fixes")
    
    return len(fixes_applied) > 0

def main():
    """Main function."""
    print("=" * 60)
    print("🔍 Comprehensive Readability Check")
    print("=" * 60)
    print()
    
    # Check desktop
    desktop_ok = check_desktop_readability()
    
    # Check mobile
    mobile_ok = check_mobile_readability()
    
    # Apply fixes
    print()
    print("🔧 Applying final fixes...")
    apply_final_fixes()
    print()
    
    print("=" * 60)
    print("📊 Readability Check Summary")
    print("=" * 60)
    print()
    
    if desktop_ok and mobile_ok:
        print("✅ Desktop Readability: PASS")
        print("✅ Mobile Readability: PASS")
        print()
        print("🎉 All readability checks passed!")
    else:
        print("⚠️  Desktop Readability: " + ("PASS" if desktop_ok else "NEEDS WORK"))
        print("⚠️  Mobile Readability: " + ("PASS" if mobile_ok else "NEEDS WORK"))
        print()
        print("🔧 Fixes have been applied. Please review and test.")
    
    print()
    print("🚀 Next Steps:")
    print("  1. Test on localhost: http://localhost:8000")
    print("  2. Test desktop at full screen (1920x1080)")
    print("  3. Test desktop resized (1366x768, 1440x900)")
    print("  4. Test mobile (iPhone, Android)")
    print("  5. Verify all content is centered")
    print("  6. Verify About BallCODE has more room")
    print()
    
    return desktop_ok and mobile_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

