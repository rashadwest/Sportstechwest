# Garvis Orchestrator Fix - Editable Expression Only

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Issue:** Can only edit the left expression, not the right value

---

## 🔧 The Fix

Since you can only edit the **left expression** field, change it to use JavaScript `.includes()` method:

**Change the left expression from:**
```
{{ $json.systems }}
```

**To:**
```
{{ $json.systems.includes('book') }}
```

This returns `true` or `false` (boolean), so you'll also need to:
1. Change the **Operator Type** to **"Boolean"**
2. Change the **Operation** to **"Equals"**
3. The right value should be **`true`**

---

## 📋 Step-by-Step Fix

### **For "Route: Book System?" Node:**

1. **Click on the Route node**
2. **In the condition, find the Left Value expression field**
3. **Change it to:**
   ```
   {{ $json.systems.includes('book') }}
   ```
4. **Change Operator Type dropdown** to **"Boolean"**
5. **Change Operation dropdown** to **"Equals"**
6. **Right Value should be** `true` (should auto-update)
7. **Click "Save"**

### **Repeat for All Route Nodes:**

- **Route: Book System?** → `{{ $json.systems.includes('book') }}`
- **Route: Curriculum System?** → `{{ $json.systems.includes('curriculum') }}`
- **Route: Game System?** → `{{ $json.systems.includes('game') }}`
- **Route: Website System?** → `{{ $json.systems.includes('website') }}`
- **Route: Sales System?** → `{{ $json.systems.includes('sales') }}`

**For each:**
- Operator Type: **Boolean**
- Operation: **Equals**
- Right Value: **true**

---

## ✅ That's It!

This way you only need to edit the left expression field (which you can edit) and change the operator type/operation dropdowns.

---

**Version:** 1.0  
**Created:** December 23, 2025  
**Status:** ✅ Simple Fix - Edit Expression Only


