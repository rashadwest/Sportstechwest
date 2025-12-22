# AIMCODE Final Fix: Git Node - Saved to Memory
## Critical Learning: n8n Code Node Limitations

**Date:** December 9, 2025  
**Issue:** Cannot find module 'child_process' in n8n Code node  
**Status:** ✅ DIAGNOSED - VM2 Sandbox Restriction  
**Fix Attempt:** #5 (Final - Will use alternative if this fails)

---

## CLEAR Framework

### C - Clarity
**Problem:** `Cannot find module 'child_process'` in n8n Code node  
**Root Cause:** n8n Code node runs in VM2 sandbox that restricts Node.js built-in modules for security  
**Solution:** Use n8n's built-in Git node OR executeCommand with proper syntax

### L - Logic
**Why child_process doesn't work:**
- n8n Code node uses VM2 sandbox
- Security restrictions block `child_process`, `fs`, `path` modules
- Need to use n8n's built-in nodes or executeCommand

### E - Examples
**Working Solutions:**
1. n8n built-in Git node (if available)
2. executeCommand node with proper syntax
3. HTTP Request to external script

### A - Adaptation
**Constraint:** Must work within n8n's security model  
**Flexibility:** Will use alternative approach if this fails

### R - Results
**Success Criteria:**
- Node executes without module errors
- Git clone/pull operations work
- No more than 5 fix attempts per node

---

## Alpha Evolve (Layer-by-Layer)

### Layer 1: Understand Restriction
- VM2 sandbox blocks Node.js modules
- Code node has limited capabilities

### Layer 2: Find Alternative
- Use executeCommand (native shell access)
- Or use built-in Git node

### Layer 3: Implement Solution
- ExecuteCommand with correct syntax
- Proper error handling

### Layer 4: Test & Document
- Verify it works
- Save to memory for future

---

## Research

**n8n VM2 Sandbox Restrictions:**
- Blocks: `child_process`, `fs`, `path`, `os` modules
- Allows: Basic JavaScript, some built-in functions
- Purpose: Security - prevent arbitrary code execution

**Working Solutions:**
1. **executeCommand node** - Has native shell access
2. **Git node** - Built-in n8n node for Git operations
3. **HTTP Request** - Call external API/script

---

## Expert Consultation

### Hassabis (Systematic)
- Understand the constraint first
- Then find solution that works within constraint
- Don't fight the system - work with it

### Jobs (Simplicity)
- Use the simplest solution that works
- Built-in nodes are better than custom code

---

## SOLUTION: Use executeCommand Node (Not Code Node)

**The Code node CANNOT use child_process. Use executeCommand instead.**

### **Node Type:** executeCommand (NOT Code)

### **Command:** `git`

### **Arguments (Simple - No Expression Mode needed):**
```
clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)
```

**OR if that doesn't work, try with Expression Mode:**

**Command:** `git`  
**Arguments (with Expression Mode):**
```
={{ `clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || (cd '${$env.UNITY_PROJECT_PATH}' && git pull)` }}
```

---

## ALTERNATIVE: Use n8n Built-in Git Node

If executeCommand still doesn't work, check if n8n has a built-in Git node:

1. **Add Node** → Search "Git"
2. **If Git node exists:**
   - Use "Clone" operation for new repos
   - Use "Pull" operation for existing repos
   - Configure repository URL and path

---

## MEMORY: Key Learnings

### **n8n Code Node Limitations:**
- ❌ Cannot use `child_process`
- ❌ Cannot use `fs` (file system)
- ❌ Cannot use `path`
- ❌ Cannot use `os`
- ✅ Can use basic JavaScript
- ✅ Can use `require()` for some modules (limited)

### **When to Use Each Node:**
- **Code Node:** Simple data transformation, calculations, logic
- **executeCommand Node:** Shell commands, git operations, system commands
- **Built-in Nodes:** Always prefer built-in nodes (Git, HTTP, etc.)

### **Fix Limit Rule:**
- Maximum 5 fix attempts per node
- After 5 attempts, consider alternative approach
- Document what was tried for future reference

---

## IMPLEMENTATION

### Step 1: Delete Code Node
- Remove the Code node that's failing

### Step 2: Add executeCommand Node
- Add new "Execute Command" node
- Name: "Clone/Update Repository"

### Step 3: Configure
- **Command:** `git`
- **Arguments:** `clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)`

### Step 4: Test
- Save and execute
- Should work without module errors

---

**This is the final fix attempt. If this doesn't work, we'll use the built-in Git node or HTTP Request alternative.**



