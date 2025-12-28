#!/usr/bin/env python3
"""
Get Netlify Site ID for ballcode site
Helps find the Site ID from Netlify API or dashboard
"""
import os
import sys
import requests

def get_site_id_from_api():
    """Get Site ID from Netlify API"""
    netlify_token = os.getenv("NETLIFY_AUTH_TOKEN")
    
    if not netlify_token:
        print("⚠️  NETLIFY_AUTH_TOKEN not set")
        print("   Get token: https://app.netlify.com/user/applications")
        return None
    
    try:
        headers = {"Authorization": f"Bearer {netlify_token}"}
        response = requests.get("https://api.netlify.com/api/v1/sites", headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ API error: {response.status_code}")
            return None
        
        sites = response.json()
        
        # Find ballcode site
        for site in sites:
            if "ballcode" in site.get("name", "").lower() or "ballcode" in site.get("url", "").lower():
                site_id = site.get("site_id") or site.get("id")
                print(f"✅ Found ballcode site!")
                print(f"   Site Name: {site.get('name')}")
                print(f"   Site URL: {site.get('url')}")
                print(f"   Site ID: {site_id}")
                return site_id
        
        print("⚠️  ballcode site not found in API")
        print("   Available sites:")
        for site in sites[:5]:  # Show first 5
            print(f"   - {site.get('name')} ({site.get('url')})")
        
        return None
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🔍 Finding Netlify Site ID for ballcode...")
    print("")
    
    # Try API first
    site_id = get_site_id_from_api()
    
    if site_id:
        print("")
        print("✅ Site ID found!")
        print(f"   {site_id}")
        print("")
        print("📋 To use it:")
        print(f"   export NETLIFY_SITE_ID='{site_id}'")
        print("")
        print("   Or add to ~/.zshrc:")
        print(f"   echo 'export NETLIFY_SITE_ID=\"{site_id}\"' >> ~/.zshrc")
        print("   source ~/.zshrc")
    else:
        print("")
        print("📋 MANUAL METHOD:")
        print("   1. Go to: https://app.netlify.com/sites/ballcode")
        print("   2. Click: 'Site configuration' or gear icon ⚙️")
        print("   3. Click: 'General' tab")
        print("   4. Find: 'Site ID' (UUID format)")
        print("   5. Copy it!")
        print("")
        print("   Or set NETLIFY_AUTH_TOKEN and run this script again")

if __name__ == "__main__":
    main()
