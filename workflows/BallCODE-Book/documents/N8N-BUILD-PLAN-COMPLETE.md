# n8n Build Plan - Complete System
## Clear Plan for Automated Builds Using n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** 🎯 Ready for Implementation  
**Workflow:** `n8n-unity-automation-workflow-FINAL-WORKING.json`

---

## 🎯 BUILD SYSTEM OVERVIEW

### Current Workflow Structure
- **Triggers:** 3 types (Scheduled hourly, Webhook manual, GitHub webhook)
- **Nodes:** 23 total nodes
- **Flow:** Trigger → AI Analysis → Git Operations → Build → Deploy → Notify
- **Schedule:** Runs every hour (`0 * * * *`)

### Build Process Flow
```
1. Trigger (Scheduled/Webhook/GitHub)
   ↓
2. Normalize Input (detect trigger type)
   ↓
3. AI Analyze Request (determine what needs to be done)
   ↓
4. Parse AI Response (extract action plan)
   ↓
5. Get Git Variables (environment variables)
   ↓
6. Clone/Update Repository (git pull or clone)
   ↓
7. Needs Unity Edits? (conditional check)
   ↓
8. AI Unity Editor Edits (if needed)
   ↓
9. Commit & Push Changes (git add, commit, push)
   ↓
10. Needs Build? (conditional check)
   ↓
11. Trigger GitHub Actions Build (if needed)
   ↓
12. Wait for Build (5 minutes)
   ↓
13. Needs Deploy? (conditional check)
   ↓
14. Deploy to Netlify (if needed)
   ↓
15. Finalize & Prepare Report
   ↓
16. Send Notification (if configured)
   ↓
17. Webhook Response (if webhook trigger)
```

---

## 📋 BUILD TYPES & USE CASES

### Build Type 1: Scheduled Hourly Builds
**Trigger:** Automatic (every hour at :00)  
**Purpose:** Regular automated builds to keep game updated  
**Use Case:** Continuous integration, regular updates

**What Happens:**
1. Workflow triggers automatically
2. AI analyzes: "Automated build from scheduled trigger"
3. Checks if any changes need to be made
4. If changes needed: Edit → Commit → Build → Deploy
5. If no changes: Skip gracefully

**Expected Result:**
- Build runs every hour
- Only commits if changes exist
- Builds and deploys if needed

---

### Build Type 2: Manual Webhook Builds
**Trigger:** POST request to webhook  
**Purpose:** On-demand builds for specific requests  
**Use Case:** "Create new level for Book 1, exercise 2"

**How to Trigger:**
```bash
curl -X POST http://your-n8n-url/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "Create new level for Book 1, exercise 2: foundation block coding"}'
```

**What Happens:**
1. Webhook receives request
2. AI analyzes the specific request
3. Determines what Unity edits are needed
4. Makes edits → Commits → Builds → Deploys
5. Returns response with results

**Expected Result:**
- Specific request is fulfilled
- Code changes are made
- Build and deploy complete
- Response shows success/failure

---

### Build Type 3: GitHub Webhook Builds
**Trigger:** GitHub push/commit events  
**Purpose:** Build when code is pushed to GitHub  
**Use Case:** Manual code changes trigger automatic builds

**How to Set Up:**
1. In GitHub repo: Settings → Webhooks
2. Add webhook URL: `http://your-n8n-url/webhook/github-webhook`
3. Select events: "push", "workflow_dispatch"

**What Happens:**
1. GitHub sends webhook on push
2. Workflow detects GitHub trigger
3. Extracts commit message
4. Analyzes what was changed
5. Builds and deploys if needed

**Expected Result:**
- Automatic builds on code pushes
- No manual intervention needed
- Builds match code changes

---

## 🔧 BUILD CONFIGURATION

### Environment Variables Required

**Git Configuration:**
- `UNITY_REPO_URL` - GitHub repository URL (e.g., `https://github.com/rashadwest/BTEBallCODE`)
- `UNITY_PROJECT_PATH` - Local path where repo is cloned (e.g., `/Users/rashadwest/BTEBallCODE`)

**GitHub Actions:**
- `GITHUB_REPO_OWNER` - Repository owner (e.g., `rashadwest`)
- `GITHUB_REPO_NAME` - Repository name (e.g., `BTEBallCODE`)
- `GITHUB_WORKFLOW_FILE` - Workflow filename (e.g., `unity-webgl-build.yml`)

