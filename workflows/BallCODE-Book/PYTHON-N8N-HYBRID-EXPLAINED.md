# 🐍 Python + n8n Hybrid Integration - Complete Explanation

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 17, 2025  
**Purpose:** Explain how Python scripts integrate with n8n workflows  
**Status:** ✅ Complete Guide

---

## 🎯 KEY CONCEPT

**You don't "push code" into n8n. Instead:**
- **n8n workflows are JSON files** (not code)
- **Python scripts run FROM n8n** via "Execute Command" nodes
- **This is called "Hybrid Integration"** - n8n orchestrates, Python executes

---

## 📋 HOW IT WORKS (Step-by-Step)

### **The Process:**

```
1. You trigger n8n workflow (via webhook)
   ↓
2. n8n workflow runs through nodes
   ↓
3. When it hits "Execute Command" node → Runs Python script
   ↓
4. Python script does the work (updates files, processes data)
   ↓
5. Python script returns JSON output
   ↓
6. n8n workflow continues with Python's output
   ↓
7. Workflow completes and responds
```

---

## 🔧 HOW TO UPDATE WORKFLOWS

### **You DON'T Push Code - You Import JSON Files**

**n8n workflows are JSON files, not code. To update a workflow:**

#### **Method 1: Import via n8n UI** (Recommended)
1. Edit the JSON file locally (e.g., `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`)
2. Open n8n UI: `http://192.168.1.226:5678`
3. Click "Workflows" → "Import from File"
4. Select your updated JSON file
5. Click "Import"
6. Workflow is updated!

#### **Method 2: Import via API** (What we've been doing)
```bash
# Push workflow via API
./scripts/push-orchestrator-fixed-v3.sh
```

**What this does:**
- Reads JSON file
- Sends it to n8n API
- n8n creates/updates workflow

---

## 🐍 PYTHON HYBRID INTEGRATION - HOW IT WORKS

### **Why Python + n8n?**

**Problem:** n8n's Code nodes run in a sandbox (VM2) that has limitations:
- ❌ Can't access file system directly
- ❌ Can't use `fs.readFileSync()` 
- ❌ Limited to JavaScript only
- ❌ Can't run complex operations

**Solution:** Use Python scripts via "Execute Command" nodes:
- ✅ Python can access file system
- ✅ Python can do complex logic
- ✅ Python scripts are reusable
- ✅ Better error handling

---

## 📊 EXAMPLE: How Python Integrates

### **Example Workflow Structure:**

```
Webhook Trigger
    ↓
Normalize Input
    ↓
Execute Python: Update Schema (HYBRID)  ← This runs Python script
    ↓
Parse Python Output
    ↓
Continue workflow...
```

### **The "Execute Command" Node:**

**In the workflow JSON:**
```json
{
  "name": "Execute Python: Update Schema (HYBRID)",
  "type": "n8n-nodes-base.executeCommand",
  "parameters": {
    "command": "python3",
    "arguments": "{{ $env.WORKFLOW_PATH }}/scripts/n8n-update-schema.py --type book --id {{ $json.bookId }} --data '{{ JSON.stringify($json.bookData) }}'"
  }
}
```

**What happens:**
1. n8n runs: `python3 /path/to/scripts/n8n-update-schema.py --type book --id 1 --data '{"title":"New"}'`
2. Python script executes
3. Python script updates files
4. Python script outputs JSON: `{"status": "success", "updated": true}`
5. n8n captures the output
6. Next node parses the JSON and continues

---

## 🔄 THE COMPLETE FLOW

### **Real Example: Book Content Update**

**1. You send webhook:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/book-update \
  -d '{"bookId": 1, "title": "New Title"}'
```

**2. n8n workflow receives it:**
- Webhook Trigger node receives request
- Normalize Input node processes it
- Validation node checks data

**3. Python script runs:**
- Execute Command node runs: `python3 scripts/n8n-update-schema.py --type book --id 1 --data '{"title":"New Title"}'`
- Python script:
  - Reads `CURRICULUM-DATA-EXAMPLE.json`
  - Updates book 1 with new title
  - Saves file
  - Returns: `{"status": "success", "bookId": 1, "updated": true}`

**4. n8n continues:**
- Parse Python Output node gets the JSON
- Next nodes use the result
- Workflow completes
- Returns response to you

---

## 📝 PYTHON SCRIPTS USED

### **1. `scripts/n8n-update-schema.py`**

**Purpose:** Updates unified curriculum schema

**Used by:**
- Full Integration Workflow
- Book Content Update Workflow
- Curriculum Schema Sync Workflow
- Game Exercise Integration Workflow

**How it's called:**
```bash
python3 scripts/n8n-update-schema.py \
  --type book \
  --id 1 \
  --data '{"title": "New Title"}'
