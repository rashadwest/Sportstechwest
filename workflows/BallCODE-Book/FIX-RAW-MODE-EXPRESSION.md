# ⚡ FIX: Raw Mode Expression Issue

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** Raw mode with `={{ $json.apiRequestBody }}` is sending invalid JSON  
**Root Cause:** Expression evaluation is adding `=` prefix or double-encoding  
**Fix:** Use different expression syntax or fix Code node output  
**Time:** 2 minutes

---

## 🎯 THE PROBLEM (From Screenshot)

**What I See:**
- ✅ Body Content Type: Raw
- ✅ Content Type: application/json
- ✅ Body: `={{ $json.apiRequestBody }}`
- ❌ Preview shows: `={"model":"gpt-4o"...` (starts with `=`)
- ❌ Error: "Could not parse JSON body"

**The Issue:**
- The expression `={{ $json.apiRequestBody }}` is evaluating incorrectly
- The `=` prefix suggests n8n is treating it as a template literal
- Or the string itself has encoding issues

---

## ✅ SOLUTION A: Remove Expression Wrapper

**Try this in Body field:**

Instead of:
```
={{ $json.apiRequestBody }}
```

Try:
```
$json.apiRequestBody
```

**Or:**
```
{{ $json.apiRequestBody }}
```

**Why:** The `={{ }}` syntax might be causing issues in Raw mode.

---

## ✅ SOLUTION B: Use JSON.parse() in Expression

**In Body field (Expression mode):**

```javascript
JSON.stringify(JSON.parse($json.apiRequestBody))
```

**Why:** This re-parses and re-stringifies, ensuring clean JSON.

---

## ✅ SOLUTION C: Fix Code Node to Return Object (Then Use JSON Mode)

**Change Code Node to return OBJECT (not string):**

```javascript
// ... (same requestBody object) ...

// Return as OBJECT (not stringified)
return {
  json: {
    ...$json,
    apiRequestBody: requestBody  // Object, not JSON.stringify()
  }
};
```

**Then change HTTP Request:**
```
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }}
```

**Why:** "Using JSON" mode handles objects correctly, avoids string issues.

---

## ✅ SOLUTION D: Use String() Wrapper

**In Body field (Expression mode):**

```javascript
String($json.apiRequestBody)
```

**Why:** Ensures it's treated as a string, not an expression result.

---

## 🧪 TEST EACH SOLUTION

**Try in order:**

1. **Solution A:** Remove `={{ }}` wrapper, use `$json.apiRequestBody`
2. **Solution C:** Change Code node to return object, use "Using JSON" mode
3. **Solution B:** Use `JSON.stringify(JSON.parse(...))`
4. **Solution D:** Use `String()` wrapper

---

## 🎯 RECOMMENDED: Solution C (Object → JSON Mode)

**This is most reliable:**

**Code Node:**
```javascript
const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";
const context = $json.context || "Unknown error";

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

**HTTP Request:**
```
Send Body: ON
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }}

Send Headers: ON
Headers:
  - Content-Type: application/json
  - Authorization: Bearer sk-proj-...
```

---

**Status:** ✅ Multiple Solutions  
**Recommended:** Solution C (Object → JSON Mode)  
**Next:** Try Solution C first


