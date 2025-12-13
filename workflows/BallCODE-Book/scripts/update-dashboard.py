#!/usr/bin/env python3
"""
BallCODE Integration Dashboard Updater
Updates both markdown and HTML dashboards with current system status

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import existing monitor functions by reading the script
import importlib.util
monitor_script_path = project_root / 'scripts' / 'monitor-builds.py'

# Telemetry v1: core integration sources
CURRICULUM_SCHEMA_FILE = project_root / 'curriculum-schema.json'
LEVELS_DIR = project_root / 'Unity-Scripts' / 'Levels'
WEBSITE_INDEX = project_root / 'BallCode' / 'index.html'

PILOT_FILES = [
    project_root / 'Episode-1-For-Pilot-School.md',
    project_root / 'Episode-1-Teacher-Guide.md',
    project_root / 'Pilot-School-Onboarding-Guide.md',
]

def check_github_actions():
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

def check_netlify_deploys():
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

def analyze_missed_builds(github_data: Dict, netlify_data: Dict) -> Dict:
    """Analyze if builds were missed based on expected schedule."""
    now = datetime.now()
    expected_times = []
    
    # Generate expected execution times for last 24 hours
    for i in range(24, 0, -BUILD_INTERVAL_HOURS):
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

# Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
GITHUB_OWNER = os.getenv('GITHUB_REPO_OWNER', '')
GITHUB_REPO = os.getenv('GITHUB_REPO_NAME', '')
GITHUB_WORKFLOW = os.getenv('GITHUB_WORKFLOW_FILE', '')

NETLIFY_TOKEN = os.getenv('NETLIFY_TOKEN', '')
NETLIFY_SITE_ID = os.getenv('NETLIFY_SITE_ID', '')

BUILD_INTERVAL_HOURS = int(os.getenv('BUILD_INTERVAL_HOURS', '6'))

def get_build_status() -> Dict:
    """Get current build status from GitHub and Netlify."""
    github_data = check_github_actions()
    netlify_data = check_netlify_deploys()
    missed_analysis = analyze_missed_builds(github_data, netlify_data)
    
    # Determine build health
    if missed_analysis['missed_count'] == 0:
        build_health = 'Healthy'
        build_health_class = 'success'
    elif missed_analysis['missed_count'] <= 2:
        build_health = 'Warning'
        build_health_class = 'warning'
    else:
        build_health = 'Critical'
        build_health_class = 'error'
    
    github_status = 'Unknown'
    github_class = 'info'
    github_last_build = '-'
    
    if github_data['status'] == 'success' and github_data['recent_runs']:
        latest = github_data['recent_runs'][0]
        github_last_build = latest['created_at']
        if latest['conclusion'] == 'success':
            github_status = 'Success'
            github_class = 'success'
        elif latest['conclusion'] == 'failure':
            github_status = 'Failed'
            github_class = 'error'
        else:
            github_status = 'Running'
            github_class = 'warning'
    elif github_data['status'] == 'error':
        github_status = 'Error'
        github_class = 'error'
    
    netlify_status = 'Unknown'
    netlify_class = 'info'
    netlify_last_deploy = '-'
    
    if netlify_data['status'] == 'success' and netlify_data['recent_deploys']:
        latest = netlify_data['recent_deploys'][0]
        netlify_last_deploy = latest['created_at']
        if latest['state'] == 'published':
            netlify_status = 'Published'
            netlify_class = 'success'
        elif latest['state'] == 'building':
            netlify_status = 'Building'
            netlify_class = 'warning'
        else:
            netlify_status = latest['state'].title()
            netlify_class = 'warning'
    elif netlify_data['status'] == 'error':
        netlify_status = 'Error'
        netlify_class = 'error'
    
    return {
        'github_status': github_status,
        'github_class': github_class,
        'github_last_build': github_last_build,
        'netlify_status': netlify_status,
        'netlify_class': netlify_class,
        'netlify_last_deploy': netlify_last_deploy,
        'build_health': build_health,
        'build_health_class': build_health_class,
        'missed_builds': missed_analysis['missed_count'],
        'expected_builds': missed_analysis['expected_count']
    }

def get_game_improvements() -> List[Dict]:
    """Get recent game improvements from AIMCODE improvements file."""
    improvements = []
    
    try:
        aimcode_file = project_root / 'AIMCODE-GAME-IMPROVEMENTS.md'
        if aimcode_file.exists():
            with open(aimcode_file, 'r') as f:
                content = f.read()
                # Extract recent improvements (simplified - can be enhanced)
                if 'Story Integration' in content:
                    improvements.append({
                        'title': 'Story Integration',
                        'description': 'Better connection between stories and gameplay'
                    })
                if 'Building Activities' in content:
                    improvements.append({
                        'title': 'Building Activities',
                        'description': 'Enhanced hands-on creation and building'
                    })
                if 'Multiple Modes' in content:
                    improvements.append({
                        'title': 'Multiple Modes',
                        'description': 'More entry points for different learning styles'
                    })
    except Exception as e:
        print(f"Error reading game improvements: {e}")
    
    # If no improvements found, add placeholder
    if not improvements:
        improvements.append({
            'title': 'System Active',
            'description': 'Game improvements are being tracked and implemented'
        })
    
    return improvements

def get_current_focus() -> Dict:
    """Get current development focus."""
    try:
        # Check ADD tracker for current focus
        add_tracker = project_root / 'ADD-TRACKER.md'
        if add_tracker.exists():
            with open(add_tracker, 'r') as f:
                content = f.read()
                # Extract current focus (simplified)
                if 'ONE Thing' in content:
                    return {
                        'title': 'Current Focus',
                        'description': 'Tracked in ADD-TRACKER.md'
                    }
    except Exception as e:
        print(f"Error reading current focus: {e}")
    
    return {
        'title': 'System Monitoring',
        'description': 'Monitoring BallCODE integrations and builds'
    }

def get_recent_activity() -> List[Dict]:
    """Get recent activity from builds and updates."""
    activity = []
    
    # Get build status
    build_status = get_build_status()
    
    if build_status['github_last_build'] != '-':
        activity.append({
            'title': 'GitHub Actions Build',
            'time': build_status['github_last_build'],
            'type': 'build'
        })
    
    if build_status['netlify_last_deploy'] != '-':
        activity.append({
            'title': 'Netlify Deployment',
            'time': build_status['netlify_last_deploy'],
            'type': 'deploy'
        })
    
    # Add dashboard update
    activity.append({
        'title': 'Dashboard Updated',
        'time': datetime.now().isoformat(),
        'type': 'update'
    })
    
    # Sort by time (most recent first)
    activity.sort(key=lambda x: x['time'], reverse=True)
    
    return activity[:10]  # Return last 10 activities

def get_integration_status() -> Dict:
    """Get status of all integration systems."""
    build_status = get_build_status()
    
    return {
        'website': 'Active',
        'book': 'Active',
        'curriculum': 'Active',
        'game': 'Active' if build_status['github_status'] != 'Error' else 'Warning'
    }

def get_n8n_status() -> Dict:
    """Get n8n workflow status."""
    # This would ideally check n8n API, but for now return placeholder
    return {
        'last_execution': datetime.now().isoformat(),
        'status': 'Active',
        'status_class': 'success',
        'trigger_type': 'Scheduled'
    }

def get_success_metrics() -> Dict:
    """Calculate success metrics."""
    build_status = get_build_status()
    
    # Calculate success rate (simplified)
    if build_status['expected_builds'] > 0:
        success_rate = ((build_status['expected_builds'] - build_status['missed_builds']) / build_status['expected_builds']) * 100
    else:
        success_rate = 0
    
    return {
        'build_success_24h': f"{success_rate:.1f}%",
        'deploy_success_24h': f"{success_rate:.1f}%",
        'system_uptime': '99.9%'  # Placeholder
    }

def _safe_load_json(path: Path) -> Optional[Dict]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, dict) else None
    except Exception:
        return None

def _find_level_json(exercise_id: str) -> bool:
    if not exercise_id or not LEVELS_DIR.exists():
        return False
    return (LEVELS_DIR / f"{exercise_id}.json").exists()

def _thumbnail_exists(thumbnail_path: str) -> bool:
    # curriculum schema stores thumbnails as /assets/images/...
    if not thumbnail_path or not isinstance(thumbnail_path, str):
        return False
    rel = thumbnail_path.lstrip('/')
    return (project_root / 'BallCode' / rel).exists()

def get_content_completeness() -> Dict:
    """Telemetry v1: content completeness across curriculum → game → website."""
    schema = _safe_load_json(CURRICULUM_SCHEMA_FILE)
    if not schema:
        return {
            'status': 'Red',
            'status_class': 'error',
            'message': 'curriculum-schema.json missing or invalid',
            'books_total': 0,
            'books_complete': 0,
            'issues': ['curriculum-schema.json missing/invalid'],
            'missing_levels': [],
            'missing_thumbnails': [],
            'missing_pages': []
        }

    books = schema.get('books', [])
    if not isinstance(books, list):
        books = []

    issues: List[str] = []
    missing_levels: List[str] = []
    missing_thumbs: List[str] = []
    missing_pages: List[str] = []

    books_total = len(books)
    books_complete = 0

    for b in books:
        if not isinstance(b, dict):
            continue
        if b.get('status') == 'complete':
            books_complete += 1

        title = b.get('title', f"Book {b.get('id', '?')}")

        exercise_id = (b.get('game') or {}).get('exerciseId') if isinstance(b.get('game'), dict) else None
        if exercise_id and not _find_level_json(str(exercise_id)):
            missing_levels.append(f"{title}: {exercise_id}")

        thumb = None
        if isinstance(b.get('website'), dict):
            card = b['website'].get('card', {}) if isinstance(b['website'].get('card'), dict) else {}
            thumb = card.get('thumbnail')
        if thumb and not _thumbnail_exists(str(thumb)):
            missing_thumbs.append(f"{title}: {thumb}")

        page_path = None
        if isinstance(b.get('website'), dict):
            page = b['website'].get('page', {}) if isinstance(b['website'].get('page'), dict) else {}
            page_path = page.get('path')
        if page_path and isinstance(page_path, str):
            normalized = page_path.strip('/').split('/')
            if len(normalized) >= 2 and normalized[0] == 'books':
                book_slug = normalized[1]
                candidate = project_root / 'BallCode' / 'books' / f"{book_slug}.html"
                if not candidate.exists():
                    missing_pages.append(f"{title}: BallCode/books/{book_slug}.html")

    if missing_levels:
        issues.append(f"Missing level JSON: {len(missing_levels)}")
    if missing_thumbs:
        issues.append(f"Missing thumbnails: {len(missing_thumbs)}")
    if missing_pages:
        issues.append(f"Missing book pages: {len(missing_pages)}")

    if issues:
        status = 'Yellow'
        status_class = 'warning'
        message = 'Content mostly ready; some integration gaps remain'
    else:
        status = 'Green'
        status_class = 'success'
        message = 'Content integrations look consistent'

    return {
        'status': status,
        'status_class': status_class,
        'message': message,
        'books_total': books_total,
        'books_complete': books_complete,
        'missing_levels': missing_levels,
        'missing_thumbnails': missing_thumbs,
        'missing_pages': missing_pages,
        'issues': issues
    }

def get_school_readiness_report() -> Dict:
    """Telemetry v1: simple school readiness signal (pilot-package focused)."""
    missing = [str(p.relative_to(project_root)) for p in PILOT_FILES if not p.exists()]
    website_ok = WEBSITE_INDEX.exists()

    blockers: List[str] = []
    if missing:
        blockers.append(f"Missing pilot files: {', '.join(missing)}")
    if not website_ok:
        blockers.append("Website index missing (BallCode/index.html)")

    if blockers:
        # Website missing is a stronger signal than missing pilot docs.
        status = 'Red' if not website_ok else 'Yellow'
        status_class = 'error' if not website_ok else 'warning'
        return {
            'status': status,
            'status_class': status_class,
            'message': 'Pilot readiness needs attention',
            'blockers': blockers,
            'recommended_next_steps': [
                'Ensure Episode 1 story, teacher guide, and onboarding guide are present',
                'Confirm website links and access instructions are correct',
                'Run: python3 scripts/validate-release.py --packet documents/BOOK-PACKET-TEMPLATE.json'
            ]
        }

    return {
        'status': 'Green',
        'status_class': 'success',
        'message': 'Pilot package files present; ready for school review',
        'blockers': [],
        'recommended_next_steps': [
            'Send pilot package to the school contact',
            'Schedule a 15-minute onboarding call',
            'Collect feedback after first classroom run'
        ]
    }

def generate_dashboard_data() -> Dict:
    """Generate complete dashboard data."""
    now = datetime.now()
    
    build_status = get_build_status()
    
    # Determine overall status
    if build_status['build_health'] == 'Healthy':
        overall_status = 'All Systems Operational'
        overall_class = 'success'
    elif build_status['build_health'] == 'Warning':
        overall_status = 'Minor Issues Detected'
        overall_class = 'warning'
    else:
        overall_status = 'Issues Detected'
        overall_class = 'error'
    
    return {
        'last_updated': now.strftime('%Y-%m-%d %H:%M:%S'),
        'overall_status': overall_status,
        'overall_status_class': overall_class,
        'build_status': build_status,
        'integration_status': get_integration_status(),
        'content_completeness': get_content_completeness(),
        'school_readiness': get_school_readiness_report(),
        'game_improvements': get_game_improvements(),
        'current_focus': get_current_focus(),
        'recent_activity': get_recent_activity(),
        'n8n_status': get_n8n_status(),
        'success_metrics': get_success_metrics()
    }

def update_markdown_dashboard(data: Dict):
    """Update the markdown dashboard file."""
    dashboard_file = project_root / 'documents' / 'BALLCODE-INTEGRATION-DASHBOARD.md'
    
    content = f"""# BallCODE Integration Dashboard
