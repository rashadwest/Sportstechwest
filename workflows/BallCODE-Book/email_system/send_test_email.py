#!/usr/bin/env python3
"""
Send Test Email with Signature
Automated test email with BallCODE signature
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

# Plain text version
plain_text = email_body + """

R.L West
CEO
BallCODE

🌐 ballcode.co
"""

if __name__ == '__main__':
    print("📧 Sending test email with signature...")
    print("To: rashadlwest@gmail.com")
    print()
    
    sender = EmailSender(smtp_host='localhost', smtp_port=2525)
    
    success = sender.send(
        to_address='rashadlwest@gmail.com',
        subject='Test Email from BallCODE Email System',
        body=plain_text,
        from_address='noreply@ballcode.co',
        html_body=full_html
    )
    
    if success:
        print("✅ Test email sent successfully!")
        print("📧 Check your inbox at rashadlwest@gmail.com")
    else:
        print("❌ Failed to send email")
        print("💡 Make sure the email server is running: python3 main.py start")
        sys.exit(1)


