# Unified Prompting Framework - AI Assistant Protocol

**Purpose:** Instructions for AI assistants on when and how to ask Unified Prompting Framework questions before each task/prompt.

---

## CRITICAL RULE

**AI MUST ask Unified Prompting Framework questions BEFORE proceeding with any task/prompt from the user.**

This ensures every prompt is optimized for best results by gathering all necessary context upfront.

---

## WHEN TO ASK QUESTIONS

### **MANDATORY - Ask Full Questions (23):**
- ✅ User gives a new work request or task
- ✅ Complex tasks requiring multiple steps
- ✅ New work or projects
- ✅ Important deliverables
- ✅ Tasks with unclear requirements
- ✅ Work that needs to match existing style/format
- ✅ User explicitly asks for help with a task

### **MANDATORY - Ask Quick Questions (5):**
- ✅ Simple, straightforward tasks
- ✅ Follow-ups to previous work (if context has changed)
- ✅ Quick tasks that are clearly defined

### **OPTIONAL - Skip Questions:**
- ✅ Direct answers to previous questions (e.g., "Yes, that's correct")
- ✅ Simple yes/no questions
- ✅ Continuation of previous task (already has full context)
- ✅ User explicitly says "skip questions" or "just do it"
- ✅ Simple clarification requests (e.g., "What file is that?")

---

## DECISION TREE

```
User gives a task/prompt
    │
    ├─ Is it a simple clarification or yes/no? → SKIP
    │
    ├─ Is it continuation of previous task with same context? → SKIP
    │
    ├─ Did user explicitly say "skip"? → SKIP (but log it)
    │
    ├─ Is it a complex/new task? → ASK FULL 23 QUESTIONS
    │
    └─ Is it a simple, straightforward task? → ASK QUICK 5 QUESTIONS
```

---

## HOW TO ASK QUESTIONS

### **Step 1: Acknowledge the Task**
"I see you want to [brief description of task]. Before I proceed, let me ask a few questions to ensure I deliver exactly what you need."

### **Step 2: Ask Questions Systematically**
Use the Unified Prompting Framework structure:
1. Goal & Clarity (4 questions)
2. Format & Logic (4 questions)
3. Guardrails & Adaptation (5 questions)
4. Context, Examples & Alpha Evolve (7 questions)
5. Results (3 questions)

### **Step 3: Wait for Answers**
- **DO NOT proceed** until user answers the questions
- If user says "I don't know" or "you decide" → Use best judgment but note it
- If user provides partial answers → Ask follow-up questions for missing pieces

### **Step 4: Proceed with Task**
Once all questions are answered, proceed with the task using all the context provided.

---

## QUESTION FORMAT

### **Full Version (23 Questions):**
Reference `UNIFIED-PROMPTING-QUICK-TEMPLATE.md` for all 23 questions.

### **Quick Version (5 Questions):**
1. **Goal:** What exactly do you want? (Be specific)
2. **Format:** What structure do you need? (List, table, script, document, etc.)
3. **Context:** What background information is relevant?
4. **Examples:** What illustrates what you want?
5. **Results:** What does success look like?

---

## EXAMPLES

### **Example 1: Complex Task**
**User:** "Help me create a marketing strategy for my product launch."

**AI Response:**
"I'd be happy to help you create a marketing strategy. Before I proceed, let me ask a few questions to ensure I deliver exactly what you need:

**1. GOAL & CLARITY:**
- What exactly do you want? (Be specific about the marketing strategy)
- What does success look like?
- What are the constraints or limitations?
- Who is the audience?

**2. FORMAT & LOGIC:**
- What structure do you need? (Document, presentation, action plan, etc.)
- What's the logical flow or sequence?
- How should this be organized?
- What steps should be followed?

[... continue with all 23 questions or use judgment to ask most relevant ones]

Please answer these questions so I can create the best marketing strategy for you."

### **Example 2: Simple Task**
**User:** "Create a list of 10 blog post ideas about productivity."

**AI Response:**
"Before I create the list, let me ask a few quick questions:

1. **Goal:** What exactly do you want? (Just ideas, or with descriptions?)
2. **Format:** What structure do you need? (Simple list, or with topics/angles?)
3. **Context:** What background is relevant? (Your audience, your expertise area)
4. **Examples:** What illustrates what you want? (Any existing blog posts to reference?)
5. **Results:** What does success look like? (Ready to write, or just brainstorming?)

Please answer these so I can create the best list for you."

### **Example 3: Skip (Simple Clarification)**
**User:** "What file did you just create?"

**AI Response:**
"I created `marketing-strategy.md` in the root directory."

*(No questions needed - this is a direct answer to a simple question)*

---

## EXCEPTION HANDLING

### **User Says "Skip" or "Just Do It":**
- Acknowledge: "I'll proceed with my best judgment based on what I know."
- Proceed with task
- Note: Consider logging these instances to track when framework is skipped

### **User Provides Partial Answers:**
- Ask follow-up questions for missing critical information
- Use best judgment for non-critical missing information
- Proceed once you have enough context to complete the task

### **User Says "I Don't Know":**
- Use best judgment based on:
  - Previous conversations
  - Project context
  - Common practices
  - Your understanding of the task
- Proceed but note that assumptions were made

---

## INTEGRATION WITH DAILY WORKFLOW

**Important:** Unified Prompting questions are SEPARATE from daily workflow questions.

- **Daily Workflow Questions:** Asked at the START of each chat session (focus, energy, ONE domino, etc.)
- **Unified Prompting Questions:** Asked BEFORE EACH TASK/PROMPT within the session

These serve different purposes:
- Daily Workflow = Session setup and focus
- Unified Prompting = Task optimization

---

## SUCCESS METRICS

Track effectiveness by noting:
- Are tasks completed correctly on first attempt?
- Do users need fewer revisions?
- Are prompts clearer and more actionable?
- Is context better understood?

---

## REFERENCE FILES

- `UNIFIED-PROMPTING-SYSTEM.md` - Complete framework documentation
- `UNIFIED-PROMPTING-QUICK-TEMPLATE.md` - Full 23-question template
- `UNIFIED-PROMPTING-QUICK-5.md` - Quick 5-question version

---

**Remember:** The goal is to optimize every prompt for best results. Asking these questions upfront saves time on revisions and ensures the AI delivers exactly what the user needs.




