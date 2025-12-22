# 📸 Screenshot to Fix Workflow - Testing Guide
## How to Consistently Test the Screenshot Fix Workflow

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Guide for consistently testing the Screenshot to Fix workflow  
**Status:** ✅ Active Guide

---

## 🎯 CURRENT STATUS

**Workflow:** Screenshot to Fix  
**File:** `n8n-screenshot-to-fix-workflow.json`  
**Webhook:** `/webhook/screenshot-fix`  
**Status:** ✅ Working but needs consistent testing

**Current Issue:** Hard to test consistently

---

## 🧪 TESTING METHODS

### Method 1: Quick Test (Recommended)

**Use the test script:**
```bash
./scripts/test-screenshot-fix.sh
```

**What it does:**
1. Prompts for screenshot URL
2. Prompts for context/description
3. Sends request to webhook
4. Shows response
5. Saves test results

---

### Method 2: Manual curl Test

**Basic test:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "Unity build error - missing dependency"
  }'
```

**With more context:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "Unity build error - missing dependency",
    "errorType": "build_failure",
    "system": "unity",
    "urgency": "high"
  }'
```

---

### Method 3: Test with Local Screenshot

**Step 1: Upload screenshot to public URL**
- Use Imgur, GitHub, or any public image host
- Get the direct image URL

**Step 2: Test with URL**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d "{
    \"screenshotUrl\": \"YOUR_PUBLIC_IMAGE_URL\",
    \"context\": \"Test error description\"
  }"
```

---

## 📋 TESTING CHECKLIST

### Before Testing:

- [ ] Screenshot URL is publicly accessible
- [ ] Screenshot shows a clear error/problem
- [ ] Context description is clear
- [ ] Workflow is active in n8n UI
- [ ] OpenAI credentials are configured
- [ ] `WORKFLOW_PATH` environment variable is set

### During Testing:

- [ ] Webhook responds (not 404 or timeout)
- [ ] Response includes error identification
- [ ] Response includes fix suggestions
- [ ] Response includes fix code (if applicable)
- [ ] Response indicates if fix was applied

### After Testing:

- [ ] Review error identification (is it accurate?)
- [ ] Review fix suggestions (are they helpful?)
- [ ] Check if fix was actually applied (if auto-fix enabled)
- [ ] Verify files were modified (if fix applied)
- [ ] Check n8n execution logs for errors

---

## 🎯 TEST SCENARIOS

### Scenario 1: Unity Build Error

**Screenshot:** Unity build error message  
**Context:** "Unity build failed with missing dependency error"

**Expected Response:**
- Identifies missing dependency
- Suggests fix (add dependency)
- Provides fix code
- Indicates if fix can be auto-applied

**Test Command:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "YOUR_UNITY_ERROR_SCREENSHOT_URL",
    "context": "Unity build failed with missing dependency error"
  }'
```

---

### Scenario 2: n8n Workflow Error

**Screenshot:** n8n workflow error in UI  
**Context:** "n8n workflow showing connection error"

**Expected Response:**
- Identifies connection issue
- Suggests fix (check credentials, verify nodes)
- Provides troubleshooting steps

**Test Command:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "YOUR_N8N_ERROR_SCREENSHOT_URL",
    "context": "n8n workflow showing connection error between nodes"
  }'
```

---

### Scenario 3: Website Display Error

**Screenshot:** Website showing broken layout  
**Context:** "Website homepage showing broken CSS"

**Expected Response:**
- Identifies CSS issue
- Suggests fix (CSS file path, missing styles)
- Provides fix code

**Test Command:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "YOUR_WEBSITE_ERROR_SCREENSHOT_URL",
    "context": "Website homepage showing broken CSS layout"
  }'
```

---

## 🔧 TROUBLESHOOTING TEST ISSUES

### Issue: "Screenshot URL not accessible"

**Symptoms:**
- Response says "Cannot access screenshot"
- Error about URL

**Solutions:**
1. Ensure screenshot URL is publicly accessible
2. Use direct image URL (not page URL)
3. Test URL in browser first
4. Use image hosting service (Imgur, GitHub)

---

### Issue: "No response from webhook"

**Symptoms:**
- Request hangs
- No response

**Solutions:**
1. Check if workflow is active in n8n UI
2. Check n8n logs for errors
3. Verify OpenAI credentials
4. Try simpler test first

---

### Issue: "Error identification is wrong"

**Symptoms:**
- AI misidentifies the error
- Fix suggestions don't match error

**Solutions:**
1. Provide more context in request
2. Use clearer screenshot (highlight error area)
3. Include error type in context
4. Try different screenshot angle

---

### Issue: "Fix not applied"

**Symptoms:**
- Response says fix suggested but not applied
- Files not modified

**Solutions:**
1. Check if auto-fix is enabled in workflow
2. Verify file permissions
3. Check if fix requires manual intervention
4. Review n8n logs for errors

---

## 📊 EXPECTED RESPONSE FORMAT

### Success Response:

```json
{
  "status": "success",
  "errorIdentified": "Missing dependency in Unity project",
  "errorType": "build_failure",
  "fixApplied": true,
  "fixCode": "// Add missing dependency\nusing UnityEngine.UI;",
  "filesModified": [
    "Unity-Scripts/Game/GameController.cs"
  ],
  "fixDescription": "Added missing UnityEngine.UI dependency",
  "buildTriggered": false,
  "manualFixRequired": false
}
```

### Manual Fix Required Response:

```json
{
  "status": "success",
  "errorIdentified": "Complex configuration issue",
  "errorType": "configuration",
  "fixApplied": false,
  "fixSuggestions": [
    "Check environment variables",
    "Verify credentials",
    "Review configuration file"
  ],
  "manualFixRequired": true,
  "fixSteps": [
    "Step 1: Check n8n Settings → Environment Variables",
    "Step 2: Verify credentials are configured",
    "Step 3: Review workflow configuration"
  ]
}
```

---

## 💡 BEST PRACTICES

### 1. Use Clear Screenshots
- Screenshot should clearly show the error
- Include error messages in screenshot
- Highlight relevant areas if possible

### 2. Provide Good Context
- Describe what you were doing when error occurred
- Include error type if known
- Mention system (Unity, n8n, website, etc.)

### 3. Test Regularly
- Test with different error types
- Test with different systems
- Build confidence in workflow

### 4. Review Responses
- Always review error identification
- Check if fix suggestions are helpful
- Verify if fix was actually applied

### 5. Use Test Script
- Use `./scripts/test-screenshot-fix.sh` for consistent testing
- Saves test results for review
- Makes testing easier

---

## 🚀 QUICK TEST SCRIPT

Create this script for easy testing:

```bash
#!/bin/bash
# Quick Screenshot Fix Test

read -p "Screenshot URL: " SCREENSHOT_URL
read -p "Context/Description: " CONTEXT

curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d "{
    \"screenshotUrl\": \"${SCREENSHOT_URL}\",
    \"context\": \"${CONTEXT}\"
  }" | jq '.'
```

Save as: `scripts/test-screenshot-fix.sh`

---

## 📚 RELATED DOCUMENTATION

- **Command Reference:** `BALLCODE-N8N-COMMAND-REFERENCE.md`
- **Screenshot System:** `SCREENSHOT-TO-FIX-SYSTEM-AIMCODE.md`
- **Workflow Analysis:** `N8N-WORKFLOWS-END-TO-END-ANALYSIS.md`

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** ✅ Active Guide

