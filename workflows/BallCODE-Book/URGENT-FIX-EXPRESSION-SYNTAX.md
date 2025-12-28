# 🚨 URGENT FIX: Expression Syntax in Raw Mode

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** Preview shows `={"model"...` (starts with `=`) - expression syntax issue  
**Fix:** Remove `={{ }}` wrapper or use different syntax  
**Time:** 1 minute

---

## 🎯 THE PROBLEM (From Screenshot)

**What I See:**
- Body field: `={{ $json.apiRequestBody }}`
- Preview shows: `={"model":"gpt-4o"...` (starts with `=`)
- Error: "Could not parse JSON body"

**The Issue:**
- The `={{ }}` syntax in Raw mode might be causing n8n to add `=` prefix
- Or the expression is evaluating incorrectly
- Raw mode might need simpler syntax

---

## ✅ SOLUTION: Remove Expression Wrapper

**In Body field (Raw mode):**

**Instead of:**
```
={{ $json.apiRequestBody }}
```

**Try this (no `={{ }}` wrapper):**
```
$json.apiRequestBody
```

**Or try this (just `{{ }}`):**
```
{{ $json.apiRequestBody }}
```

**Or try this (String wrapper):**
```
String($json.apiRequestBody)
```

---

## ✅ ALTERNATIVE: Add Code Node to Prepare Body

**Add Code node BEFORE HTTP Request:**

```javascript
// Get the apiRequestBody string
const bodyString = $json.apiRequestBody;

// Clean it - remove any extra encoding
let cleanBody;
try {
  // If it's already a string, use it
  if (typeof bodyString === 'string') {
    cleanBody = bodyString;
  } else {
    // If it's an object, stringify it
    cleanBody = JSON.stringify(bodyString);
  }
} catch (e) {
  cleanBody = String(bodyString);
}

return {
  json: {
    ...$json,
    cleanRequestBody: cleanBody
  }
};
```

**Then in HTTP Request (Raw mode):**
```
Body: {{ $json.cleanRequestBody }}
```

---

## ✅ BEST SOLUTION: Use Code Node to Return Object

**Change Code node to return OBJECT (not string):**

```javascript
// ... (build requestBody object) ...

// Return as OBJECT
return {
  json: {
    ...$json,
    apiRequestBody: requestBody  // Object, not JSON.stringify()
  }
};
```

**Then change HTTP Request to JSON mode:**
```
Body Content Type: JSON
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }}
```

**Why:** "Using JSON" mode handles objects correctly, avoids string encoding issues.

---

## 🧪 TEST IN ORDER

1. **First:** Try `$json.apiRequestBody` (no `={{ }}`)
2. **If fails:** Try `{{ $json.apiRequestBody }}` (no `=`)
3. **If fails:** Add Code node to clean body
4. **If fails:** Change Code node to return object, use JSON mode

---

**Status:** 🚨 URGENT  
**Action:** Try removing `={{ }}` wrapper first


