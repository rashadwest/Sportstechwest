# Quick Action Checklist - December 18, 2025

**Status:** Credentials created, needs verification and fixes

---

## ✅ DONE TODAY

- [x] Created GitHub credential (`github-actions-token`)
- [x] Created Netlify credential (`netlify-api-token`)
- [x] Tested Unity Build webhook (working, but locked)
- [x] Reviewed Garvis Orchestrator nodes
- [x] Created test scripts and documentation

---

## ⚠️ NEEDS FIXING (Priority Order)

### **1. Fix Garvis Orchestrator Nodes** (5 min)
- [ ] Open Garvis Orchestrator workflow in n8n
- [ ] For each "Execute" node (5 nodes):
  - [ ] Change Method: **GET → POST**
  - [ ] Save
- [ ] Test webhook

**Nodes to fix:**
- Execute: Book Content Update
- Execute: Curriculum Sync
- Execute: Unity Build
- Execute: Website Update
- Execute: Sales/Onboarding

---

### **2. Verify Credentials Work** (10 min)
- [ ] Wait for workflow lock to clear (or check n8n UI)
- [ ] Run test: `./test-unity-build-workflow.sh`
- [ ] Check n8n execution for errors
- [ ] If credential errors:
  - [ ] Verify credential Name/ID is exactly:
    - `github-actions-token`
    - `netlify-api-token`
  - [ ] Check Header Name is `Authorization`
  - [ ] Check Header Value has correct token format:
    - GitHub: `token YOUR_PAT`
    - Netlify: `Bearer YOUR_TOKEN`

---

### **3. Verify Environment Variables** (5 min)
- [ ] Check if all required vars are set:
  - `GITHUB_REPO_OWNER`
  - `GITHUB_REPO_NAME`
  - `GITHUB_WORKFLOW_FILE`
  - `NETLIFY_SITE_ID` (can be placeholder)
- [ ] If missing, run: `python scripts/robot-hardcode-env-vars.py`

---

### **4. Test End-to-End Flow** (15 min)
- [ ] Test Garvis Orchestrator webhook
- [ ] Verify it calls Unity Build workflow
- [ ] Verify GitHub Actions triggers
- [ ] Verify Netlify deployment
- [ ] Check all credentials work

---

## 🧪 TEST COMMANDS

**Test Unity Build:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./test-unity-build-workflow.sh
```

**Check Status:**
```bash
./check-workflow-status.sh
```

**Manual Test:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

---

## 📊 CURRENT STATUS

| Task | Status | Time |
|------|--------|------|
| Credentials Created | ✅ Done | - |
| Garvis Nodes Fix | ⚠️ Needs Fix | 5 min |
| Credential Verification | ⚠️ Pending | 10 min |
| Env Var Check | ⚠️ Pending | 5 min |
| End-to-End Test | ❌ Not Done | 15 min |

**Total Remaining:** ~35 minutes

---

**Next: Fix Garvis nodes (GET→POST), then verify credentials!** ✅
