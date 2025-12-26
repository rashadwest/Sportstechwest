#!/usr/bin/env python3
"""
Use Game Screenshots for Visual Assets
Helps select and copy game screenshots to use as visual assets

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import shutil
from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).parent.parent
SCREENSHOTS_DIR = Path("/Users/rashadwest/Desktop/BallCODE screenshots")
ASSETS_DIR = PROJECT_ROOT / "BallCode" / "assets" / "images"

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}{text:^70}{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def list_screenshots():
    """List available screenshots."""
    if not SCREENSHOTS_DIR.exists():
        print_error(f"Screenshots folder not found: {SCREENSHOTS_DIR}")
        return []
    
    screenshots = list(SCREENSHOTS_DIR.glob("*.png"))
    screenshots += list(SCREENSHOTS_DIR.glob("*.jpg"))
    screenshots += list(SCREENSHOTS_DIR.glob("*.PNG"))
    screenshots += list(SCREENSHOTS_DIR.glob("*.JPG"))
    
    return sorted(screenshots)

def show_screenshot_suggestions():
    """Show which screenshots to use for each visual asset."""
    print_header("GAME SCREENSHOTS FOR VISUAL ASSETS")
    
    screenshots = list_screenshots()
    
    if not screenshots:
        print_error("No screenshots found!")
        return
    
    print_info(f"Found {len(screenshots)} screenshots in: {SCREENSHOTS_DIR}")
    print()
    
    # Court Map suggestions
    print(f"{BLUE}1. COURT MAP VISUAL{NC}")
    print("   Looking for: Basketball court showing center circle")
    print()
    court_suggestions = [s for s in screenshots if any(term in s.name.lower() for term in ['main menu', 'tutorial', 'court', 'gameplay'])]
    if court_suggestions:
        print("   Suggested screenshots:")
        for i, screenshot in enumerate(court_suggestions[:5], 1):
            print(f"   {i}. {screenshot.name}")
    print()
    
    # Shadow Press Scouts suggestions
    print(f"{BLUE}2. SHADOW PRESS SCOUTS CHARACTER ART{NC}")
    print("   Looking for: Game characters/robots (the 'villains')")
    print()
    character_suggestions = [s for s in screenshots if any(term in s.name.lower() for term in ['tutorial', 'gameplay', 'coding', 'mathlete'])]
    if character_suggestions:
        print("   Suggested screenshots:")
        for i, screenshot in enumerate(character_suggestions[:5], 1):
            print(f"   {i}. {screenshot.name}")
    print()
    
    # State Diagram suggestions
    print(f"{BLUE}3. STATE DIAGRAM VISUALIZATION{NC}")
    print("   Looking for: Coding interface or game state visualization")
    print()
    diagram_suggestions = [s for s in screenshots if any(term in s.name.lower() for term in ['coding', 'tutorial', 'gameplay'])]
    if diagram_suggestions:
        print("   Suggested screenshots:")
        for i, screenshot in enumerate(diagram_suggestions[:5], 1):
            print(f"   {i}. {screenshot.name}")
    print()
    
    print("=" * 70)
    print()
    print_info("All available screenshots:")
    for i, screenshot in enumerate(screenshots, 1):
        print(f"   {i:2d}. {screenshot.name}")

def copy_screenshot(source_file, target_name):
    """Copy screenshot to assets folder with new name."""
    if not source_file.exists():
        print_error(f"Source file not found: {source_file}")
        return False
    
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    target_path = ASSETS_DIR / target_name
    
    try:
        shutil.copy2(source_file, target_path)
        print_success(f"Copied: {source_file.name} → {target_name}")
        return True
    except Exception as e:
        print_error(f"Failed to copy: {e}")
        return False

def interactive_selection():
    """Interactive selection of screenshots."""
    screenshots = list_screenshots()
    
    if not screenshots:
        print_error("No screenshots found!")
        return
    
    print_header("SELECT SCREENSHOTS FOR VISUAL ASSETS")
    
    # Show all screenshots
    print("Available screenshots:")
    for i, screenshot in enumerate(screenshots, 1):
        print(f"  {i:2d}. {screenshot.name}")
    
    print()
    print("Enter screenshot numbers (or 'q' to quit):")
    print()
    
    # Court Map
    court_input = input("Court Map (enter number): ").strip()
    if court_input.lower() == 'q':
        return
    
    # Shadow Press Scouts
    scouts_input = input("Shadow Press Scouts (enter number): ").strip()
    if scouts_input.lower() == 'q':
        return
    
    # State Diagram
    diagram_input = input("State Diagram (enter number, or 'skip'): ").strip()
    if diagram_input.lower() == 'q':
        return
    
    # Copy screenshots
    results = {}
    
    if court_input.isdigit():
        idx = int(court_input) - 1
        if 0 <= idx < len(screenshots):
            results['court'] = copy_screenshot(screenshots[idx], "episode1-court-map-v1.png")
    
    if scouts_input.isdigit():
        idx = int(scouts_input) - 1
        if 0 <= idx < len(screenshots):
            results['scouts'] = copy_screenshot(screenshots[idx], "episode1-shadow-press-scouts-v1.png")
    
    if diagram_input.isdigit():
        idx = int(diagram_input) - 1
        if 0 <= idx < len(screenshots):
            results['diagram'] = copy_screenshot(screenshots[idx], "episode1-state-diagram-v1.png")
    
    # Summary
    print()
    print_header("COPY RESULTS")
    for key, success in results.items():
        if success:
            print_success(f"{key}: Copied successfully")
        else:
            print_error(f"{key}: Failed to copy")
    
    if all(results.values()):
        print()
        print_success("All screenshots copied! Now run: python3 scripts/add-visuals-to-book1.py")

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Use game screenshots for visual assets')
    parser.add_argument('--list', action='store_true', help='List available screenshots')
    parser.add_argument('--suggestions', action='store_true', help='Show screenshot suggestions')
    parser.add_argument('--interactive', action='store_true', help='Interactive selection')
    
    args = parser.parse_args()
    
    if args.list or args.suggestions:
        show_screenshot_suggestions()
    elif args.interactive:
        interactive_selection()
    else:
        # Default: show suggestions
        show_screenshot_suggestions()
        print()
        print_info("To select screenshots interactively, run:")
        print_info("  python3 scripts/use-game-screenshots-for-visuals.py --interactive")

if __name__ == "__main__":
    main()

