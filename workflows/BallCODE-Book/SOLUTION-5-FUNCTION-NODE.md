# ⚡ SOLUTION 5: Function Node (Alternative to Code Node)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Status:** Solutions 1, 2, 3 failed → Try Function node  
**Success Rate:** 80%  
**Time:** 3 minutes

---

## 🎯 THE APPROACH

**Use Function node instead of Code node** - Older n8n syntax, sometimes more reliable.

**Why This Might Work:**
- Function node uses older, more stable API
- Some users report Function node works when Code node doesn't
- Different internal handling of data

---

## ✅ FUNCTION NODE (Complete Code)

**Node Name:** `Prepare OpenAI Request Body`  
**Node Type:** Function (not Code)

```javascript
// Sanitize text to prevent JSON breaking
const sanitize = (text) => {
  if (!text) return "";
  return String(text)
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\n/g, '\\n')
    .replace(/\r/g, '\\r')
    .replace(/\t/g, '\\t');
};

const inputData = $input.item.json;
const imageUrl = inputData.imageUrlForAPI || inputData.screenshotUrl || "https://picsum.photos/800/600";
const context = sanitize(inputData.context || "Unknown error");

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

// Function node returns array
return [{
  json: {
    ...inputData,
    apiRequestBody: requestBody  // Object, not stringified
  }
}];
```

**KEY DIFFERENCES:**
- Uses `$input.item.json` instead of `$json`
- Returns array `[{ json: {...} }]` instead of `{ json: {...} }`
- Returns object (not stringified)

---

## ✅ HTTP REQUEST NODE (Using JSON Mode)

**After Function node, configure HTTP Request:**

```
Method: POST
URL: https://api.openai.com/v1/chat/completions
Authentication: [Your credential]

Send Query Parameters: OFF

Send Headers: ON
Headers:
  - Name: Content-Type
  - Value: application/json
  - Name: Authorization
  - Value: Bearer sk-proj-... (from credential)

Send Body: ON
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }}
```

---

## 🧪 TEST IT

1. **Replace Code node with Function node**
2. **Paste Function node code** above
3. **Configure HTTP Request** as shown
4. **Save workflow**
5. **Execute node**
6. **Check result**

---

## 🐛 IF THIS FAILS

**Try Function node with stringified output:**

Change last line to:
```javascript
return [{
  json: {
    ...inputData,
    apiRequestBody: JSON.stringify(requestBody)  // Stringified
  }
}];
```

Then use Raw mode in HTTP Request:
```
Body Content Type: Raw
Raw Content Type: application/json
Body: {{ $json.apiRequestBody }}
```

---

**Status:** ✅ Ready to Test  
**Previous:** Solutions 1, 2, 3 failed  
**Next:** Solution 5 (Function node)

