# BallCODE Full Integration n8n Workflow Guide
## Complete System Integration Using AIMCODE + Demis Hassabis Methodology

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 10, 2025  
**File:** `n8n-ballcode-full-integration-workflow.json`  
**Status:** ✅ Ready for Deployment

---

## 🎯 PURPOSE

This n8n workflow provides **complete BallCODE system integration** - when you type a development prompt, it automatically:

1. ✅ **Analyzes the prompt** using AIMCODE methodology (Demis Hassabis - Alpha Evolve)
2. ✅ **Updates all 4 systems** (Game, Curriculum, Book, Website) in one go
3. ✅ **Uses unified curriculum schema** as single source of truth
4. ✅ **Integrates unified prompting system** (--quick and --full questions)
5. ✅ **Saves memory context** for book/lesson/website updates
6. ✅ **Ensures seamless integration** across all systems

---

## 🚀 HOW IT WORKS

### Workflow Flow:

```
1. Webhook Trigger (Development Prompt)
   ↓
2. Normalize Input & Extract Prompt
   ↓
3. AI Analyze Prompt (AIMCODE + Demis Hassabis)
   - Applies Alpha Evolve layered approach
   - Identifies systems affected
   - Creates comprehensive action plan
   ↓
4. Parse Action Plan
   ↓
5. Load Unified Curriculum Schema
   ↓
6. Parallel System Updates:
   - Generate Game Updates (if needed)
   - Generate Curriculum Updates (if needed)
   - Generate Book Updates (if needed)
   - Generate Website Updates (if needed)
   ↓
7. Merge All System Updates
   ↓
8. Prepare Memory Context for Saving
   ↓
9. Save Memory Context to File
   ↓
10. Finalize Integration Report
   ↓
11. Webhook Response (Complete report)
```

---

## 📋 WORKFLOW FEATURES

### 1. **AIMCODE Methodology Integration**
- **Demis Hassabis (Alpha Evolve):** Systematic, layered approach
  - Layer 1: Foundation
  - Layer 2: Application
  - Layer 3: Integration
  - Layer 4: Mastery
- **Systems Thinking:** All changes connect across systems
- **Deep Understanding:** Each layer solid before moving forward

### 2. **Unified Prompting Framework**
- Supports both `--quick` (5 questions) and `--full` (23 questions) modes
- Automatically applies unified prompting questions to development prompts
- Ensures comprehensive context gathering

### 3. **Complete System Integration**
- **Game Updates:** Unity scripts, JSON level files, exercise configs
- **Curriculum Updates:** Unified schema updates, learning objectives, standards
- **Book Updates:** Story content, learning sections, exercise buttons
- **Website Updates:** HTML/CSS/JS files, curriculum pathways, book cards

### 4. **Memory Context Saving**
- Saves all updates to memory files
- Tracks book updates, lesson updates, website updates
- Enables future reference and continuity

### 5. **Unified Curriculum Schema**
- Uses `CURRICULUM-DATA-EXAMPLE.json` as single source of truth
- All systems read from and update the same schema
- Ensures perfect synchronization

---

## 🔧 SETUP INSTRUCTIONS

### Step 1: Import Workflow to n8n

1. Open n8n interface
2. Click "Workflows" → "Import from File"
3. Select `n8n-ballcode-full-integration-workflow.json`
4. Workflow will be imported with all nodes

### Step 2: Configure Credentials

**Required Credentials:**

1. **OpenAI API Key:**
   - Go to n8n Settings → Credentials
   - Create new credential: "OpenAI API"
   - Add your OpenAI API key
   - Name it: `openai-credentials`

### Step 3: Set Environment Variables

**Required Environment Variables:**

Set these in n8n Settings → Environment Variables:

```bash
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

### Step 4: Activate Workflow

1. Open the workflow in n8n
2. Click "Active" toggle to activate
3. Note the webhook URL (e.g., `https://your-n8n-instance.com/webhook/ballcode-dev`)

---

## 📡 USAGE

### Basic Usage (Simple Prompt)

```bash
curl -X POST https://your-n8n-instance.com/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a new exercise for Book 2 that teaches conditionals",
    "mode": "quick"
  }'
```

### Advanced Usage (Full Context)

```bash
curl -X POST https://your-n8n-instance.com/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Update Book 3 to include pattern recognition concepts and create matching game exercise",
    "mode": "full",
    "context": {
      "bookId": 3,
      "focus": "pattern recognition",
      "gradeLevel": "6-8"
    },
    "sessionId": "session-12345"
  }'
```

### Request Format

```json
{
  "prompt": "Your development prompt here",
  "mode": "quick" | "full",  // Optional, defaults to "full"
  "context": {                // Optional
    "bookId": 1,
    "focus": "specific area",
    "gradeLevel": "3-5"
  },
  "sessionId": "optional-session-id"  // Optional
}
```

### Response Format

