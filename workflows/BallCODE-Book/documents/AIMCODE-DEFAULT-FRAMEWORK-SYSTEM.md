# AIMCODE Default Framework System
## Automatic Framework Application for Prompts

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 21, 2025  
**Purpose:** Default framework system for automatic AIMCODE and AIMCODE Ed application  
**Status:** Production System  
**Version:** 1.0

---

## 🎯 EXECUTIVE SUMMARY

**Default Framework System:**
- **AIMCODE** = Default for in-depth, comprehensive prompts (ANY domain - system design, research, analysis, methodology, etc.)
- **AIMCODE Ed** = Default for educational/curriculum-specific prompts (lesson plans, assessments, teacher guides)

**Key Distinction:**
- **AIMCODE** is a comprehensive methodology (CLEAR → Alpha Evolve → Research → Experts) used for ANY in-depth work
- **AIMCODE Ed** is a specialized prompting framework (S-M-A-R-T-PED) for educational/curriculum tasks
- AIMCODE is NOT just for education - it's a general methodology for comprehensive analysis

**How It Works:**
- AI automatically applies appropriate framework based on prompt type
- User can explicitly override with "@" commands
- Seamless integration with existing "@" system

---

## 📋 DEFAULT FRAMEWORK RULES

### AIMCODE (Default for In-Depth Prompts - ANY Domain)

**What AIMCODE Is:**
A comprehensive methodology for ANY in-depth work - system design, research, analysis, methodology development, problem-solving, etc. NOT limited to education.

**Automatically Applied When:**
- ✅ User requests comprehensive analysis (any domain)
- ✅ User asks for deep research or investigation
- ✅ User wants systematic, layered approach
- ✅ User requests expert consultation
- ✅ User asks for PhD-level research
- ✅ User wants full methodology application
- ✅ User says "go in depth" or "deep dive"
- ✅ User requests complete analysis
- ✅ System design, architecture, integration work
- ✅ Workflow development, automation design
- ✅ Technical problem-solving requiring deep analysis

**AIMCODE Workflow Applied:**
1. **CLEAR Framework** - Establish clarity, logic, examples, adaptation, results
2. **Alpha Evolve** - Systematic deep learning, layer-by-layer
3. **PhD-Level Research** - Peer-reviewed research with citations
4. **Expert Consultation** - AIMCODE advisory board (Zhang, Resnick, Reggio, Hassabis, Jobs) + domain experts
5. **Implementation** - Apply findings systematically

**Example Triggers (Any Domain):**
- "Research the best approach for..." (system design, integration, workflow, etc.)
- "Analyze this comprehensively..." (architecture, methodology, process, etc.)
- "Go in depth on..." (any topic requiring deep analysis)
- "What's the best way to..." (design, implement, solve, etc.)
- "Deep dive into..." (any complex topic)
- "Investigate thoroughly..." (problems, solutions, approaches)
- "Design a system for..."
- "Create a methodology for..."
- "Analyze the architecture..."

---

### AIMCODE Ed (Default for Educational Prompts)

**Automatically Applied When:**
- ✅ User requests lesson plans
- ✅ User asks for curriculum materials
- ✅ User wants teacher guides
- ✅ User requests assessments/rubrics
- ✅ User asks for differentiation strategies
- ✅ User wants standards alignment
- ✅ User requests educational content
- ✅ User mentions books, episodes, or teaching

