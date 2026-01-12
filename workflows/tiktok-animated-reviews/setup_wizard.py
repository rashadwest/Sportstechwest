#!/usr/bin/env python3
"""
JAEDS Setup Wizard - Automated Configuration
Automates everything possible in the setup process.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, Optional

def print_header(text: str):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")

def print_step(step: int, text: str):
    """Print step number and text."""
    print(f"\n[{step}] {text}")
    print("-" * 70)

def get_input(prompt: str, default: Optional[str] = None, required: bool = True) -> str:
    """Get user input with optional default."""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    
    while True:
        value = input(full_prompt).strip()
        if value:
            return value
        elif default:
            return default
        elif not required:
            return ""
        else:
            print("  ⚠️  This field is required. Please enter a value.")

def validate_file_path(path: str, file_type: str = "file") -> bool:
    """Validate that file or directory exists."""
    path_obj = Path(path)
    if file_type == "file":
        exists = path_obj.is_file()
    else:
        exists = path_obj.is_dir()
    
    if not exists:
        print(f"  ⚠️  Warning: {file_type} not found at: {path}")
        response = input("  Continue anyway? (y/n): ").strip().lower()
        return response == 'y'
    return True

def create_voice_clone_automated(api_key: str, voice_sample_path: str) -> Optional[str]:
    """Automatically create voice clone."""
    print("\n  🤖 Creating voice clone automatically...")
    
    try:
        from src.voice.voice_synthesizer import create_voice_clone
        
        # Set API key in environment
        os.environ['ELEVENLABS_API_KEY'] = api_key
        
        voice_id = create_voice_clone(voice_sample_path, provider='elevenlabs')
        print(f"  ✅ Voice clone created successfully!")
        print(f"  📝 Voice ID: {voice_id}")
        return voice_id
        
    except Exception as e:
        print(f"  ❌ Error creating voice clone: {e}")
        print("  💡 You can create it manually later")
        return None

def create_config_file(config_data: Dict, output_path: str):
    """Create configuration file."""
    config_dir = Path(output_path).parent
    config_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(config_data, f, indent=2)
    
    print(f"  ✅ Config file created: {output_path}")

def main():
    """Main setup wizard."""
    print_header("🎯 TikTok Animated Review System - Setup Wizard")
    print("This wizard will help you configure the system automatically.")
    print("We'll ask for the minimum required information.\n")
    
    # Get project root
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    config_data = {
        "output_dir": "output/reviews",
        "characters": {},
        "voice": {},
        "character_selection": {
            "youth_keywords": ["youth", "kid", "student", "young", "teen", "children", "kids"],
            "robot_keywords": ["robot", "robotics", "ai", "automation", "machine", "artificial intelligence"],
            "adult_keywords": ["adult", "professional", "grown", "mature"]
        },
        "composition": {
            "layout": "side_by_side",
            "character_position": "right",
            "character_size": "40%",
            "output": {
                "format": "mp4",
                "width": 1080,
                "height": 1920,
                "fps": 30
            }
        },
        "lip_sync": {
            "method": "basic",
            "model_path": None
        }
    }
    
    # Step 1: Voice Setup
    print_step(1, "Voice Configuration")
    print("  We need your ElevenLabs API key and voice sample.")
    
    api_key = get_input("  Enter your ElevenLabs API key", required=True)
    config_data["voice"]["api_key"] = api_key
    config_data["voice"]["provider"] = "elevenlabs"
    
    voice_sample = get_input(
        "  Enter path to your voice sample (MP3)",
        default="assets/voice_samples/main_voice.mp3"
    )
    
    if validate_file_path(voice_sample, "file"):
        # Try to create voice clone automatically
        voice_id = create_voice_clone_automated(api_key, voice_sample)
        
        if voice_id:
            config_data["voice"]["voice_id"] = voice_id
            config_data["voice"]["settings"] = {
                "stability": 0.75,
                "similarity_boost": 0.75,
                "speed": 1.0
            }
        else:
            # Ask for voice ID manually
            voice_id = get_input("  Enter your voice ID (or press Enter to skip)", required=False)
            if voice_id:
                config_data["voice"]["voice_id"] = voice_id
                config_data["voice"]["settings"] = {
                    "stability": 0.75,
                    "similarity_boost": 0.75,
                    "speed": 1.0
                }
    
    # Step 2: Character Setup
    print_step(2, "Character Configuration")
    print("  We need paths to your 3 character files.")
    print("  (You can add these later if files aren't ready yet)\n")
    
    characters = ["youth", "adult", "robot"]
    for char_type in characters:
        default_path = f"assets/characters/{char_type}/character.mp4"
        char_path = get_input(
            f"  Enter path to {char_type} character",
            default=default_path,
            required=False
        )
        
        if char_path:
            if validate_file_path(char_path, "file"):
                config_data["characters"][char_type] = {
                    "name": f"{char_type}_character",
                    "file_path": char_path,
                    "voice_type": char_type,
                    "position": {
                        "x": "right",
                        "y": "center",
                        "size": "medium"
                    }
                }
            else:
                # Still add to config, user can fix path later
                config_data["characters"][char_type] = {
                    "name": f"{char_type}_character",
                    "file_path": char_path,
                    "voice_type": char_type,
                    "position": {
                        "x": "right",
                        "y": "center",
                        "size": "medium"
                    }
                }
    
    # Step 3: Save Configuration
    print_step(3, "Saving Configuration")
    
    config_path = "config/my_config.json"
    create_config_file(config_data, config_path)
    
    # Step 4: Summary
    print_header("✅ Setup Complete!")
    print("\n📋 Configuration Summary:")
    print(f"  ✅ Config file: {config_path}")
    print(f"  ✅ API key: {'✓ Set' if api_key else '✗ Missing'}")
    print(f"  ✅ Voice ID: {'✓ Set' if config_data['voice'].get('voice_id') else '✗ Missing'}")
    print(f"  ✅ Characters configured: {len(config_data['characters'])}/3")
    
    print("\n📝 Next Steps:")
    if not config_data['voice'].get('voice_id'):
        print("  1. Create voice clone manually (see MANUAL-STEPS-ONLY.md)")
    if len(config_data['characters']) < 3:
        print("  2. Add missing character files to config")
    print("  3. Test the system:")
    print("     python3 src/pipeline/review_pipeline.py \\")
    print("       --tiktok-video test.mp4 \\")
    print("       --script test.txt \\")
    print("       --config config/my_config.json \\")
    print("       --auto-select-character")
    
    print("\n" + "=" * 70)
    print("  🚀 You're ready to go!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error during setup: {e}")
        sys.exit(1)

