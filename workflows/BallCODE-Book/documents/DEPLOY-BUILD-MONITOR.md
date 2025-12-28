# Deploy Build Monitor - Quick Guide
## Step-by-Step Deployment

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** Ready to Deploy

---

## 🚀 QUICK DEPLOY (3 Steps)

### Step 1: Set Environment Variables

Add to `~/.zshrc`:

```bash
# GitHub Configuration
export GITHUB_TOKEN='your_github_token'
export GITHUB_REPO_OWNER='your_github_username'
export GITHUB_REPO_NAME='your_repo_name'
export GITHUB_WORKFLOW_FILE='your_workflow_file.yml'

# Netlify Configuration
export NETLIFY_TOKEN='your_netlify_token'
export NETLIFY_SITE_ID='your_netlify_site_id'

# Build Schedule
export BUILD_INTERVAL_HOURS=1
```

**Then reload:**
```bash
source ~/.zshrc
```

---

### Step 2: Run Deploy Script

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/deploy-build-monitor.sh
```

**This will:**
- ✅ Check environment variables
- ✅ Test the monitor script
- ✅ Set up cron job (runs every hour)
- ✅ Create log file

---

### Step 3: Verify It's Working

```bash
# Check cron job
crontab -l

# Run manually to test
python3 scripts/monitor-builds.py

# View logs (after first run)
tail -f build-monitor.log
```

---

## 📋 GETTING API TOKENS

### GitHub Token:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Scopes: `repo`, `workflow`
4. Copy token

### Netlify Token:
1. Netlify → User settings → Applications
2. Generate new access token
3. Copy token

### Netlify Site ID:
1. Netlify → Your site → Site settings
2. Copy Site ID (under "General")

---

## ✅ DEPLOYMENT CHECKLIST

- [ ] Environment variables set in ~/.zshrc
- [ ] Source ~/.zshrc to load variables
- [ ] Run deploy script: `./scripts/deploy-build-monitor.sh`
- [ ] Test monitor: `python3 scripts/monitor-builds.py`
- [ ] Verify cron job: `crontab -l`
- [ ] Check logs: `tail -f build-monitor.log`

---

## 🎯 WHAT HAPPENS AFTER DEPLOYMENT

### Automated Monitoring:
- ✅ Runs every hour at :00 minutes
- ✅ Checks GitHub Actions builds
- ✅ Checks Netlify deployments
- ✅ Detects missed builds
- ✅ Logs to `build-monitor.log`
- ✅ Generates report: `build-monitor-report.txt`

### Manual Commands:
```bash
# Run monitor manually
python3 scripts/monitor-builds.py

# View latest report
cat build-monitor-report.txt

# Watch logs in real-time
tail -f build-monitor.log

# Check cron job
crontab -l
```

---

## 🐛 TROUBLESHOOTING

### Error: "Missing environment variables"
**Fix:** Set all required variables in ~/.zshrc and reload

### Error: "Module 'requests' not found"
**Fix:** `pip3 install requests`

### Cron job not running
**Fix:** Check cron service is running: `sudo launchctl list | grep cron`

### No logs appearing
**Fix:** Wait for first hourly run, or run manually to test

---

## 📊 SUCCESS INDICATORS

✅ **Deployment successful when:**
- Deploy script completes without errors
- Monitor script runs and generates report
- Cron job appears in `crontab -l`
- Log file is created
- Report file is generated

---

**Version:** Quick Deploy Guide  
**Created:** December 12, 2025  
**Status:** Ready to Deploy



