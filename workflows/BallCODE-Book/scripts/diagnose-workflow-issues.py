#!/usr/bin/env python3
"""
Diagnose n8n Workflow Issues - AIMCODE R&D
Identifies issues that cause "Could not find workflow" and "Could not find property option" errors

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path

def diagnose_workflow(file_path):
    """Diagnose workflow for common issues."""
    issues = []
    warnings = []
    
    try:
        with open(file_path, 'r') as f:
            workflow = json.load(f)
    except Exception as e:
        return [f"❌ Cannot read file: {e}"], []
    
    # Check 1: Empty options objects
    def check_node(node, node_name):
        node_issues = []
        node_warnings = []
        
        # Check for empty options
        if 'parameters' in node:
            params = node.get('parameters', {})
            if 'options' in params:
                options = params['options']
                if isinstance(options, dict) and len(options) == 0:
                    node_issues.append(f"Empty options: {{}} in {node_name}")
                elif isinstance(options, dict):
                    # Check for empty nested objects
                    for key, value in options.items():
                        if isinstance(value, dict) and len(value) == 0:
                            node_issues.append(f"Empty nested options.{key}: {{}} in {node_name}")
        
        # Check respondToWebhook nodes
        if node.get('type') == 'n8n-nodes-base.respondToWebhook':
            if node.get('typeVersion') == 1:
                if 'parameters' in node and 'options' in node['parameters']:
                    node_issues.append(f"respondToWebhook (typeVersion 1) has options property - NOT ALLOWED")
        
        # Check httpRequest nodes with options.headers
        if node.get('type') == 'n8n-nodes-base.httpRequest':
            params = node.get('parameters', {})
            if 'options' in params:
                options = params['options']
                if isinstance(options, dict) and 'headers' in options:
                    # This is valid, but check if it's empty
                    if isinstance(options['headers'], dict) and len(options['headers']) == 0:
                        node_warnings.append(f"Empty options.headers in {node_name}")
        
        return node_issues, node_warnings
    
    # Check all nodes
    for node in workflow.get('nodes', []):
        node_name = node.get('name', 'Unnamed')
        node_issues, node_warnings = check_node(node, node_name)
        issues.extend(node_issues)
        warnings.extend(node_warnings)
    
    # Check 2: Extra metadata properties
    metadata_props = ['updatedAt', 'createdAt', 'id', 'versionId', 'versionCounter', 
                     'activeVersionId', 'triggerCount']
    for prop in metadata_props:
        if prop in workflow:
            warnings.append(f"Has {prop} property (n8n generates this, may cause issues)")
    
    # Check 3: meta.templateCredsSetupCompleted
    if 'meta' in workflow and 'templateCredsSetupCompleted' in workflow.get('meta', {}):
        warnings.append("Has meta.templateCredsSetupCompleted (can cause issues)")
    
    # Check 4: Invalid connections
    connections = workflow.get('connections', {})
    node_names = {node.get('name'): node.get('id') for node in workflow.get('nodes', [])}
    
    for source_name, targets in connections.items():
        if source_name not in node_names:
            issues.append(f"Connection references non-existent node: {source_name}")
        if isinstance(targets, dict):
            for output_type, output_connections in targets.items():
                if isinstance(output_connections, list):
                    for connection_list in output_connections:
                        if isinstance(connection_list, list):
                            for connection in connection_list:
                                if isinstance(connection, dict):
                                    target_node = connection.get('node')
                                    if target_node and target_node not in node_names:
                                        issues.append(f"Connection to non-existent node: {target_node}")
    
    return issues, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/diagnose-workflow-issues.py <workflow-file.json>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    print("🔍 Diagnosing workflow for common issues...")
    print("=" * 70)
    print()
    
    issues, warnings = diagnose_workflow(file_path)
    
    if issues:
        print("❌ CRITICAL ISSUES FOUND:")
        print("-" * 70)
        for issue in issues:
            print(f"  • {issue}")
        print()
    else:
        print("✅ No critical issues found")
        print()
    
    if warnings:
        print("⚠️  WARNINGS:")
        print("-" * 70)
        for warning in warnings:
            print(f"  • {warning}")
        print()
    else:
        print("✅ No warnings")
        print()
    
    if issues:
        print("=" * 70)
        print("💡 RECOMMENDATIONS:")
        print("  1. Run: python scripts/clean-workflow-for-api.py <file> <output>")
        print("  2. Or use the cleaned workflow file if available")
        print("  3. Try importing in incognito/private browser window")
        print("  4. Clear browser cache")
        sys.exit(1)
    else:
        print("=" * 70)
        print("✅ Workflow structure looks good!")
        print("   If you still see 'Could not find workflow', try:")
        print("   1. Clear browser cache")
        print("   2. Try incognito/private window")
        print("   3. Check n8n version compatibility")

if __name__ == "__main__":
    main()


