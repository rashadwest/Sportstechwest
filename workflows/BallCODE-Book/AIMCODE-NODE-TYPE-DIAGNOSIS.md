# AIMCODE Diagnosis: Node Type Mismatch Issue
## CLEAR → Alpha Evolve → Research → Experts → Solution

**Date:** December 9, 2025  
**Issue:** JavaScript code being executed as shell command  
**Error:** `/bin/sh: syntax error: unexpected "("`  
**Root Cause:** Node type is executeCommand, not Code node

---

## CLEAR Framework

### C - Clarity
**Problem:** Error shows JavaScript code is being run as shell command  
**Error Message:** `/bin/sh: syntax error: unexpected "("`  
**Root Cause:** Node is still `executeCommand` type, not `Code` type  
**Evidence:** Error shows entire JavaScript code being passed to `/bin/sh`

### L - Logic
**Issue Analysis:**
1. JavaScript code was provided
2. But node type is still `executeCommand`
3. executeCommand expects shell commands, not JavaScript
4. n8n is trying to run JavaScript as shell script → fails

### E - Examples
**Correct Node Types:**
- `executeCommand` → Uses shell commands (bash, git, etc.)
- `Code` → Uses JavaScript/Node.js code

### A - Adaptation
**Solution Options:**
1. Change node type to Code (recommended)
2. Or use proper shell commands in executeCommand

### R - Results
**Success Criteria:**
- Node executes without errors
- Git operations work correctly
- No shell syntax errors

---

## Alpha Evolve (Layer-by-Layer Diagnosis)

### Layer 1: Error Analysis
- Error: `/bin/sh: syntax error: unexpected "("`
- This means shell is trying to parse JavaScript code
- JavaScript `const`, `require()`, `()` syntax is invalid in shell

### Layer 2: Node Type Check
- Current: executeCommand node
- Needed: Code node for JavaScript
- Mismatch: JavaScript code in shell command node

### Layer 3: Solution Path
- Option A: Change to Code node (use JavaScript)
- Option B: Keep executeCommand (use shell commands)

### Layer 4: Implementation
- Verify node type in n8n UI
- Apply correct solution based on node type

---

## Research Findings

**n8n Node Types:**
- **executeCommand:** Executes system commands (shell scripts)
- **Code:** Executes JavaScript/Node.js code
- **Cannot mix:** JavaScript code won't work in executeCommand

**Common Issues:**
- Users often confuse node types
- executeCommand nodes get stuck with complex commands
- Code nodes more reliable for git operations in n8n

**Best Practices:**
- Use Code node for complex logic
- Use executeCommand for simple shell commands
- Git operations often work better in Code nodes

---

## Expert Consultation

### Hassabis (Systematic)
- Diagnose systematically: Error → Root Cause → Solution
- Verify node type before applying fix

### Jobs (Simplicity)
- Simplest solution: Use Code node for JavaScript
- Clear separation: Shell commands vs JavaScript

---

## SOLUTION

### **The Problem:**
Your node is still an **executeCommand** node, but you're trying to use **JavaScript code**. These don't mix!

### **Solution 1: Change to Code Node (RECOMMENDED)**

**Steps:**
1. **Delete** the current "Clone/Update Repository" node
2. **Add** a new **Code** node (not executeCommand)
3. **Name it:** "Clone/Update Repository"
4. **Paste the JavaScript code** I provided earlier
5. **Save** and test

**How to tell if it's a Code node:**
- Icon looks like `</>` or `>_` (code symbol)
- Has "JavaScript Code" field, not "Command" and "Arguments" fields

---

### **Solution 2: Use Shell Commands in executeCommand**

If you want to keep executeCommand node, use this **shell command** instead:

**Command:** `/bin/sh`

**Arguments (with Expression Mode enabled):**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## VERIFICATION CHECKLIST

**Before testing, verify:**
- [ ] Node type is correct (Code for JavaScript, executeCommand for shell)
- [ ] If Code node: JavaScript code is in "JavaScript Code" field
- [ ] If executeCommand: Shell command is in "Command" and "Arguments" fields
- [ ] Environment variables are set in n8n
- [ ] Node is connected properly in workflow

---

## RECOMMENDED ACTION

**Use Solution 1 (Code Node):**
1. Delete executeCommand node
2. Add Code node
3. Paste JavaScript code
4. This is more reliable and won't get stuck

**The error proves the node type is wrong - fix that first!**
