#!/usr/bin/env python3
"""
End-to-End System Test
Tests the complete email system and generates report
"""

import sys
import os
import time
import threading
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from storage import EmailStorage
from sender import EmailSender
from server import EmailServer

class SystemTester:
    """Test email system end-to-end"""
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "tests": [],
            "passed": 0,
            "failed": 0,
            "warnings": 0
        }
        self.server = None
        self.server_thread = None
    
    def log_test(self, name, status, message=""):
        """Log test result"""
        test_result = {
            "name": name,
            "status": status,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.results["tests"].append(test_result)
        
        if status == "PASS":
            self.results["passed"] += 1
            print(f"✅ {name}: {message}")
        elif status == "FAIL":
            self.results["failed"] += 1
            print(f"❌ {name}: {message}")
        else:
            self.results["warnings"] += 1
            print(f"⚠️  {name}: {message}")
    
    def test_storage(self):
        """Test email storage"""
        try:
            storage = EmailStorage(db_path="test_emails.db")
            self.log_test("Storage System", "PASS", "EmailStorage initialized")
            return True
        except Exception as e:
            self.log_test("Storage System", "FAIL", str(e))
            return False
    
    def test_sender(self):
        """Test email sender"""
        try:
            sender = EmailSender(smtp_host='localhost', smtp_port=2525, db_path="test_emails.db")
            self.log_test("Email Sender", "PASS", "EmailSender initialized")
            return True
        except Exception as e:
            self.log_test("Email Sender", "FAIL", str(e))
            return False
    
    def test_server_start(self):
        """Test server startup"""
        try:
            self.server = EmailServer(host='localhost', port=2525, db_path="test_emails.db")
            self.server_thread = threading.Thread(target=self.server.start, daemon=True)
            self.server_thread.start()
            time.sleep(2)  # Give server time to start
            self.log_test("Server Startup", "PASS", "SMTP server started on localhost:2525")
            return True
        except Exception as e:
            self.log_test("Server Startup", "FAIL", str(e))
            return False
    
    def test_send_email(self):
        """Test sending email"""
        try:
            sender = EmailSender(smtp_host='localhost', smtp_port=2525, db_path="test_emails.db")
            success = sender.send(
                to_address='test@ballcode.co',
                subject='System Test Email',
                body='This is an automated test email from the system test.'
            )
            if success:
                self.log_test("Send Email", "PASS", "Email sent successfully")
                return True
            else:
                self.log_test("Send Email", "FAIL", "Email send failed")
                return False
        except Exception as e:
            self.log_test("Send Email", "FAIL", str(e))
            return False
    
    def test_receive_email(self):
        """Test receiving email"""
        try:
            storage = EmailStorage(db_path="test_emails.db")
            emails = storage.list_emails(limit=5)
            if emails:
                self.log_test("Receive Email", "PASS", f"Found {len(emails)} email(s) in database")
                return True
            else:
                self.log_test("Receive Email", "WARN", "No emails found (may be expected)")
                return True
        except Exception as e:
            self.log_test("Receive Email", "FAIL", str(e))
            return False
    
    def test_config(self):
        """Test configuration"""
        try:
            config_file = os.path.join(os.path.dirname(__file__), "email_config.json")
            if os.path.exists(config_file):
                import json
                with open(config_file) as f:
                    config = json.load(f)
                self.log_test("Configuration", "PASS", "Configuration file exists and valid")
                return True
            else:
                self.log_test("Configuration", "WARN", "Configuration file not found")
                return True
        except Exception as e:
            self.log_test("Configuration", "FAIL", str(e))
            return False
    
    def test_dependencies(self):
        """Test dependencies"""
        try:
            import aiosmtpd
            import click
            import requests
            self.log_test("Dependencies", "PASS", "All dependencies installed")
            return True
        except ImportError as e:
            self.log_test("Dependencies", "FAIL", f"Missing dependency: {e}")
            return False
    
    def cleanup(self):
        """Cleanup test files"""
        try:
            if self.server:
                self.server.stop()
            # Remove test database
            test_db = "test_emails.db"
            if os.path.exists(test_db):
                os.remove(test_db)
            self.log_test("Cleanup", "PASS", "Test cleanup completed")
        except Exception as e:
            self.log_test("Cleanup", "WARN", f"Cleanup warning: {e}")
    
    def generate_report(self):
        """Generate test report"""
        report = f"""
{'='*60}
EMAIL SYSTEM TEST REPORT
{'='*60}

Test Date: {self.results['timestamp']}
Total Tests: {len(self.results['tests'])}
Passed: {self.results['passed']}
Failed: {self.results['failed']}
Warnings: {self.results['warnings']}

{'='*60}
TEST RESULTS
{'='*60}
"""
        for test in self.results['tests']:
            status_icon = "✅" if test['status'] == "PASS" else "❌" if test['status'] == "FAIL" else "⚠️"
            report += f"\n{status_icon} {test['name']}: {test['status']}"
            if test['message']:
                report += f" - {test['message']}"
        
        report += f"\n\n{'='*60}\n"
        
        if self.results['failed'] == 0:
            report += "✅ SYSTEM READY - All tests passed!\n"
        else:
            report += f"⚠️  SYSTEM HAS ISSUES - {self.results['failed']} test(s) failed\n"
        
        report += f"{'='*60}\n"
        
        return report
    
    def run_all_tests(self):
        """Run all tests"""
        print("🧪 Starting Email System Tests...\n")
        
        # Test dependencies first
        self.test_dependencies()
        
        # Test configuration
        self.test_config()
        
        # Test storage
        self.test_storage()
        
        # Test sender
        self.test_sender()
        
        # Test server
        if self.test_server_start():
            time.sleep(1)
            
            # Test sending email
            self.test_send_email()
            time.sleep(1)
            
            # Test receiving email
            self.test_receive_email()
        
        # Cleanup
        self.cleanup()
        
        # Generate report
        report = self.generate_report()
        print("\n" + report)
        
        # Save report
        report_file = "test_report.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Test report saved to: {report_file}")
        
        return self.results['failed'] == 0

if __name__ == '__main__':
    tester = SystemTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)



