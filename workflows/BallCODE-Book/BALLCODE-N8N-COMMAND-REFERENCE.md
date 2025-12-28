# 🚀 BallCODE n8n Workflow Command Reference
## Complete Guide to All BallCODE n8n Workflows & Python Hybrid Integration

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Single source of truth for all BallCODE n8n workflows, commands, and usage  
**Status:** ✅ Active Reference

---

## 📋 QUICK COMMAND REFERENCE

### Test All Workflows
```bash
./scripts/test-all-webhooks.sh
```

### Check Workflow Status
```bash
./scripts/check-n8n-status.sh
```

### Trigger Unity Build
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Build request", "branch": "main"}'
```

### Trigger Full Integration
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Your development prompt", "mode": "quick"}'
```

### Trigger Screenshot Fix
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/error.png", "context": "Error description"}'
```

---

## 🎯 THE 3 CRITICAL WORKFLOWS

### 1. Unity Build Orchestrator 🔴 **CRITICAL - #1 Priority**

**Purpose:** Automates Unity builds, triggers GitHub Actions, checks Netlify deployment

**File:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`

**Webhook:** `/webhook/unity-build`

**Status:** ⚠️ **NEEDS FIXING** - Has been working before but currently not working

**Current Issues:**
- Workflow exists but not functioning properly
- Same error repeating over and over
- Had one working before with wrong n8n URL, but can't get it back working

**What It Does:**
1. Receives build request via webhook
2. Triggers GitHub Actions workflow
3. Monitors build status
4. Checks Netlify deployment
5. Returns build status

**Dependencies:**
- Environment Variables: `GITHUB_REPO_OWNER`, `GITHUB_REPO_NAME`, `GITHUB_WORKFLOW_FILE`, `NETLIFY_SITE_ID`, `NETLIFY_SITE_NAME`, `N8N_INSTANCE_ROLE`
- Credentials: `github-actions-token`, `netlify-api-token`

**Test Command:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**Troubleshooting:**
- Check if workflow is active in n8n UI
- Verify all environment variables are set
- Verify credentials are configured
- Check n8n logs for errors
- Use diagnostic script: `./scripts/diagnose-orchestrator.sh`

---

### 2. Full Integration Workflow 🟠 **HIGH Priority - Core Automation**

**Purpose:** AI-driven development automation that updates all 4 systems (Game, Curriculum, Book, Website) from a single prompt

**File:** `n8n-ballcode-full-integration-workflow.json`

**Webhook:** `/webhook/ballcode-dev`

**Status:** ✅ **WORKING** - Ready to use

**What It Does:**
1. Receives development prompt
2. Analyzes prompt using AIMCODE methodology (Demis Hassabis - Alpha Evolve)
3. Updates all 4 systems in parallel:
   - Game (Unity scripts, JSON levels)
   - Curriculum (Unified schema)
   - Book (Story content, exercises)
   - Website (HTML/CSS/JS)
4. Saves memory context
5. Returns integration report

**When to Use:**
- ✅ **Use when:** You want to update multiple systems from one prompt
- ✅ **Use when:** You have a clear development goal that affects multiple systems
- ✅ **Use when:** You want AI to figure out what needs updating across systems
- ❌ **Don't use when:** You only need to update one system (use direct Python/scripts instead)
- ❌ **Don't use when:** You need immediate results without AI processing time

**Can It Be Used Without Other Workflows?**
- ✅ **YES** - Full Integration is independent
- ✅ It can work standalone without Orchestrator or Screenshot workflows
- ✅ It uses Python scripts directly, doesn't depend on other workflows
- ⚠️ However, if you want to trigger a build after updates, you'll need Orchestrator

**Usage Examples:**

**Quick Mode (Fast):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new exercise for Book 1 that teaches sequences",
    "mode": "quick"
  }'
```

**Full Mode (Comprehensive):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Update Book 2 to include pattern recognition concepts and create matching game exercise",
    "mode": "full",
    "context": {
      "bookId": 2,
      "focus": "pattern recognition",
      "gradeLevel": "6-8"
    }
  }'
```

**Dependencies:**
- Environment Variables: `WORKFLOW_PATH`
- Credentials: `openai-credentials` (OpenAI API key)
- Python Scripts: `scripts/n8n-update-schema.py`

**Response Format:**
```json
{
  "status": "success",
  "systemsUpdated": {
    "game": true,
    "curriculum": true,
    "book": true,
    "website": true
  },
  "integrationStatus": "All systems integrated successfully",
  "memoryContextSaved": true,
  "actionPlanLayers": [...],
  "nextSteps": [...]
}
```

