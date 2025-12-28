# Garvis Push System - Complete & Permanent
## One-Command Deployment from Any Prompt

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Status:** ✅ **COMPLETE - PERMANENT SYSTEM**

---

## 🚀 ONE-COMMAND DEPLOYMENT

### **Simple Usage:**

```bash
# Deploy everything (website + game)
python scripts/garvis-push.py

# Deploy website only
python scripts/garvis-push.py --website

# Deploy game levels only
python scripts/garvis-push.py --game

# Custom commit message
python scripts/garvis-push.py --all --message "Your custom message"
```

**That's it!** Garvis handles everything automatically.

---

## ✅ WHAT GARVIS PUSH DOES

### **Website Deployment:**
1. ✅ Checks for changes in `BallCode/` directory
2. ✅ Commits changes automatically
3. ✅ Pushes to GitHub (`rashadwest/BallCode`)
4. ✅ Netlify auto-deploys (if connected)

### **Game Deployment:**
1. ✅ Checks for level files
2. ✅ Copies levels to Unity repo (if local)
3. ✅ Commits and pushes to GitHub (`rashadwest/BTEBallCODE`)
4. ✅ Triggers Unity build via n8n (if available)
5. ✅ GitHub Actions builds and deploys to Netlify

### **Smart Handling:**
- ✅ Skips if no changes
- ✅ Provides manual instructions if Unity repo not local
- ✅ Handles errors gracefully
- ✅ Shows clear status messages

---

## 📋 SYSTEM FEATURES

### **Automatic Detection:**
- Detects if changes exist
- Detects if Unity repo is local
- Detects if level files exist
- Detects if builds are locked

### **Error Handling:**
- Graceful fallbacks
- Clear error messages
- Manual instructions when needed
- Continues with other deployments if one fails

### **Status Reporting:**
- Color-coded output
- Clear success/error messages
- Summary at the end
- Next steps provided

---

## 🎯 USAGE EXAMPLES

### **Example 1: Deploy Everything**
```bash
python scripts/garvis-push.py
```

**Output:**
- Checks website for changes
- Pushes website if changes exist
- Checks game levels
- Pushes game levels if Unity repo is local
- Triggers Unity build
- Shows summary

### **Example 2: Deploy Website Only**
```bash
python scripts/garvis-push.py --website
```

**Output:**
- Only checks and pushes website
- Skips game deployment

### **Example 3: Deploy Game Only**
```bash
python scripts/garvis-push.py --game
```

**Output:**
- Only checks and pushes game levels
- Triggers Unity build
- Skips website deployment

### **Example 4: Custom Message**
```bash
python scripts/garvis-push.py --all --message "Add new features"
```

**Output:**
- Uses custom commit message
- Deploys everything

---

## 🔧 HOW IT WORKS

### **Website Push:**
1. Checks `BallCode/` directory for changes
2. If changes exist:
   - `git add -A`
   - `git commit -m "message"`
   - `git push origin main`
3. Netlify auto-deploys (if connected)

### **Game Push:**
1. Checks if Unity repo is local (`Unity-Scripts/.git`)
2. If local:
   - Copies level files to `Assets/StreamingAssets/Levels/`
   - `git add -A`
   - `git commit -m "message"`
   - `git push origin main`
   - Triggers Unity build via n8n
3. If not local:
   - Provides GitHub UI instructions
   - User uploads manually

---

## 📊 OUTPUT FORMAT

**Garvis Push provides:**
- ✅ Clear section headers
- ✅ Color-coded status messages
- ✅ Success/error indicators
- ✅ File lists when relevant
- ✅ Manual instructions when needed
- ✅ Summary at the end
- ✅ Next steps

---

## 🎯 INTEGRATION WITH GARVIS

**Garvis Push is part of the complete Garvis system:**

- **Garvis Command:** `python scripts/garvis-command.py` - Full workflow orchestration
- **Garvis Push:** `python scripts/garvis-push.py` - Quick deployment
- **Garvis Deploy All:** `python scripts/garvis-deploy-all.py` - Complete deployment with API

**Choose based on your needs:**
- **Quick push?** → `garvis-push.py`
- **Full workflow?** → `garvis-command.py`
- **API deployment?** → `garvis-deploy-all.py`

---

## ✅ PERMANENT SYSTEM

**This is now part of the permanent Garvis system:**

1. **Script:** `scripts/garvis-push.py`
   - One-command deployment
   - Handles website and game
   - Smart error handling

2. **Documentation:** `documents/GARVIS-PUSH-SYSTEM-COMPLETE.md`
   - Complete usage guide
   - Examples and troubleshooting

3. **Integration:** Works with existing Garvis system
   - Uses same paths and repositories
   - Compatible with other Garvis tools

---

## 🚀 QUICK START

**Just run:**
```bash
python scripts/garvis-push.py
```

**Garvis will:**
- ✅ Check what needs to be pushed
- ✅ Push automatically
- ✅ Show you what happened
- ✅ Tell you next steps

**No configuration needed - it just works!**

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** ✅ Complete - Permanent System


