"""
SMTP Server
Local SMTP server using aiosmtpd to receive emails
"""

import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Message
from typing import Optional
try:
    from .storage import EmailStorage
except ImportError:
    from storage import EmailStorage


class EmailHandler(Message):
    """Custom email handler that stores emails"""
    
    def __init__(self, storage: EmailStorage):
        """
        Initialize email handler
        
        Args:
            storage: EmailStorage instance
        """
        super().__init__()
        self.storage = storage
    
    async def handle_message(self, message):
        """
        Handle received email message
        
        Args:
            message: Email message object
        """
        # Convert message to bytes
        raw_email = message.as_bytes()
        
        # Save to storage
        email_id = self.storage.save_email(raw_email)
        
        print(f"📧 Received email (ID: {email_id})")
        
        # Process for sales pipeline (if enabled)
        try:
            try:
                from .sales_pipeline import SalesPipeline
            except ImportError:
                from sales_pipeline import SalesPipeline
            pipeline = SalesPipeline()
            pipeline.process_new_email(email_id)
        except Exception as e:
            print(f"⚠️  Pipeline processing failed: {e}")
        
        # Notify Slack (if enabled)
        try:
            try:
                from .slack_notifier import SlackNotifier
            except ImportError:
                from slack_notifier import SlackNotifier
            notifier = SlackNotifier()
            email_data = self.storage.get_email(email_id)
            if email_data:
                notifier.notify_new_email(email_data)
        except Exception as e:
            print(f"⚠️  Slack notification failed: {e}")
        
        return email_id


class EmailServer:
    """Local SMTP server for receiving emails"""
    
    def __init__(self, host: str = 'localhost', port: int = 2525, 
                 db_path: str = "emails.db"):
        """
        Initialize email server
        
        Args:
            host: Host to bind server to
            port: Port to listen on (2525 to avoid root privileges)
            db_path: Path to email database
        """
        self.host = host
        self.port = port
        self.storage = EmailStorage(db_path)
        self.controller: Optional[Controller] = None
    
    def start(self):
        """Start the SMTP server"""
        handler = EmailHandler(self.storage)
        self.controller = Controller(handler, hostname=self.host, port=self.port)
        
        print(f"🚀 Starting SMTP server on {self.host}:{self.port}")
        print(f"📧 Ready to receive emails!")
        print(f"💡 Configure n8n SMTP to: {self.host}:{self.port}")
        
        self.controller.start()
    
    def stop(self):
        """Stop the SMTP server"""
        if self.controller:
            print("🛑 Stopping SMTP server...")
            self.controller.stop()
            print("✅ SMTP server stopped")
    
    def run_forever(self):
        """Run server forever (blocking)"""
        try:
            self.start()
            # Keep server running
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

