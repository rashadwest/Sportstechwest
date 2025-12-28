#!/usr/bin/env python3
"""
Full Integration: Apply Book Updates
Takes AI-generated book updates and applies them to the book system.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
BOOKS_DIR = PROJECT_ROOT / "My Books"
MEMORY_DIR = PROJECT_ROOT / "documents"

def apply_book_updates(book_updates_json: str) -> dict:
    """Apply book updates from AI generation."""
    try:
        # Parse AI-generated JSON
        if isinstance(book_updates_json, str):
            try:
                updates = json.loads(book_updates_json)
            except json.JSONDecodeError:
                # Try to extract JSON from markdown or text
                import re
                json_match = re.search(r'\{[\s\S]*\}', book_updates_json)
                if json_match:
                    updates = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            updates = book_updates_json
        
        results = {
            "status": "success",
            "book_updated": False,
            "files_updated": [],
            "memory_context": {},
            "errors": []
        }
        
        # Extract updates
        story_content = updates.get('storyContent', '')
        learning_section = updates.get('learningSection', {})
        exercise_button = updates.get('exerciseButton', {})
        curriculum_connection = updates.get('curriculumConnection', {})
        memory_context = updates.get('memoryContext', {})
        
        book_id = memory_context.get('bookId') or updates.get('bookId')
        
        # Save story content if provided
        if story_content:
            try:
                book_file_name = f"Book-{book_id}-Content.md" if book_id else "Book-Content.md"
                book_file_path = BOOKS_DIR / book_file_name
                book_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Append or create content
                if book_file_path.exists():
                    existing_content = book_file_path.read_text(encoding='utf-8')
                    book_file_path.write_text(f"{existing_content}\n\n---\n\n{story_content}", encoding='utf-8')
                else:
                    book_file_path.write_text(story_content, encoding='utf-8')
                
                results["files_updated"].append(str(book_file_path))
                results["book_updated"] = True
            except Exception as e:
                results["errors"].append(f"Error saving story content: {str(e)}")
        
        # Save learning section and exercise button to memory context
        if learning_section or exercise_button or curriculum_connection:
            try:
                memory_file_name = f"Book-{book_id}-Integration-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json" if book_id else f"Book-Integration-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
                memory_file_path = MEMORY_DIR / memory_file_name
                
                memory_data = {
                    "timestamp": datetime.now().isoformat(),
                    "bookId": book_id,
                    "learningSection": learning_section,
                    "exerciseButton": exercise_button,
                    "curriculumConnection": curriculum_connection,
                    "updates": memory_context.get('updates', []),
                    "nextSteps": memory_context.get('nextSteps', [])
                }
                
                memory_file_path.write_text(json.dumps(memory_data, indent=2), encoding='utf-8')
                results["files_updated"].append(str(memory_file_path))
                results["memory_context"] = memory_data
            except Exception as e:
                results["errors"].append(f"Error saving memory context: {str(e)}")
        
        # Determine overall status
        if results["errors"]:
            results["status"] = "partial" if results["book_updated"] else "error"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "story_content_saved": bool(story_content),
            "learning_section_saved": bool(learning_section),
            "exercise_button_saved": bool(exercise_button),
            "files_updated_count": len(results["files_updated"]),
            "errors_count": len(results["errors"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "book_updated": False,
            "files_updated": [],
            "errors": [str(e)]
        }

if __name__ == "__main__":
    # Read from stdin or file argument
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        if input_path.exists():
            input_json = input_path.read_text(encoding='utf-8')
        else:
            input_json = sys.argv[1]  # Treat as JSON string
    else:
        input_json = sys.stdin.read()
    
    result = apply_book_updates(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


