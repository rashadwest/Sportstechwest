# 📝 OpenAI Node Configurations & Webhook Commands

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Purpose:** Complete reference for all OpenAI node configurations and quick webhook terminal commands

---

## 🎯 WORKFLOW 1: BallCODE Curriculum Schema Sync Workflow

**Webhook Path:** `curriculum-sync`  
**Webhook URL:** `http://192.168.1.226:5678/webhook/curriculum-sync`

### Node 1: "Update Game Exercise Configurations (AI)"

**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Temperature:** `0.2`  
**Max Tokens:** `3000`

**System Message:**
```
You are a Unity game development expert. Update game exercise configurations to match curriculum schema changes. Ensure game exercises align with learning objectives and curriculum standards.
```

**User Message:**
```
Curriculum Schema: {{ JSON.stringify($json.curriculumSchema) }}

Change Type: {{ $json.changeType }}

Learning Objective: {{ JSON.stringify($json.learningObjective) }}

Standards: {{ JSON.stringify($json.standards) }}

Update game exercise configurations:
1. Update exercise difficulty levels to match curriculum
2. Update exercise descriptions to match learning objectives
3. Update exercise success criteria
4. Ensure exercises align with curriculum standards
5. Update exercise progression paths

Return JSON with:
- exerciseConfigs: [{ exerciseId, difficulty, description, successCriteria, standards }]
- levelFiles: [{ file: string, json: object }]
- progressionPaths: [{ fromExercise: string, toExercise: string, requirements: [] }]

Format as valid JSON only.
```

---

### Node 2: "Update Book Learning Sections (AI)"

**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Temperature:** `0.3`  
**Max Tokens:** `3000`

**System Message:**
```
You are a children's book author and educational content creator. Update book learning sections to match curriculum schema changes. Ensure book content reflects updated learning objectives and curriculum standards.
```

**User Message:**
```
Curriculum Schema: {{ JSON.stringify($json.curriculumSchema) }}

Change Type: {{ $json.changeType }}

Learning Objective: {{ JSON.stringify($json.learningObjective) }}

Standards: {{ JSON.stringify($json.standards) }}

Update book learning sections:
1. Update 'What You're Learning' sections
2. Update learning objectives display
3. Update curriculum connection sections
4. Update assessment criteria
5. Ensure book content matches curriculum standards

Return JSON with:
- bookUpdates: [{ bookId, learningSection: {}, curriculumConnection: {} }]
- learningObjectives: [{ objective: string, gradeLevels: [], standards: [] }]
- assessmentCriteria: [{ criterion: string, description: string }]

Format as valid JSON only.
```

---

### Node 3: "Update Website Curriculum Display (AI)"

**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Temperature:** `0.2`  
**Max Tokens:** `3000`

**System Message:**
```
You are a web developer and UX designer. Update website curriculum pathways to reflect curriculum schema changes. Ensure website displays updated learning objectives, standards, and progression paths.
```

**User Message:**
```
Curriculum Schema: {{ JSON.stringify($json.curriculumSchema) }}

Change Type: {{ $json.changeType }}

Learning Objective: {{ JSON.stringify($json.learningObjective) }}

Standards: {{ JSON.stringify($json.standards) }}

Update website curriculum display:
1. Update curriculum pathway pages
2. Update learning objectives display
3. Update standards indicators
4. Update progression visualizations
5. Update grade level filters

Return JSON with:
- htmlFiles: [{ path: string, content: string }]
- curriculumPathway: { html: string, css: string, js: string }
- learningObjectivesDisplay: { html: string, data: [] }
- standardsDisplay: { html: string, data: [] }

Format as valid JSON only.
```

---

## 🎯 WORKFLOW 2: BallCODE Game Exercise Integration Workflow

**Webhook Path:** `game-exercise-integration`  
**Webhook URL:** `http://192.168.1.226:5678/webhook/game-exercise-integration`

### Node 1: "Update Curriculum Schema (AI)"

**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Temperature:** `0.2`  
**Max Tokens:** `3000`

**System Message:**
```
You are a curriculum design expert. Update the curriculum schema with new exercise information, ensuring exercises align with learning objectives and curriculum standards.
```

**User Message:**
```
Exercise Entry: {{ JSON.stringify($json.exerciseEntry) }}

Book: {{ JSON.stringify($json.book) }}

Curriculum Schema: {{ JSON.stringify($json.curriculumSchema) }}

Update curriculum schema:
1. Add exercise to curriculum progression paths
2. Update learning objectives if needed
3. Update curriculum standards alignment
4. Update assessment criteria
5. Ensure exercise fits curriculum progression

Return updated curriculum schema JSON matching CURRICULUM-DATA-EXAMPLE.json structure.

Format as valid JSON only.
```

