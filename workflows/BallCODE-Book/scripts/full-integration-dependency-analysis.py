#!/usr/bin/env python3
"""
Full Integration: AI-Assisted Dependency Analysis
Analyzes dependencies between systems and determines optimal execution order.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def analyze_dependencies(analysis_data_json: str) -> dict:
    """Analyze dependencies between systems and determine execution order."""
    try:
        # Parse analysis data
        if isinstance(analysis_data_json, str):
            try:
                analysis_data = json.loads(analysis_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', analysis_data_json)
                if json_match:
                    analysis_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            analysis_data = analysis_data_json
        
        results = {
            "status": "success",
            "dependencies": {},
            "execution_order": [],
            "conflicts": [],
            "recommendations": [],
            "errors": []
        }
        
        # Get systems to update
        systems = analysis_data.get("systems", [])
        updates = analysis_data.get("updates", {})
        
        # Define system dependencies
        system_dependencies = {
            "curriculum": [],  # No dependencies - can run first
            "book": ["curriculum"],  # Depends on curriculum
            "game": ["curriculum", "book"],  # Depends on curriculum and book
            "website": ["curriculum", "book", "game"]  # Depends on all others
        }
        
        # Analyze dependencies for each system
        for system in systems:
            deps = system_dependencies.get(system, [])
            results["dependencies"][system] = {
                "depends_on": deps,
                "blocks": [s for s in systems if system in system_dependencies.get(s, [])],
                "can_run_parallel": [s for s in systems if not set(deps) & set(system_dependencies.get(s, []))]
            }
        
        # Determine execution order (topological sort)
        execution_order = []
        remaining = set(systems)
        completed = set()
        
        while remaining:
            # Find systems with no unmet dependencies
            ready = [
                s for s in remaining
                if all(dep in completed for dep in system_dependencies.get(s, []))
            ]
            
            if not ready:
                # Circular dependency or error
                results["conflicts"].append(f"Circular dependency detected: {remaining}")
                # Force execution order
                execution_order.extend(list(remaining))
                break
            
            # Add ready systems to execution order (can run in parallel)
            execution_order.append(ready)
            completed.update(ready)
            remaining -= set(ready)
        
        results["execution_order"] = execution_order
        
        # Check for conflicts
        for system in systems:
            deps = system_dependencies.get(system, [])
            missing_deps = [d for d in deps if d not in systems]
            if missing_deps:
                results["conflicts"].append(f"{system} depends on missing systems: {missing_deps}")
        
        # Generate recommendations
        if len(execution_order) == 1 and len(execution_order[0]) == len(systems):
            results["recommendations"].append("All systems can run in parallel")
        else:
            results["recommendations"].append(f"Execute in {len(execution_order)} phases")
            for i, phase in enumerate(execution_order, 1):
                if len(phase) > 1:
                    results["recommendations"].append(f"Phase {i}: Run {', '.join(phase)} in parallel")
                else:
                    results["recommendations"].append(f"Phase {i}: Run {phase[0]}")
        
        # Determine overall status
        if results["conflicts"]:
            results["status"] = "warning" if execution_order else "error"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "systems_analyzed": len(systems),
            "execution_phases": len(execution_order),
            "conflicts_found": len(results["conflicts"]),
            "recommendations_count": len(results["recommendations"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "dependencies": {},
            "execution_order": [],
            "conflicts": [],
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
        # Default: analyze all systems
        input_json = json.dumps({
            "systems": ["curriculum", "book", "game", "website"],
            "updates": {}
        })
    
    result = analyze_dependencies(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


