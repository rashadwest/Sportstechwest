#!/usr/bin/env python3
"""
Complete Automation - Robot Does Everything Possible
Only stops when human intervention is absolutely required
"""

import sys
import os
import json
import subprocess
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class CompleteAutomation:
    """Complete automation - robot does everything possible"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.blockers = []
        self.completed = []
    
    def log_completed(self, task, details=""):
        """Log completed task"""
        self.completed.append({"task": task, "details": details})
        print(f"✅ {task}")
        if details:
            print(f"   {details}")
    
    def log_blocker(self, blocker, reason, human_action_needed):
        """Log blocker requiring human intervention"""
        self.blockers.append({
            "blocker": blocker,
            "reason": reason,
            "human_action": human_action_needed
        })
        print(f"⚠️  BLOCKER: {blocker}")
        print(f"   Reason: {reason}")
        print(f"   Human Action: {human_action_needed}")
    
    def install_dependencies(self):
        """Install all dependencies"""
        try:
            print("📦 Installing dependencies...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "aiosmtpd", "click", "requests", "flask", "flask-cors", "schedule"
            ])
            self.log_completed("Dependencies installed")
            return True
        except Exception as e:
            self.log_blocker("Dependency Installation", str(e), "Check Python/pip installation")
            return False
    
    def verify_system_files(self):
        """Verify all system files exist"""
        required_files = [
            "main.py", "cli.py", "server.py", "storage.py", "sender.py",
            "slack_notifier.py", "apollo_integration.py", "sales_pipeline.py",
            "test_system.py", "monitor.py", "backup.py", "api_server.py",
            "dashboard.py", "scheduler.py", "filters.py", "analytics.py"
        ]
        
        missing = []
        for file in required_files:
            if not (self.base_dir / file).exists():
                missing.append(file)
        
        if missing:
            self.log_blocker("Missing System Files", f"Files not found: {missing}", "Check file creation")
            return False
        
        self.log_completed("All system files verified", f"{len(required_files)} files")
        return True
    
    def test_system(self):
        """Test email system"""
        try:
            print("\n🧪 Testing system...")
            result = subprocess.run(
                [sys.executable, "test_system.py"],
                cwd=str(self.base_dir),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.log_completed("System tests passed")
                return True
            else:
                self.log_blocker("System Tests", "Tests failed", "Review test output")
                return False
        except Exception as e:
            self.log_blocker("System Tests", str(e), "Check system configuration")
            return False
    
    def check_external_smtp(self):
        """Check for external SMTP credentials"""
        env_vars = {
            "Gmail": ["GMAIL_USERNAME", "GMAIL_APP_PASSWORD"],
            "SendGrid": ["SENDGRID_API_KEY", "SENDGRID_FROM_EMAIL"],
            "Mailgun": ["MAILGUN_API_KEY", "MAILGUN_SMTP_USERNAME"]
        }
        
        found = {}
        for service, vars_needed in env_vars.items():
            if all(os.getenv(var) for var in vars_needed):
                found[service] = True
        
        if found:
            self.log_completed("External SMTP credentials detected", f"Services: {list(found.keys())}")
            # Auto-configure
            try:
                from smtp_auto_config import SMTPAutoConfig
                configurator = SMTPAutoConfig()
                if configurator.auto_configure():
                    self.log_completed("External SMTP configured automatically")
                    return True
            except Exception as e:
                self.log_blocker("SMTP Auto-Configuration", str(e), "Check SMTP credentials")
        else:
            self.log_blocker(
                "External SMTP Delivery",
                "No SMTP credentials in environment",
                "Set environment variables: GMAIL_USERNAME, GMAIL_APP_PASSWORD (or SendGrid/Mailgun)"
            )
        
        return False
    
    def check_slack_integration(self):
        """Check Slack integration"""
        config_file = self.base_dir / "email_config.json"
        if config_file.exists():
            with open(config_file) as f:
                config = json.load(f)
            
            slack_config = config.get("slack", {})
            if slack_config.get("enabled") and slack_config.get("webhook_url"):
                self.log_completed("Slack integration configured")
                return True
        
        self.log_blocker(
            "Slack Notifications",
            "No Slack webhook URL configured",
            "Optional: Get Slack webhook URL and add to email_config.json"
        )
        return False
    
    def check_apollo_integration(self):
        """Check Apollo integration"""
        config_file = self.base_dir / "email_config.json"
        if config_file.exists():
            with open(config_file) as f:
                config = json.load(f)
            
            apollo_config = config.get("apollo", {})
            if apollo_config.get("enabled") and apollo_config.get("api_key"):
                self.log_completed("Apollo integration configured")
                return True
        
        self.log_blocker(
            "Apollo Lead Enrichment",
            "No Apollo API key configured",
            "Optional: Get Apollo API key and add to email_config.json"
        )
        return False
    
    def create_startup_scripts(self):
        """Create automated startup scripts"""
        try:
            # Create systemd service file (for Linux)
            systemd_service = f"""[Unit]
Description=BallCODE Email System
After=network.target

[Service]
Type=simple
User={os.getenv('USER', 'user')}
WorkingDirectory={self.base_dir}
ExecStart={sys.executable} {self.base_dir}/main.py start
Restart=always

