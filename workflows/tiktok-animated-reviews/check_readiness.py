#!/usr/bin/env python3
"""
Readiness Checker - Verifies everything is ready to go
"""

import os
import sys
from pathlib import Path

def check_readiness():
    """Check if system is ready to use."""
    print("\n" + "=" * 70)
    print("  🔍 SYSTEM READINESS CHECK")
    print("=" * 70 + "\n")
    
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    all_ready = True
    issues = []
    
    # Check 1: Python and dependencies
    print("📦 Checking Python and dependencies...")
    try:
        import moviepy
        import cv2
        print("   ✅ Python dependencies installed")
    except ImportError as e:
        print(f"   ❌ Missing dependency: {e}")
        issues.append("Run: pip install -r requirements.txt")
        all_ready = False
    
    # Check 2: FFmpeg
    print("\n🎬 Checking FFmpeg...")
    import subprocess
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, timeout=5)
        if result.returncode == 0:
            print("   ✅ FFmpeg installed")
        else:
            print("   ❌ FFmpeg not working")
            issues.append("Install FFmpeg: brew install ffmpeg")
            all_ready = False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("   ❌ FFmpeg not installed")
        issues.append("Install FFmpeg: brew install ffmpeg")
        all_ready = False
    
    # Check 3: API Key
    print("\n🔑 Checking API key...")
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if api_key:
        print("   ✅ API key found in environment")
    else:
        # Check config file
        config_path = Path("config/my_config.json")
        if config_path.exists():
            import json
            with open(config_path) as f:
                config = json.load(f)
                if config.get("voice", {}).get("api_key"):
                    print("   ✅ API key found in config")
                else:
                    print("   ⚠️  API key not found")
                    issues.append("Add API key to config or set ELEVENLABS_API_KEY environment variable")
                    all_ready = False
        else:
            print("   ⚠️  No config file found")
            issues.append("Run setup wizard: python3 setup_wizard.py")
            all_ready = False
    
    # Check 4: Voice sample
    print("\n🎤 Checking voice sample...")
    voice_sample = Path("assets/voice_samples/main_voice.mp3")
    if voice_sample.exists():
        print("   ✅ Voice sample found")
    else:
        print("   ⚠️  Voice sample not found")
        issues.append("Record voice sample and save to: assets/voice_samples/main_voice.mp3")
        all_ready = False
    
    # Check 5: Characters
    print("\n🎨 Checking characters...")
    characters_found = 0
    for char_type in ["youth", "adult", "robot"]:
        char_dir = Path(f"assets/characters/{char_type}")
        if char_dir.exists():
            char_files = list(char_dir.glob("*.mp4")) + list(char_dir.glob("*.png"))
            if char_files:
                print(f"   ✅ {char_type} character found")
                characters_found += 1
            else:
                print(f"   ⚠️  {char_type} character missing")
        else:
            print(f"   ⚠️  {char_type} character directory missing")
    
    if characters_found == 0:
        issues.append("Add at least one character file to assets/characters/")
        all_ready = False
    elif characters_found < 3:
        print(f"   ℹ️  {characters_found}/3 characters found (you can add more later)")
    
    # Check 6: Config file
    print("\n⚙️  Checking configuration...")
    config_path = Path("config/my_config.json")
    if config_path.exists():
        print("   ✅ Config file exists")
        try:
            import json
            with open(config_path) as f:
                config = json.load(f)
                if config.get("voice", {}).get("voice_id"):
                    print("   ✅ Voice ID configured")
                else:
                    print("   ⚠️  Voice ID not configured")
                    issues.append("Create voice clone: python3 -c \"from src.voice.voice_synthesizer import create_voice_clone; print(create_voice_clone('assets/voice_samples/main_voice.mp3'))\"")
        except Exception as e:
            print(f"   ⚠️  Config file error: {e}")
            issues.append("Fix config file or run setup wizard")
    else:
        print("   ⚠️  Config file not found")
        issues.append("Run setup wizard: python3 setup_wizard.py")
        all_ready = False
    
    # Check 7: Output directory
    print("\n📁 Checking output directory...")
    output_dir = Path("output/reviews")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        test_file = output_dir / ".test"
        test_file.write_text("test")
        test_file.unlink()
        print("   ✅ Output directory writable")
    except Exception as e:
        print(f"   ❌ Cannot write to output directory: {e}")
        issues.append(f"Fix output directory permissions: {e}")
        all_ready = False
    
    # Summary
    print("\n" + "=" * 70)
    if all_ready:
        print("  ✅ SYSTEM IS READY!")
        print("=" * 70)
        print("\n🚀 You can now use:")
        print("   python3 create_review.py \"video.mp4\" \"Your reaction text\"\n")
    else:
        print("  ⚠️  SYSTEM NEEDS SETUP")
        print("=" * 70)
        print("\n📋 To fix:")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
        print("\n💡 Quick setup:")
        print("   1. Get API key from elevenlabs.io")
        print("   2. Record voice sample")
        print("   3. Add character files")
        print("   4. Run: python3 setup_wizard.py\n")
    
    return all_ready

if __name__ == "__main__":
    ready = check_readiness()
    sys.exit(0 if ready else 1)