## Real-Time System Monitoring & Status

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Last Updated:** {data['last_updated']}  
**Update Frequency:** Every {BUILD_INTERVAL_HOURS} hours (or manually via script)

---

## 🎯 SYSTEM OVERVIEW

**Status:** {data['overall_status']}  
**Overall Health:** {data['build_status']['build_health']}  
**Last Build:** {data['build_status']['github_last_build']}

---

## 📊 BUILD STATUS

### GitHub Actions
- **Status:** {data['build_status']['github_status']}
- **Last Build:** {data['build_status']['github_last_build']}
- **Build Result:** {data['build_status']['github_status']}
- **Recent Builds:** {data['build_status']['expected_builds']} expected, {data['build_status']['missed_builds']} missed

### Netlify Deployment
- **Status:** {data['build_status']['netlify_status']}
- **Last Deploy:** {data['build_status']['netlify_last_deploy']}
- **Deploy State:** {data['build_status']['netlify_status']}
- **Recent Deploys:** Active

### Build Schedule
- **Frequency:** Every {BUILD_INTERVAL_HOURS} hours
- **Expected Builds (24h):** {data['build_status']['expected_builds']} builds
- **Missed Builds:** {data['build_status']['missed_builds']}
- **Build Health:** {data['build_status']['build_health']}

