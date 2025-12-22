# 🚀 Execute Phase 2 Workflows - Command Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Quick commands to execute/trigger Phase 2 workflows

---

## ⚡ QUICK EXECUTE COMMANDS

### Setup Environment First

```bash
# Source environment (if not already done)
source .n8n-env

# Or set manually
export N8N_URL="http://localhost:5678"  # or your Pi IP
```

---

## 📋 EXECUTE WORKFLOWS

### 1. Execute Book Content Update Workflow

```bash
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

**Minimal version:**
```bash
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test Book"}, "updateType": "modify"}'
```

---

### 2. Execute Curriculum Sync Workflow

```bash
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "newObjective",
    "learningObjective": {
      "objective": "Understand sequences in Python",
      "gradeLevels": ["3-5"],
      "standards": ["CSTA-1B-AP-10"]
    },
    "standards": {
      "csta": ["1B-AP-10"],
      "commonCore": ["MP.2"]
    }
  }'
```

**Minimal version:**
```bash
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'
```

---

### 3. Execute Game Exercise Integration Workflow

```bash
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "exercise-1-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "Sequences",
      "mode": "story",
      "description": "Foundation block exercise"
    }
  }'
```

**Minimal version:**
```bash
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 🎯 ONE-LINER COMMANDS (Copy & Paste)

### Book Content Update
```bash
curl -X POST "http://localhost:5678/webhook/book-content-update" -H "Content-Type: application/json" -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'
```

### Curriculum Sync
```bash
curl -X POST "http://localhost:5678/webhook/curriculum-sync" -H "Content-Type: application/json" -d '{"changeType": "modify"}'
```

### Game Exercise Integration
```bash
curl -X POST "http://localhost:5678/webhook/game-exercise-integration" -H "Content-Type: application/json" -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 🔧 EXECUTE VIA API (Alternative Method)

If you have the workflow ID, you can also execute via API:

```bash
# Execute workflow by ID
curl -X POST "$N8N_URL/api/v1/workflows/WORKFLOW_ID/execute" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data": {"bookId": 1}}'
```

**Get workflow ID:**
```bash
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("Book Content Update")) | .id'
```

---

## 📝 SAVE AS SCRIPTS

### Create execute scripts

**`execute-book-update.sh`:**
```bash
#!/bin/bash
source .n8n-env
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'
```

**`execute-curriculum-sync.sh`:**
```bash
#!/bin/bash
source .n8n-env
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'
```

**`execute-exercise-integration.sh`:**
```bash
#!/bin/bash
source .n8n-env
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

**Make executable:**
```bash
chmod +x execute-book-update.sh
chmod +x execute-curriculum-sync.sh
chmod +x execute-exercise-integration.sh
```

**Then run:**
```bash
./execute-book-update.sh
./execute-curriculum-sync.sh
./execute-exercise-integration.sh
```

---

## 🧪 TEST ALL WORKFLOWS

```bash
# Test all three workflows in sequence
echo "Testing Book Content Update..."
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'

echo -e "\nTesting Curriculum Sync..."
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

echo -e "\nTesting Game Exercise Integration..."
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 📊 CHECK EXECUTION RESULTS

```bash
# Get recent executions
curl -X GET "$N8N_URL/api/v1/executions" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.data[:5] | .[] | {id, finished, mode, stoppedAt, workflowId}'
```

---

## 🆘 TROUBLESHOOTING

### Workflow not found
```bash
# Check if workflow is active
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("Book Content")) | {id, name, active}'
```

### Webhook not responding
```bash
# Test webhook endpoint
curl -v -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"test": true}'
```

### Check workflow logs
```bash
# View workflow execution logs in n8n UI
# Go to: http://localhost:5678/workflows/WORKFLOW_ID/executions
```

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use


