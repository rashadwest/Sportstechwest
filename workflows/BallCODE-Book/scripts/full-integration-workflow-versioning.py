#!/usr/bin/env python3
"""
Full Integration: Workflow Versioning
Manages workflow versions for rollback and testing.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime
import shutil

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
VERSIONS_DIR = PROJECT_ROOT / ".workflow-versions"

def create_workflow_version(workflow_name: str, workflow_data_json: str) -> dict:
    """Create a new version of a workflow."""
    try:
        # Parse workflow data
        if isinstance(workflow_data_json, str):
            try:
                workflow_data = json.loads(workflow_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', workflow_data_json)
                if json_match:
                    workflow_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            workflow_data = workflow_data_json
        
        results = {
            "status": "success",
            "version_created": False,
            "workflow_name": workflow_name,
            "version": "",
            "version_path": "",
            "errors": []
        }
        
        # Create versions directory
        VERSIONS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Get next version number
        workflow_versions_dir = VERSIONS_DIR / workflow_name
        workflow_versions_dir.mkdir(exist_ok=True)
        
        existing_versions = [d.name for d in workflow_versions_dir.iterdir() if d.is_dir()]
        if existing_versions:
            version_numbers = [int(v.replace("v", "")) for v in existing_versions if v.startswith("v") and v[1:].isdigit()]
            next_version = max(version_numbers) + 1 if version_numbers else 1
        else:
            next_version = 1
        
        version = f"v{next_version}"
        version_path = workflow_versions_dir / version
        version_path.mkdir(exist_ok=True)
        
        # Save workflow data
        workflow_file = version_path / "workflow.json"
        workflow_file.write_text(json.dumps(workflow_data, indent=2), encoding='utf-8')
        
        # Save version metadata
        metadata = {
            "workflow_name": workflow_name,
            "version": version,
            "created_at": datetime.now().isoformat(),
            "description": workflow_data.get("description", "")
        }
        metadata_file = version_path / "metadata.json"
        metadata_file.write_text(json.dumps(metadata, indent=2), encoding='utf-8')
        
        results["version_created"] = True
        results["version"] = version
        results["version_path"] = str(version_path)
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "version_created": False,
            "errors": [str(e)]
        }

def get_workflow_version(workflow_name: str, version: Optional[str] = None) -> dict:
    """Get a specific workflow version or latest."""
    try:
        workflow_versions_dir = VERSIONS_DIR / workflow_name
        
        if not workflow_versions_dir.exists():
            return {
                "status": "error",
                "error": f"Workflow {workflow_name} not found",
                "workflow_name": workflow_name
            }
        
        # Get all versions
        versions = [d.name for d in workflow_versions_dir.iterdir() if d.is_dir() and d.name.startswith("v")]
        versions.sort(key=lambda v: int(v.replace("v", "")) if v[1:].isdigit() else 0, reverse=True)
        
        if not versions:
            return {
                "status": "error",
                "error": f"No versions found for {workflow_name}",
                "workflow_name": workflow_name
            }
        
        # Get specified version or latest
        target_version = version if version else versions[0]
        version_path = workflow_versions_dir / target_version
        
        if not version_path.exists():
            return {
                "status": "error",
                "error": f"Version {target_version} not found",
                "workflow_name": workflow_name,
                "version": target_version
            }
        
        # Load workflow data
        workflow_file = version_path / "workflow.json"
        if workflow_file.exists():
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
        else:
            workflow_data = {}
        
        # Load metadata
        metadata_file = version_path / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        else:
            metadata = {}
        
        return {
            "status": "success",
            "workflow_name": workflow_name,
            "version": target_version,
            "workflow_data": workflow_data,
            "metadata": metadata,
            "all_versions": versions
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "workflow_name": workflow_name
        }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Workflow Versioning")
    parser.add_argument("--create", help="Create version for workflow name")
    parser.add_argument("--workflow", help="Workflow data (JSON)")
    parser.add_argument("--get", help="Get version for workflow name")
    parser.add_argument("--version", help="Specific version to get")
    
    args = parser.parse_args()
    
    if args.create:
        if not args.workflow:
            print(json.dumps({"status": "error", "error": "Workflow data required"}, indent=2))
            sys.exit(1)
        
        result = create_workflow_version(args.create, args.workflow)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    elif args.get:
        result = get_workflow_version(args.get, args.version)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    else:
        print("Usage: --create <workflow_name> --workflow <json> or --get <workflow_name> [--version <v>]")
        sys.exit(1)

