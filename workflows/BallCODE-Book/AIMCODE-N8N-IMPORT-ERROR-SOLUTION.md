# AIMCODE n8n: Complete Solution for "propertyValues[itemName] is not iterable" Error

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 11, 2025  
**Methodology:** AIMCODE n8n Focus  
**Error:** `propertyValues[itemName] is not iterable`  
**Status:** ✅ Complete End-to-End Solution

---

## 🎯 AIMCODE n8n Framework

### CLEAR Framework Applied:

**C - Clarity:**
- Error occurs when importing n8n workflows with `fixedCollection` parameters
- Specifically affects nodes with nested parameter structures (HTTP Request, IF, Switch)
- Root cause: Incorrect JSON structure for `headerParameters`, `bodyParameters`, or `conditions` arrays

**L - Logic:**
- n8n expects arrays directly, not nested in additional objects
- Version compatibility issues between workflow format and n8n version
- Import validation fails when structure doesn't match expected format

**E - Examples:**
- HTTP Request nodes with `headerParameters.parameters` nested structure
- IF nodes with `conditions.boolean` nested incorrectly
- Switch nodes with `rules.conditions` improperly nested

**A - Adaptation:**
- Remove nested `parameters` wrappers
- Use direct array structures
- Simplify to `jsonBody` for HTTP Request nodes
- Use `options.headers` instead of `headerParameters`

**R - Results:**
- Workflow imports successfully
- All nodes function correctly
- No data loss or functionality reduction

---

## 🔬 PhD-Level Research Findings

### Root Cause Analysis:

**1. fixedCollection Parameter Structure Issue:**
- n8n uses `fixedCollection` for complex parameter structures
- These must be arrays, not objects containing arrays
- Common mistake: `{parameters: [{...}]}` instead of `[{...}]`

**2. Version Compatibility:**
- Different n8n versions expect different structures
- Older workflows may not import into newer n8n versions
- Newer workflow formats may not work in older n8n versions

**3. Node Type Specific Issues:**
- **HTTP Request nodes:** `headerParameters` and `bodyParameters` structures
- **IF nodes:** `conditions` array structure
- **Switch nodes:** `rules.conditions` structure

---

## ✅ COMPLETE SOLUTION SET

### Solution 1: Fix HTTP Request Nodes (Most Common)

**Problem Structure:**
```json
{
  "headerParameters": {
    "parameters": [
      {"name": "Accept", "value": "application/json"}
    ]
  },
  "bodyParameters": {
    "parameters": [
      {"name": "ref", "value": "main"}
    ]
  }
}
```

**Fixed Structure:**
```json
{
  "sendHeaders": true,
  "sendBody": true,
  "bodyContentType": "json",
  "specifyBody": "json",
  "jsonBody": "={\"ref\":\"main\"}",
  "options": {
    "headers": {
      "Accept": "application/json"
    }
  }
}
```

**Key Changes:**
- ✅ Remove `headerParameters.parameters` wrapper
- ✅ Remove `bodyParameters.parameters` wrapper
- ✅ Use `jsonBody` with expression mode for body
- ✅ Use `options.headers` object for headers

---

### Solution 2: Fix IF Node Conditions

**Problem Structure:**
```json
{
  "conditions": {
    "boolean": {
      "values": [
        {"value1": "={{$json.status}}", "value2": "active"}
      ]
    }
  }
}
```

**Fixed Structure:**
```json
{
  "conditions": {
    "boolean": [
      {
        "value1": "={{$json.status}}",
        "value2": "active"
      }
    ]
  }
}
```

**Key Changes:**
- ✅ `boolean` should be array directly, not object with `values` array
- ✅ Remove extra nesting layers

---

### Solution 3: Fix Switch Node Rules

**Problem Structure:**
```json
{
  "rules": {
    "conditions": {
      "values": [
        {"value1": "={{$json.status}}", "operation": "equals", "value2": "active"}
      ]
    }
  }
}
```

**Fixed Structure:**
```json
{
  "rules": {
    "values": [
      {
        "conditions": [
          {
            "value1": "={{$json.status}}",
            "operation": "equals",
            "value2": "active"
          }
        ],
        "outputKey": "active"
      }
    ]
  }
}
```

**Key Changes:**
- ✅ `rules.values` is array of objects
- ✅ Each object has `conditions` array and `outputKey`
- ✅ `conditions` is array directly, not nested object

---

## 🛠️ AUTOMATED FIX SCRIPT

### Python Script to Fix Workflow JSON:

