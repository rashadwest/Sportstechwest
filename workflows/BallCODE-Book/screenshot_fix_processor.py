#!/usr/bin/env python3
"""
Screenshot Fix Processor
Processes fixes generated from screenshot analysis and applies them to files
"""

import sys
import json
import os
from pathlib import Path
from typing import Dict, Any

def update_n8n_workflow(workflow_path: str, node_id: str, updates: Dict[str, Any]) -> bool:
    """Update n8n workflow JSON file"""
    try:
        with open(workflow_path, 'r') as f:
            workflow = json.load(f)
        
        # Find node by ID or name
        for node in workflow.get('nodes', []):
            if node.get('id') == node_id or node.get('name') == node_id:
                # Update node parameters
                if 'parameters' not in node:
                    node['parameters'] = {}
                
                # Merge updates into parameters
                for key, value in updates.items():
                    if '.' in key:
                        # Handle nested keys (e.g., "options.temperature")
                        keys = key.split('.')
                        current = node['parameters']
                        for k in keys[:-1]:
                            if k not in current:
                                current[k] = {}
                            current = current[k]
                        current[keys[-1]] = value
                    else:
                        node['parameters'][key] = value
                
                # Write updated workflow
                with open(workflow_path, 'w') as f:
                    json.dump(workflow, f, indent=2)
                
                print(f"✅ Updated workflow: {workflow_path}")
                print(f"   Node: {node_id}")
                print(f"   Updates: {json.dumps(updates, indent=2)}")
                return True
        
        print(f"❌ Node not found: {node_id}")
        return False
        
    except Exception as e:
        print(f"❌ Error updating workflow: {e}")
        return False

def update_code_file(file_path: str, original_code: str, fixed_code: str) -> bool:
    """Update code file with fix"""
    try:
        full_path = Path(file_path)
        
        if not full_path.exists():
            print(f"❌ File not found: {file_path}")
            return False
        
        # Read current file
        with open(full_path, 'r') as f:
            current_content = f.read()
        
        # Replace original with fixed code
        if original_code in current_content:
            updated_content = current_content.replace(original_code, fixed_code)
        else:
            # If exact match not found, append fix (safer)
            print(f"⚠️  Original code not found exactly, appending fix as comment")
            updated_content = current_content + f"\n\n# AUTO-FIX APPLIED:\n{fixed_code}\n"
        
        # Write updated file
        with open(full_path, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Updated code file: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating code file: {e}")
        return False

def update_config_file(file_path: str, config_updates: Dict[str, Any]) -> bool:
    """Update configuration file"""
    try:
        full_path = Path(file_path)
        
        if not full_path.exists():
            print(f"❌ Config file not found: {file_path}")
            return False
        
        # Determine file type
        if file_path.endswith('.json'):
            with open(full_path, 'r') as f:
                config = json.load(f)
            
            # Merge updates
            config.update(config_updates)
            
            with open(full_path, 'w') as f:
                json.dump(config, f, indent=2)
        
        elif file_path.endswith('.env') or file_path.endswith('.toml'):
            # For .env or .toml files, append or update
            with open(full_path, 'r') as f:
                lines = f.readlines()
            
            # Update existing keys or append new ones
            updated_lines = []
            keys_to_add = set(config_updates.keys())
            
            for line in lines:
                for key, value in config_updates.items():
                    if line.startswith(f"{key}="):
                        updated_lines.append(f"{key}={value}\n")
                        keys_to_add.discard(key)
                        break
                else:
                    updated_lines.append(line)
            
            # Add new keys
            for key in keys_to_add:
                updated_lines.append(f"{key}={config_updates[key]}\n")
            
            with open(full_path, 'w') as f:
                f.writelines(updated_lines)
        
        print(f"✅ Updated config file: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating config file: {e}")
        return False

def process_fix(fix_data: Dict[str, Any], request_id: str) -> bool:
    """Process fix based on fix type"""
    fix_type = fix_data.get('fixType', 'unknown')
    file_path = fix_data.get('filePath', '')
    
    print(f"🔧 Processing fix: {fix_type}")
    print(f"   File: {file_path}")
    print(f"   Request ID: {request_id}")
    
    if fix_type == 'workflow_json':
        # Update n8n workflow JSON
        # Extract node ID and updates from fix
        node_id = fix_data.get('nodeId', '')
        updates = fix_data.get('updates', {})
        
        # Parse fixed code to extract updates
        fixed_code = fix_data.get('fixedCode', '{}')
        try:
            fixed_node = json.loads(fixed_code)
            if 'parameters' in fixed_node:
                updates = fixed_node['parameters']
        except:
            pass
        
        return update_n8n_workflow(file_path, node_id, updates)
    
    elif fix_type == 'code_file':
        # Update code file
        original_code = fix_data.get('originalCode', '')
        fixed_code = fix_data.get('fixedCode', '')
        return update_code_file(file_path, original_code, fixed_code)
    
    elif fix_type == 'config_file':
        # Update config file
        # Parse fixed code as config updates
        try:
            config_updates = json.loads(fix_data.get('fixedCode', '{}'))
        except:
            config_updates = {}
        return update_config_file(file_path, config_updates)
    
    else:
        print(f"❌ Unknown fix type: {fix_type}")
        return False

def main():
    """Main function"""
    if len(sys.argv) < 4:
        print("Usage: screenshot_fix_processor.py <file_path> <fix_json> <request_id>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    fix_json = sys.argv[2]
    request_id = sys.argv[3]
    
    try:
        fix_data = json.loads(fix_json)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)
    
    # Override file path if provided in fix data
    if 'filePath' in fix_data:
        file_path = fix_data['filePath']
    
    success = process_fix(fix_data, request_id)
    
    if success:
        print(f"✅ Fix applied successfully (Request: {request_id})")
        sys.exit(0)
    else:
        print(f"❌ Fix application failed (Request: {request_id})")
        sys.exit(1)

if __name__ == "__main__":
    main()



