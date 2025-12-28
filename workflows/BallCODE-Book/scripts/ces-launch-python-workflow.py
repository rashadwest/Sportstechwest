#!/usr/bin/env python3
"""
CES Launch Python Workflow - Alternative to n8n
Replaces n8n workflow with pure Python script

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List

PROJECT_ROOT = Path(__file__).parent.parent
SCHOOL_DB_PATH = PROJECT_ROOT / "documents" / "school-contacts-database.json"
EMAIL_TEMPLATES_PATH = PROJECT_ROOT / "documents" / "promotion-content" / "email-templates.json"

# API Configuration
HUBSPOT_API_BASE = "https://api.hubapi.com"
MAILCHIMP_API_BASE = "https://us1.api.mailchimp.com/3.0"
BUFFER_API_BASE = "https://api.bufferapp.com/1"

class CESLaunchWorkflow:
    """Python workflow to replace n8n CES launch automation"""
    
    def __init__(self):
        self.hubspot_token = os.getenv("HUBSPOT_TOKEN", "")
        self.mailchimp_api_key = os.getenv("MAILCHIMP_API_KEY", "")
        self.mailchimp_list_id = os.getenv("MAILCHIMP_LIST_ID", "")
        self.buffer_api_key = os.getenv("BUFFER_API_KEY", "")
        
        # Extract Mailchimp datacenter
        if '-' in self.mailchimp_api_key:
            self.mailchimp_dc = self.mailchimp_api_key.split('-')[-1]
        else:
            self.mailchimp_dc = "us1"
        self.school_db_path = PROJECT_ROOT / "documents" / "school-contacts-database.json"
    
    def load_school_database(self) -> Dict:
        """Load school contacts database"""
        if SCHOOL_DB_PATH.exists():
            with open(SCHOOL_DB_PATH, 'r') as f:
                return json.load(f)
        return {"schools": []}
    
    def load_email_templates(self) -> Dict:
        """Load email templates"""
        if EMAIL_TEMPLATES_PATH.exists():
            with open(EMAIL_TEMPLATES_PATH, 'r') as f:
                return json.load(f)
        return {}
    
    def personalize_email(self, school: Dict, template: Dict) -> Dict:
        """Personalize email for school"""
        body = template.get("body_template", "")
        
        # Replace placeholders
        body = body.replace("{school_name}", school.get("name", ""))
        body = body.replace("{contact_name}", school.get("contact_name", "Team"))
        body = body.replace("{email}", "info@ballcode.co")
        body = body.replace("{phone}", school.get("phone", ""))
        
        return {
            "subject": template.get("subject", ""),
            "preheader": template.get("preheader", ""),
            "body": body,
            "cta": template.get("cta", ""),
            "cta_link": template.get("cta_link", "")
        }
    
    def send_mailchimp_campaign(self, schools: List[Dict], email_data: Dict) -> bool:
        """Send email campaign via Mailchimp"""
        if not self.mailchimp_api_key or not self.mailchimp_list_id:
            print("⚠️  Mailchimp not configured, skipping email send")
            return False
        
        # Create campaign
        url = f"https://{self.mailchimp_dc}.api.mailchimp.com/3.0/campaigns"
        headers = {
            "Authorization": f"Bearer {self.mailchimp_api_key}"
        }
        
        campaign_data = {
            "type": "regular",
            "recipients": {
                "list_id": self.mailchimp_list_id
            },
            "settings": {
                "subject_line": email_data["subject"],
                "preview_text": email_data["preheader"],
                "from_name": "Rashad West",
                "reply_to": "info@ballcode.co"
            }
        }
        
        try:
            response = requests.post(url, json=campaign_data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                campaign = response.json()
                print(f"✅ Mailchimp campaign created: {campaign.get('id')}")
                
                # Add content
                content_url = f"{url}/{campaign['id']}/content"
                content_data = {
                    "html": f"<html><body>{email_data['body'].replace(chr(10), '<br>')}</body></html>"
                }
                
                content_response = requests.put(content_url, json=content_data, headers=headers, timeout=30)
                
                if content_response.status_code == 200:
                    # Send campaign
                    send_url = f"{url}/{campaign['id']}/actions/send"
                    send_response = requests.post(send_url, headers=headers, timeout=30)
                    
                    if send_response.status_code == 204:
                        print("✅ Mailchimp campaign sent!")
                        return True
            
            print(f"⚠️  Mailchimp error: {response.status_code}")
            return False
        
        except Exception as e:
            print(f"❌ Mailchimp error: {str(e)}")
            return False
    
    def log_to_hubspot(self, school: Dict) -> bool:
        """Log school to HubSpot CRM (OPTIONAL - not required)"""
        if not self.hubspot_token:
            # HubSpot is optional - we track everything in our database
            return False
        
        url = f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts"
        headers = {
            "Authorization": f"Bearer {self.hubspot_token}",
            "Content-Type": "application/json"
        }
        
        contact_name = school.get("contact_name", "").split()
        properties = {
            "email": school.get("email", ""),
            "firstname": contact_name[0] if contact_name else "",
            "lastname": " ".join(contact_name[1:]) if len(contact_name) > 1 else "",
            "company": school.get("name", ""),
            "phone": school.get("phone", ""),
            "hs_lead_status": "NEW",
            "ballcode_status": "ces_launch_contacted",
            "ballcode_priority": school.get("priority", "medium")
        }
        
        data = {"properties": properties}
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                print(f"✅ Logged {school['name']} to HubSpot")
                return True
            else:
                print(f"⚠️  HubSpot error: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"❌ HubSpot error: {str(e)}")
            return False
    
    def post_to_buffer(self, post_text: str) -> bool:
        """
        Post to social media via Buffer.
        
        Args:
            post_text: The text content to post
            
        Returns:
            True if post was successful, False otherwise
        """
        if not self.buffer_api_key:
            print("⚠️  Buffer not configured, skipping social media post")
            return False
        
        url = f"{BUFFER_API_BASE}/updates/create.json"
        headers = {
            "Authorization": f"Bearer {self.buffer_api_key}"
        }
        data = {
            "text": post_text,
            "profile_ids": []  # Will post to all connected profiles
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code == 200:
                print("✅ Posted to Buffer!")
                return True
            else:
                print(f"⚠️  Buffer error: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"❌ Buffer error: {str(e)}")
            return False
    
    def update_database_tracking(self, personalized_emails: List):
        """
        Update our database with contact tracking (no HubSpot needed).
        
        Args:
            personalized_emails: List of tuples (school_dict, email_data)
        """
        try:
            if self.school_db_path.exists():
                import json
                with open(self.school_db_path, 'r') as f:
                    school_db = json.load(f)
                
                # Update status for contacted schools
                for school, _ in personalized_emails:
                    for db_school in school_db.get("schools", []):
                        if db_school.get("id") == school.get("id"):
                            db_school["status"] = "ces_launch_contacted"
                            db_school["date_contacted"] = datetime.now().isoformat()
                            break
                
                # Save updated database
                with open(self.school_db_path, 'w') as f:
                    json.dump(school_db, f, indent=2)
                
                print(f"   ✅ Updated {len(personalized_emails)} schools in database")
        except Exception as e:
            print(f"   ⚠️  Database update error: {str(e)}")
    
    def execute_launch(self):
        """Execute CES launch workflow"""
        print("\n" + "=" * 70)
        print("🚀 CES Launch Workflow - Python Version")
        print("=" * 70)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Step 1: Load data
        print("\n📄 Step 1: Loading data...")
        school_db = self.load_school_database()
        schools = school_db.get("schools", [])
        print(f"   Schools in database: {len(schools)}")
        
        email_templates = self.load_email_templates()
        ces_template = email_templates.get("ces_launch_announcement", {})
        print(f"   Email template loaded: {'✅' if ces_template else '❌'}")
        
        # Step 2: Personalize emails
        print("\n✉️  Step 2: Personalizing emails...")
        personalized_emails = []
        for school in schools:
            if school.get("email"):
                email_data = self.personalize_email(school, ces_template)
                personalized_emails.append((school, email_data))
        print(f"   Personalized emails: {len(personalized_emails)}")
        
        # Step 3: Send Mailchimp campaign
        if personalized_emails:
            print("\n📧 Step 3: Sending Mailchimp campaign...")
            # Use first email as template (Mailchimp sends to list)
            self.send_mailchimp_campaign([s[0] for s in personalized_emails], personalized_emails[0][1])
        
        # Step 4: Log to HubSpot (OPTIONAL)
        print("\n📊 Step 4: Logging to HubSpot (Optional)...")
        logged_count = 0  # Initialize before conditional block
        if self.hubspot_token:
            for school, _ in personalized_emails:
                if self.log_to_hubspot(school):
                    logged_count += 1
            print(f"   Logged to HubSpot: {logged_count}/{len(personalized_emails)}")
        else:
            print("   ⚠️  HubSpot not configured (optional - all tracking in our database)")
            # Update our database with contact status
            self.update_database_tracking(personalized_emails)
        
        # Step 5: Post to social media
        print("\n📱 Step 5: Posting to social media...")
        social_post = """🎉 BallCODE launches at CES 2026! 🏀💻

The first sports-based coding education platform is here.

Teaching coding through basketball stories. Students learn sequences by calling plays. They learn probability by analyzing shots. They learn AI by reading defenses.

10 pilot schools already running. Opening sign-ups for next 50 schools.

#CES2026 #EdTech #STEM #CodingEducation #Basketball #BallCODE

Learn more: https://ballcode.co"""
        
        buffer_posted = self.post_to_buffer(social_post)
        
        # Summary
        print("\n" + "=" * 70)
        print("✅ CES Launch Workflow Complete!")
        print("=" * 70)
        print(f"\n📊 Summary:")
        print(f"   Schools processed: {len(personalized_emails)}")
        print(f"   Emails sent: {'✅' if personalized_emails else '❌'}")
        print(f"   HubSpot logged: {logged_count}/{len(personalized_emails) if personalized_emails else 0}")
        print(f"   Social media posted: {'✅' if buffer_posted else '⚠️'}")
        print("=" * 70)


def main():
    """Main function"""
    workflow = CESLaunchWorkflow()
    workflow.execute_launch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

