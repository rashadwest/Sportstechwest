# Priority Order - What to Do First

**Ordered by importance for getting the system working**

---

## 🔴 TIER 1: CRITICAL - Do These First (15 minutes)

### 1. Create ElevenLabs Account & Get API Key
**Priority: #1 - BLOCKS EVERYTHING ELSE**

**Why Critical:**
- Required for voice synthesis
- Nothing works without this
- Takes 5 minutes

**What to Do:**
1. Go to https://elevenlabs.io
2. Sign up (free account works)
3. Go to Profile > API Keys
4. Copy your API key

**Time:** 5 minutes  
**Can't Skip:** System won't work without this

---

### 2. Record Voice Sample
**Priority: #2 - REQUIRED FOR VOICE CLONING**

**Why Critical:**
- Need your voice to clone
- Required before voice synthesis works
- Takes 10 minutes

**What to Do:**
1. Record 1-2 minutes of clear speech
2. Use QuickTime (macOS) or phone
3. Speak naturally (not reading)
4. Save as MP3
5. Place in: `assets/voice_samples/main_voice.mp3`

**Time:** 10 minutes  
**Can't Skip:** Need your actual voice

---

## 🟡 TIER 2: IMPORTANT - Do Next (1-2 hours)

### 3. Get/Create 3 Characters
**Priority: #3 - CORE FUNCTIONALITY**

**Why Important:**
- System needs characters to animate
- Can test with just one character first
- Takes 1-2 hours (mostly creative work)

**What to Do:**
1. Extract from Instagram: https://www.instagram.com/p/DQxNseoEdnE/
   - Use video downloader or screen recording
   - Or export from animation tool
2. Create 3 variations:
   - **Youth character** (younger version)
   - **Adult character** (your character)
   - **Robot character** (robot version)
3. Save to:
   - `assets/characters/youth/character.mp4`
   - `assets/characters/adult/character.mp4`
   - `assets/characters/robot/character.mp4`

**Time:** 1-2 hours  
**Can Test With:** Just one character to start

---

## 🟢 TIER 3: EASY - Automated/Quick (5 minutes)

### 4. Run Setup Wizard
**Priority: #4 - FULLY AUTOMATED**

**Why Easy:**
- Automated script does everything
- Just answer prompts
- Takes 5 minutes

**What to Do:**
```bash
cd workflows/tiktok-animated-reviews
python3 setup_wizard.py
```

**What It Does:**
- Asks for API key
- Asks for voice sample path
- Creates voice clone automatically
- Generates config file
- Validates everything

**Time:** 5 minutes  
**Automated:** Yes, just run the script

---

### 5. Voice Clone Creation
**Priority: #5 - AUTOMATED BY WIZARD**

**Why Easy:**
- Setup wizard does this automatically
- No manual steps needed
- Takes 2 minutes (automated)

**What to Do:**
- Already done by setup wizard!
- Or run manually if needed:
```bash
export ELEVENLABS_API_KEY="your_key"
python3 -c "from src.voice.voice_synthesizer import create_voice_clone; print(create_voice_clone('assets/voice_samples/main_voice.mp3'))"
```

**Time:** 2 minutes (automated)  
**Automated:** Yes, by setup wizard

---

## 📊 Summary Table

| Priority | Task | Time | Automated | Critical |
|----------|------|------|-----------|----------|
| #1 | Get API Key | 5 min | ❌ No | ✅ Yes |
| #2 | Record Voice | 10 min | ❌ No | ✅ Yes |
| #3 | Get Characters | 1-2 hrs | ⚠️ Partial | ⚠️ Important |
| #4 | Run Setup Wizard | 5 min | ✅ Yes | ❌ No |
| #5 | Voice Clone | 2 min | ✅ Yes | ❌ No |

---

## 🚀 Quick Start Path

### Fastest Way to Get Running:

1. **Get API Key** (5 min) → https://elevenlabs.io
2. **Record Voice** (10 min) → QuickTime or phone
3. **Run Setup Wizard** (5 min) → `python3 setup_wizard.py`
4. **Add One Character** (30 min) → Test with just adult character
5. **Test System** (5 min) → Verify it works
6. **Add Other Characters** (1-2 hrs) → When ready

**Total to First Test: ~1 hour**  
**Total to Full System: ~2-3 hours**

---

## 💡 Pro Tips

### Start Minimal:
- Get API key + voice sample first
- Test with just ONE character
- Add other characters later

### Use Automation:
- Run `setup_wizard.py` - it does most of the work
- Don't manually create config files
- Let the wizard handle voice cloning

### Test Early:
- Test with one character first
- Verify voice works
- Then add other characters

---

## ✅ Checklist (In Order)

- [ ] **#1** Get ElevenLabs API key (5 min)
- [ ] **#2** Record voice sample (10 min)
- [ ] **#4** Run setup wizard (5 min)
- [ ] **#3** Get at least one character (30 min)
- [ ] Test system works
- [ ] **#3** Add other characters (1-2 hrs)

**Do #1 and #2 first - they block everything else!**

