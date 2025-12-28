#!/usr/bin/env python3
"""
Validate Python Hybrid n8n Workflow JSON
Checks workflow structure, Python script references, and environment variables

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python3 validate-hybrid-workflow.py <workflow.json>
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple

def validate_json_structure(workflow: Dict) -> Tuple[bool, List[str]]:
    """Validate basic JSON structure."""
    errors = []
    
    # Check required top-level fields
    required_fields = ['name', 'nodes', 'connections']
    for field in required_fields:
        if field not in workflow:
            errors.append(f"Missing required field: {field}")
    
    # Check nodes is a list
    if 'nodes' in workflow and not isinstance(workflow['nodes'], list):
        errors.append("'nodes' must be a list")
    
    # Check connections is a dict
    if 'connections' in workflow and not isinstance(workflow.get('connections'), dict):
        errors.append("'connections' must be a dict")
    
    return len(errors) == 0, errors

def validate_python_nodes(workflow: Dict, workflow_path: str) -> Tuple[bool, List[str]]:
    """Validate Python script execution nodes."""
    errors = []
    warnings = []
    
    python_nodes = []
    for node in workflow.get('nodes', []):
        if node.get('type') == 'n8n-nodes-base.executeCommand':
            params = node.get('parameters', {})
            command = params.get('command', '')
            if 'n8n-check-github.py' in command or 'n8n-check-netlify.py' in command:
                python_nodes.append({
                    'name': node.get('name', 'Unknown'),
                    'command': command
                })
    
    # Check Python nodes exist
    for node_info in python_nodes:
        # Extract script path from command
        command = node_info['command']
        if 'n8n-check-github.py' in command:
            script_name = 'n8n-check-github.py'
        elif 'n8n-check-netlify.py' in command:
            script_name = 'n8n-check-netlify.py'
        else:
            continue
        
        # Check if script exists
        script_path = Path(workflow_path) / 'scripts' / script_name
        if not script_path.exists():
            errors.append(f"Python script not found: {script_path}")
        elif not os.access(script_path, os.X_OK):
            warnings.append(f"Python script not executable: {script_path}")
    
    # Check for JSON parsing nodes after Python nodes
    node_names = [n.get('name', '') for n in workflow.get('nodes', [])]
    has_github_parser = any('Parse GitHub JSON' in name for name in node_names)
    has_netlify_parser = any('Parse Netlify JSON' in name for name in node_names)
    
    if any('Check GitHub' in n['name'] for n in python_nodes) and not has_github_parser:
        warnings.append("GitHub Python node found but no 'Parse GitHub JSON' node")
    
    if any('Check Netlify' in n['name'] for n in python_nodes) and not has_netlify_parser:
        warnings.append("Netlify Python node found but no 'Parse Netlify JSON' node")
    
    return len(errors) == 0, errors, warnings

def validate_environment_variables(workflow: Dict) -> Tuple[bool, List[str]]:
    """Check for required environment variable references."""
    errors = []
    warnings = []
    
    required_vars = [
        'WORKFLOW_PATH',
        'GITHUB_REPO_OWNER',
        'GITHUB_REPO_NAME',
        'GITHUB_WORKFLOW_FILE',
        'NETLIFY_SITE_ID'
    ]
    
    # Search for env var references in workflow JSON
    workflow_str = json.dumps(workflow)
    
    for var in required_vars:
        if f'$env.{var}' in workflow_str or f'${{$env.{var}}}' in workflow_str:
            continue
        elif var == 'WORKFLOW_PATH':
            # WORKFLOW_PATH is critical for Python scripts
            errors.append(f"Required environment variable not referenced: {var}")
        else:
            warnings.append(f"Environment variable may be needed: {var}")
    
    return len(errors) == 0, errors, warnings

def validate_connections(workflow: Dict) -> Tuple[bool, List[str]]:
    """Validate node connections."""
    errors = []
    warnings = []
    
    connections = workflow.get('connections', {})
    node_names = {n.get('name', ''): n.get('id', '') for n in workflow.get('nodes', [])}
    
    # Check that all connection targets exist
    for source_name, targets in connections.items():
        if source_name not in node_names:
            warnings.append(f"Connection source node not found: {source_name}")
            continue
        
        for output_list in targets.get('main', []):
            for target in output_list:
                target_name = target.get('node', '')
                if target_name and target_name not in node_names:
                    errors.append(f"Connection target node not found: {target_name} (from {source_name})")
    
    # Check Python nodes have parsing nodes after them
    python_node_names = [
        n.get('name', '') for n in workflow.get('nodes', [])
        if n.get('type') == 'n8n-nodes-base.executeCommand' and 
        ('n8n-check' in n.get('parameters', {}).get('command', ''))
    ]
    
    for python_node in python_node_names:
        # Check if there's a parser node connected after this
        found_parser = False
        if python_node in connections:
            for output_list in connections[python_node].get('main', []):
                for target in output_list:
                    target_name = target.get('node', '')
                    if 'Parse' in target_name and 'JSON' in target_name:
                        found_parser = True
                        break
        
        if not found_parser:
            warnings.append(f"Python node '{python_node}' may need a JSON parser node after it")
    
    return len(errors) == 0, errors, warnings

def validate_finalize_node(workflow: Dict) -> Tuple[bool, List[str]]:
    """Check Finalize Report node uses Python data."""
    errors = []
    warnings = []
    
    finalize_nodes = [
        n for n in workflow.get('nodes', [])
        if 'Finalize' in n.get('name', '') and n.get('type') == 'n8n-nodes-base.code'
    ]
    
    for node in finalize_nodes:
        code = node.get('parameters', {}).get('jsCode', '')
        
        # Check if it references Python parsed data
        if '$json.github' in code or '$json.netlify' in code:
            # Good - uses parsed data
            pass
        elif '$items(' in code and 'Check Latest' in code:
            # May be using old HTTP Request node references
            warnings.append(f"Finalize node '{node.get('name')}' may be using old HTTP Request references instead of Python data")
    
    return len(errors) == 0, errors, warnings

def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate-hybrid-workflow.py <workflow.json>")
        sys.exit(1)
    
    workflow_file = Path(sys.argv[1])
    if not workflow_file.exists():
        print(f"Error: Workflow file not found: {workflow_file}")
        sys.exit(1)
    
    # Get workflow path (parent directory of scripts)
    workflow_path = str(workflow_file.parent.parent) if 'Desktop' in str(workflow_file) else str(Path.cwd())
    
    print("🔍 Validating Python Hybrid n8n Workflow...")
    print("=" * 70)
    print(f"Workflow: {workflow_file}")
    print(f"Workflow Path: {workflow_path}")
    print()
    
    # Load workflow JSON
    try:
        with open(workflow_file, 'r') as f:
            workflow = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)
    
    all_errors = []
    all_warnings = []
    
    # Run validations
    print("📋 Running Validations...")
    print()
    
    # 1. JSON Structure
    valid, errors = validate_json_structure(workflow)
    if errors:
        all_errors.extend(errors)
    else:
        print("✅ JSON structure valid")
    
    # 2. Python Nodes
    valid, errors, warnings = validate_python_nodes(workflow, workflow_path)
    if errors:
        all_errors.extend(errors)
    if warnings:
        all_warnings.extend(warnings)
    if not errors:
        print("✅ Python script nodes valid")
    
    # 3. Environment Variables
    valid, errors, warnings = validate_environment_variables(workflow)
    if errors:
        all_errors.extend(errors)
    if warnings:
        all_warnings.extend(warnings)
    if not errors:
        print("✅ Environment variable references valid")
    
    # 4. Connections
    valid, errors, warnings = validate_connections(workflow)
    if errors:
        all_errors.extend(errors)
    if warnings:
        all_warnings.extend(warnings)
    if not errors:
        print("✅ Node connections valid")
    
    # 5. Finalize Node
    valid, errors, warnings = validate_finalize_node(workflow)
    if errors:
        all_errors.extend(errors)
    if warnings:
        all_warnings.extend(warnings)
    if not errors:
        print("✅ Finalize node configuration valid")
    
    print()
    print("=" * 70)
    
    # Report results
    if all_errors:
        print("❌ ERRORS FOUND:")
        for error in all_errors:
            print(f"   • {error}")
        print()
    
    if all_warnings:
        print("⚠️  WARNINGS:")
        for warning in all_warnings:
            print(f"   • {warning}")
        print()
    
    if not all_errors and not all_warnings:
        print("✅ All validations passed! Workflow is ready to import.")
        sys.exit(0)
    elif not all_errors:
        print("⚠️  Workflow has warnings but should import successfully.")
        sys.exit(0)
    else:
        print("❌ Workflow has errors. Please fix before importing.")
        sys.exit(1)

if __name__ == '__main__':
    main()


