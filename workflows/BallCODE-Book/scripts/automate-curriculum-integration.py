#!/usr/bin/env python3
"""
Automate Curriculum Integration
Adds curriculum information to Book 1 page and integrates with measurement system

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"
CURRICULUM_DATA = WEBSITE_DIR / "data" / "curriculum-data.json"
CURRICULUM_SCHEMA = PROJECT_ROOT / "curriculum-schema.json"

def load_curriculum_data():
    """Load curriculum data for Book 1."""
    # Try curriculum-data.json first
    if CURRICULUM_DATA.exists():
        with open(CURRICULUM_DATA, 'r') as f:
            data = json.load(f)
            if 'books' in data and len(data['books']) > 0:
                return data['books'][0]
    
    # Fallback to curriculum-schema.json
    if CURRICULUM_SCHEMA.exists():
        with open(CURRICULUM_SCHEMA, 'r') as f:
            data = json.load(f)
            if 'books' in data and len(data['books']) > 0:
                return data['books'][0]
    
    # Default curriculum data
    return {
        "id": 1,
        "title": "The Foundation Block",
        "curriculum": {
            "gradeLevels": ["3-5", "6-8", "9-12"],
            "standards": {
                "csta": ["1B-AP-10", "1B-AP-11"],
                "commonCore": ["MP.2", "MP.7"],
                "ngss": ["ETS1-2"]
            },
            "learningObjectives": [
                "Understand that code is step-by-step instructions",
                "Create sequences using visual blocks",
                "See connection between blocks and Python code",
                "Write basic Python sequences"
            ]
        },
        "concepts": {
            "python": "Sequences",
            "pythonSyntax": "Sequential code execution",
            "aiConcept": "Step-by-step reasoning",
            "mathConcept": "Order of operations"
        },
        "basketball": {
            "skill": "Pound Dribble",
            "level": 1
        }
    }

def create_curriculum_section(curriculum_data):
    """Create HTML for curriculum section."""
    curriculum = curriculum_data.get('curriculum', {})
    concepts = curriculum_data.get('concepts', {})
    basketball = curriculum_data.get('basketball', {})
    
    learning_objectives = curriculum.get('learningObjectives', [])
    standards = curriculum.get('standards', {})
    grade_levels = curriculum.get('gradeLevels', [])
    
    html = f'''
        <section id="curriculum-section" class="curriculum-section" style="background: #f8f9fa; padding: 2rem; border-radius: 8px; margin: 3rem 0;">
            <h2 style="color: #0C72B3; margin-bottom: 1.5rem;">📚 What You're Learning</h2>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #333; margin-bottom: 1rem;">Learning Objectives</h3>
                <ul style="list-style: none; padding: 0;">
'''
    
    for obj in learning_objectives:
        html += f'                    <li style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative;">'
        html += f'<span style="position: absolute; left: 0;">✅</span> {obj}</li>\n'
    
    html += '''                </ul>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #333; margin-bottom: 1rem;">Concepts You'll Master</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
'''
    
    if concepts.get('python'):
        html += f'                    <span style="background: #0C72B3; color: white; padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.9rem;">Python: {concepts["python"]}</span>\n'
    if concepts.get('mathConcept'):
        html += f'                    <span style="background: #eb6123; color: white; padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.9rem;">Math: {concepts["mathConcept"]}</span>\n'
    if concepts.get('aiConcept'):
        html += f'                    <span style="background: #4a90e2; color: white; padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.9rem;">AI: {concepts["aiConcept"]}</span>\n'
    if basketball.get('skill'):
        html += f'                    <span style="background: #28a745; color: white; padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.9rem;">Basketball: {basketball["skill"]}</span>\n'
    
    html += '''                </div>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #333; margin-bottom: 1rem;">Standards Alignment</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
'''
    
    if standards.get('csta'):
        html += '                    <div style="background: white; padding: 1rem; border-radius: 4px; border-left: 4px solid #0C72B3;">\n'
        html += '                        <strong style="color: #0C72B3;">CSTA Standards</strong>\n'
        html += '                        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.5rem; font-size: 0.9rem;">\n'
        for std in standards['csta']:
            html += f'                            <li>{std}</li>\n'
        html += '                        </ul>\n                    </div>\n'
    
    if standards.get('commonCore'):
        html += '                    <div style="background: white; padding: 1rem; border-radius: 4px; border-left: 4px solid #eb6123;">\n'
        html += '                        <strong style="color: #eb6123;">Common Core</strong>\n'
        html += '                        <ul style="margin: 0.5rem 0 0 0; padding-left: 1.5rem; font-size: 0.9rem;">\n'
        for std in standards['commonCore']:
            html += f'                            <li>{std}</li>\n'
        html += '                        </ul>\n                    </div>\n'
    
    if grade_levels:
        html += '                    <div style="background: white; padding: 1rem; border-radius: 4px; border-left: 4px solid #28a745;">\n'
        html += '                        <strong style="color: #28a745;">Grade Levels</strong>\n'
        html += '                        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">' + ', '.join(grade_levels) + '</p>\n'
        html += '                    </div>\n'
    
    html += '''                </div>
            </div>
        </section>
'''
    
    return html

def add_curriculum_to_book1(curriculum_data):
    """Add curriculum section to Book 1 page."""
    if not BOOK1_HTML.exists():
        print(f"❌ Book 1 page not found: {BOOK1_HTML}")
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if curriculum section already exists
    if 'curriculum-section' in content or 'What You\'re Learning' in content:
        print("⚠️  Curriculum section already exists in Book 1")
        # Update it instead
        curriculum_html = create_curriculum_section(curriculum_data)
        
        # Try to replace existing section
        pattern = r'(<section[^>]*id="curriculum-section"[^>]*>.*?</section>)'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, curriculum_html.strip(), content, flags=re.DOTALL)
            print("✅ Updated existing curriculum section")
        else:
            print("⚠️  Could not find existing section to update")
            return False
    else:
        # Add new curriculum section
        curriculum_html = create_curriculum_section(curriculum_data)
        
        # Insert after "About This Book" section or before exercise section
        insertion_points = [
            (r'(<h2>Watch the Story</h2>)', curriculum_html + r'\n            \1'),
            (r'(<div class="exercise-section">)', curriculum_html + r'\n        \1'),
            (r'(<h2>About This Book</h2>.*?</p>)', r'\1' + curriculum_html),
        ]
        
        added = False
        for pattern, replacement in insertion_points:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                added = True
                print(f"✅ Added curriculum section to Book 1")
                break
        
        if not added:
            # Add before closing </div> of book-content
            if '<div class="book-content">' in content:
                content = content.replace(
                    '</div>', 
                    curriculum_html + '\n        </div>',
                    1
                )
                added = True
                print("✅ Added curriculum section to Book 1 (fallback)")
    
    if added or 'curriculum-section' in content:
        with open(BOOK1_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print("⚠️  Could not find insertion point")
        return False

def integrate_with_measurement():
    """Add curriculum tracking to measurement system."""
    measurement_data = PROJECT_ROOT / "measurement-data.json"
    
    if not measurement_data.exists():
        print("⚠️  Measurement data file not found")
        return False
    
    with open(measurement_data, 'r') as f:
        data = json.load(f)
    
    # Add curriculum tracking to effectiveness metrics
    if 'effectiveness' not in data:
        data['effectiveness'] = {}
    
    if 'learning_objectives' not in data['effectiveness']:
        data['effectiveness']['learning_objectives'] = {
            "objective_achievement_rate": 0.0,
            "concept_mastery": 0.0,
            "progress_tracking": 0.0
        }
    
    with open(measurement_data, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✅ Integrated curriculum with measurement system")
    return True

def main():
    """Main function."""
    print("=" * 60)
    print("📚 BallCODE Curriculum Integration Automation")
    print("=" * 60)
    print()
    
    # Load curriculum data
    print("📖 Loading curriculum data...")
    curriculum_data = load_curriculum_data()
    print(f"✅ Loaded curriculum for: {curriculum_data.get('title', 'Book 1')}")
    print()
    
    # Add curriculum to Book 1
    print("📝 Adding curriculum section to Book 1...")
    if add_curriculum_to_book1(curriculum_data):
        print("✅ Curriculum section added to Book 1")
    else:
        print("⚠️  Could not add curriculum section")
    print()
    
    # Integrate with measurement
    print("📊 Integrating with measurement system...")
    integrate_with_measurement()
    print()
    
    print("=" * 60)
    print("✅ Curriculum Integration Complete!")
    print("=" * 60)
    print()
    
    print("🚀 Next Steps:")
    print("  1. Review Book 1 page to see curriculum section")
    print("  2. Test curriculum display on website")
    print("  3. Run measurement-dashboard.py to see curriculum metrics")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


