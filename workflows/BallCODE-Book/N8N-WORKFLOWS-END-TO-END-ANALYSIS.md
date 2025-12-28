# 🔍 n8n Workflows - End-to-End Analysis & Test Plan

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Complete analysis of all n8n workflows, their dependencies, and what needs to be done to make them work  
**Status:** 🔄 In Progress

---

## 📋 EXECUTIVE SUMMARY

**Total Workflows:** 6 production workflows  
**Currently Imported:** 1 (Unity Build Orchestrator)  
**Ready to Import:** 4  
**Needs Recreation:** 1 (Game Exercise Integration - empty file)

**Priority Ranking:**
1. 🔴 **CRITICAL:** Unity Build Orchestrator (already working)
2. 🟠 **HIGH:** Full Integration Workflow (core automation)
3. 🟡 **MEDIUM:** Book Content Update, Curriculum Sync, Game Exercise Integration
4. 🟢 **LOW:** Screenshot to Fix Workflow (nice to have)

---

## 🎯 WORKFLOW #1: Unity Build Orchestrator

**File:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`  
**Status:** ✅ **IMPORTED & WORKING**  
**Priority:** 🔴 **CRITICAL - #1 Most Important**

### Purpose
Automates Unity builds, triggers GitHub Actions, and checks Netlify deployment status.

### Current State
- ✅ Imported in n8n
- ✅ 13 nodes
- ⚠️ Currently `"active": false` in JSON (needs activation in UI)
- ✅ Has webhook trigger: `/webhook/unity-build`
- ✅ Has scheduled trigger (hourly, disabled on dev)

### Dependencies Required

#### Environment Variables:
- ✅ `GITHUB_REPO_OWNER` - GitHub username (e.g., "rashadwest")
- ✅ `GITHUB_REPO_NAME` - Repository name (e.g., "BTEBallCODE")
- ✅ `GITHUB_WORKFLOW_FILE` - Workflow filename (e.g., "unity-webgl-build.yml")
- ✅ `NETLIFY_SITE_ID` - Netlify site ID
- ✅ `NETLIFY_SITE_NAME` - Netlify site name (e.g., "ballcode-game")
- ✅ `N8N_INSTANCE_ROLE` - Set to "prod" on Pi (or "dev" on Mac)

#### Credentials:
- ✅ `github-actions-token` - HTTP Header Auth with GitHub Personal Access Token
- ✅ `netlify-api-token` - HTTP Header Auth with Netlify API Token

### What Needs to Be Done
1. ✅ Verify workflow is imported (DONE)
2. ⚠️ **Activate workflow in n8n UI** (toggle Active switch)
3. ⚠️ **Verify all environment variables are set**
4. ⚠️ **Verify credentials are configured**
5. ✅ Test webhook: `POST /webhook/unity-build`

### Test Command
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

### Status: ✅ **READY - Just needs activation**

---

## 🎯 WORKFLOW #2: Full Integration Workflow

**File:** `n8n-ballcode-full-integration-workflow.json`  
**Status:** ⏳ **NOT IMPORTED - Ready for deployment**  
**Priority:** 🟠 **HIGH - Core AI-driven automation**

### Purpose
AI-driven development automation that updates all 4 systems (Game, Curriculum, Book, Website) based on development prompts.

### Current State
- ❌ Not imported in n8n
- ✅ 15 nodes
- ✅ Has webhook trigger: `/webhook/ballcode-dev`
- ✅ Uses OpenAI GPT-4 for AI analysis
- ✅ Uses Python script for schema updates

### Dependencies Required

#### Environment Variables:
- ✅ `WORKFLOW_PATH` - Path to workflow directory (e.g., `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`)

#### Credentials:
- ✅ `openai-credentials` - OpenAI API key

#### Python Scripts:
- ✅ `scripts/n8n-update-schema.py` - EXISTS ✅

### What Needs to Be Done
1. ⚠️ **Import workflow to n8n**
2. ⚠️ **Set environment variable:** `WORKFLOW_PATH`
3. ⚠️ **Configure credential:** `openai-credentials` with OpenAI API key
4. ⚠️ **Activate workflow**
5. ✅ Test webhook: `POST /webhook/ballcode-dev`

### Test Command
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new exercise for sequences",
    "mode": "quick"
  }'
```

### Potential Issues
- ⚠️ Code node tries to use `fs.readFileSync` which doesn't work in n8n VM2 sandbox
- ✅ **FIXED:** Uses Python script instead via executeCommand node

### Status: ✅ **READY TO IMPORT**

---

## 🎯 WORKFLOW #3: Screenshot to Fix Workflow

**File:** `n8n-screenshot-to-fix-workflow.json`  
**Status:** ⏳ **NOT IMPORTED - Ready for deployment**  
**Priority:** 🟢 **LOW - Nice to have, not critical**

### Purpose
Visual debugging and auto-repair: analyzes error screenshots and automatically fixes issues.

### Current State
- ❌ Not imported in n8n
- ✅ 15 nodes
- ✅ Has webhook trigger: `/webhook/screenshot-fix`
- ✅ Uses GPT-4 Vision for screenshot analysis
- ✅ Uses Python script to apply fixes

