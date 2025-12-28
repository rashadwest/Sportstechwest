# 🔧 Fix: "JSON parameter needs to be valid JSON" Error

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** "JSON parameter needs to be valid JSON"  
**Cause:** Expression not producing valid JSON string  
**Fix:** Use simpler, validated expression  
**Fix Time:** 2 minutes

---

## 🎯 THE PROBLEM

The expression is not producing valid JSON. This happens when:
- Expression has syntax errors
- `JSON.stringify()` fails
- Expression returns undefined or invalid value
- Quotes or escaping issues

---

## ✅ THE FIX: Use Simpler Expression

### **Step 1: Use This Exact Expression**

**In your "OpenAI API Key" node:**
1. Make sure **Expression mode is ON** (fx button)
2. **Delete everything** in the JSON Body field
3. **Paste this EXACT code:**

```javascript
={{ JSON.stringify({
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
          text: "Analyze this error screenshot and provide structured diagnosis:\n\nContext: " + String($json.context || "Unknown error") + "\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
        },
        {
          type: "image_url",
          image_url: {
            url: String($json.imageUrlForAPI || $json.screenshotUrl || "https://via.placeholder.com/800x600.png?text=Error+Screenshot")
          }
        }
      ]
    }
  ]
}) }}
```

**Key Changes:**
- ✅ Removed quotes around object keys (JavaScript allows this)
- ✅ Used `String()` to ensure values are strings
- ✅ Simplified syntax
- ✅ Added fallbacks for all variables

---

## 🔍 ALTERNATIVE: Use Code Node First (More Reliable)

**If expression still fails, use this approach:**

### **Step 1: Add Code Node Before HTTP Request**

**Node Name:** `Prepare API Request Body`

**Code:**
```javascript
// Prepare the request body as a JavaScript object
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
            url: $json.imageUrlForAPI || $json.screenshotUrl || "https://via.placeholder.com/800x600.png?text=Error+Screenshot"
          }
        }
      ]
    }
  ]
};

// Return the body as a JSON string
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody),
    apiRequestBodyObject: requestBody
  }
};
```

### **Step 2: Update HTTP Request Node**

**In HTTP Request node:**
- **Specify Body:** Using JSON
- **JSON Body (Expression):** `={{ $json.apiRequestBody }}`

**OR use the object directly:**
- **Specify Body:** Using JSON
- **JSON Body (Expression):** `={{ JSON.stringify($json.apiRequestBodyObject) }}`

---

## 🐛 TROUBLESHOOTING

### **If still getting "invalid JSON":**

**Test the expression:**
1. Add a Code node after your expression
2. Check what it outputs:
```javascript
// Debug: See what the expression produces
return {
  json: {
    testExpression: $json.apiRequestBody || "undefined",
    testType: typeof ($json.apiRequestBody || "undefined")
  }
};
```

### **If expression returns undefined:**

**Check:**
1. Expression mode is ON (fx button)
2. Expression starts with `={{` and ends with `}}`
3. No syntax errors (check for missing quotes, brackets)
4. All variables exist in input data

### **If JSON.stringify fails:**

**Use Code Node approach** (Alternative above) - more reliable

---

## ✅ VERIFICATION

**After fixing:**
1. **Save the workflow**
2. **Execute the node**
3. **Check for errors:**
   - ✅ No "invalid JSON" error
   - ✅ Request is sent
   - ✅ API responds (even if rate limited)

---

## 🎯 QUICKEST FIX

**Use Code Node approach:**
1. Add "Prepare API Request Body" Code node (code above)
2. In HTTP Request node, use: `={{ $json.apiRequestBody }}`
3. This is more reliable than complex expressions

---

**Time:** 2 minutes  
**Status:** Ready to fix  
**Next:** Use the simpler expression OR Code node approach


