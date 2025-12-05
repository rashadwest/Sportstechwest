# BallCODE Book: Complete Notion Setup Guide
## Get All Chapters and Structure Ready for Daily Work

This guide will help you set up your complete BallCODE book structure in Notion so you can work on it daily.

---

## Quick Setup: Option 1 - Automated (Using MCP)

If you have Notion MCP connected, you can use these commands to create everything at once.

### Step 1: Create the Book Database

Copy and paste this in Claude Desktop (with Notion MCP connected):

```
Use Notion MCP to create a new database with these properties:

Database Name: "BallCODE Book Project"

Properties to add:
- Title (Title type)
- Status (Select type) - Options: Planning, Outline Complete, Chapter Draft, In Review, Edited, Final Review, Published
- Chapter Number (Number type)
- Chapter Title (Text type)
- Word Count (Number type)
- Completion % (Number type)
- Date Started (Date type)
- Date Completed (Date type)
- Tags (Multi-select type) - Options: coding, math, basketball, exercises, examples
- Author (Text type) - Default: "Rashad West"
- Editor (Text type)
- Reviewer (Text type)
- Notes (Text type)
- Code Examples (Text type)
- Image Prompts (Text type)
- Revision Count (Number type)

After creating the database, give me the database ID.
```

### Step 2: Create Book Overview Page

```
Use Notion MCP to create a new page in the BallCODE Book Project database with:

Title: "Book Overview: BallCODE - Coding and Math for Basketball Programming"
Status: Planning
Chapter Number: 0

Then add this content structure:

# BallCODE Book Project Overview

## Project Information
- **Title:** BallCODE: Coding and Math for Basketball Programming
- **Target Audience:** Educators, Students (Middle School to High School), Developers
- **Estimated Pages:** 200-250 pages
- **Timeline:** 6-9 months development
- **Current Status:** Planning Phase

## Learning Objectives
- Teach coding fundamentals through basketball analogies
- Connect math concepts to real-world sports scenarios
- Build systematic thinking skills
- Create hands-on coding exercises

## Table of Contents
[Will be populated as chapters are created]

## Financial Breakdown
See: /workflows/ballcode-book-financial-breakdown.md

## Project Timeline
- Week 1: Outline and planning
- Week 2-4: Chapter 1-3 drafts
- Week 5-7: Chapter 4-6 drafts
- Week 8-10: Chapter 7-9 drafts
- Week 11-13: Chapter 10-12 drafts
- Week 14-16: Review and editing
- Week 17-18: Final revisions
- Week 19-20: Publishing preparation

After creating the page, give me the page URL.
```

### Step 3: Create All Chapter Pages (12 Chapters)

Run this command for each chapter (update Chapter Number and Title):

**Chapter 1:**
```
Use Notion MCP to create a new page in the BallCODE Book Project database with:

Title: "Chapter 1: Introduction to BallCODE"
Status: Planning
Chapter Number: 1
Chapter Title: "Introduction to BallCODE"
Tags: coding, basketball
Author: Rashad West
Word Count: 0
Completion %: 0

Then add this template content structure:

# Chapter 1: Introduction to BallCODE

## Chapter Metadata
- **Chapter Number:** 1
- **Word Count Target:** 3,000-4,000
- **Completion Status:** Planning
- **Related Chapters:** None (Introduction)

## Chapter Content

### Outline/Structure
1. What is BallCODE?
2. Why Basketball and Coding?
3. What You'll Learn
4. How to Use This Book
5. Setting Up Your Environment

### Main Content
[Your content here]

### Code Examples
[Code snippets will go here]

### Math Concepts
[Math concepts for this chapter]

### Basketball Applications
[How basketball connects to coding concepts]

### Exercises/Problems
[Practice exercises]

## Visual Assets

### Diagram Prompts (for Glif)
- BallCODE logo/concept visualization
- Basketball court with coding elements overlay

### Code Visualization Needs
- Basic syntax examples
- First program structure

### Basketball Play Diagrams
- Simple court diagram
- Player movement patterns

## Review Checklist
- [ ] Content Complete
- [ ] Code Examples Tested
- [ ] Math Verified
- [ ] Basketball Examples Accurate
- [ ] Exercises Reviewed
- [ ] Images Generated
- [ ] Technical Review Complete
- [ ] Educational Review Complete
- [ ] Copy Edited
- [ ] Ready for Final Review

After creating, give me the page URL.
```

**Repeat for Chapters 2-12 with these titles:**

- Chapter 2: Basketball as Logic - If/Then Statements
- Chapter 3: Loops and Repetition - Defensive Rotations
- Chapter 4: Pattern Recognition - Reading the Court
- Chapter 5: Variables and Data - Player Stats
- Chapter 6: Functions - Offensive Sets
- Chapter 7: Arrays and Lists - Team Rosters
- Chapter 8: Math Foundations - Shooting Percentages
- Chapter 9: Algorithms - Play Execution
- Chapter 10: Debugging - Analyzing Mistakes
- Chapter 11: Advanced Concepts - Complex Plays
- Chapter 12: Building Your First BallCODE Program

