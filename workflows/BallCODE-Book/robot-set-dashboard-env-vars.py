#!/usr/bin/env python3
"""
Robot: Automatically Set Dashboard Environment Variables
Fully automated script that sets required environment variables for dashboard monitoring

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import re
from pathlib import Path

# Configuration - Default values (user can update these)
CONFIG = {
    'GITHUB_TOKEN': '',  # User needs to set this
    'GITHUB_REPO_OWNER': 'rashadwest',
    'GITHUB_REPO_NAME': 'BallCode',
    'GITHUB_WORKFLOW_FILE': '.github/workflows/build.yml',  # Common workflow file
    'NETLIFY_TOKEN': '',  # User needs to set this
    'NETLIFY_SITE_ID': '',  # User needs to set this
    'BUILD_INTERVAL_HOURS': '6'  # Every 6 hours
}

# Shell config file
SHELL_CONFIG = Path.home() / '.zshrc'
BACKUP_CONFIG = Path.home() / '.zshrc.backup'

def check_variable_set(var_name: str, config_file: Path) -> bool:
    """Check if environment variable is already set in config file."""
    if not config_file.exists():
        return False
    
    with open(config_file, 'r') as f:
        content = f.read()
        # Check for export VAR_NAME= or export VAR_NAME = patterns
        pattern = rf'export\s+{var_name}\s*='
        return bool(re.search(pattern, content))

def get_variable_value(var_name: str, config_file: Path) -> str:
    """Get current value of environment variable from config file."""
    if not config_file.exists():
        return ''
    
    with open(config_file, 'r') as f:
        for line in f:
            match = re.search(rf'export\s+{var_name}\s*=\s*["\']?([^"\'\n]+)["\']?', line)
            if match:
                return match.group(1).strip()
    return ''

def set_variable(var_name: str, value: str, config_file: Path) -> bool:
    """Set environment variable in config file."""
    if not config_file.exists():
        # Create file if it doesn't exist
        config_file.touch()
    
    # Read current content
    with open(config_file, 'r') as f:
        lines = f.readlines()
    
    # Check if variable already exists
    pattern = rf'export\s+{var_name}\s*='
    var_found = False
    new_lines = []
    
    for line in lines:
        if re.search(pattern, line):
            # Replace existing line
            new_lines.append(f'export {var_name}="{value}"\n')
            var_found = True
        else:
            new_lines.append(line)
    
    # If variable not found, add it
    if not var_found:
        # Add dashboard section if it doesn't exist
        dashboard_section = False
        for i, line in enumerate(new_lines):
            if '# BallCODE Dashboard Configuration' in line:
                dashboard_section = True
                # Insert after this section header
                new_lines.insert(i + 1, f'export {var_name}="{value}"\n')
                break
        
        if not dashboard_section:
            # Add dashboard section at the end
            new_lines.append('\n# BallCODE Dashboard Configuration\n')
            new_lines.append(f'export {var_name}="{value}"\n')
    
    # Write back
    with open(config_file, 'w') as f:
        f.writelines(new_lines)
    
    return True

def check_dashboard_alias(config_file: Path) -> bool:
    """Check if dashboard alias is set."""
    if not config_file.exists():
        return False
    
    with open(config_file, 'r') as f:
        content = f.read()
        return 'alias dashboard=' in content

def set_dashboard_alias(config_file: Path) -> bool:
    """Set dashboard alias in config file."""
    if not config_file.exists():
        config_file.touch()
    
    alias_line = 'alias dashboard="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard"\n'
    
    with open(config_file, 'r') as f:
        lines = f.readlines()
    
    # Check if alias already exists
    alias_found = False
    new_lines = []
    
    for line in lines:
        if 'alias dashboard=' in line:
            new_lines.append(alias_line)
            alias_found = True
        else:
            new_lines.append(line)
    
    if not alias_found:
        # Add alias section if it doesn't exist
        alias_section = False
        for i, line in enumerate(new_lines):
            if '# BallCODE Dashboard' in line:
                alias_section = True
                new_lines.insert(i + 1, alias_line)
                break
        
        if not alias_section:
            new_lines.append('\n# BallCODE Dashboard - Quick Access\n')
            new_lines.append(alias_line)
    
    with open(config_file, 'w') as f:
        f.writelines(new_lines)
    
    return True

def verify_dashboard_files() -> dict:
    """Verify all dashboard files exist."""
    project_root = Path(__file__).parent
    files = {
        'dashboard_script': project_root / 'scripts' / 'dashboard',
        'update_script': project_root / 'scripts' / 'update-dashboard.py',
        'serve_script': project_root / 'scripts' / 'serve-dashboard.py',
        'markdown_dashboard': project_root / 'documents' / 'BALLCODE-INTEGRATION-DASHBOARD.md',
        'html_dashboard': project_root / 'dashboard.html'
    }
    
    results = {}
    for name, path in files.items():
        results[name] = path.exists() and path.is_file()
    
    return results

def robot_set_dashboard_env():
    """Robot: Automatically set all dashboard environment variables"""
    
    print("=" * 70)
    print("🤖 ROBOT: Setting Dashboard Environment Variables")
    print("=" * 70)
    print()
    
    # Backup config file
    if SHELL_CONFIG.exists():
        print(f"📋 Backing up {SHELL_CONFIG}...")
        with open(SHELL_CONFIG, 'r') as src, open(BACKUP_CONFIG, 'w') as dst:
            dst.write(src.read())
        print(f"   ✅ Backup saved to {BACKUP_CONFIG}")
        print()
    
    # Check and set variables
    print("🔍 Checking environment variables...")
    print()
    
    variables_set = []
    variables_skipped = []
    variables_need_value = []
    
    for var_name, default_value in CONFIG.items():
        current_value = get_variable_value(var_name, SHELL_CONFIG)
        is_set = check_variable_set(var_name, SHELL_CONFIG)
        
        if is_set and current_value:
            print(f"   ✅ {var_name} = {current_value} (already set)")
            variables_skipped.append(var_name)
        elif default_value:
            # Set with default value
            set_variable(var_name, default_value, SHELL_CONFIG)
            print(f"   ✅ {var_name} = {default_value} (set)")
            variables_set.append(var_name)
        else:
            # Variable needs user input
            print(f"   ⚠️  {var_name} = (needs to be set manually)")
            variables_need_value.append(var_name)
    
    print()
    
    # Check and set dashboard alias
    print("🔍 Checking dashboard alias...")
    if check_dashboard_alias(SHELL_CONFIG):
        print("   ✅ Dashboard alias already set")
    else:
        set_dashboard_alias(SHELL_CONFIG)
        print("   ✅ Dashboard alias set")
    print()
    
    # Verify dashboard files
    print("🔍 Verifying dashboard files...")
    file_status = verify_dashboard_files()
    all_files_exist = all(file_status.values())
    
    for name, exists in file_status.items():
        status = "✅" if exists else "❌"
        print(f"   {status} {name}: {exists}")
    
    print()
    
    # Summary
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print()
    
    if variables_set:
        print(f"✅ Variables set: {len(variables_set)}")
        for var in variables_set:
            print(f"   - {var}")
        print()
    
    if variables_skipped:
        print(f"⏭️  Variables already set: {len(variables_skipped)}")
        for var in variables_skipped:
            print(f"   - {var}")
        print()
    
    if variables_need_value:
        print(f"⚠️  Variables need manual setup: {len(variables_need_value)}")
        for var in variables_need_value:
            print(f"   - {var}")
        print()
        print("   To set these, edit ~/.zshrc and add:")
        print("   export GITHUB_TOKEN='your_token_here'")
        print("   export NETLIFY_TOKEN='your_token_here'")
        print("   export NETLIFY_SITE_ID='your_site_id_here'")
        print()
    
    if all_files_exist:
        print("✅ All dashboard files exist")
    else:
        print("⚠️  Some dashboard files are missing")
        print("   Run: python3 scripts/update-dashboard.py")
        print()
    
    print("=" * 70)
    print("✅ ROBOT: Dashboard environment setup complete!")
    print("=" * 70)
    print()
    print("📝 NEXT STEPS:")
    print()
    print("1. Reload your shell configuration:")
    print("   source ~/.zshrc")
    print()
    print("2. Test the dashboard:")
    print("   dashboard view    # View markdown dashboard")
    print("   dashboard serve   # Start HTML dashboard")
    print("   dashboard update  # Update dashboard data")
    print()
    if variables_need_value:
        print("3. Set missing variables (optional, for full build monitoring):")
        print("   Edit ~/.zshrc and add GITHUB_TOKEN, NETLIFY_TOKEN, NETLIFY_SITE_ID")
        print("   Then: source ~/.zshrc")
        print()
    
    return True

if __name__ == '__main__':
    try:
        robot_set_dashboard_env()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


