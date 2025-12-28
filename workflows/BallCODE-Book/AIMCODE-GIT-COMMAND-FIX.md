# AIMCODE Solution: Fix n8n Git Clone/Pull Command
## CLEAR Framework → Alpha Evolve → Research → Experts → Solution

**Date:** December 9, 2025  
**Issue:** Git clone/pull command not working in n8n executeCommand node  
**Methodology:** AIMCODE

---

## CLEAR Framework

### C - Clarity
**Problem:** Template variables `{{ $env.UNITY_REPO_URL }}` not expanding in executeCommand arguments  
**Current Command:** `git clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} 2>/dev/null || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)`  
**Expected:** Variables expand, command executes successfully  
**Actual:** Variables not expanding, command fails

### L - Logic
**Root Cause:** n8n executeCommand arguments field needs Expression Mode (`=`) to expand template variables  
**Solution Path:** Use shell script with Expression Mode for variable expansion

### E - Examples
**Previous Fix:** We fixed similar issue with `/bin/sh -c` and Expression Mode  
**Working Pattern:** `={{ `-c "command with ${$env.VAR}"` }}`

### A - Adaptation
**Constraints:** Must work in n8n executeCommand node  
**Flexibility:** Can use bash or sh, can use different error handling

### R - Results
**Success Criteria:**
- Template variables expand correctly
- Git clone works if directory doesn't exist
- Git pull works if directory exists
- Command doesn't fail silently

---

## Alpha Evolve (Layer-by-Layer Solution)

### Layer 1: Basic Shell Command
Use `/bin/sh` or `bash` with `-c` flag to execute script

### Layer 2: Expression Mode
Wrap arguments in `={{ }}` to enable template variable expansion

### Layer 3: Template Literals
Use backticks for string interpolation: `` `${$env.VAR}` ``

### Layer 4: Error Handling
Add proper error handling for git operations

---

## Research

**Previous Solutions:**
- We fixed template variable expansion using Expression Mode
- Working pattern: `={{ `-c "script"` }}`
- Template variables need `${$env.X}` syntax inside template literals

**n8n Documentation:**
- executeCommand arguments need Expression Mode for template expansion
- Use `=` prefix to enable expression evaluation

---

## Expert Consultation

### Hassabis (Systematic)
- Build solution systematically: Shell → Expression → Variables → Error Handling
- Ensure each layer is correct before moving to next

### Jobs (Simplicity)
- Keep command simple and readable
- Use clear error messages

---

## SOLUTION

### **Option 1: Using Expression Mode with Shell Script (RECOMMENDED)**

**Command:** `/bin/sh`  
**Arguments:**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

**Why This Works:**
- `={{ }}` enables Expression Mode
- Backticks create template literal for string interpolation
- `${$env.X}` expands environment variables
- Proper error handling with `|| { echo; exit 1; }`

---

### **Option 2: Simpler Git Command (If Option 1 Doesn't Work)**

**Command:** `git`  
**Arguments:**
```
={{ `clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' 2>/dev/null || (cd '${$env.UNITY_PROJECT_PATH}' && git pull)` }}
```

**Why This Works:**
- Direct git command (no shell wrapper)
- Expression Mode for variable expansion
- Fallback to pull if clone fails

---

### **Option 3: Using Bash (If sh Not Available)**

**Command:** `bash`  
**Arguments:**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## IMPLEMENTATION

### Step 1: Update Node Configuration

1. **Click on "Clone/Update Repository" node**
2. **In Parameters tab:**
   - **Command:** Change to `/bin/sh`
   - **Arguments:** Click the **Expression** toggle (or type `=`)
   - **Paste Option 1 code above**

### Step 2: Test

1. **Save** the workflow
2. **Execute** the node
3. **Check output** for success or error messages

---

## VERIFICATION

**Command works when:**
- ✅ Template variables expand (no `{{ }}` in error messages)
- ✅ Git clone succeeds if directory doesn't exist
- ✅ Git pull succeeds if directory exists
- ✅ Error messages are clear if something fails

---

## TROUBLESHOOTING

**If variables still don't expand:**
- Make sure Expression Mode is enabled (`=` prefix)
- Check that environment variables are set in n8n
- Verify variable names match exactly

**If command fails:**
- Check git is installed in n8n environment
- Verify repository URL is correct
- Check file permissions for project path

---

**Recommended Solution:** Use **Option 1** - most reliable and has proper error handling