**Appendices:**
```
Use Notion MCP to create a new page in the BallCODE Book Project database with:

Title: "Appendices: Reference Guide and Exercise Solutions"
Status: Planning
Chapter Number: 13
Tags: reference, exercises

Add content structure for:
- Reference Guide
- Exercise Solutions
- Glossary
- Additional Resources
```

---

## Manual Setup: Option 2 - Step by Step

If you prefer to set up manually or MCP isn't available:

### Step 1: Create Database in Notion

1. Open Notion
2. Click "+ New page" or create in your workspace
3. Type "/database" and select "Table - Full page"
4. Name it "BallCODE Book Project"

### Step 2: Add Database Properties

Click the "+" button in the rightmost column and add each property:

1. **Status** - Select type
   - Click property, choose "Select"
   - Add options: Planning, Outline Complete, Chapter Draft, In Review, Edited, Final Review, Published

2. **Chapter Number** - Number type
3. **Chapter Title** - Text type
4. **Word Count** - Number type
5. **Completion %** - Number type
6. **Date Started** - Date type
7. **Date Completed** - Date type
8. **Tags** - Multi-select type
   - Add options: coding, math, basketball, exercises, examples
9. **Author** - Text type (default: "Rashad West")
10. **Editor** - Text type
11. **Reviewer** - Text type
12. **Notes** - Text type
13. **Code Examples** - Text type
14. **Image Prompts** - Text type
15. **Revision Count** - Number type

### Step 3: Create Book Overview Page

1. In the database, click "New" to create a page
2. Title: "Book Overview: BallCODE - Coding and Math for Basketball Programming"
3. Set properties:
   - Status: Planning
   - Chapter Number: 0
4. Add content sections (use toggles for collapsible sections):
   - Project Information
   - Learning Objectives
   - Table of Contents
   - Financial Breakdown (link to external doc)
   - Project Timeline

### Step 4: Create Chapter Template

1. Create a new page in the database
2. Title it "Template: Chapter Page"
3. Build the structure as shown in the automated section above
4. Save as template: Click "..." → "Templates" → "New template"
5. Name it "Book Chapter Template"

### Step 5: Create All Chapter Pages

1. Click "New" in database
2. Select "Book Chapter Template"
3. Update:
   - Title (Chapter 1, Chapter 2, etc.)
   - Chapter Number
   - Chapter Title
   - Status: Planning
4. Repeat for all 12 chapters + Appendices

### Step 6: Link Chapters to Overview

1. Open Book Overview page
2. Create "Table of Contents" section
3. Use "@" to link each chapter page
4. Create a bulleted or numbered list of all chapters

---

## Daily Workflow Setup

### Create Views for Daily Work

1. **Current Work View:**
   - Filter: Status = "Chapter Draft" OR Status = "In Review"
   - Sort by: Chapter Number
   - Group by: Status

2. **Progress View:**
   - Group by: Completion %
   - Sort by: Chapter Number
   - Show: Chapter Number, Chapter Title, Completion %, Word Count

3. **All Chapters View:**
   - Show all chapters
   - Sort by: Chapter Number
   - Columns: Title, Status, Completion %, Word Count, Date Started

### Set Up Daily Reminders

1. Create a "Daily Tasks" section in Book Overview
2. Use Notion's reminder feature or create a recurring task:
   - Review current chapter progress
   - Write 500-1000 words daily
   - Update completion percentage
   - Test code examples

### Weekly Review Setup

1. Create a "Weekly Review" template page
2. Track:
   - Chapters completed this week
   - Word count progress
   - Issues/blockers
   - Next week's goals

---

## Quick Reference: Chapter List

For easy copy-paste when creating chapters:

1. Introduction to BallCODE
2. Basketball as Logic - If/Then Statements
3. Loops and Repetition - Defensive Rotations
4. Pattern Recognition - Reading the Court
5. Variables and Data - Player Stats
6. Functions - Offensive Sets
7. Arrays and Lists - Team Rosters
8. Math Foundations - Shooting Percentages
9. Algorithms - Play Execution
10. Debugging - Analyzing Mistakes
11. Advanced Concepts - Complex Plays
12. Building Your First BallCODE Program
13. Appendices: Reference Guide and Exercise Solutions

---

## Integration with Existing Workflow

Once set up, you can:

1. **Use Claude + MCP** to:
   - Generate chapter content
   - Create code examples
   - Develop exercises
   - Generate image prompts

2. **Use Glif MCP** to:
   - Generate diagrams for each chapter
   - Create visualizations
   - Design basketball play diagrams

3. **Track alongside blog posts** in your weekly reviews

---

## Next Steps After Setup

1. ✅ Create database with all properties
2. ✅ Create Book Overview page
3. ✅ Create all 13 chapter pages (12 chapters + appendices)
4. ✅ Set up custom views for daily work
5. ✅ Link chapters in Table of Contents
6. ✅ Start writing Chapter 1!

---

*Once you have the database set up, you can work on any chapter daily by simply opening it from your Notion workspace.*






