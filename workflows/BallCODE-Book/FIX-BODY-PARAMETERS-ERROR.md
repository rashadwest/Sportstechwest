# 🔧 Fix: Body Parameters Issue - "you must provide a model parameter"

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** Using "Body Parameters" instead of raw JSON  
**Fix Time:** 1 minute  
**Status:** 🔴 CRITICAL FIX

---

## 🎯 THE PROBLEM

You're using:
- ❌ **Specify Body:** "Using Fields Below"
- ❌ **Body Parameters:** Name="Body", Value={JSON}

This wraps your JSON incorrectly. OpenAI expects raw JSON, not form-encoded data.

---

## ✅ THE FIX (1 MINUTE)

### **Step 1: Change Specify Body Setting**

1. In your "OpenAI API Key" node
2. Find **"Specify Body"** dropdown
3. Change it from **"Using Fields Below"** to **"Using JSON"**

### **Step 2: Remove Body Parameters**

1. Delete the "Body Parameters" section
2. Click the trash icon next to the "Body" parameter
3. Or just ignore it - it won't be used anymore

### **Step 3: Add JSON Body Field**

After changing to "Using JSON", a new field will appear:
- **Label:** "JSON Body" or "Body"
- **Type:** Large text area

### **Step 4: Paste This JSON**

In the new JSON Body field, paste this:

```json
{
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
          "text": "Analyze this error screenshot and provide structured diagnosis:\n\nContext: {{ $json.context }}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "={{ $json.imageUrlForAPI }}"
          }
        }
      ]
    }
  ]
}
```

### **Step 5: Save and Test**

1. Click **"Save"** on the workflow
2. Click **"Execute step"** on the node
3. Should work now! ✅

---

## 📋 WHAT CHANGES

**Before (Wrong):**
```
Specify Body: "Using Fields Below"
Body Parameters:
  Name: "Body"
  Value: {JSON here}
```

**After (Correct):**
```
Specify Body: "Using JSON"
JSON Body: {JSON here directly}
```

---

## ✅ VERIFICATION

After the fix:
- [ ] "Specify Body" = "Using JSON"
- [ ] "Body Parameters" section is gone or ignored
- [ ] "JSON Body" field appears with your JSON
- [ ] JSON contains `"model": "gpt-4o"`
- [ ] "Send Body" toggle is ON

---

## 🎯 WHY THIS FIXES IT

**"Using Fields Below" (Body Parameters):**
- Sends data as form-encoded or key-value pairs
- Wraps JSON in a parameter structure
- OpenAI doesn't recognize it as valid JSON

**"Using JSON" (Raw JSON):**
- Sends raw JSON directly in request body
- OpenAI receives it exactly as you wrote it
- Works perfectly! ✅

---

**Time:** 1 minute  
**Status:** Ready to fix  
**Next:** Change "Specify Body" to "Using JSON" and paste JSON directly


