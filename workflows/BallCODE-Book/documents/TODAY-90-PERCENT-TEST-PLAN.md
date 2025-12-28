# 🎯 Today's 90% Integration Test Plan

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Goal:** Reach 90% integration completion  
**Status:** ✅ Ready - Old Orchestrator Verified

---

## ✅ VERIFICATION COMPLETE

**Old Unity Build Orchestrator:**
- ✅ JSON Valid
- ✅ 13 nodes
- ✅ No empty options (import-ready)
- ✅ Ready to use

**Desktop Folder:**
- ✅ 3 workflows ready to import
- ✅ All simplified and optimized

---

## 🧪 TESTING SEQUENCE (40 minutes to 90%)

### PHASE 1: Import & Activate (5 min) ⏱️

**In Pi n8n UI:** `http://192.168.1.226:5678`

1. **Import Workflows:**
   - [ ] Import `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
   - [ ] Import `n8n-screenshot-to-fix-workflow.json`
   - [ ] Import `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`

2. **Activate All:**
   - [ ] Toggle each workflow to "Active" (green/blue)
   - [ ] Verify all 3 are active

**✅ Phase 1 Complete When:** All 3 workflows imported and active

---

### PHASE 2: Test Unity Build Orchestrator (5 min) ⏱️

**Test Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**Verify:**
- [ ] Webhook receives request (check n8n executions)
- [ ] Workflow executes without errors
- [ ] Response returned (check response body)
- [ ] All nodes execute successfully

**✅ Phase 2 Complete When:** Workflow executes and returns response

---

### PHASE 3: Test Full Integration Simplified (5 min) ⏱️

**Test Command:**
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
- [ ] AI analyzes prompt (check execution)
- [ ] Action plan returned in response
- [ ] Response includes schema update instructions

**Expected Response:**
```json
{
  "status": "success",
  "actionPlan": {
    "analysis": {...},
    "schemaUpdates": {
      "whatToUpdate": "...",
      "howToUpdate": "..."
    }
  }
}
```

**✅ Phase 3 Complete When:** AI returns actionable plan

---

### PHASE 4: Test JavaScript Auto-Sync (10 min) ⏱️

**4.1: Update Schema**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Edit CURRICULUM-DATA-EXAMPLE.json
# Change Book 1 title to "TEST: Updated Title" or add test learning objective

# Copy to API location
cp CURRICULUM-DATA-EXAMPLE.json BallCode/data/curriculum-data.json
```

**4.2: Test Website Auto-Sync**
- Open website: `http://localhost:8080` or Netlify URL
- Check browser console (F12) for integration.js loading
- Verify:
  - [ ] Book cards update automatically
  - [ ] Book pages show updated content
  - [ ] Curriculum pathway displays
  - [ ] Learning objectives show correctly

**4.3: Test Book Page Sync**
- Navigate to Book 1 page
- Verify:
  - [ ] "What You're Learning" section updates
  - [ ] Learning objectives display
  - [ ] Exercise button links correctly

**✅ Phase 4 Complete When:** All systems sync automatically from schema

---

### PHASE 5: Test Screenshot to Fix (5 min) ⏱️

**Test Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error.png",
    "context": "n8n workflow error test"
  }'
```

**Verify:**
- [ ] Webhook receives request
- [ ] Vision AI analyzes screenshot
- [ ] Diagnosis returned
- [ ] Fix suggested (if auto-fixable)

**✅ Phase 5 Complete When:** Screenshot analysis works

---

### PHASE 6: End-to-End Integration Test (10 min) ⏱️

**6.1: Get Action Plan from AI**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Update Book 1 to add loops concept", "mode": "quick"}'
```

**6.2: Follow Action Plan**
- Read the `schemaUpdates` section from response
- Update `CURRICULUM-DATA-EXAMPLE.json` accordingly
- Copy to `BallCode/data/curriculum-data.json`

**6.3: Verify Complete Integration**
- Check website updates
- Check book pages update
- Check curriculum displays
- Verify all 4 systems synchronized

**✅ Phase 6 Complete When:** Complete loop works: AI → Schema → Auto-Sync → All Systems

---

## ✅ 90% COMPLETION CHECKLIST

### Core Systems (Must Have):
- [ ] Unified Schema working (`CURRICULUM-DATA-EXAMPLE.json`)
- [ ] JavaScript auto-sync working (`integration.js`)
- [ ] Netlify Functions API working (all endpoints)
- [ ] Website reads from schema
- [ ] Books read from schema
- [ ] Curriculum reads from schema

### Workflows (Must Have):
- [ ] Unity Build Orchestrator executes successfully
- [ ] Full Integration Simplified returns action plans
- [ ] Screenshot to Fix analyzes screenshots

### Integration Points (Must Have):
- [ ] Website → Book (links work)
- [ ] Book → Game (exercise buttons work)
- [ ] Book → Curriculum (learning sections sync)
- [ ] Curriculum → Website (pathway displays)

**🎯 90% = ALL ABOVE CHECKED ✅**

---

## 🚨 QUICK TROUBLESHOOTING

### Workflow Not Executing?
1. Check workflow is **Active** (green/blue toggle)
2. Check webhook path matches exactly
3. Check n8n execution logs for errors
4. Verify credentials configured (OpenAI API)

### JavaScript Not Syncing?
1. Check `BallCode/data/curriculum-data.json` exists
2. Check browser console (F12) for errors
3. Verify `integration.js` loaded on page
4. Check API endpoints accessible

### Schema Not Updating?
1. Verify JSON is valid (no syntax errors)
2. Check file paths are correct
3. Verify file permissions
4. Check both files updated (source + API copy)

---

## 📊 PROGRESS TRACKING

**Current Status:** Ready to test  
**Target:** 90% integration  
**Time Estimate:** 40 minutes

**After Testing:**
- ✅ All workflows working = 90% complete
- ⚠️ Any issues = Fix and retest

---

## 🎯 SUCCESS = 90%

**You're at 90% when:**
- All 3 workflows imported and active
- All 3 workflows execute successfully
- JavaScript auto-syncs all systems
- Integration points verified
- End-to-end flow works

**Then you can:**
- Document any remaining 10%
- Plan final optimizations
- Celebrate! 🎉

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Execute