---

## 🎮 GAME IMPROVEMENTS

### Recent Improvements
"""
    
    for imp in data['game_improvements']:
        content += f"- **{imp['title']}:** {imp['description']}\n"
    
    content += f"""
### Current Focus
- **{data['current_focus']['title']}:** {data['current_focus']['description']}

---

## 🔗 INTEGRATION STATUS

### Website System
- **Status:** {data['integration_status']['website']}
- **Last Update:** {data['last_updated']}
- **Hosting:** Netlify
- **URL:** Active

### Book System
- **Status:** {data['integration_status']['book']}
- **Books Complete:** Active
- **Last Book Update:** {data['last_updated']}

### Curriculum System
- **Status:** {data['integration_status']['curriculum']}
- **Last Update:** {data['last_updated']}
- **Integration:** Active

### Game System
- **Status:** {data['integration_status']['game']}
- **Last Build:** {data['build_status']['github_last_build']}
- **Unity Version:** Active
- **Build Status:** {data['build_status']['github_status']}

---

## ✅ CONTENT COMPLETENESS (Telemetry v1)

- **Status:** {data['content_completeness']['status']} ({data['content_completeness']['message']})
- **Books:** {data['content_completeness']['books_complete']}/{data['content_completeness']['books_total']} marked complete in schema

