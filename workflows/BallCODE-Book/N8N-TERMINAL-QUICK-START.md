# 🚀 n8n Terminal Editing - Quick Start

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Status:** ✅ Ready to Use  
**Time to Setup:** 2 minutes

---

## ⚡ Quick Setup (2 Minutes)

### Step 1: Run Setup Script

```bash
./setup-n8n-terminal.sh
```

This will:
- ✅ Create `.n8n-env` configuration file
- ✅ Make all scripts executable
- ✅ Check Python dependencies
- ✅ Test n8n connection

### Step 2: Configure Environment

Edit `.n8n-env`:

```bash
nano .n8n-env
```

**Required:**
- `N8N_URL` - Your n8n instance URL (e.g., `http://localhost:5678` or `http://your-pi-ip:5678`)

**Optional:**
- `N8N_API_KEY` - Get from n8n UI → Settings → API → Generate API Key
- `WORKFLOW_FILE` - Default workflow file to work with
- `WORKFLOW_ID` - For updating existing workflows

### Step 3: Source Environment

```bash
source .n8n-env
```

Or add to your shell profile:
```bash
echo "source $(pwd)/.n8n-env" >> ~/.zshrc
```

---

## 🎯 Common Workflows

### Edit Workflow in Cursor

1. **Tell me what to change:**
   ```
   "Add error handling to the GitHub Actions trigger node"
   ```

2. **I edit the workflow:**
   - Read workflow JSON
   - Apply changes
   - Fix issues
   - Validate JSON
   - Save file

3. **You debug (terminal):**
   ```bash
   python3 debug-workflow.py n8n-unity-automation-workflow.json
   ```

4. **You deploy (terminal):**
   ```bash
   ./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json [workflow-id]
   ```

**Done!** ✅

---

## 🛠️ Available Tools

### Interactive Menu (Recommended)

```bash
./n8n-workflow-editor.sh n8n-unity-automation-workflow.json
```

**Menu Options:**
1. Debug workflow (check for issues)
2. Fix workflow (auto-fix common issues)
3. Validate JSON
4. Deploy to n8n (create/update)
5. Export from n8n (download current)
6. Compare workflows (diff)
7. Show workflow info
8. Full workflow check (debug + fix + validate)

### Individual Commands

**Debug Workflow:**
```bash
python3 debug-workflow.py workflow.json
```

**Fix Workflow:**
```bash
python3 fix-workflow-file.py workflow.json workflow.json.fixed
```

**Validate JSON:**
```bash
python3 -m json.tool workflow.json
```

**Deploy Workflow (New):**
```bash
./deploy-n8n-workflow.sh workflow.json
```

**Deploy Workflow (Update):**
```bash
./deploy-n8n-workflow.sh workflow.json WORKFLOW_ID
```

**Update via Python:**
```bash
export WORKFLOW_FILE="workflow.json"
export WORKFLOW_ID="abc123"  # Optional for updates
python3 update-workflow.py
```

**Test Webhook:**
```bash
curl -X POST "$N8N_URL/webhook/unity-dev" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test"}'
```

---

## 📋 Workflow Editing Process

```
1. You: "Update workflow to add X"
   ↓
2. Me: Edit workflow.json in Cursor
   - Apply changes
   - Fix issues
   - Validate
   ↓
3. You: Run debug script (terminal)
   python3 debug-workflow.py workflow.json
   ↓
4. You: Deploy (terminal)
   ./deploy-n8n-workflow.sh workflow.json [id]
   ↓
5. Done! ✅
```

**No n8n UI needed after initial setup!**

---

## 🔧 Configuration

### Environment Variables

**`.n8n-env` file:**
```bash
export N8N_URL="http://localhost:5678"
export N8N_API_KEY="your-api-key"  # Optional
export WORKFLOW_FILE="n8n-unity-automation-workflow.json"
export WORKFLOW_ID=""  # For updates
```

### Get n8n API Key (One-Time)

1. Open n8n UI: `http://your-n8n-instance:5678`
2. Settings → API
3. Generate API Key
4. Add to `.n8n-env`:
   ```bash
   export N8N_API_KEY="your-generated-key"
   ```

---

## ✅ Verification

**Check if everything works:**

```bash
# 1. Source environment
source .n8n-env

# 2. Test connection
curl -s "$N8N_URL/healthz" || curl -s "$N8N_URL"

# 3. Test debug script
python3 debug-workflow.py n8n-unity-automation-workflow.json

# 4. Test interactive editor
./n8n-workflow-editor.sh n8n-unity-automation-workflow.json
```

---

## 📖 Full Documentation

- **`N8N-CURSOR-EDITING-SYSTEM.md`** - Complete editing system guide
- **`N8N_WORKFLOW_DEVELOPMENT_GUIDE.md`** - Development best practices
- **`N8N-FINAL-WORKING-SETUP.md`** - Working setup reference

---

## 🎯 What You Can Do

**100% Terminal-Based:**
- ✅ Edit workflow JSON in Cursor
- ✅ Debug workflow (terminal)
- ✅ Fix workflow (terminal)
- ✅ Validate workflow (terminal)
- ✅ Deploy workflow (terminal)
- ✅ Export workflow (terminal)
- ✅ Test workflow (terminal via webhook)

**One-Time UI Setup:**
- ⚠️ Set credentials (OpenAI, GitHub, Netlify)
- ⚠️ Get API key (optional)
- ⚠️ Initial workflow verification

**After setup: 100% terminal-based!**

---

**Status:** ✅ Ready to Use  
**Next:** Run `./setup-n8n-terminal.sh` to get started!




