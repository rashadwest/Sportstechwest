# User Preference: Environment Variables in ~/.zshrc

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** ✅ **SAVED TO MEMORY**

---

## 🎯 USER PREFERENCE

**User wants all environment variables saved to `~/.zshrc` from now on, as long as it's safe.**

**This preference is now saved to memory and will be followed for all future variable setups.**

---

## ✅ SAFE PRACTICES

**What makes it safe:**
- ✅ Variables are added to `~/.zshrc` (user's shell profile)
- ✅ No duplicates - script checks before adding
- ✅ Safe script created: `scripts/safe-add-to-zshrc.sh`
- ✅ Backs up before modifying (creates `.bak` file)
- ✅ Asks before replacing existing variables
- ✅ Adds comments with timestamps

**What to avoid:**
- ❌ Never add secrets without user's explicit permission
- ❌ Never overwrite without asking
- ❌ Never add to system-wide files (only user's `~/.zshrc`)

---

## 🔧 SAFE SCRIPT USAGE

**Add a variable safely:**
```bash
./scripts/safe-add-to-zshrc.sh VARIABLE_NAME "value"
```

**Example:**
```bash
./scripts/safe-add-to-zshrc.sh NETLIFY_SITE_ID "39ebfb47-c716-4f38-8f8b-7bfba36f3dc7"
./scripts/safe-add-to-zshrc.sh NETLIFY_AUTH_TOKEN "your_token_here"
```

**What it does:**
1. Checks if variable already exists
2. If exists → asks if you want to replace
3. If new → adds to end of `~/.zshrc`
4. Creates backup (`.bak` file)
5. Adds timestamp comment

---

## 📋 CURRENT NETLIFY VARIABLES

**To add Netlify variables now:**
```bash
cd /Users/rashadwest/BTEBallCODE
./scripts/safe-add-to-zshrc.sh NETLIFY_SITE_ID "39ebfb47-c716-4f38-8f8b-7bfba36f3dc7"
./scripts/safe-add-to-zshrc.sh NETLIFY_AUTH_TOKEN "your_token_here"
source ~/.zshrc
```

---

## 🚀 FUTURE VARIABLES

**For any new environment variables:**
- ✅ Always use `safe-add-to-zshrc.sh` script
- ✅ Always ask user before adding secrets/tokens
- ✅ Always add to `~/.zshrc` (not system-wide)
- ✅ Always check for duplicates first
- ✅ Always create backup before modifying

---

## 📝 SCRIPT LOCATIONS

**Available in:**
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/safe-add-to-zshrc.sh`
- `/Users/rashadwest/BTEBallCODE/scripts/safe-add-to-zshrc.sh`

**Both locations have the same safe script.**

---

## ✅ MEMORY SAVED

**This preference is now saved:**
- ✅ User wants all variables in `~/.zshrc`
- ✅ Must be safe (no duplicates, backups, ask before replace)
- ✅ Use `safe-add-to-zshrc.sh` script for all additions
- ✅ This applies to all future variable setups

---

**Status:** ✅ **PREFERENCE SAVED TO MEMORY** - Will be followed for all future variable setups

