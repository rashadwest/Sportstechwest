#!/usr/bin/env python3
"""
Full Integration: System Sync Verification
Verifies that all systems (game, curriculum, book, website) are in sync.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def verify_system_sync(verification_data_json: str) -> dict:
    """Verify all systems are in sync."""
    try:
        # Parse verification data
        if isinstance(verification_data_json, str):
            try:
                verification_data = json.loads(verification_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', verification_data_json)
                if json_match:
                    verification_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            verification_data = verification_data_json
        
        results = {
            "status": "success",
            "systems_synced": {},
            "sync_issues": [],
            "errors": []
        }
        
        # Load curriculum schema (source of truth)
        schema_path = PROJECT_ROOT / "CURRICULUM-DATA-EXAMPLE.json"
        if not schema_path.exists():
            results["errors"].append("Curriculum schema not found")
            results["status"] = "error"
            return results
        
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        # Verify game system sync
        try:
            game_levels_dir = PROJECT_ROOT / "Unity-Scripts" / "Levels"
            game_levels = list(game_levels_dir.glob("book*.json")) if game_levels_dir.exists() else []
            
            # Check if level files match schema books
            schema_books = schema.get("books", [])
            schema_book_ids = {b.get("id") for b in schema_books if isinstance(b, dict)}
            
            game_sync = {
                "status": "success",
                "levels_found": len(game_levels),
                "books_in_schema": len(schema_books),
                "sync_issues": []
            }
            
            # Check for missing levels or extra levels
            for book in schema_books:
                if isinstance(book, dict):
                    book_id = book.get("id")
                    level_file = game_levels_dir / f"book{book_id}_*.json"
                    matching_levels = list(game_levels_dir.glob(f"book{book_id}_*.json"))
                    if not matching_levels:
                        game_sync["sync_issues"].append(f"Book {book_id} has no level file")
                        game_sync["status"] = "partial"
            
            results["systems_synced"]["game"] = game_sync
            
        except Exception as e:
            results["systems_synced"]["game"] = {"status": "error", "error": str(e)}
            results["errors"].append(f"Game sync verification failed: {str(e)}")
        
        # Verify book system sync
        try:
            books_dir = PROJECT_ROOT / "My Books"
            book_files = list(books_dir.glob("Book-*.md")) if books_dir.exists() else []
            
            book_sync = {
                "status": "success",
                "book_files_found": len(book_files),
                "books_in_schema": len(schema.get("books", [])),
                "sync_issues": []
            }
            
            # Check if book files match schema
            for book in schema.get("books", []):
                if isinstance(book, dict):
                    book_id = book.get("id")
                    book_file = books_dir / f"Book-{book_id}-*.md"
                    matching_files = list(books_dir.glob(f"Book-{book_id}-*.md"))
                    if not matching_files:
                        book_sync["sync_issues"].append(f"Book {book_id} has no content file")
                        book_sync["status"] = "partial"
            
            results["systems_synced"]["book"] = book_sync
            
        except Exception as e:
            results["systems_synced"]["book"] = {"status": "error", "error": str(e)}
            results["errors"].append(f"Book sync verification failed: {str(e)}")
        
        # Verify website system sync
        try:
            website_dir = PROJECT_ROOT / "BallCode"
            website_book_pages = list(website_dir.glob("books/book*.html")) if website_dir.exists() else []
            
            website_sync = {
                "status": "success",
                "book_pages_found": len(website_book_pages),
                "books_in_schema": len(schema.get("books", [])),
                "sync_issues": []
            }
            
            # Check if website pages match schema
            for book in schema.get("books", []):
                if isinstance(book, dict):
                    book_id = book.get("id")
                    book_page = website_dir / "books" / f"book{book_id}.html"
                    if not book_page.exists():
                        website_sync["sync_issues"].append(f"Book {book_id} has no website page")
                        website_sync["status"] = "partial"
            
            results["systems_synced"]["website"] = website_sync
            
        except Exception as e:
            results["systems_synced"]["website"] = {"status": "error", "error": str(e)}
            results["errors"].append(f"Website sync verification failed: {str(e)}")
        
        # Verify curriculum system sync
        try:
            curriculum_sync = {
                "status": "success",
                "schema_exists": schema_path.exists(),
                "books_count": len(schema.get("books", [])),
                "curriculum_sections": len(schema.get("curriculum", {})),
                "sync_issues": []
            }
            
            # Check schema structure
            if not schema.get("books") and not schema.get("curriculum"):
                curriculum_sync["sync_issues"].append("Schema is empty")
                curriculum_sync["status"] = "warning"
            
            results["systems_synced"]["curriculum"] = curriculum_sync
            
        except Exception as e:
            results["systems_synced"]["curriculum"] = {"status": "error", "error": str(e)}
            results["errors"].append(f"Curriculum sync verification failed: {str(e)}")
        
        # Collect all sync issues
        for system, sync_data in results["systems_synced"].items():
            if sync_data.get("sync_issues"):
                results["sync_issues"].extend([f"{system}: {issue}" for issue in sync_data["sync_issues"]])
        
        # Determine overall status
        all_synced = all(
            sync_data.get("status") == "success"
            for sync_data in results["systems_synced"].values()
        )
        
        if results["errors"]:
            results["status"] = "error"
        elif results["sync_issues"]:
            results["status"] = "partial"
        elif all_synced:
            results["status"] = "success"
        else:
            results["status"] = "partial"
        
        results["summary"] = {
            "systems_checked": len(results["systems_synced"]),
            "systems_synced": sum(1 for s in results["systems_synced"].values() if s.get("status") == "success"),
            "sync_issues_count": len(results["sync_issues"]),
            "errors_count": len(results["errors"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "systems_synced": {},
            "sync_issues": [],
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
        input_json = '{}'  # Empty config - verify all systems
    
    result = verify_system_sync(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


