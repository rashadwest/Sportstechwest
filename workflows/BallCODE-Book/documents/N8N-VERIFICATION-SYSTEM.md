# n8n Verification System
## Verify Workflow is Working & Code is Being Pushed

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** 🎯 Ready for Use  
**Purpose:** Comprehensive verification system to ensure n8n workflow is working effectively

---

## 🎯 VERIFICATION OVERVIEW

### What We're Verifying
1. **Workflow Execution:** Is the n8n workflow running?
2. **Code Pushing:** Is code being pushed to GitHub?
3. **Build Triggering:** Are GitHub Actions builds being triggered?
4. **Deployment:** Are Netlify deployments succeeding?
5. **System Health:** Is the entire system working end-to-end?

---

## 🔍 VERIFICATION METHODS

### Method 1: n8n Execution History (PRIMARY)

**Location:** n8n UI → Executions tab

**Steps:**
1. Open n8n UI: `http://192.168.1.226:5678` (or your n8n URL)
2. Click **"Executions"** tab (top navigation)
3. Find your workflow: "Unity AI Automation - HOURLY BUILD"
4. Check recent executions:
   - ✅ Green checkmark = Success
   - ❌ Red X = Failed
   - ⏳ Orange spinner = Running/Stuck

**What to Look For:**
- Recent executions (within last 24 hours)
- Success status (green checkmarks)
- All nodes completed
- No error messages
- Execution timestamps match schedule

**Expected Results:**
- At least 1 execution per hour (if scheduled)
- Most executions show success
- All 23 nodes complete
- No stuck executions

---

### Method 2: GitHub Commit History (CODE PUSH VERIFICATION)

**Location:** GitHub repository commits page

**Steps:**
1. Go to: `https://github.com/rashadwest/BTEBallCODE/commits/main` (or your repo)
2. Check recent commits
3. Look for automated commits:
   - Commit messages like: "AI automated edits: [request]"
   - Commit messages like: "Automated build from scheduled trigger"
   - Commits from last 24 hours

**What to Look For:**
- Recent commits (within last 24 hours)
- Automated commit messages
- Commit timestamps match workflow execution times
- Code changes in commits

**Expected Results:**
- Commits appear after workflow runs
- Commit messages match workflow requests
- Commits include actual code changes
- Commits are pushed to "main" branch

**Command Line Check:**
```bash
cd /Users/rashadwest/BTEBallCODE  # or your Unity project path
git log --oneline --since="24 hours ago" -10
```

**Expected Output:**
```
abc1234 AI automated edits: Create new level for Book 1
def5678 Automated build from scheduled trigger
ghi9012 AI automated edits: Improve UI/UX
```

---

### Method 3: GitHub Actions Build History (BUILD VERIFICATION)

**Location:** GitHub repository Actions tab

**Steps:**
1. Go to: `https://github.com/rashadwest/BTEBallCODE/actions` (or your repo)
2. Check recent workflow runs
3. Look for "Unity WebGL Build" workflow
4. Check build status:
   - ✅ Green = Success
   - ❌ Red = Failed
   - ⏳ Yellow = Running

**What to Look For:**
- Recent workflow runs (within last 24 hours)
- Builds triggered after commits
- Build status (success/failure)
- Build completion times

**Expected Results:**
- Builds trigger after commits
- Most builds succeed
- Builds complete within 10-15 minutes
- No stuck builds

**Command Line Check:**
```bash
gh run list --repo rashadwest/BTEBallCODE --limit 10
```

**Expected Output:**
```
STATUS  TITLE                    WORKFLOW              BRANCH  EVENT   CREATED
✓       Unity WebGL Build        unity-webgl-build.yml main    push    2 hours ago
✓       Unity WebGL Build        unity-webgl-build.yml main    push    3 hours ago
```

---

### Method 4: Netlify Deployment History (DEPLOYMENT VERIFICATION)

**Location:** Netlify dashboard

**Steps:**
1. Go to: `https://app.netlify.com`
2. Select your site (e.g., "ballcode-game")
3. Click **"Deploys"** tab
4. Check recent deployments:
   - ✅ Published = Success
   - ⏳ Building = In progress
   - ❌ Failed = Error

