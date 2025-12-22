#!/usr/bin/env python3
"""
AIMCODE n8n: Automated Fix for propertyValues[itemName] Error
Fixes all known problematic structures in n8n workflow JSON

Copyright © 2025 Rashad West. All Rights Reserved.

Usage: python3 fix-n8n-import-error.py <workflow.json>
"""

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

def normalize_options_key(params):
    """
    Some broken exports use 'option' (singular) instead of 'options' (plural).
    n8n nodes generally expect 'options'.
    """
    changed = False
    if isinstance(params, dict) and 'option' in params and 'options' not in params:
        if isinstance(params['option'], dict):
            params['options'] = params['option']
            del params['option']
            changed = True
    return params, changed

def remove_empty_options(params):
    """
    Removes empty options objects which can break imports on some node types/versions.
    Also prunes empty nested objects under options.
    """
    changed = False
    if not isinstance(params, dict) or 'options' not in params:
        return params, changed

    opt = params.get('options')
    if opt == {}:
        del params['options']
        return params, True

    if isinstance(opt, dict):
        cleaned = {k: v for k, v in opt.items() if v not in ({}, [], None, '')}
        if cleaned != opt:
            changed = True
        if cleaned:
            params['options'] = cleaned
        else:
            del params['options']
            changed = True

    return params, changed

def fix_http_request_node(params):
    """Fix HTTP Request node parameters - removes problematic nested structures"""
    changed = False
    
    # Remove headerParameters wrapper
    if 'headerParameters' in params:
        # Move headers to options.headers
        if 'options' not in params:
            params['options'] = {}
        if 'headers' not in params['options']:
            params['options']['headers'] = {}
        
        # Extract headers from headerParameters
        if 'parameters' in params['headerParameters']:
            for header in params['headerParameters']['parameters']:
                if isinstance(header, dict) and 'name' in header and 'value' in header:
                    params['options']['headers'][header['name']] = header['value']
        
        # Remove headerParameters
        del params['headerParameters']
        changed = True
    
    # Remove bodyParameters wrapper, convert to jsonBody
    if 'bodyParameters' in params:
        if params.get('sendBody'):
            params['bodyContentType'] = 'json'
            params['specifyBody'] = 'json'
            
            # Build JSON body from parameters
            body_obj = {}
            if 'parameters' in params['bodyParameters']:
                for param in params['bodyParameters']['parameters']:
                    if isinstance(param, dict) and 'name' in param and 'value' in param:
                        # Preserve expression mode if present
                        val = param['value']
                        body_obj[param['name']] = val
            
            # Convert to JSON string with expression mode
            if body_obj:
                # Simple approach: use JSON.stringify in expression
                body_str = json.dumps(body_obj)
                params['jsonBody'] = f"={{ JSON.stringify({body_str}) }}"
        
        # Remove bodyParameters
        del params['bodyParameters']
        changed = True
    
    return params, changed

def fix_if_node(params):
    """Fix IF node conditions structure - ensures arrays are direct, not nested"""
    changed = False
    
    if 'conditions' in params:
        conditions = params['conditions']
        
        # Fix boolean conditions
        if 'boolean' in conditions:
            boolean_cond = conditions['boolean']
            # If it's an object with 'values', extract the array
            if isinstance(boolean_cond, dict) and 'values' in boolean_cond:
                conditions['boolean'] = boolean_cond['values']
                changed = True
            # Ensure it's an array
            elif not isinstance(boolean_cond, list):
                conditions['boolean'] = [boolean_cond] if boolean_cond else []
                changed = True
        
        # Fix string conditions
        if 'string' in conditions:
            string_cond = conditions['string']
            if isinstance(string_cond, dict) and 'values' in string_cond:
                conditions['string'] = string_cond['values']
                changed = True
            elif not isinstance(string_cond, list):
                conditions['string'] = [string_cond] if string_cond else []
                changed = True
    
    return params, changed

def fix_switch_node(params):
    """Fix Switch node rules structure - corrects nested conditions"""
    changed = False
    
    if 'rules' in params:
        rules = params['rules']
        
        # Fix rules.values structure
        if 'values' in rules:
            if isinstance(rules['values'], list):
                # Ensure each rule has correct structure
                for rule in rules['values']:
                    if 'conditions' in rule:
                        conds = rule['conditions']
                        # If conditions is object with 'values', extract array
                        if isinstance(conds, dict) and 'values' in conds:
                            rule['conditions'] = conds['values']
                            changed = True
                        # Ensure conditions is array
                        elif not isinstance(conds, list):
                            rule['conditions'] = [conds] if conds else []
                            changed = True
        elif 'conditions' in rules:
            # Old format: rules.conditions instead of rules.values
            conds = rules['conditions']
            if isinstance(conds, dict) and 'values' in conds:
                params['rules'] = {
                    'values': [
                        {
                            'conditions': conds['values'],
                            'outputKey': 'output1'
                        }
                    ]
                }
                changed = True
    
    return params, changed

def fix_respond_to_webhook_node(params):
    """
    Some n8n versions reject respondToWebhook nodes with an 'options' param,
    especially when it's empty. We only strip it when empty/meaningless.
    """
    changed = False
    params, c1 = remove_empty_options(params)
    changed = changed or c1
    return params, changed

