#!/usr/bin/env python3
"""
Robot: Setup All APIs for CES Launch
Guides through API key configuration for all services

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List

PROJECT_ROOT = Path(__file__).parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
ENV_EXAMPLE = PROJECT_ROOT / ".env.example"

class APISetupGuide:
    """Robot to guide API setup"""
    
    def __init__(self):
        self.apis = {
            "HubSpot": {
                "free": True,
                "optional": True,
                "description": "CRM for contact management (OPTIONAL - we track in our database)",
                "get_key_url": "https://app.hubspot.com/settings/integrations/private-apps",
                "env_var": "HUBSPOT_TOKEN",
                "instructions": [
                    "NOTE: HubSpot is OPTIONAL - we track everything in our database",
                    "You can skip HubSpot and use Mailchimp + our database instead",
                    "",
                    "If you want HubSpot (free tier available):",
                    "1. Go to HubSpot Settings → Integrations → Private Apps",
                    "2. Click 'Create a private app'",
                    "3. Name it 'BallCODE CES Launch'",
                    "4. Select scopes: 'crm.objects.contacts.read', 'crm.objects.contacts.write'",
                    "5. Click 'Create app'",
                    "6. Copy the 'Access token'",
                    "7. Add to .env: HUBSPOT_TOKEN=your_token (optional)"
                ]
            },
            "Mailchimp": {
                "free": True,
                "description": "Email marketing (500 contacts free)",
                "get_key_url": "https://us1.admin.mailchimp.com/account/api/",
                "env_vars": ["MAILCHIMP_API_KEY", "MAILCHIMP_LIST_ID"],
                "instructions": [
                    "1. Go to Mailchimp Account → Extras → API keys",
                    "2. Click 'Create A Key'",
                    "3. Copy the API key (format: xxxxxxxx-us1)",
                    "4. Add to .env: MAILCHIMP_API_KEY=your_key-us1",
                    "5. Get List ID:",
                    "   - Go to Audience → All contacts",
                    "   - Click 'Settings' → 'Audience name and defaults'",
                    "   - Copy the 'Audience ID'",
                    "6. Add to .env: MAILCHIMP_LIST_ID=your_list_id"
                ]
            },
            "Buffer": {
                "free": True,
                "description": "Social media scheduling (3 accounts free)",
                "get_key_url": "https://buffer.com/developers/apps",
                "env_var": "BUFFER_API_KEY",
                "instructions": [
                    "1. Go to Buffer → Settings → Apps & Extras",
                    "2. Click 'Developer App'",
                    "3. Create new app",
                    "4. Copy the 'Access Token'",
                    "5. Add to .env: BUFFER_API_KEY=your_token"
                ]
            },
            "Apollo": {
                "free": False,
                "paid": True,
                "description": "School database research (you have paid tier)",
                "get_key_url": "https://app.apollo.io/#/settings/integrations/api",
                "env_var": "APOLLO_API_KEY",
                "instructions": [
                    "1. Go to Apollo → Settings → Integrations → API",
                    "2. Copy your API key",
                    "3. Add to .env: APOLLO_API_KEY=your_key",
                    "Note: You have paid tier (1,000+ calls/month)"
                ]
            },
            "Canva": {
                "free": True,
                "description": "Design automation (free tier available)",
                "get_key_url": "https://www.canva.dev/",
                "env_var": "CANVA_API_KEY",
                "instructions": [
                    "1. Go to https://www.canva.dev/",
                    "2. Sign up for Developer Platform (free)",
                    "3. Create a new app",
                    "4. Get API key or OAuth token",
                    "5. Add to .env: CANVA_API_KEY=your_key",
                    "OR: CANVA_ACCESS_TOKEN=your_token",
                    "Note: Free tier available for developers"
                ]
            }
        }
    
    def create_env_example(self):
        """Create .env.example template"""
        template = """# BallCODE CES Launch - API Configuration
# Copy this file to .env and fill in your API keys

