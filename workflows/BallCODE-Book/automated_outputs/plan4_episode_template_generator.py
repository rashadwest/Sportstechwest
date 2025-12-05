#!/usr/bin/env python3
"""
Plan 4: Episode Template Generator
Generates templates for Episodes 2-12 based on Episode 1 structure.
"""

import json
from pathlib import Path
from typing import Dict, List

def load_episode1_structure():
    """Load Episode 1 structure as template"""
    # This would load from episode1.json or similar
    return {
        "episode_number": 1,
        "title": "The Tip-off Trial",
        "premise": "Win first advantage by managing possession state from tip through transition.",
        "setting": "Data Court — Center Circle",
        "monster": "Shadow Press Scouts",
        "on_court_objective": "Clean transition into half-court without a turnover.",
        "coding_concept": "State (start/live/dead/outcome)",
        "math_concept": "Possession count, turnovers (basic stats)",
        "ai_mechanic": "Vision cue detects state shifts; player confirms.",
        "climax_challenge": "Maintain correct state across 3 linked actions.",
        "story_structure": {
            "act_i": "Meet the crew; tip-off chaos; possession changes feel like glitches.",
            "act_ii": "Shadow Press Scouts force turnovers; Nova tracks states.",
            "act_iii": "Controlled outlet → fill lanes → safe entry to set."
        },
        "exercises": [
            "Exercise A: Label states in a play",
            "Exercise B: Write state transitions",
            "Exercise C: Handle an edge case"
        ]
    }

def load_episode_premises():
    """Load episode premises from Story-Premises-For-12-Episodes.md"""
    # This would parse the markdown file
    # For now, return structure
    return {
        2: {
            "title": "The If/Then Fork in the Key",
            "coding_concept": "Conditionals",
            "math_concept": "Decision trees, probability",
            "ai_mechanic": "Opponent prediction"
        },
        3: {
            "title": "Loop of the Rotating Guardians",
            "coding_concept": "Loops",
            "math_concept": "Sequences, patterns",
            "ai_mechanic": "Pattern recognition"
        }
        # ... would continue for all 12 episodes
    }

def generate_episode_template(episode_num: int, episode_data: Dict) -> Dict:
    """Generate template for a specific episode"""
    template = {
        "episode_number": episode_num,
        "title": episode_data.get("title", f"Episode {episode_num}"),
        "premise": episode_data.get("premise", "TBD"),
        "setting": episode_data.get("setting", "Data Court"),
        "monster": episode_data.get("monster", "TBD"),
        "on_court_objective": episode_data.get("on_court_objective", "TBD"),
        "coding_concept": episode_data.get("coding_concept", "TBD"),
        "math_concept": episode_data.get("math_concept", "TBD"),
        "ai_mechanic": episode_data.get("ai_mechanic", "TBD"),
        "climax_challenge": episode_data.get("climax_challenge", "TBD"),
        "story_structure": {
            "act_i": "TBD",
            "act_ii": "TBD",
            "act_iii": "TBD"
        },
        "exercises": [
            "Exercise A: TBD",
            "Exercise B: TBD",
            "Exercise C: TBD"
        ],
        "status": "template_created",
        "completion": 0
    }
    return template

def generate_all_templates():
    """Generate templates for Episodes 2-12"""
    episode1 = load_episode1_structure()
    premises = load_episode_premises()
    
    templates = {}
    
    for episode_num in range(2, 13):
        episode_data = premises.get(episode_num, {})
        template = generate_episode_template(episode_num, episode_data)
        templates[episode_num] = template
    
    return templates

def save_templates(templates: Dict):
    """Save templates to JSON file"""
    output_file = Path(__file__).parent / "episodes_2-12_templates.json"
    
    with open(output_file, 'w') as f:
        json.dump(templates, f, indent=2)
    
    return output_file

def main():
    """Main execution"""
    print("📚 Plan 4: Episode Template Generator")
    print("=" * 60)
    
    print("\nGenerating templates for Episodes 2-12...")
    templates = generate_all_templates()
    
    output_file = save_templates(templates)
    
    print(f"\n✅ Generated {len(templates)} episode templates")
    print(f"📁 Saved to: {output_file}")
    
    print("\nTemplates include:")
    print("- Episode structure (based on Episode 1)")
    print("- Placeholders for all required fields")
    print("- Ready for content creation")
    
    print("\n" + "=" * 60)
    print("✅ Template generation complete!")
    print("\nNext steps:")
    print("1. Review templates")
    print("2. Fill in episode-specific content")
    print("3. Use Episode 1 as reference for structure")

if __name__ == "__main__":
    main()




