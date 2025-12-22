# ✅ COMPLETE CODE NODE - Full Code (Copy-Paste Ready)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Node Name:** `Prepare OpenAI Request Body`  
**Language:** JavaScript  
**Status:** ✅ Complete - Ready to Copy-Paste

---

## 📋 COMPLETE CODE (Copy All of This)

```javascript
// Get values with fallbacks
const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";
const context = String($json.context || "Unknown error");

// Build request body as JavaScript object
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
          text: `Analyze this error screenshot and provide structured diagnosis:\n\nContext: ${context}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  "errorType": "string",\n  "errorMessage": "string",\n  "affectedSystem": "string",\n  "likelyCause": "string",\n  "filesToFix": ["array", "of", "files"],\n  "severity": "low|medium|high|critical",\n  "canAutoFix": true/false,\n  "fixComplexity": "simple|moderate|complex"\n}`
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
    apiRequestBody: requestBody
  }
};
```

---

## ✅ HTTP REQUEST NODE CONFIGURATION

**After using this Code node:**

```
Method: POST
URL: https://api.openai.com/v1/chat/completions
Authentication: [Your credential]

Send Body: ON
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: [Click Expression button, paste:] {{ $json.apiRequestBody }}

Send Headers: ON
Headers:
  - Content-Type: application/json
  - Authorization: Bearer sk-proj-... (from credential)
```

---

## 🎯 KEY POINTS

1. **Complete code:** Everything above is the full Code node
2. **Returns object:** No `JSON.stringify()` - returns object directly
3. **Expression syntax:** Use `{{ }}` not `={{ }}` in HTTP Request
4. **JSON mode:** Use "Using JSON" mode, not Raw mode

---

**Status:** ✅ Complete Code  
**Action:** Copy the entire code block above into your Code node

