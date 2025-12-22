#!/usr/bin/env python3
"""
n8n Workflow Debugger
Systematically analyzes workflow for common issues based on N8N_WORKFLOW_DEVELOPMENT_GUIDE.md

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

class WorkflowDebugger:
    def __init__(self, workflow_file: str):
        self.workflow_file = Path(workflow_file)
        self.workflow = None
        self.issues = []
        self.warnings = []
        
    def load_workflow(self):
        """Load workflow JSON file"""
        try:
            with open(self.workflow_file, 'r', encoding='utf-8') as f:
                self.workflow = json.load(f)
            return True
        except FileNotFoundError:
            print(f"❌ Error: Workflow file not found: {self.workflow_file}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON in workflow file: {e}")
            return False
    
    def check_placeholders(self):
        """Check for placeholder values"""
        workflow_str = json.dumps(self.workflow)
        placeholders = [
            "YOUR_", "PLACEHOLDER", "your-email", "your-api-key",
            "example.com", "localhost", "test@", "demo@"
        ]
        
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            params_str = json.dumps(node.get("parameters", {}))
            
            for placeholder in placeholders:
                if placeholder.lower() in params_str.lower():
                    self.issues.append(f"❌ {node_name}: Contains placeholder value ({placeholder})")
    
    def check_required_fields(self):
        """Check for missing required fields based on node type"""
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            node_type = node.get("type", "")
            params = node.get("parameters", {})
            
            # Email nodes
            if "email" in node_type.lower() or "email" in node_name.lower():
                if not params.get("message") and "sender" in node_name.lower():
                    self.issues.append(f"❌ {node_name}: Missing message body (required for email)")
                if "YOUR_" in str(params.get("fromEmail", "")):
                    self.issues.append(f"❌ {node_name}: Has placeholder email address")
            
            # Code nodes
            if "code" in node_type.lower():
                if not params.get("jsCode"):
                    self.warnings.append(f"⚠️  {node_name}: Code node has no JavaScript code")
            
            # OpenAI nodes
            if "openai" in node_type.lower() or "openAi" in node_type:
                if not params.get("model"):
                    self.issues.append(f"❌ {node_name}: Missing model parameter")
                if not params.get("messages"):
                    self.issues.append(f"❌ {node_name}: Missing messages parameter")
            
            # Execute Command nodes
            if "executeCommand" in node_type.lower():
                if not params.get("command"):
                    self.issues.append(f"❌ {node_name}: Missing command parameter")
    
    def check_connections(self):
        """Verify all nodes are properly connected"""
        connections = self.workflow.get("connections", {})
        node_names = {node.get("name"): node.get("id") for node in self.workflow.get("nodes", [])}
        
        # Check for orphaned nodes (nodes with no connections)
        connected_nodes = set()
        for source, targets in connections.items():
            connected_nodes.add(source)
            for target_list in targets.get("main", []):
                for target in target_list:
                    connected_nodes.add(target.get("node"))
        
        for node_name in node_names.keys():
            # Triggers don't need incoming connections
            node = next((n for n in self.workflow.get("nodes", []) if n.get("name") == node_name), None)
            if node and "trigger" not in node.get("type", "").lower():
                if node_name not in connected_nodes:
                    self.warnings.append(f"⚠️  {node_name}: No incoming connections (orphaned node?)")
    
    def check_expressions(self):
        """Check expression syntax and common issues"""
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            params_str = json.dumps(node.get("parameters", {}))
            
            # Check for expressions without optional chaining
            if "{{ $json." in params_str and "?." not in params_str:
                # This is a warning, not an error - some simple expressions don't need optional chaining
                if "{{ $json." in params_str and "||" not in params_str:
                    self.warnings.append(f"⚠️  {node_name}: Expression without fallback value (consider adding || 'default')")
    
    def check_data_flow(self):
        """Check data flow between nodes"""
        # This is a simplified check - full data flow analysis would be more complex
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            params_str = json.dumps(node.get("parameters", {}))
            
            # Check for references to previous nodes
            if "$('" in params_str or "$('" in params_str:
                # Extract referenced node names
                import re
                referenced = re.findall(r"\$\(['\"]([^'\"]+)['\"]\)", params_str)
                for ref_node in referenced:
                    # Check if referenced node exists
                    if not any(n.get("name") == ref_node for n in self.workflow.get("nodes", [])):
                        self.issues.append(f"❌ {node_name}: References non-existent node: {ref_node}")
    
    def check_credentials(self):
        """Check for credential references"""
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            credentials = node.get("credentials", {})
            
            if credentials:
                for cred_type, cred_data in credentials.items():
                    if not cred_data.get("id") and not cred_data.get("name"):
                        self.warnings.append(f"⚠️  {node_name}: Credential reference may be incomplete")
    
    def analyze(self):
        """Run all checks"""
        if not self.load_workflow():
            return False
        
        print(f"🔍 Analyzing workflow: {self.workflow_file.name}")
        print(f"   Nodes: {len(self.workflow.get('nodes', []))}")
        print()
        
        self.check_placeholders()
        self.check_required_fields()
        self.check_connections()
        self.check_expressions()
        self.check_data_flow()
        self.check_credentials()
        
        return True
    
    def report(self):
        """Print analysis report"""
        print("=" * 60)
        print("WORKFLOW ANALYSIS REPORT")
        print("=" * 60)
        print()
        
        if self.issues:
            print("❌ ISSUES FOUND:")
            for issue in self.issues:
                print(f"  {issue}")
            print()
        else:
            print("✅ No critical issues found!")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        # Summary
        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"  Critical Issues: {len(self.issues)}")
        print(f"  Warnings: {len(self.warnings)}")
        print()
        
        if self.issues:
            print("❌ Workflow has issues that should be fixed before deployment")
            return False
        elif self.warnings:
            print("⚠️  Workflow has warnings - review before deployment")
            return True
        else:
            print("✅ Workflow looks good! Ready for deployment")
            return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 debug-workflow.py <workflow.json>")
        sys.exit(1)
    
    workflow_file = sys.argv[1]
    debugger = WorkflowDebugger(workflow_file)
    
    if debugger.analyze():
        success = debugger.report()
        sys.exit(0 if success else 1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()