---

### 3. Screenshot to Fix Workflow 🟡 **MEDIUM Priority - Visual Debugging**

**Purpose:** Visual debugging and auto-repair - analyzes error screenshots and automatically fixes issues

**File:** `n8n-screenshot-to-fix-workflow.json`

**Webhook:** `/webhook/screenshot-fix`

**Status:** ✅ **WORKING** - But needs consistent testing

**What It Does:**
1. Receives screenshot URL and context
2. Analyzes screenshot using GPT-4 Vision
3. Identifies the error/problem
4. Generates fix code/instructions
5. Applies fix automatically (if possible)
6. Commits and pushes fix (if git access available)
7. Triggers build (if Orchestrator available)
8. Returns fix report

**When to Use:**
- ✅ **Use when:** You have an error screenshot and want AI to analyze and fix it
- ✅ **Use when:** You're debugging visual issues in the game or website
- ✅ **Use when:** You want automated error fixing
- ❌ **Don't use when:** Error is already clear from logs
- ❌ **Don't use when:** Fix requires manual intervention

**Testing:**
- ⚠️ **Current Issue:** Hard to test consistently
- Use test script: `./scripts/test-screenshot-fix.sh`
- Provide screenshot URL and context
- Check response for fix suggestions

**Usage:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "Unity build error - missing dependency"
  }'
```

**Dependencies:**
- Environment Variables: `WORKFLOW_PATH`, `GITHUB_REPO_OWNER`, `GITHUB_REPO_NAME`, `GITHUB_WORKFLOW_FILE`, `NETLIFY_SITE_NAME`
- Credentials: `openai-credentials`, `github-actions-token`
- Python Scripts: `screenshot_fix_processor.py`

**Response Format:**
```json
{
  "status": "success",
  "errorIdentified": "Missing dependency in Unity project",
  "fixApplied": true,
  "fixCode": "...",
  "filesModified": ["path/to/file.cs"],
  "buildTriggered": true
}
```

---

## 🔧 PYTHON HYBRID INTEGRATION

### How Python Works with n8n Workflows

**Key Insight:** n8n workflows use Python scripts via `Execute Command` nodes to:
- Update schema files
- Process complex logic
- Interact with file system
- Avoid n8n VM2 sandbox limitations

### Python Scripts Used:

**1. `scripts/n8n-update-schema.py`**
- Used by: Full Integration, Book Content Update, Curriculum Sync
- Purpose: Updates unified curriculum schema
- Usage: Called automatically by workflows

**2. `screenshot_fix_processor.py`**
- Used by: Screenshot to Fix workflow
- Purpose: Processes screenshot analysis and applies fixes
- Usage: Called automatically by workflow

### ELI10 Integration

**ELI10** = Explain Like I'm 10 (simplified explanations)

**How It Works:**
- Python scripts can generate ELI10 explanations
- Workflows can include ELI10 in responses
- Makes technical updates understandable

**Example:**
```python
# In Python script
eli10_explanation = "We added a new exercise that teaches kids how to put things in order, like lining up for recess!"
```

---

## 📊 WORKFLOW STATUS MONITORING

### Quick Status Check

**Command:**
```bash
./scripts/check-n8n-status.sh
```

**What It Shows:**
- Which workflows are imported
- Which workflows are active
- Which workflows are working
- Last execution times
- Error counts

### Daily Status Report

**Command:**
```bash
./scripts/daily-n8n-report.sh
```

**What It Shows:**
- Yesterday's workflow executions
- Success/failure rates
- What needs attention today
- Recommended actions

---

## 🎯 DAILY WORKFLOW INTEGRATION

### How It Works

**Every morning when you say "Top of the morning":**

1. **AI presents yesterday's summary** (from `DAILY-WORKFLOW-[DATE].md`)
2. **AI presents 10 daily workflow questions**
3. **AI includes BallCODE n8n workflow status** (NEW!)
4. **You answer questions**
5. **AI provides:**
   - What was done yesterday with n8n workflows
   - What needs to be done today with n8n workflows
   - ONE thing focus for today

### BallCODE n8n Section in Daily Workflow

**After "Top of the morning" questions, AI will show:**

```
📊 BALLCODE N8N WORKFLOW STATUS

Yesterday's Executions:
- Unity Build Orchestrator: 2 builds (1 success, 1 failed)
- Full Integration: 3 prompts processed (all success)
- Screenshot Fix: 0 executions

