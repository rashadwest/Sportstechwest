# ⚡ FIX: Enable Expression Mode in JSON Field

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Problem Found:** "JSON" field has literal JSON, not expression  
**Fix:** Enable Expression mode and use `$json.apiRequestBody`  
**Time:** 1 minute

---

## 🎯 THE PROBLEM (From Screenshot)

**What I See:**
- ✅ INPUT has `apiRequestBody` (stringified JSON)
- ❌ HTTP Request "JSON" field has **literal JSON object** (not expression)
- ❌ Error: "JSON parameter needs to be valid JSON"

**The Issue:**
- The "JSON" field is in **literal mode** (showing static JSON)
- It needs to be in **Expression mode** to reference `$json.apiRequestBody`
- n8n is trying to validate the literal JSON and failing

---

## ✅ THE FIX (1 MINUTE)

### **Step 1: Enable Expression Mode**

1. In "OpenAI API Key" HTTP Request node
2. Find the **"JSON"** field (in "Specify Body" section)
3. **Click the "Expression" button** (fx icon) - This is CRITICAL!
4. The field should change to show expression editor

### **Step 2: Enter Expression**

1. **Delete the literal JSON** that's currently there
2. **Paste this expression:**
   ```
   {{ $json.apiRequestBody }}
   ```

### **Step 3: Verify Settings**

**Check these are correct:**
- ✅ **Send Body:** ON
- ✅ **Body Content Type:** JSON
- ✅ **Specify Body:** Using JSON
- ✅ **JSON field:** Expression mode (fx button active/blue)
- ✅ **Expression:** `={{ $json.apiRequestBody }}`

---

## 🎯 WHY THIS FAILED

**The Error:**
- "JSON parameter needs to be valid JSON"
- This happens when n8n tries to validate the JSON field
- It's seeing a literal JSON object that it can't parse correctly

**The Fix:**
- Expression mode tells n8n: "This is dynamic data, evaluate it"
- `$json.apiRequestBody` pulls the value from previous node
- n8n will use that value as the body

---

## ⚠️ IMPORTANT: Check apiRequestBody Type

**From your INPUT, I see:**
- `apiRequestBody` is a **string** (stringified JSON)

**This means you have TWO options:**

### **Option A: Use Raw Mode (For String)**

If `apiRequestBody` is a string:
```
Body Content Type: Raw
Raw Content Type: application/json
Body: {{ $json.apiRequestBody }}
```

### **Option B: Change Code Node to Return Object**

If you want to use "Using JSON" mode:
- Code node should return object (not `JSON.stringify()`)
- Then use "Using JSON" mode

---

## 🧪 TEST IT

1. **Click Expression button** (fx) in JSON field
2. **Delete literal JSON**
3. **Paste:** `={{ $json.apiRequestBody }}`
4. **Save workflow**
5. **Execute node**
6. **Should work!** ✅

---

## 🐛 IF STILL FAILS

**Check the type of `apiRequestBody`:**

**If it's a string:**
- Use Raw mode (Option A above)

**If it's an object:**
- Use "Using JSON" mode (current setup)

**To check type, add debug Code node:**
```javascript
return {
  json: {
    ...$json,
    debug_type: typeof $json.apiRequestBody,
    debug_isString: typeof $json.apiRequestBody === 'string',
    debug_isObject: typeof $json.apiRequestBody === 'object'
  }
};
```

---

**Status:** ✅ Ready to Fix  
**Problem:** Expression mode not enabled  
**Fix:** Click fx button, use `={{ $json.apiRequestBody }}`


