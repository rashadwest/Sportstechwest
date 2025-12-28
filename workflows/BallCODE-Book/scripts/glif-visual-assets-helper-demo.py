#!/usr/bin/env python3
"""
Glif Visual Assets Helper - DEMO VERSION
Shows what the script does without requiring user input

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
VISUAL_ASSETS_DIR = PROJECT_ROOT / "documents" / "visual-assets"
ASSETS_DIR = PROJECT_ROOT / "BallCode" / "assets" / "images"
PROMPTS_FILE = VISUAL_ASSETS_DIR / "episode1-visual-prompts.json"

def load_prompts():
    """Load prompts from JSON file."""
    if not PROMPTS_FILE.exists():
        print(f"❌ Prompts file not found: {PROMPTS_FILE}")
        return None
    
    with open(PROMPTS_FILE, 'r') as f:
        return json.load(f)

def demo_glif_workflow():
    """Show what the Glif workflow looks like."""
    prompts_data = load_prompts()
    if not prompts_data:
        return
    
    assets = prompts_data.get("assets", {})
    
    print("=" * 70)
    print("GLIF VISUAL ASSETS HELPER - DEMO")
    print("=" * 70)
    print()
    print("This is what the script will guide you through:")
    print()
    
    print("=" * 70)
    print("ASSET 1: COURT MAP")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    court_prompt = assets.get("court_map", {}).get("prompt", "")
    print(court_prompt[:200] + "..." if len(court_prompt) > 200 else court_prompt)
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-court-map-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("📐 DIMENSIONS:")
    print("  1920x1080px (16:9 ratio)")
    print()
    print("=" * 70)
    print()
    
    print("=" * 70)
    print("ASSET 2: SHADOW PRESS SCOUTS")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    scouts_prompt = assets.get("shadow_press_scouts", {}).get("prompt", "")
    print(scouts_prompt[:200] + "..." if len(scouts_prompt) > 200 else scouts_prompt)
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-shadow-press-scouts-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("📐 DIMENSIONS:")
    print("  1024x1024px (square format)")
    print()
    print("=" * 70)
    print()
    
    print("=" * 70)
    print("ASSET 3: STATE DIAGRAM")
    print("=" * 70)
    print()
    print("📝 PROMPT TO COPY:")
    print("-" * 70)
    diagram_prompt = assets.get("state_diagram", {}).get("prompt", "")
    print(diagram_prompt[:200] + "..." if len(diagram_prompt) > 200 else diagram_prompt)
    print("-" * 70)
    print()
    print("💾 SAVE AS:")
    print("  episode1-state-diagram-v1.png")
    print()
    print("📁 SAVE TO:")
    print(f"  {ASSETS_DIR}")
    print()
    print("📐 DIMENSIONS:")
    print("  1200x800px (3:2 ratio)")
    print()
    print("=" * 70)
    print()
    
    print("=" * 70)
    print("WHAT HAPPENS NEXT")
    print("=" * 70)
    print()
    print("1. You generate all 3 images in Glif (glif.app)")
    print("2. You save them to the folder above")
    print("3. Run: python3 scripts/add-visuals-to-book1.py")
    print("4. Script automatically adds images to Book 1 page")
    print("5. Done! ✅")
    print()
    print("=" * 70)

if __name__ == "__main__":
    demo_glif_workflow()