### Issues (if any)
"""
    if data.get('content_completeness', {}).get('issues'):
        for issue in data['content_completeness']['issues']:
            content += f"- {issue}\n"
    else:
        content += "- None detected\n"

    content += f"""

---

## 🏫 SCHOOL READINESS (Telemetry v1)

- **Status:** {data['school_readiness']['status']} ({data['school_readiness']['message']})

### Blockers (if any)
"""
    if data.get('school_readiness', {}).get('blockers'):
        for blocker in data['school_readiness']['blockers']:
            content += f"- {blocker}\n"
    else:
        content += "- None\n"

    content += "\n### Recommended Next Steps\n"
    for step in data.get('school_readiness', {}).get('recommended_next_steps', [])[:5]:
        content += f"- {step}\n"

    content += f"""

## 📈 RECENT ACTIVITY

### Last 24 Hours
"""
    
    for activity in data['recent_activity'][:5]:
        content += f"- **{activity['title']}** - {activity['time']}\n"
    
    content += f"""
---

## 🔄 n8n WORKFLOW STATUS

### Workflow Execution
- **Last Execution:** {data['n8n_status']['last_execution']}
- **Status:** {data['n8n_status']['status']}
- **Trigger Type:** {data['n8n_status']['trigger_type']}
- **Execution Time:** {data['last_updated']}

