# 📋 HTTP Request Node - Exact Settings Checklist

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Quick Reference:** Exact settings for OpenAI API HTTP Request node

---

## ✅ EXACT SETTINGS TO CONFIGURE

### **1. Method**
```
POST
```

### **2. URL**
```
https://api.openai.com/v1/chat/completions
```

### **3. Authentication**
```
Type: HTTP Header Auth
Credential: OpenAI API Key
```

**Credential Details:**
- **Name:** OpenAI API Key
- **Header Name:** `Authorization`
- **Header Value:** `Bearer sk-your-key-here`

### **4. Send Query Parameters**
```
OFF (toggle left/white)
```

### **5. Send Headers**
```
ON (toggle right/blue) ← TURN THIS ON
```

**OR manually add:**
- **Name:** `Content-Type`
- **Value:** `application/json`

### **6. Send Body**
```
ON (toggle right/blue) ← TURN THIS ON
```

### **7. Body Content Type**
```
JSON
```

### **8. Specify Body**
```
Using JSON
```

### **9. JSON Body**
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

---

## 🔑 CREDENTIAL SETUP (If Not Created Yet)

### **Step-by-Step:**

1. In HTTP Request node, click **"Authentication"** dropdown
2. Select **"HTTP Header Auth"**
3. Click **"Credential to connect with"** → **"Create New"** or **"+"**
4. Search: **"HTTP Header Auth"**
5. Fill in:
   - **Name:** `OpenAI API Key`
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer sk-your-actual-api-key`
6. Click **"Save"**
7. Back in node, select the credential you just created

---

## 🎯 VISUAL CHECKLIST

When you look at your node, it should show:

```
┌─────────────────────────────────────┐
│ Method: [POST ▼]                   │
│ URL: https://api.openai.com/...    │
│                                     │
│ Authentication:                     │
│ [HTTP Header Auth ▼]                │
│ Credential: [OpenAI API Key ▼]     │
│                                     │
│ ☐ Send Query Parameters (OFF)      │
│ ☑ Send Headers (ON) ← TURN ON     │
│ ☑ Send Body (ON) ← TURN ON        │
│                                     │
│ Body Content Type: [JSON ▼]        │
│ Specify Body: [Using JSON ▼]       │
│                                     │
│ JSON Body: [JSON code above]       │
└─────────────────────────────────────┘
```

---

## ⚡ QUICK FIX FOR YOUR CURRENT ERROR

**Your current state:**
- ❌ Send Body: OFF
- ❌ Authentication: None
- ❌ Send Headers: OFF

**What to do:**
1. **Toggle "Send Body" to ON** ← This fixes "model parameter" error
2. **Set Authentication to HTTP Header Auth** ← This adds API key
3. **Toggle "Send Headers" to ON** ← This sends headers
4. **Paste JSON body** (from section 9 above)
5. **Click "Save"**
6. **Click "Execute step"** to test

---

## ✅ SUCCESS INDICATORS

After fixing, when you execute the node:

**Good Response:**
- Status: `200 OK`
- Response contains: `choices[0].message.content`
- No error messages

**Bad Response (still needs fixing):**
- Status: `401` = Authentication issue (check API key)
- Status: `400` = Body issue (check JSON format)
- Status: `429` = Rate limit (wait a moment)

---

**Time:** 5 minutes to fix  
**Status:** Ready to configure  
**Follow:** FIX-HTTP-NODE-ERROR.md for detailed steps


