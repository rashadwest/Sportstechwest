"""
Apollo.io Integration
Integrate with Apollo for sales pipeline and lead management
"""

import json
import requests
from pathlib import Path
from typing import Optional, Dict, List

class ApolloIntegration:
    """Integrate with Apollo.io API for sales pipeline"""
    
    def __init__(self, config_file: str = "email_config.json"):
        self.config_file = Path(__file__).parent / config_file
        self.api_key = None
        self.enabled = False
        self.base_url = "https://api.apollo.io/v1"
        self._load_config()
    
    def _load_config(self):
        """Load Apollo configuration"""
        if self.config_file.exists():
            try:
                config = json.load(open(self.config_file))
                apollo_config = config.get("apollo", {})
                self.api_key = apollo_config.get("api_key", "")
                self.enabled = apollo_config.get("enabled", False) and bool(self.api_key)
            except:
                self.enabled = False
    
    def search_people(self, email: Optional[str] = None, domain: Optional[str] = None, 
                     name: Optional[str] = None) -> List[Dict]:
        """
        Search for people in Apollo
        
        Args:
            email: Email address to search
            domain: Company domain to search
            name: Name to search
            
        Returns:
            List of matching people
        """
        if not self.enabled:
            return []
        
        params = {
            "api_key": self.api_key,
            "page": 1,
            "per_page": 10
        }
        
        if email:
            params["person_emails"] = email
        if domain:
            params["organization_domains"] = domain
        if name:
            params["person_titles"] = name
        
        try:
            response = requests.get(
                f"{self.base_url}/mixed_people/search",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get("people", [])
        except Exception as e:
            print(f"⚠️  Apollo search failed: {e}")
            return []
    
    def get_person_by_email(self, email: str) -> Optional[Dict]:
        """
        Get person information by email
        
        Args:
            email: Email address
            
        Returns:
            Person data or None
        """
        people = self.search_people(email=email)
        return people[0] if people else None
    
    def add_to_sequence(self, person_id: str, sequence_id: str) -> bool:
        """
        Add person to Apollo sequence
        
        Args:
            person_id: Apollo person ID
            sequence_id: Apollo sequence ID
            
        Returns:
            True if successful
        """
        if not self.enabled:
            return False
        
        try:
            response = requests.post(
                f"{self.base_url}/emailer_campaigns/{sequence_id}/add_contact",
                json={
                    "api_key": self.api_key,
                    "contact_id": person_id
                },
                timeout=10
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"⚠️  Apollo sequence add failed: {e}")
            return False
    
    def enrich_email(self, email: str) -> Optional[Dict]:
        """
        Enrich email with Apollo data
        
        Args:
            email: Email address to enrich
            
        Returns:
            Enriched person data
        """
        return self.get_person_by_email(email)
    
    def create_lead_from_email(self, email_data: Dict) -> Optional[Dict]:
        """
        Create sales lead from email
        
        Args:
            email_data: Email data with from, subject, body
            
        Returns:
            Lead data with Apollo enrichment
        """
        from_address = email_data.get("from_address", "")
        
        if not from_address or not self.enabled:
            return None
        
        # Extract email from "Name <email@domain.com>" format
        email = from_address.split("<")[-1].split(">")[0].strip()
        
        # Enrich with Apollo
        person_data = self.enrich_email(email)
        
        if person_data:
            return {
                "name": person_data.get("name", ""),
                "email": email,
                "company": person_data.get("organization", {}).get("name", ""),
                "title": person_data.get("title", ""),
                "apollo_id": person_data.get("id", ""),
                "status": "new",
                "source": "email",
                "email_subject": email_data.get("subject", ""),
                "email_body": email_data.get("body", "")[:500]  # First 500 chars
            }
        
        return None



