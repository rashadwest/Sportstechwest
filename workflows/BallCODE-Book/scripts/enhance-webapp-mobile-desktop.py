#!/usr/bin/env python3
"""
Enhance Website for Webapp Experience
Improves mobile/desktop responsiveness and webapp features

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"
CSS_FILE = WEBSITE_DIR / "css" / "style.css"

def enhance_webapp_meta_tags():
    """Add webapp meta tags for mobile app-like experience."""
    if not INDEX_HTML.exists():
        print("❌ Homepage not found")
        return False
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if webapp meta tags already exist
    if 'apple-mobile-web-app-capable' in content and 'manifest' in content:
        print("⚠️  Webapp meta tags already exist")
        return True
    
    # Enhanced webapp meta tags
    webapp_meta = """
    <!-- Webapp Meta Tags -->
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="apple-mobile-web-app-title" content="BallCODE" />
    <meta name="theme-color" content="#0C72B3" />
    <meta name="msapplication-TileColor" content="#0C72B3" />
    <meta name="msapplication-navbutton-color" content="#0C72B3" />
    <link rel="manifest" href="/manifest.json" />
    <link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png" />
"""
    
    # Insert after viewport meta tag
    if '<meta name="viewport"' in content:
        content = content.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes" />' + webapp_meta
        )
        print("✅ Added webapp meta tags")
    else:
        # Add in head section
        if '</head>' in content:
            content = content.replace('</head>', webapp_meta + '</head>')
            print("✅ Added webapp meta tags to head")
    
    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def create_webapp_manifest():
    """Create webapp manifest.json."""
    manifest = {
        "name": "BallCODE - Coding Through Basketball",
        "short_name": "BallCODE",
        "description": "Learn coding through basketball stories and interactive games",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#00061a",
        "theme_color": "#0C72B3",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "/assets/images/icon-192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/assets/images/icon-512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ],
        "categories": ["education", "games", "learning"],
        "screenshots": [
            {
                "src": "/assets/images/screenshot-mobile.png",
                "sizes": "540x720",
                "type": "image/png",
                "form_factor": "narrow"
            },
            {
                "src": "/assets/images/screenshot-desktop.png",
                "sizes": "1280x720",
                "type": "image/png",
                "form_factor": "wide"
            }
        ]
    }
    
    import json
    manifest_file = WEBSITE_DIR / "manifest.json"
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Created: {manifest_file}")
    return manifest_file

def enhance_mobile_responsiveness():
    """Enhance mobile responsiveness in CSS."""
    if not CSS_FILE.exists():
        print("❌ CSS file not found")
        return False
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if webapp enhancements already exist
    if '/* Webapp Enhancements */' in content:
        print("⚠️  Webapp enhancements may already exist")
        # Continue to add more if needed
    
    # Enhanced mobile/desktop CSS
    webapp_css = """
/* ============================================
   WEBAPP ENHANCEMENTS - Mobile & Desktop
   ============================================ */

/* Prevent horizontal scroll on all devices */
html, body {
    overflow-x: hidden;
    width: 100%;
    max-width: 100vw;
}

/* Smooth scrolling for webapp feel */
html {
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
}

/* Webapp container improvements */
body {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
}

/* Touch-friendly interactions */
a, button, .header-top-navlink, .header-top-cta {
    -webkit-tap-highlight-color: rgba(12, 114, 179, 0.3);
    touch-action: manipulation;
}

/* Prevent text size adjustment on iOS */
@media screen and (max-width: 767px) {
    input, textarea, select {
        font-size: 16px !important; /* Prevents iOS zoom on focus */
    }
}

/* Webapp-like header on mobile */
@media (max-width: 767px) {
    .header-top {
        position: sticky;
        top: 0;
        z-index: 1000;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    /* Better mobile navigation */
    .header-top-navbar {
        position: fixed;
        top: 77px;
        left: 0;
        right: 0;
        background: rgba(0, 6, 26, 0.95);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 1rem;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
        z-index: 999;
    }
    
    .header-top-navbar.active {
        transform: translateX(0);
    }
}

/* Desktop webapp improvements */
@media (min-width: 768px) {
    /* Smooth transitions */
    * {
        transition: all 0.3s ease;
    }
    
    /* Hover effects for desktop */
    .header-top-navlink:hover,
    .header-top-cta:hover,
    .books-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(12, 114, 179, 0.3);
    }
}

