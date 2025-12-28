# 🔧 n8n Workflow Errors - AIMCODE Fix & Self-Healing System Design

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Status:** ✅ Complete Solutions + Self-Healing System Design  
**Methodology:** AIMCODE (CLEAR → Alpha Evolve → Research → Experts)

---

## 🎯 CLEAR Framework Analysis

### C - Clarity
**Problem 1:** Unity Build Orchestrator - "Header name must be a valid HTTP token ["BalICODE n8n"]"  
**Problem 2:** Screenshot-to-Fix - "Bad request - please check your parameters" (OpenAI API)

**Root Causes:**
1. Invalid HTTP header name in credential configuration (contains space: "BalICODE n8n")
2. OpenAI API request missing required parameters or malformed JSON

### L - Logic
**Systematic Fix Approach:**
1. Fix credential header name (remove spaces, use valid HTTP token)
2. Fix OpenAI API request structure (ensure all required parameters present)
3. Design self-healing system to prevent future issues

### E - Examples
**Previous Working Configurations:**
- Header Name: `Authorization` ✅ (valid HTTP token)
- Header Name: `Content-Type` ✅ (valid HTTP token)
- Header Name: `BalICODE n8n` ❌ (invalid - contains space)

### A - Adaptation
**Current State:** Credentials have invalid header names  
**Needed:** Valid HTTP header names, proper OpenAI API structure

### R - Results
**Success Criteria:**
- ✅ Workflows execute without header errors
- ✅ OpenAI API calls succeed
- ✅ Self-healing system detects and fixes similar issues automatically

---

## 🔧 FIX 1: Unity Build Orchestrator Header Error

### Problem
**Error:** `Header name must be a valid HTTP token ["BalICODE n8n"]`

**Root Cause:** 
The credential's "Header Name" field contains an invalid value. HTTP header names must be valid tokens (no spaces, only alphanumeric and hyphens).

### Solution

#### Step 1: Check Credential Configuration

