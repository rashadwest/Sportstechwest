#!/usr/bin/env python3
"""
Independent Build Monitor
Monitors GitHub Actions and Netlify builds outside of n8n

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Configuration - Set these environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
GITHUB_OWNER = os.getenv('GITHUB_REPO_OWNER', '')
GITHUB_REPO = os.getenv('GITHUB_REPO_NAME', '')
GITHUB_WORKFLOW = os.getenv('GITHUB_WORKFLOW_FILE', '')

# Support both names used across this repo/docs.
# Prefer NETLIFY_AUTH_TOKEN (consistent with other scripts + GitHub Actions),
# but fall back to NETLIFY_TOKEN for backwards compatibility.
NETLIFY_TOKEN = os.getenv('NETLIFY_AUTH_TOKEN', '') or os.getenv('NETLIFY_TOKEN', '')
NETLIFY_SITE_ID = os.getenv('NETLIFY_SITE_ID', '')

# Expected schedule (in hours)
EXPECTED_INTERVAL_HOURS = int(os.getenv('BUILD_INTERVAL_HOURS', '1'))

def check_github_actions() -> Dict:
    """Check GitHub Actions for recent workflow runs."""
    if not all([GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO, GITHUB_WORKFLOW]):
        return {
            'status': 'error',
            'message': 'GitHub credentials not configured',
            'recent_runs': []
        }
    
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/workflows/{GITHUB_WORKFLOW}/runs"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'per_page': 10,
        'status': 'all'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        runs = []
        for run in data.get('workflow_runs', []):
            runs.append({
                'id': run['id'],
                'status': run['status'],
                'conclusion': run.get('conclusion', 'unknown'),
                'created_at': run['created_at'],
                'updated_at': run['updated_at'],
                'html_url': run['html_url']
            })
        
        return {
            'status': 'success',
            'recent_runs': runs,
            'total_runs': len(runs)
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'recent_runs': []
        }

def get_github_status_json() -> Dict:
    """Get GitHub Actions status in JSON format for n8n integration."""
    result = check_github_actions()
    
    # Add latest_run for convenience
    latest_run = None
    if result['status'] == 'success' and result['recent_runs']:
        latest_run = result['recent_runs'][0]
    
    return {
        'status': result['status'],
        'workflow_runs': result['recent_runs'],
        'latest_run': latest_run,
        'total_runs': result.get('total_runs', 0),
        'message': result.get('message', '')
    }

def check_netlify_deploys() -> Dict:
    """Check Netlify for recent deployments."""
    if not all([NETLIFY_TOKEN, NETLIFY_SITE_ID]):
        return {
            'status': 'error',
            'message': 'Netlify credentials not configured',
            'recent_deploys': []
        }
    
    url = f"https://api.netlify.com/api/v1/sites/{NETLIFY_SITE_ID}/deploys"
    headers = {
        'Authorization': f'Bearer {NETLIFY_TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {
        'per_page': 10
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        deploys = []
        for deploy in data[:10]:  # Get first 10
            deploys.append({
                'id': deploy['id'],
                'state': deploy['state'],
                'created_at': deploy['created_at'],
                'updated_at': deploy.get('updated_at', deploy['created_at']),
                'deploy_url': deploy.get('deploy_url', ''),
                'build_id': deploy.get('build_id', '')
            })
        
        return {
            'status': 'success',
            'recent_deploys': deploys,
            'total_deploys': len(deploys)
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'recent_deploys': []
        }

def get_netlify_status_json() -> Dict:
    """Get Netlify deployment status in JSON format for n8n integration."""
    result = check_netlify_deploys()
    
    # Add latest_deploy for convenience
    latest_deploy = None
    if result['status'] == 'success' and result['recent_deploys']:
        latest_deploy = result['recent_deploys'][0]
    
    return {
        'status': result['status'],
        'deploys': result['recent_deploys'],
        'latest_deploy': latest_deploy,
        'total_deploys': result.get('total_deploys', 0),
        'message': result.get('message', '')
    }

def analyze_missed_builds(github_data: Dict, netlify_data: Dict) -> Dict:
    """Analyze if builds were missed based on expected schedule."""
    now = datetime.now()
    expected_times = []
    
    # Generate expected execution times for last 24 hours
    for i in range(24, 0, -EXPECTED_INTERVAL_HOURS):
        expected_time = now - timedelta(hours=i)
        expected_time = expected_time.replace(minute=0, second=0, microsecond=0)
        expected_times.append(expected_time)
    
    missed_builds = []
    
    # Check GitHub Actions
    if github_data['status'] == 'success':
        github_runs = github_data['recent_runs']
        github_times = []
        for run in github_runs:
            try:
                run_time = datetime.fromisoformat(run['created_at'].replace('Z', '+00:00'))
                github_times.append(run_time.replace(tzinfo=None))
            except:
                pass
        
        # Check for missed builds
        for expected in expected_times:
            # Check if there's a build within 30 minutes of expected time
            found = False
            for github_time in github_times:
                if abs((github_time - expected).total_seconds()) < 1800:  # 30 minutes
                    found = True
                    break
            
            if not found:
                missed_builds.append({
                    'type': 'github_actions',
                    'expected_time': expected.isoformat(),
                    'status': 'missed'
                })
    
    # Check Netlify
    if netlify_data['status'] == 'success':
        netlify_deploys = netlify_data['recent_deploys']
        netlify_times = []
        for deploy in netlify_deploys:
            try:
                deploy_time = datetime.fromisoformat(deploy['created_at'].replace('Z', '+00:00'))
                netlify_times.append(deploy_time.replace(tzinfo=None))
            except:
                pass
        
        # Check for missed deployments
        for expected in expected_times:
            found = False
            for netlify_time in netlify_times:
                if abs((netlify_time - expected).total_seconds()) < 1800:  # 30 minutes
                    found = True
                    break
            
            if not found:
                missed_builds.append({
                    'type': 'netlify',
                    'expected_time': expected.isoformat(),
                    'status': 'missed'
                })
    
    return {
        'missed_count': len(missed_builds),
        'missed_builds': missed_builds,
        'expected_count': len(expected_times)
    }

def generate_report(github_data: Dict, netlify_data: Dict, missed_analysis: Dict) -> str:
    """Generate a human-readable report."""
    report = []
    report.append("=" * 70)
    report.append("BUILD MONITORING REPORT")
    report.append("=" * 70)
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # GitHub Actions Status
    report.append("📊 GITHUB ACTIONS:")
    report.append("-" * 70)
    if github_data['status'] == 'success':
        report.append(f"✅ Status: Connected")
        report.append(f"   Recent runs: {github_data['total_runs']}")
        if github_data['recent_runs']:
            latest = github_data['recent_runs'][0]
            report.append(f"   Latest run: {latest['created_at']}")
            report.append(f"   Status: {latest['status']} | Conclusion: {latest.get('conclusion', 'N/A')}")
            report.append(f"   URL: {latest.get('html_url', 'N/A')}")
    else:
        report.append(f"❌ Status: Error - {github_data.get('message', 'Unknown error')}")
    report.append("")
    
    # Netlify Status
    report.append("📊 NETLIFY DEPLOYMENTS:")
    report.append("-" * 70)
    if netlify_data['status'] == 'success':
        report.append(f"✅ Status: Connected")
        report.append(f"   Recent deploys: {netlify_data['total_deploys']}")
        if netlify_data['recent_deploys']:
            latest = netlify_data['recent_deploys'][0]
            report.append(f"   Latest deploy: {latest['created_at']}")
            report.append(f"   State: {latest['state']}")
            report.append(f"   Deploy URL: {latest.get('deploy_url', 'N/A')}")
    else:
        report.append(f"❌ Status: Error - {netlify_data.get('message', 'Unknown error')}")
    report.append("")
    
    # Missed Builds Analysis
    report.append("🔍 MISSED BUILDS ANALYSIS:")
    report.append("-" * 70)
    report.append(f"Expected builds (last 24h): {missed_analysis['expected_count']}")
    report.append(f"Missed builds: {missed_analysis['missed_count']}")
    
    if missed_analysis['missed_builds']:
        report.append("")
        report.append("⚠️  MISSED BUILD TIMES:")
        for missed in missed_analysis['missed_builds'][:10]:  # Show first 10
            report.append(f"   - {missed['expected_time']} ({missed['type']})")
    else:
        report.append("")
        report.append("✅ No missed builds detected!")
    
    report.append("")
    report.append("=" * 70)
    
    return "\n".join(report)

def main():
    """Main monitoring function."""
    parser = argparse.ArgumentParser(description='Monitor GitHub Actions and Netlify builds')
    parser.add_argument('--json', action='store_true', help='Output JSON format instead of text report')
    args = parser.parse_args()
    
    # Check GitHub Actions
    github_data = check_github_actions()
    
    # Check Netlify
    netlify_data = check_netlify_deploys()
    
    # If JSON output requested, output and exit
    if args.json:
        output = {
            'github': get_github_status_json(),
            'netlify': get_netlify_status_json()
        }
        print(json.dumps(output, indent=2))
        # Exit with error code if either check failed
        if github_data['status'] == 'error' or netlify_data['status'] == 'error':
            sys.exit(1)
        sys.exit(0)
    
    # Default behavior: text report
    print("🔍 Starting build monitoring...")
    print()
    
    print("Checking GitHub Actions...")
    print("Checking Netlify...")
    
    # Analyze missed builds
    print("Analyzing missed builds...")
    missed_analysis = analyze_missed_builds(github_data, netlify_data)
    
    # Generate report
    report = generate_report(github_data, netlify_data, missed_analysis)
    print(report)
    
    # Save report to file
    report_file = 'build-monitor-report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"\n📄 Report saved to: {report_file}")
    
    # Exit with error code if builds were missed
    if missed_analysis['missed_count'] > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()