**What to Look For:**
- Recent deployments (within last 24 hours)
- Deployment status (Published)
- Deployment times match build times
- Site URL is accessible

**Expected Results:**
- Deployments appear after builds
- Most deployments succeed
- Site is accessible
- Game loads correctly

**Site URL Check:**
```bash
curl -I https://ballcode-game.netlify.app  # or your site URL
```

**Expected Output:**
```
HTTP/2 200
```

---

### Method 5: End-to-End Test (COMPLETE VERIFICATION)

**Purpose:** Test entire flow from trigger to deployment

**Steps:**
1. **Trigger Manual Build:**
   ```bash
   curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
     -H "Content-Type: application/json" \
     -d '{"request": "Test build verification - verify system is working"}'
   ```

2. **Monitor n8n Execution:**
   - Go to n8n UI → Executions
   - Find the test execution
   - Watch it complete

3. **Verify GitHub Commit:**
   - Check GitHub commits page
   - Look for test commit
   - Verify commit message

4. **Verify GitHub Actions Build:**
   - Check GitHub Actions
   - Verify build triggered
   - Wait for build to complete

5. **Verify Netlify Deployment:**
   - Check Netlify deploys
   - Verify deployment succeeded
   - Test site URL

**Expected Timeline:**
- 0:00 - Webhook triggered
- 0:05 - n8n execution completes
- 0:10 - Commit appears in GitHub
- 0:15 - GitHub Actions build starts
- 0:25 - Build completes
- 0:30 - Netlify deployment starts
- 0:35 - Deployment completes
- 0:40 - Site updated

**Success Criteria:**
- ✅ All steps complete successfully
- ✅ No errors at any stage
- ✅ Code is pushed
- ✅ Build succeeds
- ✅ Deployment succeeds
- ✅ Site is updated

---

## 📊 VERIFICATION CHECKLIST

### Daily Verification (Quick Check - 5 minutes)

**Morning Check:**
- [ ] Check n8n executions (last 24 hours)
- [ ] Verify at least 1 successful execution
- [ ] Check GitHub for recent commits
- [ ] Verify GitHub Actions builds are running
- [ ] Check Netlify for recent deployments

**Evening Check:**
- [ ] Review all executions from today
- [ ] Check for any failures
- [ ] Verify code was pushed
- [ ] Verify builds completed
- [ ] Verify deployments succeeded

---

### Weekly Verification (Comprehensive - 30 minutes)

**Monday Morning:**
- [ ] Review all executions from last week
- [ ] Calculate success rate
- [ ] Identify any recurring issues
- [ ] Check GitHub commit history
- [ ] Review GitHub Actions build history
- [ ] Review Netlify deployment history
- [ ] Test end-to-end flow
- [ ] Document any issues found

**Success Metrics:**
- Build success rate: >95%
- Code push success: 100%
- Deployment success: >95%
- Average build time: <15 minutes

---

## 🚨 TROUBLESHOOTING VERIFICATION ISSUES

### Issue: No Executions in n8n

**Symptoms:** No executions appear in n8n UI  
**Possible Causes:**
1. Workflow is not active
2. Schedule trigger is disabled
3. n8n server is not running
4. Workflow was deleted

**Solutions:**
1. Check workflow is "Active" (toggle on)
2. Verify schedule trigger is enabled
3. Check n8n server status
4. Verify workflow exists

**Verification:**
```bash
# Check n8n is running
curl http://192.168.1.226:5678/healthz
```

---

### Issue: Executions Show But No Commits

**Symptoms:** n8n shows success but no commits in GitHub  
**Possible Causes:**
1. Git operations failing silently
2. No changes to commit
3. Git credentials not configured
4. Repository path incorrect

**Solutions:**
1. Check "Clone/Update Repository" node output
2. Check "Commit & Push Changes" node output
3. Verify git credentials
4. Check repository path

**Verification:**
- Check n8n execution details
- Look at "Commit & Push Changes" node output
- Verify `UNITY_PROJECT_PATH` is correct
- Check git credentials in n8n

---

### Issue: Commits But No Builds

**Symptoms:** Commits appear but GitHub Actions doesn't build  
**Possible Causes:**
1. GitHub Actions workflow not configured
2. GitHub token invalid
3. Workflow file missing
4. Repository name incorrect

