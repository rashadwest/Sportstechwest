# Execute Screenshot Analysis - What You Need to Do

**Quick Reference:** Steps to analyze BallCODE game screenshots

---

## Decision: Choose Your API

**Option 1: OpenAI GPT-4 Vision (Recommended - Easiest)**
- ✅ Most accessible
- ✅ Good documentation
- ✅ Free tier: $5 credit
- 🔗 Sign up: https://platform.openai.com/api-keys

**Option 2: Anthropic Claude Vision**
- ✅ Also excellent quality
- ✅ Free tier available
- 🔗 Sign up: https://console.anthropic.com/

**Your Choice:** Pick one (OpenAI is recommended for simplicity)

---

## Step-by-Step: What You Need to Do

### Step 1: Get API Key (5 minutes)

**If choosing OpenAI:**
1. Go to: https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)
5. ⚠️ **Save it somewhere safe** - you won't see it again!

**If choosing Anthropic:**
1. Go to: https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys
4. Create new key
5. Copy the key

**Decision Needed:** Which API do you want to use? (OpenAI recommended)

---

### Step 2: Install Python Library (1 minute)

Open terminal and run:

**For OpenAI:**
```bash
pip install openai
```

**For Anthropic:**
```bash
pip install anthropic
```

**What You Need:**
- Terminal/command line access
- Python installed (you likely have this)
- Internet connection

**Decision Needed:** None - just run the command

---

### Step 3: Set API Key (1 minute)

**Option A: Set Environment Variable (Recommended)**

**On Mac/Linux:**
```bash
export OPENAI_API_KEY="your-key-here"
# OR
export ANTHROPIC_API_KEY="your-key-here"
```

**On Windows:**
```cmd
set OPENAI_API_KEY=your-key-here
# OR
set ANTHROPIC_API_KEY=your-key-here
```

**Option B: Pass as Command Line Argument**
- You can pass `--api-key` when running the script
- Less secure but works

**What You Need:**
- Your API key from Step 1
- Terminal access

**Decision Needed:** Environment variable (recommended) or command line argument?

---

### Step 4: Run the Analysis (10-15 minutes)

**Command to run:**

```bash
# Navigate to project directory
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Analyze tutorial (Watson1)
python analyze_game_screenshots.py "My Books/BallCODE_Watson1" --api openai --output watson1_analysis.json

# Then Watson2
python analyze_game_screenshots.py "My Books/BallCODE_Watson2" --api openai --output watson2_analysis.json

# Then CiscoIQ
python analyze_game_screenshots.py "My Books/BallCODE_CiscoIQ" --api openai --output ciscoiq_analysis.json
```

**What Happens:**
- Script analyzes each screenshot (one at a time)
- Shows progress: `[1/11] Analyzing: Screenshot...`
- Saves results to JSON files
- Takes ~10-15 minutes total (depends on API speed)

**What You Need:**
- Terminal access
- Wait for it to complete (you can do other things)
- Internet connection

**Decision Needed:** 
- Run all three directories? (Recommended)
- Or start with just tutorial (Watson1)?

---

### Step 5: Share Results (1 minute)

**What I Need From You:**
- The JSON files created (`watson1_analysis.json`, etc.)
- OR just tell me when it's done and I'll read them

**What I'll Do:**
- Read the analysis results
- Document level mechanics
- Update BallCODE-Level-Mechanics-Analysis.md
- Save key information to memory
- Create summary of game understanding

**Decision Needed:** None - just share the files or let me know when done

---

## Summary: What You Need

### Required From You:
1. ✅ **API Key** - Get from OpenAI or Anthropic (5 min)
2. ✅ **Install Library** - Run `pip install openai` (1 min)
3. ✅ **Set API Key** - Export environment variable (1 min)
4. ✅ **Run Script** - Execute analysis commands (10-15 min)
5. ✅ **Share Results** - Give me the JSON files or tell me when done (1 min)

### Total Time: ~20 minutes (mostly waiting)

### Decisions You Need to Make:
1. **Which API?** (OpenAI recommended)
2. **Environment variable or command line?** (Environment variable recommended)
3. **Run all directories or start with tutorial?** (All recommended)

---

## Alternative: If You Don't Want to Use API

**Option: Manual Description**
- You describe screenshots to me
- I'll structure the information
- We build understanding together
- No API needed, but takes longer

**Option: Free Image Tools**
- Use Google Lens or similar
- Copy descriptions
- Share with me
- I'll structure and document

**Decision Needed:** API analysis (recommended) or manual approach?

---

## Troubleshooting

### "pip: command not found"
- Try: `pip3 install openai`
- Or: `python3 -m pip install openai`

### "API key not found"
- Make sure you exported it: `echo $OPENAI_API_KEY` (should show your key)
- Or use `--api-key` argument

### "Module not found"
- Make sure you installed: `pip install openai`
- Check Python version: `python --version` (need 3.7+)

### "Permission denied"
- Try: `python3 analyze_game_screenshots.py` instead of `python`

---

## Ready to Start?

**Quick Start (3 commands):**
```bash
# 1. Install
pip install openai

# 2. Set key (replace with your actual key)
export OPENAI_API_KEY="sk-your-actual-key-here"

# 3. Run (start with tutorial)
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python analyze_game_screenshots.py "My Books/BallCODE_Watson1" --api openai
```

**That's it!** The script will do the rest.

---

## What Happens Next?

1. **Script analyzes screenshots** → Creates JSON files
2. **You share results** → Give me the JSON files
3. **I document mechanics** → Update analysis document
4. **I save to memory** → Key mechanics for future reference
5. **We build stories** → Use game understanding for better stories

**Total effort from you: ~20 minutes**  
**Result: Complete understanding of all game levels**

---

**Questions?** Just ask! I can help with any step.



