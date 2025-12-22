#!/usr/bin/env python3
"""
Clean n8n workflow JSON for API import
Removes metadata properties that n8n API doesn't accept

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys

def clean_workflow_for_api(workflow_data):
    """
    Remove properties that n8n API doesn't accept when creating workflows.
    These are internal metadata fields that n8n manages itself.
    """
    # Properties to remove (n8n API doesn't accept these)
    properties_to_remove = [
        'id',              # n8n generates this
        'updatedAt',      # n8n manages this
        'createdAt',      # n8n manages this
        'versionId',      # n8n manages this
        'activeVersionId', # n8n manages this
        'versionCounter', # n8n manages this
        'triggerCount',   # n8n calculates this
        'isArchived',     # Can be set via API but often causes issues
    ]
    
    # Handle both single workflow and array of workflows
    # n8n API expects a single workflow object, not an array
    if isinstance(workflow_data, list):
        # If it's an array, take the first workflow
        workflow = workflow_data[0] if workflow_data else {}
    else:
        workflow = workflow_data
    
    cleaned = {}
    
    # Copy only allowed properties (n8n API is very strict)
    # Based on n8n API docs, these are the only properties accepted for POST /api/v1/workflows
    allowed_properties = [
        'name',           # Required
        'nodes',          # Required
        'connections',    # Required
        'settings',       # Optional but recommended
        'staticData',     # Optional
        'pinData',        # Optional
        # 'tags' is read-only and cannot be set via API
    ]
    # NOTE: 'description', 'active', 'meta', 'tags' are NOT accepted by API
    # They must be set via separate API calls after creation
    
    for prop in allowed_properties:
        if prop in workflow:
            cleaned[prop] = workflow[prop]
    
    # Ensure settings exists with minimal structure
    if 'settings' not in cleaned:
        cleaned['settings'] = {}
    if 'executionOrder' not in cleaned['settings']:
        cleaned['settings']['executionOrder'] = 'v1'
    
    # Remove tags (read-only, cannot be set via API)
    cleaned.pop('tags', None)
    
    # Remove null/empty optional properties that might cause issues
    for prop in ['staticData', 'pinData']:
        if prop in cleaned and (cleaned[prop] is None or cleaned[prop] == {}):
            cleaned.pop(prop, None)
    
    # Fix node-level issues that cause "Could not find property option" error
    # Based on research: empty options, respondToWebhook with options, etc.
    if 'nodes' in cleaned:
        fixes_applied = []
        for node in cleaned['nodes']:
            node_type = node.get('type', '')
            node_name = node.get('name', 'Unknown')
            params = node.get('parameters', {})
            changed = False
            
            # Fix 1: Remove empty options objects (causes "Could not find property option")
            if 'options' in params:
                if params['options'] == {} or params['options'] is None:
                    del params['options']
                    changed = True
                    fixes_applied.append(f"{node_name}: removed empty options")
            
            # Fix 2: respondToWebhook nodes (typeVersion 1) should NOT have options
            if 'respondToWebhook' in node_type and node.get('typeVersion') == 1:
                if 'options' in params:
                    del params['options']
                    changed = True
                    fixes_applied.append(f"{node_name}: removed options from respondToWebhook v1")
            
            # Fix 3: Webhook nodes - remove empty options
            if 'webhook' in node_type.lower() and 'options' in params:
                if params['options'] == {} or params['options'] is None:
                    del params['options']
                    changed = True
                    fixes_applied.append(f"{node_name}: removed empty options from webhook")
            
            if changed:
                node['parameters'] = params
        
        if fixes_applied:
            print(f"   Fixed {len(fixes_applied)} node-level issues:")
            for fix in fixes_applied[:5]:  # Show first 5
                print(f"     - {fix}")
    
    # Always return a single workflow object (not array) for API
    return cleaned

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clean-workflow-for-api.py <input.json> [output.json]")
        print("  If output.json is not provided, writes to <input-CLEANED.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.json', '-CLEANED.json')
    
    try:
        with open(input_file, 'r') as f:
            workflow = json.load(f)
        
        cleaned = clean_workflow_for_api(workflow)
        
        with open(output_file, 'w') as f:
            json.dump(cleaned, f, indent=2)
        
        print(f"✅ Cleaned workflow saved to: {output_file}")
        print(f"   Removed: id, updatedAt, createdAt, versionId, triggerCount, isArchived, tags, meta, active, description")
        return 0
    
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_file}")
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {input_file}: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())

