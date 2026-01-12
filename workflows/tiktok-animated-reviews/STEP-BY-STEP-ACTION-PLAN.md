# Step-by-Step Action Plan - TikTok Animated Review System

**Complete checklist to get your 3-character animated review system running**

Based on your Instagram character: https://www.instagram.com/p/DQxNseoEdnE/

---

## 🎯 Goal

Create automated TikTok reviews with 3 animated characters:
1. **Youth Character** - Talks for youth content
2. **Adult Character** (You) - Talks for adult/grown content  
3. **Robot Character** - Talks for robotics content

All using your voice (or character-specific voices if preferred).

---

## 📋 Phase 1: Setup & Installation (30 minutes)

### Step 1: Install System Requirements

```bash
# Check Python version (need 3.8+)
python3 --version

# Install FFmpeg (required for video processing)
brew install ffmpeg  # macOS
# OR
sudo apt-get install ffmpeg  # Linux

# Navigate to project
cd /Users/rashadwest/Sportstechwest/workflows/tiktok-animated-reviews
```

**Checklist:**
- [ ] Python 3.8+ installed
- [ ] FFmpeg installed (`ffmpeg -version` works)
- [ ] In correct directory: `workflows/tiktok-animated-reviews`

---

### Step 2: Run Quick Setup Script

```bash
# Make script executable
chmod +x QUICK-SETUP.sh

# Run setup
./QUICK-SETUP.sh
```

**This will:**
- Create all necessary directories
- Install Python dependencies
- Check for required tools
- Guide you through next steps

**Checklist:**
- [ ] Setup script ran successfully
- [ ] All directories created
- [ ] Python packages installed

---

### Step 3: Install Python Dependencies

```bash
# Install all required packages
pip3 install -r requirements.txt

# Verify installation
python3 -c "import moviepy; print('✅ moviepy installed')"
python3 -c "import cv2; print('✅ opencv installed')"
```

**Checklist:**
- [ ] All packages installed without errors
- [ ] Can import moviepy and opencv

---

## 🎨 Phase 2: Get Your Characters (1-2 hours)

### Step 4: Extract/Export Your Characters

**From Instagram Character:**
Based on your Instagram post, you have an animated character. You need to:

**Option A: Export from Animation Tool**
- If using After Effects, Spine, Live2D, Blender, etc.
- Export as video (MP4) or image sequence (PNG)
- Recommended: Export as MP4 video loop (5-10 seconds)

**Option B: Download/Extract from Instagram**
- Use a video downloader to get the Instagram video
- Extract the character portion
- Or screen record the character animation

**Option C: Create New Characters**
- Use animation tools to create:
  - Youth character (younger version)
  - Adult character (yourself)
  - Robot character

**Checklist:**
- [ ] Youth character file ready (MP4, PNG sequence, or animation file)
- [ ] Adult character file ready
- [ ] Robot character file ready
- [ ] All characters are animated (looping animations work best)

---

### Step 5: Prepare Character Files

```bash
# Create character directories
mkdir -p assets/characters/youth
mkdir -p assets/characters/adult
mkdir -p assets/characters/robot

# Copy your character files
# Example:
cp /path/to/youth_character.mp4 assets/characters/youth/character.mp4
cp /path/to/adult_character.mp4 assets/characters/adult/character.mp4
cp /path/to/robot_character.mp4 assets/characters/robot/character.mp4
```

**File Requirements:**
- Format: MP4, AVI, MOV (video) OR PNG sequence (images)
- Duration: 5-10 second loop (will be extended automatically)
- Resolution: At least 720p (1080p recommended)
- Background: Transparent or solid color (can be removed)

**Checklist:**
- [ ] Youth character in `assets/characters/youth/`
- [ ] Adult character in `assets/characters/adult/`
- [ ] Robot character in `assets/characters/robot/`
- [ ] All files are readable and playable

---

## 🎤 Phase 3: Voice Setup (30 minutes)

### Step 6: Record Your Voice Sample

**What You Need:**
- 1-2 minutes of clear speech
- High quality audio (use good microphone if possible)
- Natural speaking (not reading a script)
- Minimal background noise

**How to Record:**
```bash
# Option 1: Use QuickTime (macOS)
# Open QuickTime > New Audio Recording
# Record 1-2 minutes of you speaking naturally
# Export as MP3

# Option 2: Use your phone
# Record voice memo
# Transfer to computer
# Convert to MP3 if needed
```

**Checklist:**
- [ ] Voice sample recorded (1-2 minutes)
- [ ] Saved as MP3 or WAV
- [ ] Good quality, clear speech

---

### Step 7: Save Voice Sample

```bash
# Create voice samples directory
mkdir -p assets/voice_samples

# Copy your voice sample
cp /path/to/your_voice_sample.mp3 assets/voice_samples/main_voice.mp3
```

**Checklist:**
- [ ] Voice sample in `assets/voice_samples/main_voice.mp3`

---

### Step 8: Get Voice Synthesis API Key

**Option 1: ElevenLabs (Recommended - Best Quality)**

