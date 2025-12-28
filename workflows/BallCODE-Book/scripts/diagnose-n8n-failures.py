#!/usr/bin/env python3
"""
n8n Workflow Failure Diagnostic Tool
Helps identify and analyze workflow failures

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import requests
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# n8n Configuration
N8N_URL = "http://192.168.1.226:5678"
N8N_API_KEY = None  # Set if you have API key

def get_n8n_executions(limit: int = 50, status: Optional[str] = None) -> List[Dict]:
    """Get n8n execution history via API."""
    try:
        url = f"{N8N_URL}/api/v1/executions"
        params = {
            "limit": limit,
            "includeData": True
        }
        if status:
            params["status"] = status
        
        headers = {}
        if N8N_API_KEY:
            headers["X-N8N-API-KEY"] = N8N_API_KEY
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        else:
            print(f"⚠️ API request failed: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return []
    except requests.exceptions.ConnectionError:
        print(f"⚠️ Cannot connect to n8n at {N8N_URL}")
        print("   Make sure n8n is running and accessible")
        return []
    except Exception as e:
        print(f"⚠️ Error fetching executions: {e}")
        return []

def analyze_execution(execution: Dict) -> Dict:
    """Analyze a single execution for failure reasons."""
    execution_id = execution.get("id", "unknown")
    status = execution.get("finished", False)
    stopped_at = execution.get("stoppedAt")
    started_at = execution.get("startedAt")
    workflow_id = execution.get("workflowId")
    mode = execution.get("mode", "unknown")
    
    # Get execution data
    execution_data = execution.get("data", {})
    result_data = execution_data.get("resultData", {})
    
    # Check for errors
    errors = []
    if result_data:
        error_data = result_data.get("error", {})
        if error_data:
            errors.append({
                "message": error_data.get("message", "Unknown error"),
                "name": error_data.get("name", "Error"),
                "stack": error_data.get("stack", "")
            })
    
    # Check node execution data
    node_errors = []
    if execution_data.get("resultData", {}).get("runData"):
        run_data = execution_data["resultData"]["runData"]
        for node_name, node_runs in run_data.items():
            for run in node_runs:
                if run.get("error"):
                    node_errors.append({
                        "node": node_name,
                        "error": run["error"].get("message", "Unknown error"),
                        "type": run["error"].get("name", "Error")
                    })
    
    return {
        "id": execution_id,
        "status": "success" if status else "failed",
        "workflow_id": workflow_id,
        "mode": mode,
        "started_at": started_at,
        "stopped_at": stopped_at,
        "errors": errors,
        "node_errors": node_errors,
        "has_errors": len(errors) > 0 or len(node_errors) > 0
    }

def categorize_failures(analyses: List[Dict]) -> Dict:
    """Categorize failures by type."""
    categories = {
        "environment_variables": [],
        "api_credentials": [],
        "network_timeout": [],
        "workflow_logic": [],
        "node_errors": [],
        "unknown": []
    }
    
    for analysis in analyses:
        if analysis["status"] != "failed" and not analysis["has_errors"]:
            continue
        
        # Check error messages for patterns
        all_errors = analysis["errors"] + analysis["node_errors"]
        
        if not all_errors:
            categories["unknown"].append(analysis)
            continue
        
        categorized = False
        for error in all_errors:
            error_msg = error.get("error", error.get("message", "")).lower()
            
            # Environment variable errors
            if any(term in error_msg for term in ["environment variable", "env", "process.env", "not set", "undefined"]):
                categories["environment_variables"].append(analysis)
                categorized = True
                break
            
            # API credential errors
            if any(term in error_msg for term in ["credential", "authentication", "unauthorized", "401", "403", "api key"]):
                categories["api_credentials"].append(analysis)
                categorized = True
                break
            
            # Network/timeout errors
            if any(term in error_msg for term in ["timeout", "connection", "network", "econnrefused", "etimedout"]):
                categories["network_timeout"].append(analysis)
                categorized = True
                break
            
            # Workflow logic errors
            if any(term in error_msg for term in ["cannot read", "undefined", "null", "typeerror", "referenceerror"]):
                categories["workflow_logic"].append(analysis)
                categorized = True
                break
        
        if not categorized:
            categories["node_errors"].append(analysis)
    
    return categories

def generate_diagnostic_report(executions: List[Dict]) -> str:
    """Generate diagnostic report."""
    if not executions:
        return """
# ⚠️ n8n Failure Diagnostic Report

**Status:** Cannot connect to n8n API

**Possible Reasons:**
1. n8n is not running
2. n8n URL is incorrect
3. API key is required but not set
4. Network connectivity issue

**How to Fix:**
1. Check n8n is running: http://192.168.1.226:5678
2. Check n8n API settings
3. Set N8N_API_KEY if required
"""
    
    # Analyze all executions
    analyses = [analyze_execution(exec) for exec in executions]
    
    # Count stats
    total = len(analyses)
    successful = sum(1 for a in analyses if a["status"] == "success" and not a["has_errors"])
    failed = total - successful
    failure_rate = (failed / total * 100) if total > 0 else 0
    
    # Categorize failures
    categories = categorize_failures(analyses)
    
    # Generate report
    report = f"""
# 🔍 n8n Workflow Failure Diagnostic Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**n8n URL:** {N8N_URL}

## 📊 Overall Statistics

