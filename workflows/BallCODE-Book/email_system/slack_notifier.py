"""
Slack Notification System
Sends email notifications to Slack (no email client needed)
"""

import json
import requests
from pathlib import Path
from typing import Optional, Dict

class SlackNotifier:
    """Send email notifications to Slack"""
    
    def __init__(self, config_file: str = "email_config.json"):
        self.config_file = Path(__file__).parent / config_file
        self.webhook_url = None
        self.enabled = False
        self._load_config()
    
    def _load_config(self):
        """Load Slack configuration"""
        if self.config_file.exists():
            try:
                config = json.load(open(self.config_file))
                slack_config = config.get("slack", {})
                self.webhook_url = slack_config.get("webhook_url", "")
                self.enabled = slack_config.get("enabled", False) and bool(self.webhook_url)
            except:
                self.enabled = False
    
    def notify_new_email(self, email_data: Dict):
        """
        Send notification to Slack when new email arrives
        
        Args:
            email_data: Email dictionary with from, to, subject, body
        """
        if not self.enabled:
            return False
        
        message = {
            "text": "📧 New Email Received",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "📧 New Email"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*From:*\n{email_data.get('from_address', 'Unknown')}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*To:*\n{email_data.get('to_address', 'Unknown')}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Subject:*\n{email_data.get('subject', 'No Subject')}"
                        }
                    ]
                }
            ]
        }
        
        # Add body preview if available
        body = email_data.get('body', '')[:200]  # First 200 chars
        if body:
            message["blocks"].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Preview:*\n{body}..."
                }
            })
        
        return self._send_to_slack(message)
    
    def notify_email_sent(self, to_address: str, subject: str):
        """
        Send notification to Slack when email is sent
        
        Args:
            to_address: Recipient email
            subject: Email subject
        """
        if not self.enabled:
            return False
        
        message = {
            "text": f"✅ Email Sent to {to_address}",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"✅ *Email Sent*\n*To:* {to_address}\n*Subject:* {subject}"
                    }
                }
            ]
        }
        
        return self._send_to_slack(message)
    
    def notify_sales_lead(self, lead_data: Dict):
        """
        Send sales lead notification to Slack
        
        Args:
            lead_data: Lead information from Apollo or email
        """
        if not self.enabled:
            return False
        
        message = {
            "text": "🎯 New Sales Lead",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "🎯 New Sales Lead"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Name:*\n{lead_data.get('name', 'Unknown')}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Email:*\n{lead_data.get('email', 'Unknown')}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Company:*\n{lead_data.get('company', 'Unknown')}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Status:*\n{lead_data.get('status', 'New')}"
                        }
                    ]
                }
            ]
        }
        
        return self._send_to_slack(message)
    
    def _send_to_slack(self, message: Dict) -> bool:
        """Send message to Slack webhook"""
        if not self.webhook_url:
            return False
        
        try:
            response = requests.post(
                self.webhook_url,
                json=message,
                timeout=5
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"⚠️  Slack notification failed: {e}")
            return False


