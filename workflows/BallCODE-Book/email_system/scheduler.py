#!/usr/bin/env python3
"""
Scheduled Tasks System
Automated scheduled tasks for email system
"""

import schedule
import time
import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from backup import BackupSystem
    from monitor import SystemMonitor
    from analytics import EmailAnalytics
except ImportError:
    import backup
    import monitor
    import analytics
    BackupSystem = backup.BackupSystem
    SystemMonitor = monitor.SystemMonitor
    EmailAnalytics = analytics.EmailAnalytics

class TaskScheduler:
    """Scheduled task manager"""
    
    def __init__(self):
        self.backup_system = BackupSystem()
        self.monitor = SystemMonitor()
        self.analytics = EmailAnalytics()
    
    def daily_backup(self):
        """Daily backup task"""
        print(f"[{datetime.now()}] Running daily backup...")
        self.backup_system.create_backup()
        print(f"[{datetime.now()}] Backup complete")
    
    def health_check(self):
        """Health check task"""
        print(f"[{datetime.now()}] Running health check...")
        self.monitor.run_checks()
        print(f"[{datetime.now()}] Health check complete")
    
    def cleanup_old_backups(self):
        """Cleanup old backups"""
        print(f"[{datetime.now()}] Cleaning up old backups...")
        self.backup_system.cleanup_old_backups(keep_days=30)
        print(f"[{datetime.now()}] Cleanup complete")
    
    def generate_daily_report(self):
        """Generate daily analytics report"""
        print(f"[{datetime.now()}] Generating daily report...")
        insights = self.analytics.get_insights()
        print(f"Daily insights: {insights.get('insights', [])}")
        print(f"[{datetime.now()}] Report complete")
    
    def setup_schedule(self):
        """Setup scheduled tasks"""
        # Daily backup at 2 AM
        schedule.every().day.at("02:00").do(self.daily_backup)
        
        # Health check every 6 hours
        schedule.every(6).hours.do(self.health_check)
        
        # Cleanup backups weekly (Sunday at 3 AM)
        schedule.every().sunday.at("03:00").do(self.cleanup_old_backups)
        
        # Daily report at 9 AM
        schedule.every().day.at("09:00").do(self.generate_daily_report)
        
        print("✅ Scheduled tasks configured:")
        print("   - Daily backup: 2:00 AM")
        print("   - Health check: Every 6 hours")
        print("   - Backup cleanup: Sunday 3:00 AM")
        print("   - Daily report: 9:00 AM")
    
    def run(self):
        """Run scheduler"""
        self.setup_schedule()
        
        print("\n🔄 Task scheduler running...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n🛑 Scheduler stopped")

if __name__ == '__main__':
    scheduler = TaskScheduler()
    scheduler.run()