Today's Actions Needed:
- [ ] Fix Unity Build Orchestrator (priority: HIGH)
- [ ] Test Full Integration with new prompt
- [ ] Verify Screenshot Fix workflow

ONE Thing Focus Today:
[Your ONE thing focus]
```

---

## 🚨 TROUBLESHOOTING GUIDE

### Orchestrator Not Working

**Symptoms:**
- Returns 200 but doesn't trigger build
- Same error repeating
- Workflow shows as active but nothing happens

**Diagnostic Steps:**
1. Run: `./scripts/diagnose-orchestrator.sh`
2. Check n8n UI: Is workflow active?
3. Check environment variables: Are they set?
4. Check credentials: Are they valid?
5. Check n8n logs: What errors appear?

**Common Fixes:**
- Re-import workflow from cleaned file
- Verify GitHub token has correct permissions
- Check n8n URL is correct (Pi vs Mac)
- Verify workflow path is correct

### Full Integration Not Responding

**Symptoms:**
- Webhook returns timeout
- No response
- Error in n8n logs

**Diagnostic Steps:**
1. Check OpenAI credentials
2. Verify `WORKFLOW_PATH` is set
3. Check Python script exists: `scripts/n8n-update-schema.py`
4. Test with simple prompt first

**Common Fixes:**
- Verify OpenAI API key is valid
- Check file permissions for `WORKFLOW_PATH`
- Test Python script directly

### Screenshot Fix Not Working

**Symptoms:**
- Can't test consistently
- No response from webhook
- Fix not applied

**Diagnostic Steps:**
1. Verify screenshot URL is accessible
2. Check OpenAI Vision API access
3. Verify Python script exists
4. Test with sample screenshot

**Common Fixes:**
- Use publicly accessible screenshot URL
- Verify OpenAI Vision model access
- Check file system permissions

---

## 📝 WORKFLOW PRIORITY RANKING

**Based on Your Requirements:**

1. 🔴 **Unity Build Orchestrator** - CRITICAL
   - Must work for builds
   - Top priority to fix
   - Needed for deployment

2. 🟠 **Full Integration** - HIGH
   - Core automation
   - Can work independently
   - Most useful for daily work

3. 🟡 **Screenshot Fix** - MEDIUM
   - Nice to have
   - Useful for debugging
   - Lower priority

**You said:** "If these 3 can work, I don't really want to have to do any of the other ones."

**Agreed:** Focus on these 3. The other workflows (Book Content Update, Curriculum Sync, Game Exercise Integration) are lower priority.

---

## 🎯 SUCCESS CRITERIA

**System is successful when:**

1. ✅ **Orchestrator works reliably** - Can trigger builds without errors
2. ✅ **Full Integration works independently** - Can update all systems from prompts
3. ✅ **Screenshot Fix is testable** - Can consistently test and get results
4. ✅ **Daily workflow includes n8n status** - You see status every morning
5. ✅ **No need for other workflows** - These 3 are sufficient
6. ✅ **Process is not brutal** - Easy to use, easy to monitor

---

## 🔄 ALTERNATIVES TO N8N

**You mentioned:** "What can we do to make it easier or unnecessary to do this n8n process?"

**Options to Explore:**

1. **Pure Python Scripts**
   - Replace n8n workflows with Python
   - More flexible, easier to debug
   - Can use same Python scripts directly

2. **GitHub Actions**
   - Move automation to GitHub Actions
   - Closer to code, easier to version control
   - No n8n dependency

3. **Cursor AI Direct Integration**
   - Use Cursor AI to execute workflows directly
   - No n8n needed
   - More direct control

4. **Hybrid Approach**
   - Keep critical workflows in n8n
   - Move others to Python/GitHub Actions
   - Reduce n8n complexity

**Periodic Review:**
- Every month, review: "Can we simplify this?"
- Look for new tools that make n8n unnecessary
- Consider moving to pure Python if n8n becomes too complex

---

## 📚 RELATED DOCUMENTATION

- **Full Integration Guide:** `N8N-FULL-INTEGRATION-WORKFLOW-GUIDE.md`
- **End-to-End Analysis:** `N8N-WORKFLOWS-END-TO-END-ANALYSIS.md`
- **Workflow Priority:** `WORKFLOW-PRIORITY-RANKING.md`
- **Python Hybrid:** `PYTHON-HYBRID-QUICK-START.md`

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** ✅ Active Reference - Update as workflows evolve


