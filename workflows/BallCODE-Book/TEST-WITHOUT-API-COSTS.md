# 💰 Testing Without API Costs - Complete Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Purpose:** Test OpenAI API workflows without incurring charges  
**Status:** ✅ Complete Testing Strategy

---

## 🎯 THE PROBLEM

Every test of the Screenshot-to-Fix workflow calls OpenAI API, which costs money:
- Vision Analysis (GPT-4o): ~$0.01-0.03 per image
- Generate Fix (GPT-4): ~$0.03-0.06 per request
- **Total per test:** ~$0.04-0.09

**Testing 10 times = $0.40-0.90**  
**Testing 100 times = $4-9**

---

## ✅ SOLUTION 1: Mock Response Node (BEST FOR TESTING)

### **How It Works:**
Replace the HTTP Request node with a Code node that returns a mock response.

### **Step 1: Create Mock Vision Analysis Node**

**Replace "Vision Analysis (HTTP Request)" with a Code node:**

**Node Name:** `Mock Vision Analysis`

**Code:**
```javascript
// Mock response for testing - no API cost
const mockDiagnosis = {
  "errorType": "n8n_workflow",
  "errorMessage": "Could not find property option",
  "affectedSystem": "n8n workflow import",
  "likelyCause": "Empty options object in node parameters",
  "filesToFix": ["n8n-unity-build-orchestrator.json"],
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
    ]
  }
};
```

### **Step 2: Create Mock Generate Fix Node**

**Replace "Generate Fix (HTTP Request)" with a Code node:**

**Node Name:** `Mock Generate Fix`

**Code:**
```javascript
// Mock response for testing - no API cost
const mockFix = {
  "fixType": "workflow_json",
  "filePath": "n8n-unity-build-orchestrator.json",
  "originalCode": '{"parameters": {"options": {}}}',
  "fixedCode": '{"parameters": {}}',
  "explanation": "Removed empty options object that causes validation error",
  "validation": "Import workflow and verify no 'could not find property option' error"
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
    ]
  }
};
```

### **Step 3: Toggle Between Mock and Real**

**Option A: Use IF Node to Switch**
- Add IF node before HTTP Request
- Check environment variable: `USE_MOCK_RESPONSES`
- If true → use Mock nodes
- If false → use real HTTP Request nodes

**Option B: Duplicate Workflow**
- Create "Screenshot-to-Fix (TEST)" workflow with mock nodes
- Keep "Screenshot-to-Fix (PROD)" with real API calls
- Test in TEST workflow, use PROD for real fixes

---

## ✅ SOLUTION 2: Response Caching

### **How It Works:**
Cache API responses so identical requests don't hit the API again.

### **Implementation:**

**Add Code Node Before HTTP Request:**

```javascript
// Check if we've seen this request before
const requestHash = `${$json.context}-${$json.screenshotUrl}`;
const cache = $getWorkflowStaticData('global');

// Check cache
if (cache.responses && cache.responses[requestHash]) {
  // Return cached response
  return {
    json: {
      ...$json,
      cached: true,
      apiResponse: cache.responses[requestHash]
    }
  };
}

// Mark as not cached - will call API
return {
  json: {
    ...$json,
    cached: false,
    requestHash: requestHash
  }
};
```

**Add Code Node After HTTP Request:**

```javascript
// Cache the response
const requestHash = $json.requestHash;
const cache = $getWorkflowStaticData('global');

if (!cache.responses) {
  cache.responses = {};
}

cache.responses[requestHash] = $input.item.json;

return {
  json: {
    ...$json,
    apiResponse: $input.item.json
  }
};
```

**Benefits:**
- First test: Costs money
- Subsequent identical tests: FREE (uses cache)
- Great for testing the same error multiple times

---

## ✅ SOLUTION 3: Use Cheaper Models for Testing

### **How It Works:**
Use cheaper models during testing, switch to better models in production.

### **Implementation:**

**Use Environment Variable:**

```javascript
={{ JSON.stringify({
  "model": $env.OPENAI_TEST_MODE === "true" ? "gpt-3.5-turbo" : "gpt-4o",
  "temperature": 0.1,
  "max_tokens": 2000,
  "messages": [...]
}) }}
```

**Cost Comparison:**
- GPT-3.5-turbo: ~$0.001-0.002 per request (10x cheaper)
- GPT-4o: ~$0.01-0.03 per request
- **Savings:** 90% cost reduction for testing

**Set Environment Variable:**
- In n8n: Settings → Environment Variables
- Add: `OPENAI_TEST_MODE = true` (for testing)
- Set to `false` or remove for production

---

## ✅ SOLUTION 4: Test Mode Flag

### **How It Works:**
Add a test mode that skips API calls entirely.

### **Implementation:**

**Add IF Node After "Prepare Image for API":**

**Condition:** Check if `$env.TEST_MODE === "true"`

**True Branch (Test Mode):**
- Use Mock Code nodes (Solution 1)
- No API calls = No cost

