# 🧪 Full Integration Workflow - Testing & Usage Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Purpose:** Complete guide on testing and using the Full Integration workflow  
**Status:** ✅ Active Guide

---

## 🎯 QUICK SUMMARY

**What is Full Integration?**
- AI-driven workflow that updates all 4 systems (Game, Curriculum, Book, Website) from one prompt
- Uses AIMCODE methodology (Demis Hassabis - Alpha Evolve approach)
- Analyzes your prompt and determines what needs updating across all systems

**Webhook URL:**
- Production: `http://192.168.1.226:5678/webhook/ballcode-dev`
- Test: `http://192.168.1.226:5678/webhook-test/ballcode-dev`

**Status:** ✅ WORKING (according to daily report)

---

## 📋 BEST WAY TO PROMPT IT

### ✅ GOOD PROMPTS (What to Use)

**1. Multi-System Updates:**
```json
{
  "prompt": "Add a new exercise for Book 1 that teaches sequences",
  "mode": "quick"
}
```
**What it does:** Updates Game (creates exercise), Curriculum (adds to schema), Book (adds exercise button), Website (adds link)

**2. Clear Development Goals:**
```json
{
  "prompt": "Update Book 2 to include pattern recognition concepts",
  "mode": "full"
}
```
**What it does:** Analyzes Book 2, updates curriculum schema, creates game exercises, updates website pages

**3. AI-Determined Updates:**
```json
{
  "prompt": "Create a new lesson about loops for Book 3",
  "mode": "quick"
}
```
**What it does:** AI determines what game exercises, book content, curriculum updates, and website changes are needed

**4. Comprehensive Integration:**
```json
{
  "prompt": "Add conditionals exercise to Book 3 game level",
  "mode": "full"
}
```
**What it does:** Creates game level, updates curriculum, adds to book content, updates website

---

### ❌ BAD PROMPTS (What NOT to Use)

**1. Single System Only:**
```json
{
  "prompt": "Update just the website homepage"
}
```
**Why not:** Use direct Python script or manual edit instead - Full Integration is for multi-system updates

**2. Simple File Edits:**
```json
{
  "prompt": "Fix typo in Book 1"
}
```
**Why not:** Too simple - just edit the file directly

**3. Immediate Results Needed:**
```json
{
  "prompt": "Change button color to blue"
}
```
**Why not:** Full Integration uses AI analysis (takes time) - use direct scripts for faster results

---

## 🚀 HOW TO TEST IT

### Step 1: Ensure Workflow is Active

1. Open n8n: `http://192.168.1.226:5678`
2. Find workflow: "BallCODE Full Integration - AI Analysis (Simplified)" or similar
3. Click the **"Active"** toggle (top-right) to turn it ON
4. Wait a few seconds for webhook to register

### Step 2: Test with Default Prompt

**Quick Test (Recommended):**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a simple test exercise for Book 1 that teaches sequences",
    "mode": "quick"
  }'
```

**Full Test (More Comprehensive):**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add conditionals exercise to Book 3 game level",
    "mode": "full"
  }'
```

**If Production URL Doesn't Work, Try Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Test prompt",
    "mode": "quick"
  }'
```

### Step 3: Check Response

**Expected Response Format:**
```json
{
  "status": "success",
  "actionPlan": {
    "analysis": "...",
    "systemsAffected": ["game", "curriculum", "book", "website"],
    "updates": {...}
  },
  "integrationReport": {
    "gameUpdates": "...",
    "curriculumUpdates": "...",
    "bookUpdates": "...",
    "websiteUpdates": "..."
  }
}
```

---

## 📊 WHAT YOU GET FROM USING IT

### 1. **Comprehensive Analysis**
- AI analyzes your prompt using AIMCODE methodology
- Identifies which systems need updating
- Creates action plan for all affected systems

### 2. **Multi-System Updates**
- **Game:** Creates Unity exercise JSON, level data
- **Curriculum:** Updates unified schema
- **Book:** Adds exercise buttons, content updates
- **Website:** Updates pages, adds links

### 3. **Memory Context**
- Saves context automatically for continuity
- Tracks what was updated
- Enables follow-up prompts

### 4. **Integration Report**
- Complete report of all changes
- Shows what was updated in each system
- Provides verification of integration

---

## 🎯 RECOMMENDED DEFAULT PROMPT FOR TESTING

**Best Default Prompt to Start With:**
```json
{
  "prompt": "Create a simple test exercise for Book 1 that teaches sequences. Make it connect to the game, curriculum, and website.",
  "mode": "quick"
}
```

**Why This Prompt Works:**
- ✅ Clear goal (test exercise)
- ✅ Specific book (Book 1)
- ✅ Specific concept (sequences)
- ✅ Multi-system (game, curriculum, website)
- ✅ Quick mode (faster response)

**What You'll Get:**
1. Analysis of the prompt
2. Game exercise JSON created
3. Curriculum schema updated
4. Book content updated
5. Website link added
6. Integration report

---

## ⚠️ TROUBLESHOOTING

### Webhook Not Registered (404 Error)

**Problem:**
```json
{"code":404,"message":"The requested webhook \"ballcode-dev\" is not registered."}
```

**Solution:**
1. Open n8n UI: `http://192.168.1.226:5678`
2. Find the Full Integration workflow
3. Click "Active" toggle to turn it ON
4. Wait 5-10 seconds
5. Try webhook again

### Workflow Not Executing

**Check:**
1. Is workflow active? (green toggle in n8n)
2. Are credentials configured? (OpenAI API key)
3. Check n8n execution logs
4. Verify webhook path is correct

### Slow Response

**Normal:** Full Integration uses AI analysis, can take 30-60 seconds
**If too slow:** Use "quick" mode instead of "full" mode

---

## 📝 MODE OPTIONS

### "quick" Mode
- ✅ Faster response (5-10 seconds)
- ✅ Uses quick 5-question framework
- ✅ Good for simple updates
- ✅ Recommended for testing

### "full" Mode
- ✅ More comprehensive (30-60 seconds)
- ✅ Uses full 23-question framework
- ✅ Better for complex updates
- ✅ More thorough analysis

---

## 🔄 WORKFLOW REVIEW FROM YESTERDAY

**To Check Yesterday's Executions:**
1. Open n8n UI: `http://192.168.1.226:5678`
2. Click "Executions" tab (left sidebar)
3. Filter by workflow: "Full Integration"
4. Review execution history
5. Check for any errors or issues

**What to Look For:**
- ✅ Successful executions (green)
- ⚠️ Failed executions (red) - check error messages
- 📊 Execution times (should be 30-60 seconds)
- 📝 Response data (check integration reports)

---

## 🎯 NEXT STEPS

1. **Test with default prompt** (see above)
2. **Review execution results** in n8n UI
3. **Check integration report** for what was updated
4. **Verify changes** in Game, Curriculum, Book, Website
5. **Use for real updates** once you understand the flow

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Last Updated:** December 22, 2025


