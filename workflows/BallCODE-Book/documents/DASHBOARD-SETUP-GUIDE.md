# BallCODE Integration Dashboard - Setup Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** Ready to Use

---

## 🎯 QUICK START

### 1. Update Dashboard Manually
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/update-dashboard.py
```

### 2. View HTML Dashboard on Localhost
```bash
python3 scripts/serve-dashboard.py
# Then open: http://localhost:8000/dashboard.html
```

### 3. View Markdown Dashboard
```bash
cat documents/BALLCODE-INTEGRATION-DASHBOARD.md
```

---

## 📋 SETUP INSTRUCTIONS

### Step 1: Set Environment Variables (Optional)

For full functionality, set these environment variables in `~/.zshrc`:

```bash
# GitHub Configuration (for build monitoring)
export GITHUB_TOKEN='your_github_token'
export GITHUB_REPO_OWNER='your_github_username'
export GITHUB_REPO_NAME='your_repo_name'
export GITHUB_WORKFLOW_FILE='your_workflow_file.yml'

# Netlify Configuration (for deployment monitoring)
export NETLIFY_TOKEN='your_netlify_token'
export NETLIFY_SITE_ID='your_netlify_site_id'

# Build Schedule
export BUILD_INTERVAL_HOURS=6  # How often builds run (6 = every 6 hours)
```

**Then reload:**
```bash
source ~/.zshrc
```

**Note:** Dashboard will work without these, but with limited functionality.

---

### Step 2: Install Dependencies

```bash
pip3 install requests
```

---

### Step 3: Test the Dashboard

```bash
# Update dashboard
python3 scripts/update-dashboard.py

# Start server
python3 scripts/serve-dashboard.py
```

**Then open:** http://localhost:8000/dashboard.html

---

## 🔄 AUTOMATED UPDATES

### Option 1: Cron Job (Recommended)

Update dashboard every 6 hours:

```bash
# Edit crontab
crontab -e

# Add this line (runs every 6 hours):
0 */6 * * * cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && /usr/bin/python3 scripts/update-dashboard.py >> dashboard-update.log 2>&1
```

### Option 2: Manual Updates

Just run when needed:
```bash
python3 scripts/update-dashboard.py
```

---

## 📊 WHAT THE DASHBOARD SHOWS

### Build Status
- GitHub Actions build status
- Netlify deployment status
- Build health (Healthy/Warning/Critical)
- Missed builds analysis

### Integration Status
- Website system status
- Book system status
- Curriculum system status
- Game system status

### Game Improvements
- Recent game improvements
- Current focus
- Planned improvements

### Recent Activity
- Last 24 hours of activity
- Build executions
- Deployments
- Updates

### n8n Workflow Status
- Last execution time
- Workflow status
- Trigger type

### Success Metrics
- Build success rate
- Deployment success rate
- System uptime

---

## 🎨 DASHBOARD FEATURES

### Markdown Dashboard
- **Location:** `documents/BALLCODE-INTEGRATION-DASHBOARD.md`
- **Format:** Clean markdown list format
- **Update:** Automatic or manual
- **Use:** Quick reference, documentation

### HTML Dashboard
- **Location:** `dashboard.html`
- **Format:** Beautiful web dashboard
- **View:** http://localhost:8000/dashboard.html
- **Features:**
  - Real-time status indicators
  - Color-coded status badges
  - Auto-refresh every 5 minutes
  - Manual refresh button
  - Responsive design

---

## 🔧 TROUBLESHOOTING

### Dashboard shows "Error Loading"
**Fix:** Check that `dashboard-data.json` exists. Run `update-dashboard.py` to generate it.

### Build status shows "Unknown"
**Fix:** Set GitHub and Netlify environment variables (see Step 1).

### HTML dashboard doesn't load
**Fix:** Make sure `dashboard.html` and `dashboard-data.json` are in the project root.

### Server won't start
**Fix:** Check if port 8000 is already in use. Change PORT in `serve-dashboard.py` if needed.

---

## 📝 FILES CREATED

1. **`documents/BALLCODE-INTEGRATION-DASHBOARD.md`** - Markdown dashboard
2. **`dashboard.html`** - HTML dashboard
3. **`dashboard-data.json`** - Dashboard data (auto-generated)
4. **`scripts/update-dashboard.py`** - Dashboard updater script
5. **`scripts/serve-dashboard.py`** - Dashboard server script

---

## ✅ QUICK REFERENCE

### Update Dashboard
```bash
python3 scripts/update-dashboard.py
```

### View HTML Dashboard
```bash
python3 scripts/serve-dashboard.py
# Open: http://localhost:8000/dashboard.html
```

### View Markdown Dashboard
```bash
cat documents/BALLCODE-INTEGRATION-DASHBOARD.md
```

### Set Up Auto-Updates
```bash
crontab -e
# Add: 0 */6 * * * cd /path/to/project && python3 scripts/update-dashboard.py
```

---

**Dashboard Version:** 1.0  
**Created:** December 12, 2025  
**Status:** Ready to Use


