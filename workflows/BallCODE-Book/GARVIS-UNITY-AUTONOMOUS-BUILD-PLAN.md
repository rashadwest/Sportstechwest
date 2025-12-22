# 🎮 Garvis Unity Autonomous Build System - Complete Plan

**Date:** December 17, 2025  
**Status:** 📋 Planning Complete - Ready for Implementation  
**Goal:** Fully autonomous Unity game building, debugging, and deployment via Garvis

---

## ✅ YOUR REQUIREMENTS (CONFIRMED)

### What You Want:
1. **Answer 23 questions** (--full questionnaire) about Unity game changes
2. **Garvis executes autonomously** - builds, debugs, deploys without you
3. **End-of-day updates** - what was done, what needs finishing
4. **Next-day continuation** - seamlessly picks up where it left off
5. **Zero manual intervention** - true "Set It And Forget It"

### Game Context:
- **Similar to:** Lightbot (programming puzzle game)
- **Unique:** Basketball component integrated
- **Platform:** Unity WebGL (deployed to Netlify)
- **Repository:** `rashadwest/BTEBallCODE` (separate from BallCODE-Book)

---

## 🔧 WHAT GARVIS NEEDS TO INTERACT WITH UNITY

### 1. GitHub API Access (Required)

**Purpose:**
- Read Unity project files (C# scripts, scenes, assets)
- Create branches for changes
- Commit and push code changes
- Trigger GitHub Actions workflows
- Monitor build status

**What You Need to Provide:**
- [ ] **GitHub Personal Access Token (PAT)** with these scopes:
  - `repo` (full repository access)
  - `workflow` (trigger/manage GitHub Actions)
  - `read:org` (if repository is in organization)

**How to Create:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name: "Garvis Unity Automation"
4. Expiration: 90 days (or custom)
5. Select scopes: `repo`, `workflow`
6. Generate and copy token
7. Store securely (we'll add to environment variables)

**Where to Store:**
- n8n environment variables: `GITHUB_PAT`
- Or: `.env` file in project root

---

### 2. Netlify API Access (Required)

**Purpose:**
- Deploy WebGL builds automatically
- Check deployment status
- View build logs
- Trigger manual deploys
- Get deployment URLs

**What You Need to Provide:**
- [ ] **Netlify Access Token**

**How to Create:**
1. Go to: https://app.netlify.com/user/applications
2. Click "New access token"
3. Description: "Garvis Unity Deployment"
4. Generate and copy token

**Where to Store:**
- n8n environment variables: `NETLIFY_AUTH_TOKEN`
- Also need: `NETLIFY_SITE_ID` (your Unity game site ID)

---

### 3. Unity Project Access (Required)

**Current Situation:**
- Unity project is in separate repo: `rashadwest/BTEBallCODE`
- Not cloned in current workspace

**Options:**

#### Option A: Clone Unity Repo Locally (Recommended)
```bash
cd /Users/rashadwest/Sportstechwest/workflows
git clone https://github.com/rashadwest/BTEBallCODE.git
```

**Benefits:**
- Garvis can read Unity files directly
- Can analyze scenes, scripts, assets
- Can make code changes locally
- Can test before pushing

#### Option B: Use GitHub API Only
- Garvis reads files via GitHub API
- Makes changes via API
- Less efficient but works

**Recommendation:** Option A (clone locally)

---

### 4. Unity Build System Access

**Current Setup:**
- ✅ GitHub Actions workflow exists: `.github/workflows/unity-webgl-build.yml`
- ✅ Can trigger builds via GitHub API
- ✅ Can monitor build status

**What Garvis Needs:**
- [ ] GitHub Actions workflow URL/name
- [ ] Unity license (if required for CI/CD)
- [ ] Build output location

---

## 🚀 HOW GARVIS WILL WORK

### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    YOU (Answer 23 Questions)            │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────┐
│         Python Script: ask_unified_questions.py        │
│         Creates: UNITY-BUILD-PLAN-YYYY-MM-DD.md         │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────┐
│              n8n Workflow (CORE ORCHESTRATOR)          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 1. Webhook Trigger (detects plan file created)   │  │
│  │ 2. Read Plan File                                │  │
│  │ 3. AI Analysis (OpenAI) - Parse into tasks      │  │
│  │ 4. Execute Garvis Scripts (Python)               │  │
│  │ 5. Monitor GitHub Actions Build                  │  │
│  │ 6. Deploy to Netlify                             │  │
│  │ 7. Generate Progress Report                      │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ GitHub API   │ │ Netlify API  │ │ Local Scripts│
│ (Code/Build) │ │ (Deploy)     │ │ (Execution)  │
└──────────────┘ └──────────────┘ └──────────────┘
```

**n8n is the central orchestrator** that:
- Monitors for your 23-question answers
- Coordinates all the pieces (GitHub, Netlify, scripts)
- Handles errors and retries
- Generates reports
- Runs continuously in background

---

### Step 1: You Answer 23 Questions (--full)

**Command:**
```bash
python scripts/ask_unified_questions.py --full
```

**What Happens:**
1. You answer all 23 questions about Unity game changes
2. Answers saved to: `UNITY-BUILD-PLAN-YYYY-MM-DD.md`
3. Garvis analyzes answers and creates execution plan

---

### Step 2: Garvis Creates Execution Plan

**Garvis Process:**
1. **ANALYZE:** Reads your 23 answers
2. **IDEATE:** Determines what needs to change:
   - Which C# scripts to modify
   - Which Unity scenes to update
   - Which assets to add/change
   - What build configuration changes needed
3. **MODEL:** Creates detailed execution plan:
   - Step-by-step tasks
   - Files to modify
   - Tests to run
   - Build sequence
4. **OPTIMIZE:** Prioritizes tasks, identifies dependencies
5. **DEPLOY:** Executes plan autonomously

---

### Step 3: n8n Orchestrates Execution (Autonomous)

**n8n Workflow Execution Flow:**

```
1. n8n Webhook Triggered
   (Detects UNITY-BUILD-PLAN-YYYY-MM-DD.md created)
   ↓
2. n8n Reads Plan File
   (Loads your 23 answers)
   ↓
3. n8n → OpenAI Analysis
   (Parses answers into actionable tasks)
   ↓
4. n8n → Execute Command Node
   (Runs: python scripts/garvis-unity-executor.py)
   ↓
5. Garvis Script → GitHub API
   (Clone repo, create branch, make changes)
   ↓
6. Garvis Script → Commit & Push
   (Git operations via API)
   ↓
7. n8n → GitHub API Node
   (Trigger GitHub Actions build)
   ↓
8. n8n → Wait & Monitor
   (Poll GitHub Actions status)
   ↓
9. If Build Fails:
   n8n → AI Analysis → Fix → Retry
   ↓
10. If Build Succeeds:
    n8n → Netlify API Node
    (Deploy WebGL build)
    ↓
11. n8n → Generate Report
    (Creates progress summary)
    ↓
12. n8n → Send Notification (optional)
    (Email/webhook with results)
```

**n8n coordinates everything - all without you!**

---

### Step 4: End-of-Day Report

**Garvis Generates:**
- ✅ What was completed today
- ⚠️ What's in progress
- 📋 What needs to be done tomorrow
- 🐛 Any errors encountered
- 📊 Build/deployment status

**Format:**
- Markdown file: `GARVIS-UNITY-PROGRESS-YYYY-MM-DD.md`
- Summary in: `TODAY-WORKFLOW-DATA.json`

---

### Step 5: Next-Day Continuation

**Garvis Checks:**
1. Reads yesterday's progress file
2. Identifies incomplete tasks
3. Continues from where it left off
4. Updates you on resumption

**Seamless continuation!**

---

## 📋 IMPLEMENTATION CHECKLIST

### Phase 1: Setup (Before Tomorrow)

- [ ] **GitHub PAT Created**
  - Token generated
  - Stored in n8n: `GITHUB_PAT`
  - Tested with API call

- [ ] **Netlify Token Created**
  - Token generated
  - Stored in n8n: `NETLIFY_AUTH_TOKEN`
  - Site ID stored: `NETLIFY_SITE_ID`

- [ ] **Unity Repo Cloned**
  - Cloned to: `/Users/rashadwest/Sportstechwest/workflows/BTEBallCODE`
  - Verified access
  - Tested git operations

- [ ] **Garvis Scripts Created**
  - `scripts/garvis-unity-executor.py` - Main execution engine
  - `scripts/garvis-unity-analyzer.py` - Analyzes 23-question answers
  - `scripts/garvis-unity-builder.py` - Handles GitHub Actions triggers
  - `scripts/garvis-unity-deployer.py` - Handles Netlify deployment
  - `scripts/garvis-unity-reporter.py` - Generates end-of-day reports

### Phase 2: Integration (Tomorrow Morning)

- [ ] **n8n Workflow Created** ⚡ **CORE COMPONENT**
  - **Workflow Name:** "Garvis Unity Autonomous Build"
  - **Trigger:** Webhook (triggered when 23-question answer file is created)
  - **Or:** Schedule trigger (runs periodically to check for new plans)
  - **Nodes:**
    1. Webhook/Schedule Trigger
    2. Read 23-Question Answer File
    3. AI Analysis (OpenAI) - Parse answers into execution plan
    4. Execute Command - Run Garvis Unity executor scripts
    5. Monitor GitHub Actions Build
    6. Deploy to Netlify
    7. Generate Progress Report
    8. Send Notification (optional)
  - **Integration:** Works with existing Unity Build Orchestrator workflow
  - **Reports:** End-of-day summary automatically

- [ ] **Testing**
  - Test with simple change (e.g., update a comment)
  - Verify GitHub API access
  - Verify Netlify deployment
  - Verify reporting

### Phase 3: Full Automation (Ready to Use)

- [ ] **Documentation Complete**
- [ ] **All scripts tested**
- [ ] **n8n workflow active**
- [ ] **Ready for your first --full questionnaire**

---

## 🎯 SUCCESS CRITERIA

**You Can:**
1. ✅ Run `python scripts/ask_unified_questions.py --full`
2. ✅ Answer 23 questions about Unity game changes
3. ✅ Walk away and let Garvis work
4. ✅ Get end-of-day report automatically
5. ✅ See progress continue next day seamlessly

**Garvis Can:**
1. ✅ Read Unity project files (via GitHub API or local clone)
2. ✅ Make code changes autonomously
3. ✅ Trigger builds via GitHub Actions
4. ✅ Deploy to Netlify automatically
5. ✅ Debug build failures and retry
6. ✅ Generate progress reports
7. ✅ Continue work next day

---

## 📝 NEXT STEPS (TOMORROW)

### When You Return:

1. **Review this document** - Make sure everything is clear
2. **Create API tokens** - GitHub PAT and Netlify token
3. **Clone Unity repo** - If not already done
4. **Run first --full questionnaire** - Test the system
5. **Let Garvis work** - Set it and forget it!

---

## 🔗 RELATED DOCUMENTS

- `UNITY-LANDING-PAGE-UI-IMPROVEMENT-GUIDE.md` - Current UI/UX guide
- `UNIFIED-PROMPTING-SYSTEM.md` - Full 23-question framework
- `.github/workflows/unity-webgl-build.yml` - Existing build workflow
- `GARVIS-SYSTEM-GUIDE.md` - Overall Garvis system documentation
- `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json` - Existing n8n workflow (can be extended)
- `n8n-unity-automation-workflow.json` - Existing Unity automation workflow

## 📊 N8N INTEGRATION DETAILS

### Why n8n is Essential:

1. **Orchestration:** Coordinates multiple systems (GitHub, Netlify, scripts)
2. **Error Handling:** Retries, fallbacks, error notifications
3. **Monitoring:** Tracks progress, logs everything
4. **Scheduling:** Can run on schedule or trigger on events
5. **Integration:** Easy API connections (GitHub, Netlify, OpenAI)
6. **Visual:** See workflow status in n8n UI
7. **Reliable:** Runs 24/7 on your Raspberry Pi

### Existing n8n Workflows to Leverage:

- ✅ **Unity Build Orchestrator** - Already handles GitHub Actions triggers
- ✅ **Full Integration Workflow** - Already has AI analysis patterns
- ✅ **Screenshot-to-Fix** - Already has error handling patterns

**We'll extend these or create new workflow specifically for Garvis Unity automation.**

---

## ✅ CONFIRMATION

**Everything is clear!** 

**What I understand:**
- ✅ You want to answer 23 questions (--full)
- ✅ Garvis executes autonomously on Unity game
- ✅ Uses GitHub API for code changes and builds
- ✅ Uses Netlify API for deployments
- ✅ End-of-day reports automatically
- ✅ Next-day continuation seamlessly
- ✅ Zero manual intervention needed

**What I'll create tomorrow:**
- Garvis Unity executor scripts
- n8n workflow for automation
- Integration with GitHub/Netlify APIs
- Progress reporting system

**What you need to provide:**
- GitHub Personal Access Token
- Netlify Access Token
- Unity repo clone (or confirm GitHub API access)

**Ready to build this tomorrow!** 🚀

---

**Have a good night! See you tomorrow to make this happen!** 🌙✨