1. Go to https://elevenlabs.io
2. Sign up for account
3. Go to Profile > API Keys
4. Copy your API key
5. Choose a plan:
   - **Starter**: $5/month (10,000 characters) - Good for testing
   - **Creator**: $22/month (30,000 characters) - Recommended for production

**Option 2: Google Cloud TTS (Alternative)**

1. Go to https://cloud.google.com
2. Create account
3. Enable Cloud Text-to-Speech API
4. Create service account
5. Download JSON credentials

**Checklist:**
- [ ] Account created at voice service
- [ ] API key obtained
- [ ] API key saved securely

---

### Step 9: Create Voice Clone

```bash
# Set your API key
export ELEVENLABS_API_KEY="your_api_key_here"

# Create voice clone
python3 -c "
from src.voice.voice_synthesizer import create_voice_clone
voice_id = create_voice_clone(
    'assets/voice_samples/main_voice.mp3',
    provider='elevenlabs'
)
print(f'Your voice ID: {voice_id}')
print('Save this voice ID for configuration!')
"
```

**Output:**
- You'll get a voice ID (long string of characters)
- **SAVE THIS** - you'll need it for configuration

**Checklist:**
- [ ] Voice clone created successfully
- [ ] Voice ID saved/noted

---

## ⚙️ Phase 4: Configuration (15 minutes)

### Step 10: Create Multi-Character Configuration

```bash
# Copy default config
cp config/default_config.json config/multi_character_config.json

# Edit the config file
nano config/multi_character_config.json
# OR open in your text editor
```

**Update Configuration:**

```json
{
  "output_dir": "output/reviews",
  "characters": {
    "youth": {
      "name": "youth_character",
      "file_path": "assets/characters/youth/character.mp4",
      "voice_type": "youth",
      "position": {
        "x": "right",
        "y": "center",
        "size": "medium"
      }
    },
    "adult": {
      "name": "adult_character",
      "file_path": "assets/characters/adult/character.mp4",
      "voice_type": "adult",
      "position": {
        "x": "right",
        "y": "center",
        "size": "medium"
      }
    },
    "robot": {
      "name": "robot_character",
      "file_path": "assets/characters/robot/character.mp4",
      "voice_type": "robot",
      "position": {
        "x": "right",
        "y": "center",
        "size": "medium"
      }
    }
  },
  "voice": {
    "provider": "elevenlabs",
    "api_key": "YOUR_API_KEY_HERE",
    "voice_id": "YOUR_VOICE_ID_HERE",
    "settings": {
      "stability": 0.75,
      "similarity_boost": 0.75,
      "speed": 1.0
    }
  },
  "character_selection": {
    "youth_keywords": ["youth", "kid", "student", "young", "teen"],
    "robot_keywords": ["robot", "robotics", "ai", "automation", "machine"],
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
    "model_path": null
  }
}
```

**Checklist:**
- [ ] Config file created
- [ ] All 3 character paths set correctly
- [ ] API key added
- [ ] Voice ID added
- [ ] Character selection keywords configured

---

## 🧪 Phase 5: Testing (30 minutes)

### Step 11: Test with Sample Video

**Get a Test Video:**
```bash
# Download a sample TikTok video for testing
# Or use any short video you have

# Create a test script
echo "This is a test reaction script. I'm testing the animated review system." > test_script.txt
```

**Run Test:**
```bash
# Test with adult character (default)
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "path/to/test_video.mp4" \
  --script "test_script.txt" \
  --output "output/reviews/test_adult.mp4" \
  --config "config/multi_character_config.json" \
  --character "adult"
```

**Checklist:**
- [ ] Test video downloaded/available
- [ ] Test script created
- [ ] Test run completed
- [ ] Output video generated
- [ ] Video plays correctly
- [ ] Character appears
- [ ] Voice audio plays

---

### Step 12: Test All 3 Characters

```bash
# Test Youth Character
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --output "output/reviews/test_youth.mp4" \
  --config "config/multi_character_config.json" \
  --character "youth"

# Test Adult Character
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --output "output/reviews/test_adult.mp4" \
  --config "config/multi_character_config.json" \
  --character "adult"

# Test Robot Character
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_script.txt" \
  --output "output/reviews/test_robot.mp4" \
  --config "config/multi_character_config.json" \
  --character "robot"
```

**Checklist:**
- [ ] All 3 characters tested
- [ ] All videos generated successfully
- [ ] Each character appears correctly
- [ ] Voice works for all

---

### Step 13: Test Auto-Character Selection

```bash
# Test with youth keywords in script
echo "This is a youth sports tech video for kids and students." > test_youth_script.txt
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_youth_script.txt" \
  --output "output/reviews/auto_youth.mp4" \
  --config "config/multi_character_config.json" \
  --auto-select-character

# Test with robot keywords
echo "This video is about robotics and AI automation." > test_robot_script.txt
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "test_video.mp4" \
  --script "test_robot_script.txt" \
  --output "output/reviews/auto_robot.mp4" \
  --config "config/multi_character_config.json" \
  --auto-select-character
```

