# ✅ Exact Fields to Fill - Step by Step

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Your Fields:**
1. Body Content Type - Raw ✅
2. Content Type - text/html ❌ (needs to change)
3. Body - (needs expression)

---

## ✅ EXACT VALUES TO SET

### **Field 1: Body Content Type**
- **Current:** Raw ✅
- **Keep it:** Raw (this is correct!)

### **Field 2: Content Type**
- **Current:** text/html ❌
- **Change to:** `application/json` or `JSON`
- **How:** Click dropdown, select "application/json" or type it

### **Field 3: Body**
- **Current:** (empty)
- **Set to:** `={{ $json.apiRequestBody }}`
- **How:** 
  1. Click in the Body field
  2. Click "Expression" button (fx icon) if available
  3. Paste: `={{ $json.apiRequestBody }}`

---

## ✅ COMPLETE CONFIGURATION

```
Body Content Type: Raw ✅
Content Type: application/json ← CHANGE THIS
Body: {{ $json.apiRequestBody }} ← PUT EXPRESSION HERE
```

---

## 🎯 STEP-BY-STEP

1. **Body Content Type:** Already "Raw" ✅ - Keep it!

2. **Content Type:**
   - Click the dropdown or field
   - Change from "text/html" to "application/json"
   - OR type: `application/json`

3. **Body:**
   - Click in the Body field
   - If you see "Fixed" and "Expression" buttons, click "Expression" (fx)
   - Paste: `={{ $json.apiRequestBody }}`
   - If no buttons, just paste: `={{ $json.apiRequestBody }}`

4. **Save and Test:**
   - Click "Save"
   - Click "Execute step"
   - Should work! ✅

---

**Time:** 1 minute  
**Status:** Ready to fix  
**Next:** Change Content Type to "application/json" and add expression to Body

