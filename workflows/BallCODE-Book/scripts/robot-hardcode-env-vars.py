#!/usr/bin/env python3
"""
Robot: Hardcode Environment Variables in Workflow (Option B)
Fallback solution when SSH access is not available.
"""

import json
import sys
from pathlib import Path

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{BLUE}{text:^60}{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def get_netlify_site_id():
    """Get Netlify Site ID from user (optional)."""
    print_info("Netlify Site ID is needed for deployment status checks")
    print_info("If you don't have a Netlify site yet, you can:")
    print_info("  1. Skip for now (enter 'skip' or press Enter)")
    print_info("  2. Create a site first: https://app.netlify.com → Add new site")
    print_info("  3. Get Site ID from: Site settings → General → Site ID")
    print()
    site_id = input(f"{YELLOW}Enter Netlify Site ID (or 'skip' to continue without it): {NC}").strip()
    
    if not site_id or site_id.lower() == 'skip':
        print_warning("Continuing without Netlify Site ID")
        print_info("You can add it later by re-running this script")
        return "PLACEHOLDER_SITE_ID"  # Placeholder that will be skipped in workflow
    return site_id

def hardcode_env_vars_in_workflow(workflow_file, netlify_site_id):
    """Hardcode environment variables in workflow Code node."""
    print_info(f"Reading workflow file: {workflow_file}")
    
    try:
        with open(workflow_file, 'r') as f:
            workflow = json.load(f)
    except Exception as e:
        print_error(f"Cannot read workflow file: {e}")
        return False
    
    # Find the "Env Preflight" node
    env_node = None
    for node in workflow.get('nodes', []):
        if node.get('name') == 'Env Preflight + Dev Guardrails (AIMCODE L1)':
            env_node = node
            break
    
    if not env_node:
        print_error("Cannot find 'Env Preflight + Dev Guardrails (AIMCODE L1)' node")
        return False
    
    # Get current code
    current_code = env_node['parameters']['jsCode']
    
    # Hardcoded values
    hardcoded_values = {
        'GITHUB_REPO_OWNER': 'rashadwest',
        'GITHUB_REPO_NAME': 'BTEBallCODE',
        'GITHUB_WORKFLOW_FILE': 'unity-webgl-build.yml',
        'NETLIFY_SITE_ID': netlify_site_id
    }
    
    # Check if Site ID is placeholder
    is_placeholder = netlify_site_id == "PLACEHOLDER_SITE_ID"
    
    # Replace env var checks with hardcoded values
    new_code = f"""// L1 (Foundation): env/credential preflight + DEV guardrails
// Guardrail goal: prevent the Mac instance from accidentally running scheduled builds.
//
// Set on Mac:
// - N8N_INSTANCE_ROLE=dev
//
// Set on Pi/prod:
// - N8N_INSTANCE_ROLE=prod
//
// Override (if you really want scheduled builds on dev):
// - ALLOW_SCHEDULED_BUILDS=1

// HARDCODED VALUES (set via robot script - Option B)
const GITHUB_REPO_OWNER = 'rashadwest';
const GITHUB_REPO_NAME = 'BTEBallCODE';
const GITHUB_WORKFLOW_FILE = 'unity-webgl-build.yml';
const NETLIFY_SITE_ID = '{netlify_site_id}';
const NETLIFY_SITE_ID_IS_PLACEHOLDER = {str(is_placeholder).lower()};

// Use hardcoded values instead of env vars
const requiredEnv = [
  'GITHUB_REPO_OWNER',
  'GITHUB_REPO_NAME',
  'GITHUB_WORKFLOW_FILE'
  // NETLIFY_SITE_ID is optional - only required if checking Netlify status
];

// Check if hardcoded values are set (they always are, but keeping structure)
const missing = [];
if (!GITHUB_REPO_OWNER) missing.push('GITHUB_REPO_OWNER');
if (!GITHUB_REPO_NAME) missing.push('GITHUB_REPO_NAME');
if (!GITHUB_WORKFLOW_FILE) missing.push('GITHUB_WORKFLOW_FILE');
// Skip NETLIFY_SITE_ID check if placeholder
if (!NETLIFY_SITE_ID_IS_PLACEHOLDER && !NETLIFY_SITE_ID) {{
  missing.push('NETLIFY_SITE_ID');
}}

if (missing.length) {{
  return {{
    json: {{
      ...$json,
      proceed: false,
      status: 'fail',
      error: `Missing required env var(s): ${{missing.join(', ')}}`,
    }}
  }};
}}

const role = ($env.N8N_INSTANCE_ROLE || 'dev').toString().trim().toLowerCase();
const allowScheduled = ($env.ALLOW_SCHEDULED_BUILDS || '').toString().trim() === '1';

// Block scheduled trigger on dev by default.
if ($json.triggerType === 'scheduled' && role !== 'prod' && !allowScheduled) {{
  return {{
    json: {{
      ...$json,
      proceed: false,
      status: 'skipped',
      skipReason: `Scheduled builds are blocked on ${{role}}. Set N8N_INSTANCE_ROLE=prod (recommended only on Pi) or set ALLOW_SCHEDULED_BUILDS=1 to override.`,
      instanceRole: role,
      allowScheduled
    }}
  }};
}}

return {{
  json: {{
    ...$json,
    proceed: true,
    instanceRole: role,
    allowScheduled,
    // Include hardcoded values in output for downstream nodes
    githubRepoOwner: GITHUB_REPO_OWNER,
    githubRepoName: GITHUB_REPO_NAME,
    githubWorkflowFile: GITHUB_WORKFLOW_FILE,
    netlifySiteId: NETLIFY_SITE_ID,
    netlifySiteIdIsPlaceholder: NETLIFY_SITE_ID_IS_PLACEHOLDER
  }}
}};"""
    
    # Update the node
    env_node['parameters']['jsCode'] = new_code
    
    # Also update nodes that use $env variables
    for node in workflow.get('nodes', []):
        node_name = node.get('name', '')
        
        # Update GitHub dispatch node
        if 'Dispatch GitHub Build' in node_name:
            url = node.get('parameters', {}).get('url', '')
            if '$env.GITHUB_REPO_OWNER' in url:
                node['parameters']['url'] = url.replace(
                    '{{ $env.GITHUB_REPO_OWNER }}', 'rashadwest'
                ).replace(
                    '{{ $env.GITHUB_REPO_NAME }}', 'BTEBallCODE'
                ).replace(
                    '{{ $env.GITHUB_WORKFLOW_FILE }}', 'unity-webgl-build.yml'
                )
        
        # Update GitHub check node
        if 'Check Latest GitHub Run' in node_name:
            url = node.get('parameters', {}).get('url', '')
            if '$env.GITHUB_REPO_OWNER' in url:
                node['parameters']['url'] = url.replace(
                    '{{ $env.GITHUB_REPO_OWNER }}', 'rashadwest'
                ).replace(
                    '{{ $env.GITHUB_REPO_NAME }}', 'BTEBallCODE'
                ).replace(
                    '{{ $env.GITHUB_WORKFLOW_FILE }}', 'unity-webgl-build.yml'
                )
        
        # Update Netlify check node (skip if placeholder)
        if 'Check Latest Netlify Deploy' in node_name:
            if is_placeholder:
                # Make Netlify check optional - return placeholder response
                js_code = node.get('parameters', {}).get('jsCode', '')
                if not js_code:
                    # Add code to skip if placeholder
                    node['parameters']['jsCode'] = f"""// Skip Netlify check if Site ID is placeholder
if ($json.netlifySiteId === 'PLACEHOLDER_SITE_ID' || !$json.netlifySiteId) {{
  return {{
    json: {{
      ...$json,
      netlify: {{
        ok: false,
        state: 'skipped',
        skipReason: 'Netlify Site ID not configured - create site first',
        deployUrl: ''
      }}
    }}
  }};
}}
// Continue with normal Netlify check
return $json;"""
            else:
                url = node.get('parameters', {}).get('url', '')
                if '$env.NETLIFY_SITE_ID' in url or '{{ $env.NETLIFY_SITE_ID }}' in url:
                    node['parameters']['url'] = url.replace(
                        '{{ $env.NETLIFY_SITE_ID }}', netlify_site_id
                    ).replace(
                        '$env.NETLIFY_SITE_ID', netlify_site_id
                    )
    
    # Save backup first
    backup_file = workflow_file.replace('.json', '.json.backup')
    print_info(f"Creating backup: {backup_file}")
    with open(backup_file, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    # Save modified workflow
    print_info(f"Saving modified workflow: {workflow_file}")
    with open(workflow_file, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    return True

def main():
    """Main function."""
    print_header("Robot: Hardcode Environment Variables (Option B)")
    
    # Get Netlify Site ID
    netlify_site_id = get_netlify_site_id()
    if not netlify_site_id:
        return False
    
    # Find workflow file
    script_dir = Path(__file__).parent.parent
    workflow_file = script_dir / 'n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json'
    
    if not workflow_file.exists():
        print_error(f"Workflow file not found: {workflow_file}")
        return False
    
    print_success(f"Found workflow file: {workflow_file}")
    
    # Hardcode values
    print_info("Hardcoding environment variables in workflow...")
    if hardcode_env_vars_in_workflow(str(workflow_file), netlify_site_id):
        print_success("✅ Environment variables hardcoded successfully!")
        print("\nNext steps:")
        print("  1. Re-import workflow in n8n UI:")
        print(f"     File: {workflow_file.name}")
        print("  2. Run: python scripts/verify-garvis-unity-integration.py")
        print("  3. Run: python scripts/garvis-command.py --one-thing 'Test' --tasks 'Build Unity game'")
        return True
    else:
        print_error("Failed to hardcode environment variables")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

