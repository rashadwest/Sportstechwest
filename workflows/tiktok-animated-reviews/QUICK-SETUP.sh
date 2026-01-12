#!/bin/bash

# Quick Setup Script for TikTok Animated Review System
# This script sets up the basic structure and checks requirements

set -e

echo "🚀 TikTok Animated Review System - Quick Setup"
echo "=============================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Python version: $python_version"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check pip
echo "📋 Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Check FFmpeg
echo "📋 Checking FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg is not installed."
    echo "   Install with: brew install ffmpeg (macOS)"
    echo "   Or: sudo apt-get install ffmpeg (Linux)"
    echo "   Or download from: https://ffmpeg.org/download.html"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    ffmpeg_version=$(ffmpeg -version 2>&1 | head -n 1)
    echo "   ✅ FFmpeg found: $ffmpeg_version"
fi

# Create directory structure
echo ""
echo "📁 Creating directory structure..."
mkdir -p assets/characters
mkdir -p assets/voice_samples
mkdir -p assets/templates
mkdir -p output/reviews
mkdir -p config
echo "   ✅ Directories created"

# Check if config exists
if [ ! -f "config/default_config.json" ]; then
    echo "⚠️  Default config not found. Creating from template..."
    # Config will be created by the system
fi

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "   ✅ Dependencies installed"
else
    echo "⚠️  requirements.txt not found"
fi

# Check for character file
echo ""
echo "📋 Checking for character file..."
if [ -z "$(ls -A assets/characters 2>/dev/null)" ]; then
    echo "   ⚠️  No character file found in assets/characters/"
    echo "   Please add your animated character file:"
    echo "   - Video file (MP4, AVI, MOV)"
    echo "   - Image sequence (PNG, JPG)"
    echo "   - Spine file (.spine)"
    echo "   - Live2D file (.cubism)"
    echo "   - Blender file (.blend, .fbx, .dae)"
else
    echo "   ✅ Character file(s) found"
fi

# Check for voice sample
echo ""
echo "📋 Checking for voice sample..."
if [ -z "$(ls -A assets/voice_samples 2>/dev/null)" ]; then
    echo "   ⚠️  No voice sample found in assets/voice_samples/"
    echo "   Please add your voice sample (1-2 minutes of clear speech):"
    echo "   - MP3 or WAV format"
    echo "   - High quality, minimal background noise"
else
    echo "   ✅ Voice sample(s) found"
fi

# Check for API key
echo ""
echo "📋 Checking for API key..."
if [ -z "$ELEVENLABS_API_KEY" ] && [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ] && [ -z "$AZURE_SPEECH_KEY" ] && [ -z "$OPENAI_API_KEY" ]; then
    echo "   ⚠️  No voice synthesis API key found in environment"
    echo "   Set one of:"
    echo "   - ELEVENLABS_API_KEY (recommended)"
    echo "   - GOOGLE_APPLICATION_CREDENTIALS"
    echo "   - AZURE_SPEECH_KEY"
    echo "   - OPENAI_API_KEY"
else
    echo "   ✅ API key found in environment"
fi

# Summary
echo ""
echo "=============================================="
echo "✅ Setup Complete!"
echo ""
echo "Next Steps:"
echo "1. Add your character file to: assets/characters/"
echo "2. Add your voice sample to: assets/voice_samples/"
echo "3. Set your API key: export ELEVENLABS_API_KEY='your_key'"
echo "4. Create voice clone (see README.md)"
echo "5. Configure settings: config/default_config.json"
echo "6. Test: python src/pipeline/review_pipeline.py --help"
echo ""
echo "For detailed instructions, see:"
echo "- README.md"
echo "- BUILD-OUT-REQUIREMENTS.md"
echo "- INTEGRATION-GUIDE.md"
echo ""