- **Total Executions Analyzed:** {total}
- **Successful:** {successful} ({100 - failure_rate:.1f}%)
- **Failed:** {failed} ({failure_rate:.1f}%)
- **Failure Rate:** {failure_rate:.1f}%

"""
    
    if failure_rate == 0:
        report += "✅ **No failures detected!** All executions are successful.\n\n"
    elif failure_rate < 10:
        report += f"✅ **Low failure rate** ({failure_rate:.1f}%) - System is healthy.\n\n"
    elif failure_rate < 25:
        report += f"⚠️ **Moderate failure rate** ({failure_rate:.1f}%) - Some issues to address.\n\n"
    else:
        report += f"🚨 **High failure rate** ({failure_rate:.1f}%) - Critical issues need attention.\n\n"
    
    # Failure categories
    report += "## 🔍 Failure Categories\n\n"
    
    for category, failures in categories.items():
        if failures:
            report += f"### {category.replace('_', ' ').title()} ({len(failures)} failures)\n\n"
            
            # Show unique errors
            unique_errors = {}
            for failure in failures[:5]:  # Show first 5
                for error in failure.get("errors", []) + failure.get("node_errors", []):
                    error_msg = error.get("error", error.get("message", "Unknown"))
                    if error_msg not in unique_errors:
                        unique_errors[error_msg] = {
                            "count": 1,
                            "execution_id": failure["id"]
                        }
                    else:
                        unique_errors[error_msg]["count"] += 1
            
            for error_msg, info in list(unique_errors.items())[:3]:
                report += f"- **{error_msg[:100]}** (occurs {info['count']} times)\n"
            
            if len(failures) > 5:
                report += f"- ... and {len(failures) - 5} more\n"
            
            report += "\n"
    
    # Recommendations
    report += "## 💡 Recommendations\n\n"
    
    if categories["environment_variables"]:
        report += """
### Fix Environment Variables
1. Check n8n Settings → Environment Variables
2. Ensure all required variables are set:
   - `GITHUB_REPO_OWNER`
   - `GITHUB_REPO_NAME`
   - `NETLIFY_SITE_ID`
   - `N8N_INSTANCE_ROLE`
3. Restart n8n after adding variables

"""
    
    if categories["api_credentials"]:
        report += """
### Fix API Credentials
1. Check n8n Credentials section
2. Verify OpenAI API key is set
3. Verify GitHub token is set
4. Verify Netlify token is set
5. Test credentials individually

"""
    
    if categories["network_timeout"]:
        report += """
### Fix Network/Timeout Issues
1. Check network connectivity
2. Increase timeout values in HTTP Request nodes
3. Add retry logic to workflows
4. Check if external APIs are accessible

"""
    
    if categories["workflow_logic"]:
        report += """
### Fix Workflow Logic Errors
1. Review Code nodes for undefined variables
2. Add null checks before accessing properties
3. Add error handling to workflows
4. Test workflows with sample data

"""
    
    # Recent failures
    recent_failures = [a for a in analyses if a["status"] == "failed" or a["has_errors"]][:5]
    if recent_failures:
        report += "## 🚨 Recent Failures\n\n"
        for failure in recent_failures:
            report += f"### Execution {failure['id'][:8]}...\n"
            report += f"- **Status:** {failure['status']}\n"
            report += f"- **Mode:** {failure['mode']}\n"
            report += f"- **Started:** {failure['started_at']}\n"
            
            if failure["errors"]:
                report += f"- **Errors:** {len(failure['errors'])}\n"
                for error in failure["errors"][:2]:
                    report += f"  - {error.get('message', 'Unknown error')[:100]}\n"
            
            if failure["node_errors"]:
                report += f"- **Node Errors:** {len(failure['node_errors'])}\n"
                for error in failure["node_errors"][:2]:
                    report += f"  - {error.get('node', 'Unknown')}: {error.get('error', 'Unknown')[:100]}\n"
            
            report += "\n"
    
    return report

def main():
    """Main diagnostic function."""
    print("=" * 60)
    print("🔍 n8n Workflow Failure Diagnostic Tool")
    print("=" * 60)
    print()
    
    print(f"📡 Connecting to n8n at {N8N_URL}...")
    
    # Get recent executions
    print("📥 Fetching execution history...")
    executions = get_n8n_executions(limit=50)
    
    if not executions:
        print("\n⚠️ No executions found or cannot connect to n8n")
        print("\n💡 Alternative: Check n8n UI directly:")
        print(f"   1. Open: {N8N_URL}")
        print("   2. Go to 'Executions' tab")
        print("   3. Review failed executions manually")
        return
    
    print(f"✅ Found {len(executions)} executions")
    print()
    
    # Analyze
    print("🔍 Analyzing executions...")
    report = generate_diagnostic_report(executions)
    
    # Save report
    report_file = Path(__file__).parent.parent / "N8N-FAILURE-DIAGNOSTIC-REPORT.md"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"✅ Diagnostic report saved: {report_file}")
    print()
    print(report)
    
    # Summary
    analyses = [analyze_execution(exec) for exec in executions]
    total = len(analyses)
    failed = sum(1 for a in analyses if a["status"] == "failed" or a["has_errors"])
    failure_rate = (failed / total * 100) if total > 0 else 0
    
    print()
    print("=" * 60)
    print(f"📊 Summary: {failed}/{total} failed ({failure_rate:.1f}%)")
    print("=" * 60)

if __name__ == "__main__":
    main()


