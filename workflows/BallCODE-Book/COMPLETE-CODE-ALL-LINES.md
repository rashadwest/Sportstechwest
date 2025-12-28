# ✅ COMPLETE CODE - ALL LINES (Copy Everything)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** "requestBody is not defined"  
**Cause:** Only return statement was copied, missing the `requestBody` definition  
**Fix:** Copy ALL lines below

---

## 📋 COPY ALL OF THIS (Start to Finish)

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

## ✅ WHAT YOU NEEDED

**You copied:**
```javascript
// Return as OBJECT (not stringified)
return {
  json: {
    ...$json,
    apiRequestBody: requestBody  // ← requestBody not defined!
  }
};
```

**You need:**
- ✅ Lines 1-2: Get `imageUrl` and `context`
- ✅ Lines 4-40: Define `requestBody` object
- ✅ Lines 42-47: Return statement

**ALL OF IT!**

---

## 🎯 STEP-BY-STEP

1. **Select ALL the code** above (from `// Get values` to the closing `};`)
2. **Copy it** (Ctrl+C / Cmd+C)
3. **Paste into Code node** (replace everything)
4. **Save**
5. **Test**

---

**Status:** ✅ Complete Code  
**Action:** Copy ALL lines, not just the return statement


