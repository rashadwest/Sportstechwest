# 🐍 Python Schema Update Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** How to use Python script to update schema (replaces n8n workflows)

---

## 🎯 WHERE PYTHON FITS IN

### The Flow:
```
1. You want to update content
   ↓
2. Python script updates CURRICULUM-DATA-EXAMPLE.json
   ↓
3. Python copies to BallCode/data/curriculum-data.json
   ↓
4. JavaScript auto-syncs all systems (Website, Books, Curriculum)
   ↓
5. Done! ✅
```

**Python replaces:** The 3 deleted n8n workflows (Book Update, Curriculum Sync, Exercise Integration)

**Why Python?**
- ✅ Easier to write/test/debug than n8n
- ✅ Better for JSON manipulation
- ✅ Can be called from anywhere (CLI, scripts, n8n)
- ✅ JavaScript handles the sync automatically

---

## 📋 USAGE

### Update a Book

```bash
python3 scripts/update_ballcode_schema.py \
  --type book \
  --id 1 \
  --data '{"title": "New Title", "status": "complete"}'
```

### Update Curriculum

```bash
python3 scripts/update_ballcode_schema.py \
  --type curriculum \
  --data '{"learningObjectives": ["New objective 1", "New objective 2"]}'
```

### Add Exercise to Book

```bash
python3 scripts/update_ballcode_schema.py \
  --type exercise \
  --book-id 1 \
  --data '{
    "exerciseId": "ex1",
    "url": "ballcode.co/play?book=1&exercise=ex1",
    "difficulty": "beginner",
    "description": "Test exercise"
  }'
```

### Dry Run (Preview Changes)

```bash
python3 scripts/update_ballcode_schema.py \
  --type book \
  --id 1 \
  --data '{"title": "New Title"}' \
  --dry-run
```

---

## 🔧 INTEGRATION WITH N8N

### Option 1: Call from n8n Execute Command Node

**In n8n workflow:**
```json
{
  "command": "python3",
  "arguments": "{{ $env.WORKFLOW_PATH }}/scripts/update_ballcode_schema.py --type book --id {{ $json.bookId }} --data '{{ JSON.stringify($json.bookData) }}'"
}
```

### Option 2: Use from Full Integration Workflow

**After AI returns action plan:**
1. Parse action plan
2. Extract schema updates needed
3. Call Python script with updates
4. JavaScript auto-syncs everything

---

## ✅ WHAT IT DOES

1. **Loads schema** from `CURRICULUM-DATA-EXAMPLE.json`
2. **Updates** the requested section (book/curriculum/exercise)
3. **Updates metadata** (version, lastUpdated)
4. **Saves** to main schema file
5. **Copies** to API location (`BallCode/data/curriculum-data.json`)
6. **JavaScript auto-syncs** all systems on next page load

---

## 🎯 COMPLETE WORKFLOW

### Before (Complex):
```
n8n workflow → Validate → Update Schema → Update Website → Update Books → Update Curriculum → Done
(5 workflows, 62 nodes, complex)
```

### After (Simple):
```
Python script → Update Schema → JavaScript auto-syncs → Done
(1 script, automatic sync, simple)
```

---

## 📊 EXAMPLES

### Example 1: Update Book Title

```bash
python3 scripts/update_ballcode_schema.py \
  --type book \
  --id 1 \
  --data '{"title": "The Foundation Block - Updated"}'
```

**Result:**
- ✅ Schema updated
- ✅ Website book cards update automatically
- ✅ Book pages update automatically
- ✅ No manual steps needed

### Example 2: Add Learning Objective

```bash
python3 scripts/update_ballcode_schema.py \
  --type curriculum \
  --data '{
    "learningObjectives": [
      "Understand sequences",
      "NEW: Understand loops",
      "Apply concepts to basketball"
    ]
  }'
```

**Result:**
- ✅ Curriculum updated
- ✅ All books show new objectives
- ✅ Website curriculum pathway updates
- ✅ No manual steps needed

### Example 3: Add Exercise

```bash
python3 scripts/update_ballcode_schema.py \
  --type exercise \
  --book-id 1 \
  --data '{
    "exerciseId": "loops-exercise",
    "url": "ballcode.co/play?book=1&exercise=loops-exercise",
    "difficulty": "intermediate",
    "description": "Practice loops with basketball moves"
  }'
```

**Result:**
- ✅ Exercise added to Book 1
- ✅ Exercise button appears on book page
- ✅ Game link works
- ✅ Return flow configured
- ✅ No manual steps needed

---

## 🚀 QUICK REFERENCE

```bash
# Update book
python3 scripts/update_ballcode_schema.py --type book --id 1 --data '{"title": "New"}'

# Update curriculum
python3 scripts/update_ballcode_schema.py --type curriculum --data '{"learningObjectives": [...]}'

# Add exercise
python3 scripts/update_ballcode_schema.py --type exercise --book-id 1 --data '{"exerciseId": "ex1"}'

# Preview changes
python3 scripts/update_ballcode_schema.py --type book --id 1 --data '{"title": "New"}' --dry-run
```

---

## ✅ BENEFITS

1. **Simpler:** 1 script vs 3 workflows
2. **Faster:** Direct updates, no workflow overhead
3. **Easier to debug:** Python is more readable
4. **Automatic sync:** JavaScript handles everything
5. **Flexible:** Can be called from anywhere

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use



