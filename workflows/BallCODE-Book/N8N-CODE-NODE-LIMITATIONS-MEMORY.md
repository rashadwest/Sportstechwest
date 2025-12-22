# n8n Code Node Limitations - Saved to Memory
## Critical Knowledge for Future Efficiency

**Date:** December 9, 2025  
**Purpose:** Prevent repeating failed attempts  
**Status:** ✅ DOCUMENTED - Do Not Use Code Node for Git Operations

---

## 🚨 CRITICAL RULE: Fix Limit

**Maximum 5 fix attempts per node before considering alternatives.**

**After 5 attempts:**
- Document what was tried
- Consider alternative approach
- Use different node type
- Use external service/API

---

## ❌ n8n Code Node CANNOT Use:

### **Blocked Modules:**
- `child_process` - ❌ Cannot execute shell commands
- `fs` - ❌ Cannot access file system
- `path` - ❌ Cannot use path operations
- `os` - ❌ Cannot access OS functions
- Most Node.js built-in modules

### **Why:**
- n8n Code node runs in VM2 sandbox
- Security restrictions prevent arbitrary code execution
- Designed for data transformation, not system operations

---

## ✅ What Code Node CAN Do:

- Basic JavaScript operations
- Data transformation
- Calculations
- Logic/conditionals
- Some `require()` modules (limited)

---

## ✅ Use These Nodes Instead:

### **For Git Operations:**
1. **executeCommand Node** - Has native shell access
2. **Git Node** (if available) - Built-in n8n node
3. **HTTP Request Node** - Call external API/script

### **For File Operations:**
1. **executeCommand Node** - Shell commands
2. **HTTP Request Node** - External file service

### **For System Operations:**
1. **executeCommand Node** - Direct shell access
2. **HTTP Request Node** - External service

---

## 📝 Git Clone/Pull Working Solution

### **Node Type:** executeCommand

### **Command:** `git`

### **Arguments (Simple Template Syntax):**
```
clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)
```

**Why This Works:**
- executeCommand has native shell access
- Template variables `{{ }}` work in executeCommand
- No Expression Mode needed for simple cases
- Direct git command execution

---

## 🔄 Alternative Solutions (If executeCommand Fails)

### **Option 1: Split Into Two Nodes**
- Node 1: Check if directory exists (Code node - just logic)
- Node 2A: Git clone (executeCommand)
- Node 2B: Git pull (executeCommand)
- Use IF node to route

### **Option 2: Use Built-in Git Node**
- Search for "Git" node in n8n
- Use Clone operation
- Use Pull operation

### **Option 3: External Script**
- Create Python/Bash script
- Call via HTTP Request
- Script handles git operations

### **Option 4: Skip Git Operations**
- Use GitHub API to trigger actions
- Let GitHub Actions handle clone/pull
- n8n just triggers the workflow

---

## 📊 Fix Attempt History (This Node)

1. ✅ **Attempt 1:** executeCommand with Expression Mode - Template variable issues
2. ✅ **Attempt 2:** executeCommand with `/bin/sh -c` - Quote escaping issues
3. ✅ **Attempt 3:** Code node with child_process - Module not found
4. ✅ **Attempt 4:** Code node with clean quotes - Still module not found
5. ✅ **Attempt 5:** executeCommand with simple template syntax - **CURRENT**

**If Attempt 5 fails:** Use Alternative Solution (Git node or HTTP Request)

---

## 🎯 Decision Tree for Future

### **Need to execute shell commands?**
- ❌ Don't use Code node
- ✅ Use executeCommand node

### **Need file system access?**
- ❌ Don't use Code node
- ✅ Use executeCommand node

### **Need Git operations?**
- ❌ Don't use Code node
- ✅ Use executeCommand or Git node

### **Need data transformation?**
- ✅ Use Code node
- ✅ Works perfectly for this

---

## 💡 Key Takeaway

**Code Node = Data Processing**  
**executeCommand Node = System Operations**

**Never use Code node for:**
- Git operations
- File system operations
- Shell commands
- System calls

**Always use executeCommand for:**
- Git clone/pull
- File operations
- Shell scripts
- System commands

---

**This is now saved to memory. Future fixes will reference this document.**



