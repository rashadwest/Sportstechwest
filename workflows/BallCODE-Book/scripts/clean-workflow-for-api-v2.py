#!/usr/bin/env python3
"""
Clean n8n workflow JSON for API import - V2 (Based on Successful Imports)
Removes ALL properties that n8n API doesn't accept

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys

def clean_workflow_for_api_v2(workflow_data):
    """
    Clean workflow based on successful imports and research.
    Only includes properties that n8n API accepts.
    """
    # Handle array or single workflow
    if isinstance(workflow_data, list):
        workflow = workflow_data[0] if workflow_data else {}
    else:
        workflow = workflow_data
    
    # Create minimal workflow - ONLY what API accepts
    cleaned = {}
    
    # Required properties
    cleaned['name'] = workflow.get('name', 'Workflow')
    cleaned['nodes'] = workflow.get('nodes', [])
    cleaned['connections'] = workflow.get('connections', {})
    
    # Settings - ONLY allowed properties
    settings = workflow.get('settings', {})
    cleaned_settings = {}
    
    # Only include these settings properties (based on research)
    if 'executionOrder' in settings:
        cleaned_settings['executionOrder'] = settings['executionOrder']
    else:
        cleaned_settings['executionOrder'] = 'v1'  # Default
    
    if 'timezone' in settings:
        cleaned_settings['timezone'] = settings['timezone']
    
    # DO NOT include: callerPolicy, availableInMCP (causes "must NOT have additional properties")
    cleaned['settings'] = cleaned_settings
    
    # Fix node-level issues
    if 'nodes' in cleaned:
        for node in cleaned['nodes']:
            params = node.get('parameters', {})
            changed = False
            
            # Fix 1: Remove empty options objects
            if 'options' in params:
                if params['options'] == {} or params['options'] is None:
                    del params['options']
                    changed = True
            
            # Fix 2: respondToWebhook (typeVersion 1) should NOT have options
            if node.get('type') == 'n8n-nodes-base.respondToWebhook' and node.get('typeVersion') == 1:
                if 'options' in params:
                    del params['options']
                    changed = True
            
            # Fix 3: Clean credentials structure (keep only what's needed)
            if 'credentials' in node:
                creds = node['credentials']
                if isinstance(creds, dict):
                    # Keep credentials structure but ensure it's valid
                    # API accepts: {"httpHeaderAuth": {"id": "...", "name": "..."}}
                    cleaned_creds = {}
                    for key, value in creds.items():
                        if isinstance(value, dict):
                            # Keep id and name if present
                            cleaned_creds[key] = {
                                k: v for k, v in value.items() 
                                if k in ['id', 'name']
                            }
                    if cleaned_creds:
                        node['credentials'] = cleaned_creds
                    else:
                        # If empty, remove it (credentials can be set in UI after import)
                        del node['credentials']
                    changed = True
            
            # Fix 4: Remove webhookId if it's causing issues (can be regenerated)
            # Actually, keep webhookId - it's needed for webhook nodes
            
            if changed:
                node['parameters'] = params
    
    return cleaned

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clean-workflow-for-api-v2.py <input.json> [output.json]")
        print("  If output.json is not provided, writes to <input-CLEANED-V2.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.json', '-CLEANED-V2.json')
    
    try:
        with open(input_file, 'r') as f:
            workflow = json.load(f)
        
        cleaned = clean_workflow_for_api_v2(workflow)
        
        with open(output_file, 'w') as f:
            json.dump(cleaned, f, indent=2)
        
        print(f"✅ Cleaned workflow saved to: {output_file}")
        print(f"   Properties: {list(cleaned.keys())}")
        print(f"   Settings: {list(cleaned.get('settings', {}).keys())}")
        print(f"   Nodes: {len(cleaned.get('nodes', []))}")
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

