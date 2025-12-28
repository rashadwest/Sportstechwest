# Curriculum Update Template
## Standard Integration Sections for Code-Basketball-Files

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Template for integrating code-basketball-files into curriculum documents  
**Status:** Standard Template

---

## SECTION 1: BOOK 3 DATA INTEGRATION UPDATE

### Template for Book 3 Section Updates

```markdown
#### Book 3: The Pattern (In & Out Dribble) - UPDATED
**Status:** ⚠️ Outline Ready (Story needs writing) - **NOW WITH DATA INTEGRATION**

**Basketball Context:** Repeated moves, patterns, deception + **Data-driven pattern analysis**  
**Python Concept:** Loops and repetition + **Data fetching and pattern analysis**  
**Dribble Level:** 3 (In & Out Dribble)

**Three-Phase Progression:**

**Phase 1 (Block Coding):**
```
REPEAT [Fake Left] 3 TIMES
THEN [Go Right]

NEW: FETCH [Opponent Data] FROM [Ball Don't Lie API]
```

**Phase 2 (Transition Bridge):**
```
Block: REPEAT [Fake Left] 3 TIMES
Code:  for i in range(3): fake_left()

NEW:
Block: FETCH [Opponent Data]
Code:  data = fetch_opponent_stats()
```

**Phase 3 (Python):**
```python
# Pattern repetition - loops
for move in range(3):
    fake_left()
    go_right()
    if defender_falls_for_fake:
        break

# NEW: Data fetching and analysis
opponent_data = fetch_opponent_stats()  # Simplified for kids
for game in opponent_data:
    if game.reaction == "left":
        left_count += 1
# Pattern found: 87% left reactions
```

**Learning Objectives:**
1. Understand loops and repetition - Repeat actions multiple times
2. Create repeat blocks - Use loop blocks in programs
3. Write Python loops - Use `for` and `while` loops
4. Use patterns in code - Apply loops to solve problems
5. **NEW:** Understand data fetching - Get information from APIs (simplified)
6. **NEW:** Analyze patterns in data - Loop through data to find patterns

**Supplementary Resources:**
- **"Learn to Code with Basketball" by Nathan Braun**
  - Real basketball data files for analysis
  - API integration examples (Ball Don't Lie API)
  - Data visualization exercises
  - Perfect bridge from story-based learning to practical Python
  - **Repository:** https://github.com/nathanbraun/code-basketball-files
  - **When to Use:** After completing Book 3, students can use this for advanced practice with real data
```

---

## SECTION 2: SUPPLEMENTARY RESOURCES

### Template for Supplementary Resources Section

```markdown
---

## 📚 SUPPLEMENTARY RESOURCES

### "Learn to Code with Basketball" by Nathan Braun

**What It Is:**
- Comprehensive Python programming book using basketball data
- Real basketball statistics and game data
- API integration examples (Ball Don't Lie API)
- Data visualization techniques
- Exercise solutions and Anki flashcards

**How It Complements BallCODE:**
- **BallCODE:** Story-based learning (concepts through narrative)
- **code-basketball-files:** Practical application (real data, real code)
- **Together:** Complete pathway from story to real-world Python

**Integration Points:**

**For Students:**
- **After Book 1-3:** "Want to go deeper? Check out 'Learn to Code with Basketball'"
- **Book 4+:** Use their data files for real-world exercises
- **Advanced Track:** Full API integration examples

**For Teachers:**
- **Supplementary Material:** Use for advanced students
- **Extension Activities:** Real data analysis exercises
- **Assessment:** Additional practice problems

**Repository:** https://github.com/nathanbraun/code-basketball-files

**What's Included:**
- Real basketball data files (CSV, JSON, SQLite)
- Python code examples (pandas, API, visualization)
- Exercise solutions
- Anki flashcards for spaced repetition

**When to Use:**
- Students who complete Books 1-3 quickly
- Students interested in data science
- Advanced Python practice
- Real-world application projects

---
```

---

## SECTION 3: REAL-WORLD DATA INTEGRATION

### Template for Real-World Data Integration Section

```markdown
---

## 📊 REAL-WORLD DATA INTEGRATION

### Ball Don't Lie API Integration

**What It Is:**
- Free basketball statistics API
- Provides NBA player stats, game data, team information
- Requires free account (easy signup)
- Perfect for educational use

**How We Use It:**
- **Book 3+:** Students learn data fetching concepts (simplified)
- **Book 4+:** Students analyze real basketball data
- **Book 5+:** Students integrate API calls into Python code
- **Advanced Track:** Full API integration for high school students

**Integration Points:**
1. **Story Integration:** Arc fetches opponent data in Book 3 story
2. **Block Coding:** "FETCH [data] FROM [API]" blocks (simplified)
3. **Python Practice:** Simplified `fetch_data()` functions
4. **Real Data:** Use actual NBA statistics from code-basketball-files

**Example Flow:**
```
Book 3 Story: Arc fetches opponent data
    ↓
Book 3 Exercise: Students see data fetching concept
    ↓
Book 4: Students work with real data files
    ↓
Book 5: Students use Ball Don't Lie API
    ↓
Advanced: Full API integration with code-basketball-files
```

**Supplementary Resource:**
- **"Learn to Code with Basketball" by Nathan Braun**
  - Repository: https://github.com/nathanbraun/code-basketball-files
  - Perfect for: Students who want to go deeper after Books 1-3
  - Provides: Real data files, API examples, data visualization exercises

---
```

---

## SECTION 4: "WANT TO GO DEEPER?" REFERENCE

### Template for "Want to Go Deeper?" Section

```markdown
---

## 📚 Want to Go Deeper?

You've learned the basics of [concept] through Nova's story. Want to apply these skills to real basketball data?

**Check out "Learn to Code with Basketball" by Nathan Braun:**
- Real basketball data analysis
- API integration with live game statistics
- Data visualization techniques
- Advanced Python projects

**GitHub Repository:** https://github.com/nathanbraun/code-basketball-files

**Perfect for:** Students who want to go beyond the story and work with real data!

---
```

---

## SECTION 5: LEARNING OBJECTIVES UPDATE

### Template for Adding Data-Related Learning Objectives

```markdown
**Learning Objectives:**
[Existing objectives...]
5. **NEW:** Understand data fetching - Get information from APIs (simplified)
6. **NEW:** Analyze patterns in data - Loop through data to find patterns
7. **NEW:** Use real-world data - Work with actual basketball statistics
```

---

## SECTION 6: PYTHON CODE EXAMPLES

### Template for Data Integration Code Examples

```markdown
**Python Code Example:**
```python
# Pattern repetition - loops
for move in range(3):
    fake_left()
    go_right()
    if defender_falls_for_fake:
        break

# NEW: Data fetching and analysis
opponent_data = fetch_opponent_stats()  # Simplified for kids
for game in opponent_data:
    if game.reaction == "left":
        left_count += 1
# Pattern: 87% left reactions
```
```

---

## SECTION 7: GAME INTEGRATION UPDATE

### Template for Game Integration Updates

```markdown
**Game Integration:**
- **Exercise Name:** "Pattern Master Challenge" + "Data Detective Challenge"
- **Skill Practice:** Creating patterns with loops + Analyzing opponent data
- **Block Coding:** Create loop blocks + Data fetching blocks
- **Python Practice:** Write loop code + Simplified data analysis
- **Success Criteria:** Create 3 different loop patterns + Analyze opponent data
```

---

## USAGE INSTRUCTIONS

### When to Use Each Section

1. **Section 1 (Book 3 Update):** Use when updating Book 3 sections in curriculum documents
2. **Section 2 (Supplementary Resources):** Add to all curriculum documents after main content
3. **Section 3 (Real-World Data):** Add to comprehensive curriculum documents
4. **Section 4 (Want to Go Deeper):** Add after Book 1-3 sections
5. **Section 5 (Learning Objectives):** Update existing learning objectives sections
6. **Section 6 (Code Examples):** Update Python code example sections
7. **Section 7 (Game Integration):** Update game integration sections

### Integration Guidelines

- **Maintain Story-First:** Keep 70% story, 30% skill ratio
- **Keep Simple:** Data concepts simplified for grades 3-8
- **Basketball-First:** Data is a tool, basketball is the framework
- **Consistent Messaging:** Use same language across all documents
- **AIMCODE Alignment:** Ensure all updates maintain AIMCODE principles

---

**Copyright © 2025 Rashad West. All Rights Reserved.**






