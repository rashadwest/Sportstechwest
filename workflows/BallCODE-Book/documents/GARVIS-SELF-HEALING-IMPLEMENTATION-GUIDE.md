# 🤖 Garvis Self-Healing System - Complete Implementation Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Status:** ✅ Complete System Ready for Implementation  
**Methodology:** AIMCODE (CLEAR → Alpha Evolve → Research → Experts)

---

## 🎯 OVERVIEW

**Garvis Self-Healing System** automatically detects, diagnoses, and fixes common n8n workflow errors, reducing manual intervention and improving system reliability.

### Key Features:
- ✅ **Automatic Error Detection** - Monitors workflow executions every 5 minutes
- ✅ **Intelligent Diagnosis** - Identifies root causes and generates fix plans
- ✅ **Auto-Fix Capabilities** - Fixes common errors automatically (with high confidence)
- ✅ **Verification System** - Confirms fixes worked
- ✅ **Notification System** - Reports what was fixed
- ✅ **Manual Review Queue** - Flags errors requiring human attention

---

## 📁 FILES CREATED

### 1. **n8n Workflow**
- `n8n-garvis-self-healing-workflow.json` - Main self-healing workflow

### 2. **Python Scripts**
- `scripts/garvis-auto-fix.py` - Auto-fix implementation

### 3. **Configuration**
- `scripts/garvis-error-patterns.json` - Error patterns and fix definitions

### 4. **Documentation**
- `documents/GARVIS-SELF-HEALING-IMPLEMENTATION-GUIDE.md` - This file
- `documents/N8N-WORKFLOW-ERRORS-AIMCODE-FIX.md` - Complete solutions

---

## 🚀 QUICK START (5 Minutes)

### Step 1: Import Workflow (2 minutes)

1. **Open n8n:** http://192.168.1.226:5678
2. **Click:** Workflows → Import from File
3. **Select:** `n8n-garvis-self-healing-workflow.json`
4. **Click:** Import

### Step 2: Configure Environment Variables (2 minutes)

**In n8n Settings → Environment Variables, add:**

```bash
N8N_URL=http://192.168.1.226:5678
N8N_API_KEY=your-n8n-api-key-here  # Optional - for API authentication
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
NOTIFICATION_WEBHOOK_URL=your-webhook-url  # Optional - for notifications
```

### Step 3: Set Up n8n API Key (1 minute)

**If you want API authentication:**

1. **In n8n:** Settings → API
2. **Create API Key** (or use existing)
3. **Add to environment variables:** `N8N_API_KEY`

**Note:** If no API key, the system will work but may have limited access to some operations.

### Step 4: Make Python Script Executable

```bash
chmod +x scripts/garvis-auto-fix.py
```

### Step 5: Activate Workflow

1. **In n8n:** Open "Garvis Self-Healing System" workflow
2. **Toggle:** Active (top-right)
3. **Verify:** Workflow is running (green indicator)

---

## 🔧 CONFIGURATION

### Error Patterns

**Edit:** `scripts/garvis-error-patterns.json`

**Add new error patterns:**
```json
{
  "yourErrorType": {
    "pattern": "your error pattern regex",
    "severity": "low|medium|high|critical",
    "fixable": true|false,
    "fixType": "credential|requestBody|network|rateLimit",
    "fixAction": "yourFixAction",
    "fixParams": {
      "param1": "value1"
    }
  }
}
```

### Fix Actions

**Edit:** `scripts/garvis-auto-fix.py`

**Add new fix action:**
```python
def your_fix_action(diagnosis, workflow_id, api_key):
    # Your fix logic here
    return {
        "success": True,
        "message": "Fix applied successfully"
    }
```

**Then add to `apply_fix()` function:**
```python
elif action == "yourFixAction":
    result = your_fix_action(diagnosis, workflow_id, api_key)
```

---

## 📊 HOW IT WORKS

### Flow Diagram

