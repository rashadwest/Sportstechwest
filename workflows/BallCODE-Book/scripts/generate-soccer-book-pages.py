#!/usr/bin/env python3
"""
Generate Soccer Book Pages - Automated Website Page Generation
Creates Book 1, 2, 3 pages automatically from templates
"""

import json
from pathlib import Path
from datetime import datetime

BALLCODE_DIR = Path(__file__).parent.parent / "BallCode"
SOCCER_DIR = BALLCODE_DIR / "soccer"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

BOOK_DATA = {
    1: {
        "title": "The Foundation Pass",
        "slug": "book-1-foundation-pass",
        "soccer_skill": "Basic ball control, first touch",
        "coding_concept": "Variables (player positions, ball position)",
        "math_concept": "Spatial awareness, coordinates",
        "world_cup_context": "Learning to control the ball like a World Cup player",
    },
    2: {
        "title": "The Code of Flow",
        "slug": "book-2-code-of-flow",
        "soccer_skill": "Dribbling patterns, ball movement",
        "coding_concept": "Sequences (step-by-step dribbling)",
        "math_concept": "Patterns, sequences",
        "world_cup_context": "Dribbling through defenders",
    },
    3: {
        "title": "The Pattern",
        "slug": "book-3-pattern",
        "soccer_skill": "Passing sequences, tactical patterns",
        "coding_concept": "Loops (repeating passing patterns)",
        "math_concept": "Geometric patterns, angles",
        "world_cup_context": "Team passing patterns",
    },
}

def load_basketball_template(book_number):
    """Load basketball book page as template"""
    basketball_dir = BALLCODE_DIR / "books"
    book_files = list(basketball_dir.glob(f"book-{book_number}*/index.html"))
    
    if book_files:
        return book_files[0].read_text()
    
    # Fallback template
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | BallCODE Soccer</title>
    <link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div class="book-page">
        <h1>{{title}}</h1>
        <div class="book-content">
            <p>Content coming soon...</p>
        </div>
    </div>
</body>
</html>"""

def generate_book_page(book_number, book_data):
    """Generate soccer book page"""
    # Load template
    template = load_basketball_template(book_number)
    
    # Replace placeholders
    page_content = template
    page_content = page_content.replace("{{title}}", book_data["title"])
    page_content = page_content.replace("Basketball", "Soccer")
    page_content = page_content.replace("basketball", "soccer")
    
    # Add soccer-specific content
    soccer_section = f"""
    <div class="soccer-book-info">
        <h2>Soccer Skills</h2>
        <p>{book_data['soccer_skill']}</p>
        
        <h2>Coding Concepts</h2>
        <p>{book_data['coding_concept']}</p>
        
        <h2>Math Concepts</h2>
        <p>{book_data['math_concept']}</p>
        
        <h2>World Cup 2026 Connection</h2>
        <p>{book_data['world_cup_context']}</p>
    </div>
    """
    
    # Insert soccer section before closing body
    if "</body>" in page_content:
        page_content = page_content.replace("</body>", soccer_section + "</body>")
    
    # Create book directory
    book_dir = SOCCER_DIR / "books" / book_data["slug"]
    book_dir.mkdir(parents=True, exist_ok=True)
    
    # Save page
    index_file = book_dir / "index.html"
    index_file.write_text(page_content)
    
    print(f"✅ Generated: {index_file}")
    return index_file

def create_gumroad_integration(book_number, book_data):
    """Create Gumroad product integration"""
    gumroad_data = {
        "book_number": book_number,
        "title": book_data["title"],
        "slug": book_data["slug"],
        "price": 5.00,
        "description": f"Learn {book_data['coding_concept']} through {book_data['soccer_skill']}",
        "status": "coming_soon",
        "launch_date": "2026-03-01",
    }
    
    gumroad_file = SOCCER_DIR / "books" / book_data["slug"] / "gumroad.json"
    gumroad_file.write_text(json.dumps(gumroad_data, indent=2))
    
    print(f"✅ Created Gumroad data: {gumroad_file}")
    return gumroad_data

def main():
    """Main execution"""
    print("⚽ Generating Soccer Book Pages...")
    print("=" * 50)
    
    for book_num, book_data in BOOK_DATA.items():
        print(f"\n📖 Generating Book {book_num}: {book_data['title']}")
        generate_book_page(book_num, book_data)
        create_gumroad_integration(book_num, book_data)
    
    print("\n" + "=" * 50)
    print("✅ All soccer book pages generated!")
    print(f"📁 Location: {SOCCER_DIR / 'books'}")
    print("\nNext steps:")
    print("1. Review generated pages")
    print("2. Add actual story content")
    print("3. Add video embeds")
    print("4. Deploy to ballcode.co")

if __name__ == "__main__":
    main()

