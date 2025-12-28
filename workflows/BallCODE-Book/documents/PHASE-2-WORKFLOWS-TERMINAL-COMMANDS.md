# 🖥️ Phase 2 Workflows - Terminal Commands Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Quick reference for all terminal commands to manage Phase 2 workflows

---

## ⚡ QUICK START

### 1. Setup Environment (One-Time)

```bash
# Setup n8n terminal environment
./setup-n8n-terminal.sh local    # For Mac (localhost)
./setup-n8n-terminal.sh pi       # For Raspberry Pi (LAN IP)

# Source environment
source .n8n-env
```

### 2. Configure Environment

Edit `.n8n-env`:
```bash
nano .n8n-env
```

**Required:**
```bash
export N8N_URL="http://localhost:5678"  # or your Pi IP
export N8N_API_KEY="your-api-key"       # Optional but recommended
```

---

## 📋 WORKFLOW MANAGEMENT COMMANDS

### Import Workflows to n8n

**Option 1: Via n8n UI (Easiest)**
1. Open n8n: `http://localhost:5678` (or your Pi IP)
2. Click "Workflows" → "Import from File"
3. Select workflow file:
   - `n8n-book-content-update-workflow.json`
   - `n8n-curriculum-sync-workflow.json`
   - `n8n-game-exercise-integration-workflow.json`

**Option 2: Via API (Terminal)**
```bash
# Import Book Content Update Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-book-content-update-workflow.json

# Import Curriculum Sync Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-curriculum-sync-workflow.json

# Import Game Exercise Integration Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-game-exercise-integration-workflow.json
```

### Deploy Workflows (Using Deploy Script)

```bash
# Deploy Book Content Update Workflow (new)
./deploy-n8n-workflow.sh n8n-book-content-update-workflow.json

# Deploy Curriculum Sync Workflow (new)
./deploy-n8n-workflow.sh n8n-curriculum-sync-workflow.json

# Deploy Game Exercise Integration Workflow (new)
./deploy-n8n-workflow.sh n8n-game-exercise-integration-workflow.json

# Update existing workflow (replace WORKFLOW_ID with actual ID)
./deploy-n8n-workflow.sh n8n-book-content-update-workflow.json WORKFLOW_ID
```

### List All Workflows

```bash
# List workflows via API
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | jq '.[] | {id, name, active}'

# Or use list script (if available)
./n8n-list-workflows.sh
```

### Get Workflow ID

```bash
# Get workflow by name
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("Book Content Update")) | .id'
```

---

## 🔍 VALIDATION & DEBUGGING

### Validate JSON

```bash
# Validate Book Content Update Workflow
python3 -m json.tool n8n-book-content-update-workflow.json > /dev/null && echo "✅ Valid"

# Validate Curriculum Sync Workflow
python3 -m json.tool n8n-curriculum-sync-workflow.json > /dev/null && echo "✅ Valid"

# Validate Game Exercise Integration Workflow
python3 -m json.tool n8n-game-exercise-integration-workflow.json > /dev/null && echo "✅ Valid"

# Validate all Phase 2 workflows
for file in n8n-book-content-update-workflow.json n8n-curriculum-sync-workflow.json n8n-game-exercise-integration-workflow.json; do
  echo "Validating $file..."
  python3 -m json.tool "$file" > /dev/null && echo "✅ $file is valid" || echo "❌ $file has errors"
done
```

### Debug Workflows

```bash
# Debug Book Content Update Workflow
python3 debug-workflow.py n8n-book-content-update-workflow.json

# Debug Curriculum Sync Workflow
python3 debug-workflow.py n8n-curriculum-sync-workflow.json

# Debug Game Exercise Integration Workflow
python3 debug-workflow.py n8n-game-exercise-integration-workflow.json
```

### Fix Workflow Issues

```bash
# Auto-fix Book Content Update Workflow
python3 fix-workflow-file.py n8n-book-content-update-workflow.json

# Auto-fix Curriculum Sync Workflow
python3 fix-workflow-file.py n8n-curriculum-sync-workflow.json

# Auto-fix Game Exercise Integration Workflow
python3 fix-workflow-file.py n8n-game-exercise-integration-workflow.json
```

---

## 🧪 TESTING WORKFLOWS

### Test Book Content Update Workflow

```bash
# Test webhook trigger
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{
    "bookId": 1,
    "content": {
      "title": "The Foundation Block",
      "slug": "the-foundation-block",
      "concepts": {"python": "Sequences"},
      "basketball": {"skill": "Pound Dribble"},
      "curriculum": {"gradeLevels": ["3-5", "6-8"]}
    },
    "updateType": "modify"
  }'
```

### Test Curriculum Sync Workflow

