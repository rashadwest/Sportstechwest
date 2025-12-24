#!/usr/bin/env python3
"""
Full Integration: AI Model Selection
Selects optimal AI model based on task complexity.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional

# Model configurations
MODEL_CONFIGS = {
    "simple": {
        "model": "gpt-3.5-turbo",
        "max_tokens": 1000,
        "temperature": 0.7,
        "cost_per_1k": 0.0015
    },
    "medium": {
        "model": "gpt-4",
        "max_tokens": 2000,
        "temperature": 0.7,
        "cost_per_1k": 0.03
    },
    "complex": {
        "model": "gpt-4-turbo",
        "max_tokens": 4000,
        "temperature": 0.7,
        "cost_per_1k": 0.06
    }
}

def select_ai_model(task_data_json: str) -> dict:
    """Select optimal AI model based on task complexity."""
    try:
        # Parse task data
        if isinstance(task_data_json, str):
            try:
                task_data = json.loads(task_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', task_data_json)
                if json_match:
                    task_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            task_data = task_data_json
        
        results = {
            "status": "success",
            "selected_model": "",
            "model_config": {},
            "reasoning": "",
            "estimated_cost": 0.0
        }
        
        # Determine task complexity
        prompt = task_data.get("prompt", "")
        prompt_length = len(prompt)
        systems = task_data.get("systems", [])
        mode = task_data.get("mode", "quick")
        
        # Complexity heuristics
        complexity = "simple"
        
        if prompt_length > 2000 or len(systems) > 2 or mode == "comprehensive":
            complexity = "complex"
        elif prompt_length > 1000 or len(systems) > 1 or mode == "full":
            complexity = "medium"
        else:
            complexity = "simple"
        
        # Select model
        model_config = MODEL_CONFIGS[complexity]
        results["selected_model"] = model_config["model"]
        results["model_config"] = model_config
        results["reasoning"] = f"Task complexity: {complexity} (prompt length: {prompt_length}, systems: {len(systems)}, mode: {mode})"
        
        # Estimate cost (rough estimate based on max_tokens)
        estimated_tokens = min(prompt_length // 4 + model_config["max_tokens"], model_config["max_tokens"])
        results["estimated_cost"] = (estimated_tokens / 1000) * model_config["cost_per_1k"]
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "selected_model": "",
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
    
    result = select_ai_model(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)

