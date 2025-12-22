#!/usr/bin/env python3
"""
Email System Monitor
Health checks and status monitoring
"""

import sys
import os
import json
import sqlite3
from datetime import datetime
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from storage import EmailStorage
    from sender import EmailSender
except ImportError:
    import storage
    import sender

class SystemMonitor:
    """Monitor email system health and status"""
    
    def __init__(self, config_file: str = "email_config.json"):
        self.config_file = Path(__file__).parent / config_file
        self.db_path = Path(__file__).parent / "emails.db"
        self.status = {
            "timestamp": datetime.now().isoformat(),
            "checks": [],
            "overall": "unknown"
        }
    
    def check_database(self):
        """Check database health"""
        try:
            if not self.db_path.exists():
                return {"status": "FAIL", "message": "Database file not found"}
            
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM emails")
            count = cursor.fetchone()[0]
            conn.close()
            
            return {"status": "PASS", "message": f"Database healthy ({count} emails)"}
        except Exception as e:
            return {"status": "FAIL", "message": str(e)}
    
    def check_config(self):
        """Check configuration"""
        try:
            if not self.config_file.exists():
                return {"status": "WARN", "message": "Configuration file not found"}
            
            with open(self.config_file) as f:
                config = json.load(f)
            
            return {"status": "PASS", "message": "Configuration valid"}
        except Exception as e:
            return {"status": "FAIL", "message": str(e)}
    
    def check_dependencies(self):
        """Check dependencies"""
        try:
            import aiosmtpd
            import click
            import requests
            return {"status": "PASS", "message": "All dependencies installed"}
        except ImportError as e:
            return {"status": "FAIL", "message": f"Missing: {e}"}
    
    def check_slack(self):
        """Check Slack integration"""
        try:
            if not self.config_file.exists():
                return {"status": "SKIP", "message": "Config not found"}
            
            with open(self.config_file) as f:
                config = json.load(f)
            
            slack_config = config.get("slack", {})
            if slack_config.get("enabled"):
                webhook = slack_config.get("webhook_url", "")
                if webhook:
                    return {"status": "PASS", "message": "Slack configured"}
                else:
                    return {"status": "WARN", "message": "Slack enabled but no webhook"}
            else:
                return {"status": "SKIP", "message": "Slack not enabled"}
        except Exception as e:
            return {"status": "FAIL", "message": str(e)}
    
    def check_apollo(self):
        """Check Apollo integration"""
        try:
            if not self.config_file.exists():
                return {"status": "SKIP", "message": "Config not found"}
            
            with open(self.config_file) as f:
                config = json.load(f)
            
            apollo_config = config.get("apollo", {})
            if apollo_config.get("enabled"):
                api_key = apollo_config.get("api_key", "")
                if api_key:
                    return {"status": "PASS", "message": "Apollo configured"}
                else:
                    return {"status": "WARN", "message": "Apollo enabled but no API key"}
            else:
                return {"status": "SKIP", "message": "Apollo not enabled"}
        except Exception as e:
            return {"status": "FAIL", "message": str(e)}
    
    def check_storage(self):
        """Check storage system"""
        try:
            storage = EmailStorage()
            emails = storage.list_emails(limit=1)
            return {"status": "PASS", "message": "Storage system working"}
        except Exception as e:
            return {"status": "FAIL", "message": str(e)}
    
    def get_statistics(self):
        """Get system statistics"""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            
            # Total emails
            cursor.execute("SELECT COUNT(*) FROM emails")
            total = cursor.fetchone()[0]
            
            # Unread emails
            cursor.execute("SELECT COUNT(*) FROM emails WHERE read = 0")
            unread = cursor.fetchone()[0]
            
            # By folder
            cursor.execute("SELECT folder, COUNT(*) FROM emails GROUP BY folder")
            folders = dict(cursor.fetchall())
            
            conn.close()
            
            return {
                "total_emails": total,
                "unread_emails": unread,
                "read_emails": total - unread,
                "folders": folders
            }
        except Exception as e:
            return {"error": str(e)}
    
    def run_checks(self):
        """Run all health checks"""
        print("🔍 Running System Health Checks...\n")
        
        checks = [
            ("Dependencies", self.check_dependencies),
            ("Configuration", self.check_config),
            ("Database", self.check_database),
            ("Storage System", self.check_storage),
            ("Slack Integration", self.check_slack),
            ("Apollo Integration", self.check_apollo)
        ]
        
        for name, check_func in checks:
            result = check_func()
            self.status["checks"].append({
                "name": name,
                "status": result["status"],
                "message": result["message"]
            })
            
            icon = {
                "PASS": "✅",
                "FAIL": "❌",
                "WARN": "⚠️",
                "SKIP": "⏭️"
            }.get(result["status"], "❓")
            
            print(f"{icon} {name}: {result['message']}")
        
        # Determine overall status
        fails = sum(1 for c in self.status["checks"] if c["status"] == "FAIL")
        if fails == 0:
            self.status["overall"] = "HEALTHY"
        else:
            self.status["overall"] = "ISSUES"
        
        # Get statistics
        stats = self.get_statistics()
        self.status["statistics"] = stats
        
        return self.status
    
    def generate_report(self):
        """Generate status report"""
        report = f"""
{'='*60}
EMAIL SYSTEM STATUS REPORT
{'='*60}

Timestamp: {self.status['timestamp']}
Overall Status: {self.status['overall']}

{'='*60}
HEALTH CHECKS
{'='*60}
"""
        for check in self.status["checks"]:
            icon = {
                "PASS": "✅",
                "FAIL": "❌",
                "WARN": "⚠️",
                "SKIP": "⏭️"
            }.get(check["status"], "❓")
            report += f"\n{icon} {check['name']}: {check['message']}"
        
        if "statistics" in self.status:
            stats = self.status["statistics"]
            report += f"""

{'='*60}
STATISTICS
{'='*60}
Total Emails: {stats.get('total_emails', 0)}
Unread: {stats.get('unread_emails', 0)}
Read: {stats.get('read_emails', 0)}

Folders:
"""
            for folder, count in stats.get('folders', {}).items():
                report += f"  {folder}: {count}\n"
        
        report += f"\n{'='*60}\n"
        
        return report

if __name__ == '__main__':
    monitor = SystemMonitor()
    status = monitor.run_checks()
    report = monitor.generate_report()
    print("\n" + report)
    
    # Save report
    report_file = "system_status.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"\n📄 Status report saved to: {report_file}")
    
    sys.exit(0 if status["overall"] == "HEALTHY" else 1)


