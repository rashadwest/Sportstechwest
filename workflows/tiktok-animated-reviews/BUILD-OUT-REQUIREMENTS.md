# Build-Out Requirements - TikTok Animated Review System

**Complete checklist of everything needed to build and deploy this system**

---

## 📋 Prerequisites Checklist

### ✅ 1. System Requirements

**Hardware:**
- [ ] Computer with Python 3.8+ installed
- [ ] Minimum 8GB RAM (16GB recommended for video processing)
- [ ] Storage space: ~10GB for dependencies + output videos
- [ ] GPU (optional but recommended for faster processing)

**Software:**
- [ ] Python 3.8 or higher
- [ ] pip (Python package manager)
- [ ] FFmpeg (for video processing)
- [ ] Git (for version control)

**Check Installation:**
```bash
python --version  # Should be 3.8+
pip --version
ffmpeg -version   # Must be installed
```

---

## 🎨 2. Character Assets (YOU PROVIDE)

### Required Character File

**What You Need:**
- [ ] Animated character file in one of these formats:
  - **Video file** (MP4, AVI, MOV) - Pre-rendered animation
  - **Image sequence** (PNG, JPG) - Frame-by-frame animation
  - **Spine file** (.spine) - 2D skeletal animation
  - **Live2D file** (.cubism) - 2D character animation
  - **Blender file** (.blend, .fbx, .dae) - 3D animation

**Character Requirements:**
- [ ] Character should be rigged for facial expressions (if using advanced animation)
- [ ] Character should have mouth/face visible for lip-sync
- [ ] Character should be in a format you can export/render
- [ ] Character file size: Reasonable (not too large for processing)

**Where to Place:**
```
workflows/tiktok-animated-reviews/assets/characters/your_character.mp4
```

**If You Don't Have a Character Yet:**
- Option 1: Create simple animated character using tools like:
  - **Spine** (2D skeletal animation)
  - **Live2D** (2D character animation)
  - **Blender** (3D animation)
  - **After Effects** (2D animation, export as video)
- Option 2: Use a simple video loop of a character
- Option 3: Use an image sequence (PNG frames)

---

## 🎤 3. Voice Assets (YOU PROVIDE)

### Voice Sample for Cloning

**What You Need:**
- [ ] Voice sample audio file (MP3 or WAV)
- [ ] Duration: 1-2 minutes of clear speech
- [ ] Quality: High quality, no background noise
- [ ] Content: You speaking naturally (not reading a script)
- [ ] Format: MP3 or WAV

**Voice Sample Requirements:**
- [ ] Clear pronunciation
- [ ] Natural speaking pace
- [ ] Minimal background noise
- [ ] Good audio quality (not compressed too much)

**Where to Place:**
```
workflows/tiktok-animated-reviews/assets/voice_samples/your_voice_sample.mp3
```

