# 🏗️ Garvis n8n Essential Infrastructure - Complete Integration Plan

**Date:** December 17, 2025  
**Status:** 📋 Infrastructure Architecture - Ready for Implementation  
**Purpose:** All 3 n8n workflows as essential infrastructure for Garvis autonomous Unity builds

---

## 🎯 THE 3 ESSENTIAL N8N WORKFLOWS

### **Workflow #1: Unity Build Orchestrator** 🔴 **CRITICAL**
**File:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`  
**Webhook:** `POST /webhook/unity-build`  
**Status:** ✅ Working (needs activation in UI)

### **Workflow #2: Garvis Orchestrator** 🟠 **HIGH PRIORITY**
**File:** `n8n-garvis-orchestrator-workflow.json`  
**Webhook:** `POST /webhook/garvis`  
**Status:** ✅ Ready (routes to all systems)

### **Workflow #3: Full Integration Workflow** 🟡 **ESSENTIAL**
**File:** `n8n-ballcode-full-integration-workflow.json`  
**Webhook:** `POST /webhook/ballcode-dev`  
**Status:** ✅ Active (AI-driven development)

---

## 🏗️ INFRASTRUCTURE ARCHITECTURE

### **The 24/7 Pi Advantage**

```
┌─────────────────────────────────────────────────────────────┐
│              Raspberry Pi (Running 24/7)                    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         n8n Instance (Always Active)                  │  │
│  │                                                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Workflow #1: Unity Build Orchestrator         │  │  │
│  │  │  - Triggers GitHub Actions builds              │  │  │
│  │  │  - Monitors build progress                     │  │  │
│  │  │  - Deploys to Netlify                          │  │  │
│  │  │  - Lock mechanism (prevents overlaps)          │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  │                                                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Workflow #2: Garvis Orchestrator               │  │  │
│  │  │  - Routes tasks to correct systems              │  │  │
│  │  │  - Identifies: game, curriculum, book, website  │  │  │
│  │  │  - Coordinates multi-system updates             │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  │                                                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Workflow #3: Full Integration                  │  │  │
│  │  │  - AI analysis (AIMCODE methodology)            │  │  │
│  │  │  - Updates all 4 systems simultaneously         │  │  │
│  │  │  - Unified curriculum schema integration        │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Why This Matters:**
- ✅ **Always Running:** Pi never sleeps, workflows always available
- ✅ **Consistent Builds:** Can deploy builds anytime, day or night
- ✅ **No Manual Intervention:** Fully automated 24/7
- ✅ **Reliable:** Dedicated hardware, no Mac sleep issues

---

## 🔄 HOW GARVIS LEVERAGES ALL 3 WORKFLOWS