/* Responsive images for webapp */
img {
    height: auto;
    max-width: 100%;
    object-fit: cover;
}

/* Webapp-safe area for notched devices */
@supports (padding: max(0px)) {
    .header-top {
        padding-left: max(16px, env(safe-area-inset-left));
        padding-right: max(16px, env(safe-area-inset-right));
    }
    
    body {
        padding-bottom: max(0px, env(safe-area-inset-bottom));
    }
}

/* Better form inputs for webapp */
input, textarea, select {
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
    -webkit-appearance: none;
    appearance: none;
}

/* Webapp button improvements */
button, .header-top-cta, .try-exercise-button {
    min-height: 44px; /* iOS touch target */
    min-width: 44px;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    user-select: none;
    -webkit-user-select: none;
}

/* Loading states for webapp */
.loading {
    opacity: 0.6;
    pointer-events: none;
}

/* Webapp container max-width */
.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 20px;
}

@media (max-width: 767px) {
    .container {
        padding: 0 16px;
    }
}

/* Webapp card improvements */
.books-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    will-change: transform;
}

.books-card:active {
    transform: scale(0.98);
}

/* Better spacing for webapp */
section {
    padding: 4rem 0;
}

@media (max-width: 767px) {
    section {
        padding: 2rem 0;
    }
}

/* Webapp typography */
h1, h2, h3 {
    line-height: 1.2;
    margin-bottom: 1rem;
}

p {
    line-height: 1.6;
    margin-bottom: 1rem;
}

/* Webapp grid improvements */
.books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

@media (max-width: 767px) {
    .books-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
}

/* Webapp footer improvements */
footer {
    margin-top: 4rem;
    padding: 2rem 0;
}

/* Print styles for webapp */
@media print {
    .header-top,
    .header-hamburger-btn,
    footer {
        display: none;
    }
}
"""
    
    # Append to end of CSS file
    if webapp_css.strip() not in content:
        if not content.endswith('\n'):
            content += '\n'
        content += webapp_css
        
        with open(CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Enhanced CSS with webapp improvements")
        return True
    else:
        print("⚠️  Webapp CSS may already exist")
        return True

def enhance_book1_mobile():
    """Enhance Book 1 page for mobile/desktop."""
    book1_file = WEBSITE_DIR / "books" / "book1.html"
    
    if not book1_file.exists():
        print("⚠️  Book 1 page not found")
        return False
    
    with open(book1_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Enhanced mobile styles for Book 1
    mobile_css = """
        /* Mobile optimizations for Book 1 */
        @media (max-width: 767px) {
            .book-container {
                padding: 1rem;
            }
            
            .book-title {
                font-size: 1.8rem;
            }
            
            .book-subtitle {
                font-size: 1rem;
            }
            
            .book-video {
                width: 100%;
                height: auto;
            }
            
            .exercise-section {
                padding: 1.5rem;
                margin: 2rem 0;
            }
            
            .try-exercise-button {
                width: 100%;
                padding: 1rem;
                font-size: 1.1rem;
            }
            
            #curriculum-section {
                padding: 1.5rem;
            }
            
            #progress-display {
                padding: 1rem;
            }
        }
        
        /* Desktop improvements */
        @media (min-width: 768px) {
            .book-container {
                max-width: 1200px;
            }
            
            .book-content {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 2rem;
            }
        }
"""
    
    # Check if mobile CSS already in style tag
    if '/* Mobile optimizations for Book 1 */' in content:
        print("⚠️  Book 1 mobile CSS already exists")
        return True
    
    # Add to existing style tag or create new one
    if '<style>' in content and '</style>' in content:
        # Add to existing style tag
        style_pattern = r'(<style>.*?)(</style>)'
        match = re.search(style_pattern, content, re.DOTALL)
        if match:
            style_content = match.group(1)
            style_end = match.group(2)
            content = content.replace(match.group(0), style_content + mobile_css + '\n    ' + style_end)
            print("✅ Enhanced Book 1 mobile/desktop styles")
    else:
        # Add new style tag
        if '</head>' in content:
            content = content.replace('</head>', f'    <style>{mobile_css}\n    </style>\n</head>')
            print("✅ Added Book 1 mobile/desktop styles")
    
    with open(book1_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def create_localhost_test_script():
    """Create localhost testing script."""
    script_content = """#!/bin/bash