**Solutions:**
1. Check "Trigger GitHub Actions Build" node
2. Verify GitHub token is valid
3. Check workflow file exists in repo
4. Verify repository name

**Verification:**
- Check GitHub Actions tab
- Verify workflow file: `.github/workflows/unity-webgl-build.yml`
- Check GitHub token in n8n credentials
- Test manual workflow dispatch

---

### Issue: Builds But No Deployments

**Symptoms:** GitHub Actions builds succeed but Netlify doesn't deploy  
**Possible Causes:**
1. Netlify API token invalid
2. Site ID incorrect
3. Build output path wrong
4. Netlify site not configured

**Solutions:**
1. Check "Deploy to Netlify" node
2. Verify Netlify API token
3. Check site ID
4. Verify build output path

**Verification:**
- Check Netlify dashboard
- Verify site exists
- Check API token in n8n
- Test Netlify API manually

---

## 📈 VERIFICATION REPORT TEMPLATE

### Daily Verification Report

**Date:** [Date]  
**Time:** [Time]  
**Verified By:** [Name]

**n8n Executions:**
- Total executions: [Number]
- Successful: [Number]
- Failed: [Number]
- Success rate: [Percentage]

**GitHub Commits:**
- Commits in last 24h: [Number]
- Automated commits: [Number]
- Manual commits: [Number]

**GitHub Actions Builds:**
- Builds triggered: [Number]
- Successful builds: [Number]
- Failed builds: [Number]
- Success rate: [Percentage]

**Netlify Deployments:**
- Deployments: [Number]
- Successful: [Number]
- Failed: [Number]
- Success rate: [Percentage]

**Issues Found:**
- [List any issues]

**Actions Taken:**
- [List actions taken]

**Status:** ✅ Working / ⚠️ Issues / ❌ Not Working

---

## 🔧 AUTOMATED VERIFICATION SCRIPT

### Create Verification Script

**File:** `scripts/verify-n8n-system.sh`

```bash
#!/bin/bash

echo "🔍 n8n System Verification"
echo "=========================="
echo ""

# Check n8n is accessible
echo "1. Checking n8n accessibility..."
if curl -s http://192.168.1.226:5678/healthz > /dev/null; then
    echo "   ✅ n8n is accessible"
else
    echo "   ❌ n8n is not accessible"
fi

# Check recent executions (requires n8n API)
echo ""
echo "2. Checking recent executions..."
# Add n8n API call here

# Check GitHub commits
echo ""
echo "3. Checking GitHub commits..."
cd /Users/rashadwest/BTEBallCODE
RECENT_COMMITS=$(git log --oneline --since="24 hours ago" | wc -l)
echo "   Commits in last 24h: $RECENT_COMMITS"

# Check GitHub Actions
echo ""
echo "4. Checking GitHub Actions..."
gh run list --repo rashadwest/BTEBallCODE --limit 5

# Check Netlify
echo ""
echo "5. Checking Netlify deployments..."
# Add Netlify API call here

echo ""
echo "✅ Verification complete"
```

**Usage:**
```bash
chmod +x scripts/verify-n8n-system.sh
./scripts/verify-n8n-system.sh
```

---

## ✅ VERIFICATION SUCCESS CRITERIA

### System is Working When:
- ✅ n8n executions appear regularly
- ✅ Executions show success status
- ✅ Commits appear in GitHub after executions
- ✅ GitHub Actions builds trigger after commits
- ✅ Builds complete successfully
- ✅ Netlify deployments succeed after builds
- ✅ Site is accessible and updated
- ✅ No errors in any stage

### System is Effective When:
- ✅ >95% of executions succeed
- ✅ Code is pushed within 5 minutes of execution
- ✅ Builds complete within 15 minutes
- ✅ Deployments complete within 5 minutes
- ✅ End-to-end time < 30 minutes
- ✅ No manual intervention needed
- ✅ All changes are tracked

---

## 🎯 NEXT STEPS

### Immediate (Today):
1. Run verification checklist
2. Test end-to-end flow
3. Document current status
4. Fix any issues found
5. Verify code is being pushed

### Short-term (This Week):
6. Set up automated verification
7. Create daily verification routine
8. Monitor system health
9. Document verification process
10. Create verification reports

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** Ready for Use