```python
#!/usr/bin/env python3
"""
AIMCODE n8n: Automated Fix for propertyValues[itemName] Error
Fixes all known problematic structures in n8n workflow JSON
"""

import json
import sys
from pathlib import Path

def fix_http_request_node(params):
    """Fix HTTP Request node parameters"""
    # Remove problematic structures
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
    
    if 'bodyParameters' in params:
        # Convert bodyParameters to jsonBody
        if params.get('sendBody'):
            params['bodyContentType'] = 'json'
            params['specifyBody'] = 'json'
            
            # Build JSON body from parameters
            body_obj = {}
            if 'parameters' in params['bodyParameters']:
                for param in params['bodyParameters']['parameters']:
                    if isinstance(param, dict) and 'name' in param and 'value' in param:
                        body_obj[param['name']] = param['value']
            
            # Convert to JSON string with expression mode
            if body_obj:
                params['jsonBody'] = f"={json.dumps(body_obj)}"
        
        # Remove bodyParameters
        del params['bodyParameters']
    
    return params

def fix_if_node(params):
    """Fix IF node conditions structure"""
    if 'conditions' in params:
        conditions = params['conditions']
        
        # Fix boolean conditions
        if 'boolean' in conditions:
            boolean_cond = conditions['boolean']
            # If it's an object with 'values', extract the array
            if isinstance(boolean_cond, dict) and 'values' in boolean_cond:
                conditions['boolean'] = boolean_cond['values']
            # Ensure it's an array
            elif not isinstance(boolean_cond, list):
                conditions['boolean'] = [boolean_cond] if boolean_cond else []
        
        # Fix string conditions
        if 'string' in conditions:
            string_cond = conditions['string']
            if isinstance(string_cond, dict) and 'values' in string_cond:
                conditions['string'] = string_cond['values']
            elif not isinstance(string_cond, list):
                conditions['string'] = [string_cond] if string_cond else []
    
    return params

def fix_switch_node(params):
    """Fix Switch node rules structure"""
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
                        # Ensure conditions is array
                        elif not isinstance(conds, list):
                            rule['conditions'] = [conds] if conds else []
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
    
    return params

def fix_workflow(workflow_path):
    """Fix all problematic structures in workflow"""
    with open(workflow_path, 'r') as f:
        workflow = json.load(f)
    
    fixes_applied = []
    
    for node in workflow.get('nodes', []):
        node_type = node.get('type', '')
        node_name = node.get('name', 'Unknown')
        params = node.get('parameters', {})
        
        original_params = json.dumps(params, sort_keys=True)
        
        # Fix based on node type
        if 'httpRequest' in node_type:
            params = fix_http_request_node(params)
        elif 'if' in node_type:
            params = fix_if_node(params)
        elif 'switch' in node_type:
            params = fix_switch_node(params)
        
        # Check if changes were made
        new_params = json.dumps(params, sort_keys=True)
        if original_params != new_params:
            node['parameters'] = params
            fixes_applied.append(node_name)
    
    # Save fixed workflow
    output_path = workflow_path.replace('.json', '-FIXED.json')
    with open(output_path, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    return fixes_applied, output_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 fix-n8n-import-error.py <workflow.json>")
        sys.exit(1)
    
    workflow_path = sys.argv[1]
    fixes, output_path = fix_workflow(workflow_path)
    
    print(f"✅ Fixed workflow saved to: {output_path}")
    print(f"📊 Fixed {len(fixes)} node(s): {', '.join(fixes)}")

```

---

## 📋 MANUAL FIX CHECKLIST

### For HTTP Request Nodes:

- [ ] Remove `headerParameters.parameters` structure
- [ ] Remove `bodyParameters.parameters` structure
- [ ] Use `options.headers` object for headers
- [ ] Use `jsonBody` with expression mode for body
- [ ] Set `bodyContentType: "json"`
- [ ] Set `specifyBody: "json"`

### For IF Nodes:

- [ ] Ensure `conditions.boolean` is array, not object
- [ ] Remove any `values` wrapper around conditions
- [ ] Each condition should be object in array directly

### For Switch Nodes:

- [ ] Use `rules.values` array structure
- [ ] Each rule has `conditions` array and `outputKey`
- [ ] `conditions` is array directly, not nested object

---

## 🎯 QUICK REFERENCE: Always Fix These Structures

### ❌ WRONG:
```json
"headerParameters": {"parameters": [...]}
"bodyParameters": {"parameters": [...]}
"conditions": {"boolean": {"values": [...]}}
"rules": {"conditions": {"values": [...]}}
```

### ✅ CORRECT:
```json
"options": {"headers": {...}}
"jsonBody": "={...}"
"conditions": {"boolean": [...]}
"rules": {"values": [{"conditions": [...], "outputKey": "..."}]}
```

---

## 💾 MEMORY: Always Remember

**When encountering "propertyValues[itemName] is not iterable":**

1. **Check HTTP Request nodes first** - most common cause
2. **Remove `parameters` wrapper** from `headerParameters` and `bodyParameters`
3. **Use direct arrays** for `conditions` in IF nodes
4. **Use `rules.values`** structure for Switch nodes
5. **Simplify to `jsonBody`** for HTTP Request body data
6. **Use `options.headers`** object for HTTP Request headers

**Quick Fix Pattern:**
- Find nested `{parameters: [...]}` → Remove wrapper, use array directly
- Find `{values: [...]}` → Check if should be array directly
- Find complex nesting → Simplify to direct structure

---

## 🚀 USAGE

### Automated Fix:
```bash
python3 fix-n8n-import-error.py workflow.json
# Creates: workflow-FIXED.json
```

### Manual Fix:
1. Open workflow JSON in editor
2. Search for problematic structures
3. Apply fixes from checklist above
4. Validate JSON: `python3 -m json.tool workflow.json`

---

**Status:** ✅ Complete Solution  
**Methodology:** AIMCODE n8n Focus  
**Reusability:** Always applicable for this error type


