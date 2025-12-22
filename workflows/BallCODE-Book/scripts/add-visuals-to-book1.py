#!/usr/bin/env python3
"""
Add Visual Assets to Book 1 Page
Automates adding generated visual assets to the Book 1 page

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"
ASSETS_DIR = WEBSITE_DIR / "assets" / "images"

# Expected visual asset files
VISUAL_ASSETS = {
    "court_map": {
        "filename": "episode1-court-map-v1.png",
        "alt": "Basketball court center circle with tech elements",
        "description": "Court Map showing the center circle area with integrated tech elements"
    },
    "shadow_press_scouts": {
        "filename": "episode1-shadow-press-scouts-v1.png",
        "alt": "Shadow Press Scouts character art",
        "description": "Character design for the Shadow Press Scouts team"
    },
    "state_diagram": {
        "filename": "episode1-state-diagram-v1.png",
        "alt": "Basketball possession state diagram",
        "description": "Visual representation of possession state transitions"
    }
}

def check_assets_exist():
    """Check if visual assets exist."""
    print("🔍 Checking for visual assets...")
    
    existing = []
    missing = []
    
    for key, asset in VISUAL_ASSETS.items():
        asset_path = ASSETS_DIR / asset["filename"]
        if asset_path.exists():
            existing.append(key)
            print(f"  ✅ Found: {asset['filename']}")
        else:
            missing.append(key)
            print(f"  ❌ Missing: {asset['filename']}")
    
    return existing, missing

def add_visual_to_book1(asset_key, asset_info):
    """Add a visual asset to Book 1 page."""
    print(f"📸 Adding {asset_key} to Book 1 page...")
    
    if not BOOK1_HTML.exists():
        print(f"  ❌ Book 1 page not found: {BOOK1_HTML}")
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if asset already added
    if asset_info["filename"] in content:
        print(f"  ⚠️  {asset_info['filename']} already in page")
        return True
    
    # Create image HTML
    image_html = f'''
            <div class="visual-asset" style="margin: 2rem 0; text-align: center;">
              <img src="/assets/images/{asset_info['filename']}" 
                   alt="{asset_info['alt']}" 
                   style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
              <p style="margin-top: 1rem; color: #666; font-size: 0.9rem;">
                {asset_info['description']}
              </p>
            </div>
'''
    
    # Try to insert after first story section or before exercise section
    insertion_points = [
        (r'(<div class="story-section">.*?</div>)', r'\1' + image_html),
        (r'(<div class="exercise-section">)', image_html + r'\1'),
        (r'(<h2>🎮 Try the Exercise</h2>)', image_html + r'\1'),
    ]
    
    inserted = False
    for pattern, replacement in insertion_points:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
            print(f"  ✅ Added {asset_key} to Book 1 page")
            inserted = True
            break
    
    if not inserted:
        # Add at end of main content
        if '</main>' in content:
            content = content.replace('</main>', image_html + '</main>')
            print(f"  ✅ Added {asset_key} to end of page")
            inserted = True
    
    if inserted:
        with open(BOOK1_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"  ❌ Could not find insertion point for {asset_key}")
        return False

def main():
    """Add visual assets to Book 1 page."""
    print("=" * 60)
    print("🎨 Add Visual Assets to Book 1 Page")
    print("=" * 60)
    print()
    
    # Check if assets exist
    existing, missing = check_assets_exist()
    
    if not existing:
        print()
        print("❌ No visual assets found!")
        print()
        print("📋 Expected files:")
        for key, asset in VISUAL_ASSETS.items():
            print(f"  - {asset['filename']}")
        print()
        print("🚀 Next Steps:")
        print("  1. Generate visual assets using prompts in documents/visual-assets/")
        print("  2. Save assets to BallCode/assets/images/")
        print("  3. Run this script again")
        print()
        return False
    
    if missing:
        print()
        print(f"⚠️  {len(missing)} asset(s) missing:")
        for key in missing:
            print(f"  - {VISUAL_ASSETS[key]['filename']}")
        print()
        print("You can still add the existing assets now, and add missing ones later.")
        print()
    
    # Add existing assets
    print()
    print("📝 Adding assets to Book 1 page...")
    print()
    
    added = 0
    for key in existing:
        if add_visual_to_book1(key, VISUAL_ASSETS[key]):
            added += 1
        print()
    
    print("=" * 60)
    if added == len(existing):
        print("✅ All existing assets added to Book 1 page!")
    else:
        print(f"⚠️  Added {added}/{len(existing)} assets")
    print("=" * 60)
    print()
    
    if missing:
        print("📋 Missing assets:")
        for key in missing:
            print(f"  - {VISUAL_ASSETS[key]['filename']}")
        print()
        print("Once these are generated, run this script again to add them.")
        print()
    
    print("🚀 Next Steps:")
    print("  1. Review Book 1 page: BallCode/books/book1.html")
    print("  2. Test locally: cd BallCode && python3 -m http.server")
    print("  3. Verify visuals display correctly")
    print("  4. Deploy when ready")
    print()
    
    return added > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

