#!/usr/bin/env python3
"""
Netlify Deployment Verification Script
Automatically checks Netlify deployment status using API

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python3 verify-netlify-deployment.py [--site-id SITE_ID] [--deploy-id DEPLOY_ID] [--timeout TIMEOUT]

Environment Variables:
    NETLIFY_SITE_ID - Netlify site ID
    NETLIFY_AUTH_TOKEN - Netlify API token
    NETLIFY_DEPLOY_ID - Specific deployment ID to check (optional)
"""

import os
import sys
import time
import json
import argparse
import requests
from typing import Dict, Optional, Tuple

# Netlify API base URL
NETLIFY_API_BASE = "https://api.netlify.com/api/v1"

# Deployment states
STATE_BUILDING = "building"
STATE_READY = "ready"
STATE_ERROR = "error"
STATE_NEW = "new"
STATE_ENQUEUED = "enqueued"
STATE_PROCESSING = "processing"
STATE_PREPARING = "preparing"
STATE_PREPARED = "prepared"
STATE_UPLOADING = "uploading"
STATE_UPLOADED = "uploaded"
STATE_PUBLISHED = "published"

# Success states
SUCCESS_STATES = [STATE_READY, STATE_PUBLISHED]

# Failure states
FAILURE_STATES = [STATE_ERROR]

# In-progress states
IN_PROGRESS_STATES = [
    STATE_NEW,
    STATE_ENQUEUED,
    STATE_PROCESSING,
    STATE_PREPARING,
    STATE_PREPARED,
    STATE_UPLOADING,
    STATE_UPLOADED,
    STATE_BUILDING,
]


def get_netlify_headers() -> Dict[str, str]:
    """Get headers for Netlify API requests."""
    token = os.getenv("NETLIFY_AUTH_TOKEN")
    if not token:
        raise ValueError("NETLIFY_AUTH_TOKEN environment variable is not set")
    
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def get_latest_deployment(site_id: str) -> Optional[Dict]:
    """Get the latest deployment for a site."""
    headers = get_netlify_headers()
    url = f"{NETLIFY_API_BASE}/sites/{site_id}/deploys"
    
    try:
        response = requests.get(url, headers=headers, params={"per_page": 1})
        response.raise_for_status()
        deployments = response.json()
        
        if deployments and len(deployments) > 0:
            return deployments[0]
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest deployment: {e}", file=sys.stderr)
        return None


def get_deployment_status(site_id: str, deploy_id: str) -> Optional[Dict]:
    """Get status of a specific deployment."""
    headers = get_netlify_headers()
    url = f"{NETLIFY_API_BASE}/sites/{site_id}/deploys/{deploy_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching deployment status: {e}", file=sys.stderr)
        return None


def check_deployment_status(
    site_id: str,
    deploy_id: Optional[str] = None,
    timeout: int = 600,
    poll_interval: int = 10
) -> Tuple[bool, Dict]:
    """
    Check deployment status, polling until complete or timeout.
    
    Args:
        site_id: Netlify site ID
        deploy_id: Specific deployment ID (if None, checks latest)
        timeout: Maximum time to wait in seconds (default: 10 minutes)
        poll_interval: Time between polls in seconds (default: 10 seconds)
    
    Returns:
        Tuple of (success: bool, deployment_info: dict)
    """
    start_time = time.time()
    
    # If no deploy_id provided, get the latest deployment
    if not deploy_id:
        deployment = get_latest_deployment(site_id)
        if not deployment:
            return False, {
                "error": "No deployments found",
                "site_id": site_id,
            }
        deploy_id = deployment.get("id")
        print(f"Checking latest deployment: {deploy_id}")
    else:
        print(f"Checking deployment: {deploy_id}")
    
    # Poll deployment status
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > timeout:
            return False, {
                "error": "Timeout waiting for deployment",
                "deploy_id": deploy_id,
                "timeout": timeout,
                "elapsed": elapsed,
            }
        
        # Get deployment status
        deployment = get_deployment_status(site_id, deploy_id)
        
        if not deployment:
            return False, {
                "error": "Could not fetch deployment status",
                "deploy_id": deploy_id,
            }
        
        state = deployment.get("state", "unknown")
        deploy_url = deployment.get("deploy_url", "")
        site_url = deployment.get("site_url", "")
        
        print(f"Deployment state: {state} (elapsed: {int(elapsed)}s)")
        
        # Check if deployment succeeded
        if state in SUCCESS_STATES:
            return True, {
                "success": True,
                "deploy_id": deploy_id,
                "state": state,
                "deploy_url": deploy_url,
                "site_url": site_url,
                "elapsed": elapsed,
                "deployment": deployment,
            }
        
        # Check if deployment failed
        if state in FAILURE_STATES:
            error_message = deployment.get("error_message", "Unknown error")
            return False, {
                "success": False,
                "deploy_id": deploy_id,
                "state": state,
                "error": error_message,
                "deploy_url": deploy_url,
                "site_url": site_url,
                "elapsed": elapsed,
                "deployment": deployment,
            }
        
        # If still in progress, wait and poll again
        if state in IN_PROGRESS_STATES:
            time.sleep(poll_interval)
            continue
        
        # Unknown state
        return False, {
            "error": f"Unknown deployment state: {state}",
            "deploy_id": deploy_id,
            "state": state,
            "deployment": deployment,
        }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Verify Netlify deployment status"
    )
    parser.add_argument(
        "--site-id",
        default=os.getenv("NETLIFY_SITE_ID"),
        help="Netlify site ID (or set NETLIFY_SITE_ID env var)",
    )
    parser.add_argument(
        "--deploy-id",
        default=os.getenv("NETLIFY_DEPLOY_ID"),
        help="Specific deployment ID to check (optional)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Timeout in seconds (default: 600 = 10 minutes)",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=10,
        help="Poll interval in seconds (default: 10)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON format",
    )
    
    args = parser.parse_args()
    
    # Validate site ID
    if not args.site_id:
        print("Error: NETLIFY_SITE_ID is required", file=sys.stderr)
        print("Set it as environment variable or use --site-id", file=sys.stderr)
        sys.exit(1)
    
    # Check deployment status
    success, result = check_deployment_status(
        site_id=args.site_id,
        deploy_id=args.deploy_id,
        timeout=args.timeout,
        poll_interval=args.poll_interval,
    )
    
    # Output results
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if success:
            print(f"\n✅ Deployment successful!")
            print(f"   Deploy ID: {result.get('deploy_id')}")
            print(f"   State: {result.get('state')}")
            print(f"   Site URL: {result.get('site_url')}")
            print(f"   Deploy URL: {result.get('deploy_url')}")
            print(f"   Elapsed: {result.get('elapsed', 0):.1f}s")
        else:
            print(f"\n❌ Deployment failed or error occurred")
            print(f"   Error: {result.get('error', 'Unknown error')}")
            if 'deploy_id' in result:
                print(f"   Deploy ID: {result.get('deploy_id')}")
            if 'state' in result:
                print(f"   State: {result.get('state')}")
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()



