#!/usr/bin/env python3
"""
Robot: Expand School Database for CES Launch
Automates school database expansion from 2 to 100+ schools

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
SCHOOL_DB_PATH = PROJECT_ROOT / "documents" / "school-contacts-database.json"
TEMPLATE_SCHOOLS_PATH = PROJECT_ROOT / "documents" / "school-database-template.json"

class SchoolDatabaseExpander:
    """Robot to expand school database for CES launch"""
    
    def __init__(self):
        self.school_db = self.load_database()
        self.target_count = 100
        self.current_count = len(self.school_db.get('schools', []))
        self.gap = self.target_count - self.current_count
    
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
    
    def generate_school_id(self) -> str:
        """Generate next school ID"""
        current_count = len(self.school_db.get('schools', []))
        return f"school_{current_count + 1:03d}"
    
    def validate_school_data(self, school_data: Dict) -> tuple[bool, List[str]]:
        """Validate school data structure"""
        errors = []
        required_fields = ['name', 'state', 'grades']
        
        for field in required_fields:
            if not school_data.get(field):
                errors.append(f"Missing required field: {field}")
        
        # Validate grades format
        grades = school_data.get('grades', '')
        if grades and not any(char.isdigit() for char in grades):
            errors.append("Grades must include grade levels (e.g., '3-8', '6-12')")
        
        # Validate state (2-letter code)
        state = school_data.get('state', '')
        if state and len(state) != 2:
            errors.append("State must be 2-letter code (e.g., 'NC', 'CA')")
        
        return len(errors) == 0, errors
    
    def add_school(self, school_data: Dict, validate: bool = True) -> tuple[bool, str]:
        """Add a school to the database"""
        if validate:
            is_valid, errors = self.validate_school_data(school_data)
            if not is_valid:
                return False, f"Validation errors: {', '.join(errors)}"
        
        # Set defaults
        school_data['id'] = self.generate_school_id()
        school_data.setdefault('status', 'not_contacted')
        school_data.setdefault('priority', 'medium')
        school_data.setdefault('pilot_committed', False)
        school_data.setdefault('basketball_programs', True)
        school_data.setdefault('stem_programs', ['Science', 'Math', 'Technology'])
        school_data.setdefault('date_contacted', None)
        school_data.setdefault('response_status', None)
        school_data.setdefault('call_scheduled', None)
        
        if 'schools' not in self.school_db:
            self.school_db['schools'] = []
        
        self.school_db['schools'].append(school_data)
        return True, school_data['id']
    
    def add_schools_batch(self, schools: List[Dict]) -> Dict:
        """Add multiple schools at once"""
        results = {
            'success': 0,
            'failed': 0,
            'errors': []
        }
        
        for school in schools:
            success, message = self.add_school(school)
            if success:
                results['success'] += 1
            else:
                results['failed'] += 1
                results['errors'].append({
                    'school': school.get('name', 'Unknown'),
                    'error': message
                })
        
        if results['success'] > 0:
            self.save_database()
        
        return results
    
    def generate_template_schools(self, count: int = 20) -> List[Dict]:
        """Generate template schools for manual completion"""
        template_schools = []
        
        # Sample states with strong STEM programs
        states = ['NC', 'CA', 'TX', 'NY', 'FL', 'IL', 'MA', 'VA', 'GA', 'WA']
        
        # Sample school name patterns
        name_patterns = [
            "{city} STEM Academy",
            "{city} Science & Math School",
            "{city} Innovation Academy",
            "{city} Technology School",
            "{city} STEM Charter School"
        ]
        
        cities = [
            'Raleigh', 'Durham', 'Charlotte', 'Greensboro', 'Winston-Salem',
            'Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'Oakland',
            'Houston', 'Dallas', 'Austin', 'San Antonio', 'Fort Worth',
            'New York', 'Buffalo', 'Rochester', 'Albany', 'Syracuse'
        ]
        
        for i in range(count):
            state = states[i % len(states)]
            city = cities[i % len(cities)]
            name_pattern = name_patterns[i % len(name_patterns)]
            
            school = {
                'name': name_pattern.format(city=city),
                'district': f"{city} School District",
                'state': state,
                'contact_name': '',  # To be filled
                'contact_title': 'Principal/STEM Coordinator',
                'email': '',  # To be filled
                'phone': '',  # To be filled
                'grades': '3-8',
                'student_count': '',
                'stem_programs': ['Science', 'Math', 'Technology', 'Computer Science'],
                'basketball_programs': True,
                'priority': 'high' if i < 10 else 'medium',
                'status': 'not_contacted',
                'notes': f'Template school #{i+1} - Research contact information'
            }
            template_schools.append(school)
        
        return template_schools
    
    def create_research_template(self, count: int = 50):
        """Create a template file for manual research"""
        template_schools = self.generate_template_schools(count)
        
        research_data = {
            'metadata': {
                'created': datetime.now().isoformat(),
                'purpose': 'Template for manual school research',
                'instructions': [
                    '1. Research each school to find contact information',
                    '2. Verify grades 3-8, STEM programs, and basketball programs',
                    '3. Fill in contact_name, email, phone fields',
                    '4. Use add_schools_batch() to import completed schools',
                    '5. Or manually add to school-contacts-database.json'
                ]
            },
            'template_schools': template_schools
        }
        
        TEMPLATE_SCHOOLS_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(TEMPLATE_SCHOOLS_PATH, 'w') as f:
            json.dump(research_data, f, indent=2)
        
        print(f"✅ Research template created: {TEMPLATE_SCHOOLS_PATH}")
        print(f"   {count} template schools ready for research")
        return TEMPLATE_SCHOOLS_PATH
    
    def import_from_template(self):
        """Import schools from research template"""
        if not TEMPLATE_SCHOOLS_PATH.exists():
            print(f"❌ Template file not found: {TEMPLATE_SCHOOLS_PATH}")
            print("   Run with --create-template first")
            return False
        
        with open(TEMPLATE_SCHOOLS_PATH, 'r') as f:
            template_data = json.load(f)
        
        template_schools = template_data.get('template_schools', [])
        
        # Filter to only schools with contact information
        completed_schools = [
            s for s in template_schools
            if s.get('email') or s.get('contact_name')
        ]
        
        if not completed_schools:
            print("⚠️  No completed schools found in template")
            print("   Schools need at least email or contact_name to import")
            return False
        
        results = self.add_schools_batch(completed_schools)
        
        print(f"\n📊 Import Results:")
        print(f"   ✅ Successfully added: {results['success']}")
        print(f"   ❌ Failed: {results['failed']}")
        
        if results['errors']:
            print(f"\n⚠️  Errors:")
            for error in results['errors'][:5]:  # Show first 5
                print(f"   - {error['school']}: {error['error']}")
        
        return results['success'] > 0
    
    def get_status(self) -> Dict:
        """Get current database status"""
        schools = self.school_db.get('schools', [])
        
        return {
            'current_count': len(schools),
            'target_count': self.target_count,
            'gap': self.gap,
            'completion_percent': (len(schools) / self.target_count * 100) if self.target_count > 0 else 0,
            'by_status': self._count_by_status(),
            'by_priority': self._count_by_priority(),
            'with_contact_info': len([s for s in schools if s.get('email') or s.get('contact_name')])
        }
    
    def _count_by_status(self) -> Dict:
        """Count schools by status"""
        schools = self.school_db.get('schools', [])
        counts = {}
        for school in schools:
            status = school.get('status', 'unknown')
            counts[status] = counts.get(status, 0) + 1
        return counts
    
    def _count_by_priority(self) -> Dict:
        """Count schools by priority"""
        schools = self.school_db.get('schools', [])
        counts = {}
        for school in schools:
            priority = school.get('priority', 'unknown')
            counts[priority] = counts.get(priority, 0) + 1
        return counts
    
    def print_status(self):
        """Print current status"""
        status = self.get_status()
        
        print("\n" + "=" * 70)
        print("📊 School Database Status")
        print("=" * 70)
        print(f"Current Schools: {status['current_count']}")
        print(f"Target: {status['target_count']}")
        print(f"Gap: {status['gap']} schools needed")
        print(f"Completion: {status['completion_percent']:.1f}%")
        print(f"With Contact Info: {status['with_contact_info']}")
        
        print(f"\nBy Status:")
        for stat, count in status['by_status'].items():
            print(f"  {stat}: {count}")
        
        print(f"\nBy Priority:")
        for priority, count in status['by_priority'].items():
            print(f"  {priority}: {count}")
        print("=" * 70)


def main():
    """CLI interface"""
    expander = SchoolDatabaseExpander()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python expand-school-database.py status              # Show current status")
        print("  python expand-school-database.py create-template [N] # Create research template (default: 50)")
        print("  python expand-school-database.py import              # Import from template")
        print("  python expand-school-database.py add <json_file>     # Add schools from JSON file")
        return
    
    command = sys.argv[1]
    
    if command == "status":
        expander.print_status()
    
    elif command == "create-template":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        print(f"\n🤖 Creating research template with {count} schools...")
        expander.create_research_template(count)
        print("\n✅ Next steps:")
        print("   1. Research each school to find contact information")
        print("   2. Fill in email, contact_name, phone fields")
        print("   3. Run: python expand-school-database.py import")
    
    elif command == "import":
        print("\n🤖 Importing schools from template...")
        expander.import_from_template()
        expander.print_status()
    
    elif command == "add":
        if len(sys.argv) < 3:
            print("❌ Please provide JSON file path")
            return
        
        json_file = Path(sys.argv[2])
        if not json_file.exists():
            print(f"❌ File not found: {json_file}")
            return
        
        with open(json_file, 'r') as f:
            schools_data = json.load(f)
        
        if isinstance(schools_data, list):
            schools = schools_data
        elif isinstance(schools_data, dict) and 'schools' in schools_data:
            schools = schools_data['schools']
        else:
            print("❌ Invalid JSON format. Expected list of schools or {'schools': [...]}")
            return
        
        print(f"\n🤖 Adding {len(schools)} schools...")
        results = expander.add_schools_batch(schools)
        print(f"\n✅ Added {results['success']} schools")
        if results['failed'] > 0:
            print(f"❌ Failed: {results['failed']}")
        expander.print_status()
    
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()


