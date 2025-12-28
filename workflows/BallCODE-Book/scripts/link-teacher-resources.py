#!/usr/bin/env python3
"""
Link Teacher Resources Page
Adds teacher resources link to main website navigation

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"
TEACHER_PAGE = WEBSITE_DIR / "teachers" / "index.html"

def add_teacher_resources_link():
    """Add teacher resources link to navigation."""
    if not INDEX_HTML.exists():
        print(f"❌ Homepage not found: {INDEX_HTML}")
        return False
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if link already exists
    if 'teachers' in content.lower() and ('href="/teachers' in content or 'href="teachers' in content):
        print("⚠️  Teacher resources link already exists")
        return True
    
    # Find navigation menu
    # Look for nav, header, or menu sections
    nav_patterns = [
        r'(<nav[^>]*>.*?</nav>)',
        r'(<header[^>]*>.*?</header>)',
        r'(<div[^>]*class="[^"]*nav[^"]*"[^>]*>.*?</div>)',
        r'(<ul[^>]*class="[^"]*nav[^"]*"[^>]*>.*?</ul>)'
    ]
    
    teacher_link = '<li><a href="/teachers/">Teachers</a></li>'
    
    # Try to find existing navigation and add link
    added = False
    
    # Pattern 1: Find <nav> with <ul> inside
    nav_ul_pattern = r'(<nav[^>]*>.*?<ul[^>]*>)(.*?)(</ul>.*?</nav>)'
    match = re.search(nav_ul_pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        nav_start = match.group(1)
        nav_content = match.group(2)
        nav_end = match.group(3)
        
        # Add link before closing </ul>
        if 'teachers' not in nav_content.lower():
            new_nav_content = nav_content.rstrip() + '\n        ' + teacher_link + '\n      '
            content = content.replace(match.group(0), nav_start + new_nav_content + nav_end)
            added = True
            print("✅ Added teacher resources link to navigation")
    
    # Pattern 2: Find header with links
    if not added:
        header_link_pattern = r'(<header[^>]*>.*?)(<a[^>]*href="[^"]*"[^>]*>.*?</a>)(.*?</header>)'
        match = re.search(header_link_pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            # Add link after existing links
            before = match.group(1)
            existing_link = match.group(2)
            after = match.group(3)
            
            if 'teachers' not in content.lower():
                new_link = f'\n        <a href="/teachers/">Teachers</a>'
                content = content.replace(match.group(0), before + existing_link + new_link + after)
                added = True
                print("✅ Added teacher resources link to header")
    
    # Pattern 3: Find About/Contact links and add nearby
    if not added:
        about_contact_pattern = r'(<a[^>]*href="[^"]*about[^"]*"[^>]*>.*?</a>.*?)(<a[^>]*href="[^"]*contact[^"]*"[^>]*>.*?</a>)'
        match = re.search(about_contact_pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            before = match.group(1)
            contact_link = match.group(2)
            
            if 'teachers' not in content.lower():
                teacher_link_html = f'\n        <a href="/teachers/">Teachers</a>'
                content = content.replace(match.group(0), before + teacher_link_html + '\n        ' + contact_link)
                added = True
                print("✅ Added teacher resources link near About/Contact")
    
    # Pattern 4: Add to footer if navigation not found
    if not added:
        footer_pattern = r'(<footer[^>]*>.*?)(</footer>)'
        match = re.search(footer_pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            footer_content = match.group(1)
            footer_end = match.group(2)
            
            if 'teachers' not in content.lower():
                teacher_link_html = f'\n        <a href="/teachers/">Teacher Resources</a>'
                content = content.replace(match.group(0), footer_content + teacher_link_html + '\n      ' + footer_end)
                added = True
                print("✅ Added teacher resources link to footer")
    
    # Pattern 5: Add before closing </body> as last resort
    if not added:
        if '</body>' in content and 'teachers' not in content.lower():
            teacher_link_html = f'    <nav style="text-align: center; padding: 1rem;"><a href="/teachers/">Teacher Resources</a></nav>\n'
            content = content.replace('</body>', teacher_link_html + '</body>')
            added = True
            print("✅ Added teacher resources link before </body>")
    
    if added:
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print("⚠️  Could not find navigation section. Please add manually.")
        print("   Add this link: <a href=\"/teachers/\">Teachers</a>")
        return False

def verify_teacher_page():
    """Verify teacher resources page exists."""
    if TEACHER_PAGE.exists():
        print(f"✅ Teacher resources page exists: {TEACHER_PAGE}")
        return True
    else:
        print(f"⚠️  Teacher resources page not found: {TEACHER_PAGE}")
        print("   Run: python3 scripts/generate-teacher-package.py")
        return False

def main():
    """Main function."""
    print("=" * 60)
    print("🔗 Link Teacher Resources Page")
    print("=" * 60)
    print()
    
    # Verify teacher page exists
    verify_teacher_page()
    print()
    
    # Add link to navigation
    if add_teacher_resources_link():
        print()
        print("=" * 60)
        print("✅ Teacher Resources Link Added!")
        print("=" * 60)
        print()
        print("🚀 Next Steps:")
        print("  1. Test link: Open index.html and click 'Teachers'")
        print("  2. Verify teacher resources page loads")
        print("  3. Deploy changes to website")
        print()
        return True
    else:
        print()
        print("⚠️  Could not automatically add link")
        print("   Please add manually to navigation")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


