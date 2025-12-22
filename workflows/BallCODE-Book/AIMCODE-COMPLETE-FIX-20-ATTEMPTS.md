# 🎯 AIMCODE Complete Fix - 20+ Attempts Analysis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Attempts:** 20+  
**Methodology:** AIMCODE + Web Research + End-to-End Analysis  
**Status:** 🔴 CRITICAL - Found Root Cause

---

## 🔬 AIMCODE ANALYSIS (CLEAR Framework)

### **C - Clarity:**
**The Problem:**
- `apiRequestBody` exists in input with correct JSON
- HTTP Request node shows warning icon
- Error: "you must provide a model parameter"
- **Root Cause:** Expression `{{ $json.apiRequestBody }}` is in WRONG field

### **L - Logic:**
**Based on Research:**
1. **"Body Content Type"** = Dropdown to select "JSON" (literal value)
2. **"JSON Body"** = Field where you put the actual body content (expression)
3. **Current State:** Expression is in "Body Content Type" field (WRONG!)
4. **Should Be:** "Body Content Type" = "JSON", "JSON Body" = expression

### **E - Evidence:**
**From Web Research:**
- n8n HTTP Request node has TWO separate fields
- "Body Content Type" is a dropdown (JSON, Raw, Form-Data, etc.)
- "JSON Body" is where you put the actual JSON content
- Using expression in "Body Content Type" causes it to be used as Content-Type header value, not body

**From Image Analysis:**
- Warning icon next to `{{ $json.apiRequestBody }}` in "Body Content Type" field
- No visible "JSON Body" field shown (likely below scroll)
- Body preview shows JSON but it's being used incorrectly

### **A - Adaptation:**
**Solution:**
1. Set "Body Content Type" to literal "JSON" (dropdown)
2. Find "JSON Body" field (separate field below)
3. Put expression `={{ $json.apiRequestBody }}` in "JSON Body" field
4. Fix Custom Auth credential (has error JSON instead of auth config)

### **R - Results:**
**Expected:**
- ✅ Body Content Type = "JSON" (literal)
- ✅ JSON Body = `={{ $json.apiRequestBody }}` (expression)
- ✅ Request body sent correctly
- ✅ Model parameter received by OpenAI

---

## 🎯 THE EXACT PROBLEM

**You have:**
```
Body Content Type: {{ $json.apiRequestBody }} ← WRONG FIELD!
```

**You need:**
```
Body Content Type: JSON ← Literal dropdown value
JSON Body: {{ $json.apiRequestBody }} ← Expression in separate field
```

---

## ✅ COMPLETE FIX (Step-by-Step)

### **Step 1: Fix Body Content Type Field**

1. In "OpenAI API Key" HTTP Request node
2. Find **"Body Content Type"** field
3. **Clear the expression** `{{ $json.apiRequestBody }}`
4. **Select from dropdown:** `JSON` (literal value, not expression)

### **Step 2: Find and Use JSON Body Field**

1. Scroll down below "Body Content Type"
2. Find **"Specify Body"** dropdown
3. Set to: **"Using JSON"**
4. A new field will appear: **"JSON Body"**
5. In "JSON Body" field:
   - Click **"Expression" button** (fx icon)
   - Paste: `={{ $json.apiRequestBody }}`

### **Step 3: Verify All Settings**

**Exact Configuration:**
```
Method: POST
URL: https://api.openai.com/v1/chat/completions
Authentication: [Your credential]

Send Query Parameters: OFF
Send Headers: ON

Send Body: ON
Body Content Type: JSON ← Literal "JSON" from dropdown
Specify Body: Using JSON
JSON Body: {{ $json.apiRequestBody }} ← Expression here
```

### **Step 4: Fix Custom Auth Credential**

**The Custom Auth account has error JSON in it - this is wrong!**

1. Go to **Credentials** → **Custom Auth account**
2. The **JSON field** should NOT contain error messages
3. **Clear the error JSON**
4. **Leave it empty** OR configure properly for HTTP Header Auth

**Actually, you're using HTTP Header Auth, so:**
- The Custom Auth credential might not be needed
- Use "HTTP Header Auth" credential instead
- Set Header Name: `Authorization`
- Set Header Value: `Bearer sk-proj-...`

---

## 🔍 END-TO-END NODE CHECK

### **Complete Node Configuration:**

**Method:**
- ✅ POST

**URL:**
- ✅ `https://api.openai.com/v1/chat/completions`

**Authentication:**
- ⚠️ Check credential is correct
- Should be HTTP Header Auth with `Authorization: Bearer sk-proj-...`

**Send Query Parameters:**
- ✅ OFF

**Send Headers:**
- ✅ ON
- Header: `Authorization: Bearer sk-proj-...`

**Send Body:**
- ✅ ON

**Body Content Type:**
- ❌ Currently: `{{ $json.apiRequestBody }}` ← WRONG!
- ✅ Should be: `JSON` (literal from dropdown)

**Specify Body:**
- ✅ `Using JSON`

**JSON Body:**
- ❌ Currently: Empty or wrong
- ✅ Should be: `={{ $json.apiRequestBody }}` (expression)

---

## 🐛 WHY THIS HAPPENED

**Common Mistake:**
- n8n UI shows "Body Content Type" field first
- User thinks this is where the body goes
- Actually, "Body Content Type" is just the type selector
- "JSON Body" is a separate field below (easy to miss)

**The Fix:**
- "Body Content Type" = What type of body (JSON, Raw, Form-Data)
- "JSON Body" = The actual body content

---

## ✅ VERIFICATION CHECKLIST

After fixing:

- [ ] **Body Content Type:** "JSON" (from dropdown, not expression)
- [ ] **Specify Body:** "Using JSON"
- [ ] **JSON Body field exists** (below Specify Body)
- [ ] **JSON Body:** Expression mode (fx button active)
- [ ] **JSON Body expression:** `={{ $json.apiRequestBody }}`
- [ ] **Send Body:** ON
- [ ] **Custom Auth credential:** Fixed (no error JSON in it)

---

## 🧪 TEST IT

1. **Save workflow**
2. **Execute "OpenAI API Key" node**
3. **Expected:** Should work! ✅

**If still fails:**
- Check browser console (F12 → Network tab)
- See what's actually being sent
- Verify body is in request payload

---

## 📚 RESEARCH REFERENCES

**Sources:**
1. n8n Documentation: HTTP Request Node Body Configuration
2. n8n Community: "Body Content Type vs JSON Body" discussions
3. Web Search: n8n HTTP Request body configuration
4. AIMCODE Analysis: Field-by-field verification

**Key Finding:**
- "Body Content Type" and "JSON Body" are TWO SEPARATE FIELDS
- Expression goes in "JSON Body", not "Body Content Type"

---

**Time:** 2 minutes  
**Status:** Root cause identified  
**Next:** Fix the two fields correctly

