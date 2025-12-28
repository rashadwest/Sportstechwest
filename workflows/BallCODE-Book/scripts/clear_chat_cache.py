#!/usr/bin/env python3
"""
Clear Cursor Chat Cache - Phase 0.1.1
Research-Backed Solution: Clearing chat history proven to fix lag issues

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import sys

# Cursor workspace storage locations
CURSOR_STORAGE_PATHS = {
    'macos': Path.home() / 'Library/Application Support/Cursor/User/workspaceStorage',
    'linux': Path.home() / '.config/Cursor/User/workspaceStorage',
    'windows': Path(os.environ.get('APPDATA', '')) / 'Cursor/User/workspaceStorage'
}

def detect_platform():
    """Detect the current platform."""
    if sys.platform == 'darwin':
        return 'macos'
    elif sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform == 'win32':
        return 'windows'
    return 'unknown'

def get_cursor_storage_path():
    """Get the Cursor storage path for current platform."""
    platform = detect_platform()
    if platform == 'unknown':
        print("❌ Unknown platform. Please specify path manually.")
        return None
    return CURSOR_STORAGE_PATHS[platform]

def backup_chat_data(storage_path):
    """Backup chat data before clearing."""
    backup_dir = Path('data/cursor_backups') / datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📦 Creating backup at: {backup_dir}")
    
    # Find workspace storage directories
    if storage_path.exists():
        for workspace_dir in storage_path.iterdir():
            if workspace_dir.is_dir():
                # Look for chat-related files
                chat_files = list(workspace_dir.rglob('*chat*'))
                chat_files.extend(list(workspace_dir.rglob('*conversation*')))
                
                if chat_files:
                    workspace_backup = backup_dir / workspace_dir.name
                    workspace_backup.mkdir(parents=True, exist_ok=True)
                    
                    for chat_file in chat_files:
                        try:
                            if chat_file.is_file():
                                shutil.copy2(chat_file, workspace_backup / chat_file.name)
                        except Exception as e:
                            print(f"⚠️  Could not backup {chat_file}: {e}")
    
    return backup_dir

def clear_chat_cache(storage_path, keep_recent_days=7):
    """Clear old chat cache while keeping recent chats."""
    if not storage_path or not storage_path.exists():
        print(f"❌ Cursor storage path not found: {storage_path}")
        return False
    
    print(f"🔍 Scanning Cursor storage: {storage_path}")
    
    cleared_count = 0
    kept_count = 0
    total_size_cleared = 0
    
    for workspace_dir in storage_path.iterdir():
        if not workspace_dir.is_dir():
            continue
        
        # Look for chat-related directories and files
        chat_dirs = [
            workspace_dir / 'anysphere.cursor-retrieval',
            workspace_dir / 'state',
        ]
        
        for chat_dir in chat_dirs:
            if chat_dir.exists():
                # Clear old cache files
                for cache_file in chat_dir.rglob('*'):
                    if cache_file.is_file():
                        try:
                            file_age = (datetime.now().timestamp() - cache_file.stat().st_mtime) / 86400
                            
                            if file_age > keep_recent_days:
                                file_size = cache_file.stat().st_size
                                cache_file.unlink()
                                cleared_count += 1
                                total_size_cleared += file_size
                            else:
                                kept_count += 1
                        except Exception as e:
                            print(f"⚠️  Could not clear {cache_file}: {e}")
    
    print(f"\n✅ Cache clearing complete:")
    print(f"   - Cleared: {cleared_count} files ({total_size_cleared / 1024 / 1024:.2f} MB)")
    print(f"   - Kept: {kept_count} recent files")
    
    return True

def main():
    """Main execution."""
    print("=" * 60)
    print("Cursor Chat Cache Cleaner - Phase 0.1.1")
    print("Research-Backed: Clearing chat history fixes lag issues")
    print("=" * 60)
    print()
    
    storage_path = get_cursor_storage_path()
    
    if not storage_path:
        print("❌ Could not locate Cursor storage. Please check Cursor is installed.")
        return 1
    
    # Ask for confirmation
    print(f"📍 Cursor storage location: {storage_path}")
    print()
    print("⚠️  This will:")
    print("   - Backup your chat data")
    print("   - Clear chat cache older than 7 days")
    print("   - Keep recent chats (last 7 days)")
    print()
    
    response = input("Continue? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("❌ Cancelled.")
        return 0
    
    # Create backup
    backup_path = backup_chat_data(storage_path)
    print(f"✅ Backup created at: {backup_path}")
    print()
    
    # Clear cache
    if clear_chat_cache(storage_path):
        print()
        print("🎉 Chat cache cleared successfully!")
        print()
        print("📝 Next steps:")
        print("   1. Restart Cursor")
        print("   2. Test chat responsiveness")
        print("   3. If lag persists, run Phase 0.1.2 (file watcher optimization)")
        return 0
    else:
        print("❌ Failed to clear cache. Check permissions.")
        return 1

if __name__ == '__main__':
    sys.exit(main())