### Dependencies Required

#### Environment Variables:
- ✅ `WORKFLOW_PATH` - Path to workflow directory
- ⚠️ `GITHUB_REPO_OWNER` - For git commit/push
- ⚠️ `GITHUB_REPO_NAME` - For git commit/push
- ⚠️ `GITHUB_WORKFLOW_FILE` - For triggering builds
- ⚠️ `NETLIFY_SITE_NAME` - For deployment verification
- ⚠️ `WEBHOOK_NOTIFICATION_URL` - Optional, for notifications

#### Credentials:
- ✅ `openai-credentials` - OpenAI API key (for GPT-4 Vision)
- ⚠️ `github-actions-token` - For triggering builds after fix

#### Python Scripts:
- ✅ `screenshot_fix_processor.py` - EXISTS ✅

### What Needs to Be Done
1. ⚠️ **Import workflow to n8n**
2. ⚠️ **Set environment variables**
3. ⚠️ **Configure credentials**
4. ⚠️ **Activate workflow**
5. ✅ Test webhook: `POST /webhook/screenshot-fix`

### Test Command
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error.png",
    "context": "n8n workflow error"
  }'
```

### Potential Issues
- ⚠️ Requires file system access for applying fixes
- ⚠️ Requires git access for commit/push
- ⚠️ Complex workflow with many dependencies

### Status: ⚠️ **READY BUT COMPLEX - Lower priority**

---

## 🎯 WORKFLOW #4: Book Content Update Workflow

**File:** `n8n-book-content-update-workflow.json`  
**Status:** ⏳ **NOT IMPORTED - Ready for deployment**  
**Priority:** 🟡 **MEDIUM - Content management**

### Purpose
Automates book content updates across all systems (curriculum schema, website, game links).

### Current State
- ❌ Not imported in n8n
- ✅ 9 nodes
- ✅ Has webhook trigger: `/webhook/book-content-update`
- ✅ Uses Python script for schema updates (HYBRID approach)
- ✅ Uses OpenAI for website updates

### Dependencies Required

#### Environment Variables:
- ✅ `WORKFLOW_PATH` - Path to workflow directory

#### Credentials:
- ✅ `openai-credentials` - OpenAI API key

#### Python Scripts:
- ✅ `scripts/n8n-update-schema.py` - EXISTS ✅

### What Needs to Be Done
1. ⚠️ **Import workflow to n8n**
2. ⚠️ **Set environment variable:** `WORKFLOW_PATH`
3. ⚠️ **Configure credential:** `openai-credentials`
4. ⚠️ **Activate workflow**
5. ✅ Test webhook: `POST /webhook/book-content-update`

### Test Command
```bash
curl -X POST http://192.168.1.226:5678/webhook/book-content-update \
  -H "Content-Type: application/json" \
  -d '{
    "bookId": 1,
    "content": {
      "title": "The Foundation Block",
      "slug": "the-foundation-block",
      "concepts": {"python": "Sequences"},
      "basketball": {"skill": "Pound Dribble"},
      "curriculum": {"gradeLevels": ["3-5", "6-8"]}
    },
    "updateType": "modify"
  }'
```

### Status: ✅ **READY TO IMPORT**

---

## 🎯 WORKFLOW #5: Curriculum Schema Sync Workflow

**File:** `n8n-curriculum-sync-workflow.json`  
**Status:** ⏳ **NOT IMPORTED - Ready for deployment**  
**Priority:** 🟡 **MEDIUM - Content synchronization**

### Purpose
Keeps all systems synchronized when curriculum changes (updates game configs, book metadata, website curriculum display).

### Current State
- ❌ Not imported in n8n
- ✅ 10 nodes
- ✅ Has webhook trigger: `/webhook/curriculum-sync`
- ✅ Uses Python script for curriculum updates (HYBRID approach)
- ✅ Uses OpenAI for parallel updates (game, book, website)

### Dependencies Required

#### Environment Variables:
- ✅ `WORKFLOW_PATH` - Path to workflow directory

#### Credentials:
- ✅ `openai-credentials` - OpenAI API key

#### Python Scripts:
- ✅ `scripts/n8n-update-schema.py` - EXISTS ✅

### What Needs to Be Done
1. ⚠️ **Import workflow to n8n**
2. ⚠️ **Set environment variable:** `WORKFLOW_PATH`
3. ⚠️ **Configure credential:** `openai-credentials`
4. ⚠️ **Activate workflow**
5. ✅ Test webhook: `POST /webhook/curriculum-sync`

### Test Command
```bash
curl -X POST http://192.168.1.226:5678/webhook/curriculum-sync \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "newObjective",
    "learningObjective": {
      "objective": "Understand sequences in Python",
      "gradeLevels": ["3-5"],
      "standards": ["CSTA-1A-AP-08"]
    }
  }'