**AIMCODE Ed Framework Applied:**
- **S** - Specify the Role (educational persona)
- **M** - Mention the Purpose (educational goal)
- **A** - Define the Audience (learners)
- **R** - Pedagogical Constraints (Bloom's, standards, AIMCODE principles)
- **T** - Output Format (structure)
- **PED** - Prompt → Evaluate → Develop (iterative refinement)

**Example Triggers:**
- "Create a lesson plan for..."
- "Develop curriculum for..."
- "Write a teacher guide..."
- "Create an assessment..."
- "Design differentiation..."
- "Align to standards..."
- "For Book 1..."
- "For grades 3-5..."

---

## 🔄 FRAMEWORK DETECTION LOGIC

### Step 1: Analyze Prompt Intent

**Check for Educational Keywords:**
- lesson plan, curriculum, teacher guide, assessment, rubric
- grades, students, learners, classroom
- standards (CSTA, Common Core, NGSS)
- book, episode, story (in educational context)
- differentiation, scaffolding, Bloom's

**Check for In-Depth Keywords:**
- research, analyze, investigate, comprehensive
- deep dive, go in depth, thorough
- systematic, methodology, framework
- expert, PhD-level, peer-reviewed
- best approach, optimal solution

### Step 2: Apply Framework

**If Educational Keywords Found:**
→ Apply **AIMCODE Ed** framework automatically

**If In-Depth Keywords Found:**
→ Apply **AIMCODE** methodology automatically

**If Both Found:**
→ Apply **AIMCODE** methodology first, then use **AIMCODE Ed** for educational components

**If Neither Found:**
→ Use standard workflow (no default framework)

### Step 3: User Override

**User Can Override With:**
- "@AIMCODE" - Force AIMCODE methodology
- "@AIMCODE Ed" - Force AIMCODE Ed framework
- "@skip" - Skip default frameworks
- Explicit framework mention in prompt

---

## 📝 USAGE EXAMPLES

### Example 1: Educational Prompt (Auto AIMCODE Ed)

**User Prompt:**
"Create a lesson plan for Book 1, Episode 1, focusing on sequences for grades 3-5"

**AI Behavior:**
- ✅ Automatically applies AIMCODE Ed framework
- Uses S-M-A-R-T-PED structure
- Includes pedagogical constraints
- Applies AIMCODE principles (basketball framework, multiple entry points, etc.)

**Response Structure:**
```
S - Specify the Role: [Educational persona]
M - Mention the Purpose: [Lesson plan for Book 1]
A - Define the Audience: [Grades 3-5]
R - Pedagogical Constraints: [Bloom's, standards, AIMCODE principles]
T - Output Format: [Lesson plan structure]
PED - Refinement: [Iterative improvement]
```

---

### Example 2: In-Depth Prompt - System Design (Auto AIMCODE)

**User Prompt:**
"Research the best approach for integrating game exercises with book content"

**AI Behavior:**
- ✅ Automatically applies AIMCODE methodology (system design/integration work)
- Starts with CLEAR Framework
- Applies Alpha Evolve (systematic layers)
- Conducts PhD-level research
- Consults AIMCODE advisory board + domain experts
- Provides comprehensive analysis

**Response Structure:**
```
CLEAR Framework:
- Clarity: [Clear objectives]
- Logic: [Structured approach]
- Examples: [Relevant examples]
- Adaptation: [Flexibility]
- Results: [Measurable outcomes]

Alpha Evolve:
- Layer 1: [Foundation]
- Layer 2: [Application]
- Layer 3: [Integration]

PhD-Level Research:
- [Citations and research]

Expert Consultation:
- [AIMCODE advisory board insights]
- [Domain experts (system design, integration)]

Implementation:
- [Systematic application]
```

### Example 2b: In-Depth Prompt - Non-Educational (Auto AIMCODE)

**User Prompt:**
"Analyze the best workflow automation approach for our n8n system"

**AI Behavior:**
- ✅ Automatically applies AIMCODE methodology (workflow/system design)
- Uses CLEAR Framework
- Applies Alpha Evolve
- Conducts research on workflow automation
- Consults experts (automation, system design)
- Provides comprehensive analysis

**Note:** This is NOT educational - it's system/workflow design, but AIMCODE still applies because it's comprehensive, in-depth work.

---

### Example 3: Mixed Prompt (AIMCODE + AIMCODE Ed)

**User Prompt:**
"Go in depth on the best way to create curriculum materials for Book 2, including lesson plans and assessments"

**AI Behavior:**
- ✅ Applies AIMCODE methodology for comprehensive analysis
- ✅ Uses AIMCODE Ed for educational components (lesson plans, assessments)
- Combines both frameworks appropriately

**Response Structure:**
```
AIMCODE Methodology:
- CLEAR Framework
- Alpha Evolve
- Research
- Expert Consultation

AIMCODE Ed Components:
- Lesson Plan (S-M-A-R-T-PED)
- Assessment (S-M-A-R-T-PED)
```

---

## 🎯 INTEGRATION WITH "@" COMMANDS

### Default Behavior
- **No "@" command** = Auto-detect and apply appropriate framework
- **"@AIMCODE"** = Force AIMCODE methodology
- **"@AIMCODE Ed"** = Force AIMCODE Ed framework
- **"@skip"** = Skip default frameworks

### "@" Command Priority
1. Explicit "@" command (highest priority)
2. Auto-detection (if no "@" command)
3. Standard workflow (if no match)

---

## 📊 DECISION TREE

```
User Prompt
    │
    ├─ Has "@" command?
    │   ├─ YES → Use specified framework
    │   └─ NO → Continue to detection
    │
    ├─ Has educational keywords?
    │   ├─ YES → Apply AIMCODE Ed
    │   └─ NO → Continue to detection
    │
    ├─ Has in-depth keywords?
    │   ├─ YES → Apply AIMCODE
    │   └─ NO → Standard workflow
    │
    └─ Has both?
        └─ YES → Apply AIMCODE, then AIMCODE Ed for educational parts
```

---

## 🔧 IMPLEMENTATION

### AI Assistant Behavior

**When User Provides Prompt:**

1. **Check for "@" Commands:**
   - If "@AIMCODE" → Apply AIMCODE methodology
   - If "@AIMCODE Ed" → Apply AIMCODE Ed framework
   - If "@skip" → Use standard workflow

2. **If No "@" Command, Auto-Detect:**
   - Scan for educational keywords → Apply AIMCODE Ed
   - Scan for in-depth keywords → Apply AIMCODE
   - If both found → Apply AIMCODE first, then AIMCODE Ed for educational parts
   - If neither found → Use standard workflow

3. **Apply Framework:**
   - Execute framework workflow
   - Provide structured response
   - Include framework elements

4. **User Can Override:**
   - User can say "use AIMCODE Ed instead" or "skip framework"
   - AI adjusts accordingly

---

## 📚 KEYWORDS REFERENCE

### Educational Keywords (Trigger AIMCODE Ed)
- lesson plan, lesson, teaching
- curriculum, curricula
- teacher guide, teacher resource
- assessment, rubric, evaluation
- differentiation, scaffolding
- standards (CSTA, Common Core, NGSS)
- grades, students, learners, classroom
- book, episode, story (educational context)
- Bloom's, taxonomy
- pedagogy, pedagogical

### In-Depth Keywords (Trigger AIMCODE)
- research, analyze, investigation
- comprehensive
- deep dive, go in depth, thorough
- systematic, methodology, framework
- expert, PhD-level, peer-reviewed
- best approach, optimal solution
- comprehensive analysis
- investigate thoroughly
- systematic approach

---

## 🎓 EXAMPLES

### Example 1: Auto AIMCODE Ed
**User:** "Create a lesson plan for Book 1"
**AI:** Applies AIMCODE Ed automatically (S-M-A-R-T-PED)

### Example 2: Auto AIMCODE
**User:** "Research the best integration approach"
**AI:** Applies AIMCODE methodology automatically (CLEAR → Alpha Evolve → Research → Experts)

### Example 3: Explicit Override
**User:** "@AIMCODE Create a lesson plan"
**AI:** Applies AIMCODE methodology (not AIMCODE Ed), then creates lesson plan

### Example 4: Skip Framework
**User:** "@skip Create a lesson plan"
**AI:** Creates lesson plan without framework structure

---

## ✅ BENEFITS

1. **Automatic Application:** No need to remember framework names
2. **Context-Aware:** AI detects appropriate framework
3. **Flexible:** User can override when needed
4. **Consistent:** Same framework for similar prompts
5. **Efficient:** Reduces prompt engineering overhead

---

## 📝 MEMORY SAVING INSTRUCTIONS

**This system should be saved to memory with:**
1. **AIMCODE** = Default for in-depth, comprehensive prompts
2. **AIMCODE Ed** = Default for educational/curriculum prompts
3. **Auto-detection** = AI automatically applies appropriate framework
4. **User override** = "@" commands or explicit mentions override defaults
5. **Integration** = Works seamlessly with existing "@" command system

---

**Version:** 1.0  
**Created:** December 21, 2025  
**Status:** Production System - Active  
**Next Action:** AI Assistant applies these defaults automatically

---

**Copyright © 2025 Rashad West. All Rights Reserved.**

