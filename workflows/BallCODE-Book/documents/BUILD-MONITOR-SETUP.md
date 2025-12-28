# Independent Build Monitor Setup
## Monitor Builds Outside of n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Purpose:** Monitor GitHub Actions and Netlify builds independently

---

## 🎯 WHAT THIS DOES

**Independent monitoring system that:**
- ✅ Checks GitHub Actions for recent builds
- ✅ Checks Netlify for recent deployments
- ✅ Detects missed builds based on schedule
- ✅ Runs outside of n8n (doesn't depend on it)
- ✅ Can run via cron or manually
- ✅ Generates reports

---

## 📋 SETUP INSTRUCTIONS

### Step 1: Get API Tokens

#### GitHub Token:
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Scopes needed: `repo`, `workflow`
4. Copy token

#### Netlify Token:
1. Go to Netlify → User settings → Applications
2. Generate new access token
3. Copy token

#### Netlify Site ID:
1. Go to Netlify → Your site → Site settings
2. Copy Site ID (under "General")

---

### Step 2: Set Environment Variables

Add to `~/.zshrc` (or `~/.bashrc`):

```bash
# GitHub Configuration
export GITHUB_TOKEN='your_github_token_here'
export GITHUB_REPO_OWNER='your_github_username'
export GITHUB_REPO_NAME='your_repo_name'
export GITHUB_WORKFLOW_FILE='your_workflow_file.yml'  # e.g., 'build.yml'

# Netlify Configuration
export NETLIFY_TOKEN='your_netlify_token_here'
export NETLIFY_SITE_ID='your_netlify_site_id'

# Build Schedule
export BUILD_INTERVAL_HOURS=1  # How often builds should run (1 = hourly)
```

**Then reload:**
```bash
source ~/.zshrc
```

---

### Step 3: Test the Monitor

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/monitor-builds.py
```

**Expected output:**
- GitHub Actions status
- Netlify deployments status
- Missed builds analysis
- Report saved to `build-monitor-report.txt`

---

### Step 4: Set Up Automated Monitoring

#### Option A: Cron Job (Recommended)

```bash
# Edit crontab
crontab -e

# Add this line (runs every hour):
0 * * * * cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && /usr/bin/python3 scripts/monitor-builds.py >> build-monitor.log 2>&1
```

#### Option B: Run Manually

```bash
# Run anytime to check builds
./scripts/monitor-builds.py
```

#### Option C: Setup Script

```bash
# Run setup helper
./scripts/setup-build-monitor.sh
```

---

## 📊 USING THE MONITOR

### Run Manually:

```bash
python3 scripts/monitor-builds.py
```

**Output:**
- Console report showing build status
- Report saved to `build-monitor-report.txt`
- Exit code 0 = no missed builds
- Exit code 1 = missed builds detected

### Check Report:

```bash
cat build-monitor-report.txt
```

---

## 🔔 ALERT SETUP (Optional)

### Email Alerts on Missed Builds:

Add to cron job:
```bash
0 * * * * cd /path/to/project && python3 scripts/monitor-builds.py && if [ $? -ne 0 ]; then echo "Missed builds detected!" | mail -s "Build Alert" your@email.com; fi
```

### Slack Webhook (Future):

Can add Slack webhook notification when builds are missed.

---

## 📋 WHAT IT MONITORS

### GitHub Actions:
- ✅ Recent workflow runs
- ✅ Build status (success/failure)
- ✅ Build timestamps
- ✅ Detects missed builds

### Netlify:
- ✅ Recent deployments
- ✅ Deployment status
- ✅ Deployment timestamps
- ✅ Detects missed deployments

### Analysis:
- ✅ Compares actual builds vs expected schedule
- ✅ Identifies missed build times
- ✅ Reports on build health

---

## 🐛 TROUBLESHOOTING

### Error: "GitHub credentials not configured"
**Fix:** Set GITHUB_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME, GITHUB_WORKFLOW_FILE

### Error: "Netlify credentials not configured"
**Fix:** Set NETLIFY_TOKEN and NETLIFY_SITE_ID

### Error: "Module 'requests' not found"
**Fix:** Install requests: `pip3 install requests`

### No builds detected:
**Check:**
- Are builds actually running?
- Are credentials correct?
- Is workflow file name correct?

---

## ✅ QUICK START

1. **Set environment variables** (see Step 2)
2. **Test:** `python3 scripts/monitor-builds.py`
3. **Set up cron:** `crontab -e` (add hourly job)
4. **Check reports:** `cat build-monitor-report.txt`

---

## 📊 EXAMPLE OUTPUT

```
======================================================================
BUILD MONITORING REPORT
======================================================================
Generated: 2025-12-12 14:30:00

📊 GITHUB ACTIONS:
----------------------------------------------------------------------
✅ Status: Connected
   Recent runs: 10
   Latest run: 2025-12-12T14:00:00Z
   Status: completed | Conclusion: success
   URL: https://github.com/owner/repo/actions/runs/123456

📊 NETLIFY DEPLOYMENTS:
----------------------------------------------------------------------
✅ Status: Connected
   Recent deploys: 10
   Latest deploy: 2025-12-12T14:05:00Z
   State: published
   Deploy URL: https://app.netlify.com/sites/site/deploys/123456

🔍 MISSED BUILDS ANALYSIS:
----------------------------------------------------------------------
Expected builds (last 24h): 24
Missed builds: 0

✅ No missed builds detected!
======================================================================
```

---

**Version:** Independent Build Monitor  
**Created:** December 12, 2025  
**Status:** Ready to Use



