#!/usr/bin/env python3
"""
Verify Garvis → Unity → Netlify Integration
Checks that all components are properly connected and working.
"""

import os
import sys
import json
import requests
from typing import Dict, List, Tuple

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'  # No Color

def print_header(text: str):
    """Print a formatted header."""
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{BLUE}{text:^60}{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def print_success(text: str):
    """Print success message."""
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text: str):
    """Print error message."""
    print(f"{RED}❌ {text}{NC}")

def print_warning(text: str):
    """Print warning message."""
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text: str):
    """Print info message."""
    print(f"{BLUE}ℹ️  {text}{NC}")

def check_n8n_running(n8n_url: str) -> bool:
    """Check if n8n is running."""
    try:
        response = requests.get(f"{n8n_url}/healthz", timeout=5)
        return response.status_code == 200
    except:
        return False

def check_webhook(n8n_url: str, webhook_path: str, test_payload: Dict) -> Tuple[bool, str]:
    """Check if a webhook is accessible."""
    try:
        response = requests.post(
            f"{n8n_url}{webhook_path}",
            json=test_payload,
            timeout=10
        )
        if response.status_code in [200, 201]:
            return True, "Webhook accessible"
        elif response.status_code == 404:
            return False, "Webhook not found (workflow may not be imported/activated)"
        else:
            return False, f"Webhook returned status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Cannot connect to n8n (is it running?)"
    except Exception as e:
        return False, f"Error: {str(e)}"

def check_env_vars() -> Tuple[List[str], List[str]]:
    """Check required environment variables."""
    required_vars = {
        'GITHUB_REPO_OWNER': 'rashadwest',
        'GITHUB_REPO_NAME': 'BTEBallCODE',
        'GITHUB_WORKFLOW_FILE': 'unity-webgl-build.yml',
        'NETLIFY_SITE_ID': None,  # Must be set by user
        'NETLIFY_SITE_NAME': 'ballcode-game',
        'GITHUB_PAT': None,  # Must be set by user
        'NETLIFY_AUTH_TOKEN': None,  # Must be set by user
    }
    
    missing = []
    optional_missing = []
    
    for var, default in required_vars.items():
        value = os.getenv(var, '')
        if not value:
            if default is None:
                missing.append(var)
            else:
                optional_missing.append(var)
    
    return missing, optional_missing

def check_github_workflow_exists() -> bool:
    """Check if GitHub Actions workflow file exists."""
    workflow_path = ".github/workflows/unity-webgl-build.yml"
    return os.path.exists(workflow_path)

def main():
    """Main verification function."""
    print_header("Garvis → Unity → Netlify Integration Verification")
    
    # Get n8n URL from environment or use default (Pi instance)
    n8n_url = os.getenv('N8N_URL', 'http://192.168.1.226:5678')
    print_info(f"Using n8n URL: {n8n_url}")
    
    results = {
        'n8n_running': False,
        'garvis_webhook': False,
        'unity_webhook': False,
        'env_vars': False,
        'github_workflow': False,
    }
    
    # Check 1: n8n is running
    print("\n1. Checking if n8n is running...")
    if check_n8n_running(n8n_url):
        print_success("n8n is running")
        results['n8n_running'] = True
    else:
        print_error("n8n is not running or not accessible")
        print_info(f"   Start n8n: n8n start (or check URL: {n8n_url})")
        return
    
    # Check 2: Garvis Orchestrator webhook
    print("\n2. Checking Garvis Orchestrator webhook...")
    garvis_payload = {
        "one_thing": "Integration test",
        "tasks": ["Test Unity build"],
        "job_id": "verify-test"
    }
    accessible, message = check_webhook(n8n_url, "/webhook/garvis", garvis_payload)
    if accessible:
        print_success(f"Garvis Orchestrator webhook: {message}")
        results['garvis_webhook'] = True
    else:
        print_error(f"Garvis Orchestrator webhook: {message}")
        print_info("   Import workflow: n8n-garvis-orchestrator-workflow.json")
        print_info("   Activate workflow in n8n UI")
    
    # Check 3: Unity Build Orchestrator webhook
    print("\n3. Checking Unity Build Orchestrator webhook...")
    unity_payload = {
        "request": "Integration test",
        "branch": "main",
        "jobId": "verify-test"
    }
    accessible, message = check_webhook(n8n_url, "/webhook/unity-build", unity_payload)
    if accessible:
        print_success(f"Unity Build Orchestrator webhook: {message}")
        results['unity_webhook'] = True
    else:
        print_error(f"Unity Build Orchestrator webhook: {message}")
        print_info("   Import workflow: n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json")
        print_info("   Activate workflow in n8n UI")
    
    # Check 4: Environment variables
    print("\n4. Checking environment variables...")
    missing, optional_missing = check_env_vars()
    if not missing:
        print_success("All required environment variables are set")
        results['env_vars'] = True
        if optional_missing:
            print_warning(f"Optional vars not set: {', '.join(optional_missing)}")
    else:
        print_error(f"Missing required environment variables: {', '.join(missing)}")
        print_info("   Set in n8n: Settings → Environment Variables")
        print_info("   Or set in shell: export VAR_NAME=value")
    
    # Check 5: GitHub Actions workflow
    print("\n5. Checking GitHub Actions workflow file...")
    if check_github_workflow_exists():
        print_success("GitHub Actions workflow file exists")
        results['github_workflow'] = True
    else:
        print_warning("GitHub Actions workflow file not found locally")
        print_info("   This is OK if workflow exists in GitHub repo")
        print_info("   Check: https://github.com/rashadwest/BTEBallCODE/tree/main/.github/workflows")
    
    # Summary
    print_header("Verification Summary")
    
    total_checks = len(results)
    passed_checks = sum(1 for v in results.values() if v)
    
    print(f"\n{BLUE}Results: {passed_checks}/{total_checks} checks passed{NC}\n")
    
    for check, passed in results.items():
        status = f"{GREEN}✅ PASS{NC}" if passed else f"{RED}❌ FAIL{NC}"
        print(f"  {status}  {check.replace('_', ' ').title()}")
    
    if passed_checks == total_checks:
        print(f"\n{GREEN}🎉 All checks passed! Integration is ready!{NC}")
        print(f"\n{BLUE}Next steps:{NC}")
        print("  1. Test integration: python scripts/garvis-command.py --one-thing 'Test' --tasks 'Build Unity game'")
        print("  2. Monitor build: Check GitHub Actions and Netlify")
        print("  3. Move to UI/UX improvements!")
    else:
        print(f"\n{YELLOW}⚠️  Some checks failed. Please fix the issues above.{NC}")
        print(f"\n{BLUE}Quick fixes:{NC}")
        if not results['garvis_webhook']:
            print("  • Import Garvis Orchestrator workflow in n8n UI")
        if not results['unity_webhook']:
            print("  • Import Unity Build Orchestrator workflow in n8n UI")
        if not results['env_vars']:
            print("  • Set missing environment variables in n8n Settings")
    
    print()

if __name__ == "__main__":
    main()

