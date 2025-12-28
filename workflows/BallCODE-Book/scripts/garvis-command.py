#!/usr/bin/env python3
"""
Garvis Command Interface
BallCODE Fully Integrated System - Set It And Forget It

Purpose: Single entry point for all Garvis requests.
You give ONE thing + tasks, walk away, return to completed work.

Usage:
    python scripts/garvis-command.py --one-thing "Complete Book 2 story" --tasks "Write story, Update curriculum, Deploy website"
    python scripts/garvis-command.py --status <job_id>
    python scripts/garvis-command.py --list
"""

import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import execution engine
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util
spec = importlib.util.spec_from_file_location(
    "garvis_execution_engine",
    Path(__file__).parent / "garvis-execution-engine.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
GarvisExecutionEngine = module.GarvisExecutionEngine

WORKFLOW_DIR = Path(__file__).parent.parent

def main():
    """Main command interface"""
    parser = argparse.ArgumentParser(
        description='Garvis - BallCODE Fully Integrated System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new job and execute
  python scripts/garvis-command.py --one-thing "Complete Book 2 story" \\
    --tasks "Write story, Update curriculum, Deploy website"
  
  # Check job status
  python scripts/garvis-command.py --status garvis-abc12345
  
  # List recent jobs
  python scripts/garvis-command.py --list
  
  # Execute existing job
  python scripts/garvis-command.py --execute garvis-abc12345
        """
    )
    
    parser.add_argument(
        '--one-thing',
        type=str,
        help='The ONE thing to accomplish'
    )
    
    parser.add_argument(
        '--tasks',
        type=str,
        help='Comma-separated list of tasks'
    )
    
    parser.add_argument(
        '--status',
        type=str,
        help='Get status of a job by job_id'
    )
    
    parser.add_argument(
        '--execute',
        type=str,
        help='Execute an existing job by job_id'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='List recent jobs'
    )
    
    parser.add_argument(
        '--file',
        type=str,
        help='Read request from GARVIS-REQUEST.md file'
    )
    
    args = parser.parse_args()
    
    engine = GarvisExecutionEngine()
    
    # Handle different commands
    if args.status:
        # Get job status
        status = engine.get_job_status(args.status)
        if 'error' in status:
            print(f"Error: {status['error']}")
            sys.exit(1)
        
        print("\n" + "="*70)
        print(f"GARVIS JOB STATUS: {args.status}")
        print("="*70)
        print(f"\nONE Thing: {status['one_thing']}")
        print(f"\nTasks:")
        for i, task in enumerate(status['tasks'], 1):
            print(f"  {i}. {task}")
        print(f"\nStatus: {status['status'].upper()}")
        print(f"Created: {status['created_at']}")
        if status.get('started_at'):
            print(f"Started: {status['started_at']}")
        if status.get('completed_at'):
            print(f"Completed: {status['completed_at']}")
        if status.get('confidence_score') is not None:
            print(f"Confidence: {status['confidence_score']:.0%}")
        if status.get('error'):
            print(f"\nError: {status['error']}")
        if status.get('escalation_needed'):
            print(f"\n⚠️  ESCALATION NEEDED: {status.get('escalation_reason', 'Unknown reason')}")
        if status.get('result'):
            print(f"\nResults:")
            results = status['result']
            for task, result in results.items():
                print(f"  • {task}: {result.get('status', 'unknown')}")
        
        if status.get('execution_log'):
            print(f"\nExecution Log:")
            for entry in status['execution_log'][-10:]:  # Show last 10 entries
                print(f"  [{entry['timestamp']}] {entry['step']}: {entry['action']}")
        
        print("\n" + "="*70)
    
    elif args.execute:
        # Execute existing job
        print(f"\n🚀 Executing Garvis job: {args.execute}")
        print("="*70)
        try:
            result = engine.execute_job(args.execute)
            print(f"\n✅ Job completed successfully!")
            print(f"Status: {result['status']}")
            if result.get('quality'):
                print(f"Quality: {'✅ Passed' if result['quality']['passed'] else '⚠️  Issues found'}")
                if result['quality'].get('confidence'):
                    print(f"Confidence: {result['quality']['confidence']:.0%}")
            print("\n" + "="*70)
        except Exception as e:
            print(f"\n❌ Error executing job: {str(e)}")
            sys.exit(1)
    
    elif args.list:
        # List recent jobs
        import sqlite3
        db_path = WORKFLOW_DIR / "garvis_jobs.db"
        if not db_path.exists():
            print("No jobs found. Database not initialized.")
            sys.exit(0)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT job_id, one_thing, status, created_at, completed_at
            FROM garvis_jobs
            ORDER BY created_at DESC
            LIMIT 20
        """)
        jobs = cursor.fetchall()
        conn.close()
        
        if not jobs:
            print("No jobs found.")
            sys.exit(0)
        
        print("\n" + "="*70)
        print("RECENT GARVIS JOBS")
        print("="*70)
        print(f"\n{'Job ID':<15} {'Status':<12} {'ONE Thing':<30} {'Created':<20}")
        print("-"*70)
        for job in jobs:
            job_id, one_thing, status, created_at, completed_at = job
            one_thing_short = (one_thing[:27] + '...') if len(one_thing) > 30 else one_thing
            status_emoji = {
                'pending': '⏳',
                'in_progress': '🔄',
                'completed': '✅',
                'failed': '❌',
                'escalated': '⚠️'
            }.get(status, '❓')
            print(f"{job_id:<15} {status_emoji} {status:<10} {one_thing_short:<30} {created_at[:19]}")
        print("="*70)
        print(f"\nTotal: {len(jobs)} jobs")
        print("\nUse --status <job_id> to see details")
    
    elif args.file:
        # Read from file
        file_path = Path(args.file)
        if not file_path.exists():
            file_path = WORKFLOW_DIR / "GARVIS-REQUEST.md"
        
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        
        # Parse file
        content = file_path.read_text()
        one_thing = None
        tasks = []
        context = None
        
        for line in content.split('\n'):
            if line.startswith('**ONE Thing:**'):
                one_thing = line.split('**ONE Thing:**')[1].strip()
            elif line.startswith('**Tasks:**'):
                continue
            elif line.strip().startswith('1.') or line.strip().startswith('-'):
                task = line.strip().lstrip('1.2.3.4.5.6.7.8.9.0.-').strip()
                if task:
                    tasks.append(task)
            elif line.startswith('**Context:**'):
                context = line.split('**Context:**')[1].strip()
        
        if not one_thing or not tasks:
            print("Error: Could not parse ONE Thing and Tasks from file")
            sys.exit(1)
        
        print(f"\n📋 Read request from: {file_path}")
        print(f"ONE Thing: {one_thing}")
        print(f"Tasks: {', '.join(tasks)}")
        print("\n🚀 Creating Garvis job...")
        
        job_id = engine.create_job(one_thing, tasks, context)
        print(f"\n✅ Job created: {job_id}")
        print("="*70)
        print("Garvis is starting execution...")
        print("You can walk away now. Garvis will complete everything.")
        print("="*70)
        
        # Start execution in background (for now, execute synchronously)
        try:
            result = engine.execute_job(job_id)
            print(f"\n✅ Job completed!")
            print(f"Status: {result['status']}")
        except Exception as e:
            print(f"\n⚠️  Job started but encountered an issue: {str(e)}")
            print(f"Check status with: python scripts/garvis-command.py --status {job_id}")
    
    elif args.one_thing and args.tasks:
        # Create and execute new job
        tasks = [t.strip() for t in args.tasks.split(',')]
        
        print("\n" + "="*70)
        print("🚀 GARVIS - BallCODE Fully Integrated System")
        print("="*70)
        print(f"\nONE Thing: {args.one_thing}")
        print(f"\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        print("\n" + "="*70)
        print("Creating job and starting execution...")
        print("You can walk away now. Garvis will complete everything.")
        print("="*70 + "\n")
        
        job_id = engine.create_job(args.one_thing, tasks)
        print(f"Job ID: {job_id}")
        print("Status: Starting execution...\n")
        
        try:
            result = engine.execute_job(job_id)
            print("\n" + "="*70)
            print("✅ JOB COMPLETED")
            print("="*70)
            print(f"Status: {result['status']}")
            if result.get('quality'):
                quality = result['quality']
                if quality['passed']:
                    print("Quality: ✅ All checks passed")
                else:
                    print(f"Quality: ⚠️  Issues found: {quality.get('reason', 'Unknown')}")
                if quality.get('confidence'):
                    print(f"Confidence: {quality['confidence']:.0%}")
            
            if result.get('results'):
                print("\nResults:")
                for task, task_result in result['results'].items():
                    status_emoji = '✅' if task_result.get('status') == 'success' else '⚠️'
                    print(f"  {status_emoji} {task}: {task_result.get('status', 'unknown')}")
            
            print("\n" + "="*70)
            print(f"Check full details: python scripts/garvis-command.py --status {job_id}")
            print("="*70)
        except Exception as e:
            print(f"\n❌ Error during execution: {str(e)}")
            print(f"Job ID: {job_id}")
            print(f"Check status: python scripts/garvis-command.py --status {job_id}")
            sys.exit(1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()