**How to Create Voice Sample:**
1. Record yourself speaking for 1-2 minutes
2. Use a good microphone if possible
3. Speak naturally (like you're explaining something)
4. Export as MP3 or WAV
5. Place in `assets/voice_samples/` folder

**Voice Cloning Services:**
- **ElevenLabs** (recommended) - Best quality, easy to use
- **Google Cloud TTS** - Alternative with voice cloning
- **Azure Cognitive Services** - Enterprise option

---

## 🔑 4. API Keys & Services

### Voice Synthesis API (Choose One)

**Option 1: ElevenLabs (Recommended)**
- [ ] Create account at https://elevenlabs.io
- [ ] Get API key from dashboard
- [ ] Create voice clone from your sample
- [ ] Save voice ID
- [ ] Cost: ~$5-22/month depending on usage

**Option 2: Google Cloud TTS**
- [ ] Create Google Cloud account
- [ ] Enable Cloud Text-to-Speech API
- [ ] Create service account
- [ ] Download JSON credentials
- [ ] Cost: Pay-as-you-go (~$4 per 1M characters)

**Option 3: Azure Cognitive Services**
- [ ] Create Azure account
- [ ] Create Speech resource
- [ ] Get API key and region
- [ ] Cost: Pay-as-you-go

**Option 4: OpenAI TTS**
- [ ] Create OpenAI account
- [ ] Get API key
- [ ] Cost: Pay-as-you-go

**Environment Variables:**
```bash
# Add to your .env file or export
export ELEVENLABS_API_KEY="your_api_key_here"
export ELEVENLABS_VOICE_ID="your_voice_id_here"
```

---

## 📦 5. Python Dependencies

### Install Required Packages

**Core Dependencies:**
```bash
cd workflows/tiktok-animated-reviews
pip install -r requirements.txt
```

**What Gets Installed:**
- [ ] moviepy (video processing)
- [ ] opencv-python (video manipulation)
- [ ] elevenlabs (voice synthesis) - if using ElevenLabs
- [ ] google-cloud-texttospeech - if using Google
- [ ] azure-cognitiveservices-speech - if using Azure
- [ ] openai - if using OpenAI
- [ ] numpy, pillow, requests (utilities)

**Optional Dependencies (for advanced features):**
- [ ] wav2lip (for advanced lip-sync) - requires separate setup
- [ ] rhubarb-lip-sync (for phoneme-based lip-sync)
- [ ] bpy (Blender Python API) - if using Blender characters

**Install FFmpeg:**
```bash
# macOS
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

---

## ⚙️ 6. Configuration Setup

### Create Configuration File

**Step 1: Copy Default Config**
```bash
cp config/default_config.json config/my_config.json
```

**Step 2: Edit Configuration**
- [ ] Set character file path
- [ ] Set voice provider and API key
- [ ] Set voice ID (after cloning)
- [ ] Configure layout preferences
- [ ] Set output directory

**Example Config:**
```json
{
  "character": {
    "file_path": "assets/characters/your_character.mp4"
  },
  "voice": {
    "provider": "elevenlabs",
    "api_key": "your_api_key",
    "voice_id": "your_voice_id"
  },
  "composition": {
    "layout": "side_by_side",
    "character_position": "right"
  }
}
```

---

## 🧪 7. Testing Requirements

### Test Files Needed

**For Initial Testing:**
- [ ] Sample TikTok video (download one for testing)
- [ ] Sample reaction script (text file)
- [ ] Test output directory (auto-created)

**Test Script:**
```bash
python src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --output "output/test_review.mp4" \
  --config "config/my_config.json"
```

**What to Test:**
- [ ] Voice synthesis works
- [ ] Character animation loads
- [ ] Video composition works
- [ ] Output video is created
- [ ] Audio sync is correct
- [ ] Video quality is good

---

## 🔗 8. Integration Requirements

### Connect to Existing System

**If Using n8n:**
- [ ] n8n installed and running
- [ ] Access to n8n workflows
- [ ] Ability to add new nodes

**If Using Python Scripts:**
- [ ] Access to existing reaction automation scripts
- [ ] Ability to import new modules
- [ ] Path configuration for imports

**Integration Points:**
- [ ] After script generation
- [ ] Before video publishing
- [ ] In existing workflow

---

## 📁 9. Directory Structure Setup

### Create Required Directories

```bash
cd workflows/tiktok-animated-reviews

# Create asset directories
mkdir -p assets/characters
mkdir -p assets/voice_samples
mkdir -p assets/templates

# Create output directory
mkdir -p output/reviews

# Create config directory (if not exists)
mkdir -p config
```

**Directory Structure:**
```
tiktok-animated-reviews/
├── assets/
│   ├── characters/          # Your character files
│   └── voice_samples/       # Your voice samples
├── config/                   # Configuration files
├── output/
│   └── reviews/             # Generated videos
└── src/                     # Source code (already created)
```

---

## 🚀 10. Quick Start Checklist

### Step-by-Step Setup

**Step 1: Install Dependencies**
```bash
cd workflows/tiktok-animated-reviews
pip install -r requirements.txt
brew install ffmpeg  # macOS
```

**Step 2: Add Your Assets**
```bash
# Add character
cp /path/to/your/character.mp4 assets/characters/

# Add voice sample
cp /path/to/your/voice_sample.mp3 assets/voice_samples/
```

**Step 3: Create Voice Clone**
```python
from src.voice.voice_synthesizer import create_voice_clone

voice_id = create_voice_clone(
    "assets/voice_samples/your_voice_sample.mp3",
    provider="elevenlabs"
)
print(f"Your voice ID: {voice_id}")
```

**Step 4: Configure Settings**
```bash
# Edit config file
nano config/my_config.json
# Add your API key, voice ID, character path
```

**Step 5: Test**
```bash
python src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --config "config/my_config.json"
```

---

## 💰 11. Cost Estimates

### Monthly Costs (Approximate)

**Voice Synthesis:**
- ElevenLabs Starter: $5/month (10,000 characters)
- ElevenLabs Creator: $22/month (30,000 characters)
- Google Cloud TTS: ~$4 per 1M characters
- Azure: ~$4 per 1M characters

**Storage:**
- Local storage: Free (your hard drive)
- Cloud storage (optional): Varies

**Processing:**
- Local processing: Free (your computer)
- Cloud processing (optional): Varies

**Estimated Monthly Cost:**
- **Minimum**: $5-10/month (ElevenLabs Starter + basic usage)
- **Recommended**: $20-30/month (ElevenLabs Creator + moderate usage)

---

## ⚠️ 12. Common Issues & Solutions

### Potential Problems

**Issue: FFmpeg not found**
- Solution: Install FFmpeg (see installation above)
- Check: `ffmpeg -version`

**Issue: Character file not loading**
- Solution: Check file path in config
- Check: File format is supported
- Check: File permissions

**Issue: Voice synthesis fails**
- Solution: Check API key is correct
- Check: Voice ID is valid
- Check: API quota not exceeded

**Issue: Video composition fails**
- Solution: Check video resolutions match
- Check: FFmpeg is installed
- Check: Output directory permissions

---

## 📝 13. Next Steps After Setup

### Once Everything is Installed

1. **Test with Sample Video**
   - Download a TikTok video
   - Create a test script
   - Run the pipeline
   - Verify output

2. **Refine Configuration**
   - Adjust character position
   - Tune voice settings
   - Test different layouts

3. **Integrate with Automation**
   - Connect to existing workflow
   - Test end-to-end
   - Monitor results

4. **Scale Up**
   - Process multiple videos
   - Optimize settings
   - Monitor costs

---

## 🎯 Summary: What You Need to Provide

### Required (Must Have)
1. ✅ **Animated Character** - Your character file
2. ✅ **Voice Sample** - 1-2 minutes of your voice
3. ✅ **API Key** - For voice synthesis service
4. ✅ **Python Environment** - Python 3.8+ installed
5. ✅ **FFmpeg** - Video processing tool

### Optional (Nice to Have)
- GPU for faster processing
- Advanced lip-sync tools (Wav2Lip, Rhubarb)
- Multiple character variations
- Cloud storage for outputs

---

## 🚀 Ready to Build?

**Quick Start Command:**
```bash
# 1. Install dependencies
cd workflows/tiktok-animated-reviews
pip install -r requirements.txt

# 2. Add your assets
# (character and voice sample)

# 3. Configure
# (edit config file with your settings)

# 4. Test
python src/pipeline/review_pipeline.py \
  --tiktok-video "test.mp4" \
  --script "test.txt"
```

**Need Help?**
- Check README.md for detailed instructions
- Check INTEGRATION-GUIDE.md for workflow integration
- Review error messages for troubleshooting

---

**Status**: ✅ System is ready to build  
**Framework**: JAEDS (Jobs + Alpha Evolve + Demis + Superhero CV)  
**Next Step**: Install dependencies and add your assets!

