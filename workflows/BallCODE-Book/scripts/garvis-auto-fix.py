#!/usr/bin/env python3
"""
Garvis Self-Healing System - Auto-Fix Script
Automatically fixes common n8n workflow errors

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import requests
import re
from typing import Dict, List, Any, Optional

# Configuration
N8N_API_BASE = "http://192.168.1.226:5678/api/v1"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def get_n8n_api_key() -> Optional[str]:
    """Get n8n API key from environment or config"""
    # TODO: Add API key retrieval from environment or config file
    return None


def get_workflow(workflow_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Get workflow JSON from n8n API"""
    url = f"{N8N_API_BASE}/workflows/{workflow_id}"
    
    if api_key:
        HEADERS["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workflow {workflow_id}: {e}", file=sys.stderr)
        return {}


def update_workflow(workflow_id: str, workflow_data: Dict[str, Any], api_key: Optional[str] = None) -> bool:
    """Update workflow in n8n"""
    url = f"{N8N_API_BASE}/workflows/{workflow_id}"
    
    if api_key:
        HEADERS["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.put(url, headers=HEADERS, json=workflow_data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating workflow {workflow_id}: {e}", file=sys.stderr)
        return False


def get_credential(credential_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Get credential from n8n API"""
    url = f"{N8N_API_BASE}/credentials/{credential_id}"
    
    if api_key:
        HEADERS["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching credential {credential_id}: {e}", file=sys.stderr)
        return {}


def update_credential_header_name(credential_id: str, correct_value: str = "Authorization", api_key: Optional[str] = None) -> bool:
    """Update credential header name to valid HTTP token"""
    credential = get_credential(credential_id, api_key)
    
    if not credential:
        return False
    
    # Update header name in credential data
    if "data" in credential:
        if "headerName" in credential["data"]:
            credential["data"]["headerName"] = correct_value
        elif "name" in credential["data"]:
            credential["data"]["name"] = correct_value
    
    # Update via API
    url = f"{N8N_API_BASE}/credentials/{credential_id}"
    
    if api_key:
        HEADERS["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.put(url, headers=HEADERS, json=credential)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating credential {credential_id}: {e}", file=sys.stderr)
        return False


def find_node_by_name(workflow: Dict[str, Any], node_name: str) -> Optional[Dict[str, Any]]:
    """Find node in workflow by name"""
    nodes = workflow.get("nodes", [])
    for node in nodes:
        if node.get("name") == node_name:
            return node
    return None


def fix_openai_request_body(node: Dict[str, Any]) -> bool:
    """Fix OpenAI API request body to include required parameters"""
    params = node.get("parameters", {})
    json_body = params.get("jsonBody", "")
    
    # Check if model and messages are present
    has_model = "model" in json_body.lower() or '"model"' in json_body
    has_messages = "messages" in json_body.lower() or '"messages"' in json_body
    
    if has_model and has_messages:
        return False  # Already correct
    
    # Try to fix by adding missing parameters
    # This is a simplified fix - in production, would parse and validate JSON properly
    if not has_model:
        # Add model parameter
        if json_body.startswith("{{") and json_body.endswith("}}"):
            # It's an expression - would need more sophisticated parsing
            pass
        else:
            # Try to add model to JSON
            try:
                body_obj = json.loads(json_body)
                body_obj["model"] = "gpt-4o"  # Default to gpt-4o for vision
                params["jsonBody"] = json.dumps(body_obj, indent=2)
                node["parameters"] = params
                return True
            except json.JSONDecodeError:
                pass
    
    return False


def fix_credential_header_name_in_workflow(workflow: Dict[str, Any], node_name: str, correct_value: str = "Authorization") -> bool:
    """Fix credential header name issue by updating workflow node configuration"""
    node = find_node_by_name(workflow, node_name)
    
    if not node:
        return False
    
    # Check if node uses credentials
    credentials = node.get("credentials", {})
    
    # For HTTP Request nodes with httpHeaderAuth
    if "httpHeaderAuth" in credentials:
        cred_info = credentials["httpHeaderAuth"]
        cred_id = cred_info.get("id")
        
        if cred_id:
            # Update the credential itself
            return update_credential_header_name(cred_id, correct_value)
    
    return False


def apply_fix(diagnosis: Dict[str, Any], workflow_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Apply fix based on diagnosis"""
    fix = diagnosis.get("fix", {})
    action = fix.get("action")
    node_name = diagnosis.get("nodeName")
    
    result = {
        "success": False,
        "action": action,
        "nodeName": node_name,
        "message": "",
        "error": None
    }
    
    try:
        if action == "updateCredentialHeaderName":
            # Get workflow to find credential ID
            workflow = get_workflow(workflow_id, api_key)
            
            if workflow:
                success = fix_credential_header_name_in_workflow(
                    workflow,
                    node_name,
                    fix.get("correctValue", "Authorization")
                )
                
                if success:
                    result["success"] = True
                    result["message"] = f"Updated credential header name to '{fix.get('correctValue', 'Authorization')}'"
                else:
                    result["message"] = "Could not update credential (credential ID not found or API error)"
            else:
                result["message"] = "Could not fetch workflow"
        
        elif action == "validateOpenAIRequestBody":
            # Get workflow and fix node
            workflow = get_workflow(workflow_id, api_key)
            
            if workflow:
                node = find_node_by_name(workflow, node_name)
                
                if node:
                    success = fix_openai_request_body(node)
                    
                    if success:
                        # Update workflow
                        if update_workflow(workflow_id, workflow, api_key):
                            result["success"] = True
                            result["message"] = "Fixed OpenAI request body (added missing parameters)"
                        else:
                            result["message"] = "Fixed node but could not update workflow"
                    else:
                        result["message"] = "Request body already correct or could not parse"
                else:
                    result["message"] = f"Node '{node_name}' not found in workflow"
            else:
                result["message"] = "Could not fetch workflow"
        
        elif action == "verifyCredential":
            result["message"] = "Credential verification requires manual review"
            result["success"] = False
        
        elif action == "manualReview":
            result["message"] = "Requires manual review - cannot auto-fix"
            result["success"] = False
        
        else:
            result["message"] = f"Unknown fix action: {action}"
            result["success"] = False
    
    except Exception as e:
        result["error"] = str(e)
        result["message"] = f"Error applying fix: {e}"
    
    return result


def main():
    """Main function - process diagnoses and apply fixes"""
    if len(sys.argv) < 3:
        print("Usage: garvis-auto-fix.py <diagnoses_json> <n8n_url> [api_key]", file=sys.stderr)
        sys.exit(1)
    
    diagnoses_json = sys.argv[1]
    n8n_url = sys.argv[2]
    api_key = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Update global N8N_API_BASE
    global N8N_API_BASE
    N8N_API_BASE = f"{n8n_url.rstrip('/')}/api/v1"
    
    try:
        diagnoses = json.loads(diagnoses_json)
    except json.JSONDecodeError as e:
        print(f"Error parsing diagnoses JSON: {e}", file=sys.stderr)
        sys.exit(1)
    
    fixes = []
    
    for diagnosis in diagnoses:
        if not diagnosis.get("fixable", False):
            continue
        
        if diagnosis.get("confidence", 0) < 0.7:
            continue
        
        workflow_id = diagnosis.get("workflowId")
        if not workflow_id:
            continue
        
        fix_result = apply_fix(diagnosis, workflow_id, api_key)
        fixes.append(fix_result)
    
    # Output results as JSON
    output = {
        "fixes": fixes,
        "totalFixes": len(fixes),
        "successfulFixes": len([f for f in fixes if f.get("success")]),
        "timestamp": __import__("datetime").datetime.now().isoformat()
    }
    
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

