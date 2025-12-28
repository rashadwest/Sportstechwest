# n8n Remote Building - Quick Start Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Answer:** ✅ **YES - You CAN build n8n remotely using Claude + Cursor!**

---

## 🚀 Quick Answer

**Question:** Can we use a mixture of Claude and the Cursor integration to build n8n remotely?

**Answer:** **YES!** You can build n8n workflows remotely using:
1. **Claude** (in Cursor) to modify workflow JSON files
2. **n8n REST API** to deploy workflows programmatically
3. **Python/Bash scripts** to automate deployment

**You do NOT need to do it manually!**

---

## ⚡ 3-Step Process

### Step 1: Claude Modifies Workflow (in Cursor)
```
You: "Update the n8n workflow to add error handling"

Claude: 
- Reads n8n-unity-automation-workflow.json
- Modifies JSON structure
- Adds error handling nodes
- Validates JSON
```

### Step 2: Deploy via Script
```bash
./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json
```

### Step 3: Verify (One-Time)
```
Open n8n UI → Check workflow → Test → Done!
```

---

## 📋 Setup (One-Time)

### 1. Configure Environment

Create `.n8n-env` file:
```bash
export N8N_URL="http://your-raspberry-pi-ip:5678"
export N8N_API_KEY="your-api-key-here"
```

### 2. Get n8n API Key

1. Open n8n: `http://your-pi-ip:5678`
2. Go to Settings → API
3. Generate API key
4. Save to `.n8n-env`

### 3. Test Connection
```bash
source .n8n-env
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

---

## 🎯 Usage Examples

### Example 1: Create New Workflow

**In Cursor, ask Claude:**
```
"Create a new n8n workflow that runs daily at 2 AM and sends a status report"
```

**Claude creates:** `new-status-workflow.json`

**Deploy:**
```bash
./deploy-n8n-workflow.sh new-status-workflow.json
```

### Example 2: Update Existing Workflow

**In Cursor, ask Claude:**
```
"Add retry logic to the Unity automation workflow for GitHub Actions failures"
```

**Claude modifies:** `n8n-unity-automation-workflow.json`

**Deploy:**
```bash
# Get workflow ID from n8n UI first
./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json abc123
```

### Example 3: Bulk Updates

**In Cursor, ask Claude:**
```
"Update all workflows to add error notifications to Discord"
```

**Claude modifies:** All workflow JSON files

**Deploy:**
```bash
for workflow in *.json; do
  ./deploy-n8n-workflow.sh "$workflow"
done
```

---

## 🔧 Available Tools

### 1. Deployment Script
**File:** `deploy-n8n-workflow.sh`
- Deploys workflows via n8n API
- Validates JSON before deployment
- Handles create/update operations

### 2. Validation Script
**File:** `validate-workflow.py` (from N8N_WORKFLOW_DEVELOPMENT_GUIDE.md)
- Validates JSON structure
- Checks for placeholder values
- Verifies node connections

### 3. Update Script
**File:** `update-workflow.py` (from N8N_WORKFLOW_DEVELOPMENT_GUIDE.md)
- Updates existing workflows
- Preserves workflow settings
- Handles API authentication

---

## 📚 Full Documentation

For complete analysis and detailed steps, see:
- **`AIMCODE-N8N-REMOTE-BUILD-ANALYSIS.md`** - Complete AIMCODE analysis
- **`N8N_WORKFLOW_DEVELOPMENT_GUIDE.md`** - n8n development guide
- **`PHASE-3-N8N-WORKFLOW-BUILD.md`** - Manual build guide (for reference)

---

## ✅ Benefits of Remote Building

| Benefit | Description |
|---------|-------------|
| ⚡ **Speed** | Deploy in seconds vs minutes |
| 🔄 **Version Control** | Workflow JSON in git |
| 🤖 **Automation** | Fully automated deployment |
| 📝 **Repeatability** | Same process every time |
| 🔍 **Validation** | JSON validation before deployment |

---

## ⚠️ Important Notes

1. **Initial Setup:** One-time manual verification recommended
2. **API Access:** Requires n8n API key or basic auth
3. **Network Access:** Must be able to reach Raspberry Pi n8n instance
4. **Validation:** Always validate JSON before deployment

---

## 🎯 Recommended Workflow

```
┌─────────────────────────────────────┐
│ 1. Claude modifies workflow.json   │
│    (in Cursor)                      │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. Validate JSON                   │
│    (automatic in script)            │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. Deploy via API                  │
│    (./deploy-n8n-workflow.sh)       │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. Verify in n8n UI                │
│    (one-time or when needed)        │
└─────────────────────────────────────┘
```

---

## 🚨 Troubleshooting

### Error: "Invalid JSON"
```bash
# Validate JSON manually
python3 -m json.tool workflow.json
```

### Error: "Authentication failed"
```bash
# Check API key
echo $N8N_API_KEY

# Test connection
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

### Error: "Workflow not found"
```bash
# List all workflows
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | jq '.[].id'
```

---

## ✅ Summary

**Can you build n8n remotely?** ✅ **YES!**

**How?**
1. Claude modifies workflow JSON (in Cursor)
2. Deploy via `deploy-n8n-workflow.sh` script
3. Verify in n8n UI (one-time)

**Best Approach:** Hybrid (Remote building + Manual verification)

**Ready to use:** ✅ Scripts created, documentation complete

---

**Copyright © 2025 Rashad West. All Rights Reserved.**




