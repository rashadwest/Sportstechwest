# 🤖 Robot Curriculum Guide
## Python Curriculum Development Automation

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Created:** December 14, 2025  
**Purpose:** Guide for using robot-curriculum.py automation tool

---

## 🎯 WHAT IS ROBOT-CURRICULUM?

`robot-curriculum.py` is an automation tool that helps you work on the future Python curriculum by:

- ✅ Creating book proposal documents
- ✅ Generating curriculum integration maps
- ✅ Checking curriculum development status
- ✅ Generating curriculum summaries
- ✅ Following the BallCODE Curriculum Development System

---

## 🚀 QUICK START

### Basic Usage

```bash
# Show help
python3 robot-curriculum.py

# Check curriculum status
python3 robot-curriculum.py status

# Create book proposal
python3 robot-curriculum.py proposal 4 "Functions" "Running plays"

# Create curriculum integration map
python3 robot-curriculum.py mapping 1

# Generate curriculum summary
python3 robot-curriculum.py summary
```

---

## 📋 COMMANDS

### 1. Status Check

**Command:** `robot-curriculum.py status`

**What it does:**
- Shows total books in curriculum
- Displays status breakdown (complete, in-progress, planned)
- Lists all books with their concepts and status
- Checks which documents exist (proposals, integration maps)

**Example:**
```bash
python3 robot-curriculum.py status
```

**Output:**
- Total books count
- Status breakdown
- Book details (title, concept, status)
- Document status (proposals, maps)

---

### 2. Create Book Proposal

**Command:** `robot-curriculum.py proposal <book_num> <concept> <basketball_context>`

**What it does:**
- Creates a book proposal document following the Curriculum Development System
- Generates template with all required sections
- Saves to `documents/BOOK-{N}-PROPOSAL-{CONCEPT}.md`

**Example:**
```bash
python3 robot-curriculum.py proposal 4 "Functions" "Running plays"
```

**Creates:** `documents/BOOK-4-PROPOSAL-FUNCTIONS.md`

**Template includes:**
- Title & Concept
- Learning Objectives (Measurable)
- Basketball Story Framework (3-Act Structure)
- Python Progression (Phase 1, 2, 3)
- Standards Alignment
- Game Integration
- Curriculum Connections
- Next Steps

---

### 3. Create Curriculum Integration Map

**Command:** `robot-curriculum.py mapping <book_num>`

**What it does:**
- Creates curriculum integration map for a specific book
- Pulls data from `CURRICULUM-DATA-EXAMPLE.json`
- Generates complete integration document
- Saves to `documents/Book-{N}-Curriculum-Integration-Map.md`

**Example:**
```bash
python3 robot-curriculum.py mapping 1
```

**Creates:** `documents/Book-1-Curriculum-Integration-Map.md`

**Includes:**
- Curriculum Connection (Python concepts, basketball skills, learning objectives)
- Three-Phase Learning Pathway
- Integration Points (Website → Book → Game → Curriculum)
- Standards Alignment (CSTA, Common Core, NGSS)
- Game Exercise Specification
- Integration Checklist

---

### 4. Generate Curriculum Summary

**Command:** `robot-curriculum.py summary`

**What it does:**
- Generates a complete curriculum overview
- Groups books by series (Foundation, Intermediate, Advanced)
- Shows progress summary
- Saves to `documents/CURRICULUM-SUMMARY-ROBOT-GENERATED.md`

**Example:**
```bash
python3 robot-curriculum.py summary
```

**Creates:** `documents/CURRICULUM-SUMMARY-ROBOT-GENERATED.md`

**Includes:**
- Curriculum Overview
- Book Series (Foundation, Intermediate, Advanced)
- Three-Phase Learning Pathway
- Progress Summary

---

## 📚 WORKFLOW EXAMPLES

### Example 1: Starting a New Book

```bash
# 1. Check current status
python3 robot-curriculum.py status

# 2. Create proposal for Book 4
python3 robot-curriculum.py proposal 4 "Functions" "Running plays"

# 3. Create integration map
python3 robot-curriculum.py mapping 4

# 4. Check status again to see progress
python3 robot-curriculum.py status
```

### Example 2: Generating Documentation for All Books

```bash
# Generate integration maps for all books
python3 robot-curriculum.py mapping 1
python3 robot-curriculum.py mapping 2
python3 robot-curriculum.py mapping 3

# Generate overall summary
python3 robot-curriculum.py summary
```

### Example 3: Planning Future Books

```bash
# Create proposals for future books
python3 robot-curriculum.py proposal 5 "Data Structures" "Team formations"
python3 robot-curriculum.py proposal 6 "Algorithms" "Play selection"
python3 robot-curriculum.py proposal 7 "AI Integration" "Game strategy"

# Check status to see all proposals
python3 robot-curriculum.py status
```

---

## 🔧 TECHNICAL DETAILS

### File Locations

- **Script:** `robot-curriculum.py` (project root)
- **Curriculum Data:** `CURRICULUM-DATA-EXAMPLE.json` (project root)
- **Output Directory:** `documents/` folder
- **Documents Created:**
  - `BOOK-{N}-PROPOSAL-{CONCEPT}.md`
  - `Book-{N}-Curriculum-Integration-Map.md`
  - `CURRICULUM-SUMMARY-ROBOT-GENERATED.md`

### Data Source

The robot reads from `CURRICULUM-DATA-EXAMPLE.json` which contains:
- Book information (title, status, concepts)
- Curriculum data (learning objectives, standards, phases)
- Game exercise specifications
- Website integration data

### Requirements

- Python 3.8+
- Access to `CURRICULUM-DATA-EXAMPLE.json`
- `documents/` folder (created automatically if missing)

---

## ✅ INTEGRATION WITH CURRICULUM DEVELOPMENT SYSTEM

The robot follows the **BallCODE Curriculum Development System** workflow:

1. **Phase 1: Concept Development** → `proposal` command
2. **Phase 2: Story Development** → Manual (user writes story)
3. **Phase 3: Production Outline** → Manual (user creates outline)
4. **Phase 4: Visual Assets** → Manual (user generates images)
5. **Phase 5: Book Assembly** → Manual (user assembles book)
6. **Phase 6: Teacher Resources** → Manual (user creates guide)
7. **Phase 7: Game Integration** → `mapping` command helps with this

---

## 🎯 NEXT STEPS

1. **Run status check** to see current curriculum state
2. **Create proposals** for future books you want to develop
3. **Generate integration maps** for books that need curriculum connections
4. **Generate summary** to see overall curriculum progress

---

## 📝 NOTES

- All documents are saved to `documents/` folder (not desktop)
- Documents follow BallCODE Curriculum Development System format
- Robot generates templates - you fill in the details
- Robot reads from `CURRICULUM-DATA-EXAMPLE.json` for existing book data

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Last Updated:** December 14, 2025


