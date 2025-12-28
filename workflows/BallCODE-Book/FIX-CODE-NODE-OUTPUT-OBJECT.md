# 🔧 Fix: Code Node Should Output Object, Not String

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** "We could not parse the JSON body"  
**Root Cause:** Code node outputs JSON string, but Raw mode isn't handling it correctly  
**Solution:** Change Code node to output object, use "Using JSON" mode  
**Fix Time:** 2 minutes

---

## 🎯 THE PROBLEM

**Current Code Node:**
```javascript
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody) // ← String
  }
};
```

**Current HTTP Request:**
- Raw mode with `={{ $json.apiRequestBody }}`
- Sends the string, but OpenAI can't parse it

**The Issue:**
- Stringified JSON in Raw mode might have encoding issues
- Better to send object directly

---

## ✅ THE FIX

### **Step 1: Change Code Node to Output Object**

**In "Prepare OpenAI Request Body" Code node:**

**Change from:**
```javascript
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody) // String
  }
};
```

**Change to:**
```javascript
return {
  json: {
    ...$json,
    apiRequestBody: requestBody // Object, not string
  }
};
```

### **Step 2: Change HTTP Request to "Using JSON" Mode**

**In "OpenAI API Key" HTTP Request node:**

1. **Body Content Type:** Change from "Raw" to **"JSON"**
2. **Specify Body:** Set to **"Using JSON"**
3. **JSON Body:** Expression: `={{ $json.apiRequestBody }}`

---

## ✅ COMPLETE CODE NODE (Updated)

**Node Name:** `Prepare OpenAI Request Body`

**Code:**
```javascript
// Prepare request body as JavaScript object (not string)
const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";

const requestBody = {
  model: "gpt-4o",
  temperature: 0.1,
  max_tokens: 2000,
  messages: [
    {
      role: "system",
      content: "You are an expert error diagnosis system. Analyze screenshots of errors and provide structured diagnosis."
    },
    {
      role: "user",
      content: [
        {
          type: "text",
          text: `Analyze this error screenshot and provide structured diagnosis:

Context: ${$json.context || "Unknown error"}

Identify:
1. Error type (n8n_workflow, unity_build, deployment, web_error, other)
2. Exact error message
3. Affected system/component
4. Likely cause
5. Files/components that need fixing
6. Severity (low, medium, high, critical)

Return JSON only:
{
  "errorType": "string",
  "errorMessage": "string",
  "affectedSystem": "string",
  "likelyCause": "string",
  "filesToFix": ["array", "of", "files"],
  "severity": "low|medium|high|critical",
  "canAutoFix": true/false,
  "fixComplexity": "simple|moderate|complex"
}`
        },
        {
          type: "image_url",
          image_url: {
            url: imageUrl
          }
        }
      ]
    }
  ]
};

// Return as OBJECT (not stringified)
return {
  json: {
    ...$json,
    apiRequestBody: requestBody // Object, not JSON.stringify()
  }
};
```

---

## ✅ HTTP REQUEST CONFIGURATION (Updated)

**In "OpenAI API Key" HTTP Request node:**

```
Send Body: ON
Body Content Type: JSON ← CHANGE FROM RAW
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }} ← Expression (object)
```

---

## 🎯 WHY THIS WORKS

**Current (Fails):**
- Code node: `JSON.stringify()` → String
- HTTP Request: Raw mode → Sends string
- OpenAI: Can't parse string correctly

**Fixed (Works):**
- Code node: Returns object directly
- HTTP Request: "Using JSON" mode → n8n stringifies it correctly
- OpenAI: Receives valid JSON ✅

---

## ✅ VERIFICATION

After fixing:

- [ ] Code node outputs `apiRequestBody` as object (not string)
- [ ] HTTP Request: Body Content Type = "JSON"
- [ ] HTTP Request: Specify Body = "Using JSON"
- [ ] HTTP Request: JSON Body = `={{ $json.apiRequestBody }}`

---

**Time:** 2 minutes  
**Status:** This will work  
**Next:** Update Code node to output object, change HTTP Request to "Using JSON"


