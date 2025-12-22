#!/usr/bin/env python3
"""
n8n Workflow Updater
Updates workflow in n8n via REST API

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
import requests
from pathlib import Path
from typing import Optional

class WorkflowUpdater:
    def __init__(self):
        self.n8n_url = os.getenv("N8N_URL", "http://localhost:5678")
        self.api_key = os.getenv("N8N_API_KEY")
        self.workflow_id = os.getenv("WORKFLOW_ID")
        self.workflow_file = os.getenv("WORKFLOW_FILE")
        
    def load_workflow(self, filepath: str) -> Optional[dict]:
        """Load workflow JSON file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Error: Workflow file not found: {filepath}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON: {e}")
            return None
    
    def get_headers(self):
        """Get API request headers"""
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["X-N8N-API-KEY"] = self.api_key
        return headers
    
    def update_workflow(self, workflow_data: dict) -> bool:
        """Update workflow in n8n"""
        if not self.workflow_id:
            print("❌ Error: WORKFLOW_ID environment variable not set")
            return False
        
        url = f"{self.n8n_url}/api/v1/workflows/{self.workflow_id}"
        headers = self.get_headers()
        
        # Set workflow ID in data
        workflow_data["id"] = self.workflow_id
        
        try:
            response = requests.put(url, json=workflow_data, headers=headers, timeout=30)
            
            if response.status_code == 200:
                print(f"✅ Workflow updated successfully!")
                result = response.json()
                print(f"   Workflow ID: {result.get('id')}")
                print(f"   Name: {result.get('name')}")
                return True
            else:
                print(f"❌ Error updating workflow (HTTP {response.status_code})")
                print(f"   Response: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Error connecting to n8n: {e}")
            return False
    
    def create_workflow(self, workflow_data: dict) -> bool:
        """Create new workflow in n8n"""
        url = f"{self.n8n_url}/api/v1/workflows"
        headers = self.get_headers()
        
        try:
            response = requests.post(url, json=workflow_data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                print(f"✅ Workflow created successfully!")
                result = response.json()
                workflow_id = result.get('id')
                print(f"   Workflow ID: {workflow_id}")
                print(f"   Name: {result.get('name')}")
                print(f"\n   Save this ID for future updates:")
                print(f"   export WORKFLOW_ID='{workflow_id}'")
                return True
            else:
                print(f"❌ Error creating workflow (HTTP {response.status_code})")
                print(f"   Response: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Error connecting to n8n: {e}")
            return False
    
    def run(self):
        """Main execution"""
        if not self.workflow_file:
            print("❌ Error: WORKFLOW_FILE environment variable not set")
            print("\nUsage:")
            print("  export N8N_URL='http://your-n8n-instance:5678'")
            print("  export N8N_API_KEY='your-api-key'  # Optional")
            print("  export WORKFLOW_FILE='workflow.json'")
            print("  export WORKFLOW_ID='workflow-id'  # For updates, omit for create")
            print("  python3 update-workflow.py")
            return False
        
        workflow_data = self.load_workflow(self.workflow_file)
        if not workflow_data:
            return False
        
        print(f"📋 Updating workflow from: {self.workflow_file}")
        print(f"   n8n URL: {self.n8n_url}")
        print()
        
        if self.workflow_id:
            return self.update_workflow(workflow_data)
        else:
            print("⚠️  No WORKFLOW_ID set - creating new workflow")
            return self.create_workflow(workflow_data)

def main():
    updater = WorkflowUpdater()
    success = updater.run()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()



