#!/usr/bin/env python3
"""
Fix "Could not find property option" error - V3
Converts options.headers to direct headers (like Solution 5)
Removes all empty options objects
"""

import json
import sys

def fix_http_request_options(params):
    """Convert options.headers to direct headers (Solution 5 pattern)"""
    if 'options' in params and isinstance(params['options'], dict):
        options = params['options']
        
        # If options has headers, move them to direct headers
        if 'headers' in options:
            # Move headers out of options
            if 'headers' not in params:
                params['headers'] = options['headers']
            else:
                # Merge with existing headers
                params['headers'].update(options['headers'])
            del options['headers']
        
        # If options is now empty, remove it
        if len(options) == 0:
            del params['options']
        # If options has other properties, keep it but remove headers

def fix_node_options(node):
    """Fix options in a single node"""
    params = node.get('parameters', {})
    
    # Fix HTTP Request nodes (convert options.headers to direct headers)
    if node.get('type') == 'n8n-nodes-base.httpRequest':
        fix_http_request_options(params)
    
    # Remove empty options from any node
    if 'options' in params:
        if isinstance(params['options'], dict) and len(params['options']) == 0:
            del params['options']
    
    # respondToWebhook (typeVersion 1) should NEVER have options
    if node.get('type') == 'n8n-nodes-base.respondToWebhook':
        if 'options' in params:
            del params['options']
    
    # Webhook nodes should not have empty options
    if node.get('type') == 'n8n-nodes-base.webhook':
        if 'options' in params:
            if isinstance(params['options'], dict) and len(params['options']) == 0:
                del params['options']

def clean_workflow_v3(workflow_data):
    """Clean workflow using Solution 5 pattern (direct headers)"""
    
    # Fix each node
    for node in workflow_data.get('nodes', []):
        fix_node_options(node)
    
    # Remove credentials (user will add manually)
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
        print("Usage: python3 fix-options-error-v3.py <input.json> <output.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        workflow = json.load(f)
    
    cleaned = clean_workflow_v3(workflow)
    
    with open(output_file, 'w') as f:
        json.dump(cleaned, f, indent=2)
    
    # Report what was fixed
    http_nodes_fixed = 0
    empty_options_removed = 0
    respond_to_webhook_fixed = 0
    
    for node in cleaned.get('nodes', []):
        params = node.get('parameters', {})
        
        if node.get('type') == 'n8n-nodes-base.httpRequest':
            if 'headers' in params and 'options' not in params:
                http_nodes_fixed += 1
        
        if 'options' not in params:
            if node.get('type') == 'n8n-nodes-base.httpRequest' or node.get('type') == 'n8n-nodes-base.webhook':
                empty_options_removed += 1
        
        if node.get('type') == 'n8n-nodes-base.respondToWebhook' and 'options' not in params:
            respond_to_webhook_fixed += 1
    
    print(f"✅ Fixed {http_nodes_fixed} HTTP Request nodes (converted options.headers to direct headers)")
    print(f"✅ Removed empty options from {empty_options_removed} nodes")
    print(f"✅ Fixed {respond_to_webhook_fixed} respondToWebhook nodes")
    print(f"✅ Removed all credentials (add manually in UI)")
    print(f"✅ Output: {output_file}")

if __name__ == '__main__':
    main()

