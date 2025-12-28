# 🏀 BallCODE Dashboard - Quick Access

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** ✅ Ready to Use

---

## ⚡ SHORT CODE - QUICK ACCESS

### The Short Command: `dashboard`

After reloading your shell, use:

```bash
dashboard view    # View markdown dashboard
dashboard update   # Update dashboard data
dashboard serve    # Start HTML dashboard (localhost:8000)
```

---

## 📍 WHERE EVERYTHING IS

### Dashboard System Location
**Project Root:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`

**Files:**
- **Markdown Dashboard:** `documents/BALLCODE-INTEGRATION-DASHBOARD.md`
- **HTML Dashboard:** `dashboard.html` (project root)
- **Quick Access Script:** `scripts/dashboard`
- **Updater Script:** `scripts/update-dashboard.py`
- **Server Script:** `scripts/serve-dashboard.py`

---

## 🚀 HOW TO ACCESS

### Option 1: Use Short Command (After Reload)
```bash
# Reload shell first
source ~/.zshrc

# Then use:
dashboard view    # Quick markdown view
dashboard serve   # Start web dashboard
dashboard update  # Refresh data
```

### Option 2: Use Full Path (Works Now)
```bash
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard view
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard serve
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/dashboard update
```

### Option 3: Direct Access
```bash
# View markdown
cat /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/documents/BALLCODE-INTEGRATION-DASHBOARD.md

# Start server
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/serve-dashboard.py
# Then open: http://localhost:8000/dashboard.html
```

---

## 🔧 WHAT WAS SET TODAY

### Environment Variables (for n8n)
From today's setup, these were set:
- ✅ `UNITY_REPO_URL` = `https://github.com/rashadwest/BallCode.git`
- ✅ `UNITY_PROJECT_PATH` = `/Users/rashadwest/BTEBallCODE`
- ✅ `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`

**Location:** These are set in n8n (not shell environment variables)

**For Dashboard Build Monitoring (Optional):**
You can optionally set these in `~/.zshrc` for full build monitoring:
- `GITHUB_TOKEN`
- `GITHUB_REPO_OWNER`
- `GITHUB_REPO_NAME`
- `GITHUB_WORKFLOW_FILE`
- `NETLIFY_TOKEN`
- `NETLIFY_SITE_ID`

---

## 📊 WHAT THE DASHBOARD SHOWS

- ✅ **Build Status** - GitHub Actions, Netlify deployments
- ✅ **Integration Status** - Website, Book, Curriculum, Game systems
- ✅ **Game Improvements** - Recent improvements and current focus
- ✅ **Recent Activity** - Last 24 hours of builds and updates
- ✅ **n8n Workflow Status** - Last execution and status
- ✅ **Success Metrics** - Build success rates, uptime

---

## 🎯 QUICK START (Right Now)

### 1. View Dashboard (Markdown)
```bash
cat /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/documents/BALLCODE-INTEGRATION-DASHBOARD.md
```

### 2. View Dashboard (HTML - Beautiful Web View)
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/serve-dashboard.py
# Then open browser: http://localhost:8000/dashboard.html
```

### 3. Update Dashboard Data
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/update-dashboard.py
```

---

## 🔄 AUTO-UPDATE (Optional)

To auto-update every 6 hours:

```bash
crontab -e
# Add this line:
0 */6 * * * cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && /usr/bin/python3 scripts/update-dashboard.py >> dashboard-update.log 2>&1
```

---

## 📝 SUMMARY

**New System:** BallCODE Integration Dashboard  
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`  
**Short Command:** `dashboard` (after reloading shell)  
**Quick Access:** Use full path or direct commands above

**What It Does:** Monitors all BallCODE integrations, builds, improvements, and activity in one place.

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** ✅ Ready to Use



