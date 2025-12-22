# 🎭 Mock Responses - Copy-Paste Ready

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Quick Reference:** Mock Code nodes to replace HTTP Request nodes for free testing

---

## 🎯 MOCK VISION ANALYSIS NODE

**Replace:** "Vision Analysis (HTTP Request)"  
**With:** Code node named "Mock Vision Analysis"

**Code to Paste:**
```javascript
// Mock OpenAI Vision API response - NO API COST
// Returns realistic diagnosis for testing

const mockDiagnosis = {
  "errorType": "n8n_workflow",
  "errorMessage": "Could not find property option",
  "affectedSystem": "n8n workflow import",
  "likelyCause": "Empty options object in node parameters causes validation error",
  "filesToFix": [
    "n8n-unity-build-orchestrator.json",
    "n8n-screenshot-to-fix-workflow.json"
  ],
  "severity": "high",
  "canAutoFix": true,
  "fixComplexity": "simple"
};

// Simulate OpenAI API response format
return {
  json: {
    choices: [
      {
        message: {
          content: JSON.stringify(mockDiagnosis)
        }
      }
    ],
    usage: {
      prompt_tokens: 150,
      completion_tokens: 200,
      total_tokens: 350
    }
  }
};
```

---

## 🎯 MOCK GENERATE FIX NODE

**Replace:** "Generate Fix (HTTP Request)"  
**With:** Code node named "Mock Generate Fix"

**Code to Paste:**
```javascript
// Mock OpenAI Fix Generation API response - NO API COST
// Returns realistic fix for testing

const mockFix = {
  "fixType": "workflow_json",
  "filePath": "n8n-unity-build-orchestrator.json",
  "originalCode": '{\n  "parameters": {\n    "options": {}\n  }\n}',
  "fixedCode": '{\n  "parameters": {}\n}',
  "explanation": "Removed empty options object. n8n validation rejects empty options: {} objects. Removing it resolves the 'could not find property option' error.",
  "validation": "1. Import the fixed workflow JSON\n2. Verify no import errors\n3. Activate workflow\n4. Test webhook endpoint"
};

// Simulate OpenAI API response format
return {
  json: {
    choices: [
      {
        message: {
          content: JSON.stringify(mockFix)
        }
      }
    ],
    usage: {
      prompt_tokens: 300,
      completion_tokens: 400,
      total_tokens: 700
    }
  }
};
```

---

## 🔄 HOW TO SWITCH BETWEEN MOCK AND REAL

### **Method 1: IF Node Toggle**

**Add IF Node Before Vision Analysis:**

**Condition:**
```javascript
={{ $env.TEST_MODE === "true" }}
```

**True Branch:** Mock Vision Analysis (Code node)  
**False Branch:** Vision Analysis (HTTP Request node)

**Same for Generate Fix node.**

### **Method 2: Environment Variable**

**Set in n8n:**
- Settings → Environment Variables
- `TEST_MODE = true` (use mocks)
- `TEST_MODE = false` (use real API)

---

## ✅ QUICK SETUP (5 MINUTES)

1. **Add Code Node:** "Mock Vision Analysis"
   - Paste code above
   - Connect: "Prepare Image for API" → "Mock Vision Analysis"

2. **Add Code Node:** "Mock Generate Fix"
   - Paste code above
   - Connect: "Can Auto-Fix?" (true branch) → "Mock Generate Fix"

3. **Test Workflow:**
   - Execute workflow
   - **Cost: $0.00** ✅

4. **When Ready for Real API:**
   - Disconnect mock nodes
   - Reconnect HTTP Request nodes
   - Test with real API

---

## 🎭 VARIATIONS: Different Mock Responses

### **Mock for Different Error Types:**

**Unity Build Error:**
```javascript
const mockDiagnosis = {
  "errorType": "unity_build",
  "errorMessage": "Build failed: Missing dependencies",
  "affectedSystem": "Unity WebGL build",
  "likelyCause": "Missing package references in manifest.json",
  "filesToFix": ["Packages/manifest.json"],
  "severity": "medium",
  "canAutoFix": true,
  "fixComplexity": "moderate"
};
```

**Deployment Error:**
```javascript
const mockDiagnosis = {
  "errorType": "deployment",
  "errorMessage": "Netlify deployment failed",
  "affectedSystem": "Netlify CDN",
  "likelyCause": "Build output path incorrect",
  "filesToFix": ["netlify.toml"],
  "severity": "high",
  "canAutoFix": true,
  "fixComplexity": "simple"
};
```

---

**Status:** ✅ Ready to Use  
**Cost:** $0.00 per test  
**Next:** Replace HTTP Request nodes with these mock Code nodes

