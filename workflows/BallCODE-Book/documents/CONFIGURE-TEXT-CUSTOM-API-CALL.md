# ✅ Configure Text Resource + Custom API Call for Vision

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Solution:** Use "Text" resource + "Custom API Call" to call chat completions endpoint

---

## 🎯 PERFECT! HERE'S HOW TO CONFIGURE IT

**You have:**
- ✅ Resource: "Text"
- ✅ Operation: "Custom API Call" (available!)

**We'll configure "Custom API Call" to use the chat completions endpoint.**

---

## ✅ STEP-BY-STEP CONFIGURATION

### Step 1: Select "Custom API Call"

1. **Resource:** Keep as "Text" ✅
2. **Operation:** Select "Custom API Call" ✅

---

### Step 2: Configure Custom API Call

**After selecting "Custom API Call", you should see additional fields. Configure them:**

#### **Endpoint/Path:**
```
chat/completions
```
or
```
/v1/chat/completions
```

#### **Method:**
```
POST
```

#### **Body (JSON):**

**Enter this in the Body field (use Expression mode if available):**

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
            "url": "={{ $json.screenshotUrl || 'data:image/png;base64,' + $json.screenshotFile?.data }}"
          }
        }
      ]
    }
  ]
}
```

---

### Step 3: Authentication

**Verify:**
- **Credential:** "OpenAI account" is selected ✅
- The API key will be automatically included in the Authorization header

---

### Step 4: Headers (if needed)

**If there's a Headers section, ensure:**
- `Content-Type: application/json`

---

## 🔍 WHAT FIELDS TO LOOK FOR

**After selecting "Custom API Call", you should see:**

1. **Endpoint/Path** - Enter: `chat/completions`
2. **Method** - Should be `POST` (or select it)
3. **Body** - Enter the JSON above
4. **Headers** - Should auto-populate, or add `Content-Type: application/json`
5. **Authentication** - Should use your OpenAI credential automatically

---

## 📝 IF YOU DON'T SEE THESE FIELDS

**If the UI doesn't show endpoint/body fields immediately:**

1. **Look for a "Settings" tab** - Configuration might be there
2. **Check for "Additional Fields" or "Options"** - Might be collapsed
3. **Look for a "+" or "Add" button** - To add custom fields
4. **Check if there's a "Request" or "API" section** - Fields might be grouped

---

## 🧪 TEST IT

**After configuring:**

1. **Click "Execute step"** button (top right)
2. **Check the OUTPUT panel** - Should show:
   ```json
   {
     "choices": [
       {
         "message": {
           "content": "{...diagnosis JSON...}"
         }
       }
     ]
   }
   ```

3. **If it works:** The "Parse Diagnosis" node should extract the diagnosis correctly

---

## ✅ WHY THIS WORKS

**"Text" resource + "Custom API Call":**
- The resource name is just a UI label
- "Custom API Call" lets us call ANY OpenAI endpoint
- We're calling `/v1/chat/completions` (chat endpoint)
- This works perfectly for vision analysis with gpt-4o

**This is actually a valid approach!** The resource label doesn't matter - what matters is the actual API endpoint we're calling.

---

## 🎯 SUMMARY

**Configuration:**
- Resource: "Text" ✅
- Operation: "Custom API Call" ✅
- Endpoint: `chat/completions` ✅
- Method: `POST` ✅
- Body: Chat completion JSON with image_url ✅
- Model: `gpt-4o` ✅

**This should work!** Let me know what fields you see after selecting "Custom API Call" and we'll configure them together.

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Ready to Configure



