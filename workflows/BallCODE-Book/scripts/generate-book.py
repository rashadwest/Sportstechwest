#!/usr/bin/env python3
"""
Book Template Generator
Generates new book page from template

Usage: python3 generate-book.py <book_number> <title>
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATE_FILE = PROJECT_ROOT / "templates" / "book-template.html"
OUTPUT_DIR = PROJECT_ROOT / "BallCode" / "books"

def generate_book_page(book_number, title, slug):
    """Generate book page from template."""
    if not TEMPLATE_FILE.exists():
        print(f"❌ Template not found: {TEMPLATE_FILE}")
        return False
    
    with open(TEMPLATE_FILE, 'r') as f:
        template = f.read()
    
    # Replace placeholders
    content = template.replace('{{BOOK_NUMBER}}', str(book_number))
    content = content.replace('{{BOOK_TITLE}}', title)
    content = content.replace('{{BOOK_SLUG}}', slug)
    content = content.replace('{{BOOK_ID}}', str(book_number))
    
    # Save to output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"book{book_number}.html"
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Generated: {output_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate-book.py <book_number> <title> [slug]")
        sys.exit(1)
    
    book_number = sys.argv[1]
    title = sys.argv[2]
    slug = sys.argv[3] if len(sys.argv) > 3 else title.lower().replace(' ', '-')
    
    generate_book_page(book_number, title, slug)
