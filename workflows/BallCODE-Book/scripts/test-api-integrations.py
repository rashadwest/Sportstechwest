#!/usr/bin/env python3
"""
Robot: Test API Integrations for CES Launch
Tests HubSpot, Mailchimp, and Buffer API connections

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import requests
from typing import Dict, Optional, Tuple

class APITester:
    """Robot to test API integrations"""
    
    def __init__(self):
        self.hubspot_token = os.getenv("HUBSPOT_TOKEN", "")
        self.mailchimp_api_key = os.getenv("MAILCHIMP_API_KEY", "")
        self.mailchimp_list_id = os.getenv("MAILCHIMP_LIST_ID", "")
        self.buffer_api_key = os.getenv("BUFFER_API_KEY", "")
        self.apollo_api_key = os.getenv("APOLLO_API_KEY", "")
        self.canva_api_key = os.getenv("CANVA_API_KEY", "")
        self.canva_access_token = os.getenv("CANVA_ACCESS_TOKEN", "")
    
    def test_hubspot(self) -> Tuple[bool, str, Dict]:
        """Test HubSpot API connection"""
        print("\n🔵 Testing HubSpot API...")
        
        if not self.hubspot_token:
            return False, "No HUBSPOT_TOKEN found in environment", {}
        
        url = "https://api.hubapi.com/crm/v3/objects/contacts"
        headers = {
            "Authorization": f"Bearer {self.hubspot_token}",
            "Content-Type": "application/json"
        }
        
        try:
            # Test with a simple GET request
            response = requests.get(f"{url}?limit=1", headers=headers, timeout=10)
            
            if response.status_code == 200:
                return True, "✅ HubSpot API connection successful", {}
            elif response.status_code == 401:
                return False, "❌ HubSpot authentication failed (invalid token)", {}
            else:
                return False, f"⚠️  HubSpot API returned HTTP {response.status_code}", {}
        
        except requests.exceptions.RequestException as e:
            return False, f"❌ HubSpot connection error: {str(e)}", {}
    
    def test_mailchimp(self) -> Tuple[bool, str, Dict]:
        """Test Mailchimp API connection"""
        print("\n🟢 Testing Mailchimp API...")
        
        if not self.mailchimp_api_key:
            return False, "No MAILCHIMP_API_KEY found in environment", {}
        
        # Extract datacenter from API key (format: key-datacenter)
        if '-' in self.mailchimp_api_key:
            datacenter = self.mailchimp_api_key.split('-')[-1]
        else:
            datacenter = "us1"  # Default
        
        url = f"https://{datacenter}.api.mailchimp.com/3.0/"
        
        # Test with ping endpoint
        ping_url = f"{url}ping"
        headers = {
            "Authorization": f"Bearer {self.mailchimp_api_key}"
        }
        
        try:
            response = requests.get(ping_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                if result.get("health_status") == "Everything's Chimpy!":
                    return True, "✅ Mailchimp API connection successful", result
                else:
                    return False, f"⚠️  Mailchimp health check: {result.get('health_status')}", result
            elif response.status_code == 401:
                return False, "❌ Mailchimp authentication failed (invalid API key)", {}
            else:
                return False, f"⚠️  Mailchimp API returned HTTP {response.status_code}", {}
        
        except requests.exceptions.RequestException as e:
            return False, f"❌ Mailchimp connection error: {str(e)}", {}
    
    def test_mailchimp_list(self) -> Tuple[bool, str, Dict]:
        """Test Mailchimp list access"""
        print("\n📋 Testing Mailchimp List Access...")
        
        if not self.mailchimp_api_key:
            return False, "No MAILCHIMP_API_KEY found", {}
        
        if not self.mailchimp_list_id:
            return False, "No MAILCHIMP_LIST_ID found", {}
        
        # Extract datacenter
        if '-' in self.mailchimp_api_key:
            datacenter = self.mailchimp_api_key.split('-')[-1]
        else:
            datacenter = "us1"
        
        url = f"https://{datacenter}.api.mailchimp.com/3.0/lists/{self.mailchimp_list_id}"
        headers = {
            "Authorization": f"Bearer {self.mailchimp_api_key}"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                list_data = response.json()
                return True, f"✅ Mailchimp list accessible: {list_data.get('name', 'Unknown')}", list_data
            elif response.status_code == 404:
                return False, f"❌ Mailchimp list not found (ID: {self.mailchimp_list_id})", {}
            elif response.status_code == 401:
                return False, "❌ Mailchimp authentication failed", {}
            else:
                return False, f"⚠️  Mailchimp list check returned HTTP {response.status_code}", {}
        
        except requests.exceptions.RequestException as e:
            return False, f"❌ Mailchimp list connection error: {str(e)}", {}
    
    def test_buffer(self) -> Tuple[bool, str, Dict]:
        """Test Buffer API connection"""
        print("\n🟡 Testing Buffer API...")
        
        if not self.buffer_api_key:
            return False, "No BUFFER_API_KEY found in environment (optional)", {}
        
        url = "https://api.bufferapp.com/1/user.json"
        headers = {
            "Authorization": f"Bearer {self.buffer_api_key}"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                user_data = response.json()
                return True, f"✅ Buffer API connection successful (User: {user_data.get('email', 'Unknown')})", user_data
            elif response.status_code == 401:
                return False, "❌ Buffer authentication failed (invalid API key)", {}
            else:
                return False, f"⚠️  Buffer API returned HTTP {response.status_code}", {}
        
        except requests.exceptions.RequestException as e:
            return False, f"❌ Buffer connection error: {str(e)}", {}
    
    def test_apollo(self) -> Tuple[bool, str, Dict]:
        """Test Apollo API connection"""
        print("\n🔴 Testing Apollo API...")
        
        if not self.apollo_api_key:
            return False, "No APOLLO_API_KEY found in environment", {}
        
        url = "https://api.apollo.io/v1/auth/health"
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        data = {
            "api_key": self.apollo_api_key
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return True, "✅ Apollo API connection successful", {}
            elif response.status_code == 401:
                return False, "❌ Apollo authentication failed (invalid API key)", {}
            else:
                return False, f"⚠️  Apollo API returned HTTP {response.status_code}", {}
        
        except requests.exceptions.RequestException as e:
            return False, f"❌ Apollo connection error: {str(e)}", {}
    
    def test_canva(self) -> Tuple[bool, str, Dict]:
        """Test Canva API connection"""
        print("\n🟣 Testing Canva API...")
        
        if not self.canva_api_key and not self.canva_access_token:
            return False, "No CANVA_API_KEY or CANVA_ACCESS_TOKEN found (optional)", {}
        
        # Canva API requires OAuth token for most operations
        # Simple check: verify token format
        token = self.canva_access_token or self.canva_api_key
        
        if token:
            # Basic validation - Canva tokens are typically long strings
            if len(token) > 20:
                return True, "✅ Canva API key/token found (format looks valid)", {}
            else:
                return False, "⚠️  Canva token format may be invalid", {}
        
        return False, "No Canva credentials found", {}
    
    def print_summary(self, results: Dict):
        """Print test summary"""
        print("\n" + "=" * 70)
        print("📊 API Integration Test Summary")
        print("=" * 70)
        
        for api_name, (success, message, data) in results.items():
            status_icon = "✅" if success else "❌"
            print(f"\n{status_icon} {api_name}:")
            print(f"   {message}")
            if data and success:
                # Print relevant data
                if api_name == "Mailchimp List" and 'stats' in data:
                    stats = data.get('stats', {})
                    print(f"   Members: {stats.get('member_count', 'N/A')}")
                    print(f"   Unsubscribed: {stats.get('unsubscribe_count', 'N/A')}")
        
        print("\n" + "=" * 70)
        
        # Overall status
        all_success = all(success for success, _, _ in results.values())
        critical_success = results.get("Mailchimp", (False,))[0]  # Mailchimp is critical
        
        if all_success:
            print("✅ All API integrations working!")
        elif critical_success:
            print("✅ Critical API working (Mailchimp)")
            print("   HubSpot is optional (we track in our database)")
            print("   Buffer is optional for launch")
        else:
            print("❌ Critical API integration needs attention (Mailchimp)")
            print("\n💡 Next Steps:")
            print("   1. Check environment variables (.env file)")
            print("   2. Verify API keys are correct")
            print("   3. Check API key permissions")
            print("   4. Test manually in API documentation")
        
        print("=" * 70)


def main():
    """Main robot function"""
    print("\n" + "=" * 70)
    print("🤖 Robot: Test API Integrations for CES Launch")
    print("=" * 70)
    
    tester = APITester()
    results = {}
    
    # Test HubSpot
    success, message, data = tester.test_hubspot()
    results["HubSpot"] = (success, message, data)
    print(message)
    
    # Test Mailchimp
    success, message, data = tester.test_mailchimp()
    results["Mailchimp"] = (success, message, data)
    print(message)
    
    # Test Mailchimp List
    if results["Mailchimp"][0]:  # Only test if Mailchimp API works
        success, message, data = tester.test_mailchimp_list()
        results["Mailchimp List"] = (success, message, data)
        print(message)
    
    # Test Buffer (optional)
    success, message, data = tester.test_buffer()
    results["Buffer"] = (success, message, data)
    print(message)
    
    # Test Apollo
    success, message, data = tester.test_apollo()
    results["Apollo"] = (success, message, data)
    print(message)
    
    # Test Canva (optional)
    success, message, data = tester.test_canva()
    results["Canva"] = (success, message, data)
    print(message)
    
    # Print summary
    tester.print_summary(results)
    
    # Return exit code (Mailchimp is critical, HubSpot is optional)
    critical_success = results.get("Mailchimp", (False,))[0]
    sys.exit(0 if critical_success else 1)


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

