# Robot Dashboard - Quick Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** ✅ Ready to Use

---

## ⚡ QUICK COMMANDS

### Single Robot Command for Everything

```bash
robot-dashboard [command]
```

---

## 🚀 COMMANDS

### Setup (First Time)
```bash
robot-dashboard setup
```
**What it does:**
- Sets environment variables
- Updates dashboard data
- Verifies everything is working

### Update Dashboard
```bash
robot-dashboard update
```
**What it does:**
- Fetches latest build status
- Updates markdown and HTML dashboards
- Refreshes all data

### View Dashboard (Markdown)
```bash
robot-dashboard view
```
**What it does:**
- Shows markdown dashboard in terminal
- Quick text view

### Serve Dashboard (HTML - Web View)
```bash
robot-dashboard serve
```
**What it does:**
- Starts web server on localhost:8000
- Opens beautiful HTML dashboard
- Auto-refreshes every 5 minutes

### Check Status
```bash
robot-dashboard status
```
**What it does:**
- Shows all dashboard files
- Shows environment variables
- Shows alias status
- Complete system check

### Set Environment Variables
```bash
robot-dashboard env
```
**What it does:**
- Sets/updates environment variables
- Backs up ~/.zshrc
- Shows what needs manual setup

---

## 📋 COMMON WORKFLOWS

### First Time Setup
```bash
robot-dashboard setup
source ~/.zshrc
robot-dashboard view
```

### Daily Check
```bash
robot-dashboard update
robot-dashboard view
```

### Web Dashboard Session
```bash
robot-dashboard serve
# Then open: http://localhost:8000/dashboard.html
```

### Check System Health
```bash
robot-dashboard status
```

---

## 🎯 WHAT EACH COMMAND DOES

| Command | Sets Env Vars | Updates Data | Shows Output | Starts Server |
|---------|--------------|--------------|-------------|---------------|
| `setup` | ✅ | ✅ | ✅ | ❌ |
| `update` | ❌ | ✅ | ✅ | ❌ |
| `view` | ❌ | ❌ | ✅ | ❌ |
| `serve` | ❌ | ❌ | ❌ | ✅ |
| `status` | ❌ | ❌ | ✅ | ❌ |
| `env` | ✅ | ❌ | ✅ | ❌ |

---

## 🔧 ALIAS SETUP (Optional)

Add to `~/.zshrc` for even shorter command:

```bash
alias rd='python3 /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/robot-dashboard.py'
```

Then use:
```bash
rd view
rd serve
rd update
```

---

## 📍 LOCATION

**Robot Script:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/robot-dashboard.py`

**Run from anywhere:**
```bash
python3 /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/robot-dashboard.py [command]
```

**Or from project root:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 robot-dashboard.py [command]
```

---

## ✅ VERIFICATION

Test that everything works:

```bash
# Check status
robot-dashboard status

# Update dashboard
robot-dashboard update

# View dashboard
robot-dashboard view

# Start server (test in browser)
robot-dashboard serve
```

---

## 🆘 TROUBLESHOOTING

### Command not found
```bash
# Use full path
python3 /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/robot-dashboard.py [command]
```

### Environment variables not set
```bash
robot-dashboard env
source ~/.zshrc
```

### Dashboard files missing
```bash
robot-dashboard setup
```

### Server won't start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Or change port in serve-dashboard.py
```

---

## 📝 SUMMARY

**One Command:** `robot-dashboard`  
**All Operations:** Setup, Update, View, Serve, Status, Env  
**Fully Automated:** No manual steps needed  
**Works Everywhere:** Run from any directory

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** ✅ Ready to Use


