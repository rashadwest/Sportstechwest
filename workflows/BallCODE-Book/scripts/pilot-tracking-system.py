#!/usr/bin/env python3
"""
Pilot Program Tracking System
Tracks school outreach, responses, and pilot commitments for CES launch

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
SCHOOL_DB_PATH = PROJECT_ROOT / "documents" / "school-contacts-database.json"
REPORTS_DIR = PROJECT_ROOT / "documents"
HUBSPOT_API_BASE = "https://api.hubapi.com"
MAILCHIMP_API_BASE = "https://us1.api.mailchimp.com/3.0"

class PilotTrackingSystem:
    """Track pilot program outreach and commitments"""
    
    def __init__(self):
        self.school_db = self.load_school_database()
        self.hubspot_token = os.getenv("HUBSPOT_TOKEN")
        self.mailchimp_api_key = os.getenv("MAILCHIMP_API_KEY")
        self.mailchimp_list_id = os.getenv("MAILCHIMP_LIST_ID")
    
    def load_school_database(self) -> Dict:
        """Load school contacts database"""
        if SCHOOL_DB_PATH.exists():
            with open(SCHOOL_DB_PATH, 'r') as f:
                return json.load(f)
        return {"metadata": {}, "schools": []}
    
    def save_school_database(self):
        """Save school contacts database"""
        SCHOOL_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(SCHOOL_DB_PATH, 'w') as f:
            json.dump(self.school_db, f, indent=2)
    
    def add_school(self, school_data: Dict):
        """Add a new school to the database"""
        school_id = f"school_{len(self.school_db.get('schools', [])) + 1:03d}"
        school_data['id'] = school_id
        school_data['status'] = school_data.get('status', 'not_contacted')
        school_data['pilot_committed'] = school_data.get('pilot_committed', False)
        
        if 'schools' not in self.school_db:
            self.school_db['schools'] = []
        
        self.school_db['schools'].append(school_data)
        self.save_school_database()
        return school_id
    
    def update_school_status(self, school_id: str, status: str, **kwargs):
        """Update school status and additional fields"""
        for school in self.school_db.get('schools', []):
            if school['id'] == school_id:
                school['status'] = status
                if status == 'contacted':
                    school['date_contacted'] = datetime.now().isoformat()
                for key, value in kwargs.items():
                    school[key] = value
                self.save_school_database()
                return True
        return False
    
    def get_schools_by_status(self, status: str) -> List[Dict]:
        """Get all schools with a specific status"""
        return [s for s in self.school_db.get('schools', []) if s.get('status') == status]
    
    def get_pilot_commitments(self) -> List[Dict]:
        """Get all schools with pilot commitments"""
        return [s for s in self.school_db.get('schools', []) if s.get('pilot_committed') == True]
    
    def log_to_hubspot(self, school: Dict):
        """Log school contact to HubSpot CRM"""
        if not self.hubspot_token:
            print("⚠️  HubSpot token not configured. Skipping HubSpot logging.")
            return
        
        url = f"{HUBSPOT_API_BASE}/crm/v3/objects/contacts"
        headers = {
            "Authorization": f"Bearer {self.hubspot_token}",
            "Content-Type": "application/json"
        }
        
        properties = {
            "email": school.get('email', ''),
            "firstname": school.get('contact_name', '').split()[0] if school.get('contact_name') else '',
            "lastname": ' '.join(school.get('contact_name', '').split()[1:]) if school.get('contact_name') and len(school.get('contact_name', '').split()) > 1 else '',
            "company": school.get('name', ''),
            "phone": school.get('phone', ''),
            "hs_lead_status": "NEW",
            "ballcode_school_id": school.get('id', ''),
            "ballcode_status": school.get('status', 'not_contacted'),
            "ballcode_priority": school.get('priority', 'medium')
        }
        
        data = {"properties": properties}
        
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code in [200, 201]:
                print(f"✅ Logged {school['name']} to HubSpot")
                return response.json()
            else:
                print(f"⚠️  HubSpot error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"⚠️  Error logging to HubSpot: {e}")
    
    def generate_daily_report(self) -> Dict:
        """Generate daily metrics report"""
        schools = self.school_db.get('schools', [])
        
        report = {
            "date": datetime.now().isoformat(),
            "total_schools": len(schools),
            "by_status": {},
            "metrics": {
                "contacted": len([s for s in schools if s.get('status') == 'contacted']),
                "responded": len([s for s in schools if s.get('response_status') == 'responded']),
                "calls_scheduled": len([s for s in schools if s.get('call_scheduled')]),
                "pilot_committed": len([s for s in schools if s.get('pilot_committed') == True]),
                "onboarded": len([s for s in schools if s.get('onboarding_status') == 'onboarded'])
            },
            "response_rate": 0,
            "conversion_rate": 0
        }
        
        # Calculate rates
        contacted = report["metrics"]["contacted"]
        if contacted > 0:
            report["response_rate"] = (report["metrics"]["responded"] / contacted) * 100
            report["conversion_rate"] = (report["metrics"]["pilot_committed"] / contacted) * 100
        
        # Group by status
        for school in schools:
            status = school.get('status', 'unknown')
            report["by_status"][status] = report["by_status"].get(status, 0) + 1
        
        return report
    
    def save_daily_report(self):
        """Save daily report to file"""
        report = self.generate_daily_report()
        date_str = datetime.now().strftime("%Y-%m-%d")
        report_file = REPORTS_DIR / f"pilot-ces-daily-report-{date_str}.json"
        
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"✅ Daily report saved: {report_file}")
        return report_file
    
    def get_follow_up_schools(self, days: int = 3) -> List[Dict]:
        """Get schools that need follow-up (contacted X days ago, no response)"""
        cutoff_date = datetime.now() - timedelta(days=days)
        follow_ups = []
        
        for school in self.school_db.get('schools', []):
            if school.get('status') == 'contacted' and not school.get('response_status'):
                date_contacted = school.get('date_contacted')
                if date_contacted:
                    try:
                        contact_date = datetime.fromisoformat(date_contacted)
                        if contact_date <= cutoff_date:
                            follow_ups.append(school)
                    except:
                        pass
        
        return follow_ups
    
    def export_for_mailchimp(self) -> List[Dict]:
        """Export schools for Mailchimp email campaign"""
        return [
            {
                "email_address": school.get('email', ''),
                "status": "subscribed",
                "merge_fields": {
                    "FNAME": school.get('contact_name', '').split()[0] if school.get('contact_name') else '',
                    "LNAME": ' '.join(school.get('contact_name', '').split()[1:]) if school.get('contact_name') and len(school.get('contact_name', '').split()) > 1 else '',
                    "SCHOOL": school.get('name', ''),
                    "GRADES": school.get('grades', ''),
                    "STATUS": school.get('status', 'not_contacted')
                }
            }
            for school in self.school_db.get('schools', [])
            if school.get('email')
        ]


def main():
    """CLI interface for pilot tracking system"""
    tracker = PilotTrackingSystem()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python pilot-tracking-system.py report          # Generate daily report")
        print("  python pilot-tracking-system.py status          # Show current status")
        print("  python pilot-tracking-system.py followup [days] # Get follow-up list")
        print("  python pilot-tracking-system.py commitments     # List pilot commitments")
        return
    
    command = sys.argv[1]
    
    if command == "report":
        report = tracker.generate_daily_report()
        print("\n📊 Daily Pilot Program Report")
        print("=" * 50)
        print(f"Date: {report['date']}")
        print(f"Total Schools: {report['total_schools']}")
        print(f"\nMetrics:")
        for key, value in report['metrics'].items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
        print(f"\nResponse Rate: {report['response_rate']:.1f}%")
        print(f"Conversion Rate: {report['conversion_rate']:.1f}%")
        tracker.save_daily_report()
    
    elif command == "status":
        schools = tracker.school_db.get('schools', [])
        print(f"\n📋 Current Status: {len(schools)} schools in database")
        print("=" * 50)
        for status in ['not_contacted', 'contacted', 'responded', 'call_scheduled', 'pilot_committed']:
            count = len(tracker.get_schools_by_status(status))
            if count > 0:
                print(f"  {status.replace('_', ' ').title()}: {count}")
    
    elif command == "followup":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        follow_ups = tracker.get_follow_up_schools(days)
        print(f"\n📧 Schools Needing Follow-up ({days} days): {len(follow_ups)}")
        print("=" * 50)
        for school in follow_ups:
            print(f"  {school['name']} - Contacted: {school.get('date_contacted', 'Unknown')}")
    
    elif command == "commitments":
        commitments = tracker.get_pilot_commitments()
        print(f"\n✅ Pilot Commitments: {len(commitments)}")
        print("=" * 50)
        for school in commitments:
            print(f"  {school['name']} - Status: {school.get('onboarding_status', 'pending')}")
    
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()


