#!/usr/bin/env python3
"""
Automated Email System Setup
Completes entire setup with minimal user input (only credentials when needed)
"""

import os
import sys
import subprocess
import json
from pathlib import Path

class AutomatedEmailSetup:
    """Automated setup for email system with minimal prompts"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.config_file = self.base_dir / "email_config.json"
        self.setup_complete = False
    
    def check_dependencies(self):
        """Check and install dependencies automatically"""
        print("🔍 Checking dependencies...")
        
        try:
            import aiosmtpd
            import click
            print("✅ Dependencies already installed")
            return True
        except ImportError:
            print("📦 Installing dependencies...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "aiosmtpd", "click"])
                print("✅ Dependencies installed")
                return True
            except subprocess.CalledProcessError:
                print("❌ Failed to install dependencies")
                return False
    
    def create_config(self):
        """Create configuration file with defaults"""
        config = {
            "smtp": {
                "host": "localhost",
                "port": 2525
            },
            "slack": {
                "webhook_url": "",  # Will prompt if needed
                "enabled": False
            },
            "apollo": {
                "api_key": "",  # Will prompt if needed
                "enabled": False
            },
            "sales_pipeline": {
                "enabled": True,
                "auto_categorize": True
            }
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configuration created: {self.config_file}")
        return config
    
    def setup_slack(self):
        """Setup Slack integration (only prompts for webhook URL)"""
        print("\n📱 Slack Integration Setup")
        print("(Press Enter to skip - you can add this later)")
        
        try:
            webhook_url = input("Slack Webhook URL (optional): ").strip()
        except (EOFError, KeyboardInterrupt):
            # Non-interactive mode - skip
            print("⏭️  Slack integration skipped (can add later in email_config.json)")
            return False
        
        if webhook_url:
            config = json.load(open(self.config_file))
            config["slack"]["webhook_url"] = webhook_url
            config["slack"]["enabled"] = True
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            print("✅ Slack integration configured")
            return True
        else:
            print("⏭️  Slack integration skipped (can add later)")
            return False
    
    def setup_apollo(self):
        """Setup Apollo integration (only prompts for API key)"""
        print("\n🔍 Apollo Integration Setup")
        print("(Press Enter to skip - you can add this later)")
        
        try:
            api_key = input("Apollo API Key (optional): ").strip()
        except (EOFError, KeyboardInterrupt):
            # Non-interactive mode - skip
            print("⏭️  Apollo integration skipped (can add later in email_config.json)")
            return False
        
        if api_key:
            config = json.load(open(self.config_file))
            config["apollo"]["api_key"] = api_key
            config["apollo"]["enabled"] = True
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            print("✅ Apollo integration configured")
            return True
        else:
            print("⏭️  Apollo integration skipped (can add later)")
            return False
    
    def test_system(self):
        """Test the email system"""
        print("\n🧪 Testing email system...")
        
        try:
            # Check if files exist
            required_files = ['server.py', 'storage.py', 'sender.py', 'cli.py']
            for file in required_files:
                file_path = self.base_dir / file
                if not file_path.exists():
                    print(f"❌ Missing file: {file}")
                    return False
            
            # Test database creation (simple test)
            import sqlite3
            test_db = self.base_dir / "test_emails.db"
            conn = sqlite3.connect(str(test_db))
            conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
            conn.close()
            test_db.unlink()  # Clean up
            
            print("✅ Email system files verified")
            print("✅ Database system working")
            print("✅ Email system ready")
            return True
                
        except Exception as e:
            print(f"❌ Test failed: {e}")
            return False
    
    def run(self):
        """Run complete automated setup"""
        print("=" * 60)
        print("🚀 Automated Email System Setup")
        print("=" * 60)
        print()
        
        # Step 1: Check dependencies
        if not self.check_dependencies():
            print("\n❌ Setup failed: Dependencies not installed")
            return False
        
        # Step 2: Create config
        self.create_config()
        
        # Step 3: Setup Slack (optional - only prompts for webhook)
        self.setup_slack()
        
        # Step 4: Setup Apollo (optional - only prompts for API key)
        self.setup_apollo()
        
        # Step 5: Test system
        if not self.test_system():
            print("\n⚠️  Setup completed but tests failed")
            return False
        
        print("\n" + "=" * 60)
        print("✅ Automated Setup Complete!")
        print("=" * 60)
        print("\n📧 To start the email server:")
        print("   python3 main.py start")
        print("\n📧 To send an email:")
        print("   python3 main.py send --to EMAIL --subject 'SUBJECT' --body 'BODY'")
        print("\n📧 To check emails:")
        print("   python3 main.py list")
        print()
        
        self.setup_complete = True
        return True

if __name__ == '__main__':
    setup = AutomatedEmailSetup()
    success = setup.run()
    sys.exit(0 if success else 1)