def fix_if_node_v2(params):
    """
    n8n v2+ If node uses a different condition structure.
    Convert common legacy structures to the v2 format.
    """
    # Already v2-shaped?
    if isinstance(params, dict) and isinstance(params.get('conditions', {}).get('conditions'), list):
        return params, False

    # Try to extract a leftValue from common legacy shapes
    left_value = None
    conds = (params or {}).get('conditions', {}) if isinstance(params, dict) else {}
    try:
        # legacy: conditions.boolean[0].value1
        if isinstance(conds.get('boolean'), list) and conds['boolean']:
            left_value = conds['boolean'][0].get('value1')
    except Exception:
        pass
    try:
        # legacy: conditions.string[0].value1
        if left_value is None and isinstance(conds.get('string'), list) and conds['string']:
            left_value = conds['string'][0].get('value1')
    except Exception:
        pass

    if not left_value:
        # safe default; callers may override later
        left_value = "={{ $json.proceed }}"

    new_params = {
        "conditions": {
            "options": {
                "leftValue": "",
                "caseSensitive": True,
                "typeValidation": "strict",
            },
            "conditions": [
                {
                    "id": str(uuid.uuid4()),
                    "leftValue": left_value,
                    "rightValue": True,
                    "operator": {
                        "type": "boolean",
                        "operation": "true",
                    },
                }
            ],
            "combinator": "and",
        },
        "options": {},
    }
    return new_params, True

def ensure_node_options_param(params):
    """
    Many nodes have an 'options' parameter in their schema. Some exports omit it,
    but some importers are stricter. Add options: {} when safe.
    """
    if not isinstance(params, dict):
        return params, False
    if 'options' not in params:
        params['options'] = {}
        return params, True
    if params.get('options') is None:
        params['options'] = {}
        return params, True
    return params, False

def to_importable_export_format(workflow):
    """
    Convert a simple workflow export (name/nodes/connections/...) into the
    full export-format entity array that n8n CLI/UI can reliably import.
    """
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    base = {
        "updatedAt": now,
        "createdAt": now,
        "id": str(uuid.uuid4()),
        "name": workflow.get("name", "Imported workflow"),
        "description": workflow.get("description"),
        "active": bool(workflow.get("active", False)),
        "isArchived": bool(workflow.get("isArchived", False)),
        "nodes": workflow.get("nodes", []),
        "connections": workflow.get("connections", {}),
        "settings": workflow.get("settings", {"executionOrder": "v1"}),
        "staticData": workflow.get("staticData"),
        "meta": workflow.get("meta", {"templateCredsSetupCompleted": True}),
        "pinData": workflow.get("pinData", {}),
        "versionId": workflow.get("versionId") or str(uuid.uuid4()),
        "activeVersionId": workflow.get("activeVersionId"),
        "versionCounter": int(workflow.get("versionCounter") or 1),
        "triggerCount": int(workflow.get("triggerCount") or 0),
        # tags must be array of objects in modern exports; safest is empty array
        "tags": [],
    }
    return [base]

def fix_workflow(workflow_path):
    """Fix all problematic structures in workflow using AIMCODE n8n methodology"""
    with open(workflow_path, 'r') as f:
        workflow = json.load(f)
    
    fixes_applied = []

    # Support both {workflow} and [{workflow}] inputs
    workflow_obj = workflow[0] if isinstance(workflow, list) and workflow else workflow

    for node in workflow_obj.get('nodes', []):
        node_type = node.get('type', '')
        node_name = node.get('name', 'Unknown')
        params = node.get('parameters', {})
        
        changed = False

        # Global normalizations first
        params, c0 = normalize_options_key(params)
        changed = changed or c0
        
        # Fix based on node type
        if 'httpRequest' in node_type:
            params, c = fix_http_request_node(params)
            changed = changed or c
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt
        elif 'if' in node_type:
            params, c = fix_if_node(params)
            changed = changed or c
            # Upgrade legacy IF node structures to v2 schema
            params, c_v2 = fix_if_node_v2(params)
            changed = changed or c_v2
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt
        elif 'switch' in node_type:
            params, c = fix_switch_node(params)
            changed = changed or c
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt
        elif 'respondToWebhook' in node_type:
            params, c = fix_respond_to_webhook_node(params)
            changed = changed or c
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt
        elif 'webhook' in node_type:
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt
        elif 'wait' in node_type:
            params, c_opt = ensure_node_options_param(params)
            changed = changed or c_opt

        # Global cleanup last
        params, c2 = remove_empty_options(params)
        changed = changed or c2
        
        # Update node if changes were made
        if changed:
            node['parameters'] = params
            fixes_applied.append(node_name)
    
    # Save fixed workflow (same shape as input)
    output_path = workflow_path.replace('.json', '-FIXED.json')
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    # Also save an export-format importable version for stricter n8n versions
    importable = to_importable_export_format(workflow_obj)
    importable_path = workflow_path.replace('.json', '-IMPORTABLE.json')
    with open(importable_path, 'w') as f:
        json.dump(importable, f, indent=2)
    
    return fixes_applied, output_path, importable_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 fix-n8n-import-error.py <workflow.json>")
        print("Output: Creates <workflow-FIXED.json>")
        sys.exit(1)
    
    workflow_path = sys.argv[1]
    
    if not Path(workflow_path).exists():
        print(f"❌ Error: File not found: {workflow_path}")
        sys.exit(1)
    
    try:
        fixes, output_path, importable_path = fix_workflow(workflow_path)
        
        print("=" * 70)
        print("✅ AIMCODE n8n: Workflow Fixed Successfully")
        print("=" * 70)
        print(f"📁 Fixed workflow saved to: {output_path}")
        print(f"📦 Importable (export-format) saved to: {importable_path}")
        print(f"📊 Fixed {len(fixes)} node(s)")
        if fixes:
            print(f"   Nodes: {', '.join(fixes)}")
        print("=" * 70)
        print("")
        print("Next steps:")
        print(f"  1. Import {importable_path} into n8n (recommended)")
        print(f"  2. If UI import supports it, {output_path} may also work")
        print("  2. Verify all nodes are configured correctly")
        print("  3. Test workflow execution")
        
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in workflow file")
        print(f"   {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

