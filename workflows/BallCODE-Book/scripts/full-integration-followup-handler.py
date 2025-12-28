#!/usr/bin/env python3
"""
Full Integration: Follow-up Prompt Handler
Handles follow-up prompts by loading previous context and continuing work.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def handle_followup_prompt(followup_data_json: str) -> dict:
    """Handle follow-up prompt by loading previous context."""
    try:
        # Parse follow-up data
        if isinstance(followup_data_json, str):
            try:
                followup_data = json.loads(followup_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', followup_data_json)
                if json_match:
                    followup_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            followup_data = followup_data_json
        
        results = {
            "status": "success",
            "context_loaded": False,
            "previous_context": {},
            "enhanced_prompt": "",
            "continuation_data": {},
            "errors": []
        }
        
        # Load previous memory context
        session_id = followup_data.get("sessionId")
        book_id = followup_data.get("bookId")
        new_prompt = followup_data.get("prompt", "")
        
        # Use memory loading script
        from full_integration_load_memory import load_memory_context
        
        memory_result = load_memory_context(
            session_id=session_id,
            book_id=book_id,
            days_back=7
        )
        
        if memory_result.get("memory_loaded"):
            results["context_loaded"] = True
            results["previous_context"] = memory_result.get("context", {})
            
            # Enhance prompt with previous context
            previous_updates = results["previous_context"].get("book_updates", [])
            next_steps = results["previous_context"].get("next_steps", [])
            
            enhanced_prompt = f"{new_prompt}\n\n"
            
            if previous_updates:
                enhanced_prompt += f"Previous updates: {json.dumps(previous_updates[:3], indent=2)}\n\n"
            
            if next_steps:
                enhanced_prompt += f"Next steps from previous session: {', '.join(next_steps[:5])}\n\n"
            
            results["enhanced_prompt"] = enhanced_prompt
            
            # Create continuation data
            results["continuation_data"] = {
                "session_id": session_id,
                "book_id": book_id,
                "previous_updates": previous_updates,
                "next_steps": next_steps,
                "context_timestamp": memory_result.get("recent_sessions", [])[0] if memory_result.get("recent_sessions") else None
            }
        else:
            # No previous context found - use prompt as-is
            results["enhanced_prompt"] = new_prompt
            results["continuation_data"] = {
                "session_id": session_id,
                "book_id": book_id,
                "previous_updates": [],
                "next_steps": []
            }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "context_loaded": False,
            "enhanced_prompt": followup_data.get("prompt", ""),
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
    
    result = handle_followup_prompt(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


