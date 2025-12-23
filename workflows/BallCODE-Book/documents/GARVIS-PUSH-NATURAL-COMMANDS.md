# Garvis Push - Natural Language Commands
## Simple "website push" and "game push" Commands

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Status:** ✅ **COMPLETE - READY TO USE**

---

## 🚀 NATURAL LANGUAGE COMMANDS

### **Simple Commands:**

```bash
# Push website
python scripts/garvis-push-command.py website
# OR
./push website

# Push game
python scripts/garvis-push-command.py game
# OR
./push game

# Push everything
python scripts/garvis-push-command.py all
# OR
./push all
```

---

## 📋 COMMAND OPTIONS

### **Website Push:**
```bash
python scripts/garvis-push-command.py website
python scripts/garvis-push-command.py web
python scripts/garvis-push-command.py site
```

**What it does:**
- Checks `BallCode/` for changes
- Commits and pushes to `rashadwest/BallCode`
- Netlify auto-deploys (if connected)

### **Game Push:**
```bash
python scripts/garvis-push-command.py game
python scripts/garvis-push-command.py games
python scripts/garvis-push-command.py unity
```

**What it does:**
- Checks for level files
- Pushes to `rashadwest/BTEBallCODE`
- Triggers Unity build
- GitHub Actions builds and deploys

### **Push All:**
```bash
python scripts/garvis-push-command.py all
python scripts/garvis-push-command.py everything
python scripts/garvis-push-command.py both
```

**What it does:**
- Pushes website
- Pushes game
- Triggers builds

---

## 🎯 QUICK REFERENCE

| Command | What It Does |
|---------|--------------|
| `./push website` | Push website only |
| `./push game` | Push game levels only |
| `./push all` | Push everything |

---

## ✅ USAGE EXAMPLES

### **Example 1: Push Website**
```bash
./push website
```

**Output:**
- Checks for website changes
- Pushes if changes exist
- Shows status

### **Example 2: Push Game**
```bash
./push game
```

**Output:**
- Checks for level files
- Pushes to Unity repo
- Triggers Unity build
- Shows status

### **Example 3: Push Everything**
```bash
./push all
```

**Output:**
- Pushes website
- Pushes game
- Triggers builds
- Shows summary

---

## 🔧 ALTERNATIVE: Direct Python

**You can also use the direct Python command:**

```bash
# Website
python scripts/garvis-push.py --website

# Game
python scripts/garvis-push.py --game

# All
python scripts/garvis-push.py --all
```

---

## 📊 SYSTEM INTEGRATION

**All commands use the same Garvis Push system:**
- `./push website` → `garvis-push.py --website`
- `./push game` → `garvis-push.py --game`
- `./push all` → `garvis-push.py --all`

**Same functionality, simpler commands!**

---

## 🚀 QUICK START

**Just say:**
- "website push" → Run `./push website`
- "game push" → Run `./push game`
- "push all" → Run `./push all`

**That's it!**

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** ✅ Ready to use

