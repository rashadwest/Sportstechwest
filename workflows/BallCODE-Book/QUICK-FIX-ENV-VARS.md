# Quick Fix: Environment Variables (Option B)

**Date:** December 18, 2025  
**Issue:** SSH access not available, using Option B (hardcode in workflow)

---

## 🚀 QUICK SOLUTION

**Since SSH access failed, we're using Option B: Hardcode values in workflow**

### **Step 1: Run Robot Script**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/robot-hardcode-env-vars.py
```

**What it does:**
- Asks for Netlify Site ID
- Modifies workflow JSON to hardcode values
- Creates backup of original workflow
- Updates all nodes that use env vars

### **Step 2: Re-import Workflow in n8n**

1. Go to: http://192.168.1.226:5678
2. Open "Unity Build Orchestrator" workflow
3. Click **"..." menu** → **"Delete"** (or deactivate first)
4. Click **"Workflows"** → **"Import from File"**
5. Select: `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
6. Click **"Import"**
7. **Activate** the workflow

### **Step 3: Verify**

```bash
python scripts/verify-garvis-unity-integration.py
```

### **Step 4: Test**

```bash
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game"
```

---

## 📋 WHAT GETS HARDCODED

**Values set in workflow:**
- `GITHUB_REPO_OWNER` = "rashadwest"
- `GITHUB_REPO_NAME` = "BTEBallCODE"
- `GITHUB_WORKFLOW_FILE` = "unity-webgl-build.yml"
- `NETLIFY_SITE_ID` = "[your site ID]"

**Where:**
- Code node: "Env Preflight + Dev Guardrails (AIMCODE L1)"
- GitHub API nodes (URLs updated)
- Netlify API nodes (URLs updated)

---

## ⚠️ IMPORTANT NOTES

1. **Backup created:** Original workflow saved as `.json.backup`
2. **Re-import required:** Must re-import workflow in n8n after modification
3. **Less secure:** Values visible in workflow JSON (but works without SSH)

---

## ✅ SUCCESS CRITERIA

- ✅ Robot script runs successfully
- ✅ Workflow file modified
- ✅ Workflow re-imported in n8n
- ✅ Verification script passes
- ✅ Test build succeeds

---

**Run the robot script now!** 🤖

