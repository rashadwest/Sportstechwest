#!/usr/bin/env python3
"""
Generate School Onboarding Package
Garvis - BallCODE Fully Integrated System

Purpose: Automatically generate complete onboarding package for schools
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict

WORKFLOW_DIR = Path(__file__).parent.parent

def generate_school_package(school_data: Dict, credentials: Dict) -> Dict:
    """Generate complete onboarding package for a school"""
    
    package = {
        'school_id': school_data.get('school_id', f"school-{datetime.now().timestamp()}"),
        'school_name': school_data.get('school_name', ''),
        'generated_at': datetime.now().isoformat(),
        'package_contents': {}
    }
    
    # 1. Episode 1 Story
    episode1_path = WORKFLOW_DIR / "Episode-1-For-Pilot-School.md"
    if episode1_path.exists():
        package['package_contents']['episode1_story'] = {
            'file': str(episode1_path),
            'format': 'Markdown',
            'ready': True
        }
    else:
        package['package_contents']['episode1_story'] = {
            'file': None,
            'format': 'Markdown',
            'ready': False,
            'note': 'Episode 1 file not found'
        }
    
    # 2. Teacher Guide
    teacher_guide_path = WORKFLOW_DIR / "Episode-1-Teacher-Guide.md"
    if teacher_guide_path.exists():
        package['package_contents']['teacher_guide'] = {
            'file': str(teacher_guide_path),
            'format': 'Markdown',
            'ready': True
        }
    else:
        # Try alternative location
        alt_path = WORKFLOW_DIR / "documents" / "teacher-resources" / "Teacher-Onboarding-Guide.md"
        if alt_path.exists():
            package['package_contents']['teacher_guide'] = {
                'file': str(alt_path),
                'format': 'Markdown',
                'ready': True
            }
        else:
            package['package_contents']['teacher_guide'] = {
                'file': None,
                'format': 'Markdown',
                'ready': False,
                'note': 'Teacher guide not found'
            }
    
    # 3. Onboarding Guide
    onboarding_path = WORKFLOW_DIR / "Pilot-School-Onboarding-Guide.md"
    if onboarding_path.exists():
        package['package_contents']['onboarding_guide'] = {
            'file': str(onboarding_path),
            'format': 'Markdown',
            'ready': True
        }
    else:
        package['package_contents']['onboarding_guide'] = {
            'file': None,
            'format': 'Markdown',
            'ready': False,
            'note': 'Onboarding guide not found'
        }
    
    # 4. Access Credentials
    package['package_contents']['access_credentials'] = {
        'access_code': credentials.get('accessCode', ''),
        'password': credentials.get('password', ''),
        'expires_at': credentials.get('expiresAt', ''),
        'game_url': f"https://ballcode.co/game?access={credentials.get('accessCode', '')}",
        'ready': True
    }
    
    # 5. Support Resources
    package['package_contents']['support_resources'] = {
        'email': 'support@ballcode.co',
        'faq_url': 'https://ballcode.co/faq',
        'ready': True
    }
    
    # Calculate package completeness
    ready_items = sum(1 for item in package['package_contents'].values() if item.get('ready', False))
    total_items = len(package['package_contents'])
    package['completeness'] = (ready_items / total_items * 100) if total_items > 0 else 0
    
    return package

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate-school-package.py <school_data_json>")
        print("Example:")
        print('  python scripts/generate-school-package.py \'{"school_name": "ABC Elementary", "email": "contact@school.edu"}\'')
        sys.exit(1)
    
    try:
        school_data = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        # Try reading from file
        file_path = Path(sys.argv[1])
        if file_path.exists():
            school_data = json.loads(file_path.read_text())
        else:
            print(f"Error: Invalid JSON or file not found: {sys.argv[1]}")
            sys.exit(1)
    
    # Generate credentials
    import uuid
    credentials = {
        'accessCode': f"BC-{uuid.uuid4().hex[:8].upper()}",
        'password': f"{uuid.uuid4().hex[:12]}",
        'expiresAt': (datetime.now().timestamp() + 90 * 24 * 60 * 60).isoformat()
    }
    
    package = generate_school_package(school_data, credentials)
    
    print(json.dumps(package, indent=2))

if __name__ == "__main__":
    main()