[Install]
WantedBy=multi-user.target
"""
            (self.base_dir / "email-system.service").write_text(systemd_service)
            
            # Create launchd plist (for macOS)
            launchd_plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.ballcode.email</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable}</string>
        <string>{self.base_dir}/main.py</string>
        <string>start</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>{self.base_dir}</string>
</dict>
</plist>
"""
            (self.base_dir / "com.ballcode.email.plist").write_text(launchd_plist)
            
            self.log_completed("Startup scripts created", "systemd service + launchd plist")
            return True
        except Exception as e:
            self.log_blocker("Startup Scripts", str(e), "Check file permissions")
            return False
    
    def generate_documentation(self):
        """Generate complete documentation"""
        try:
            docs = {
                "AUTOMATION-STATUS.md": self.generate_automation_status(),
                "BLOCKERS-REPORT.md": self.generate_blockers_report(),
                "QUICK-START.md": self.generate_quick_start()
            }
            
            for filename, content in docs.items():
                (self.base_dir / filename).write_text(content)
            
            self.log_completed("Documentation generated", f"{len(docs)} files")
            return True
        except Exception as e:
            self.log_blocker("Documentation", str(e), "Check file permissions")
            return False
    
    def generate_automation_status(self):
        """Generate automation status report"""
        from datetime import datetime
        newline = "\n"
        
        completed_list = newline.join(f"- {item['task']}" + (f": {item['details']}" if item['details'] else "") for item in self.completed)
        blockers_list = newline.join(f"### {blocker['blocker']}\n- **Reason:** {blocker['reason']}\n- **Human Action:** {blocker['human_action']}" for blocker in self.blockers)
        
        automation_pct = 100 * len(self.completed) / (len(self.completed) + len(self.blockers)) if (len(self.completed) + len(self.blockers)) > 0 else 100
        
        return f"""# Automation Status Report

**Generated:** {datetime.now().isoformat()}

## ✅ Completed by Robot

{completed_list}

## ⚠️ Blockers Requiring Human Intervention

{blockers_list}

## 📊 Summary

- **Completed:** {len(self.completed)} tasks
- **Blockers:** {len(self.blockers)} items need human
- **Automation:** {automation_pct:.1f}% automated
"""
    
    def generate_blockers_report(self):
        """Generate blockers report"""
        from datetime import datetime
        newline = "\n"
        
        blockers_content = newline.join(f"""## {i+1}. {blocker['blocker']}

**Reason:** {blocker['reason']}

**Human Action Required:**
{blocker['human_action']}

**Priority:** {'HIGH' if 'SMTP' in blocker['blocker'] or 'External' in blocker['blocker'] else 'MEDIUM' if 'Slack' in blocker['blocker'] or 'Apollo' in blocker['blocker'] else 'LOW'}

---
""" for i, blocker in enumerate(self.blockers))
        
        return f"""# Blockers Report - Human Intervention Required

**Generated:** {datetime.now().isoformat()}

## ⚠️ Blockers Requiring Human Action

{blockers_content}

## 📋 Action Items for Human

1. **Review blockers above**
2. **Complete required actions**
3. **Re-run automation:** `python3 complete_automation.py`

## ✅ After Human Actions

Robot will automatically:
- Detect new credentials
- Configure systems
- Test connections
- Enable features
"""
    
    def generate_quick_start(self):
        """Generate quick start guide"""
        newline = "\n"
        completed_list = newline.join(f"- ✅ {item['task']}" for item in self.completed)
        blockers_list = newline.join(f"- ⚠️ {blocker['blocker']}: {blocker['human_action']}" for blocker in self.blockers)
        
        return f"""# Quick Start Guide

## ✅ What Robot Has Done

{completed_list}

## ⚠️ What Human Must Do

{blockers_list}

## 🚀 Start Using

```bash
cd email_system
python3 main.py start
```

## 📧 Send Email

```bash
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"
```
"""
    
    def run(self):
        """Run complete automation"""
        print("=" * 60)
        print("🤖 Complete Automation - Robot Working...")
        print("=" * 60)
        print()
        
        # Install dependencies
        self.install_dependencies()
        
        # Verify files
        self.verify_system_files()
        
        # Test system
        self.test_system()
        
        # Check external SMTP
        self.check_external_smtp()
        
        # Check integrations
        self.check_slack_integration()
        self.check_apollo_integration()
        
        # Create startup scripts
        self.create_startup_scripts()
        
        # Generate documentation
        self.generate_documentation()
        
        # Final report
        print("\n" + "=" * 60)
        print("📊 AUTOMATION COMPLETE")
        print("=" * 60)
        print(f"\n✅ Completed: {len(self.completed)} tasks")
        print(f"⚠️  Blockers: {len(self.blockers)} items need human")
        print()
        
        if self.blockers:
            print("⚠️  BLOCKERS REQUIRING HUMAN INTERVENTION:\n")
            for i, blocker in enumerate(self.blockers, 1):
                print(f"{i}. {blocker['blocker']}")
                print(f"   Action: {blocker['human_action']}")
                print()
        
        print("📄 Reports generated:")
        print("   - AUTOMATION-STATUS.md")
        print("   - BLOCKERS-REPORT.md")
        print("   - QUICK-START.md")
        print()
        
        return len(self.blockers) == 0

if __name__ == '__main__':
    automation = CompleteAutomation()
    success = automation.run()
    sys.exit(0 if success else 1)

