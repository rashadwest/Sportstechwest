#!/usr/bin/env python3
"""
Robot: Automatically Set n8n Environment Variables
Fully automated script that sets required environment variables in n8n

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sqlite3
import json
import sys
import os
from pathlib import Path

# Configuration - Values from previous setup
CONFIG = {
    'UNITY_REPO_URL': 'https://github.com/rashadwest/BallCode.git',
    'UNITY_PROJECT_PATH': '/Users/rashadwest/BTEBallCODE',
    'WORKFLOW_PATH': '/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book'
}

# n8n database location
n8n_db_path = Path.home() / '.n8n' / 'database.sqlite'

def robot_set_env_vars():
    """Robot: Automatically set all n8n environment variables"""
    
    print("=" * 70)
    print("🤖 ROBOT: Setting n8n Environment Variables")
    print("=" * 70)
    print()
    
    if not n8n_db_path.exists():
        print(f"❌ n8n database not found at: {n8n_db_path}")
        print()
        print("If n8n is running on a remote server (Raspberry Pi):")
        print("  1. SSH into the remote server")
        print("  2. Run this script there")
        print("  OR")
        print("  3. Set via n8n UI: Settings → Environment Variables")
        return False
    
    print(f"✅ Found n8n database: {n8n_db_path}")
    print()
    print("📋 Setting environment variables:")
    for key, value in CONFIG.items():
        print(f"   {key} = {value}")
    print()
    
    try:
        conn = sqlite3.connect(str(n8n_db_path))
        cursor = conn.cursor()
        
        # Check database structure
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        if 'settings' in tables:
            # Method 1: Direct settings table (newer n8n)
            print("📊 Using Method 1: Direct settings table")
            for key, value in CONFIG.items():
                cursor.execute("""
                    INSERT OR REPLACE INTO settings ("key", value) 
                    VALUES (?, ?)
                """, (key, value))
                print(f"   ✅ Set {key}")
        
        elif 'key_value_store' in tables:
            # Method 2: Key-value store (older n8n)
            print("📊 Using Method 2: Key-value store")
            for key, value in CONFIG.items():
                cursor.execute("""
                    INSERT OR REPLACE INTO key_value_store (key, value) 
                    VALUES (?, ?)
                """, (key, value))
                print(f"   ✅ Set {key}")
        
        else:
            # Method 3: Variables JSON in settings
            print("📊 Using Method 3: Variables JSON in settings")
            cursor.execute("SELECT value FROM settings WHERE key = 'variables'")
            result = cursor.fetchone()
            
            vars_dict = json.loads(result[0]) if result and result[0] else {}
            
            # Update all variables
            for key, value in CONFIG.items():
                vars_dict[key] = value
                print(f"   ✅ Set {key}")
            
            cursor.execute("""
                INSERT OR REPLACE INTO settings ("key", value) 
                VALUES (?, ?)
            """, ('variables', json.dumps(vars_dict)))
        
        conn.commit()
        conn.close()
        
        print()
        print("=" * 70)
        print("✅ ROBOT: Environment variables set successfully!")
        print("=" * 70)
        print()
        print("⚠️  IMPORTANT: Restart n8n for changes to take effect:")
        print("   - If local: Restart n8n application")
        print("   - If remote: SSH and restart n8n service")
        print()
        print("📋 Variables set:")
        for key, value in CONFIG.items():
            print(f"   {key} = {value}")
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error setting variables: {e}")
        print()
        print("Alternative: Set via n8n UI:")
        print("   Settings → Environment Variables → Add Variable")
        return False

if __name__ == '__main__':
    success = robot_set_env_vars()
    sys.exit(0 if success else 1)



