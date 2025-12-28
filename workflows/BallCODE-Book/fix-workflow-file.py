#!/usr/bin/env python3
"""
n8n Workflow Fixer
Automatically fixes common issues in workflow JSON files

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any

class WorkflowFixer:
    def __init__(self, workflow_file: str, output_file: str = None):
        self.workflow_file = Path(workflow_file)
        self.output_file = Path(output_file) if output_file else self.workflow_file
        self.workflow = None
        self.fixes_applied = []
        
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
    
    def fix_placeholders(self):
        """Replace placeholder values with proper defaults"""
        # This is a template - customize based on your needs
        # Be careful not to replace legitimate values
        pass
    
    def fix_missing_fields(self):
        """Add missing required fields"""
        for node in self.workflow.get("nodes", []):
            node_name = node.get("name", "Unknown")
            node_type = node.get("type", "")
            params = node.setdefault("parameters", {})
            
            # Email sender nodes
            if "email" in node_type.lower() and "sender" in node_name.lower():
                if not params.get("message"):
                    params["message"] = "={{ $json.message || $json.body || $json.content || 'No message provided' }}"
                    self.fixes_applied.append(f"✅ {node_name}: Added message field")
                
                if not params.get("emailType"):
                    params["emailType"] = "text"
                    self.fixes_applied.append(f"✅ {node_name}: Set emailType to 'text'")
            
            # Code nodes - ensure proper return format
            if "code" in node_type.lower():
                js_code = params.get("jsCode", "")
                if js_code and "return" not in js_code:
                    self.fixes_applied.append(f"⚠️  {node_name}: Code node may not return data properly")
    
    def fix_expressions(self):
        """Improve expression syntax with optional chaining and fallbacks"""
        # This is complex - would need to parse expressions
        # For now, just flag potential issues
        pass
    
    def ensure_connections(self):
        """Ensure workflow has proper connections structure"""
        if "connections" not in self.workflow:
            self.workflow["connections"] = {}
            self.fixes_applied.append("✅ Added connections structure")
    
    def fix(self):
        """Apply all fixes"""
        if not self.load_workflow():
            return False
        
        print(f"🔧 Fixing workflow: {self.workflow_file.name}")
        print()
        
        self.fix_missing_fields()
        self.ensure_connections()
        # Add more fix methods as needed
        
        return True
    
    def save(self):
        """Save fixed workflow"""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(self.workflow, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Error saving workflow: {e}")
            return False
    
    def report(self):
        """Print fix report"""
        print("=" * 60)
        print("WORKFLOW FIX REPORT")
        print("=" * 60)
        print()
        
        if self.fixes_applied:
            print("✅ FIXES APPLIED:")
            for fix in self.fixes_applied:
                print(f"  {fix}")
            print()
        else:
            print("ℹ️  No fixes needed")
            print()
        
        print(f"📁 Output file: {self.output_file}")
        print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix-workflow-file.py <workflow.json> [output.json]")
        sys.exit(1)
    
    workflow_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    fixer = WorkflowFixer(workflow_file, output_file)
    
    if fixer.fix():
        if fixer.save():
            fixer.report()
            print("✅ Workflow fixed and saved!")
        else:
            print("❌ Failed to save fixed workflow")
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()