```
1. Monitor Executions (Every 5 min)
   ↓
2. Define Error Patterns
   ↓
3. Get Recent Executions (n8n API)
   ↓
4. Detect Errors (Match patterns)
   ↓
5. Has Errors? → Yes
   ↓
6. Diagnose Errors (Identify root cause + fix plan)
   ↓
7. Can Auto-Fix? → Yes (confidence > 0.7, fixable = true)
   ↓
8. Apply Auto-Fixes (Python script)
   ↓
9. Verify Fixes (Check if errors resolved)
   ↓
10. Send Notification (Report results)
```

### Error Detection

**Pattern Matching:**
- Scans execution error messages
- Matches against defined patterns
- Extracts error type, severity, fixability

**Example:**
```
Error: "Header name must be a valid HTTP token ["BalICODE n8n"]"
→ Matches: headerError pattern
→ Severity: high
→ Fixable: true
→ Fix Type: credential
```

### Diagnosis

**Root Cause Analysis:**
- Identifies likely cause
- Generates fix plan
- Calculates confidence score (0.0 - 1.0)

**Example:**
```
Error Type: headerError
Likely Cause: Invalid header name in credential (contains spaces)
Fix: updateCredentialHeaderName
  - credentialId: (extracted from workflow)
  - correctValue: "Authorization"
Confidence: 0.9
```

### Auto-Fix

**Fix Application:**
- Fetches workflow/credential from n8n API
- Applies fix (updates credential, fixes request body, etc.)
- Updates workflow/credential via API
- Returns success/failure

**Example:**
```
Action: updateCredentialHeaderName
1. Get workflow → Find node → Get credential ID
2. Get credential → Update header name to "Authorization"
3. Update credential via API
4. Return: success = true
```

### Verification

**Fix Verification:**
- Re-checks execution status
- Verifies error is resolved
- Reports success/failure

---

## 🛠️ CUSTOMIZATION

### Add New Error Pattern

**1. Edit `scripts/garvis-error-patterns.json`:**

```json
{
  "yourNewError": {
    "pattern": "your regex pattern",
    "severity": "high",
    "fixable": true,
    "fixType": "requestBody",
    "fixAction": "yourFixAction",
    "fixParams": {
      "param": "value"
    }
  }
}
```

**2. Update `Define Error Patterns` node in workflow:**

Add your pattern to the `errorPatterns` object in the Code node.

**3. Add fix action in `Diagnose Errors` node:**

```javascript
case 'yourNewError':
  diagnosis.likelyCause = 'Your description';
  diagnosis.fix = {
    action: 'yourFixAction',
    // ... fix params
  };
  break;
```

**4. Implement fix in `scripts/garvis-auto-fix.py`:**

```python
elif action == "yourFixAction":
    # Your fix logic
    result["success"] = True
```

### Modify Monitoring Frequency

**Edit workflow trigger:**
- Open workflow
- Click "Monitor Executions" node
- Change cron expression:
  - Every 5 min: `*/5 * * * *`
  - Every 10 min: `*/10 * * * *`
  - Every hour: `0 * * * *`

### Add Notification Channel

**Edit "Send Notification" node:**
- Change URL to your webhook/API
- Modify JSON body format
- Add email, Slack, Discord, etc.

---

## 🧪 TESTING

### Test Error Detection

**1. Create test error:**
- Manually trigger a workflow with known error
- Wait for self-healing system to detect it

**2. Check detection:**
- Open "Garvis Self-Healing System" workflow
- Check "Detect Errors" node output
- Verify error is detected

### Test Auto-Fix

**1. Create fixable error:**
- Set credential header name to invalid value (e.g., "BalICODE n8n")
- Trigger workflow
- Wait for self-healing to fix it

**2. Verify fix:**
- Check credential in n8n
- Verify header name is now "Authorization"
- Check "Verify Fixes" node output

### Test Manual Review Queue

