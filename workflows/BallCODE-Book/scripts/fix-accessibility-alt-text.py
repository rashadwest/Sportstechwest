#!/usr/bin/env python3
"""
Fix Accessibility - Add Alt Text to Images
Automatically adds alt text to images missing it in book1.html

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
BOOK1_HTML = PROJECT_ROOT / "BallCode" / "books" / "book1.html"

def fix_alt_text():
    """Add alt text to images missing it."""
    if not BOOK1_HTML.exists():
        print(f"❌ File not found: {BOOK1_HTML}")
        return False
    
    # Read the file
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all img tags
    img_pattern = r'<img([^>]+)>'
    images = re.findall(img_pattern, content, re.IGNORECASE)
    
    if not images:
        print("✅ No images found in book1.html")
        print("   The accessibility issue may be from background images or other elements.")
        return True
    
    # Check each image
    fixed_count = 0
    for img_attrs in images:
        # Check if alt attribute exists
        if 'alt=' not in img_attrs.lower():
            # Try to extract src to create meaningful alt text
            src_match = re.search(r'src=["\']([^"\']+)["\']', img_attrs, re.IGNORECASE)
            if src_match:
                src = src_match.group(1)
                # Create alt text from filename
                filename = Path(src).stem
                # Generate descriptive alt text
                alt_text = filename.replace('-', ' ').replace('_', ' ').title()
                
                # Add alt attribute
                new_attrs = img_attrs.rstrip() + f' alt="{alt_text}"'
                content = content.replace(f'<img{img_attrs}>', f'<img{new_attrs}>')
                fixed_count += 1
                print(f"✅ Added alt text: {alt_text}")
    
    if fixed_count > 0:
        # Write back
        with open(BOOK1_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Fixed {fixed_count} image(s) with missing alt text")
        return True
    else:
        print("✅ All images already have alt text")
        return True

if __name__ == "__main__":
    print("=" * 70)
    print("FIXING ACCESSIBILITY - ADDING ALT TEXT")
    print("=" * 70)
    print()
    fix_alt_text()
    print()
    print("=" * 70)
    print("✅ DONE!")
    print("=" * 70)