**In n8n UI (http://192.168.1.226:5678):**

1. Go to **Credentials** (left sidebar)
2. Find the credential used by "Dispatch GitHub Build (AIMCODE L2)" node
3. Look for credential named: `github-actions-token` or similar
4. **Check the "Header Name" field**

#### Step 2: Fix Header Name

**The "Header Name" field MUST be:**
- ✅ `Authorization` (for GitHub API)
- ✅ `Content-Type` (if needed)
- ❌ NOT `BalICODE n8n` (invalid - contains space)
- ❌ NOT any value with spaces or special characters

**Valid HTTP Header Names:**
- `Authorization`
- `Content-Type`
- `Accept`
- `User-Agent`
- `X-Custom-Header` (custom headers must start with `X-`)

**Invalid Header Names:**
- `BalICODE n8n` ❌ (space)
- `BallCODE-n8n` ✅ (hyphen is OK)
- `BallCODE_n8n` ❌ (underscore not recommended)
- `BallCODE/n8n` ❌ (slash not allowed)

#### Step 3: Correct Credential Configuration

**For GitHub Actions Token Credential:**

```
Credential Type: Header Auth
Credential Name/ID: github-actions-token
Header Name: Authorization          ← MUST be exactly this (no spaces)
Header Value: token YOUR_GITHUB_PAT ← Your actual token
```

**To Fix:**
1. Edit the credential
2. Change "Header Name" from `BalICODE n8n` (or whatever invalid value) to `Authorization`
3. Save
4. Test the workflow

#### Step 4: Verify Workflow Node

**Check "Dispatch GitHub Build (AIMCODE L2)" node:**
1. Open the workflow
2. Click on the node
3. Verify:
   - **Authentication:** Generic Credential Type → Header Auth
   - **Credential:** `github-actions-token` (selected)
   - **Headers:** Only `Accept: application/vnd.github.v3+json` (no Authorization header - that comes from credential)

---

## 🔧 FIX 2: Screenshot-to-Fix OpenAI API Error

### Problem
**Error:** `Bad request - please check your parameters`  
**Node:** "OpenAI API Key" (Vision Analysis or Generate Fix)

**Root Causes:**
1. Missing `model` parameter in request body
2. Invalid JSON structure
3. Missing required fields (`messages`, `model`)
4. Invalid API key or credential configuration

### Solution

#### Step 1: Check OpenAI API Request Structure

**The OpenAI API requires:**
```json
{
  "model": "gpt-4o",  // REQUIRED - must be present
  "temperature": 0.1,
  "max_tokens": 2000,
  "messages": [      // REQUIRED - must be present
    {
      "role": "system",
      "content": "..."
    },
    {
      "role": "user",
      "content": "..."
    }
  ]
}
```

#### Step 2: Verify HTTP Request Node Configuration

**For "Vision Analysis (HTTP Request)" node:**

1. **Method:** `POST` ✅
2. **URL:** `https://api.openai.com/v1/chat/completions` ✅
3. **Authentication:** HTTP Header Auth → `OpenAI API Key` ✅
4. **Send Body:** ON ✅
5. **Body Content Type:** JSON ✅
6. **JSON Body:** Must include `model` and `messages` ✅

#### Step 3: Check JSON Body Expression

**Current JSON Body (from workflow file):**
```javascript
={{ JSON.stringify({
  model: 'gpt-4o',  // ✅ Present
  temperature: 0.1,
  max_tokens: 2000,
  messages: [       // ✅ Present
    {
      role: 'system',
      content: '...'
    },
    {
      role: 'user',
      content: [...]
    }
  ]
}) }}
```

**If this is correct, check:**
1. Is the expression evaluating correctly?
2. Are there any syntax errors?
3. Is `$json.imageUrlForAPI` available?

#### Step 4: Fix Missing Data Issues

**If `imageUrlForAPI` is missing:**

The "Prepare Image for API" node should output `imageUrlForAPI`. Check:
1. Does "Normalize Screenshot Input" receive the screenshot?
2. Does "Prepare Image for API" process it correctly?
3. Is `imageUrlForAPI` in the output?

**Add validation in "Prepare Image for API" node:**
```javascript
// Add at the end of the node code
if (!imageUrl) {
  throw new Error('No image URL available for OpenAI Vision API. Check screenshot input.');
}

return {
  json: {
    ...input,
    imageUrlForAPI: imageUrl,
    hasImage: !!imageUrl  // Add validation flag
  }
};
```

#### Step 5: Verify Credential Configuration

**For OpenAI API Key Credential:**

```
Credential Type: HTTP Header Auth
Credential Name/ID: openai-api-key
Header Name: Authorization          ← MUST be exactly this
Header Value: Bearer sk-...         ← Your actual API key (with "Bearer " prefix)
```

**To Fix:**
1. Edit the credential
2. Verify "Header Name" is exactly `Authorization` (no spaces, no typos)
3. Verify "Header Value" is exactly `Bearer sk-...` (with space after "Bearer")
4. Test the API key at https://platform.openai.com/api-keys

#### Step 6: Test with Minimal Request

**Create a test node to verify API works:**

```json
{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": "Say hello"
    }
  ]
}
```

**If this works, the issue is in the complex request structure.**

---

## 🤖 SELF-HEALING SYSTEM DESIGN (Garvis)

### Vision: Garvis Should Fix Itself

**Question:** "Will we ever have a system that does not have issues?"

**Answer:** No system is perfect, but we can build self-healing capabilities.

### Self-Healing Architecture

#### Layer 1: Detection (Alpha Evolve Foundation)

**Error Detection System:**
```javascript
// Monitor workflow executions
const errorPatterns = {
  headerError: /Header name must be a valid HTTP token/i,
  openaiBadRequest: /Bad request - please check your parameters/i,
  credentialError: /credential.*not found/i,
  missingParameter: /Missing required parameter/i
};

// Detect errors automatically
function detectError(execution) {
  const error = execution.error;
  if (!error) return null;
  
  for (const [type, pattern] of Object.entries(errorPatterns)) {
    if (pattern.test(error.message)) {
      return { type, error, execution };
    }
  }
  return null;
}
```

#### Layer 2: Diagnosis (Systematic Analysis)

**Error Diagnosis System:**
```javascript
// Diagnose root cause
function diagnoseError(errorType, error, execution) {
  const diagnosis = {
    errorType,
    node: execution.node,
    likelyCause: null,
    fix: null
  };
  
  switch (errorType) {
    case 'headerError':
      diagnosis.likelyCause = 'Invalid header name in credential (contains spaces or special characters)';
      diagnosis.fix = {
        action: 'updateCredential',
        credentialId: execution.node.credentials?.httpHeaderAuth?.id,
        field: 'headerName',
        correctValue: 'Authorization'
      };
      break;
      
    case 'openaiBadRequest':
      diagnosis.likelyCause = 'Missing required parameters (model, messages) or invalid JSON';
      diagnosis.fix = {
        action: 'validateRequestBody',
        node: execution.node.id,
        requiredFields: ['model', 'messages']
      };
      break;
  }
  
  return diagnosis;
}
```

#### Layer 3: Auto-Fix (Application)

**Self-Healing Actions:**
```javascript
// Apply fixes automatically
async function applyFix(diagnosis) {
  switch (diagnosis.fix.action) {
    case 'updateCredential':
      // Update credential via n8n API
      await updateCredentialHeaderName(
        diagnosis.fix.credentialId,
        diagnosis.fix.correctValue
      );
      break;
      
    case 'validateRequestBody':
      // Validate and fix request body
      await validateAndFixRequestBody(
        diagnosis.fix.node,
        diagnosis.fix.requiredFields
      );
      break;
  }
}
```

#### Layer 4: Verification (Mastery)

**Verify Fix Worked:**
```javascript
// Re-run workflow and verify fix
async function verifyFix(execution, diagnosis) {
  // Wait for fix to be applied
  await sleep(2000);
  
  // Re-run the workflow
  const retryExecution = await retryWorkflow(execution.workflowId);
  
  // Check if error is resolved
  if (!retryExecution.error) {
    return {
      success: true,
      message: `Fixed ${diagnosis.errorType} automatically`
    };
  }
  
  return {
    success: false,
    message: `Fix attempted but error persists: ${retryExecution.error.message}`
  };
}
```

### Self-Healing Workflow Integration

**Garvis Self-Healing Workflow:**

1. **Monitor Executions** (Scheduled Trigger - every 5 minutes)
   - Check all workflow executions for errors
   - Detect known error patterns

2. **Diagnose Errors** (Code Node)
   - Analyze error messages
   - Identify root cause
   - Generate fix plan

3. **Apply Fixes** (HTTP Request to n8n API)
   - Update credentials
   - Fix node configurations
   - Validate request bodies

4. **Verify Fixes** (Code Node)
   - Re-run workflow
   - Check if error resolved
   - Log results

5. **Notify User** (Webhook/Email)
   - Report what was fixed
   - Request approval for complex fixes
   - Provide manual fix instructions if auto-fix fails

### Prevention System

**Proactive Validation:**

1. **Credential Validation** (Before workflow execution)
   - Check header names are valid HTTP tokens
   - Verify API keys are formatted correctly
   - Validate credential structure

2. **Request Body Validation** (Before API calls)
   - Ensure required parameters present
   - Validate JSON structure
   - Check data types

3. **Node Configuration Validation** (Before activation)
   - Verify all required fields set
   - Check credential references exist
   - Validate expression syntax

---

## 📋 IMMEDIATE ACTION ITEMS

### For Unity Build Orchestrator:

1. ✅ **Check credential "Header Name" field**
   - Go to: Credentials → `github-actions-token`
   - Verify: Header Name = `Authorization` (exactly, no spaces)
   - Fix: If it says `BalICODE n8n` or anything else, change to `Authorization`

2. ✅ **Test workflow**
   - Run workflow manually
   - Verify no header errors

### For Screenshot-to-Fix:

1. ✅ **Check OpenAI credential**
   - Go to: Credentials → `openai-api-key`
   - Verify: Header Name = `Authorization`
   - Verify: Header Value = `Bearer sk-...` (with space after "Bearer")

2. ✅ **Check JSON body in HTTP Request nodes**
   - Verify `model` parameter is present
   - Verify `messages` array is present
   - Test with minimal request first

3. ✅ **Verify image data flow**
   - Check "Prepare Image for API" outputs `imageUrlForAPI`
   - Add validation if missing

---

## 🎯 LONG-TERM: Self-Healing System Implementation

### Phase 1: Error Detection (Week 1)
- Monitor workflow executions
- Detect common error patterns
- Log errors for analysis

### Phase 2: Auto-Diagnosis (Week 2)
- Analyze error messages
- Identify root causes
- Generate fix plans

### Phase 3: Auto-Fix (Week 3)
- Implement credential fixes
- Fix node configurations
- Validate request bodies

### Phase 4: Prevention (Week 4)
- Proactive validation
- Pre-execution checks
- Configuration validation

---

## 📚 REFERENCES

- **n8n HTTP Header Auth:** https://docs.n8n.io/integrations/builtin/credentials/httpheader/
- **OpenAI API Reference:** https://platform.openai.com/docs/api-reference/chat
- **HTTP Header Names:** RFC 7230 Section 3.2
- **AIMCODE Methodology:** `documents/AIMCODE-METHODOLOGY.md`

---

## ✅ SUCCESS CRITERIA

- [ ] Unity Build Orchestrator executes without header errors
- [ ] Screenshot-to-Fix executes without OpenAI API errors
- [ ] Credentials have valid header names
- [ ] Self-healing system detects and fixes common errors
- [ ] Prevention system catches issues before execution

---

**Version:** 1.0  
**Created:** December 26, 2025  
**Status:** ✅ Complete Solutions + Self-Healing Design