**Netlify:**
- `NETLIFY_SITE_ID` - Netlify site ID
- `NETLIFY_SITE_NAME` - Netlify site name (e.g., `ballcode-game`)
- `BUILD_OUTPUT_PATH` - Path to build output directory

**Optional:**
- `WEBHOOK_NOTIFICATION_URL` - URL to send completion notifications
- `WORKFLOW_PATH` - Path to workflow scripts (e.g., `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`)

**OpenAI:**
- OpenAI API credentials configured in n8n

---

## 🎯 BUILD PRIORITIES (From Questions Document)

### Priority 1: Level Creation Builds (HIGH VALUE)
**Build Type:** Manual Webhook  
**Frequency:** As needed (when creating new levels)

**Request Format:**
```json
{
  "request": "Create new level: Book 1, Coding mode, Exercise 2, Foundation block coding with crossover dribble"
}
```

**What It Does:**
1. AI analyzes request
2. Generates level JSON from template
3. Creates level file in Unity project
4. Commits and pushes to GitHub
5. Triggers build and deploy

**Expected Output:**
- New level JSON file created
- Level appears in game
- Game updated on Netlify

---

### Priority 2: Math Level Creation (EASIEST)
**Build Type:** Manual Webhook  
**Frequency:** Batch creation (multiple levels at once)

**Request Format:**
```json
{
  "request": "Create 5 math levels for Book 1: exercises 1-5, each with different formulas"
}
```

**Why Math First:**
- No videos needed (easier to generate)
- Can create multiple levels quickly
- Good for testing build system

**Expected Output:**
- 5 new math level JSON files
- All levels appear in game
- Game updated with new math exercises

---

### Priority 3: Coding Level Creation (NEEDS VIDEOS)
**Build Type:** Manual Webhook  
**Frequency:** As videos are available

**Request Format:**
```json
{
  "request": "Create coding level: Book 1, Exercise 3, Crossover dribble with right hand, use video from player X"
}
```

**What It Does:**
1. AI analyzes request
2. Generates level JSON
3. Links to video asset
4. Creates block coding configuration
5. Commits, builds, deploys

**Expected Output:**
- New coding level with video
- Block coding blocks configured
- Level playable in game

---

### Priority 4: UI/UX Improvements (ITERATIVE)
**Build Type:** Manual Webhook or Scheduled  
**Frequency:** Ongoing improvements

**Request Format:**
```json
{
  "request": "Improve UI/UX: Make game feel more engaging, add better feedback messages, improve visual polish"
}
```

**What It Does:**
1. AI analyzes UI/UX needs
2. Makes Unity UI changes
3. Updates feedback system
4. Commits, builds, deploys

**Expected Output:**
- UI improvements visible
- Better user experience
- More engaging gameplay

---

### Priority 5: Chess Level Creation (HARDEST - LAST)
**Build Type:** Manual Webhook  
**Frequency:** After other modes are complete

**Request Format:**
```json
{
  "request": "Create chess level: Book 1, Strategy exercise, opponent difficulty medium"
}
```

**Why Last:**
- Most complex game mode
- Requires strategy system
- Needs opponent AI

**Expected Output:**
- New chess level
- Strategy gameplay working
- Opponent AI configured

---

## 📊 BUILD SCHEDULE RECOMMENDATIONS

### Daily Build Schedule
- **Hourly:** Scheduled builds (check for updates)
- **Morning (9 AM):** Manual build for new levels/content
- **Afternoon (2 PM):** Manual build for improvements
- **Evening (6 PM):** Manual build for fixes

### Weekly Build Schedule
- **Monday:** Math levels batch creation
- **Tuesday:** Coding levels (as videos available)
- **Wednesday:** UI/UX improvements
- **Thursday:** Coding levels continued
- **Friday:** Testing and fixes
- **Weekend:** Chess levels (when ready)

---

## 🚀 BUILD EXECUTION STEPS

### Step 1: Verify Workflow is Active
1. Open n8n UI
2. Check workflow is "Active" (toggle on)
3. Verify schedule trigger is enabled
4. Check all credentials are configured

### Step 2: Test Manual Build
1. Use webhook trigger
2. Send test request
3. Monitor execution
4. Verify all nodes complete
5. Check GitHub for commit
6. Check GitHub Actions for build
7. Check Netlify for deployment

