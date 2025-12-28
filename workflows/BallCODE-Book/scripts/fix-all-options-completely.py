#!/usr/bin/env python3
"""
Completely remove ALL options properties from workflow
Ultra-aggressive cleaning for UI import
"""

import json
import sys

def remove_all_options_recursive(obj, path=""):
    """Recursively remove all 'options' keys from any dict"""
    if isinstance(obj, dict):
        # Remove 'options' key if it exists
        if 'options' in obj:
            del obj['options']
            print(f"Removed options from: {path}")
        
        # Recursively process all values
        for key, value in list(obj.items()):
            remove_all_options_recursive(value, f"{path}.{key}" if path else key)
    
    elif isinstance(obj, list):
        # Process each item in list
        for i, item in enumerate(obj):
            remove_all_options_recursive(item, f"{path}[{i}]" if path else f"[{i}]")

def clean_workflow_completely(workflow_data):
    """Ultra-aggressive cleaning - remove ALL options"""
    
    # Remove options from all nodes
    for node in workflow_data.get('nodes', []):
        params = node.get('parameters', {})
        remove_all_options_recursive(params, node.get('name', 'Unknown'))
    
    # Remove options from workflow level
    remove_all_options_recursive(workflow_data, "workflow")
    
    # Remove credentials (add manually in UI)
    for node in workflow_data.get('nodes', []):
        if 'credentials' in node:
            del node['credentials']
    
    # Create minimal structure
    cleaned = {
        'name': workflow_data.get('name'),
        'nodes': workflow_data.get('nodes', []),
        'connections': workflow_data.get('connections', {}),
        'settings': {
            'executionOrder': workflow_data.get('settings', {}).get('executionOrder', 'v1'),
            'timezone': workflow_data.get('settings', {}).get('timezone', 'America/New_York')
        }
    }
    
    return cleaned

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 fix-all-options-completely.py <input.json> <output.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        workflow = json.load(f)
    
    cleaned = clean_workflow_completely(workflow)
    
    with open(output_file, 'w') as f:
        json.dump(cleaned, f, indent=2)
    
    print(f"\n✅ Created ultra-clean version: {output_file}")
    print(f"   Nodes: {len(cleaned.get('nodes', []))}")

if __name__ == '__main__':
    main()


