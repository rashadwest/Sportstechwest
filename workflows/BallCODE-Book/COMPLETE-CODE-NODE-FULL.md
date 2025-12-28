# ✅ Complete Code Node - Copy-Paste Ready

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Node Name:** `Prepare OpenAI Request Body`  
**Language:** JavaScript  
**Status:** ✅ Complete - Ready to Use

---

## 📋 COMPLETE CODE (Copy-Paste This)

```javascript
// Prepare OpenAI API request body as JavaScript object
// This will be stringified by HTTP Request node in "Using JSON" mode

const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";

// Build the request body as a JavaScript object
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
// HTTP Request node in "Using JSON" mode will stringify it correctly
return {
  json: {
    ...$json,
    apiRequestBody: requestBody
  }
};
```

---

## ✅ HTTP REQUEST NODE CONFIGURATION

**After using this Code node, configure HTTP Request:**

```
Send Body: ON
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }}
```

---

## 🎯 KEY POINTS

1. **Returns object, not string** - No `JSON.stringify()`
2. **HTTP Request will stringify it** - "Using JSON" mode handles that
3. **Image URL has fallback** - Uses `imageUrlForAPI`, `screenshotUrl`, or placeholder
4. **Context has fallback** - Uses `context` or "Unknown error"

---

**Status:** ✅ Ready to paste  
**Next:** Copy code above, paste in Code node, configure HTTP Request as shown


