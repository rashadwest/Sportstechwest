#!/usr/bin/env python3
"""
Select Game Screenshots for Visual Assets

This script helps you select and copy the right game screenshots
to use as visual assets for Book 1.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import shutil
from pathlib import Path

# Paths
SCREENSHOTS_DIR = Path("/Users/rashadwest/Desktop/BallCODE screenshots")
ASSETS_DIR = Path("BallCode/assets/images")
OUTPUT_NAMES = {
    "court_map": "episode1-court-map-v1.png",
    "shadow_press_scouts": "episode1-shadow-press-scouts-v1.png",
    "state_diagram": "episode1-state-diagram-v1.png"
}

def list_screenshots():
    """List all available screenshots."""
    if not SCREENSHOTS_DIR.exists():
        print(f"❌ Screenshots directory not found: {SCREENSHOTS_DIR}")
        return []
    
    screenshots = sorted([f.name for f in SCREENSHOTS_DIR.iterdir() if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg']])
    return screenshots

def show_screenshot_suggestions():
    """Show suggested screenshots for each visual asset."""
    print("\n" + "="*60)
    print("📸 SUGGESTED SCREENSHOTS FOR EACH VISUAL ASSET")
    print("="*60)
    
    suggestions = {
        "Court Map": [
            "Main Menu.png",
            "Tutorial mode.png",
            "Tutorial_1.png",
            "BallCODE section.png"
        ],
        "Shadow Press Scouts": [
            "Tutorial_1.png",
            "Tutorial_2.png",
            "Tutorial_3.png",
            "Coding_Gameplay_1.png",
            "Mathlete_Gameplay_1.png"
        ],
        "State Diagram": [
            "Coding_Gameplay_1.png",
            "Coding_Gameplay_2.png",
            "Coding_Gameplay_3.png"
        ]
    }
    
    for visual_name, files in suggestions.items():
        print(f"\n🎨 {visual_name}:")
        for file in files:
            full_path = SCREENSHOTS_DIR / file
            if full_path.exists():
                print(f"   ✅ {file}")
            else:
                print(f"   ⚠️  {file} (not found)")
    
    print("\n" + "="*60)

def copy_screenshot(source_name, visual_type):
    """Copy a screenshot to the assets directory with the correct name."""
    source_path = SCREENSHOTS_DIR / source_name
    target_name = OUTPUT_NAMES.get(visual_type)
    
    if not source_path.exists():
        print(f"❌ Screenshot not found: {source_name}")
        return False
    
    if not target_name:
        print(f"❌ Unknown visual type: {visual_type}")
        return False
    
    # Ensure assets directory exists
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    
    target_path = ASSETS_DIR / target_name
    
    try:
        shutil.copy2(source_path, target_path)
        print(f"✅ Copied: {source_name} → {target_path}")
        return True
    except Exception as e:
        print(f"❌ Error copying: {e}")
        return False

def interactive_selection():
    """Interactive mode to select screenshots."""
    screenshots = list_screenshots()
    
    if not screenshots:
        print("❌ No screenshots found!")
        return
    
    print("\n" + "="*60)
    print("🎮 INTERACTIVE SCREENSHOT SELECTION")
    print("="*60)
    
    show_screenshot_suggestions()
    
    print("\n📋 Available Screenshots:")
    for i, screenshot in enumerate(screenshots, 1):
        print(f"   {i:2d}. {screenshot}")
    
    print("\n" + "="*60)
    print("SELECT SCREENSHOTS FOR EACH VISUAL ASSET")
    print("="*60)
    
    selections = {}
    
    for visual_type, output_name in OUTPUT_NAMES.items():
        visual_name = visual_type.replace("_", " ").title()
        print(f"\n🎨 {visual_name} ({output_name}):")
        
        while True:
            choice = input(f"   Enter screenshot number or filename (or 'skip'): ").strip()
            
            if choice.lower() == 'skip':
                print(f"   ⏭️  Skipped {visual_name}")
                break
            
            # Try to parse as number
            try:
                num = int(choice)
                if 1 <= num <= len(screenshots):
                    selected = screenshots[num - 1]
                    if copy_screenshot(selected, visual_type):
                        selections[visual_type] = selected
                        break
                    else:
                        print("   ❌ Copy failed. Try again.")
                else:
                    print(f"   ❌ Invalid number. Enter 1-{len(screenshots)}")
            except ValueError:
                # Try as filename
                if choice in screenshots:
                    if copy_screenshot(choice, visual_type):
                        selections[visual_type] = choice
                        break
                    else:
                        print("   ❌ Copy failed. Try again.")
                else:
                    print(f"   ❌ File not found: {choice}")
    
    print("\n" + "="*60)
    print("✅ SELECTION COMPLETE")
    print("="*60)
    
    if selections:
        print("\n📋 Selected Screenshots:")
        for visual_type, screenshot in selections.items():
            print(f"   {visual_type}: {screenshot}")
    
    print(f"\n📁 Files saved to: {ASSETS_DIR}")
    print("\n✅ Next step: Run `python3 scripts/add-visuals-to-book1.py` to add them to the website")

if __name__ == "__main__":
    interactive_selection()