```

### Status: ✅ **READY TO IMPORT**

---

## 🎯 WORKFLOW #6: Game Exercise Integration Workflow

**File:** `n8n-game-exercise-integration-workflow.json`  
**Status:** ✅ **RECREATED - Ready for deployment**  
**Priority:** 🟡 **MEDIUM - Exercise integration**

### Purpose
Automatically integrates new game exercises with books and curriculum (links exercises to books, updates curriculum, updates website).

### Current State
- ✅ **FILE RECREATED** - Based on documentation and other Phase 2 workflows
- ✅ 12 nodes (Python Hybrid approach)
- ✅ Has webhook trigger: `/webhook/game-exercise-integration`
- ✅ Uses Python script for schema integration
- ✅ Uses OpenAI for curriculum and website updates

### Expected Structure (Based on Documentation)
```
Webhook Trigger → Normalize Input → Extract Exercise Metadata → 
Validate → Execute Python (Integrate Exercise) → Parse JSON → 
Update Curriculum (AI) → Update Website (AI) → 
Test Integration → Merge → Response
```

### Dependencies Required

#### Environment Variables:
- ✅ `WORKFLOW_PATH` - Path to workflow directory

#### Credentials:
- ✅ `openai-credentials` - OpenAI API key

#### Python Scripts:
- ✅ `scripts/n8n-update-schema.py` - EXISTS ✅

### What Needs to Be Done
1. ✅ **RECREATE WORKFLOW** - DONE ✅
2. ⚠️ **Import workflow to n8n**
3. ⚠️ **Set environment variable:** `WORKFLOW_PATH`
4. ⚠️ **Configure credential:** `openai-credentials`
5. ⚠️ **Activate workflow**
6. ✅ Test webhook: `POST /webhook/game-exercise-integration`

### Test Command (After Recreation)
```bash
curl -X POST http://192.168.1.226:5678/webhook/game-exercise-integration \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "exercise-1-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "Sequences",
      "mode": "story"
    }
  }'
```

### Status: ✅ **READY TO IMPORT** (Recreated)

---

## 📊 DEPENDENCY SUMMARY

### Environment Variables (All Workflows)
| Variable | Required By | Status |
|----------|-------------|--------|
| `WORKFLOW_PATH` | All Phase 2 workflows | ⚠️ Need to verify |
| `GITHUB_REPO_OWNER` | Unity Orchestrator, Screenshot Fix | ⚠️ Need to verify |
| `GITHUB_REPO_NAME` | Unity Orchestrator, Screenshot Fix | ⚠️ Need to verify |
| `GITHUB_WORKFLOW_FILE` | Unity Orchestrator, Screenshot Fix | ⚠️ Need to verify |
| `NETLIFY_SITE_ID` | Unity Orchestrator | ⚠️ Need to verify |
| `NETLIFY_SITE_NAME` | Unity Orchestrator, Screenshot Fix | ⚠️ Need to verify |
| `N8N_INSTANCE_ROLE` | Unity Orchestrator | ⚠️ Need to verify |

### Credentials (All Workflows)
| Credential | Required By | Status |
|------------|-------------|--------|
| `openai-credentials` | Full Integration, Screenshot Fix, Book Update, Curriculum Sync, Game Exercise | ⚠️ Need to verify |
| `github-actions-token` | Unity Orchestrator, Screenshot Fix | ⚠️ Need to verify |
| `netlify-api-token` | Unity Orchestrator | ⚠️ Need to verify |

### Python Scripts
| Script | Required By | Status |
|--------|-------------|--------|
| `scripts/n8n-update-schema.py` | Full Integration, Book Update, Curriculum Sync, Game Exercise | ✅ EXISTS |
| `screenshot_fix_processor.py` | Screenshot Fix | ✅ EXISTS |

---

## 🚀 ACTION PLAN

### Phase 1: Critical Workflow (IMMEDIATE)
1. ✅ **Unity Build Orchestrator** - Verify activation and test

### Phase 2: High Priority (THIS WEEK)
2. ⚠️ **Full Integration Workflow** - Import, configure, test
3. ⚠️ **Recreate Game Exercise Integration** - Build from scratch

### Phase 3: Medium Priority (NEXT WEEK)
4. ⚠️ **Book Content Update** - Import, configure, test
5. ⚠️ **Curriculum Sync** - Import, configure, test

### Phase 4: Low Priority (OPTIONAL)
6. ⚠️ **Screenshot to Fix** - Import, configure, test (if needed)

---

## 🧪 TESTING STRATEGY

### Step 1: Verify Current State
- Check which workflows are imported in n8n
- Check which workflows are active
- Verify environment variables
- Verify credentials

### Step 2: Test Each Workflow
- Test webhook endpoints
- Verify node execution
- Check for errors
- Validate outputs

### Step 3: Integration Testing
- Test workflows together
- Verify data flow between workflows
- Test error handling

---

## 📝 NEXT STEPS

1. **Run test script** to check current state
2. **Import missing workflows** in priority order
3. **Configure dependencies** (env vars, credentials)
4. **Test each workflow** individually
5. **Document any issues** and fix them
6. **Recreate Game Exercise Integration** workflow

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** 🔄 In Progress - Ready for Testing


