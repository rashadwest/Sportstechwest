# ⚡ Quick Test Commands - 90% Integration

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Goal:** Quick testing to reach 90% integration

---

## ✅ WORKFLOWS READY

1. ✅ Unity Build Orchestrator (old version - kept)
2. ✅ Screenshot to Fix
3. ✅ Full Integration Simplified

---

## 🧪 QUICK TEST SEQUENCE (40 minutes)

### Step 1: Import & Activate (5 min)

**In Pi n8n UI (`http://192.168.1.226:5678`):**
1. Import all 3 workflows from desktop
2. Activate each workflow (toggle switch)
3. Verify all are active (green/blue)

---

### Step 2: Test Unity Build Orchestrator (5 min)

```bash
# Test webhook trigger
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**Expected:** Workflow executes, returns response

**Verify:**
- [ ] Webhook receives request
- [ ] Workflow executes
- [ ] Response returned

---

### Step 3: Test Full Integration Simplified (5 min)

```bash
# Test AI analysis
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new learning objective to Book 1 about loops",
    "mode": "quick"
  }'
```

**Expected:** AI returns action plan with schema update instructions

**Verify:**
- [ ] Webhook receives request
- [ ] AI analyzes prompt
- [ ] Action plan returned
- [ ] Response includes schema update instructions

---

### Step 4: Test JavaScript Auto-Sync (10 min)

**4.1: Update Schema**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Edit CURRICULUM-DATA-EXAMPLE.json - add test data
# Example: Change Book 1 title to "TEST: Updated Title"

# Copy to API location
cp CURRICULUM-DATA-EXAMPLE.json BallCode/data/curriculum-data.json
```

**4.2: Test Website Sync**
- Open website (local or Netlify)
- Verify book cards update automatically
- Check book pages show updated content

**Verify:**
- [ ] Schema updated
- [ ] Website auto-syncs
- [ ] Book pages update
- [ ] Curriculum displays correctly

---

### Step 5: Test Screenshot to Fix (5 min)

```bash
# Test screenshot analysis
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error.png",
    "context": "n8n workflow error test"
  }'
```

**Expected:** Vision AI analyzes screenshot, returns diagnosis

**Verify:**
- [ ] Webhook receives request
- [ ] Vision AI analyzes
- [ ] Diagnosis returned

---

### Step 6: End-to-End Integration Test (10 min)

**6.1: Use Full Integration to get action plan**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Update Book 1 learning objectives", "mode": "quick"}'
```

**6.2: Follow action plan**
- Update `CURRICULUM-DATA-EXAMPLE.json` per action plan
- Copy to `BallCode/data/curriculum-data.json`

**6.3: Verify auto-sync**
- Check website updates
- Check book pages update
- Check curriculum updates

**Verify:**
- [ ] AI analysis works
- [ ] Schema updates correctly
- [ ] JavaScript syncs automatically
- [ ] All systems updated

---

## ✅ 90% COMPLETION CHECKLIST

### Core Systems:
- [ ] Unified Schema working
- [ ] JavaScript auto-sync working
- [ ] Netlify Functions API working
- [ ] Website reads from schema
- [ ] Books read from schema
- [ ] Curriculum reads from schema

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

## 🎯 90% = ALL CHECKED ✅

**When all boxes are checked, you're at 90%!**

---

## 🚨 TROUBLESHOOTING

### Workflow not executing?
- Check workflow is active (green/blue toggle)
- Check webhook path matches exactly
- Check n8n logs for errors

### JavaScript not syncing?
- Check `BallCode/data/curriculum-data.json` exists
- Check browser console for errors
- Verify `integration.js` is loaded on page

### Schema not updating?
- Verify JSON is valid (no syntax errors)
- Check file paths are correct
- Verify file permissions

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Test



