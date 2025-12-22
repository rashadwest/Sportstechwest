#!/usr/bin/env python3
"""
Set n8n Environment Variables
Usage: python3 set-n8n-env-vars.py [UNITY_REPO_URL] [UNITY_PROJECT_PATH]
"""

import sqlite3
import json
import sys
import os
from pathlib import Path

# n8n database location
n8n_db_path = Path.home() / '.n8n' / 'database.sqlite'

def set_env_vars(repo_url=None, project_path=None):
    """Set n8n environment variables"""
    
    if not n8n_db_path.exists():
        print(f"❌ n8n database not found at: {n8n_db_path}")
        print()
        print("If n8n is running on a remote server:")
        print("  1. SSH into the remote server")
        print("  2. Run this script there")
        print("  OR")
        print("  3. Set via n8n UI: Settings → Environment Variables")
        return False
    
    try:
        conn = sqlite3.connect(str(n8n_db_path))
        cursor = conn.cursor()
        
        # Check database structure
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        if 'settings' in tables:
            # Method 1: Direct settings table (newer n8n)
            if repo_url:
                cursor.execute("""
                    INSERT OR REPLACE INTO settings ("key", value) 
                    VALUES (?, ?)
                """, ('UNITY_REPO_URL', repo_url))
                print(f"✅ Set UNITY_REPO_URL: {repo_url}")
            
            if project_path:
                cursor.execute("""
                    INSERT OR REPLACE INTO settings ("key", value) 
                    VALUES (?, ?)
                """, ('UNITY_PROJECT_PATH', project_path))
                print(f"✅ Set UNITY_PROJECT_PATH: {project_path}")
        
        elif 'key_value_store' in tables:
            # Method 2: Key-value store (older n8n)
            if repo_url:
                cursor.execute("""
                    INSERT OR REPLACE INTO key_value_store (key, value) 
                    VALUES (?, ?)
                """, ('UNITY_REPO_URL', repo_url))
                print(f"✅ Set UNITY_REPO_URL: {repo_url}")
            
            if project_path:
                cursor.execute("""
                    INSERT OR REPLACE INTO key_value_store (key, value) 
                    VALUES (?, ?)
                """, ('UNITY_PROJECT_PATH', project_path))
                print(f"✅ Set UNITY_PROJECT_PATH: {project_path}")
        
        else:
            # Method 3: Variables JSON in settings
            cursor.execute("SELECT value FROM settings WHERE key = 'variables'")
            result = cursor.fetchone()
            
            vars_dict = json.loads(result[0]) if result and result[0] else {}
            
            if repo_url:
                vars_dict['UNITY_REPO_URL'] = repo_url
                print(f"✅ Set UNITY_REPO_URL: {repo_url}")
            
            if project_path:
                vars_dict['UNITY_PROJECT_PATH'] = project_path
                print(f"✅ Set UNITY_PROJECT_PATH: {project_path}")
            
            cursor.execute("""
                INSERT OR REPLACE INTO settings ("key", value) 
                VALUES (?, ?)
            """, ('variables', json.dumps(vars_dict)))
        
        conn.commit()
        conn.close()
        
        print()
        print("✅ Environment variables set successfully!")
        print()
        print("⚠️  IMPORTANT: Restart n8n for changes to take effect:")
        print("   - If local: Restart n8n application")
        print("   - If remote: SSH and restart n8n service")
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error setting variables: {e}")
        print()
        print("Alternative: Set via n8n UI:")
        print("   Settings → Environment Variables → Add Variable")
        return False

if __name__ == '__main__':
    # Get values from command line or prompt
    if len(sys.argv) >= 3:
        repo_url = sys.argv[1]
        project_path = sys.argv[2]
    elif len(sys.argv) == 2:
        repo_url = sys.argv[1]
        project_path = input("UNITY_PROJECT_PATH (local path): ").strip()
    else:
        repo_url = input("UNITY_REPO_URL (GitHub repo URL): ").strip()
        project_path = input("UNITY_PROJECT_PATH (local path): ").strip()
    
    if not repo_url and not project_path:
        print("❌ No values provided")
        print()
        print("Usage:")
        print("  python3 set-n8n-env-vars.py [REPO_URL] [PROJECT_PATH]")
        print()
        print("Example:")
        print("  python3 set-n8n-env-vars.py https://github.com/user/repo.git /path/to/project")
        sys.exit(1)
    
    set_env_vars(repo_url if repo_url else None, project_path if project_path else None)