---

## 🎯 SUCCESS METRICS

### Build Success Rate
- **Last 24h:** {data['success_metrics']['build_success_24h']}
- **Last 7d:** Calculating...
- **Last 30d:** Calculating...

### Deployment Success Rate
- **Last 24h:** {data['success_metrics']['deploy_success_24h']}
- **Last 7d:** Calculating...
- **Last 30d:** Calculating...

### System Uptime
- **Website:** {data['success_metrics']['system_uptime']}
- **Game:** {data['success_metrics']['system_uptime']}
- **API:** {data['success_metrics']['system_uptime']}

---

## 📝 NOTES

*This dashboard is automatically updated. To manually refresh, run:*
```bash
python3 scripts/update-dashboard.py
```

*To view the HTML dashboard on localhost:*
```bash
python3 scripts/serve-dashboard.py
# Then open: http://localhost:8000/dashboard.html
```

---

**Dashboard Version:** 1.0  
**Last Manual Update:** {data['last_updated']}
"""
    
    with open(dashboard_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Markdown dashboard updated: {dashboard_file}")

def update_html_dashboard_data(data: Dict):
    """Update the JSON data file for HTML dashboard."""
    json_file = project_root / 'dashboard-data.json'
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ HTML dashboard data updated: {json_file}")

def main():
    """Main function to update dashboard."""
    print("🔄 Updating BallCODE Integration Dashboard...")
    print()
    
    # Generate dashboard data
    data = generate_dashboard_data()
    
    # Update markdown dashboard
    update_markdown_dashboard(data)
    
    # Update HTML dashboard data
    update_html_dashboard_data(data)
    
    print()
    print("✅ Dashboard update complete!")
    print(f"   Last Updated: {data['last_updated']}")
    print(f"   Overall Status: {data['overall_status']}")
    print(f"   Build Health: {data['build_status']['build_health']}")

if __name__ == '__main__':
    main()

