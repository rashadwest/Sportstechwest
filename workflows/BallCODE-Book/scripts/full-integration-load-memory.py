#!/usr/bin/env python3
"""
Full Integration: Load Memory Context
Loads previous memory context at workflow start for continuity.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
MEMORY_DIR = PROJECT_ROOT / "documents"

def load_memory_context(session_id: Optional[str] = None, book_id: Optional[int] = None, days_back: int = 7) -> dict:
    """Load memory context from previous sessions."""
    try:
        results = {
            "status": "success",
            "memory_loaded": False,
            "context": {},
            "recent_sessions": [],
            "errors": []
        }
        
        # Find memory context files
        memory_files = []
        if MEMORY_DIR.exists():
            # Look for memory context files
            pattern = "Book-*-Integration-*.json" if book_id else "*Integration*.json"
            memory_files = list(MEMORY_DIR.glob(pattern))
            
            # Also look for memory-context-*.json files
            memory_files.extend(MEMORY_DIR.glob("memory-context-*.json"))
        
        if not memory_files:
            return results  # No memory found, return empty
        
        # Sort by modification time (newest first)
        memory_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        
        # Load most recent memory files (within days_back)
        cutoff_date = datetime.now() - timedelta(days=days_back)
        recent_memories = []
        
        for memory_file in memory_files:
            try:
                file_mtime = datetime.fromtimestamp(memory_file.stat().st_mtime)
                if file_mtime >= cutoff_date:
                    with open(memory_file, 'r', encoding='utf-8') as f:
                        memory_data = json.load(f)
                    
                    # Filter by session_id or book_id if provided
                    if session_id and memory_data.get('sessionId') != session_id:
                        continue
                    if book_id and memory_data.get('bookId') != book_id:
                        continue
                    
                    recent_memories.append({
                        "file": str(memory_file),
                        "timestamp": file_mtime.isoformat(),
                        "data": memory_data
                    })
            except Exception as e:
                results["errors"].append(f"Error loading {memory_file}: {str(e)}")
        
        # Merge recent memories into context
        if recent_memories:
            # Use most recent as primary context
            primary_memory = recent_memories[0]["data"]
            
            # Merge all recent memories
            merged_context = {
                "timestamp": datetime.now().isoformat(),
                "primary_session": primary_memory.get('sessionId'),
                "book_updates": [],
                "lesson_updates": [],
                "website_updates": [],
                "game_updates": [],
                "curriculum_updates": [],
                "next_steps": []
            }
            
            for memory in recent_memories:
                data = memory["data"]
                
                # Merge updates
                if "updates" in data:
                    merged_context["book_updates"].extend(data["updates"].get("books", []))
                    merged_context["lesson_updates"].extend(data["updates"].get("lessons", []))
                    merged_context["website_updates"].extend(data["updates"].get("website", []))
                    merged_context["game_updates"].extend(data["updates"].get("game", []))
                    merged_context["curriculum_updates"].extend(data["updates"].get("curriculum", []))
                
                # Merge next steps
                if "nextSteps" in data:
                    merged_context["next_steps"].extend(data["nextSteps"])
            
            # Remove duplicates
            merged_context["book_updates"] = list({json.dumps(u, sort_keys=True): u for u in merged_context["book_updates"]}.values())
            merged_context["next_steps"] = list(dict.fromkeys(merged_context["next_steps"]))
            
            results["memory_loaded"] = True
            results["context"] = merged_context
            results["recent_sessions"] = [m["timestamp"] for m in recent_memories[:5]]  # Last 5 sessions
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "memory_loaded": False,
            "context": {},
            "errors": [str(e)]
        }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Load memory context for Full Integration")
    parser.add_argument("--session-id", help="Specific session ID to load")
    parser.add_argument("--book-id", type=int, help="Specific book ID to load")
    parser.add_argument("--days-back", type=int, default=7, help="Days back to search for memory")
    
    args = parser.parse_args()
    
    result = load_memory_context(
        session_id=args.session_id,
        book_id=args.book_id,
        days_back=args.days_back
    )
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)

