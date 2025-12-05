#!/usr/bin/env python3
"""
AIMCODE Story Validator
Automated validation of stories against AIMCODE framework
"""

import sys
import json
import argparse
from pathlib import Path
from aimcode_validators import AIMCODEValidator


def validate_story(story_path: str, outline_path: str = None, episode_number: int = None):
    """Validate a story file against AIMCODE framework"""
    
    # Read story content
    story_file = Path(story_path)
    if not story_file.exists():
        print(f"❌ Error: Story file not found: {story_path}")
        return None
    
    story_content = story_file.read_text(encoding='utf-8')
    
    # Initialize validator
    validator = AIMCODEValidator()
    
    # Validate story
    print(f"🔍 Validating story: {story_path}")
    print(f"📊 Episode: {episode_number or 'Unknown'}")
    print("-" * 60)
    
    results = validator.validate_all(story_content, episode_number)
    
    # Print results
    print(f"\n{'='*60}")
    print(f"AIMCODE Validation Results")
    print(f"{'='*60}\n")
    
    print(f"Overall Status: {'✅ PASSED' if results['passed'] else '❌ NEEDS WORK'}")
    print(f"Overall Score: {results['overall_score']:.1%}\n")
    
    for pillar_name, pillar_result in results['results'].items():
        status = "✅" if pillar_result['passed'] else "❌"
        print(f"{status} {pillar_result['pillar']}: {pillar_result['score']:.1%}")
        
        for feedback in pillar_result['feedback']:
            print(f"   {feedback}")
        print()
    
    print(f"Summary: {results['summary']}\n")
    
    # Save results to JSON
    output_file = story_file.parent / f"{story_file.stem}-validation.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"📄 Detailed results saved to: {output_file}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Validate story against AIMCODE framework')
    parser.add_argument('--story', required=True, help='Path to story file')
    parser.add_argument('--outline', help='Path to outline file (optional)')
    parser.add_argument('--episode', type=int, help='Episode number')
    
    args = parser.parse_args()
    
    # Extract episode number from story filename if not provided
    episode_number = args.episode
    if not episode_number:
        # Try to extract from filename (e.g., "book-1-story.md" -> 1)
        import re
        match = re.search(r'book-(\d+)', args.story)
        if match:
            episode_number = int(match.group(1))
    
    results = validate_story(args.story, args.outline, episode_number)
    
    # Exit with error code if validation failed
    if results and not results['passed']:
        sys.exit(1)
    elif results:
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == '__main__':
    main()