**Checklist:**
- [ ] Auto-selection works for youth content
- [ ] Auto-selection works for robot content
- [ ] Auto-selection defaults to adult for other content

---

## 🔗 Phase 6: Integration (30 minutes)

### Step 14: Integrate with Existing Reaction System

**Update Your Reaction Workflow:**

```python
# In your existing reaction automation script
from workflows.tiktok_animated_reviews.src.pipeline import ReviewPipeline

def create_animated_review(tiktok_video_path, script_path, content_type="adult"):
    """Create animated review with auto character selection."""
    pipeline = ReviewPipeline(config_path="config/multi_character_config.json")
    
    # Auto-select character based on content
    character = pipeline.auto_select_character(script_path, content_type)
    
    output_path = pipeline.process(
        tiktok_video_path=tiktok_video_path,
        script_path=script_path,
        character=character
    )
    return output_path
```

**Checklist:**
- [ ] Integration code added
- [ ] Tested with existing workflow
- [ ] Works end-to-end

---

### Step 15: Update n8n Workflow (if using)

**Add New Node:**
1. Open your n8n reaction workflow
2. Add Code node after "Generate Script"
3. Add this code:

```javascript
const { ReviewPipeline } = require('./workflows/tiktok-animated-reviews/src/pipeline');

const pipeline = new ReviewPipeline({
  config_path: './config/multi_character_config.json'
});

// Auto-select character
const scriptText = $input.item.json.script_text;
const character = pipeline.auto_select_character_from_text(scriptText);

// Generate animated review
const outputPath = pipeline.process(
  $input.item.json.tiktok_video_path,
  $input.item.json.script_path,
  character
);

return {
  json: {
    animated_review_path: outputPath,
    character_used: character,
    ...$input.item.json
  }
};
```

**Checklist:**
- [ ] n8n node added
- [ ] Tested in n8n
- [ ] Works with existing workflow

---

## 🚀 Phase 7: Production Use (Ongoing)

### Step 16: Use in Production

**Daily Workflow:**
1. Find TikTok video (existing automation)
2. Generate reaction script (existing automation)
3. **NEW**: System auto-selects character based on content
4. **NEW**: Generate animated review video
5. Publish to platforms (existing automation)

**Command:**
```bash
# For manual use
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "path/to/video.mp4" \
  --script "path/to/script.txt" \
  --config "config/multi_character_config.json" \
  --auto-select-character
```

**Checklist:**
- [ ] System integrated into daily workflow
- [ ] Auto-character selection working
- [ ] Videos generating correctly
- [ ] Publishing automation working

---

## 🎨 Character Creation Tips

### If You Need to Create Characters:

**Option 1: Use Animation Tools**
- **After Effects**: Create simple character animation, export as MP4
- **Spine**: 2D skeletal animation (great for characters)
- **Live2D**: 2D character animation with facial expressions
- **Blender**: 3D character animation (more complex)

**Option 2: Use AI Tools**
- **RunwayML**: Generate animated characters
- **Stable Diffusion**: Generate character images, animate separately
- **D-ID**: Animate static character images

**Option 3: Simple Video Loop**
- Record yourself with green screen
- Create simple animated version
- Export as looping MP4

---

## 📊 Quick Reference

### File Locations
```
workflows/tiktok-animated-reviews/
├── assets/
│   ├── characters/
│   │   ├── youth/character.mp4
│   │   ├── adult/character.mp4
│   │   └── robot/character.mp4
│   └── voice_samples/main_voice.mp3
├── config/multi_character_config.json
└── output/reviews/
```

### Environment Variables
```bash
export ELEVENLABS_API_KEY="your_key_here"
```

### Common Commands
```bash
# Generate review
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "video.mp4" \
  --script "script.txt" \
  --config "config/multi_character_config.json" \
  --auto-select-character

# Test specific character
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "video.mp4" \
  --script "script.txt" \
  --character "youth" \
  --config "config/multi_character_config.json"
```

---

## ✅ Final Checklist

**Setup Complete When:**
- [ ] All 3 characters in place
- [ ] Voice sample recorded and cloned
- [ ] API key configured
- [ ] Config file set up
- [ ] All 3 characters tested
- [ ] Auto-selection working
- [ ] Integrated with existing workflow
- [ ] Production ready

---

## 🆘 Troubleshooting

### Character Not Appearing
- Check file path in config
- Verify file format is supported
- Check file permissions

### Voice Not Working
- Verify API key is correct
- Check voice ID is valid
- Test API quota/limits

### Auto-Selection Not Working
- Check keywords in config
- Verify script text contains keywords
- Test with explicit character flag

---

## 📝 Next Steps After Setup

1. **Refine Characters**: Adjust animations, positions, sizes
2. **Tune Voice**: Adjust stability, similarity, speed settings
3. **Optimize Layout**: Try different compositions
4. **Scale Up**: Process multiple videos
5. **Monitor**: Track quality, costs, performance

---

**Total Time Estimate: 3-4 hours for complete setup**

**Status**: Ready to build! 🚀

