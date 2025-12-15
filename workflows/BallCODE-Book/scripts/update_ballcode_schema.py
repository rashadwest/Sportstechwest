#!/usr/bin/env python3
"""
BallCODE Schema Update Script
Updates CURRICULUM-DATA-EXAMPLE.json and syncs to API location

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python3 update_ballcode_schema.py --type book --id 1 --data '{"title": "New Title"}'
    python3 update_ballcode_schema.py --type curriculum --data '{"learningObjectives": [...]}'
    python3 update_ballcode_schema.py --type exercise --book-id 1 --data '{"exerciseId": "ex1", "url": "..."}'
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Get project root
PROJECT_ROOT = Path(__file__).parent.parent
SCHEMA_PATH = PROJECT_ROOT / 'CURRICULUM-DATA-EXAMPLE.json'
API_SCHEMA_PATH = PROJECT_ROOT / 'BallCode' / 'data' / 'curriculum-data.json'


def load_schema() -> Dict[str, Any]:
    """Load the curriculum schema from file."""
    try:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Schema file not found at {SCHEMA_PATH}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in schema file: {e}")
        sys.exit(1)


def save_schema(schema: Dict[str, Any]) -> bool:
    """Save the curriculum schema to file."""
    try:
        # Update metadata
        if 'metadata' not in schema:
            schema['metadata'] = {}
        
        schema['metadata']['lastUpdated'] = datetime.now().isoformat()
        if 'version' in schema['metadata']:
            # Increment version
            version = float(schema['metadata']['version'])
            schema['metadata']['version'] = f"{version + 0.1:.1f}"
        else:
            schema['metadata']['version'] = '1.0.0'
        
        # Save to main schema file
        with open(SCHEMA_PATH, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        # Copy to API location
        API_SCHEMA_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(API_SCHEMA_PATH, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"❌ Error saving schema: {e}")
        return False


def update_book(schema: Dict[str, Any], book_id: int, book_data: Dict[str, Any]) -> bool:
    """Update a book in the schema."""
    if 'books' not in schema:
        schema['books'] = []
    
    # Find existing book
    book_index = None
    for i, book in enumerate(schema['books']):
        if book.get('id') == book_id:
            book_index = i
            break
    
    # Prepare book entry
    book_entry = {
        'id': book_id,
        **book_data
    }
    
    if book_index is not None:
        # Update existing book
        schema['books'][book_index].update(book_entry)
        print(f"✅ Updated Book {book_id}")
    else:
        # Add new book
        schema['books'].append(book_entry)
        print(f"✅ Added new Book {book_id}")
    
    return True


def update_curriculum(schema: Dict[str, Any], curriculum_data: Dict[str, Any]) -> bool:
    """Update curriculum in the schema."""
    if 'curriculum' not in schema:
        schema['curriculum'] = {}
    
    # Merge curriculum data
    schema['curriculum'].update(curriculum_data)
    print("✅ Updated curriculum")
    
    return True


def integrate_exercise(schema: Dict[str, Any], book_id: int, exercise_data: Dict[str, Any]) -> bool:
    """Integrate an exercise into a book."""
    if 'books' not in schema:
        print("❌ Error: No books in schema")
        return False
    
    # Find book
    book = None
    for b in schema['books']:
        if b.get('id') == book_id:
            book = b
            break
    
    if not book:
        print(f"❌ Error: Book {book_id} not found")
        return False
    
    # Initialize exercises array if needed
    if 'exercises' not in book:
        book['exercises'] = []
    
    # Prepare exercise entry
    exercise_id = exercise_data.get('exerciseId') or exercise_data.get('id')
    if not exercise_id:
        exercise_id = f"exercise-{book_id}-{len(book['exercises']) + 1}"
    
    exercise_entry = {
        'exerciseId': exercise_id,
        'url': exercise_data.get('url') or f"ballcode.co/play?book={book_id}&exercise={exercise_id}",
        'mode': exercise_data.get('mode', 'story'),
        'difficulty': exercise_data.get('difficulty', 'beginner'),
        'description': exercise_data.get('description', ''),
        'successCriteria': exercise_data.get('successCriteria', []),
        'addedAt': datetime.now().isoformat()
    }
    
    # Check if exercise already exists
    existing_index = None
    for i, ex in enumerate(book['exercises']):
        if ex.get('exerciseId') == exercise_id:
            existing_index = i
            break
    
    if existing_index is not None:
        # Update existing exercise
        book['exercises'][existing_index].update(exercise_entry)
        print(f"✅ Updated exercise {exercise_id} in Book {book_id}")
    else:
        # Add new exercise
        book['exercises'].append(exercise_entry)
        print(f"✅ Added exercise {exercise_id} to Book {book_id}")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Update BallCODE curriculum schema',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Update book title
  python3 update_ballcode_schema.py --type book --id 1 --data '{"title": "New Title"}'
  
  # Update curriculum learning objectives
  python3 update_ballcode_schema.py --type curriculum --data '{"learningObjectives": ["New objective"]}'
  
  # Add exercise to book
  python3 update_ballcode_schema.py --type exercise --book-id 1 --data '{"exerciseId": "ex1", "url": "ballcode.co/play?book=1&exercise=ex1"}'
        """
    )
    
    parser.add_argument(
        '--type',
        choices=['book', 'curriculum', 'exercise'],
        required=True,
        help='Type of update: book, curriculum, or exercise'
    )
    
    parser.add_argument(
        '--id',
        type=int,
        help='Book ID (for book updates)'
    )
    
    parser.add_argument(
        '--book-id',
        type=int,
        dest='book_id',
        help='Book ID (for exercise integration)'
    )
    
    parser.add_argument(
        '--data',
        required=True,
        help='JSON data for the update'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be updated without saving'
    )
    
    args = parser.parse_args()
    
    # Load schema
    schema = load_schema()
    
    # Parse data
    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in --data: {e}")
        sys.exit(1)
    
    # Perform update
    success = False
    
    if args.type == 'book':
        if not args.id:
            print("❌ Error: --id required for book updates")
            sys.exit(1)
        success = update_book(schema, args.id, data)
    
    elif args.type == 'curriculum':
        success = update_curriculum(schema, data)
    
    elif args.type == 'exercise':
        book_id = args.book_id or args.id
        if not book_id:
            print("❌ Error: --book-id or --id required for exercise integration")
            sys.exit(1)
        success = integrate_exercise(schema, book_id, data)
    
    if not success:
        print("❌ Update failed")
        sys.exit(1)
    
    # Save if not dry run
    if args.dry_run:
        print("\n🔍 Dry run - would update:")
        print(json.dumps(schema, indent=2))
        print("\n✅ Use without --dry-run to save changes")
    else:
        if save_schema(schema):
            print(f"✅ Schema saved to {SCHEMA_PATH}")
            print(f"✅ Schema copied to {API_SCHEMA_PATH}")
            print("✅ JavaScript will auto-sync all systems on next page load")
        else:
            print("❌ Failed to save schema")
            sys.exit(1)


if __name__ == '__main__':
    main()

