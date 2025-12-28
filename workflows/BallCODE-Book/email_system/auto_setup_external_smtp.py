#!/usr/bin/env python3
"""
Automated External SMTP Setup
Automatically configures external SMTP delivery with minimal human input
"""

import sys
import os
import json
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from smtp_auto_config import SMTPAutoConfig

class ExternalSMTPAutoSetup:
    """Automated external SMTP setup"""
    
    def __init__(self):
        self.config_file = Path(__file__).parent / "email_config.json"
        self.configurator = SMTPAutoConfig()
    
    def check_environment_variables(self):
        """Check for SMTP credentials in environment"""
        env_vars = {
            "Gmail": ["GMAIL_USERNAME", "GMAIL_APP_PASSWORD"],
            "SendGrid": ["SENDGRID_API_KEY", "SENDGRID_FROM_EMAIL"],
            "Mailgun": ["MAILGUN_API_KEY", "MAILGUN_SMTP_USERNAME", "MAILGUN_FROM_EMAIL"]
        }
        
        found = {}
        for service, vars_needed in env_vars.items():
            if all(os.getenv(var) for var in vars_needed):
                found[service] = {var: os.getenv(var) for var in vars_needed}
        
        return found
    
    def create_setup_instructions(self):
        """Create automated setup instructions"""
        instructions = {
            "gmail": {
                "steps": [
                    "1. Go to Google Account settings",
                    "2. Enable 2-Step Verification",
                    "3. Generate App Password",
                    "4. Set environment variables:",
                    "   export GMAIL_USERNAME='your-email@gmail.com'",
                    "   export GMAIL_APP_PASSWORD='your-app-password'",
                    "5. Run: python3 auto_setup_external_smtp.py"
                ],
                "automated": False
            },
            "sendgrid": {
                "steps": [
                    "1. Sign up at sendgrid.com (free)",
                    "2. Create API key",
                    "3. Set environment variables:",
                    "   export SENDGRID_API_KEY='your-api-key'",
                    "   export SENDGRID_FROM_EMAIL='noreply@ballcode.co'",
                    "4. Run: python3 auto_setup_external_smtp.py"
                ],
                "automated": False
            },
            "mailgun": {
                "steps": [
                    "1. Sign up at mailgun.com (free)",
                    "2. Get SMTP credentials",
                    "3. Set environment variables:",
                    "   export MAILGUN_API_KEY='your-api-key'",
                    "   export MAILGUN_SMTP_USERNAME='your-smtp-username'",
                    "   export MAILGUN_FROM_EMAIL='noreply@ballcode.co'",
                    "4. Run: python3 auto_setup_external_smtp.py"
                ],
                "automated": False
            }
        }
        
        return instructions
    
    def run(self):
        """Run automated setup"""
        print("=" * 60)
        print("🤖 Automated External SMTP Setup")
        print("=" * 60)
        print()
        
        # Check environment variables
        found_services = self.check_environment_variables()
        
        if found_services:
            print("✅ Found SMTP credentials in environment:\n")
            for service, creds in found_services.items():
                print(f"   {service}: Configured")
            print()
            
            # Auto-configure
            success = self.configurator.auto_configure()
            
            if success:
                print("\n✅ External SMTP configured automatically!")
                print("📧 Emails will now be delivered to external addresses")
                return True
        
        # No credentials found
        print("⚠️  No SMTP credentials found in environment variables")
        print()
        print("📋 To enable external email delivery, choose a service:\n")
        
        services = self.configurator.research_free_smtp_services()
        for i, service in enumerate(services[:3], 1):  # Show top 3
            print(f"{i}. {service['name']}")
            print(f"   {service['limit']}")
            print(f"   Setup: {service['setup']}")
            print()
        
        print("💡 Recommended: Gmail SMTP (unlimited, free)")
        print()
        print("📝 Setup Instructions saved to: SMTP-SETUP-INSTRUCTIONS.md")
        
        # Save instructions
        self.save_instructions()
        
        return False
    
    def save_instructions(self):
        """Save setup instructions to file"""
        instructions = self.create_setup_instructions()
        
        content = """# External SMTP Setup Instructions

## 🤖 Automated Setup (When Credentials Available)

**If you set environment variables, run:**
```bash
python3 auto_setup_external_smtp.py
```

The system will automatically detect and configure SMTP!

---

## 📋 Manual Setup Options

### Option 1: Gmail SMTP (Recommended - Unlimited, Free)

**Steps:**
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password (for "Mail")
4. Set environment variables:
   ```bash
   export GMAIL_USERNAME='your-email@gmail.com'
   export GMAIL_APP_PASSWORD='your-16-char-app-password'
   ```
5. Run: `python3 auto_setup_external_smtp.py`

**Result:** Unlimited emails, free, reliable

---

### Option 2: SendGrid (100 emails/day free)

**Steps:**
1. Sign up at sendgrid.com (free account)
2. Create API key in Settings → API Keys
3. Set environment variables:
   ```bash
   export SENDGRID_API_KEY='your-api-key'
   export SENDGRID_FROM_EMAIL='noreply@ballcode.co'
   ```
4. Run: `python3 auto_setup_external_smtp.py`

**Result:** 100 emails/day free

---

### Option 3: Mailgun (5,000 emails/month free)

**Steps:**
1. Sign up at mailgun.com (free account)
2. Get SMTP credentials from dashboard
3. Set environment variables:
   ```bash
   export MAILGUN_API_KEY='your-api-key'
   export MAILGUN_SMTP_USERNAME='your-smtp-username'
   export MAILGUN_FROM_EMAIL='noreply@ballcode.co'
   ```
4. Run: `python3 auto_setup_external_smtp.py`

**Result:** 5,000 emails/month free

---

## ✅ After Setup

Once configured, emails will automatically use external SMTP for delivery!

**Test:**
```bash
python3 send_test_email.py
```

---

**Robot will auto-configure when credentials are available!** 🤖
"""
        
        instructions_file = Path(__file__).parent / "SMTP-SETUP-INSTRUCTIONS.md"
        with open(instructions_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Instructions saved to: {instructions_file}")

if __name__ == '__main__':
    setup = ExternalSMTPAutoSetup()
    setup.run()