### **Complete Flow: 23 Questions → Autonomous Execution**

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: You Answer 23 Questions (--full)                   │
│  Creates: UNITY-BUILD-PLAN-YYYY-MM-DD.md                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Garvis Orchestrator (Workflow #2)                 │
│  Webhook: POST /webhook/garvis                              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Reads plan file                                    │  │
│  │  • Identifies systems: ["game", "curriculum", ...]    │  │
│  │  • Routes to: "unity-build" workflow                  │  │
│  │  • Creates job ID: garvis-{timestamp}                  │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Full Integration (Workflow #3)                     │
│  Webhook: POST /webhook/ballcode-dev                        │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • AI Analysis (OpenAI GPT-4)                         │  │
│  │  • Parses 23 answers into execution plan              │  │
│  │  • Identifies:                                        │  │
│  │    - Which C# scripts to modify                       │  │
│  │    - Which Unity scenes to update                      │  │
│  │    - Which assets to add/change                        │  │
│  │    - Build configuration changes                       │  │
│  │  • Creates layered action plan (AIMCODE)               │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Garvis Executes (Python Scripts)                  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Clones/updates Unity repo (GitHub API)            │  │
│  │  • Creates feature branch                            │  │
│  │  • Makes code changes (C# scripts, scenes)           │  │
│  │  • Commits and pushes to GitHub                      │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Unity Build Orchestrator (Workflow #1)            │
│  Webhook: POST /webhook/unity-build                         │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Acquires lock (prevents overlapping builds)        │  │
│  │  • Triggers GitHub Actions build                      │  │
│  │  • Monitors build progress (polls GitHub API)        │  │
│  │  • Waits for build completion                        │  │
│  │  • If build fails: Retries or reports error          │  │
│  │  • If build succeeds: Proceeds to deployment         │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Netlify Deployment (via Workflow #1)              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Checks Netlify deployment status                  │  │
│  │  • Verifies deployment URL                           │  │
│  │  • Confirms build is live                            │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Progress Report (End of Day)                      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Generates: GARVIS-UNITY-PROGRESS-YYYY-MM-DD.md    │  │
│  │  • Summary: What was completed                       │  │
│  │  • Pending: What needs to be done tomorrow           │  │
│  │  • Errors: Any issues encountered                     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 DETAILED WORKFLOW BREAKDOWN

### **Workflow #1: Unity Build Orchestrator** 🔴

**Purpose:** Handles all Unity builds and deployments

**Key Features:**
- ✅ **Lock Mechanism:** Prevents overlapping builds (55-minute lock)
- ✅ **Dev Guardrails:** Prevents accidental builds on dev Mac
- ✅ **GitHub Actions Integration:** Triggers and monitors builds
- ✅ **Netlify Integration:** Checks deployment status
- ✅ **Error Handling:** Retries and reports failures
- ✅ **Comprehensive Reporting:** Full build/deploy status

**Nodes (13 total):**
1. Scheduled Trigger (Hourly) [DISABLED ON DEV]
2. Webhook Trigger (`/webhook/unity-build`)
3. Normalize Input (AIMCODE L1)
4. Env Preflight + Dev Guardrails (AIMCODE L1)
5. Acquire Lock (AIMCODE L1)
6. Proceed? (Conditional)
7. Dispatch GitHub Build (AIMCODE L2)
8. Wait (3 min)
9. Check Latest GitHub Run (AIMCODE L3)
10. Check Latest Netlify Deploy (AIMCODE L3)
11. Compile Report (AIMCODE L4)
12. Release Lock (AIMCODE L4)
13. Respond to Webhook

**How Garvis Uses It:**
- Garvis calls this workflow after making code changes
- Workflow handles build orchestration automatically
- No manual intervention needed
- Runs 24/7 on Pi, always available

---

### **Workflow #2: Garvis Orchestrator** 🟠

**Purpose:** Routes tasks to correct systems and coordinates multi-system updates

**Key Features:**
- ✅ **System Identification:** Detects which systems need updates
- ✅ **Task Routing:** Routes to appropriate workflows
- ✅ **Job Tracking:** Creates unique job IDs
- ✅ **Multi-System Coordination:** Handles game + curriculum + book + website updates

**Nodes:**
1. Garvis Webhook Trigger (`/webhook/garvis`)
2. Parse Input & Identify Systems
3. Route: Book System?
4. Route: Curriculum System?
5. Route: Game System? ← **Unity builds go here**
6. Route: Website System?
7. Route: Sales System?
8. Execute: Unity Build (calls Workflow #1)
9. Execute: Book Content Update
10. Execute: Curriculum Sync
11. Execute: Website Update
12. Execute: Sales/Onboarding
13. Aggregate Results
14. Respond with Results

**How Garvis Uses It:**
- Garvis sends 23-question plan to this workflow
- Workflow identifies Unity game needs updates
- Routes to Unity Build Orchestrator (Workflow #1)
- Coordinates with other systems if needed

---

### **Workflow #3: Full Integration Workflow** 🟡

**Purpose:** AI-driven development automation using AIMCODE methodology

**Key Features:**
- ✅ **AI Analysis:** Uses OpenAI GPT-4 to analyze prompts
- ✅ **AIMCODE Methodology:** Layer 1 → 2 → 3 → 4 approach
- ✅ **Unified Curriculum Schema:** Single source of truth
- ✅ **Multi-System Updates:** Updates Game, Curriculum, Book, Website simultaneously
- ✅ **Memory Context:** Saves context for future reference

**Nodes:**
1. Webhook Trigger (`/webhook/ballcode-dev`)
2. Normalize Input & Extract Prompt
3. AI Analyze Prompt (OpenAI GPT-4)
4. Parse AI Response
5. Save Memory Context
6. Respond with Action Plan

**How Garvis Uses It:**
- Garvis sends 23-question answers to this workflow
- AI analyzes and creates detailed execution plan
- Identifies specific files to modify
- Creates layered action plan (Foundation → Application → Integration → Mastery)
- Saves context for next-day continuation

---

## 🔗 WORKFLOW INTEGRATION POINTS

### **How They Connect:**

```
23 Questions → Garvis Orchestrator (#2)
                    ↓
            Full Integration (#3)
                    ↓
            (AI Analysis & Planning)
                    ↓
            Garvis Python Scripts
                    ↓
            (Code Changes)
                    ↓
            Unity Build Orchestrator (#1)
                    ↓
            (Build & Deploy)
                    ↓
            Progress Report
```

### **API Calls Between Workflows:**

**Garvis Orchestrator → Full Integration:**
```bash
POST http://192.168.1.226:5678/webhook/ballcode-dev
{
  "prompt": "[23-question answers]",
  "mode": "full",
  "context": { "jobId": "garvis-123", "systems": ["game"] }
}
```

**Garvis Orchestrator → Unity Build Orchestrator:**
```bash
POST http://192.168.1.226:5678/webhook/unity-build
{
  "request": "Build Unity game with changes from plan",
  "branch": "main",
  "jobId": "garvis-123"
}
```

**Full Integration → Garvis Orchestrator (callback):**
```bash
POST http://192.168.1.226:5678/webhook/garvis
{
  "actionPlan": { ... },
  "jobId": "garvis-123",
  "nextStep": "execute-unity-build"
}
```

---

## ⚙️ CONFIGURATION REQUIREMENTS

### **Environment Variables (All Workflows):**

**For Unity Build Orchestrator:**
- `GITHUB_REPO_OWNER` = "rashadwest"
- `GITHUB_REPO_NAME` = "BTEBallCODE"
- `GITHUB_WORKFLOW_FILE` = "unity-webgl-build.yml"
- `NETLIFY_SITE_ID` = "[your-site-id]"
- `NETLIFY_SITE_NAME` = "ballcode-game"
- `N8N_INSTANCE_ROLE` = "prod" (on Pi)

**For Full Integration:**
- `OPENAI_API_KEY` = "[your-openai-key]"

**For All Workflows:**
- `GITHUB_PAT` = "[github-personal-access-token]"
- `NETLIFY_AUTH_TOKEN` = "[netlify-access-token]"

### **Credentials (n8n UI):**

1. **GitHub Actions Token:**
   - Type: HTTP Header Auth
   - Name: `github-actions-token`
   - Header: `Authorization`
   - Value: `token YOUR_GITHUB_PAT`

2. **Netlify API Token:**
   - Type: HTTP Header Auth
   - Name: `netlify-api-token`
   - Header: `Authorization`
   - Value: `Bearer YOUR_NETLIFY_TOKEN`

3. **OpenAI API Key:**
   - Type: OpenAI
   - Name: `openai-api`
   - API Key: `YOUR_OPENAI_KEY`

---

## 🚀 IMPLEMENTATION CHECKLIST

### **Phase 1: Verify All 3 Workflows (Today)**

- [ ] **Workflow #1: Unity Build Orchestrator**
  - [ ] Verify imported in n8n
  - [ ] Activate in n8n UI
  - [ ] Test webhook: `POST /webhook/unity-build`
  - [ ] Verify lock mechanism works
  - [ ] Test GitHub Actions trigger

- [ ] **Workflow #2: Garvis Orchestrator**
  - [ ] Verify imported in n8n
  - [ ] Activate in n8n UI
  - [ ] Test webhook: `POST /webhook/garvis`
  - [ ] Verify routing logic works
  - [ ] Test system identification

- [ ] **Workflow #3: Full Integration**
  - [ ] Verify imported in n8n
  - [ ] Activate in n8n UI
  - [ ] Test webhook: `POST /webhook/ballcode-dev`
  - [ ] Verify OpenAI integration
  - [ ] Test AI analysis output

### **Phase 2: Connect Workflows (Tomorrow)**

- [ ] **Create Integration Scripts:**
  - [ ] `scripts/garvis-trigger-orchestrator.py` - Triggers Workflow #2
  - [ ] `scripts/garvis-trigger-full-integration.py` - Triggers Workflow #3
  - [ ] `scripts/garvis-trigger-unity-build.py` - Triggers Workflow #1

- [ ] **Test End-to-End Flow:**
  - [ ] Create test plan file
  - [ ] Trigger Garvis Orchestrator
  - [ ] Verify Full Integration analysis
  - [ ] Verify Unity Build Orchestrator execution
  - [ ] Verify build completes and deploys

### **Phase 3: Full Automation (Ready to Use)**

- [ ] **Documentation Complete:**
  - [ ] All workflows documented
  - [ ] Integration points clear
  - [ ] Error handling defined

- [ ] **Monitoring Setup:**
  - [ ] n8n execution logs
  - [ ] Progress reporting
  - [ ] Error notifications

---

## 📈 BENEFITS OF 24/7 PI INFRASTRUCTURE

### **Why This Is Essential:**

1. **Always Available:**
   - Pi never sleeps
   - Workflows always running
   - Can trigger builds anytime

2. **Consistent Builds:**
   - No Mac sleep issues
   - No manual wake-up needed
   - Reliable deployment schedule

3. **Fully Automated:**
   - Zero manual intervention
   - True "Set It And Forget It"
   - Works while you sleep

4. **Scalable:**
   - Can handle multiple builds
   - Lock mechanism prevents conflicts
   - Queue system for multiple requests

5. **Cost Effective:**
   - Low power consumption
   - Always-on without high costs
   - Dedicated automation server

---

## ✅ SUCCESS CRITERIA

**You Can:**
1. ✅ Answer 23 questions (--full)
2. ✅ Walk away
3. ✅ Garvis Orchestrator routes to Full Integration
4. ✅ Full Integration analyzes and plans
5. ✅ Garvis executes code changes
6. ✅ Unity Build Orchestrator builds and deploys
7. ✅ Get end-of-day report
8. ✅ All happens 24/7 on Pi automatically

**All 3 Workflows:**
1. ✅ Running on Pi 24/7
2. ✅ Connected and integrated
3. ✅ Handling errors gracefully
4. ✅ Reporting progress
5. ✅ Continuing next day seamlessly

---

## 🔗 RELATED DOCUMENTS

- `GARVIS-UNITY-AUTONOMOUS-BUILD-PLAN.md` - Overall plan
- `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json` - Workflow #1
- `n8n-garvis-orchestrator-workflow.json` - Workflow #2
- `n8n-ballcode-full-integration-workflow.json` - Workflow #3
- `N8N-WORKFLOWS-END-TO-END-ANALYSIS.md` - Workflow analysis

---

**All 3 workflows are essential infrastructure for Garvis!** 🏗️✨

