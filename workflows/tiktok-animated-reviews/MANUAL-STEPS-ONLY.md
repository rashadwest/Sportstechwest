# Manual Steps Only - What YOU Need to Do

**Everything else is automated. Just do these manual steps:**

---

## 🎨 1. Get Your 3 Characters

**What:** Extract/create 3 animated character files

**How:**
- Extract character from Instagram: https://www.instagram.com/p/DQxNseoEdnE/
  - Use video downloader or screen recording
  - Or export from your animation tool
- Create 3 variations:
  - **Youth character** (younger version)
  - **Adult character** (your character)
  - **Robot character** (robot version)

**Save to:**
```
workflows/tiktok-animated-reviews/assets/characters/youth/character.mp4
workflows/tiktok-animated-reviews/assets/characters/adult/character.mp4
workflows/tiktok-animated-reviews/assets/characters/robot/character.mp4
```

**Format:** MP4, AVI, MOV, or PNG sequence

---

## 🎤 2. Record Your Voice Sample

**What:** Record 1-2 minutes of your voice speaking naturally

**How:**
- Use QuickTime (macOS) or your phone
- Speak naturally (not reading a script)
- High quality, minimal background noise
- Export as MP3

**Save to:**
```
workflows/tiktok-animated-reviews/assets/voice_samples/main_voice.mp3
```

---

## 🔑 3. Get ElevenLabs API Key

**What:** Sign up and get API key for voice cloning

**How:**
1. Go to https://elevenlabs.io
2. Sign up (free account works for testing)
3. Go to Profile > API Keys
4. Copy your API key

**Save:** Copy the API key (you'll use it in config)

---

## 🎯 4. Create Voice Clone

**What:** Create your voice clone using the API

**Run this command:**
```bash
cd workflows/tiktok-animated-reviews
export ELEVENLABS_API_KEY="your_api_key_here"
python3 -c "from src.voice.voice_synthesizer import create_voice_clone; print(create_voice_clone('assets/voice_samples/main_voice.mp3', provider='elevenlabs'))"
```

**Save:** Copy the voice ID that gets printed

---

## ⚙️ 5. Configure Settings

**What:** Edit config file with your paths and keys

**File:** `workflows/tiktok-animated-reviews/config/my_config.json`

**Update these values:**
- Character file paths (3 paths)
- API key
- Voice ID

**Example:**
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
    "api_key": "YOUR_API_KEY_HERE",
    "voice_id": "YOUR_VOICE_ID_HERE"
  }
}
```

---

## ✅ That's It!

**Everything else is automated:**
- ✅ System setup (run `./QUICK-SETUP.sh`)
- ✅ Dependency installation
- ✅ Character selection logic
- ✅ Voice synthesis
- ✅ Video composition
- ✅ Integration code

**After these 5 steps, you're ready to use:**
```bash
python3 src/pipeline/review_pipeline.py \
  --tiktok-video "video.mp4" \
  --script "script.txt" \
  --config "config/my_config.json" \
  --auto-select-character
```

---

## 📋 Quick Checklist

- [ ] 3 character files saved
- [ ] Voice sample recorded and saved
- [ ] ElevenLabs account created
- [ ] API key obtained
- [ ] Voice clone created (voice ID saved)
- [ ] Config file updated with all paths and keys

**Total Manual Time: ~2-3 hours**

