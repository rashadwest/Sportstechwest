# 📁 JSON File Locations - Complete Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 6, 2025

---

## 🎯 MAIN JSON FILES

### 1. n8n Workflow File
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/n8n-unity-automation-workflow.json`

**Purpose:** Complete n8n workflow for Unity automation  
**Status:** ✅ Bug-free (0 issues, 0 warnings)  
**Size:** ~675 lines  
**Contains:** 23 nodes, complete automation flow

**Usage:**
```bash
# Edit in Cursor
# Debug: python3 debug-workflow.py n8n-unity-automation-workflow.json
# Deploy: ./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json [id]
```

---

### 2. Unified Curriculum Schema
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/CURRICULUM-DATA-EXAMPLE.json`

**Purpose:** Single source of truth for all 4 systems (Website, Book, Curriculum, Game)  
**Status:** ✅ Complete  
**Contains:** Books 1, 2, 3 with complete integration data

**Usage:**
- Update this file → All 4 systems sync automatically
- Read by API functions
- Used by integration scripts

---

### 3. Curriculum Schema Definition
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/CURRICULUM-UNIFIED-SCHEMA.json`

**Purpose:** JSON Schema definition (validation structure)  
**Status:** ✅ Complete  
**Contains:** Schema definition for validation

---

### 4. Copied Schema (For API Access)
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode/data/curriculum-data.json`

**Purpose:** Copy of schema file accessible to Netlify Functions  
**Status:** ✅ Created  
**Source:** Copied from `CURRICULUM-DATA-EXAMPLE.json`

---

## 📋 ALL JSON FILES IN PROJECT

### n8n Workflows
- `n8n-unity-automation-workflow.json` - Main Unity automation workflow

### Curriculum Data
- `CURRICULUM-DATA-EXAMPLE.json` - Main schema file (source of truth)
- `CURRICULUM-UNIFIED-SCHEMA.json` - Schema definition
- `BallCode/data/curriculum-data.json` - Copy for API access

### Unity Game Data
- `Unity-Scripts/Levels/book1_math_foundation.json`
- `Unity-Scripts/Levels/book2_math_decision.json`
- `Unity-Scripts/Levels/book3_math_pattern.json`
- `Unity-Scripts/Levels/book4_advanced_sequences.json`
- `Unity-Scripts/Levels/book5_nested_conditionals.json`

### Other JSON Files
- `ballcode_blind_analysis.json` - Analysis data
- `automated_outputs/*.json` - Various output files

---

## 🎯 KEY FILES FOR YOUR WORK

### For 4-Pillar Integration:
**Main File:** `CURRICULUM-DATA-EXAMPLE.json`
- Update this → All systems sync
- Location: Root of project

**API Access Copy:** `BallCode/data/curriculum-data.json`
- Used by Netlify Functions
- Location: `BallCode/data/`

### For Game Editing:
**Main File:** `n8n-unity-automation-workflow.json`
- Edit in Cursor
- Deploy via terminal
- Location: Root of project

---

## 📍 QUICK ACCESS

### Edit n8n Workflow:
```bash
# File location
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/n8n-unity-automation-workflow.json

# Edit in Cursor
# Then deploy:
./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json [id]
```

### Edit Curriculum Schema:
```bash
# Main file
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/CURRICULUM-DATA-EXAMPLE.json

# Edit in Cursor
# Then copy to API location:
cp CURRICULUM-DATA-EXAMPLE.json BallCode/data/curriculum-data.json
```

---

## 🔍 FIND JSON FILES

```bash
# Find all JSON files
find . -name "*.json" -type f

# Find main workflow
find . -name "n8n-unity-automation-workflow.json"

# Find schema files
find . -name "*CURRICULUM*.json"
```

---

## 📊 FILE SIZES & STATUS

| File | Location | Status | Purpose |
|------|----------|--------|---------|
| `n8n-unity-automation-workflow.json` | Root | ✅ Bug-free | Unity automation |
| `CURRICULUM-DATA-EXAMPLE.json` | Root | ✅ Complete | 4-pillar schema |
| `CURRICULUM-UNIFIED-SCHEMA.json` | Root | ✅ Complete | Schema definition |
| `BallCode/data/curriculum-data.json` | BallCode/data | ✅ Created | API access |

---

**Status:** ✅ All JSON files located and documented  
**Ready to use:** Yes