# HubSpot CRM (Free)
HUBSPOT_TOKEN=your_hubspot_token_here

# Mailchimp Email Marketing (Free - 500 contacts)
MAILCHIMP_API_KEY=your_mailchimp_key-us1
MAILCHIMP_LIST_ID=your_list_id_here

# Buffer Social Media (Free - 3 accounts)
BUFFER_API_KEY=your_buffer_token_here

# Apollo School Research (Paid - You have this)
APOLLO_API_KEY=your_apollo_key_here

# Canva Design Automation (Free tier available)
CANVA_API_KEY=your_canva_key_here
# OR use OAuth token:
# CANVA_ACCESS_TOKEN=your_canva_token_here

# Note: Never commit .env file to git (already in .gitignore)
"""
        
        ENV_EXAMPLE.parent.mkdir(parents=True, exist_ok=True)
        with open(ENV_EXAMPLE, 'w') as f:
            f.write(template)
        
        print(f"✅ Created .env.example template: {ENV_EXAMPLE}")
    
    def check_existing_env(self) -> Dict:
        """Check what's already in .env file"""
        existing = {}
        
        if ENV_FILE.exists():
            with open(ENV_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        existing[key] = value
        
        return existing
    
    def print_setup_guide(self):
        """Print comprehensive setup guide"""
        print("\n" + "=" * 70)
        print("🤖 Robot: API Setup Guide for CES Launch")
        print("=" * 70)
        
        existing = self.check_existing_env()
        
        print("\n📋 APIs to Configure:")
        print("=" * 70)
        
        for api_name, api_info in self.apis.items():
            free_status = "✅ FREE" if api_info.get("free") else "💰 PAID"
            env_vars = api_info.get("env_vars", [api_info.get("env_var")])
            
            # Check if configured
            configured = all(ev in existing for ev in env_vars if ev)
            
            status = "✅ Configured" if configured else "❌ Not Configured"
            optional_note = " (OPTIONAL)" if api_info.get("optional") else ""
            
            print(f"\n{api_name} ({free_status}){optional_note} - {status}")
            print(f"   Purpose: {api_info['description']}")
            print(f"   Get Key: {api_info['get_key_url']}")
            
            if not configured:
                print(f"\n   Setup Instructions:")
                for instruction in api_info['instructions']:
                    print(f"   {instruction}")
        
        print("\n" + "=" * 70)
        print("📝 Quick Setup Steps:")
        print("=" * 70)
        print("\n1. Copy .env.example to .env:")
        print("   cp .env.example .env")
        print("\n2. Edit .env file and add your API keys")
        print("\n3. Test all APIs:")
        print("   python scripts/test-api-integrations.py")
        print("\n4. Test Canva API:")
        print("   python scripts/canva-design-automation.py")
        print("\n5. Test Apollo API:")
        print("   python scripts/apollo-school-research.py")
        print("=" * 70)
    
    def create_env_file(self):
        """Create .env file from example if it doesn't exist"""
        if ENV_FILE.exists():
            print(f"✅ .env file already exists: {ENV_FILE}")
            print("   Review and update as needed")
            return
        
        if not ENV_EXAMPLE.exists():
            self.create_env_example()
        
        # Copy example to .env
        import shutil
        shutil.copy(ENV_EXAMPLE, ENV_FILE)
        print(f"✅ Created .env file from template: {ENV_FILE}")
        print("   Please edit .env and add your API keys")


def main():
    """Main function"""
    setup = APISetupGuide()
    
    # Create .env.example if needed
    if not ENV_EXAMPLE.exists():
        setup.create_env_example()
    
    # Print setup guide
    setup.print_setup_guide()
    
    # Create .env file if it doesn't exist
    if not ENV_FILE.exists():
        setup.create_env_file()
        print("\n✅ .env file created! Edit it and add your API keys.")
    else:
        print(f"\n✅ .env file exists: {ENV_FILE}")
        print("   Review and update API keys as needed")


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

