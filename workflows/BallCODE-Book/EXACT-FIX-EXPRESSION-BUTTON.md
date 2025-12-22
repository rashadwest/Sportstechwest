# ⚡ EXACT FIX: Click Expression Button

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem:** "JSON" field has literal JSON instead of expression  
**Fix:** Click Expression button (fx icon)  
**Time:** 30 seconds

---

## 🎯 WHAT I SEE IN YOUR SCREENSHOT

**The "JSON" field shows:**
```json
{
  "model": "gpt-4o",
  "temperature": 0.1,
  ...
}
```

**This is LITERAL JSON** - n8n is trying to validate it and failing.

**It should show:**
```
={{ $json.apiRequestBody }}
```

**This is an EXPRESSION** - n8n will evaluate it dynamically.

---

## ✅ EXACT STEPS (30 SECONDS)

### **Step 1: Find Expression Button**

1. In "OpenAI API Key" node
2. Scroll to **"JSON"** field (under "Specify Body")
3. **Look for "fx" icon** or "Expression" button
4. **Click it** - Field should change appearance

### **Step 2: Replace Content**

1. **Delete everything** in the JSON field
2. **Type or paste:**
   ```
   {{ $json.apiRequestBody }}
   ```

### **Step 3: Save and Test**

1. **Click "Save"**
2. **Execute node**
3. **Should work!** ✅

---

## 🎯 VISUAL GUIDE

**BEFORE (Wrong):**
```
┌─────────────────────────────┐
│ JSON                        │
│ [JSON]                      │ ← Literal mode
│ {                           │
│   "model": "gpt-4o",        │
│   ...                       │
│ }                           │
└─────────────────────────────┘
```

**AFTER (Correct):**
```
┌─────────────────────────────┐
│ JSON                        │
│ [Expression] [fx]           │ ← Expression mode active
│ {{ $json.apiRequestBody }}  │ ← Expression
└─────────────────────────────┘
```

---

## ⚠️ IF EXPRESSION BUTTON NOT VISIBLE

**Try this:**
1. **Click in the JSON field** (to focus it)
2. **Look for "fx" icon** in the field toolbar
3. **Or right-click** in the field → "Use Expression"
4. **Or look for toggle** that says "Expression" or "JSON"

---

## 🐛 IF STILL FAILS AFTER EXPRESSION

**Then check `apiRequestBody` type:**

**If it's a string (from `JSON.stringify()`):**
- Change to Raw mode:
  ```
  Body Content Type: Raw
  Raw Content Type: application/json
  Body: {{ $json.apiRequestBody }}
  ```

**If it's an object:**
- Keep "Using JSON" mode (current setup)

---

**Status:** ✅ Ready to Fix  
**Action:** Click Expression button, use `={{ $json.apiRequestBody }}`