### Step 3: Monitor Scheduled Builds
1. Wait for next hourly trigger
2. Check n8n executions
3. Verify build completed
4. Check results

### Step 4: Verify Code Pushed
1. Check GitHub commits
2. Verify commit messages
3. Check commit timestamps
4. Verify code changes

---

## 🔍 BUILD VERIFICATION CHECKLIST

### Pre-Build Verification
- [ ] Workflow is active in n8n
- [ ] All environment variables set
- [ ] All credentials configured
- [ ] GitHub repository accessible
- [ ] Netlify site configured
- [ ] OpenAI API key valid

### During Build Verification
- [ ] Trigger fires (scheduled/webhook)
- [ ] AI analysis completes
- [ ] Git operations succeed
- [ ] Unity edits complete (if needed)
- [ ] Commit and push succeed
- [ ] GitHub Actions build triggers
- [ ] Build completes successfully
- [ ] Netlify deployment succeeds

### Post-Build Verification
- [ ] New commit appears in GitHub
- [ ] GitHub Actions build shows success
- [ ] Netlify deployment shows "Published"
- [ ] Game loads on Netlify site
- [ ] Changes are visible in game
- [ ] No errors in logs

---

## 🐛 TROUBLESHOOTING COMMON ISSUES

### Issue: Workflow Doesn't Trigger
**Symptoms:** No execution at scheduled time  
**Solutions:**
1. Check workflow is "Active"
2. Verify cron expression: `0 * * * *`
3. Check n8n server timezone
4. Verify schedule trigger is enabled

### Issue: Git Operations Fail
**Symptoms:** "Clone/Update Repository" node shows error  
**Solutions:**
1. Check `UNITY_REPO_URL` is set correctly
2. Check `UNITY_PROJECT_PATH` exists and is writable
3. Verify git credentials are configured
4. Check repository permissions

### Issue: No Code Pushed
**Symptoms:** Workflow completes but no commit in GitHub  
**Solutions:**
1. Check "Commit & Push Changes" node output
2. Verify there were actual changes to commit
3. Check git credentials
4. Verify branch name is "main" (not "master")

### Issue: Build Doesn't Trigger
**Symptoms:** Commit succeeds but no GitHub Actions build  
**Solutions:**
1. Check "Trigger GitHub Actions Build" node
2. Verify GitHub token is valid
3. Check workflow file exists in repo
4. Verify repository name is correct

### Issue: Deployment Fails
**Symptoms:** Build succeeds but Netlify deployment fails  
**Solutions:**
1. Check Netlify API token
2. Verify site ID is correct
3. Check build output path
4. Verify Netlify site exists

---

## 📈 BUILD METRICS & MONITORING

### Key Metrics to Track
- **Build Success Rate:** % of builds that complete successfully
- **Build Frequency:** How often builds run
- **Build Duration:** Time from trigger to deployment
- **Code Push Success:** % of commits that push successfully
- **Deployment Success:** % of deployments that succeed

### Monitoring Dashboard
Create a simple monitoring system:
1. Track each build execution
2. Log success/failure
3. Record timestamps
4. Track error types
5. Generate daily reports

---

## ✅ SUCCESS CRITERIA

### Build System is Working When:
- ✅ Scheduled builds run every hour
- ✅ Manual webhook builds work on demand
- ✅ GitHub webhook builds trigger on push
- ✅ Code is pushed to GitHub successfully
- ✅ GitHub Actions builds complete
- ✅ Netlify deployments succeed
- ✅ Game updates are visible
- ✅ No errors in execution logs

### Build System is Effective When:
- ✅ New levels can be created automatically
- ✅ UI/UX improvements deploy quickly
- ✅ Fixes can be deployed within hours
- ✅ Build process is reliable (>95% success)
- ✅ No manual intervention needed
- ✅ All changes are tracked in Git

---

## 🎯 NEXT STEPS

### Immediate (Today):
1. Verify workflow is active
2. Test manual webhook build
3. Verify code is being pushed
4. Check GitHub Actions builds
5. Verify Netlify deployments

### Short-term (This Week):
6. Create first automated level
7. Test scheduled builds
8. Monitor build success rate
9. Fix any issues found
10. Document build process

### Medium-term (Next 2 Weeks):
11. Create batch level generation
12. Implement build monitoring
13. Optimize build process
14. Add build notifications
15. Create build reports

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** Ready for Implementation


