# 🔍 How to Check if n8n Workflow Has Been Running

**Date:** December 11, 2025  
**Purpose:** Verify if your 23-node Unity automation workflow has been executing

---

## 🎯 QUICK CHECK METHODS

### Method 1: Check in n8n UI (Easiest)

1. **Open n8n UI:**
   - Local: `http://localhost:5678`
   - Remote (Raspberry Pi): `http://192.168.1.226:5678`

2. **Click "Executions" tab** (top navigation bar)

3. **Look for your workflow:**
   - Should see list of all executions
   - Green checkmark = Success
   - Red X = Failed
   - Orange spinner = Running/Stuck

4. **Click on any execution** to see:
   - When it ran
   - Which nodes executed
   - What data passed through
   - Any errors

---

### Method 2: Use Terminal Script (Automated)

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# If n8n is on remote server, set URL first:
export N8N_URL="http://192.168.1.226:5678"

# Run the check script:
./check-n8n-executions.sh
```

**This will show:**
- ✅ Recent executions with timestamps
- ✅ Success/failure status
- ✅ How many times it ran

---

### Method 3: Check GitHub Commits (Indirect Verification)

If the workflow has been running, you should see commits in GitHub:

```bash
# Check recent commits
cd /Users/rashadwest/BTEBallCODE  # or your Unity project path
git log --oneline --since="24 hours ago"
```

**Look for:**
- Commits with messages like "AI automated edits" or "Automated build"
- Commits from the last 24 hours
- Multiple commits if workflow ran multiple times

**Or check online:**
- Go to: `https://github.com/rashadwest/BallCode/commits/main`
- Look for recent commits

---

### Method 4: Check GitHub Actions (If Builds Triggered)

If workflow triggered builds, check GitHub Actions:

1. **Go to:** `https://github.com/rashadwest/BallCode/actions`
2. **Look for:**
   - Recent workflow runs
   - Builds triggered in last 24 hours
   - Build status (success/failure)

---

## 🚨 WHAT TO LOOK FOR

### ✅ Signs Workflow HAS Been Running:

1. **n8n Executions tab shows entries:**
   - Recent executions listed
   - Timestamps match schedule (every 6 hours)
   - Status shows "Success" or "Failed"

2. **GitHub has new commits:**
   - Commits with automated messages
   - Commits from last 24 hours

3. **GitHub Actions has runs:**
   - Builds triggered recently
   - Builds match commit times

### ❌ Signs Workflow HAS NOT Been Running:

1. **n8n Executions tab is empty:**
   - No executions listed
   - Workflow might not be active

2. **No recent GitHub commits:**
   - No automated commits
   - Last commit is old

3. **No GitHub Actions runs:**
   - No builds triggered
   - Last build is old

---

## 🔧 TROUBLESHOOTING

### Issue: No Executions Found

**Possible Causes:**
1. **Workflow not active:**
   - Check if "Active" toggle is ON in n8n
   - Workflow must be active to run

2. **Schedule not configured:**
   - Check "Scheduled Trigger" node
   - Verify "Every 6 Hours" is set
   - Check timezone matches your server

3. **n8n not running:**
   - Check if n8n service is running
   - Check n8n logs for errors

**Solutions:**
1. **Activate workflow:**
   - Open workflow in n8n
   - Click "Active" toggle (should be green/ON)

2. **Verify schedule:**
   - Click on "Scheduled Trigger (Every 6 Hours)" node
   - Check "Hours Between Triggers" = 6
   - Check "Trigger at Minute" = 0

3. **Check n8n status:**
   ```bash
   # If on remote server:
   ssh pi@192.168.1.226
   ps aux | grep n8n
   
   # Or check service:
   sudo systemctl status n8n
   ```

---

## 🚀 HOW TO MANUALLY TRIGGER

### Option 1: Execute from n8n UI

1. **Open workflow** in n8n
2. **Click "Execute Workflow" button** (top right)
3. **Watch it run** in real-time
4. **Check results** in execution history

### Option 2: Use Webhook Trigger

If workflow has webhook trigger:

```bash
# Get webhook URL from n8n (click on "Webhook Trigger" node)
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "Manual test trigger"}'
```

### Option 3: Test Scheduled Trigger Node

1. **Click on "Scheduled Trigger" node**
2. **Click "Execute step" button** (orange button)
3. **This triggers just that node** (for testing)

---

## 📊 EXPECTED BEHAVIOR

### If Workflow Runs Every 6 Hours:

**Today's Schedule (if started at midnight):**
- 12:00 AM - First run
- 6:00 AM - Second run
- 12:00 PM - Third run
- 6:00 PM - Fourth run

**Check if you see:**
- 4 executions per day (if running 24/7)
- Executions spaced ~6 hours apart
- All showing "Success" status

---

## ✅ VERIFICATION CHECKLIST

After checking, verify:

- [ ] n8n Executions tab shows recent runs
- [ ] Workflow is marked as "Active"
- [ ] Schedule trigger is configured (every 6 hours)
- [ ] Recent GitHub commits exist (if workflow does git operations)
- [ ] GitHub Actions has recent runs (if workflow triggers builds)
- [ ] No error messages in execution details

---

## 📝 NEXT STEPS

**If workflow HAS been running:**
- ✅ Great! It's working
- Check execution details to verify all nodes completed
- Verify actual operations (git commits, builds, etc.)

**If workflow HAS NOT been running:**
- Activate the workflow (toggle ON)
- Verify schedule configuration
- Manually trigger to test
- Check n8n logs for errors

---

**Status:** Ready to check  
**Script:** `./check-n8n-executions.sh`  
**n8n URL:** Check `.n8n-env` file or use `http://192.168.1.226:5678`


