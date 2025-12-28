#!/usr/bin/env python3
"""
Robot: Import & Test CES Launch Workflow
Imports CES launch workflow to n8n and tests execution

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
import requests
from pathlib import Path
from typing import Dict, Optional, List

PROJECT_ROOT = Path(__file__).parent.parent
WORKFLOW_FILE = PROJECT_ROOT / "n8n-ces-launch-automation-workflow.json"
N8N_URL = os.getenv("N8N_URL", "http://192.168.1.226:5678")
N8N_API_KEY = os.getenv("N8N_API_KEY", "")

class CESWorkflowImporter:
    """Robot to import and test CES launch workflow"""
    
    def __init__(self):
        self.n8n_url = N8N_URL
        self.api_key = N8N_API_KEY
        self.workflow_file = WORKFLOW_FILE
    
    def check_n8n_accessible(self) -> bool:
        """Check if n8n instance is accessible"""
        try:
            response = requests.get(f"{self.n8n_url}/healthz", timeout=5)
            return response.status_code == 200
        except:
            try:
                response = requests.get(f"{self.n8n_url}", timeout=5)
                return response.status_code == 200
            except:
                return False
    
    def load_workflow(self) -> Dict:
        """Load workflow JSON file"""
        if not self.workflow_file.exists():
            raise FileNotFoundError(f"Workflow file not found: {self.workflow_file}")
        
        with open(self.workflow_file, 'r') as f:
            workflow = json.load(f)
        
        return workflow
    
    def clean_workflow_for_api(self, workflow: Dict) -> Dict:
        """Clean workflow JSON for n8n API (remove unsupported fields)"""
        # n8n API only accepts specific fields
        cleaned = {
            "name": workflow.get("name", "CES Launch Automation"),
            "nodes": workflow.get("nodes", []),
            "connections": workflow.get("connections", {}),
            "settings": workflow.get("settings", {}),
            "staticData": workflow.get("staticData"),
            "tags": workflow.get("tags", [])
        }
        
        # Remove null staticData
        if cleaned["staticData"] is None:
            del cleaned["staticData"]
        
        return cleaned
    
    def import_workflow(self, workflow: Dict) -> tuple[bool, Optional[str], Optional[str]]:
        """Import workflow to n8n via API"""
        cleaned_workflow = self.clean_workflow_for_api(workflow)
        
        url = f"{self.n8n_url}/api/v1/workflows"
        headers = {
            "Content-Type": "application/json"
        }
        
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        
        try:
            response = requests.post(url, json=cleaned_workflow, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                result = response.json()
                workflow_id = result.get("id") or result.get("data", {}).get("id")
                return True, workflow_id, None
            else:
                error_msg = response.text
                return False, None, f"HTTP {response.status_code}: {error_msg}"
        
        except requests.exceptions.RequestException as e:
            return False, None, str(e)
    
    def check_workflow_exists(self, workflow_name: str) -> Optional[str]:
        """Check if workflow already exists"""
        url = f"{self.n8n_url}/api/v1/workflows"
        headers = {}
        
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                workflows = response.json().get("data", [])
                for wf in workflows:
                    if wf.get("name") == workflow_name:
                        return wf.get("id")
        except:
            pass
        
        return None
    
    def test_workflow_execution(self, workflow_id: str) -> tuple[bool, str]:
        """Test workflow execution (manual trigger)"""
        url = f"{self.n8n_url}/api/v1/workflows/{workflow_id}/execute"
        headers = {
            "Content-Type": "application/json"
        }
        
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        
        try:
            # Execute workflow
            response = requests.post(url, json={}, headers=headers, timeout=60)
            
            if response.status_code == 200:
                return True, "Workflow executed successfully"
            else:
                return False, f"Execution failed: HTTP {response.status_code}"
        
        except requests.exceptions.RequestException as e:
            return False, f"Execution error: {str(e)}"
    
    def verify_workflow_structure(self, workflow: Dict) -> tuple[bool, List[str]]:
        """Verify workflow structure and identify issues"""
        issues = []
        
        # Check required fields
        if not workflow.get("nodes"):
            issues.append("Missing 'nodes' field")
        
        if not workflow.get("connections"):
            issues.append("Missing 'connections' field")
        
        # Check for schedule trigger
        has_trigger = False
        for node in workflow.get("nodes", []):
            if node.get("type") == "n8n-nodes-base.scheduleTrigger":
                has_trigger = True
                # Check cron expression
                params = node.get("parameters", {})
                cron = params.get("rule", {}).get("interval", [{}])[0].get("expression", "")
                if cron:
                    print(f"   ✅ Schedule trigger found: {cron}")
                else:
                    issues.append("Schedule trigger missing cron expression")
        
        if not has_trigger:
            issues.append("No schedule trigger found (workflow won't auto-run)")
        
        # Check for required nodes
        node_types = [node.get("type") for node in workflow.get("nodes", [])]
        required_types = [
            "n8n-nodes-base.code",  # Load schools
            "n8n-nodes-base.mailchimp",  # Send email
        ]
        
        for req_type in required_types:
            if req_type not in node_types:
                issues.append(f"Missing required node type: {req_type}")
        
        return len(issues) == 0, issues
    
    def print_import_instructions(self, workflow_name: str):
        """Print UI import instructions"""
        print("\n" + "=" * 70)
        print("📋 UI Import Instructions (If API Import Fails)")
        print("=" * 70)
        print(f"\n1. Open n8n in browser:")
        print(f"   {self.n8n_url}")
        print(f"\n2. Click 'Workflows' in left sidebar")
        print(f"\n3. Click 'Import from File' button (top right)")
        print(f"\n4. Select this file:")
        print(f"   {self.workflow_file.absolute()}")
        print(f"\n5. Click 'Import'")
        print(f"\n6. After import, activate the workflow:")
        print(f"   - Open the workflow: '{workflow_name}'")
        print(f"   - Toggle 'Active' switch ON (top-right)")
        print(f"   - Verify schedule trigger is set to: Jan 7, 9 AM")
        print("=" * 70)


def main():
    """Main robot function"""
    print("\n" + "=" * 70)
    print("🤖 Robot: Import & Test CES Launch Workflow")
    print("=" * 70)
    
    importer = CESWorkflowImporter()
    
    # Step 1: Check n8n accessibility
    print("\n📡 Step 1: Checking n8n accessibility...")
    if not importer.check_n8n_accessible():
        print(f"❌ n8n not accessible at {importer.n8n_url}")
        print("   Please check:")
        print("   1. n8n is running")
        print("   2. URL is correct")
        print("   3. Network connection")
        sys.exit(1)
    print(f"✅ n8n is accessible at {importer.n8n_url}")
    
    # Step 2: Load workflow
    print("\n📄 Step 2: Loading workflow file...")
    try:
        workflow = importer.load_workflow()
        workflow_name = workflow.get("name", "CES Launch Automation")
        print(f"✅ Workflow loaded: {workflow_name}")
        print(f"   Nodes: {len(workflow.get('nodes', []))}")
        print(f"   Connections: {len(workflow.get('connections', {}))}")
    except Exception as e:
        print(f"❌ Error loading workflow: {e}")
        sys.exit(1)
    
    # Step 3: Verify workflow structure
    print("\n🔍 Step 3: Verifying workflow structure...")
    is_valid, issues = importer.verify_workflow_structure(workflow)
    if not is_valid:
        print("⚠️  Workflow structure issues found:")
        for issue in issues:
            print(f"   - {issue}")
        print("\n   Workflow may still work, but review these issues.")
    else:
        print("✅ Workflow structure verified")
    
    # Step 4: Check if workflow already exists
    print("\n🔎 Step 4: Checking if workflow already exists...")
    existing_id = importer.check_workflow_exists(workflow_name)
    if existing_id:
        print(f"⚠️  Workflow '{workflow_name}' already exists (ID: {existing_id})")
        print("   Skipping import. Use n8n UI to update if needed.")
        workflow_id = existing_id
    else:
        # Step 5: Import workflow
        print("\n📤 Step 5: Importing workflow to n8n...")
        if not importer.api_key:
            print("⚠️  No API key configured. Cannot import via API.")
            print("   Use UI import instead (instructions below).")
            importer.print_import_instructions(workflow_name)
            sys.exit(0)
        
        success, workflow_id, error = importer.import_workflow(workflow)
        if success:
            print(f"✅ Workflow imported successfully!")
            print(f"   Workflow ID: {workflow_id}")
        else:
            print(f"❌ Import failed: {error}")
            print("\n   Trying UI import instead...")
            importer.print_import_instructions(workflow_name)
            sys.exit(1)
    
    # Step 6: Test workflow (optional)
    print("\n🧪 Step 6: Testing workflow execution...")
    if workflow_id:
        test_success, test_message = importer.test_workflow_execution(workflow_id)
        if test_success:
            print(f"✅ {test_message}")
        else:
            print(f"⚠️  {test_message}")
            print("   This is normal if workflow requires credentials or specific data.")
    
    # Final instructions
    print("\n" + "=" * 70)
    print("✅ Import Complete!")
    print("=" * 70)
    print("\n📋 Next Steps:")
    print("1. Open n8n UI and verify workflow is imported")
    print("2. Configure credentials (Mailchimp, HubSpot, Buffer)")
    print("3. Activate workflow (toggle 'Active' switch)")
    print("4. Verify schedule trigger is set to: Jan 7, 9 AM")
    print("5. Test workflow execution manually")
    print("6. Monitor workflow on launch day (Jan 7)")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

