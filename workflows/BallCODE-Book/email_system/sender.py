"""
Email Sender
Send emails through SMTP server
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Optional, List
from datetime import datetime
from pathlib import Path
try:
    from .storage import EmailStorage
except ImportError:
    from storage import EmailStorage


class EmailSender:
    """Send emails through SMTP server"""
    
    def __init__(self, smtp_host: str = None, smtp_port: int = None,
                 smtp_user: Optional[str] = None, smtp_password: Optional[str] = None,
                 use_tls: bool = False, db_path: str = "emails.db"):
        """
        Initialize email sender
        
        Args:
            smtp_host: SMTP server hostname
            smtp_port: SMTP server port
            smtp_user: SMTP username (optional)
            smtp_password: SMTP password (optional)
            use_tls: Use TLS encryption
            db_path: Path to email database (for storing sent emails)
        """
        # Load configuration
        config_file = Path(__file__).parent / "email_config.json"
        if config_file.exists():
            import json
            with open(config_file) as f:
                config = json.load(f)
            
            # Check for external SMTP configuration
            smtp_external = config.get("smtp_external", {})
            if smtp_external.get("enabled"):
                self.smtp_host = smtp_external.get("host", "localhost")
                self.smtp_port = smtp_external.get("port", 2525)
                self.smtp_user = smtp_external.get("username") or smtp_user
                self.smtp_password = smtp_external.get("password") or smtp_password
                self.use_tls = smtp_external.get("use_tls", True)
            else:
                # Use local or provided values
                self.smtp_host = smtp_host or config.get("smtp", {}).get("host", "localhost")
                self.smtp_port = smtp_port or config.get("smtp", {}).get("port", 2525)
                self.smtp_user = smtp_user
                self.smtp_password = smtp_password
                self.use_tls = use_tls
        else:
            # Default to local
            self.smtp_host = smtp_host or "localhost"
            self.smtp_port = smtp_port or 2525
            self.smtp_user = smtp_user
            self.smtp_password = smtp_password
            self.use_tls = use_tls
        
        self.storage = EmailStorage(db_path)
    
    def send(self, to_address: str, subject: str, body: str, 
             from_address: str = "noreply@ballcode.co",
             html_body: Optional[str] = None,
             attachments: Optional[List[str]] = None) -> bool:
        """
        Send email
        
        Args:
            to_address: Recipient email address
            subject: Email subject
            body: Email body (plain text)
            from_address: Sender email address
            html_body: HTML body (optional)
            attachments: List of file paths to attach (optional)
            
        Returns:
            True if sent successfully, False otherwise
        """
        try:
            # Create message
            if html_body:
                msg = MIMEMultipart('alternative')
                msg.attach(MIMEText(body, 'plain'))
                msg.attach(MIMEText(html_body, 'html'))
            else:
                msg = MIMEMultipart()
                msg.attach(MIMEText(body, 'plain'))
            
            # Set headers
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject
            msg['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
            
            # Add attachments
            if attachments:
                for file_path in attachments:
                    try:
                        with open(file_path, 'rb') as f:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(f.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename= {file_path.split("/")[-1]}'
                            )
                            msg.attach(part)
                    except Exception as e:
                        print(f"⚠️  Warning: Could not attach {file_path}: {e}")
            
            # Connect to SMTP server
            if self.use_tls:
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                server.starttls()
            else:
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            
            # Authenticate if credentials provided
            if self.smtp_user and self.smtp_password:
                server.login(self.smtp_user, self.smtp_password)
            
            # Send email
            server.send_message(msg)
            server.quit()
            
            # Store sent email in database
            raw_email = msg.as_bytes()
            self.storage.save_email(raw_email, folder='sent')
            
            print(f"✅ Email sent to {to_address}")
            return True
            
        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False
    
    def send_via_local(self, to_address: str, subject: str, body: str,
                      from_address: str = "noreply@ballcode.co",
                      html_body: Optional[str] = None) -> bool:
        """
        Send email via local SMTP server (for testing)
        
        Args:
            to_address: Recipient email address
            subject: Email subject
            body: Email body
            from_address: Sender email address
            html_body: HTML body (optional)
            
        Returns:
            True if sent successfully, False otherwise
        """
        return self.send(
            to_address=to_address,
            subject=subject,
            body=body,
            from_address=from_address,
            html_body=html_body
        )

