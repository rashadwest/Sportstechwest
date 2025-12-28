# BallCODE Dashboard - Quick Access Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** Ready to Use

---

## ⚡ SHORT CODE - QUICK ACCESS

### Add to Your Shell Profile

Add this to `~/.zshrc` (or `~/.bashrc`):

```bash
# BallCODE Dashboard - Quick Access
alias dashboard='/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard'
```

**Then reload:**
```bash
source ~/.zshrc
```

---

## 🚀 USAGE (After Adding Alias)

### View Markdown Dashboard
```bash
dashboard view
# or
dashboard v
```

### Update Dashboard Data
```bash
dashboard update
# or
dashboard u
```

### Start HTML Dashboard Server
```bash
dashboard serve
# or
dashboard s
# Then open: http://localhost:8000/dashboard.html
```

### Show Help
```bash
dashboard
```

---

## 📍 WHERE EVERYTHING IS

### Dashboard Files
- **Markdown Dashboard:** `documents/BALLCODE-INTEGRATION-DASHBOARD.md`
- **HTML Dashboard:** `dashboard.html` (project root)
- **Dashboard Data:** `dashboard-data.json` (auto-generated)

### Scripts
- **Quick Access:** `scripts/dashboard`
- **Updater:** `scripts/update-dashboard.py`
- **Server:** `scripts/serve-dashboard.py`

### Documentation
- **Setup Guide:** `documents/DASHBOARD-SETUP-GUIDE.md`
- **Quick Access:** `documents/DASHBOARD-QUICK-ACCESS.md` (this file)

---

## 🔧 WHAT WAS SET TODAY

### Environment Variables Set (for n8n)
From today's chat history, these variables were set:
- `UNITY_REPO_URL` = `https://github.com/rashadwest/BallCode.git`
- `UNITY_PROJECT_PATH` = `/Users/rashadwest/BTEBallCODE`
- `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`

**Note:** These are for n8n workflows. For dashboard build monitoring, you can optionally set:
- `GITHUB_TOKEN`
- `GITHUB_REPO_OWNER`
- `GITHUB_REPO_NAME`
- `GITHUB_WORKFLOW_FILE`
- `NETLIFY_TOKEN`
- `NETLIFY_SITE_ID`

---

## 🎯 QUICK START (3 Steps)

### Step 1: Add Alias
```bash
echo 'alias dashboard="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard"' >> ~/.zshrc
source ~/.zshrc
```

### Step 2: Update Dashboard
```bash
dashboard update
```

### Step 3: View Dashboard
```bash
# Markdown view
dashboard view

# OR HTML view (in browser)
dashboard serve
# Then open: http://localhost:8000/dashboard.html
```

---

## 📊 WHAT THE DASHBOARD SHOWS

- ✅ Build Status (GitHub Actions, Netlify)
- ✅ Integration Status (Website, Book, Curriculum, Game)
- ✅ Game Improvements
- ✅ Current Focus
- ✅ Recent Activity
- ✅ n8n Workflow Status
- ✅ Success Metrics

---

## 🔄 AUTO-UPDATE (Optional)

To auto-update every 6 hours:

```bash
crontab -e
# Add:
0 */6 * * * cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && /usr/bin/python3 scripts/update-dashboard.py >> dashboard-update.log 2>&1
```

---

**Quick Access Command:** `dashboard`  
**Version:** 1.0  
**Created:** December 12, 2025



