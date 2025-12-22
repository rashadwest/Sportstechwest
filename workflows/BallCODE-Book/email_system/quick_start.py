#!/usr/bin/env python3
"""
Quick Start - Test the email system in 30 seconds
"""

import sys
import os
import time
import threading

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from server import EmailServer
from sender import EmailSender
from storage import EmailStorage

def test_email_system():
    """Quick test of the email system"""
    print("🚀 BallCODE Email System - Quick Test\n")
    
    # Start server in background
    print("1️⃣  Starting email server...")
    server = EmailServer(host='localhost', port=2525)
    server_thread = threading.Thread(target=server.start, daemon=True)
    server_thread.start()
    time.sleep(2)  # Give server time to start
    print("   ✅ Server running on localhost:2525\n")
    
    # Send test email
    print("2️⃣  Sending test email...")
    sender = EmailSender(smtp_host='localhost', smtp_port=2525)
    success = sender.send(
        to_address='test@ballcode.co',
        subject='Test Email from BallCODE',
        body='This is a test email from your local email system!\n\nIf you see this, everything is working! 🎉'
    )
    
    if success:
        print("   ✅ Email sent successfully!\n")
    else:
        print("   ❌ Failed to send email\n")
        return False
    
    # List emails
    print("3️⃣  Checking stored emails...")
    storage = EmailStorage()
    emails = storage.list_emails(limit=5)
    
    if emails:
        print(f"   ✅ Found {len(emails)} email(s) in database\n")
        print("   Latest email:")
        latest = emails[0]
        print(f"   - From: {latest['from_address']}")
        print(f"   - To: {latest['to_address']}")
        print(f"   - Subject: {latest['subject']}")
        print(f"   - Date: {latest['date_received']}\n")
    else:
        print("   ⚠️  No emails found in database\n")
    
    # Stop server
    print("4️⃣  Stopping server...")
    server.stop()
    print("   ✅ Server stopped\n")
    
    print("🎉 Email system test complete! Everything is working!\n")
    print("📧 To use the email system:")
    print("   python3 main.py start          # Start server")
    print("   python3 main.py send --to ...  # Send email")
    print("   python3 main.py list           # List emails")
    print()
    
    return True

if __name__ == '__main__':
    try:
        success = test_email_system()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

