#!/usr/bin/env python3
"""
Send Email with External SMTP (if configured)
Automatically uses external SMTP if available, falls back to local
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sender import EmailSender

# Load signature
signature_html = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #1a3d5c;">
    <div style="margin-bottom: 4px;">
        <strong style="color: #1a3d5c; font-size: 16px;">R.L West</strong>
    </div>
    <div style="color: #666666; margin-bottom: 2px; font-size: 13px;">CEO</div>
    <div style="color: #1a3d5c; margin-bottom: 8px; font-size: 14px; font-weight: 600;">BallCODE</div>
    <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid #e0e0e0;">
        <div>
            <span style="color: #666666;">🌐</span> 
            <a href="https://ballcode.co" style="color: #1a3d5c; text-decoration: none;">ballcode.co</a>
        </div>
    </div>
</div>
"""

if __name__ == '__main__':
    import json
    from pathlib import Path
    
    # Check if external SMTP is configured
    config_file = Path(__file__).parent / "email_config.json"
    external_enabled = False
    
    if config_file.exists():
        with open(config_file) as f:
            config = json.load(f)
        external_enabled = config.get("smtp_external", {}).get("enabled", False)
    
    if external_enabled:
        print("📧 Sending email via external SMTP...")
        # Sender will automatically use external SMTP from config
        sender = EmailSender()
    else:
        print("📧 Sending email via local SMTP (external not configured)...")
        print("💡 To enable external delivery, run: python3 auto_setup_external_smtp.py")
        sender = EmailSender(smtp_host='localhost', smtp_port=2525)
    
    # Email content
    email_body = """
Hello!

This is a test email from the BallCODE automated email system.

The system is working perfectly and includes:
- Automated email sending
- Professional signature
- Sales pipeline integration
- Slack notifications (if configured)
- Apollo enrichment (if configured)

Everything is set up and ready to go!

Best regards,
BallCODE Email System
"""
    
    # Combine body and signature
    full_html = f"""
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
{email_body}
<br><br>
{signature_html}
</div>
"""
    
    plain_text = email_body + """

R.L West
CEO
BallCODE

🌐 ballcode.co
"""
    
    print("To: rashadlwest@gmail.com")
    print()
    
    success = sender.send(
        to_address='rashadlwest@gmail.com',
        subject='Test Email from BallCODE Email System',
        body=plain_text,
        from_address='noreply@ballcode.co',
        html_body=full_html
    )
    
    if success:
        print("✅ Email sent successfully!")
        if external_enabled:
            print("📧 Email delivered via external SMTP - check your inbox!")
        else:
            print("📧 Email stored locally (external SMTP not configured)")
            print("💡 To enable external delivery, configure SMTP credentials")
    else:
        print("❌ Failed to send email")
        sys.exit(1)



