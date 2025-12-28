# Python Hybrid n8n Workflow - Quick Start Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 15, 2025  
**Status:** ✅ Ready to Use  
**Time to Setup:** 5 minutes

---

## 🎯 What This Is

A hybrid n8n workflow that combines:
- **n8n** for visual orchestration and triggers
- **Python scripts** for reliable monitoring and error handling

**Benefits:**
- ✅ Better error handling (Python try/except)
- ✅ Improved logging (structured JSON output)
- ✅ Reusable scripts (can run outside n8n)
- ✅ More maintainable (Python code vs n8n JSON)

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Run Environment Setup Script

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./setup-python-hybrid-env.sh
```

This will:
- ✅ Check Python scripts exist
- ✅ Verify Python dependencies
- ✅ Create/update `.n8n-hybrid-env` file
- ✅ Set `WORKFLOW_PATH` automatically
- ✅ Test Python scripts

### Step 2: Configure n8n Environment Variables

The setup script will show you what to add to n8n. Or manually:

**In n8n UI:**
1. Go to **Settings → Environment Variables**
2. Add these variables:

```bash
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
GITHUB_TOKEN=your_github_token
GITHUB_REPO_OWNER=your_owner
GITHUB_REPO_NAME=your_repo
GITHUB_WORKFLOW_FILE=your_workflow_file.yml
NETLIFY_AUTH_TOKEN=your_netlify_token
NETLIFY_SITE_ID=your_site_id
N8N_INSTANCE_ROLE=dev  # or 'prod' for Raspberry Pi
```

### Step 3: Validate Workflow Before Import

```bash
python3 scripts/validate-hybrid-workflow.py \
  /Users/rashadwest/Desktop/n8n-unity-build-orchestrator-PYTHON-HYBRID.json
```

This checks:
- ✅ JSON structure is valid
- ✅ All required nodes exist
- ✅ Python script paths are correct
- ✅ Environment variables are referenced
- ✅ Connections are valid

### Step 4: Import Workflow to n8n

1. Open n8n UI: `http://localhost:5678` (or your Pi IP)
2. Click **Workflows → Import from File**
3. Select: `/Users/rashadwest/Desktop/n8n-unity-build-orchestrator-PYTHON-HYBRID.json`
4. Click **Import**

### Step 5: Test the Workflow

**Option A: Manual Trigger (Recommended for First Test)**
1. Open the imported workflow
2. Click **Execute Workflow** button
3. Watch execution flow through nodes

**Option B: Webhook Trigger**
```bash
curl -X POST http://localhost:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

---

## 🔍 Verification Checklist

After setup, verify:

- [ ] Python scripts are executable: `ls -l scripts/n8n-check-*.py`
- [ ] Environment variables are set in n8n
- [ ] Workflow imports without errors
- [ ] Python scripts output valid JSON when run manually
- [ ] Workflow executes successfully (test with webhook)

---

## 🐛 Troubleshooting

### Python Script Not Found

**Error:** `python3: can't open file 'scripts/n8n-check-github.py'`

**Fix:**
1. Check `WORKFLOW_PATH` is set correctly in n8n
2. Verify path: `ls $WORKFLOW_PATH/scripts/n8n-check-github.py`
3. Update `WORKFLOW_PATH` if needed

### Invalid JSON Output

**Error:** `Failed to parse GitHub output`

**Fix:**
1. Test script manually: `python3 scripts/n8n-check-github.py`
2. Check credentials are set (GITHUB_TOKEN, etc.)
3. Verify script outputs valid JSON

### Workflow Import Fails

**Error:** Import validation errors

**Fix:**
1. Run validation script first: `python3 scripts/validate-hybrid-workflow.py workflow.json`
2. Fix any issues reported
3. Try importing again

---

## 📋 What's Different from Original Workflow

### Original (HTTP Request Nodes)
- Direct API calls from n8n
- Limited error handling
- Harder to debug

### Hybrid (Python Scripts)
- Python scripts handle API calls
- Better error handling (try/except)
- Structured JSON output
- Reusable outside n8n

### Workflow Structure
```
Original: HTTP Request → Finalize Report
Hybrid:   Execute Python → Parse JSON → Finalize Report
```

---

## 🚀 Next Steps

1. ✅ **Setup Complete** - You're ready to use the hybrid workflow
2. 📊 **Dashboard Integration** - See roadmap for future enhancements
3. 🔔 **Alerting** - Add Slack/email notifications (future)

---

## 📚 Additional Resources

- **Validation Script:** `scripts/validate-hybrid-workflow.py`
- **Environment Setup:** `setup-python-hybrid-env.sh`
- **Python Scripts:** `scripts/n8n-check-github.py`, `scripts/n8n-check-netlify.py`
- **Original Workflow:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`

---

**Setup Complete!** ✅  
Your hybrid workflow is ready to use.


