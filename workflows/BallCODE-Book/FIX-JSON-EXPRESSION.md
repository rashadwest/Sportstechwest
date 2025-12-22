# 🔧 Fix: Use Expression Instead of Raw JSON

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** Raw JSON with `{{ }}` expressions not working  
**Solution:** Use "Expression" mode with JSON.stringify  
**Fix Time:** 2 minutes

---

## 🎯 THE PROBLEM

When using "Using JSON" with raw JSON containing `{{ $json.context }}`, n8n might not be evaluating the expressions correctly, or the body isn't being sent properly.

---

## ✅ THE FIX: Use Expression Mode

### **Step 1: Change to Expression**

1. In your "OpenAI API Key" node
2. Find **"Specify Body"** - should be set to **"Using JSON"**
3. In the JSON Body field, look for **"Fixed"** and **"Expression"** buttons
4. Click **"Expression"** (the fx button)

### **Step 2: Paste This Expression**

In the expression field, paste this EXACT code:

```javascript
={{ JSON.stringify({
  "model": "gpt-4o",
  "temperature": 0.1,
  "max_tokens": 2000,
  "messages": [
    {
      "role": "system",
      "content": "You are an expert error diagnosis system. Analyze screenshots of errors and provide structured diagnosis."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": `Analyze this error screenshot and provide structured diagnosis:\n\nContext: ${$json.context}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  "errorType": "string",\n  "errorMessage": "string",\n  "affectedSystem": "string",\n  "likelyCause": "string",\n  "filesToFix": ["array", "of", "files"],\n  "severity": "low|medium|high|critical",\n  "canAutoFix": true/false,\n  "fixComplexity": "simple|moderate|complex"\n}`
        },
        {
          "type": "image_url",
          "image_url": {
            "url": $json.imageUrlForAPI || $json.screenshotUrl || "https://via.placeholder.com/800x600.png"
          }
        }
      ]
    }
  ]
}) }}
```

**Important Notes:**
- Starts with `={{` and ends with `}}`
- Uses `${$json.context}` instead of `{{ $json.context }}`
- Uses backticks `` ` `` for template strings
- Uses `JSON.stringify()` to convert to JSON string

### **Step 3: Verify Settings**

Make sure:
- ✅ **Send Body:** ON
- ✅ **Body Content Type:** JSON
- ✅ **Specify Body:** Using JSON
- ✅ **JSON Body:** Expression mode (fx button active)
- ✅ Expression starts with `={{` and ends with `}}`

### **Step 4: Save and Test**

1. Click **"Save"** on the workflow
2. Click **"Execute step"** on the node
3. Should work now! ✅

---

## 🔍 ALTERNATIVE: Check What's Being Sent

If it still doesn't work, check what's actually being sent:

1. Open browser Developer Console (F12)
2. Go to Network tab
3. Execute the node
4. Find the request to `api.openai.com`
5. Check the Request Payload
6. See if the body is actually being sent

---

## 🐛 IF STILL NOT WORKING

### **Option A: Use Code Node First**

Add a Code node before the HTTP Request node to prepare the body:

```javascript
const body = {
  "model": "gpt-4o",
  "temperature": 0.1,
  "max_tokens": 2000,
  "messages": [
    {
      "role": "system",
      "content": "You are an expert error diagnosis system. Analyze screenshots of errors and provide structured diagnosis."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": `Analyze this error screenshot and provide structured diagnosis:\n\nContext: ${$json.context}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  "errorType": "string",\n  "errorMessage": "string",\n  "affectedSystem": "string",\n  "likelyCause": "string",\n  "filesToFix": ["array", "of", "files"],\n  "severity": "low|medium|high|critical",\n  "canAutoFix": true/false,\n  "fixComplexity": "simple|moderate|complex"\n}`
        },
        {
          "type": "image_url",
          "image_url": {
            "url": $json.imageUrlForAPI || $json.screenshotUrl || "https://via.placeholder.com/800x600.png"
          }
        }
      ]
    }
  ]
};

return {
  json: {
    ...$json,
    requestBody: body
  }
};
```

Then in HTTP Request node:
- **Specify Body:** Using JSON
- **JSON Body (Expression):** `={{ JSON.stringify($json.requestBody) }}`

---

**Time:** 2 minutes  
**Status:** Ready to fix  
**Next:** Switch to Expression mode and paste the code above

