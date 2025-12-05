#!/usr/bin/env python3
"""
Plan 2: Visual Asset Generator
Extracts and uses Glif prompts from Episode 1 Visual Briefs to generate images.
Can work with or without API keys (prepares prompts for manual generation).
"""

import json
import os
from pathlib import Path

def load_visual_prompts():
    """Load visual prompts from JSON file"""
    prompts_file = Path(__file__).parent / "plan2_visual_prompts.json"
    
    if not prompts_file.exists():
        raise FileNotFoundError(f"Visual prompts file not found: {prompts_file}")
    
    with open(prompts_file, 'r') as f:
        return json.load(f)

def generate_with_stability_api(prompt, output_path, api_key):
    """Generate image using Stability AI API"""
    try:
        import requests
        import base64
        
        response = requests.post(
            "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "text_prompts": [{"text": prompt, "weight": 1.0}],
                "cfg_scale": 7,
                "width": 1024,
                "height": 768,
                "samples": 1,
                "steps": 30
            }
        )
        
        if response.status_code == 200:
            image_data = response.json()["artifacts"][0]["base64"]
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(image_data))
            return output_path
        else:
            raise Exception(f"API request failed: {response.text}")
            
    except ImportError:
        raise ImportError("requests library required. Install with: pip install requests")
    except Exception as e:
        raise Exception(f"Image generation failed: {e}")

def generate_manual_instructions(prompts_data):
    """Generate instructions for manual image generation"""
    instructions = []
    
    for asset in prompts_data["visual_assets"]:
        instructions.append({
            "asset": asset["name"],
            "prompt": asset["glif_prompt"],
            "specs": asset["technical_specs"],
            "tools": ["Glif", "Midjourney", "DALL-E", "Stability AI"],
            "steps": [
                f"1. Copy the Glif prompt for {asset['name']}",
                f"2. Open your preferred image generation tool",
                f"3. Paste the prompt",
                f"4. Set dimensions: {asset['technical_specs']['dimensions']}",
                f"5. Generate and save as {asset['asset_id']}.png"
            ]
        })
    
    return instructions

def main():
    """Main execution function"""
    print("🎨 Plan 2: Visual Asset Generator")
    print("=" * 60)
    
    # Load prompts
    prompts_data = load_visual_prompts()
    
    # Check for API key
    api_key = os.getenv("STABILITY_API_KEY")
    
    output_dir = Path(__file__).parent / "visuals"
    output_dir.mkdir(exist_ok=True)
    
    if api_key:
        print("\n✅ API key found - Generating images automatically...")
        for asset in prompts_data["visual_assets"]:
            print(f"\nGenerating: {asset['name']}")
            output_path = output_dir / f"{asset['asset_id']}.png"
            try:
                generate_with_stability_api(asset["glif_prompt"], output_path, api_key)
                print(f"✅ Generated: {output_path}")
            except Exception as e:
                print(f"❌ Error: {e}")
    else:
        print("\n⚠️  No API key found - Generating manual instructions...")
        instructions = generate_manual_instructions(prompts_data)
        
        instructions_file = Path(__file__).parent / "plan2_manual_generation_steps.json"
        with open(instructions_file, 'w') as f:
            json.dump(instructions, f, indent=2)
        
        print(f"\n✅ Manual generation instructions saved to: {instructions_file}")
        print("\nTo generate images manually:")
        for asset in prompts_data["visual_assets"]:
            print(f"\n{asset['name']}:")
            print(f"  Prompt: {asset['glif_prompt'][:100]}...")
            print(f"  Use: Glif, Midjourney, DALL-E, or Stability AI")
    
    print("\n" + "=" * 60)
    print("✅ Visual generation setup complete!")
    print(f"📁 Prompts loaded: {len(prompts_data['visual_assets'])} assets")
    print(f"📊 Status: {prompts_data['completion_percentage']}% complete")

if __name__ == "__main__":
    main()




