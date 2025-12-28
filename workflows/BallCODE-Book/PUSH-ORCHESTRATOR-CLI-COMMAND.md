# 🚀 Push Orchestrator CLI Command - Quick Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Status:** ✅ Ready to Use

---

## ⚡ QUICK COMMAND

**Run this to push the orchestrator workflow:**

```bash
./scripts/push-orchestrator-cli-v2.sh
```

**Or from project root:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/push-orchestrator-cli-v2.sh
```

---

## 📋 WHAT IT DOES

1. **Deletes all existing orchestrator workflows** (removes conflicts)
2. **Cleans the workflow file** (removes problematic properties)
3. **Imports via API** (proven to work)
4. **Verifies success** (checks node count)

---

## 🔍 FILE LOCATION

**Script:** `scripts/push-orchestrator-cli-v2.sh`

**Full Path:**
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/push-orchestrator-cli-v2.sh
```

---

## ✅ VERIFY IT EXISTS

**Check if script exists:**
```bash
ls -la scripts/push-orchestrator-cli-v2.sh
```

**Should show:**
```
-rwxr-xr-x  ... scripts/push-orchestrator-cli-v2.sh
```

---

## 🚀 USAGE

### Step 1: Navigate to Project
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

### Step 2: Run Script
```bash
./scripts/push-orchestrator-cli-v2.sh
```

### Step 3: Check Output
- Should show: "✅ SUCCESS! Workflow imported"
- Will give you workflow ID
- Will verify 13 nodes

---

## 📝 ALTERNATIVE: Direct Command

**If script doesn't work, run commands directly:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi

# Clean workflow
python3 scripts/clean-workflow-for-api-v2.py \
  n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json \
  n8n-unity-build-orchestrator-API-READY-V2.json

# Import via API
curl -X POST "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-unity-build-orchestrator-API-READY-V2.json
```

---

## 🎯 EXPECTED OUTPUT

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 Push Orchestrator Workflow via CLI - V2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Cleaning up existing orchestrator workflows...
Found X orchestrator workflows to delete
✅ Deleted X workflows

Step 2: Cleaning workflow for API import (V2)...
✅ Cleaned workflow ready (13 nodes)

Step 3: Importing workflow via API...
✅ SUCCESS! Workflow imported
   ID: [workflow-id]
   Name: AIMCODE (Demis) - Unity Build Orchestrator (13 nodes, MAC GUARDED)

✅ Verified: Imported workflow has 13 nodes
```

---

## 🔧 TROUBLESHOOTING

### Script Not Found:
```bash
# Check if it exists
ls scripts/push-orchestrator-cli-v2.sh

# If not found, check scripts directory
ls scripts/*.sh | grep orchestrator
```

### Permission Denied:
```bash
chmod +x scripts/push-orchestrator-cli-v2.sh
```

### API Key Not Set:
```bash
# Check if API key is set
source .n8n-env.pi
echo $N8N_API_KEY
```

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** ✅ Ready to Use


