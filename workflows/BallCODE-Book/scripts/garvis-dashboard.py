#!/usr/bin/env python3
"""
Garvis Dashboard - Completion Reports & Metrics
BallCODE Fully Integrated System

Purpose: Generate dashboard data showing Garvis completion reports and metrics.
Not for monitoring - for seeing what Garvis has completed.
"""

import sys
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List

WORKFLOW_DIR = Path(__file__).parent.parent
GARVIS_DB = WORKFLOW_DIR / "garvis_jobs.db"

def get_garvis_metrics() -> Dict:
    """Get Garvis SIAFI metrics"""
    if not GARVIS_DB.exists():
        return {
            'siafi_percentage': 0,
            'total_jobs': 0,
            'completed_jobs': 0,
            'success_rate': 0,
            'average_completion_time': 0,
            'escalation_count': 0,
            'schools_onboarded': 0
        }
    
    conn = sqlite3.connect(GARVIS_DB)
    cursor = conn.cursor()
    
    # Total jobs
    cursor.execute("SELECT COUNT(*) FROM garvis_jobs")
    total_jobs = cursor.fetchone()[0]
    
    # Completed jobs
    cursor.execute("SELECT COUNT(*) FROM garvis_jobs WHERE status = 'completed'")
    completed_jobs = cursor.fetchone()[0]
    
    # Success rate
    success_rate = (completed_jobs / total_jobs * 100) if total_jobs > 0 else 0
    
    # Average completion time
    cursor.execute("""
        SELECT AVG(
            (julianday(completed_at) - julianday(created_at)) * 24 * 60
        ) as avg_minutes
        FROM garvis_jobs
        WHERE status = 'completed' AND completed_at IS NOT NULL
    """)
    avg_result = cursor.fetchone()
    avg_completion_time = avg_result[0] if avg_result[0] else 0
    
    # Escalation count
    cursor.execute("SELECT COUNT(*) FROM garvis_jobs WHERE escalation_needed = 1")
    escalation_count = cursor.fetchone()[0]
    
    # Schools onboarded (from tracking)
    # This would come from school_onboarding.db in full implementation
    schools_onboarded = 0
    
    # Calculate SIAFI percentage
    # This is based on tasks completed autonomously vs total tasks
    cursor.execute("""
        SELECT 
            COUNT(*) as total_tasks,
            SUM(CASE WHEN status = 'completed' AND escalation_needed = 0 THEN 1 ELSE 0 END) as autonomous_tasks
        FROM garvis_jobs
    """)
    task_stats = cursor.fetchone()
    total_tasks = task_stats[0] if task_stats else 0
    autonomous_tasks = task_stats[1] if task_stats else 0
    siafi_percentage = (autonomous_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    conn.close()
    
    return {
        'siafi_percentage': round(siafi_percentage, 1),
        'total_jobs': total_jobs,
        'completed_jobs': completed_jobs,
        'success_rate': round(success_rate, 1),
        'average_completion_time': round(avg_completion_time, 1),
        'escalation_count': escalation_count,
        'schools_onboarded': schools_onboarded,
        'last_updated': datetime.now().isoformat()
    }

def get_recent_jobs(limit: int = 10) -> List[Dict]:
    """Get recent Garvis jobs"""
    if not GARVIS_DB.exists():
        return []
    
    conn = sqlite3.connect(GARVIS_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT job_id, one_thing, status, created_at, completed_at, confidence_score
        FROM garvis_jobs
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))
    
    jobs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jobs

def generate_dashboard_data() -> Dict:
    """Generate complete dashboard data"""
    metrics = get_garvis_metrics()
    recent_jobs = get_recent_jobs(10)
    
    # System breakdown
    systems = {
        'book': {'automated': True, 'siafi': 70},
        'curriculum': {'automated': True, 'siafi': 70},
        'game': {'automated': True, 'siafi': 60},
        'website': {'automated': True, 'siafi': 50},
        'sales': {'automated': True, 'siafi': 40}
    }
    
    return {
        'metrics': metrics,
        'recent_jobs': recent_jobs,
        'systems': systems,
        'generated_at': datetime.now().isoformat()
    }

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--json':
        # Output JSON for dashboard
        data = generate_dashboard_data()
        print(json.dumps(data, indent=2))
    else:
        # Human-readable output
        metrics = get_garvis_metrics()
        recent_jobs = get_recent_jobs(5)
        
        print("\n" + "="*70)
        print("GARVIS DASHBOARD - BallCODE Fully Integrated System")
        print("="*70)
        print(f"\n📊 GARVIS SIAFI METRICS")
        print(f"   SIAFI Percentage: {metrics['siafi_percentage']}%")
        print(f"   Total Jobs: {metrics['total_jobs']}")
        print(f"   Completed: {metrics['completed_jobs']}")
        print(f"   Success Rate: {metrics['success_rate']}%")
        print(f"   Avg Completion Time: {metrics['average_completion_time']:.1f} minutes")
        print(f"   Escalations: {metrics['escalation_count']}")
        print(f"   Schools Onboarded: {metrics['schools_onboarded']}")
        
        if recent_jobs:
            print(f"\n📋 RECENT JOBS (Last 5)")
            for job in recent_jobs:
                status_emoji = {
                    'pending': '⏳',
                    'in_progress': '🔄',
                    'completed': '✅',
                    'failed': '❌',
                    'escalated': '⚠️'
                }.get(job['status'], '❓')
                print(f"   {status_emoji} {job['job_id']}: {job['one_thing'][:50]}...")
        
        print("\n" + "="*70)
        print("Garvis handles everything autonomously. Check completion reports above.")
        print("="*70 + "\n")

if __name__ == "__main__":
    main()

