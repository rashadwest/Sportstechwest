#!/usr/bin/env python3
"""
Robot: Complete Dashboard Management System
Automatically handles all dashboard operations: setup, update, serve, view

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import subprocess
import re
from pathlib import Path
from typing import Optional

# Project root
PROJECT_ROOT = Path(__file__).parent
SHELL_CONFIG = Path.home() / '.zshrc'

def check_and_set_env_vars():
    """Check and set environment variables if needed."""
    # Import the robot function directly
    import importlib.util
    env_script = PROJECT_ROOT / 'robot-set-dashboard-env-vars.py'
    if env_script.exists():
        spec = importlib.util.spec_from_file_location("robot_set_dashboard_env_vars", env_script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.robot_set_dashboard_env()
    return False

def update_dashboard():
    """Update dashboard data."""
    print("🔄 Updating dashboard data...")
    print()
    
    script_path = PROJECT_ROOT / 'scripts' / 'update-dashboard.py'
    if not script_path.exists():
        print(f"❌ Update script not found: {script_path}")
        return False
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(PROJECT_ROOT),
            capture_output=False
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")
        return False

def serve_dashboard():
    """Start dashboard server."""
    print("🚀 Starting dashboard server...")
    print()
    print("   Open: http://localhost:8000/dashboard.html")
    print("   Press Ctrl+C to stop")
    print()
    
    script_path = PROJECT_ROOT / 'scripts' / 'serve-dashboard.py'
    if not script_path.exists():
        print(f"❌ Serve script not found: {script_path}")
        return False
    
    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(PROJECT_ROOT)
        )
        return True
    except KeyboardInterrupt:
        print("\n✅ Server stopped")
        return True
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def view_dashboard():
    """View markdown dashboard."""
    dashboard_path = PROJECT_ROOT / 'documents' / 'BALLCODE-INTEGRATION-DASHBOARD.md'
    
    if not dashboard_path.exists():
        print(f"❌ Dashboard not found: {dashboard_path}")
        print("   Run: robot-dashboard update")
        return False
    
    try:
        with open(dashboard_path, 'r') as f:
            content = f.read()
            print(content)
        return True
    except Exception as e:
        print(f"❌ Error reading dashboard: {e}")
        return False

def setup_dashboard():
    """Complete dashboard setup: env vars + initial update."""
    print("=" * 70)
    print("🤖 ROBOT: Complete Dashboard Setup")
    print("=" * 70)
    print()
    
    # Step 1: Set environment variables
    print("Step 1: Setting environment variables...")
    print()
    try:
        import importlib.util
        env_script = PROJECT_ROOT / 'robot-set-dashboard-env-vars.py'
        if env_script.exists():
            spec = importlib.util.spec_from_file_location("robot_set_dashboard_env_vars", env_script)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.robot_set_dashboard_env()
        else:
            print("⚠️  Env setup script not found")
    except Exception as e:
        print(f"⚠️  Error setting env vars: {e}")
    
    print()
    
    # Step 2: Update dashboard
    print("Step 2: Updating dashboard data...")
    print()
    update_dashboard()
    
    print()
    print("=" * 70)
    print("✅ Dashboard setup complete!")
    print("=" * 70)
    print()
    print("📝 Next steps:")
    print("   robot-dashboard view    # View dashboard")
    print("   robot-dashboard serve   # Start web dashboard")
    print()

def check_dashboard_status():
    """Check dashboard system status."""
    print("=" * 70)
    print("📊 Dashboard System Status")
    print("=" * 70)
    print()
    
    # Check files
    files = {
        'Dashboard Script': PROJECT_ROOT / 'scripts' / 'dashboard',
        'Update Script': PROJECT_ROOT / 'scripts' / 'update-dashboard.py',
        'Serve Script': PROJECT_ROOT / 'scripts' / 'serve-dashboard.py',
        'Markdown Dashboard': PROJECT_ROOT / 'documents' / 'BALLCODE-INTEGRATION-DASHBOARD.md',
        'HTML Dashboard': PROJECT_ROOT / 'dashboard.html',
        'Dashboard Data': PROJECT_ROOT / 'dashboard-data.json'
    }
    
    print("📁 Files:")
    for name, path in files.items():
        exists = path.exists()
        status = "✅" if exists else "❌"
        print(f"   {status} {name}: {exists}")
    
    print()
    
    # Check environment variables
    print("🔧 Environment Variables:")
    env_vars = [
        'GITHUB_TOKEN',
        'GITHUB_REPO_OWNER',
        'GITHUB_REPO_NAME',
        'GITHUB_WORKFLOW_FILE',
        'NETLIFY_TOKEN',
        'NETLIFY_SITE_ID',
        'BUILD_INTERVAL_HOURS'
    ]
    
    for var in env_vars:
        value = os.getenv(var, '')
        if value:
            # Mask sensitive tokens
            if 'TOKEN' in var:
                display_value = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            else:
                display_value = value
            print(f"   ✅ {var} = {display_value}")
        else:
            print(f"   ⚠️  {var} = (not set)")
    
    print()
    
    # Check alias
    alias_set = False
    if SHELL_CONFIG.exists():
        with open(SHELL_CONFIG, 'r') as f:
            if 'alias dashboard=' in f.read():
                alias_set = True
    
    print("🔗 Dashboard Alias:")
    if alias_set:
        print("   ✅ Dashboard alias is set")
    else:
        print("   ⚠️  Dashboard alias not set")
        print("   Run: robot-dashboard setup")
    
    print()
    print("=" * 70)

def main():
    """Main robot dashboard command handler."""
    if len(sys.argv) < 2:
        # Show help
        print("=" * 70)
        print("🤖 ROBOT: BallCODE Dashboard Management")
        print("=" * 70)
        print()
        print("Usage: robot-dashboard [command]")
        print()
        print("Commands:")
        print("  setup      - Complete setup (env vars + initial update)")
        print("  update     - Update dashboard data")
        print("  serve      - Start HTML dashboard server (localhost:8000)")
        print("  view       - View markdown dashboard")
        print("  status     - Check dashboard system status")
        print("  env        - Set environment variables")
        print()
        print("Examples:")
        print("  robot-dashboard setup     # First-time setup")
        print("  robot-dashboard view     # Quick view")
        print("  robot-dashboard serve    # Start web dashboard")
        print("  robot-dashboard update   # Refresh data")
        print()
        print("=" * 70)
        return
    
    command = sys.argv[1].lower()
    
    if command == 'setup':
        setup_dashboard()
    elif command == 'update':
        update_dashboard()
    elif command == 'serve':
        serve_dashboard()
    elif command == 'view':
        view_dashboard()
    elif command == 'status':
        check_dashboard_status()
    elif command == 'env':
        try:
            import importlib.util
            env_script = PROJECT_ROOT / 'robot-set-dashboard-env-vars.py'
            if env_script.exists():
                spec = importlib.util.spec_from_file_location("robot_set_dashboard_env_vars", env_script)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                module.robot_set_dashboard_env()
            else:
                print("❌ Env setup script not found")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print(f"❌ Unknown command: {command}")
        print("   Run: robot-dashboard (no args) for help")
        sys.exit(1)

if __name__ == '__main__':
    main()

