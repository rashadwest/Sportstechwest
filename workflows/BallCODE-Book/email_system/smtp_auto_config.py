#!/usr/bin/env python3
"""
Automated SMTP Configuration
Finds and configures best free SMTP service automatically
"""

import json
import requests
from pathlib import Path
from typing import Dict, Optional

class SMTPAutoConfig:
    """Automatically configure external SMTP delivery"""
    
    def __init__(self, config_file: str = "email_config.json"):
        self.config_file = Path(__file__).parent / config_file
        self.smtp_options = []
    
    def research_free_smtp_services(self):
        """Research and rank free SMTP services"""
        services = [
            {
                "name": "Gmail SMTP",
                "host": "smtp.gmail.com",
                "port": 587,
                "tls": True,
                "free": True,
                "limit": "Unlimited (with Gmail account)",
                "setup": "Requires Gmail app password",
                "priority": 1
            },
            {
                "name": "SendGrid",
                "host": "smtp.sendgrid.net",
                "port": 587,
                "tls": True,
                "free": True,
                "limit": "100 emails/day free",
                "setup": "Requires API key",
                "priority": 2
            },
            {
                "name": "Mailgun",
                "host": "smtp.mailgun.org",
                "port": 587,
                "tls": True,
                "free": True,
                "limit": "5,000 emails/month free",
                "setup": "Requires API key",
                "priority": 3
            },
            {
                "name": "Amazon SES",
                "host": "email-smtp.us-east-1.amazonaws.com",
                "port": 587,
                "tls": True,
                "free": True,
                "limit": "62,000 emails/month free",
                "setup": "Requires AWS credentials",
                "priority": 4
            }
        ]
        
        return sorted(services, key=lambda x: x['priority'])
    
    def detect_available_service(self) -> Optional[Dict]:
        """Detect which SMTP service is available (check environment variables)"""
        import os
        
        # Check for Gmail
        if os.getenv('GMAIL_APP_PASSWORD'):
            return {
                "name": "Gmail SMTP",
                "host": "smtp.gmail.com",
                "port": 587,
                "tls": True,
                "username": os.getenv('GMAIL_USERNAME', ''),
                "password": os.getenv('GMAIL_APP_PASSWORD'),
                "from": os.getenv('GMAIL_USERNAME', 'noreply@ballcode.co')
            }
        
        # Check for SendGrid
        if os.getenv('SENDGRID_API_KEY'):
            return {
                "name": "SendGrid",
                "host": "smtp.sendgrid.net",
                "port": 587,
                "tls": True,
                "username": "apikey",
                "password": os.getenv('SENDGRID_API_KEY'),
                "from": os.getenv('SENDGRID_FROM_EMAIL', 'noreply@ballcode.co')
            }
        
        # Check for Mailgun
        if os.getenv('MAILGUN_API_KEY'):
            return {
                "name": "Mailgun",
                "host": "smtp.mailgun.org",
                "port": 587,
                "tls": True,
                "username": os.getenv('MAILGUN_SMTP_USERNAME', ''),
                "password": os.getenv('MAILGUN_API_KEY'),
                "from": os.getenv('MAILGUN_FROM_EMAIL', 'noreply@ballcode.co')
            }
        
        return None
    
    def configure_smtp(self, service_config: Dict):
        """Configure SMTP in email_config.json"""
        if not self.config_file.exists():
            config = {}
        else:
            with open(self.config_file) as f:
                config = json.load(f)
        
        config.setdefault("smtp_external", {})
        config["smtp_external"].update({
            "enabled": True,
            "service": service_config["name"],
            "host": service_config["host"],
            "port": service_config["port"],
            "use_tls": service_config.get("tls", True),
            "username": service_config.get("username", ""),
            "password": service_config.get("password", ""),
            "from_address": service_config.get("from", "noreply@ballcode.co")
        })
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configured {service_config['name']} SMTP")
        return config
    
    def test_smtp_connection(self, service_config: Dict) -> bool:
        """Test SMTP connection"""
        try:
            import smtplib
            
            server = smtplib.SMTP(service_config["host"], service_config["port"])
            if service_config.get("tls"):
                server.starttls()
            
            if service_config.get("username") and service_config.get("password"):
                server.login(service_config["username"], service_config["password"])
            
            server.quit()
            return True
        except Exception as e:
            print(f"⚠️  SMTP test failed: {e}")
            return False
    
    def auto_configure(self):
        """Automatically configure best available SMTP service"""
        print("🔍 Auto-configuring external SMTP delivery...\n")
        
        # Check for environment variables first
        detected = self.detect_available_service()
        
        if detected:
            print(f"✅ Detected {detected['name']} credentials in environment")
            self.configure_smtp(detected)
            
            if self.test_smtp_connection(detected):
                print("✅ SMTP connection test passed!")
                return True
            else:
                print("⚠️  SMTP connection test failed")
                return False
        
        # No credentials found - show options
        services = self.research_free_smtp_services()
        
        print("📋 Available Free SMTP Services:\n")
        for i, service in enumerate(services, 1):
            print(f"{i}. {service['name']}")
            print(f"   Host: {service['host']}:{service['port']}")
            print(f"   Limit: {service['limit']}")
            print(f"   Setup: {service['setup']}")
            print()
        
        print("💡 To enable external delivery, set environment variables:")
        print("   Gmail: GMAIL_USERNAME, GMAIL_APP_PASSWORD")
        print("   SendGrid: SENDGRID_API_KEY, SENDGRID_FROM_EMAIL")
        print("   Mailgun: MAILGUN_API_KEY, MAILGUN_SMTP_USERNAME, MAILGUN_FROM_EMAIL")
        print()
        print("⏭️  External SMTP not configured - using local only")
        return False

if __name__ == '__main__':
    configurator = SMTPAutoConfig()
    configurator.auto_configure()


