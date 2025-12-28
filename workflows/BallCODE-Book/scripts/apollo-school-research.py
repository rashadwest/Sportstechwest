#!/usr/bin/env python3
"""
Robot: Research Schools Using Apollo API
Automates school database expansion using Apollo API

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
import requests
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent
SCHOOL_DB_PATH = PROJECT_ROOT / "documents" / "school-contacts-database.json"
APOLLO_API_BASE = "https://api.apollo.io/v1"

class ApolloSchoolResearch:
    """Robot to research schools using Apollo API"""
    
    def __init__(self):
        self.api_key = os.getenv("APOLLO_API_KEY", "")
        self.school_db = self.load_database()
    
    def load_database(self) -> Dict:
        """Load current school database"""
        if SCHOOL_DB_PATH.exists():
            with open(SCHOOL_DB_PATH, 'r') as f:
                return json.load(f)
        return {"metadata": {}, "schools": []}
    
    def save_database(self):
        """Save school database"""
        SCHOOL_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(SCHOOL_DB_PATH, 'w') as f:
            json.dump(self.school_db, f, indent=2)
        print(f"✅ Database saved: {len(self.school_db.get('schools', []))} schools")
    
    def search_schools(self, query: str, page: int = 1, per_page: int = 25) -> Optional[Dict]:
        """Search for schools using Apollo API"""
        if not self.api_key:
            print("❌ APOLLO_API_KEY not found in environment")
            return None
        
        url = f"{APOLLO_API_BASE}/organizations/search"
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        data = {
            "api_key": self.api_key,
            "q_keywords": query,
            "organization_locations": ["United States"],
            "organization_industry_tag_ids": ["5416"],  # Education
            "page": page,
            "per_page": per_page
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print("❌ Apollo API authentication failed (invalid API key)")
                return None
            else:
                print(f"⚠️  Apollo API returned HTTP {response.status_code}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Apollo API connection error: {str(e)}")
            return None
    
    def get_organization_contacts(self, organization_id: str) -> Optional[List[Dict]]:
        """Get contacts for an organization"""
        if not self.api_key:
            return None
        
        url = f"{APOLLO_API_BASE}/mixed_people/search"
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        data = {
            "api_key": self.api_key,
            "organization_ids": [organization_id],
            "person_titles": ["Principal", "STEM Coordinator", "Technology Director", "Curriculum Director"],
            "per_page": 10
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("people", [])
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"⚠️  Error fetching contacts: {str(e)}")
            return None
    
    def process_school_result(self, org: Dict) -> Optional[Dict]:
        """Process Apollo organization result into school format"""
        # Check if it's a school (grades 3-8)
        name = org.get("name", "")
        industry = org.get("industry", "")
        
        # Filter for schools
        if "school" not in name.lower() and "academy" not in name.lower() and "education" not in industry.lower():
            return None
        
        # Get contacts
        org_id = org.get("id")
        contacts = self.get_organization_contacts(org_id) if org_id else []
        
        # Find best contact (Principal or STEM Coordinator)
        best_contact = None
        for contact in contacts:
            title = contact.get("title", "").lower()
            if "principal" in title or "stem" in title or "technology" in title:
                best_contact = contact
                break
        
        if not best_contact and contacts:
            best_contact = contacts[0]
        
        # Build school data
        school = {
            "name": name,
            "district": org.get("city", "") + " School District",
            "state": org.get("state", ""),
            "contact_name": best_contact.get("first_name", "") + " " + best_contact.get("last_name", "") if best_contact else "",
            "contact_title": best_contact.get("title", "Principal/STEM Coordinator") if best_contact else "Principal/STEM Coordinator",
            "email": best_contact.get("email", "") if best_contact else "",
            "phone": best_contact.get("phone_numbers", [{}])[0].get("raw_number", "") if best_contact and best_contact.get("phone_numbers") else "",
            "grades": "3-8",  # Default, can be updated
            "student_count": "",
            "stem_programs": ["Science", "Math", "Technology"],
            "basketball_programs": True,
            "priority": "high",
            "status": "not_contacted",
            "pilot_committed": False,
            "notes": f"Found via Apollo API - {org.get('website_url', '')}"
        }
        
        return school
    
    def research_schools(self, queries: List[str], max_schools: int = 100) -> List[Dict]:
        """Research schools using multiple queries"""
        all_schools = []
        current_count = len(self.school_db.get('schools', []))
        target_count = current_count + max_schools
        
        print(f"\n🔍 Researching schools via Apollo API (Paid Tier)...")
        print(f"   Current: {current_count} schools")
        print(f"   Target: {target_count} schools")
        print(f"   Need: {max_schools} more schools")
        print(f"   API Tier: Paid (1,000+ calls/month available)")
        
        for query in queries:
            if len(all_schools) >= max_schools:
                break
            
            print(f"\n   Searching: '{query}'...")
            
            # Search first page
            result = self.search_schools(query, page=1)
            if not result:
                continue
            
            organizations = result.get("organizations", [])
            print(f"   Found: {len(organizations)} organizations")
            
            for org in organizations:
                if len(all_schools) >= max_schools:
                    break
                
                school = self.process_school_result(org)
                if school and school.get("email"):  # Only add if we have contact info
                    all_schools.append(school)
                    print(f"   ✅ Added: {school['name']} ({school.get('email', 'No email')})")
        
        return all_schools
    
    def add_schools_to_database(self, schools: List[Dict]):
        """Add researched schools to database"""
        if 'schools' not in self.school_db:
            self.school_db['schools'] = []
        
        current_count = len(self.school_db['schools'])
        
        for i, school in enumerate(schools, 1):
            school['id'] = f"school_{current_count + i:03d}"
            self.school_db['schools'].append(school)
        
        self.save_database()
        print(f"\n✅ Added {len(schools)} schools to database")
        print(f"   Total schools: {len(self.school_db['schools'])}")


def main():
    """Main robot function"""
    print("\n" + "=" * 70)
    print("🤖 Robot: Research Schools Using Apollo API")
    print("=" * 70)
    
    researcher = ApolloSchoolResearch()
    
    if not researcher.api_key:
        print("\n❌ APOLLO_API_KEY not found in environment")
        print("\n💡 To get started:")
        print("   1. Sign up at: https://www.apollo.io/")
        print("   2. Get API key from: Settings → API")
        print("   3. Add to .env file: APOLLO_API_KEY=your_key")
        print("   4. Paid tier: 1,000+ API calls/month (you have this!)")
        sys.exit(1)
    
    # Search queries for schools
    queries = [
        "elementary school STEM",
        "middle school STEM",
        "charter school STEM",
        "academy STEM",
        "elementary school basketball",
        "middle school basketball",
        "STEM academy",
        "science and math school",
        "technology school",
        "coding school"
    ]
    
    # Research schools
    schools = researcher.research_schools(queries, max_schools=100)
    
    if schools:
        print(f"\n📊 Research Results:")
        print(f"   Schools found: {len(schools)}")
        print(f"   With email: {len([s for s in schools if s.get('email')])}")
        print(f"   With phone: {len([s for s in schools if s.get('phone')])}")
        
        # Add to database
        researcher.add_schools_to_database(schools)
    else:
        print("\n⚠️  No schools found. Check:")
        print("   1. API key is correct")
        print("   2. Free tier has remaining calls")
        print("   3. Search queries are appropriate")
    
    print("\n" + "=" * 70)


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

