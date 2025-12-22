#!/usr/bin/env python3
"""
Visual Asset Generation Prompt Generator
Creates optimized prompts for Episode 1 visual assets

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "documents" / "visual-assets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Visual Asset Specifications
VISUAL_ASSETS = {
    "court_map": {
        "name": "Court Map Visual",
        "description": "Basketball court center circle with tech elements integrated",
        "prompt": """Create a basketball court diagram showing the center circle area. 
The court should be clean and professional, with the center circle prominently displayed. 
Integrate subtle tech elements like circuit patterns or code symbols around the circle perimeter. 
Style: Modern, clean, educational illustration. Colors: Orange (#eb6123) and blue (#0C72B3) as primary colors. 
Background: Light gray or white. Format: High resolution, suitable for print and web.""",
        "use_case": "Episode 1 storybook, website, curriculum materials",
        "dimensions": "1920x1080px (16:9 ratio)",
        "format": "PNG with transparent background option"
    },
    "shadow_press_scouts": {
        "name": "Shadow Press Scouts Character Art",
        "description": "Character design for the Shadow Press Scouts team",
        "prompt": """Design a basketball character representing the Shadow Press Scouts team. 
The character should be dynamic and athletic, wearing a basketball uniform with team colors. 
Pose: Defensive stance, ready to press. Style: Modern, engaging, suitable for children's book. 
Colors: Dark blue/navy for team colors, with orange accents. Expression: Determined, focused. 
Background: Simple gradient or court background. Format: High resolution character illustration.""",
        "use_case": "Episode 1 storybook, character introduction, game assets",
        "dimensions": "1024x1024px (square format)",
        "format": "PNG with transparent background"
    },
    "state_diagram": {
        "name": "State Diagram Visualization",
        "description": "Visual representation of possession state transitions",
        "prompt": """Create an educational diagram showing basketball possession states and transitions. 
Show three main states: 'Our Ball', 'Their Ball', 'Neutral' as connected nodes. 
Use arrows to show transitions between states. Style: Clean, diagrammatic, educational. 
Colors: Use orange (#eb6123) for 'Our Ball', blue (#0C72B3) for 'Their Ball', gray for 'Neutral'. 
Include basketball icons or symbols in each state. Format: Vector-style illustration, scalable.""",
        "use_case": "Episode 1 educational content, curriculum materials, teacher guides",
        "dimensions": "1200x800px (3:2 ratio)",
        "format": "PNG or SVG (preferred)"
    }
}

def generate_prompts_file():
    """Generate a JSON file with all visual asset prompts."""
    output_file = OUTPUT_DIR / "episode1-visual-prompts.json"
    
    prompts_data = {
        "generated": datetime.now().isoformat(),
        "episode": "Episode 1: The Tip-off Trial",
        "assets": VISUAL_ASSETS,
        "generation_instructions": {
            "method": "Use AI image generation (DALL-E, Midjourney, or Stable Diffusion)",
            "steps": [
                "1. Use the provided prompt for each asset",
                "2. Generate multiple variations (3-5 per asset)",
                "3. Select best version based on style consistency",
                "4. Save in high resolution (minimum 1920px width)",
                "5. Optimize for web (compress if needed)",
                "6. Save to BallCode/assets/images/ directory"
            ],
            "naming_convention": "episode1-[asset-name]-[version].png",
            "example": "episode1-court-map-v1.png"
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(prompts_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated prompts file: {output_file}")
    return output_file

def generate_markdown_guide():
    """Generate a markdown guide for visual asset generation."""
    output_file = OUTPUT_DIR / "episode1-visual-assets-guide.md"
    
    content = f"""# Episode 1 Visual Assets Generation Guide

**Generated:** {datetime.now().strftime('%B %d, %Y')}  
**Status:** Ready for Generation  
**Priority:** ⚠️ **CRITICAL BLOCKER** - Blocks multiple plans

---

## 📊 Overview

This guide provides everything needed to generate the 3 critical visual assets for Episode 1.

**Current Status:** 25% Complete (briefs ready, images not generated)  
**Target:** 100% Complete (all 3 images generated and integrated)

---

## 🎯 The 3 Visual Assets

"""
    
    for key, asset in VISUAL_ASSETS.items():
        content += f"""### {asset['name']}

**Description:** {asset['description']}

**Use Cases:**
- {asset['use_case']}

**Specifications:**
- Dimensions: {asset['dimensions']}
- Format: {asset['format']}

**Generation Prompt:**
```
{asset['prompt']}
```

**File Naming:**
- `episode1-{key}-v1.png`
- Save to: `BallCode/assets/images/`

---

"""
    
    content += """## 🚀 Generation Steps

### Option 1: DALL-E (OpenAI)
1. Go to https://chat.openai.com
2. Use GPT-4 with DALL-E
3. Paste the prompt for each asset
4. Generate 3-5 variations
5. Select best version

### Option 2: Midjourney
1. Join Midjourney Discord
2. Use `/imagine` command
3. Paste the prompt
4. Upscale best version
5. Download high-res

### Option 3: Stable Diffusion (Local)
1. Use Automatic1111 or similar
2. Load model (e.g., SDXL)
3. Enter prompt
4. Generate multiple variations
5. Select and upscale

### Option 4: Glif (Free Tier)
1. Go to https://glif.app
2. Create new glif
3. Use prompt as instruction
4. Generate and download

---

## ✅ Quality Checklist

Before considering an asset complete:

- [ ] High resolution (minimum 1920px width)
- [ ] Style matches other assets (consistent look)
- [ ] Colors match brand (orange #eb6123, blue #0C72B3)
- [ ] Suitable for both print and web
- [ ] File size optimized (< 500KB for web)
- [ ] Saved in correct location (`BallCode/assets/images/`)
- [ ] Named according to convention

---

## 📈 Impact

**Once these 3 assets are generated:**

- ✅ Episode 1: 45% → 70% (+25%)
- ✅ Website Updates: 0% → 20% (+20%)
- ✅ IBM Presentation: 30% → 60% (+30%)
- ✅ Overall Project: 45% → 50%+ (+5%+)

**Unblocks:**
- Episode 1 PDF creation
- Website Episode 1 page
- IBM presentation deck
- Pilot school package
- Production assets

---

## 🎯 The ONE Thing

**Generate these 3 visual assets (2-4 hours)**

This single action unblocks 5+ downstream tasks and moves the project from 45% → 50%+ completion.

---

**Next Steps:**
1. Choose generation method (DALL-E, Midjourney, etc.)
2. Generate all 3 assets
3. Review and select best versions
4. Save to `BallCode/assets/images/`
5. Update progress tracking

"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated guide: {output_file}")
    return output_file

def main():
    """Generate visual asset prompts and guide."""
    print("=" * 60)
    print("🎨 Visual Asset Generation Prompt Generator")
    print("=" * 60)
    print()
    
    prompts_file = generate_prompts_file()
    guide_file = generate_markdown_guide()
    
    print()
    print("=" * 60)
    print("✅ Generation Complete!")
    print("=" * 60)
    print()
    print("📁 Files Created:")
    print(f"  ✅ {prompts_file}")
    print(f"  ✅ {guide_file}")
    print()
    print("🚀 Next Steps:")
    print("  1. Review prompts in the generated files")
    print("  2. Choose generation method (DALL-E, Midjourney, etc.)")
    print("  3. Generate all 3 visual assets")
    print("  4. Save to BallCode/assets/images/")
    print("  5. Update progress: Episode 1 → 70% complete")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


