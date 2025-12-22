#!/usr/bin/env python3
"""
Adapt Basketball Content to Soccer - AI-Assisted Content Generation
Maps basketball concepts to soccer equivalents
"""

import json
import re
from pathlib import Path

# Mapping dictionaries
BASKETBALL_TO_SOCCER = {
    # Skills
    "dribble": "dribble",
    "dribbling": "dribbling",
    "layup": "shot",
    "jump shot": "shot",
    "three-pointer": "long shot",
    "pivot": "turn",
    "pass": "pass",
    "shoot": "shoot",
    "rebound": "tackle",
    
    # Court/Field
    "court": "field",
    "basketball court": "soccer field",
    "hoop": "goal",
    "basket": "goal",
    "free throw line": "penalty spot",
    
    # Equipment
    "basketball": "soccer ball",
    "ball": "ball",
    
    # Actions
    "score": "score",
    "scoring": "scoring",
    "defense": "defense",
    "offense": "attack",
    "team": "team",
    
    # Concepts
    "basketball skills": "soccer skills",
    "basketball player": "soccer player",
    "coach": "coach",
}

CODING_CONCEPT_MAPPING = {
    "variables": "variables",  # Same concept
    "sequences": "sequences",  # Same concept
    "conditionals": "conditionals",  # Same concept
    "loops": "loops",  # Same concept
    "functions": "functions",  # Same concept
}

def load_basketball_content(book_number):
    """Load basketball book content"""
    basketball_dir = Path(__file__).parent.parent / "BallCode" / "books"
    book_files = list(basketball_dir.glob(f"book-{book_number}*"))
    
    if not book_files:
        print(f"⚠️  Basketball Book {book_number} not found")
        return None
    
    # Try to find story/content files
    for file_path in book_files:
        if file_path.is_file() and file_path.suffix in ['.md', '.txt', '.html']:
            return file_path.read_text()
    
    return None

def adapt_text(text, mapping):
    """Adapt text using mapping dictionary"""
    adapted = text
    
    # Replace terms (case-insensitive, whole word)
    for basketball_term, soccer_term in mapping.items():
        # Whole word replacement
        pattern = r'\b' + re.escape(basketball_term) + r'\b'
        adapted = re.sub(pattern, soccer_term, adapted, flags=re.IGNORECASE)
    
    return adapted

def adapt_story(basketball_story):
    """Adapt basketball story to soccer context"""
    # Apply term mapping
    soccer_story = adapt_text(basketball_story, BASKETBALL_TO_SOCCER)
    
    # Additional context-specific adaptations
    soccer_story = soccer_story.replace("basketball game", "soccer match")
    soccer_story = soccer_story.replace("playing basketball", "playing soccer")
    soccer_story = soccer_story.replace("basketball practice", "soccer training")
    
    return soccer_story

def create_soccer_book_outline(book_number, basketball_content):
    """Create soccer book outline from basketball content"""
    outline = {
        "book_number": book_number,
        "basketball_source": f"Book {book_number}",
        "soccer_adaptation": {
            "title": get_soccer_title(book_number),
            "soccer_skill": get_soccer_skill(book_number),
            "coding_concept": get_coding_concept(book_number),
            "world_cup_context": "World Cup 2026 preparation",
        },
        "adaptation_notes": [],
    }
    
    return outline

def get_soccer_title(book_number):
    """Get soccer book title"""
    titles = {
        1: "The Foundation Pass",
        2: "The Code of Flow",
        3: "The Pattern",
    }
    return titles.get(book_number, f"Book {book_number}")

def get_soccer_skill(book_number):
    """Get primary soccer skill for book"""
    skills = {
        1: "Basic ball control, first touch",
        2: "Dribbling patterns, ball movement",
        3: "Passing sequences, tactical patterns",
    }
    return skills.get(book_number, "Soccer skills")

def get_coding_concept(book_number):
    """Get coding concept for book"""
    concepts = {
        1: "Variables (player positions, ball position)",
        2: "Sequences (step-by-step dribbling)",
        3: "Loops (repeating passing patterns)",
    }
    return concepts.get(book_number, "Coding concepts")

def generate_soccer_content(book_number):
    """Generate soccer content from basketball source"""
    print(f"🔄 Adapting Basketball Book {book_number} to Soccer...")
    
    # Load basketball content
    basketball_content = load_basketball_content(book_number)
    
    if not basketball_content:
        print(f"❌ Could not load Basketball Book {book_number}")
        return None
    
    # Create outline
    outline = create_soccer_book_outline(book_number, basketball_content)
    
    # Adapt story
    soccer_story = adapt_story(basketball_content)
    
    # Save adapted content
    output_dir = Path(__file__).parent.parent / "soccer-content"
    output_dir.mkdir(exist_ok=True)
    
    # Save outline
    outline_file = output_dir / f"book-{book_number}-outline.json"
    outline_file.write_text(json.dumps(outline, indent=2))
    print(f"✅ Created outline: {outline_file}")
    
    # Save adapted story
    story_file = output_dir / f"book-{book_number}-story-adapted.md"
    story_file.write_text(soccer_story)
    print(f"✅ Created adapted story: {story_file}")
    
    return {
        "outline": outline,
        "story": soccer_story,
    }

def main():
    """Main execution"""
    print("⚽ Adapting Basketball Content to Soccer")
    print("=" * 50)
    
    # Adapt Books 1-3
    for book_num in [1, 2, 3]:
        result = generate_soccer_content(book_num)
        if result:
            print(f"✅ Book {book_num} adapted successfully")
        print()
    
    print("=" * 50)
    print("✅ Content adaptation complete!")
    print("\nNext steps:")
    print("1. Review adapted content")
    print("2. Refine soccer-specific details")
    print("3. Add World Cup 2026 context")
    print("4. Create final stories")

if __name__ == "__main__":
    main()

