# n8n Workflows - Ready to Use (Saved to Memory)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 15, 2025  
**Status:** ✅ Ready for Deployment  
**Purpose:** Document workflows that are ready to use when appropriate

---

## 🎯 READY-TO-USE WORKFLOWS

### 1. Full Integration Workflow ✅ **READY TO GO**

**File:** `n8n-ballcode-full-integration-workflow.json`

**Purpose:** AI-driven development automation that updates all 4 BallCODE systems (Game, Curriculum, Book, Website) in one go

**Features:**
- ✅ Analyzes development prompts using AIMCODE methodology (Demis Hassabis - Alpha Evolve)
- ✅ Updates all 4 systems simultaneously (Game, Curriculum, Book, Website)
- ✅ Uses unified curriculum schema as single source of truth
- ✅ Integrates unified prompting system (--quick and --full questions)
- ✅ Saves memory context for book/lesson/website updates
- ✅ Ensures seamless integration across all systems

**Webhook:** `/webhook/ballcode-dev`

**Usage:**
```bash
curl -X POST http://your-n8n-instance/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new exercise to Book 1",
    "mode": "full",
    "context": {}
  }'
```

**When to Use:**
- Development prompts that affect multiple systems
- Content updates that need cross-system synchronization
- New features requiring integration across Game, Curriculum, Book, and Website
- When you want AI-driven analysis with AIMCODE methodology

**Status:** ✅ **Ready to import and activate when needed**

---

### 2. Screenshot-to-Fix Workflow ✅ **READY TO GO**

**File:** `n8n-screenshot-to-fix-workflow.json`

**Purpose:** Visual debugging and auto-repair - analyzes screenshots and automatically fixes errors

**Features:**
- ✅ Analyzes screenshots for errors/issues
- ✅ Auto-generates fixes when possible
- ✅ Provides manual fix instructions when auto-fix isn't possible
- ✅ Integrates with development workflow
- ✅ Returns comprehensive fix reports

**Webhook:** `/webhook/screenshot-fix`

**Usage:**
```bash
curl -X POST http://your-n8n-instance/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshot_url": "https://...",
    "description": "Error message or issue description"
  }'
```

**When to Use:**
- Visual debugging of UI issues
- Error screenshots that need analysis
- Auto-repair of common issues
- When you have a screenshot of a problem and want automated fix suggestions

**Status:** ✅ **Ready to import and activate when needed**

**Note:** This workflow was fixed (connection issue resolved) and is ready for use.

---

## 📋 OTHER WORKFLOWS (Running Soon)

The user mentioned "the others running soon" - these likely refer to:

### Phase 2: Content Management Workflows
- **Book Content Update Workflow** - `n8n-book-content-update-workflow.json`
- **Curriculum Schema Sync Workflow** - `n8n-curriculum-sync-workflow.json`
- **Game Exercise Integration Workflow** - `n8n-game-exercise-integration-workflow.json`

### Python Hybrid Workflow
- **Unity Build Orchestrator (Python Hybrid)** - `n8n-unity-build-orchestrator-PYTHON-HYBRID.json`
  - Currently on desktop, ready to import
  - Uses Python scripts for reliable monitoring

---

## 🎯 DECISION GUIDE: When to Use Which Workflow

### Use Full Integration Workflow When:
- ✅ You have a development prompt that affects multiple systems
- ✅ You want AI-driven analysis with AIMCODE methodology
- ✅ You need cross-system synchronization
- ✅ You want comprehensive action planning with Alpha Evolve layers

### Use Screenshot-to-Fix Workflow When:
- ✅ You have a screenshot of an error or issue
- ✅ You want visual debugging assistance
- ✅ You need automated fix suggestions
- ✅ You're debugging UI or visual problems

### Use Python Hybrid Workflow When:
- ✅ You need reliable build monitoring
- ✅ You want better error handling than HTTP Request nodes
- ✅ You need reusable Python scripts
- ✅ You want structured JSON output for debugging

---

## 📝 IMPORTANT NOTES

1. **All workflows are ready to import** - No additional fixes needed
2. **Use when it makes sense** - Not all workflows need to run all the time
3. **Screenshot-to-Fix** was fixed (connection issue) and is production-ready
4. **Full Integration** uses AIMCODE methodology - best for complex multi-system updates
5. **Other workflows** (Phase 2, Python Hybrid) will be running soon

---

## 🚀 QUICK REFERENCE

| Workflow | File | Status | Webhook | Use When |
|----------|------|--------|---------|----------|
| Full Integration | `n8n-ballcode-full-integration-workflow.json` | ✅ Ready | `/webhook/ballcode-dev` | Multi-system updates |
| Screenshot-to-Fix | `n8n-screenshot-to-fix-workflow.json` | ✅ Ready | `/webhook/screenshot-fix` | Visual debugging |
| Python Hybrid | Desktop file | ✅ Ready | `/webhook/unity-build` | Build monitoring |

---

**Saved to Memory:** December 15, 2025  
**Status:** ✅ Ready to use when appropriate

