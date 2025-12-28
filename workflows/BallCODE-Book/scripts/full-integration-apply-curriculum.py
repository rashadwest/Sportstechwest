#!/usr/bin/env python3
"""
Full Integration: Apply Curriculum Updates
Takes AI-generated curriculum updates and applies them to the curriculum schema.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SCHEMA_SCRIPT = PROJECT_ROOT / "scripts" / "update_ballcode_schema.py"

def apply_curriculum_updates(curriculum_updates_json: str) -> dict:
    """Apply curriculum updates from AI generation."""
    try:
        # Parse AI-generated JSON
        if isinstance(curriculum_updates_json, str):
            try:
                updates = json.loads(curriculum_updates_json)
            except json.JSONDecodeError:
                # Try to extract JSON from markdown or text
                import re
                json_match = re.search(r'\{[\s\S]*\}', curriculum_updates_json)
                if json_match:
                    updates = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            updates = curriculum_updates_json
        
        results = {
            "status": "success",
            "schema_updated": False,
            "validation_passed": False,
            "updates_applied": {},
            "errors": []
        }
        
        # Determine update type and apply accordingly
        # Check if it's a full schema update or partial update
        if "books" in updates or "curriculum" in updates:
            # Full schema update - write directly to schema file
            schema_path = PROJECT_ROOT / "CURRICULUM-DATA-EXAMPLE.json"
            
            # Load existing schema if it exists
            if schema_path.exists():
                with open(schema_path, 'r', encoding='utf-8') as f:
                    existing_schema = json.load(f)
            else:
                existing_schema = {"books": [], "curriculum": {}, "metadata": {}}
            
            # Merge updates
            if "books" in updates:
                if isinstance(existing_schema.get("books"), list):
                    # Merge book entries
                    existing_books = {b.get("id"): b for b in existing_schema["books"] if isinstance(b, dict) and "id" in b}
                    for book in updates["books"]:
                        if isinstance(book, dict) and "id" in book:
                            existing_books[book["id"]] = book
                    existing_schema["books"] = list(existing_books.values())
                else:
                    existing_schema["books"] = updates["books"]
            
            if "curriculum" in updates:
                existing_schema["curriculum"].update(updates["curriculum"])
            
            # Update metadata
            if "metadata" not in existing_schema:
                existing_schema["metadata"] = {}
            from datetime import datetime
            existing_schema["metadata"]["lastUpdated"] = datetime.now().isoformat()
            
            # Save updated schema
            schema_path.write_text(json.dumps(existing_schema, indent=2), encoding='utf-8')
            results["schema_updated"] = True
            results["updates_applied"]["schema_file"] = str(schema_path)
            
        elif "type" in updates:
            # Use update_ballcode_schema.py script
            update_type = updates.get("type")
            update_id = updates.get("id")
            update_data = updates.get("data", {})
            
            # Build command
            cmd = [sys.executable, str(SCHEMA_SCRIPT), "--type", update_type]
            
            if update_id:
                cmd.extend(["--id", str(update_id)])
            
            if update_data:
                cmd.extend(["--data", json.dumps(update_data)])
            
            # Execute update script
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=PROJECT_ROOT,
                timeout=30
            )
            
            if result.returncode == 0:
                results["schema_updated"] = True
                results["updates_applied"]["script_output"] = result.stdout
            else:
                results["errors"].append(f"Schema update script failed: {result.stderr}")
        
        # Validate schema
        schema_path = PROJECT_ROOT / "CURRICULUM-DATA-EXAMPLE.json"
        if schema_path.exists():
            try:
                with open(schema_path, 'r', encoding='utf-8') as f:
                    schema = json.load(f)
                
                # Basic validation
                if isinstance(schema, dict) and ("books" in schema or "curriculum" in schema):
                    results["validation_passed"] = True
                else:
                    results["errors"].append("Schema validation failed: invalid structure")
            except json.JSONDecodeError as e:
                results["errors"].append(f"Schema validation failed: invalid JSON - {str(e)}")
        
        # Determine overall status
        if results["errors"]:
            results["status"] = "partial" if results["schema_updated"] else "error"
        else:
            results["status"] = "success"
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "schema_updated": False,
            "validation_passed": False,
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
    
    result = apply_curriculum_updates(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