```

**What it does:**
1. Reads curriculum schema file
2. Updates the specified book/curriculum/exercise
3. Saves updated file
4. Returns JSON result

---

### **2. `screenshot_fix_processor.py`**

**Purpose:** Processes screenshot analysis and applies fixes

**Used by:**
- Screenshot to Fix Workflow

**How it's called:**
- Automatically by workflow when screenshot is analyzed

**What it does:**
1. Analyzes screenshot with GPT-4 Vision
2. Identifies error
3. Attempts to fix (if possible)
4. Returns fix result

---

## 🚀 HOW TO UPDATE WORKFLOWS

### **To Update a Workflow:**

**Step 1: Edit the JSON file**
```bash
# Edit the workflow JSON file
nano n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json
```

**Step 2: Import it**
```bash
# Option A: Via UI (recommended)
# Open n8n UI → Workflows → Import from File

# Option B: Via API
./scripts/push-orchestrator-fixed-v3.sh
```

**Step 3: Activate it**
- Open workflow in n8n UI
- Toggle "Active" switch ON

---

## 🔧 HOW TO UPDATE PYTHON SCRIPTS

### **Python Scripts Are Separate Files**

**To update a Python script:**
1. Edit the Python file directly:
   ```bash
   nano scripts/n8n-update-schema.py
   ```
2. Save the file
3. **No need to update n8n workflow** - it will use the updated script automatically!

**Why this works:**
- n8n workflow calls: `python3 scripts/n8n-update-schema.py`
- It runs whatever version of the script exists
- Update the script = workflow uses new version automatically

---

## 📊 COMPARISON: Code vs JSON

### **What You CAN'T Do:**
- ❌ Push Python code directly into n8n
- ❌ Write code in n8n UI (only JavaScript in Code nodes)
- ❌ Update Python scripts from n8n UI

### **What You CAN Do:**
- ✅ Import JSON workflow files into n8n
- ✅ Edit Python scripts separately
- ✅ n8n calls Python scripts via Execute Command nodes
- ✅ Python scripts work independently (can run standalone)

---

## 🎯 THE HYBRID APPROACH BENEFITS

### **Why Python + n8n?**

1. **n8n is Great For:**
   - ✅ Orchestration (connecting steps)
   - ✅ Webhooks (receiving requests)
   - ✅ API calls (GitHub, Netlify, OpenAI)
   - ✅ Visual workflow design

2. **Python is Great For:**
   - ✅ File system operations
   - ✅ Complex data processing
   - ✅ JSON manipulation
   - ✅ Reusable scripts

3. **Together:**
   - ✅ n8n orchestrates the flow
   - ✅ Python does the heavy lifting
   - ✅ Best of both worlds!

---

## 📋 QUICK REFERENCE

### **Update Workflow:**
```bash
# Edit JSON file, then:
./scripts/push-orchestrator-fixed-v3.sh
# OR import via UI
```

### **Update Python Script:**
```bash
# Just edit the Python file:
nano scripts/n8n-update-schema.py
# Save - workflow uses it automatically!
```

### **Test Python Script Standalone:**
```bash
python3 scripts/n8n-update-schema.py --type book --id 1 --data '{"title":"Test"}'
```

### **Test Workflow:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

---

## 🔍 WHERE TO FIND EXAMPLES

### **Workflow with Python Integration:**
- `n8n-game-exercise-integration-workflow.json` - Line 56 shows Execute Command node
- `n8n-book-content-update-workflow.json` - Has Python hybrid nodes
- `n8n-curriculum-sync-workflow.json` - Uses Python for schema updates

### **Python Scripts:**
- `scripts/n8n-update-schema.py` - Main schema updater
- `screenshot_fix_processor.py` - Screenshot analysis

---

## 💡 KEY TAKEAWAYS

1. **n8n workflows = JSON files** (not code)
2. **You import JSON files** (not push code)
3. **Python scripts run FROM n8n** (via Execute Command nodes)
4. **Update Python scripts separately** (workflow uses them automatically)
5. **Hybrid approach** = n8n orchestrates, Python executes

---

**Status:** Complete explanation  
**Next:** Try updating a Python script and see it work automatically!