# Localhost Testing Script for BallCODE
# Tests website on localhost with mobile/desktop preview

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEBSITE_DIR="$PROJECT_ROOT/BallCode"

cd "$WEBSITE_DIR"

echo "============================================================"
echo "🌐 BallCODE Localhost Testing"
echo "============================================================"
echo ""

# Get local IP address
LOCAL_IP=$(ipconfig getifaddr en0 2>/dev/null || ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

if [ -z "$LOCAL_IP" ]; then
    LOCAL_IP="localhost"
fi

echo "📱 Testing Instructions:"
echo ""
echo "1. Desktop Testing:"
echo "   Open: http://localhost:8000"
echo "   Or:   http://$LOCAL_IP:8000"
echo ""
echo "2. Mobile Testing (Same Network):"
echo "   Open on your phone: http://$LOCAL_IP:8000"
echo ""
echo "3. Chrome DevTools Mobile:"
echo "   - Press F12 or Cmd+Option+I"
echo "   - Click device toolbar icon"
echo "   - Test different device sizes"
echo ""
echo "4. Testing Checklist:"
echo "   [ ] Homepage loads correctly"
echo "   [ ] Navigation works"
echo "   [ ] Book 1 page accessible"
echo "   [ ] Exercise button works"
echo "   [ ] Mobile menu works"
echo "   [ ] Forms work on mobile"
echo "   [ ] Touch targets are 44px+"
echo "   [ ] No horizontal scroll"
echo "   [ ] Text is readable"
echo "   [ ] Images load properly"
echo ""

echo "🚀 Starting local server..."
echo "   Press Ctrl+C to stop"
echo ""

# Start Python HTTP server
python3 -m http.server 8000
"""
    
    script_file = PROJECT_ROOT / "scripts" / "test-localhost-webapp.sh"
    with open(script_file, 'w') as f:
        f.write(script_content)
    
    import os
    os.chmod(script_file, 0o755)
    
    print(f"✅ Created: {script_file}")
    return script_file

def create_webapp_testing_guide():
    """Create webapp testing guide."""
    guide_content = """# Webapp Testing Guide - Mobile & Desktop

**Purpose:** Test BallCODE website as a webapp on localhost

---

## 🚀 Quick Start

### Start Localhost Server:
```bash
cd BallCode
python3 -m http.server 8000
```

Or use the script:
```bash
bash scripts/test-localhost-webapp.sh
```

---

## 📱 Mobile Testing

### Option 1: Chrome DevTools (Recommended)
1. Open: http://localhost:8000
2. Press `F12` or `Cmd+Option+I` (Mac)
3. Click device toolbar icon (📱)
4. Select device:
   - iPhone 12/13/14
   - iPad
   - Galaxy S20
   - Custom size

### Option 2: Actual Mobile Device
1. Find your computer's IP:
   ```bash
   ipconfig getifaddr en0  # Mac
   ifconfig | grep "inet "  # Linux
   ```
2. On your phone (same WiFi):
   - Open: `http://[YOUR_IP]:8000`
   - Example: `http://192.168.1.100:8000`

### Option 3: ngrok (Public URL)
```bash
ngrok http 8000
```
- Get public URL
- Test on any device

---

## 🖥️ Desktop Testing

### Browser Testing:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### Screen Sizes:
- [ ] 1920x1080 (Full HD)
- [ ] 1366x768 (Common laptop)
- [ ] 1440x900 (MacBook)
- [ ] 2560x1440 (2K)

---

## ✅ Webapp Testing Checklist

### Mobile (iPhone/Android):
- [ ] Homepage loads correctly
- [ ] Navigation menu works (hamburger)
- [ ] Touch targets are 44px+ (easy to tap)
- [ ] No horizontal scroll
- [ ] Text is readable (16px+)
- [ ] Forms work (no zoom on focus)
- [ ] Images load properly
- [ ] Book 1 page accessible
- [ ] Exercise button works
- [ ] Can add to home screen (PWA)

### Desktop:
- [ ] Homepage looks good
- [ ] Navigation works
- [ ] Hover effects work
- [ ] Grid layouts correct
- [ ] Images display properly
- [ ] Forms work
- [ ] All links work

### Webapp Features:
- [ ] Can install as app (PWA)
- [ ] Works offline (if service worker)
- [ ] Fast loading
- [ ] Smooth scrolling
- [ ] No layout shifts

---

## 🐛 Common Issues to Check

### Mobile:
1. **Horizontal Scroll:**
   - Check: `overflow-x: hidden` on html/body
   - Fix: Add to CSS

2. **Text Too Small:**
   - Check: Font size < 16px
   - Fix: Increase to 16px+

3. **Touch Targets Too Small:**
   - Check: Buttons < 44x44px
   - Fix: Increase min-height/width

4. **iOS Zoom on Input:**
   - Check: Input font-size < 16px
   - Fix: Set to 16px

5. **Menu Not Working:**
   - Check: JavaScript enabled
   - Fix: Check console for errors

### Desktop:
1. **Layout Breaks:**
   - Check: Max-width on containers
   - Fix: Adjust container widths

2. **Images Not Loading:**
   - Check: File paths correct
   - Fix: Use relative paths

3. **Hover Effects Not Working:**
   - Check: CSS hover rules
   - Fix: Add hover states

---

## 📊 Performance Testing

### Tools:
- Chrome DevTools Lighthouse
- PageSpeed Insights
- WebPageTest

### Metrics to Check:
- [ ] First Contentful Paint < 1.8s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Time to Interactive < 3.8s
- [ ] Cumulative Layout Shift < 0.1

---

## 🎯 Webapp-Specific Tests

### PWA Features:
- [ ] Manifest.json exists
- [ ] Icons available (192x192, 512x512)
- [ ] Can install as app
- [ ] Theme color correct
- [ ] Works in standalone mode

### Mobile App Feel:
- [ ] Smooth scrolling
- [ ] Touch-friendly interactions
- [ ] No browser chrome (when installed)
- [ ] Fast page transitions
- [ ] Responsive to orientation changes

---

## 🚀 Next Steps After Testing

1. **Fix Issues Found:**
   - Update CSS for mobile
   - Fix JavaScript errors
   - Optimize images
   - Improve performance

2. **Deploy to Production:**
   - Test on production URL
   - Verify all features work
   - Check analytics

3. **Monitor:**
   - Track user behavior
   - Monitor performance
   - Collect feedback

---

**Happy Testing! 🎉**

---

*Generated: December 16, 2025*
"""
    
    guide_file = PROJECT_ROOT / "documents" / "webapp-testing-guide.md"
    guide_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(guide_file, 'w') as f:
        f.write(guide_content)
    
    print(f"✅ Created: {guide_file}")
    return guide_file

def main():
    """Main function."""
    print("=" * 60)
    print("📱 Webapp Enhancement - Mobile & Desktop")
    print("=" * 60)
    print()
    
    print("🏷️  Adding webapp meta tags...")
    enhance_webapp_meta_tags()
    print()
    
    print("📄 Creating webapp manifest...")
    create_webapp_manifest()
    print()
    
    print("🎨 Enhancing mobile/desktop CSS...")
    enhance_mobile_responsiveness()
    print()
    
    print("📖 Enhancing Book 1 mobile/desktop...")
    enhance_book1_mobile()
    print()
    
    print("🧪 Creating localhost test script...")
    create_localhost_test_script()
    print()
    
    print("📚 Creating testing guide...")
    create_webapp_testing_guide()
    print()
    
    print("=" * 60)
    print("✅ Webapp Enhancement Complete!")
    print("=" * 60)
    print()
    
    print("🚀 Next Steps:")
    print("  1. Test on localhost: bash scripts/test-localhost-webapp.sh")
    print("  2. Open: http://localhost:8000")
    print("  3. Test on mobile device (same WiFi)")
    print("  4. Use Chrome DevTools for mobile preview")
    print("  5. Check webapp-testing-guide.md for checklist")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

