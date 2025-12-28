# 🎯 90% Integration Test Plan - Today's Goal

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Goal:** Reach 90% integration completion  
**Status:** Ready for Testing

---

## ✅ CURRENT STATE

### Workflows Ready:
1. ✅ Unity Build Orchestrator (old version - kept after error)
2. ✅ Screenshot to Fix
3. ✅ Full Integration - Simplified (AI Analysis only)

### Integration Systems:
- ✅ Unified Schema: `CURRICULUM-DATA-EXAMPLE.json`
- ✅ JavaScript Auto-Sync: `BallCode/js/integration.js`
- ✅ Netlify Functions API: All endpoints working
- ✅ Website: Auto-syncs from schema
- ✅ Books: Auto-syncs from schema
- ✅ Curriculum: Auto-syncs from schema

---

## 🧪 TEST PLAN - 90% INTEGRATION

### Phase 1: Workflow Import & Activation ✅

**Test 1.1: Import Workflows**
- [ ] Import Unity Build Orchestrator to Pi n8n
- [ ] Import Screenshot to Fix to Pi n8n
- [ ] Import Full Integration Simplified to Pi n8n
- [ ] Verify all 3 workflows imported successfully

**Test 1.2: Activate Workflows**
- [ ] Activate Unity Build Orchestrator
- [ ] Activate Screenshot to Fix
- [ ] Activate Full Integration Simplified
- [ ] Verify all workflows are active (green/blue toggle)

**Expected Result:** All 3 workflows imported and active

---

### Phase 2: Unity Build Orchestrator Test ✅

**Test 2.1: Manual Trigger**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**Verify:**
- [ ] Webhook receives request
- [ ] Workflow executes
- [ ] GitHub Actions triggered (if configured)
- [ ] Response returned

**Expected Result:** Workflow executes successfully

---

### Phase 3: JavaScript Auto-Sync Test ✅

**Test 3.1: Schema Update → Auto-Sync**
1. Update `CURRICULUM-DATA-EXAMPLE.json`:
   ```json
   {
     "books": [{
       "id": 1,
       "title": "TEST: Updated Title",
       "curriculum": {
         "learningObjectives": ["TEST: New objective"]
       }
     }]
   }
   ```

2. Copy to API location:
   ```bash
   cp CURRICULUM-DATA-EXAMPLE.json BallCode/data/curriculum-data.json
   ```

3. Open website: `http://localhost:8080` (or Netlify URL)

4. Verify:
   - [ ] Website book cards update automatically
   - [ ] Book pages show updated content
   - [ ] Curriculum pathway updates
   - [ ] Learning objectives display correctly

**Expected Result:** All systems sync automatically without n8n

---

### Phase 4: Full Integration Simplified Test ✅

**Test 4.1: AI Analysis**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new learning objective to Book 1 about loops",
    "mode": "quick"
  }'
```

**Verify:**
- [ ] Webhook receives request
- [ ] AI analyzes prompt
- [ ] Action plan returned
- [ ] Response includes schema update instructions

**Expected Result:** AI returns action plan with schema update instructions

---

### Phase 5: Screenshot to Fix Test ✅

**Test 5.1: Error Screenshot Analysis**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error.png",
    "context": "n8n workflow error"
  }'
```

**Verify:**
- [ ] Webhook receives request
- [ ] Vision AI analyzes screenshot
- [ ] Diagnosis returned
- [ ] Fix generated (if auto-fixable)

**Expected Result:** Screenshot analyzed and fix suggested

---

### Phase 6: End-to-End Integration Test ✅

**Test 6.1: Complete Flow**
1. Use Full Integration workflow to analyze prompt
2. Get action plan with schema update instructions
3. Update `CURRICULUM-DATA-EXAMPLE.json` manually or via Python
4. Copy to `BallCode/data/curriculum-data.json`
5. Verify JavaScript auto-syncs all systems
6. Test website, books, curriculum all updated

**Verify:**
- [ ] AI analysis works
- [ ] Schema updates correctly
- [ ] JavaScript syncs automatically
- [ ] All 4 systems updated
- [ ] No manual steps needed (except schema update)

**Expected Result:** Complete integration loop works

---

## 📊 INTEGRATION CHECKLIST

### Core Systems:
- [ ] Unified Schema working
- [ ] JavaScript auto-sync working
- [ ] Netlify Functions API working
- [ ] Website reads from schema
- [ ] Books read from schema
- [ ] Curriculum reads from schema
- [ ] Game exercises linked to schema

### Workflows:
- [ ] Unity Build Orchestrator working
- [ ] Screenshot to Fix working
- [ ] Full Integration Simplified working

### Integration Points:
- [ ] Website → Book (links work)
- [ ] Book → Game (exercise buttons work)
- [ ] Game → Book (return flow works)
- [ ] Book → Curriculum (learning sections sync)
- [ ] Curriculum → Website (pathway displays)

---

## 🎯 90% COMPLETION CRITERIA

**90% = All Core Systems Working + Most Integration Points**

### Must Have (90%):
- ✅ Unified schema system working
- ✅ JavaScript auto-sync working
- ✅ All 3 workflows imported and active
- ✅ Unity Build Orchestrator executes
- ✅ Full Integration returns action plans
- ✅ Website syncs from schema
- ✅ Books sync from schema
- ✅ Curriculum syncs from schema

### Nice to Have (100%):
- ⚠️ Screenshot to Fix fully tested
- ⚠️ Python script for schema updates
- ⚠️ Automated testing suite
- ⚠️ Error monitoring

---

## 🚀 QUICK TEST COMMANDS

### Test Unity Build:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

### Test Full Integration:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test analysis", "mode": "quick"}'
```

### Test Screenshot Fix:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/error.png", "context": "test"}'
```

### Test Schema Sync:
1. Update `CURRICULUM-DATA-EXAMPLE.json`
2. `cp CURRICULUM-DATA-EXAMPLE.json BallCode/data/curriculum-data.json`
3. Open website → Verify auto-sync

---

## 📋 TESTING ORDER

1. **Import & Activate** (5 min)
2. **Unity Build Test** (5 min)
3. **Schema Sync Test** (10 min)
4. **Full Integration Test** (5 min)
5. **End-to-End Test** (15 min)

**Total Time:** ~40 minutes to reach 90%

---

## ✅ SUCCESS CRITERIA

**90% Complete When:**
- All 3 workflows imported and active
- Unity Build Orchestrator executes successfully
- Full Integration returns action plans
- JavaScript auto-syncs all systems
- Website, Books, Curriculum all update from schema
- Integration points verified

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready for Testing



