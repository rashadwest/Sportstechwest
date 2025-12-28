# Garvis Push System - Permanent Memory
## One-Command Deployment - SAVED TO MEMORY

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Status:** ✅ **PERMANENT SYSTEM - SAVED TO MEMORY**

---

## 💾 MEMORY FORMAT (SAVE THIS)

```
Garvis Push System (Complete & Permanent):
- Command: python scripts/garvis-push.py → One-command deployment for website and game → Automatically checks for changes, commits, pushes to GitHub, triggers builds → Works with or without local Unity repo → Provides clear status and instructions
- Usage: python scripts/garvis-push.py (deploy all) | --website (website only) | --game (game only) | --message "custom" (custom commit message)
- Website: Checks BallCode/ directory → Commits and pushes to rashadwest/BallCode → Netlify auto-deploys if connected
- Game: Checks Unity-Scripts/Levels/ for level files → Copies to Unity repo if local → Commits and pushes to rashadwest/BTEBallCODE → Triggers Unity build via n8n → GitHub Actions builds and deploys to Netlify → If Unity repo not local, provides GitHub UI instructions
- Features: Automatic change detection, smart error handling, graceful fallbacks, clear status messages, manual instructions when needed
- Status: Complete permanent system - use this for all deployments instead of manual git commands
- Rules: Added to .cursorrules - AI must always suggest garvis-push.py for deployments
```

---

## 🚀 QUICK REFERENCE

**Deploy Everything:**
```bash
python scripts/garvis-push.py
```

**Deploy Website Only:**
```bash
python scripts/garvis-push.py --website
```

**Deploy Game Only:**
```bash
python scripts/garvis-push.py --game
```

**Custom Message:**
```bash
python scripts/garvis-push.py --all --message "Your message"
```

---

## ✅ WHAT IT DOES

1. **Checks for changes** automatically
2. **Commits and pushes** to GitHub
3. **Handles website** deployment
4. **Handles game** deployment
5. **Triggers builds** when needed
6. **Provides instructions** if manual steps needed
7. **Shows clear status** and next steps

---

## 📋 SYSTEM INTEGRATION

**Part of complete Garvis system:**
- `garvis-push.py` - Quick deployment (this one)
- `garvis-command.py` - Full workflow orchestration
- `garvis-deploy-all.py` - Complete deployment with API

**Use `garvis-push.py` for:**
- Quick deployments
- Simple push operations
- When you just want to "push everything"

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** ✅ Permanent Memory - Use for all deployments


