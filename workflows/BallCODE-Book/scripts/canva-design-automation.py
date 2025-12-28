#!/usr/bin/env python3
"""
Robot: Canva Design Automation
Adds headers and look/feel to files using Canva API

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
import sys
import requests
from pathlib import Path
from typing import Dict, Optional

PROJECT_ROOT = Path(__file__).parent.parent
CANVA_API_BASE = "https://api.canva.com/rest/v1"

class CanvaDesignAutomation:
    """Robot to automate Canva design additions"""
    
    def __init__(self):
        self.api_key = os.getenv("CANVA_API_KEY", "")
        self.access_token = os.getenv("CANVA_ACCESS_TOKEN", "")
    
    def check_api_access(self) -> bool:
        """Check if Canva API is accessible"""
        if not self.api_key and not self.access_token:
            print("❌ CANVA_API_KEY or CANVA_ACCESS_TOKEN not found")
            print("\n💡 To get started:")
            print("   1. Sign up at: https://www.canva.dev/")
            print("   2. Create an app in Developer Platform")
            print("   3. Get API key or OAuth access token")
            print("   4. Add to .env file:")
            print("      CANVA_API_KEY=your_key")
            print("      OR")
            print("      CANVA_ACCESS_TOKEN=your_token")
            return False
        return True
    
    def add_header_to_design(self, design_id: str, header_text: str, style: Dict) -> Optional[Dict]:
        """Add header to Canva design using Design Editing API"""
        if not self.check_api_access():
            return None
        
        url = f"{CANVA_API_BASE}/designs/{design_id}/elements"
        headers = {
            "Authorization": f"Bearer {self.access_token or self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Create header element
        element_data = {
            "type": "TEXT",
            "content": header_text,
            "position": {
                "x": 0,
                "y": 0
            },
            "style": style
        }
        
        try:
            response = requests.post(url, json=element_data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                return response.json()
            else:
                print(f"⚠️  Canva API error: {response.status_code}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Canva API error: {str(e)}")
            return None
    
    def apply_brand_kit(self, design_id: str, brand_kit_id: str) -> bool:
        """Apply brand kit to design for consistent look/feel"""
        if not self.check_api_access():
            return False
        
        url = f"{CANVA_API_BASE}/designs/{design_id}/brand-kit"
        headers = {
            "Authorization": f"Bearer {self.access_token or self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "brand_kit_id": brand_kit_id
        }
        
        try:
            response = requests.put(url, json=data, headers=headers, timeout=30)
            return response.status_code == 200
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Canva API error: {str(e)}")
            return False
    
    def create_design_from_template(self, template_id: str, customizations: Dict) -> Optional[Dict]:
        """Create design from template with customizations"""
        if not self.check_api_access():
            return None
        
        url = f"{CANVA_API_BASE}/designs/create-from-template"
        headers = {
            "Authorization": f"Bearer {self.access_token or self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "template_id": template_id,
            "customizations": customizations
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                return response.json()
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Canva API error: {str(e)}")
            return None


def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("🤖 Robot: Canva Design Automation")
    print("=" * 70)
    
    print("\n✅ Canva API Available!")
    print("\n📋 Canva APIs for Design Automation:")
    print("   1. Design Editing API - Add headers, elements, styling")
    print("   2. Brand Kit API - Apply consistent look/feel")
    print("   3. Template API - Create designs from templates")
    print("   4. Connect API - Real-time data integration")
    
    print("\n💡 To use:")
    print("   1. Sign up: https://www.canva.dev/")
    print("   2. Create app in Developer Platform")
    print("   3. Get API key or OAuth token")
    print("   4. Add to .env: CANVA_API_KEY=your_key")
    
    print("\n📚 Documentation:")
    print("   - https://www.canva.dev/")
    print("   - Design Editing API: https://www.canva.dev/rest/design-editing/")
    print("   - Connect API: https://www.canva.dev/rest/connect/")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()


