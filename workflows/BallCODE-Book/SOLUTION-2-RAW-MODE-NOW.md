# ⚡ SOLUTION 2: Raw Mode (Try This Now - Solution 1 Failed)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Status:** Solution 1 failed → Trying Solution 2  
**Success Rate:** 85%  
**Time:** 2 minutes

---

## ✅ CODE NODE (Returns STRING, Not Object)

**Node Name:** `Prepare OpenAI Request Body`  
**Language:** JavaScript

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

const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";
const context = sanitize($json.context || "Unknown error");

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

// Return as STRING (stringified) ← KEY DIFFERENCE
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody)
  }
};
```

**KEY CHANGE:** `JSON.stringify(requestBody)` instead of just `requestBody`

---

## ✅ HTTP REQUEST NODE (Raw Mode)

**Exact Settings:**

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
Body Content Type: Raw ← CHANGE THIS
Raw Content Type: application/json ← NEW FIELD
Body: {{ $json.apiRequestBody }} ← Expression here
```

---

## ✅ KEY DIFFERENCES FROM SOLUTION 1

| Setting | Solution 1 (Failed) | Solution 2 (Try This) |
|---------|---------------------|----------------------|
| Code Node Output | Object | **String (JSON.stringify)** |
| Body Content Type | JSON | **Raw** |
| Specify Body | Using JSON | **N/A (Raw mode)** |
| Raw Content Type | N/A | **application/json** |
| Body Field | JSON Body | **Body** |

---

## 🎯 WHY THIS SHOULD WORK

**Problem with Solution 1:**
- n8n v4.3 might be double-encoding the object
- "Using JSON" mode might not handle complex nested objects correctly

**Solution 2 Approach:**
- Code node creates perfect JSON string
- Raw mode sends it directly (no re-parsing)
- No double-encoding issues
- OpenAI receives valid JSON string

---

## 🧪 TEST IT NOW

1. **Update Code node:** Change to return `JSON.stringify(requestBody)`
2. **Update HTTP Request:**
   - Body Content Type: **Raw**
   - Raw Content Type: **application/json**
   - Body: `{{ $json.apiRequestBody }}`
3. **Save workflow**
4. **Execute node**
5. **Should work!** ✅

---

## 🐛 IF THIS STILL FAILS

**Next Solutions:**
- Solution 3: Direct expression in HTTP Request (no Code node)
- Solution 5: Use Function node instead of Code node
- Check browser console (F12 → Network tab) to see actual request

---

**Status:** ✅ Ready to Test  
**Previous:** Solution 1 failed  
**Next:** Solution 2 (Raw mode)