```bash
# Test webhook trigger
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "newObjective",
    "learningObjective": {
      "objective": "Understand sequences in Python",
      "gradeLevels": ["3-5"],
      "standards": ["CSTA-1B-AP-10"]
    }
  }'
```

### Test Game Exercise Integration Workflow

```bash
# Test webhook trigger
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "exercise-1-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "Sequences",
      "mode": "story"
    }
  }'
```

---

## 📊 WORKFLOW STATUS & MONITORING

### Check Workflow Status

```bash
# Get workflow status by ID
curl -X GET "$N8N_URL/api/v1/workflows/WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | jq '{name, active, nodes: (.nodes | length)}'

# List all active workflows
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.active == true) | {id, name, active}'
```

### Activate/Deactivate Workflow

```bash
# Activate workflow
curl -X POST "$N8N_URL/api/v1/workflows/WORKFLOW_ID/activate" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"

# Deactivate workflow
curl -X POST "$N8N_URL/api/v1/workflows/WORKFLOW_ID/deactivate" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

### Get Workflow Executions

```bash
# Get recent executions
curl -X GET "$N8N_URL/api/v1/executions" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.data[:5] | .[] | {id, finished, mode, stoppedAt}'
```

---

## 🔧 WORKFLOW EDITING

### Export Workflow from n8n

```bash
# Export workflow by ID
curl -X GET "$N8N_URL/api/v1/workflows/WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" > workflow-exported.json

# Export all workflows
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" > all-workflows-exported.json
```

### Update Workflow

```bash
# Update workflow via API
curl -X PUT "$N8N_URL/api/v1/workflows/WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-book-content-update-workflow.json

# Or use deploy script
./deploy-n8n-workflow.sh n8n-book-content-update-workflow.json WORKFLOW_ID
```

### Interactive Workflow Editor

```bash
# Open interactive editor for Book Content Update Workflow
./n8n-workflow-editor.sh n8n-book-content-update-workflow.json

# Open interactive editor for Curriculum Sync Workflow
./n8n-workflow-editor.sh n8n-curriculum-sync-workflow.json

# Open interactive editor for Game Exercise Integration Workflow
./n8n-workflow-editor.sh n8n-game-exercise-integration-workflow.json
```

---

## 🚀 QUICK COMMAND REFERENCE

### All-in-One Setup & Deploy

```bash
# 1. Setup environment
./setup-n8n-terminal.sh local
source .n8n-env

# 2. Validate all workflows
for file in n8n-book-content-update-workflow.json n8n-curriculum-sync-workflow.json n8n-game-exercise-integration-workflow.json; do
  python3 -m json.tool "$file" > /dev/null && echo "✅ $file" || echo "❌ $file"
done

# 3. Deploy all workflows
./deploy-n8n-workflow.sh n8n-book-content-update-workflow.json
./deploy-n8n-workflow.sh n8n-curriculum-sync-workflow.json
./deploy-n8n-workflow.sh n8n-game-exercise-integration-workflow.json

# 4. List deployed workflows
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("BallCODE")) | {id, name, active}'
```

### Test All Workflows

```bash
# Test Book Content Update
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'

# Test Curriculum Sync
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

# Test Game Exercise Integration
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 📝 ENVIRONMENT VARIABLES

### Required

```bash
export N8N_URL="http://localhost:5678"  # or your Pi IP
```

### Optional (Recommended)

```bash
export N8N_API_KEY="your-api-key"       # Get from n8n UI → Settings → API
export WORKFLOW_PATH="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
```

### Get API Key

1. Open n8n UI: `http://localhost:5678` (or your Pi IP)
2. Settings → API
3. Generate API Key
4. Add to `.n8n-env`:
   ```bash
   export N8N_API_KEY="your-generated-key"
   ```

---

## 🆘 TROUBLESHOOTING

### Connection Issues

```bash
# Test n8n connection
curl -s "$N8N_URL/healthz" || curl -s "$N8N_URL"

# Check if n8n is running
ps aux | grep n8n
```

### Workflow Import Errors

```bash
# Validate JSON before importing
python3 -m json.tool workflow.json

# Check for common issues
python3 debug-workflow.py workflow.json

# Auto-fix issues
python3 fix-workflow-file.py workflow.json
```

### API Key Issues

```bash
# Test API key
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"

# If fails, regenerate API key in n8n UI
```

---

## 📚 RELATED DOCUMENTATION

- **Complete Workflow Guide:** `documents/PHASE-2-WORKFLOWS-COMPLETE.md`
- **Integration Plan:** `N8N-BALLCODE-INTEGRATION-PLAN-EXPANDED.md`
- **Terminal Editing Guide:** `N8N-TERMINAL-QUICK-START.md`
- **Setup Script:** `setup-n8n-terminal.sh`

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use