**False Branch (Production Mode):**
- Use real HTTP Request nodes
- Real API calls = Real cost

**Set Test Mode:**
```bash
# In n8n environment variables
TEST_MODE=true  # For testing
TEST_MODE=false # For production
```

---

## ✅ SOLUTION 5: Limit Testing Scope

### **How It Works:**
Only test the parts that don't call APIs.

### **Test These Nodes Without Cost:**
1. ✅ **Screenshot Upload Webhook** - No cost
2. ✅ **Normalize Screenshot Input** - No cost
3. ✅ **Prepare Image for API** - No cost
4. ✅ **Parse Diagnosis** - No cost (if you provide mock input)
5. ✅ **Can Auto-Fix?** - No cost
6. ✅ **Parse Fix** - No cost (if you provide mock input)
7. ✅ **Apply Fix** - No cost (local script)
8. ✅ **Commit & Push** - No cost (git operations)

### **Skip These Nodes During Testing:**
1. ❌ **Vision Analysis (HTTP Request)** - Use mock
2. ❌ **Generate Fix (HTTP Request)** - Use mock

---

## ✅ SOLUTION 6: Use n8n Test Mode

### **How It Works:**
n8n has a test mode that can intercept API calls.

### **Implementation:**

**Use "Test URL" Instead of Production URL:**
- Test webhook: `/webhook-test/screenshot-fix` (doesn't trigger real workflow)
- Production webhook: `/webhook/screenshot-fix` (triggers real workflow)

**But:** This still calls APIs if the workflow runs.

**Better:** Use test mode + mock nodes together.

---

## 📋 RECOMMENDED TESTING STRATEGY

### **Phase 1: Initial Testing (Use Mocks)**
1. Replace HTTP Request nodes with Mock Code nodes
2. Test entire workflow flow
3. Verify all nodes connect correctly
4. **Cost:** $0.00

### **Phase 2: API Testing (Use Caching)**
1. Replace Mock nodes with real HTTP Request nodes
2. Test with real API (first time costs money)
3. Enable response caching
4. Re-test same scenarios (uses cache = free)
5. **Cost:** $0.04-0.09 per unique test

### **Phase 3: Production (Use Real API)**
1. Keep real HTTP Request nodes
2. Disable test mode
3. Use production webhook
4. **Cost:** Normal API costs

---

## 🎯 QUICK SETUP: Test Mode Toggle

### **Add This Code Node Before Vision Analysis:**

**Node Name:** `Check Test Mode`

**Code:**
```javascript
const testMode = ($env.TEST_MODE || 'false').toLowerCase() === 'true';

return {
  json: {
    ...$json,
    testMode: testMode,
    useMock: testMode
  }
};
```

### **Add IF Node:**

**Condition:** `$json.useMock === true`

**True Branch:** Mock Code nodes  
**False Branch:** Real HTTP Request nodes

### **Set Environment Variable:**

In n8n: Settings → Environment Variables
```
TEST_MODE=true   # For testing (uses mocks)
TEST_MODE=false  # For production (uses real API)
```

---

## 💡 COST TRACKING

### **Monitor Your Costs:**

**Add Code Node to Log API Calls:**

```javascript
// Log API usage for cost tracking
const logEntry = {
  timestamp: new Date().toISOString(),
  node: 'Vision Analysis',
  model: 'gpt-4o',
  estimatedCost: 0.02, // $0.02 per call
  context: $json.context
};

// Store in workflow static data
const logs = $getWorkflowStaticData('global');
if (!logs.apiCalls) {
  logs.apiCalls = [];
}
logs.apiCalls.push(logEntry);

// Keep only last 100 calls
if (logs.apiCalls.length > 100) {
  logs.apiCalls = logs.apiCalls.slice(-100);
}

return { json: $json };
```

**View Costs:**
- Check workflow static data
- Sum up `estimatedCost` values
- Track daily/weekly spending

---

## ✅ BEST PRACTICES

1. **Always use mocks for initial testing**
2. **Use caching for repeated tests**
3. **Use cheaper models (GPT-3.5) for testing**
4. **Set TEST_MODE environment variable**
5. **Monitor costs with logging**
6. **Test workflow structure first, API calls last**

---

## 🚀 QUICK START: Enable Test Mode Now

**Right Now (2 minutes):**

1. Go to n8n: Settings → Environment Variables
2. Add: `TEST_MODE = true`
3. Replace HTTP Request nodes with Mock Code nodes (use code from Solution 1)
4. Test workflow - **Cost: $0.00**

**When Ready for Real Testing:**

1. Set: `TEST_MODE = false`
2. Replace Mock nodes with HTTP Request nodes
3. Test with real API - **Cost: $0.04-0.09 per unique test**

---

**Status:** ✅ Complete Testing Strategy  
**Cost Savings:** 90-100% during testing phase  
**Next:** Implement Solution 1 (Mock Nodes) for immediate free testing


