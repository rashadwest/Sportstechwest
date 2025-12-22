#!/usr/bin/env python3
"""
Backup and Restore System
Automated backup and restore for email system
"""

import sys
import os
import shutil
import json
from datetime import datetime
from pathlib import Path
import sqlite3

class BackupSystem:
    """Automated backup and restore system"""
    
    def __init__(self, backup_dir: str = "backups"):
        self.base_dir = Path(__file__).parent
        self.backup_dir = self.base_dir / backup_dir
        self.backup_dir.mkdir(exist_ok=True)
        self.db_path = self.base_dir / "emails.db"
        self.config_path = self.base_dir / "email_config.json"
    
    def create_backup(self, name: str = None) -> str:
        """
        Create backup of email system
        
        Args:
            name: Optional backup name (default: timestamp)
            
        Returns:
            Path to backup directory
        """
        if not name:
            name = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        backup_path = self.backup_dir / name
        backup_path.mkdir(exist_ok=True)
        
        # Backup database
        if self.db_path.exists():
            shutil.copy2(self.db_path, backup_path / "emails.db")
            print(f"✅ Backed up database: {self.db_path.name}")
        
        # Backup configuration
        if self.config_path.exists():
            shutil.copy2(self.config_path, backup_path / "email_config.json")
            print(f"✅ Backed up configuration: {self.config_path.name}")
        
        # Create backup manifest
        manifest = {
            "timestamp": datetime.now().isoformat(),
            "backup_name": name,
            "files": [
                "emails.db",
                "email_config.json"
            ]
        }
        
        manifest_path = backup_path / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"✅ Backup created: {backup_path}")
        return str(backup_path)
    
    def restore_backup(self, backup_name: str):
        """
        Restore from backup
        
        Args:
            backup_name: Name of backup to restore
        """
        backup_path = self.backup_dir / backup_name
        
        if not backup_path.exists():
            raise FileNotFoundError(f"Backup not found: {backup_name}")
        
        # Restore database
        backup_db = backup_path / "emails.db"
        if backup_db.exists():
            shutil.copy2(backup_db, self.db_path)
            print(f"✅ Restored database from backup")
        
        # Restore configuration
        backup_config = backup_path / "email_config.json"
        if backup_config.exists():
            shutil.copy2(backup_config, self.config_path)
            print(f"✅ Restored configuration from backup")
        
        print(f"✅ Restore complete from: {backup_name}")
    
    def list_backups(self):
        """List all available backups"""
        backups = []
        for item in self.backup_dir.iterdir():
            if item.is_dir():
                manifest_path = item / "manifest.json"
                if manifest_path.exists():
                    with open(manifest_path) as f:
                        manifest = json.load(f)
                    backups.append(manifest)
        
        return sorted(backups, key=lambda x: x['timestamp'], reverse=True)
    
    def cleanup_old_backups(self, keep_days: int = 30):
        """Remove backups older than specified days"""
        cutoff = datetime.now().timestamp() - (keep_days * 24 * 60 * 60)
        
        removed = 0
        for item in self.backup_dir.iterdir():
            if item.is_dir():
                if item.stat().st_mtime < cutoff:
                    shutil.rmtree(item)
                    removed += 1
        
        print(f"✅ Removed {removed} old backup(s)")
        return removed

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Backup and restore email system')
    parser.add_argument('action', choices=['backup', 'restore', 'list', 'cleanup'],
                       help='Action to perform')
    parser.add_argument('--name', help='Backup name (for backup/restore)')
    parser.add_argument('--keep-days', type=int, default=30, help='Days to keep backups (for cleanup)')
    
    args = parser.parse_args()
    
    backup_system = BackupSystem()
    
    if args.action == 'backup':
        backup_system.create_backup(args.name)
    elif args.action == 'restore':
        if not args.name:
            print("❌ Error: --name required for restore")
            sys.exit(1)
        backup_system.restore_backup(args.name)
    elif args.action == 'list':
        backups = backup_system.list_backups()
        print(f"\n📦 Available Backups ({len(backups)}):\n")
        for backup in backups:
            print(f"  {backup['backup_name']} - {backup['timestamp']}")
    elif args.action == 'cleanup':
        backup_system.cleanup_old_backups(args.keep_days)


