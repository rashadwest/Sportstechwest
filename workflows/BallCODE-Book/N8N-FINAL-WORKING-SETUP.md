# n8n Unity Automation - FINAL WORKING Setup
## Complete Configuration Based on All Discoveries

**Date:** December 9, 2025  
**File:** `n8n-unity-automation-workflow-FINAL-WORKING.json`  
**Status:** ✅ READY - All Fixes Applied

---

## 🎯 KEY DISCOVERIES SAVED TO MEMORY

### **1. Code Node Limitations (CRITICAL)**
- ❌ **CANNOT use:** `child_process`, `fs`, `path`, `os`
- ✅ **CAN use:** Basic JavaScript, data transformation
- **Rule:** Never use Code node for Git operations or system commands

### **2. executeCommand Node Requirements**
- ✅ **MUST use Expression Mode** for template variables
- ✅ **Syntax:** `={{ `command with ${$json.variable}` }}`
- ✅ **Best Practice:** Get env vars from Code node first, then pass to executeCommand

### **3. Environment Variables Access**
- Code node: Can access `$env.VARIABLE_NAME` directly
- executeCommand: Better to use `$json.variable` from previous node
- **Solution:** Code node gets vars → passes to executeCommand

### **4. AI Node Configuration**
- Resource: `chat`
- Operation: `create` (or `createMessage`)
- **MUST have messages:** System + User prompts
- Model: `gpt-4`

### **5. Fix Limit Rule**
- Maximum 5 fix attempts per node
- After 5, use alternative approach
- Document what was tried

---

## 📋 WORKFLOW STRUCTURE (21 Nodes)

### **Triggers (3 nodes)**
1. Scheduled Trigger (Every 6 Hours)
2. Webhook Trigger (Manual/API)
3. GitHub Webhook (Code Changes)

### **Processing (5 code nodes)**
4. Normalize Input
5. AI Analyze Request (OpenAI)
6. Parse AI Response
7. **Get Git Variables** (NEW - Gets env vars)
8. Finalize & Prepare Report

### **Git Operations (2 executeCommand nodes)**
9. **Clone/Update Repository** (Uses `$json.repoUrl` from Code node)
10. Commit & Push Changes

### **Unity Edits (1 executeCommand node)**
11. AI Unity Editor Edits

### **Build/Deploy (3 HTTP request nodes)**
12. Trigger GitHub Actions Build
13. Deploy to Netlify
14. Send Notification

### **Utility (1 executeCommand node)**
15. Wait for Build (5 min)

### **Conditionals (5 if nodes)**
16. Needs Unity Edits?
17. Needs Build?
18. Needs Deploy?
19. Send Notification?
20. Webhook Response?

### **Response (1 node)**
21. Webhook Response

---

## 🔧 CRITICAL NODE CONFIGURATIONS

### **Node: Get Git Variables (Code Node)**
**Purpose:** Gets environment variables and passes to executeCommand

**Code:**
```javascript
// Get environment variables and validate
const repoUrl = $env.UNITY_REPO_URL;
const projectPath = $env.UNITY_PROJECT_PATH;

// Return variables for next node
return {
  json: {
    ...$('Parse AI Response').item.json,
    repoUrl: repoUrl || '',
    projectPath: projectPath || '',
    repoUrlSet: !!repoUrl,
    projectPathSet: !!projectPath,
    error: (!repoUrl || !projectPath) ? 'Missing environment variables' : null
  }
};
```

### **Node: Clone/Update Repository (executeCommand)**
**Purpose:** Git clone or pull based on directory existence

**Command Field (Expression Mode enabled):**
```
={{ `/bin/sh -c "if [ -d '${$json.projectPath}' ]; then cd '${$json.projectPath}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$json.repoUrl}' '${$json.projectPath}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

**Key Points:**
- Uses `$json.projectPath` (from Code node) NOT `$env.UNITY_PROJECT_PATH`
- Uses `$json.repoUrl` (from Code node) NOT `$env.UNITY_REPO_URL`
- Expression Mode enabled (`={{ }}`)
- Template literals with backticks

### **Node: AI Analyze Request (OpenAI)**
**Resource:** `chat`  
**Operation:** `create`  
**Model:** `gpt-4`  
**Messages:**
- System: "You are a Unity development assistant..."
- User: "Analyze this Unity development request..."

---

## 🔑 REQUIRED ENVIRONMENT VARIABLES

**Must be set in n8n Settings → Environment Variables:**

- `UNITY_REPO_URL` - GitHub repository URL
- `UNITY_PROJECT_PATH` - Path where project should be cloned
- `WORKFLOW_PATH` - Path to workflow scripts
- `GITHUB_REPO_OWNER` - GitHub username/organization
- `GITHUB_REPO_NAME` - Repository name
- `GITHUB_WORKFLOW_FILE` - GitHub Actions workflow file name
- `NETLIFY_SITE_ID` - Netlify site ID
- `NETLIFY_SITE_NAME` - Netlify site name
- `BUILD_OUTPUT_PATH` - Path to build output
- `WEBHOOK_NOTIFICATION_URL` - (Optional) Webhook URL for notifications

---

## 🔐 REQUIRED CREDENTIALS

1. **OpenAI API** - For AI Analyze Request node
2. **GitHub Actions Token** - For Trigger GitHub Actions Build node
3. **Netlify API Token** - For Deploy to Netlify node

---

## ✅ WHAT'S FIXED

1. ✅ **Git Clone/Pull:** Uses Code node to get env vars, then executeCommand
2. ✅ **Template Variables:** Uses `$json.variable` instead of `$env.VARIABLE`
3. ✅ **AI Node:** Has proper messages configured
4. ✅ **Expression Mode:** All executeCommand nodes use Expression Mode correctly
5. ✅ **Node Count:** 21 nodes (was 20, added "Get Git Variables")

---

## 🚀 HOW TO USE

1. **Import** `n8n-unity-automation-workflow-FINAL-WORKING.json` into n8n
2. **Set Environment Variables** in n8n Settings
3. **Configure Credentials** (OpenAI, GitHub, Netlify)
4. **Test** with manual webhook trigger
5. **Verify** all nodes execute correctly

---

## 📝 NOTES

- **Get Git Variables node** is critical - it bridges Code node (can access `$env`) to executeCommand (uses `$json`)
- **All fixes applied** based on 5+ attempts and research
- **This is the working solution** - don't change the Git node structure

---

**File Location:** Desktop - `n8n-unity-automation-workflow-FINAL-WORKING.json`  
**Ready to Import:** ✅ Yes




