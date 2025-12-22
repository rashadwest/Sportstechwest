# AIMCODE n8n: Permanent Memory - propertyValues[itemName] Error Solution

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 11, 2025  
**Purpose:** Permanent memory for solving "propertyValues[itemName] is not iterable" error  
**Methodology:** AIMCODE n8n Focus

---

## 🧠 PERMANENT MEMORY: Always Remember

### When You See "propertyValues[itemName] is not iterable":

**1. Root Cause:**
- n8n expects arrays directly, not nested in `{parameters: [...]}` wrappers
- Common in HTTP Request, IF, and Switch nodes
- Version compatibility issue between workflow format and n8n version

**2. Always Check These First:**
- ✅ HTTP Request nodes: `headerParameters.parameters` → Remove wrapper
- ✅ HTTP Request nodes: `bodyParameters.parameters` → Use `jsonBody` instead
- ✅ IF nodes: `conditions.boolean.values` → Should be `conditions.boolean[]` directly
- ✅ Switch nodes: `rules.conditions.values` → Should be `rules.values[].conditions[]`

**3. Quick Fix Pattern:**
```
Find: {parameters: [...]}
Fix: Remove wrapper, use array directly

Find: {values: [...]}  
Fix: Check if should be array directly (not nested object)

Find: Complex nesting
Fix: Simplify to direct structure
```

---

## 🛠️ AUTOMATED FIX (Always Use This First)

```bash
python3 fix-n8n-import-error.py workflow.json
# Creates: workflow-FIXED.json
```

**What it fixes:**
- ✅ Removes `headerParameters.parameters` → Uses `options.headers`
- ✅ Removes `bodyParameters.parameters` → Uses `jsonBody`
- ✅ Fixes `conditions.boolean.values` → Direct array
- ✅ Fixes `rules.conditions.values` → Correct structure

---

## 📋 MANUAL FIX CHECKLIST (If Script Doesn't Work)

### HTTP Request Nodes:
- [ ] Remove `headerParameters.parameters` structure
- [ ] Remove `bodyParameters.parameters` structure  
- [ ] Use `options.headers` object for headers
- [ ] Use `jsonBody` with expression mode for body
- [ ] Set `bodyContentType: "json"`
- [ ] Set `specifyBody: "json"`

### IF Nodes:
- [ ] Ensure `conditions.boolean` is array directly
- [ ] Remove any `values` wrapper
- [ ] Each condition is object in array

### Switch Nodes:
- [ ] Use `rules.values` array structure
- [ ] Each rule has `conditions[]` array and `outputKey`
- [ ] `conditions` is array directly

---

## 🎯 CORRECT STRUCTURES (Reference)

### HTTP Request - Headers:
```json
❌ WRONG: "headerParameters": {"parameters": [{"name": "Accept", "value": "..."}]}
✅ CORRECT: "options": {"headers": {"Accept": "..."}}
```

### HTTP Request - Body:
```json
❌ WRONG: "bodyParameters": {"parameters": [{"name": "ref", "value": "main"}]}
✅ CORRECT: "jsonBody": "={\"ref\":\"main\"}", "bodyContentType": "json"
```

### IF Node - Conditions:
```json
❌ WRONG: "conditions": {"boolean": {"values": [...]}}
✅ CORRECT: "conditions": {"boolean": [...]}
```

### Switch Node - Rules:
```json
❌ WRONG: "rules": {"conditions": {"values": [...]}}
✅ CORRECT: "rules": {"values": [{"conditions": [...], "outputKey": "..."}]}
```

---

## 💡 AIMCODE n8n Methodology Applied

**CLEAR Framework:**
- **C** - Clarity: Error is structure mismatch, not logic error
- **L** - Logic: n8n expects direct arrays, not nested wrappers
- **E** - Examples: HTTP Request, IF, Switch nodes all have same pattern
- **A** - Adaptation: Remove wrappers, simplify structures
- **R** - Results: Workflow imports successfully

**Systematic Approach:**
1. Identify problematic nodes (HTTP Request, IF, Switch)
2. Find nested `parameters` or `values` wrappers
3. Remove wrappers, use direct structures
4. Validate JSON structure
5. Test import

---

## 🚀 ALWAYS DO THIS

**When encountering import errors:**

1. **Run automated fix script first:**
   ```bash
   python3 fix-n8n-import-error.py workflow.json
   ```

2. **If script doesn't work, manually check:**
   - Search for `"parameters":` in JSON
   - Search for `"values":` nested in objects
   - Simplify to direct array structures

3. **Validate JSON:**
   ```bash
   python3 -m json.tool workflow.json > /dev/null
   ```

4. **Import and test**

---

**Status:** ✅ Permanent Memory Saved  
**Reusability:** Always applicable  
**Methodology:** AIMCODE n8n Focus