```json
{
  "status": "success",
  "timestamp": "2025-12-10T10:35:00.000Z",
  "sessionId": "session-12345",
  "prompt": "Your original prompt",
  "systemsUpdated": {
    "game": true,
    "curriculum": true,
    "book": true,
    "website": true
  },
  "integrationStatus": "All systems integrated successfully",
  "memoryContextSaved": true,
  "memoryFilePath": "/path/to/memory-context-session-12345.json",
  "actionPlanLayers": [
    { "layer": 1, "name": "Foundation", "tasks": [...] },
    { "layer": 2, "name": "Application", "tasks": [...] },
    { "layer": 3, "name": "Integration", "tasks": [...] },
    { "layer": 4, "name": "Mastery", "tasks": [...] }
  ],
  "successCriteria": [...],
  "nextSteps": [...]
}
```

---

## 🎯 INTEGRATION WITH UNIFIED PROMPTING SYSTEM

The workflow automatically integrates with your unified prompting system:

### Quick Mode (5 Questions)
When `mode: "quick"` is set, the AI uses:
1. Goal
2. Format
3. Context
4. Examples
5. Results

### Full Mode (23 Questions)
When `mode: "full"` is set (default), the AI uses:
- Goal & Clarity (4 questions)
- Format & Logic (4 questions)
- Guardrails & Adaptation (5 questions)
- Context, Examples & Alpha Evolve (7 questions)
- Results (3 questions)

---

## 💾 MEMORY CONTEXT FILES

The workflow saves memory context to files like:
```
memory-context-session-12345.json
```

**File Structure:**
```json
{
  "sessionId": "session-12345",
  "timestamp": "2025-12-10T10:35:00.000Z",
  "prompt": "Original development prompt",
  "updates": {
    "books": [...],
    "lessons": [...],
    "website": [...],
    "game": {...},
    "curriculum": "Schema updated"
  },
  "integrationStatus": "All systems updated and integrated"
}
```

**Use Cases:**
- Reference what was updated in previous sessions
- Track book/lesson/website changes over time
- Maintain continuity across development sessions

---

## 🔄 COMPLETE INTEGRATION FLOW

### Example: Adding a New Exercise

**Prompt:** "Add a new exercise for Book 1 that teaches sequences with 3 levels of difficulty"

**Workflow Actions:**
1. ✅ Analyzes prompt using AIMCODE (Demis Hassabis methodology)
2. ✅ Identifies systems affected: Game, Curriculum, Book, Website
3. ✅ Generates:
   - **Game:** Unity exercise JSON file with 3 difficulty levels
   - **Curriculum:** Updates schema with new exercise entry
   - **Book:** Adds exercise button and description
   - **Website:** Updates book page with exercise link
4. ✅ Saves memory context for future reference
5. ✅ Returns complete integration report

**Result:** All 4 systems updated and integrated seamlessly!

---

## 🎓 AIMCODE METHODOLOGY (DEMIS HASSABIS)

The workflow applies **Alpha Evolve** principles:

### Layer 1: Foundation
- Parse prompt
- Identify systems
- Load curriculum schema

### Layer 2: Application
- Generate updates for each system
- Apply changes systematically

### Layer 3: Integration
- Merge all updates
- Ensure cross-system compatibility
- Verify integration points

### Layer 4: Mastery
- Save memory context
- Finalize integration
- Prepare for deployment

---

## ✅ VALIDATION

### JSON Validation
```bash
python3 -m json.tool n8n-ballcode-full-integration-workflow.json > /dev/null && echo "✅ Valid JSON"
```

### Node Count
- **Total Nodes:** 18
- **AI Nodes:** 5 (Analysis + 4 system generators)
- **Code Nodes:** 5 (Processing and merging)
- **Conditional Nodes:** 4 (System checks)
- **Execute Command Nodes:** 1 (Save memory)
- **Webhook Nodes:** 2 (Trigger + Response)

### Connection Validation
All nodes are properly connected:
- ✅ Webhook trigger → Normalize input
- ✅ All system updates → Merge
- ✅ Merge → Memory → Finalize → Response

---

## 🚨 TROUBLESHOOTING

### Issue: OpenAI API Errors
**Solution:** Check credentials in n8n Settings → Credentials

### Issue: File Path Errors
**Solution:** Verify `WORKFLOW_PATH` environment variable is set correctly

### Issue: Memory Context Not Saving
**Solution:** Check file permissions for workflow path directory

### Issue: Schema Not Loading
**Solution:** Verify `CURRICULUM-DATA-EXAMPLE.json` exists at workflow path

---

## 📚 RELATED DOCUMENTATION

- **Unified Curriculum Schema:** `CURRICULUM-DATA-EXAMPLE.json`
- **Schema Documentation:** `UNIFIED-SCHEMA-DOCUMENTATION.md`
- **AIMCODE Methodology:** `AIMCODE-METHODOLOGY.md`
- **Unified Prompting System:** `UNIFIED-PROMPTING-SYSTEM.md`
- **Integration Plan:** `BOOK-CURRICULUM-GAME-INTEGRATION-PLAN.md`

---

## 🎉 SUCCESS METRICS

**Workflow is successful when:**
- ✅ All 4 systems (Game, Curriculum, Book, Website) are updated
- ✅ Integration points are verified
- ✅ Memory context is saved
- ✅ Curriculum schema is synchronized
- ✅ All changes work together seamlessly

---

**Version:** 1.0.0  
**Created:** December 10, 2025  
**Last Updated:** December 10, 2025  
**Status:** ✅ Ready for Production Use



