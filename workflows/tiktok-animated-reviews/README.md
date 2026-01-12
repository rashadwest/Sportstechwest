# TikTok Animated Review System

Automated system for creating TikTok reaction videos with animated character and voice synthesis using **JAEDS Framework**.

## 🎯 What It Does

This system automatically creates TikTok reaction videos by:
1. **Generating voice audio** from your reaction script (using your cloned voice)
2. **Animating your character** based on the script
3. **Syncing lip movements** with the audio
4. **Composing the final video** with TikTok video + character + voice

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd workflows/tiktok-animated-reviews
pip install -r requirements.txt
```

### 2. Setup Configuration

```bash
# Copy default config
cp config/default_config.json config/my_config.json

# Edit with your settings:
# - Character file path
# - Voice API key and voice ID
# - Layout preferences
```

### 3. Add Your Assets

```bash
# Add your animated character
cp your_character.mp4 assets/characters/

# Add your voice sample (for cloning)
cp your_voice_sample.mp3 assets/voice_samples/
```

### 4. Create Voice Clone (One-time)

```python
from src.voice.voice_synthesizer import create_voice_clone

voice_id = create_voice_clone(
    "assets/voice_samples/your_voice_sample.mp3",
    provider="elevenlabs"
)
print(f"Your voice ID: {voice_id}")
# Add this to your config file
```

### 5. Run Pipeline

```bash
python src/pipeline/review_pipeline.py \
  --tiktok-video "path/to/tiktok_video.mp4" \
  --script "path/to/reaction_script.txt" \
  --output "output/reviews/review_001.mp4" \
  --config "config/my_config.json"
```

## 📁 Project Structure

```
tiktok-animated-reviews/
├── README.md
├── requirements.txt
├── config/
│   └── default_config.json
├── src/
│   ├── pipeline/
│   │   └── review_pipeline.py      # Main pipeline
│   ├── animation/
│   │   ├── character_animator.py    # Character animation
│   │   └── lip_sync.py              # Lip-sync system
│   ├── voice/
│   │   └── voice_synthesizer.py      # Voice synthesis
│   └── composition/
│       ├── video_composer.py        # Video composition
│       └── sync_manager.py          # Sync management
├── assets/
│   ├── characters/                   # Character files
│   └── voice_samples/               # Voice samples
└── output/
    └── reviews/                      # Generated videos
```

## ⚙️ Configuration

### Character Configuration

```json
{
  "character": {
    "file_path": "assets/characters/your_character.mp4",
    "position": {
      "x": "right",
      "y": "center",
      "size": "medium"
    }
  }
}
```

### Voice Configuration

```json
{
  "voice": {
    "provider": "elevenlabs",
    "api_key": "your_api_key",
    "voice_id": "your_voice_clone_id",
    "settings": {
      "stability": 0.75,
      "similarity_boost": 0.75,
      "speed": 1.0
    }
  }
}
```

### Composition Configuration

```json
{
  "composition": {
    "layout": "side_by_side",
    "character_position": "right",
    "character_size": "40%",
    "output": {
      "width": 1080,
      "height": 1920,
      "fps": 30
    }
  }
}
```

## 🎨 Supported Formats

### Character Animation
- **Video files**: MP4, AVI, MOV (pre-rendered animations)
- **Image sequences**: PNG, JPG (frame-by-frame)
- **Spine**: .spine files (2D skeletal animation)
- **Live2D**: .cubism files (2D character animation)
- **Blender**: .blend, .fbx, .dae (3D animation)

### Voice Synthesis
- **ElevenLabs**: Best quality, voice cloning
- **Google Cloud TTS**: Alternative with voice cloning
- **Azure Cognitive Services**: Enterprise option
- **OpenAI TTS**: New voice cloning capabilities

### Video Layouts
- **side_by_side**: TikTok video on left, character on right
- **picture_in_picture**: Character overlay on TikTok video
- **split_screen**: Equal split between TikTok and character

## 🔄 Integration with Existing System

This system integrates with your existing TikTok reaction automation:

```
Reaction Script Generation
    ↓
TikTok Animated Review System
    ↓
Final Video Output
    ↓
Existing Publishing Automation
    ↓
YouTube, TikTok, Twitter, LinkedIn
```

## 📚 JAEDS Framework

This system follows the **JAEDS Framework**:
- **Jobs**: Simple, one-command execution
- **Alpha Evolve**: Rapid iteration and testing
- **Demis**: Research-backed implementation
- **Superhero CV**: PhD-level video processing

## 🛠️ Troubleshooting

### Voice Synthesis Issues
- Check API key is set correctly
- Verify voice ID is valid
- Check API quota/limits

### Animation Issues
- Ensure character file is in supported format
- Check file paths are correct
- Verify video codec compatibility

### Composition Issues
- Check video resolutions match
- Verify audio/video durations align
- Check FFmpeg is installed

## 📝 Notes

- **Character Format**: Provide your animated character in a supported format
- **Voice Sample**: Need 1-2 minutes of clear speech for voice cloning
- **Integration**: Works with existing reaction automation workflow
- **Customization**: Fully configurable for different layouts and styles

## 🚀 Next Steps

1. Add your character and voice sample
2. Configure settings
3. Test with a sample video
4. Integrate with existing automation
5. Scale to multiple videos

---

**Framework**: JAEDS (Jobs + Alpha Evolve + Demis + Superhero CV)  
**Status**: 🚀 Active Development