---

### Node 2: "Update Website with Exercise Link (AI)"

**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Temperature:** `0.2`  
**Max Tokens:** `3000`

**System Message:**
```
You are a web developer. Generate website updates to add exercise button/link to book pages and update exercise listings.
```

**User Message:**
```
Exercise Entry: {{ JSON.stringify($json.exerciseEntry) }}

Book: {{ JSON.stringify($json.book) }}

Update website:
1. Add exercise button to book page
2. Update exercise listing page
3. Add exercise to book's exercise section
4. Update return flow (game → book)
5. Test exercise accessibility

Return JSON with:
- htmlFiles: [{ path: string, content: string }]
- exerciseButton: { html: string, css: string, js: string }
- exerciseLink: { text: string, url: string, description: string }
- returnFlow: { enabled: boolean, returnUrl: string }

Format as valid JSON only.
```

---

## 🚀 QUICK TERMINAL COMMANDS FOR ALL WEBHOOKS

### Pi n8n Base URL
```bash
N8N_URL="http://192.168.1.226:5678"
```

---

### 1. Unity Build Orchestrator

**Webhook:** `/webhook/unity-build`

**Quick Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request":"Test build","branch":"main"}'
```

**Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request":"Test build","branch":"main"}'
```

---

### 2. BallCODE Full Integration (Simplified)

**Webhook:** `/webhook/ballcode-dev`

**Quick Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Test AI analysis","mode":"quick","context":{}}'
```

**Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Test AI analysis","mode":"quick","context":{}}'
```

---

### 3. Screenshot to Fix

**Webhook:** `/webhook/screenshot-fix`

**Quick Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://example.com/error.png","context":"n8n workflow error"}'
```

**Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://example.com/error.png","context":"n8n workflow error"}'
```

---

### 4. Curriculum Schema Sync

**Webhook:** `/webhook/curriculum-sync`

**Quick Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "modify",
    "schemaChanges": {},
    "learningObjective": null,
    "standards": {}
  }'
```

**Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "modify",
    "schemaChanges": {},
    "learningObjective": null,
    "standards": {}
  }'
```

---

### 5. Game Exercise Integration

**Webhook:** `/webhook/game-exercise-integration`

**Quick Command:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "test-exercise-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "loops"
    }
  }'
```

**Test URL:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "test-exercise-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "loops"
    }
  }'
```

---

## 📋 ALL WEBHOOKS AT ONCE (Bash Script)

**Run all webhooks:**
```bash
#!/bin/bash
N8N_URL="http://192.168.1.226:5678"

echo "Testing Unity Build..."
curl -s -X POST "${N8N_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request":"Test","branch":"main"}' | head -c 100

echo -e "\n\nTesting Full Integration..."
curl -s -X POST "${N8N_URL}/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Test","mode":"quick"}' | head -c 100

echo -e "\n\nTesting Screenshot Fix..."
curl -s -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"test","context":"test"}' | head -c 100

echo -e "\n\nTesting Curriculum Sync..."
curl -s -X POST "${N8N_URL}/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType":"modify"}' | head -c 100

echo -e "\n\nTesting Exercise Integration..."
curl -s -X POST "${N8N_URL}/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType":"new","exerciseData":{"exerciseId":"test","bookId":1}}' | head -c 100

echo -e "\n\n✅ All webhooks tested"
```

---

## 🔑 CREDENTIALS REQUIRED

All OpenAI nodes require:
- **OpenAI API Key** (configured in n8n as "OpenAI API" credential)

**To add credentials:**
1. Open n8n UI: `http://192.168.1.226:5678`
2. Go to **Credentials** → **Add Credential**
3. Select **OpenAI API**
4. Enter your OpenAI API key
5. Save as "OpenAI API"

---

## 📝 NOTES

- **Production URLs** (`/webhook/...`) require workflows to be **Active**
- **Test URLs** (`/webhook-test/...`) work even when workflows are inactive
- All webhooks use **POST** method
- All requests require **Content-Type: application/json** header
- Pi n8n URL: `http://192.168.1.226:5678` (default)
- Mac n8n URL: `http://localhost:5678` (only when explicitly requested)

---

**Last Updated:** December 16, 2025