**1. Create non-fixable error:**
- Remove a credential entirely
- Trigger workflow
- Check "Log Manual Review" node output

---

## 📈 MONITORING

### Check System Status

**1. View workflow executions:**
- Open "Garvis Self-Healing System" workflow
- Click "Executions" tab
- Review recent executions

**2. Check fix results:**
- Look at "Verify Fixes" node output
- Review success/failure counts
- Check notification messages

### Metrics to Track

- **Errors Detected:** Count of errors found
- **Fixes Applied:** Count of fixes attempted
- **Success Rate:** Percentage of successful fixes
- **Manual Reviews:** Count of errors requiring human attention

---

## 🔒 SECURITY

### API Key Security

**Best Practices:**
- Store API keys in environment variables (not in code)
- Use read-only API keys when possible
- Rotate API keys regularly
- Limit API key permissions

### Credential Access

**The system needs:**
- Read access to workflows
- Read/Write access to credentials (for fixes)
- Read access to executions

**Recommendation:** Create dedicated API key with minimal required permissions.

---

## 🐛 TROUBLESHOOTING

### System Not Detecting Errors

**Check:**
1. Workflow is active
2. "Monitor Executions" trigger is running
3. n8n API is accessible
4. API key is valid (if using authentication)

### Fixes Not Applying

**Check:**
1. Python script is executable: `chmod +x scripts/garvis-auto-fix.py`
2. Script path is correct in workflow
3. API key has write permissions
4. Credential/workflow IDs are correct

### False Positives

**Adjust:**
1. Error pattern regex (make more specific)
2. Confidence threshold (increase from 0.7 to 0.8+)
3. Fixable flag (set to false for uncertain fixes)

---

## 📚 REFERENCE

### Error Pattern Format

```json
{
  "errorType": {
    "pattern": "regex pattern (case insensitive)",
    "severity": "low|medium|high|critical",
    "fixable": true|false,
    "fixType": "credential|requestBody|network|rateLimit",
    "fixAction": "action name",
    "fixParams": {
      "param": "value"
    }
  }
}
```

### Fix Action Format

```python
def fix_action(diagnosis, workflow_id, api_key):
    return {
        "success": True|False,
        "message": "Description of what was done",
        "error": None or error message
    }
```

### Diagnosis Format

```json
{
  "errorType": "headerError",
  "errorMessage": "Full error message",
  "severity": "high",
  "fixable": true,
  "fixType": "credential",
  "workflowId": "workflow-id",
  "workflowName": "Workflow Name",
  "nodeName": "Node Name",
  "executionId": "execution-id",
  "likelyCause": "Description",
  "fix": {
    "action": "updateCredentialHeaderName",
    "credentialId": "credential-id",
    "correctValue": "Authorization"
  },
  "confidence": 0.9
}
```

---

## ✅ SUCCESS CRITERIA

- [ ] Workflow imported and activated
- [ ] Environment variables configured
- [ ] Python script is executable
- [ ] System detects errors automatically
- [ ] System applies fixes for high-confidence errors
- [ ] System verifies fixes worked
- [ ] Notifications are sent
- [ ] Manual review queue works for non-fixable errors

---

## 🎯 NEXT STEPS

1. **Import workflow** - Get it running
2. **Test with known errors** - Verify it works
3. **Customize patterns** - Add your specific error patterns
4. **Monitor results** - Track success rate
5. **Iterate** - Improve based on results

---

## 📝 NOTES

- **Editable:** All components are designed to be easily edited
- **Modular:** Add new patterns/fixes without changing core system
- **Extensible:** Easy to add new error types and fix actions
- **Safe:** Only fixes high-confidence errors (confidence > 0.7)
- **Transparent:** All actions are logged and reported

---

**Version:** 1.0  
**Created:** December 26, 2025  
**Status:** ✅ Ready for Implementation

**Remember:** This is your system - edit, customize, and improve it as needed!

