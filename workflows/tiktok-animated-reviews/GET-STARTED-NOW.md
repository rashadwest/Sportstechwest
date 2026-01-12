# 🚀 GET STARTED NOW - Quick Action Checklist

**Follow these steps in order to get your 3-character animated review system running**

---

## ✅ Phase 1: Basic Setup (15 minutes)

### 1. Run Setup Script
```bash
cd /Users/rashadwest/Sportstechwest/workflows/tiktok-animated-reviews
chmod +x QUICK-SETUP.sh
./QUICK-SETUP.sh
```

**Checklist:**
- [ ] Script ran successfully
- [ ] All directories created
- [ ] Python packages installed

---

## ✅ Phase 2: Get Your Characters (1-2 hours)

### 2. Extract Your Instagram Character

**From your Instagram post** (https://www.instagram.com/p/DQxNseoEdnE/):

**Option A: Download from Instagram**
```bash
# Use a tool like:
# - 4K Video Downloader
# - yt-dlp (command line)
# - Browser extension

# Or screen record the character animation
```

**Option B: Export from Animation Tool**
- If you have the original animation file
- Export as MP4 video loop (5-10 seconds)
- Or export as PNG sequence

### 3. Create/Get All 3 Characters

You need:
- **Youth Character** - Younger version for youth content
- **Adult Character** - Your character for adult content
- **Robot Character** - Robot character for robotics content

**Where to get them:**
- Use your Instagram character as base
- Create variations in animation tool
- Or use AI tools to generate variations

### 4. Save Character Files

```bash
# Create directories
mkdir -p assets/characters/youth
mkdir -p assets/characters/adult
mkdir -p assets/characters/robot

# Copy your character files
# Example:
cp /path/to/youth_character.mp4 assets/characters/youth/character.mp4
cp /path/to/adult_character.mp4 assets/characters/adult/character.mp4
cp /path/to/robot_character.mp4 assets/characters/robot/character.mp4
```

**Checklist:**
- [ ] Youth character saved
- [ ] Adult character saved
- [ ] Robot character saved
- [ ] All files are MP4, AVI, MOV, or PNG sequence

---

## ✅ Phase 3: Voice Setup (30 minutes)

### 5. Record Your Voice Sample

**Record 1-2 minutes of clear speech:**
- Use QuickTime (macOS) or your phone
- Speak naturally (not reading)
- High quality, minimal background noise
- Save as MP3 or WAV

### 6. Save Voice Sample

```bash
cp /path/to/your_voice.mp3 assets/voice_samples/main_voice.mp3
```

**Checklist:**
- [ ] Voice sample recorded
- [ ] Saved in `assets/voice_samples/main_voice.mp3`

### 7. Get ElevenLabs API Key

1. Go to https://elevenlabs.io
2. Sign up (free account works for testing)
3. Go to Profile > API Keys
4. Copy your API key

**Checklist:**
- [ ] Account created
- [ ] API key copied

### 8. Create Voice Clone

```bash
# Set API key
export ELEVENLABS_API_KEY="your_api_key_here"

# Create voice clone
python3 -c "
from src.voice.voice_synthesizer import create_voice_clone
voice_id = create_voice_clone(
    'assets/voice_samples/main_voice.mp3',
    provider='elevenlabs'
)
print(f'VOICE_ID={voice_id}')
print('Copy this voice ID!')
"
```

**Save the voice ID** - you'll need it next!

**Checklist:**
- [ ] Voice clone created
- [ ] Voice ID saved

---

## ✅ Phase 4: Configuration (10 minutes)

### 9. Create Config File

```bash
cp config/default_config.json config/my_config.json
```

### 10. Edit Config File

Open `config/my_config.json` and update:

```json
{
  "characters": {
    "youth": {
      "file_path": "assets/characters/youth/character.mp4"
    },
    "adult": {
      "file_path": "assets/characters/adult/character.mp4"
    },
    "robot": {
      "file_path": "assets/characters/robot/character.mp4"
    }
  },
  "voice": {
    "provider": "elevenlabs",
    "api_key": "YOUR_API_KEY_HERE",
    "voice_id": "YOUR_VOICE_ID_HERE"
  }
}
```

**Checklist:**
- [ ] Config file created
- [ ] All 3 character paths set
- [ ] API key added
- [ ] Voice ID added

---

## ✅ Phase 5: Test (15 minutes)

### 11. Test with Sample Video

```bash
# Create test script
echo "This is a test reaction script for youth sports tech content." > test_script.txt

# Test with auto-selection
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "path/to/test_video.mp4" \
  --script "test_script.txt" \
  --config "config/my_config.json" \
  --auto-select-character
```

**Checklist:**
- [ ] Test video available
- [ ] Test script created
- [ ] Test run completed
- [ ] Output video generated
- [ ] Character appears correctly
- [ ] Voice plays correctly

---

## ✅ Phase 6: Test All Characters

### 12. Test Each Character

```bash
# Test Youth
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --character "youth" \
  --config "config/my_config.json"

# Test Adult
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --character "adult" \
  --config "config/my_config.json"

# Test Robot
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --character "robot" \
  --config "config/my_config.json"
```

**Checklist:**
- [ ] All 3 characters tested
- [ ] All videos generated
- [ ] All work correctly

---

## ✅ Phase 7: Integration (30 minutes)

### 13. Integrate with Your Workflow

See `INTEGRATION-GUIDE.md` for detailed integration steps.

**Quick Integration:**
```python
from workflows.tiktok_animated_reviews.src.pipeline import ReviewPipeline

pipeline = ReviewPipeline(config_path="config/my_config.json")
output_path = pipeline.process(
    tiktok_video_path="video.mp4",
    script_path="script.txt",
    character=None  # Auto-selects based on script
)
```

**Checklist:**
- [ ] Integration code added
- [ ] Tested with existing workflow
- [ ] Works end-to-end

---

## 🎯 You're Done!

**What You Have:**
- ✅ 3-character system (youth, adult, robot)
- ✅ Auto-character selection based on content
- ✅ Your voice cloned and working
- ✅ Integrated with your workflow

**Daily Use:**
```bash
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "video.mp4" \
  --script "script.txt" \
  --config "config/my_config.json" \
  --auto-select-character
```

**The system will:**
1. Read your script
2. Auto-select character (youth/robot/adult)
3. Generate voice audio
4. Animate character
5. Compose final video
6. Ready to publish!

---

## 📚 Need More Details?

- **Full Setup Guide**: `STEP-BY-STEP-ACTION-PLAN.md`
- **Requirements**: `BUILD-OUT-REQUIREMENTS.md`
- **Integration**: `INTEGRATION-GUIDE.md`
- **README**: `README.md`

---

**Total Time: 3-4 hours for complete setup**

**Status**: Ready to build! 🚀

