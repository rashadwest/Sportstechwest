#!/usr/bin/env python3
"""
Glif Visual Assets Helper
Prepares everything for generating visual assets in Glif

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).parent.parent
VISUAL_ASSETS_DIR = PROJECT_ROOT / "documents" / "visual-assets"
ASSETS_DIR = PROJECT_ROOT / "BallCode" / "assets" / "images"
PROMPTS_FILE = VISUAL_ASSETS_DIR / "episode1-visual-prompts.json"

# Ensure directories exist
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

def load_prompts():
    """Load prompts from JSON file."""
    if not PROMPTS_FILE.exists():
        print(f"❌ Prompts file not found: {PROMPTS_FILE}")
        return None
    
    with open(PROMPTS_FILE, 'r') as f:
        return json.load(f)

def print_glif_instructions():
    """Print step-by-step Glif instructions."""
    print("=" * 70)
    print("GLIF VISUAL ASSETS GENERATION GUIDE")
    print("=" * 70)
    print()
    print("📋 STEP-BY-STEP INSTRUCTIONS:")
    print()
    print("1. Go to: https://glif.app")
    print("2. Sign up/login (free tier available)")
    print("3. Click 'Create New Glif' or 'New'")
    print("4. Choose 'Image Generation' or 'Text to Image'")
    print("5. Paste the prompt below")
    print("6. Click 'Generate'")
    print("7. Wait for image (30-60 seconds)")
    print("8. Download high-resolution version")
    print("9. Save to: BallCode/assets/images/")
    print("10. Repeat for all 3 images")
    print()
    print("=" * 70)
    print()

def generate_glif_workflow():
    """Generate workflow instructions for each asset."""
    prompts_data = load_prompts()
    if not prompts_data:
        return
    
    assets = prompts_data.get("assets", {})
    
    print("=" * 70)
    print("ASSET 1: COURT MAP")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    print(assets.get("court_map", {}).get("prompt", ""))
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-court-map-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("=" * 70)
    print()
    input("Press Enter when you've generated and saved the Court Map image...")
    print()
    
    print("=" * 70)
    print("ASSET 2: SHADOW PRESS SCOUTS")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    print(assets.get("shadow_press_scouts", {}).get("prompt", ""))
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-shadow-press-scouts-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("=" * 70)
    print()
    input("Press Enter when you've generated and saved the Shadow Press Scouts image...")
    print()
    
    print("=" * 70)
    print("ASSET 3: STATE DIAGRAM")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    print(assets.get("state_diagram", {}).get("prompt", ""))
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-state-diagram-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("=" * 70)
    print()
    input("Press Enter when you've generated and saved the State Diagram image...")
    print()

def check_assets():
    """Check if all assets are generated."""
    print("=" * 70)
    print("CHECKING GENERATED ASSETS...")
    print("=" * 70)
    print()
    
    required_files = [
        "episode1-court-map-v1.png",
        "episode1-shadow-press-scouts-v1.png",
        "episode1-state-diagram-v1.png"
    ]
    
    all_found = True
    for filename in required_files:
        file_path = ASSETS_DIR / filename
        if file_path.exists():
            size = file_path.stat().st_size / 1024  # KB
            print(f"✅ {filename} ({size:.1f} KB)")
        else:
            print(f"❌ {filename} - NOT FOUND")
            all_found = False
    
    print()
    
    if all_found:
        print("=" * 70)
        print("✅ ALL ASSETS GENERATED!")
        print("=" * 70)
        print()
        print("🚀 Next step: Run the automation script to add images to website:")
        print("   python3 scripts/add-visuals-to-book1.py")
        print()
        return True
    else:
        print("=" * 70)
        print("⚠️  SOME ASSETS MISSING")
        print("=" * 70)
        print()
        print("Please generate the missing assets and save them to:")
        print(f"  {ASSETS_DIR}")
        print()
        return False

def main():
    """Main workflow."""
    print("=" * 70)
    print("GLIF VISUAL ASSETS HELPER")
    print("=" * 70)
    print()
    print("This script will guide you through generating visual assets in Glif.")
    print()
    
    # Check if prompts file exists
    if not PROMPTS_FILE.exists():
        print(f"❌ Prompts file not found: {PROMPTS_FILE}")
        print("   Please ensure the prompts file exists.")
        return 1
    
    # Print Glif instructions
    print_glif_instructions()
    
    # Ask user if they want to start
    response = input("Ready to start generating assets? (y/n): ").lower()
    if response != 'y':
        print("Exiting. Run this script again when ready.")
        return 0
    
    print()
    print("=" * 70)
    print("STARTING GENERATION WORKFLOW...")
    print("=" * 70)
    print()
    
    # Generate workflow
    generate_glif_workflow()
    
    # Check assets
    if check_assets():
        # Ask if user wants to run automation script
        response = input("Run automation script to add images to website? (y/n): ").lower()
        if response == 'y':
            print()
            print("Running automation script...")
            print()
            try:
                subprocess.run([
                    sys.executable,
                    str(PROJECT_ROOT / "scripts" / "add-visuals-to-book1.py")
                ], check=True)
                print()
                print("✅ Images added to website!")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error running automation script: {e}")
                return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

