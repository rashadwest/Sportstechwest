# Check OpenAI API Credits & Status
## Verify OpenAI API is Working in n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Purpose:** Verify OpenAI API has credits and is configured correctly

---

## 🔍 QUICK CHECK

### Option 1: Use Check Script (Recommended)

```bash
# Set your API key (if not already set)
export OPENAI_API_KEY='your-api-key-here'

# Run check script
python3 scripts/check-openai-credits.py
```

**This will:**
- ✅ Test API connection
- ✅ Verify API key is valid
- ✅ Check if credits are available
- ✅ Show usage information

---

### Option 2: Check in n8n UI

1. **Open n8n workflow**
2. **Click on "AI Analyze Request" node**
3. **Click "Execute Node"** (test button)
4. **Check for errors:**
   - ✅ **Success** = API working, has credits
   - ❌ **401 Error** = Invalid API key
   - ❌ **402 Error** = No credits/payment required
   - ❌ **429 Error** = Rate limited

---

### Option 3: Check OpenAI Dashboard

1. **Go to:** https://platform.openai.com/usage
2. **Check usage dashboard:**
   - View API usage
   - Check credit balance
   - See request history

3. **Go to:** https://platform.openai.com/account/billing
4. **Check billing:**
   - Payment method status
   - Credit balance
   - Usage limits

---

## 🐛 COMMON ISSUES

### Issue 1: "Invalid API Key" (401 Error)

**Fix:**
1. Go to: https://platform.openai.com/api-keys
2. Create new API key or copy existing
3. Update in n8n:
   - Credentials → OpenAI API
   - Update API key
   - Save

---

### Issue 2: "Payment Required" (402 Error)

**Fix:**
1. Go to: https://platform.openai.com/account/billing
2. Add payment method
3. Add credits to account
4. Wait a few minutes for activation

---

### Issue 3: "Rate Limited" (429 Error)

**Fix:**
1. Wait a few minutes
2. Check usage limits
3. Consider upgrading plan if needed
4. Reduce request frequency

---

### Issue 4: API Key Not Set in n8n

**Fix:**
1. Open n8n → Credentials
2. Add → OpenAI API
3. Enter API key
4. Save as "OpenAI API"
5. Update "AI Analyze Request" node to use this credential

---

## ✅ VERIFICATION CHECKLIST

- [ ] API key is set in n8n credentials
- [ ] API key is valid (test with script)
- [ ] Credits available (check dashboard)
- [ ] Payment method added (if needed)
- [ ] n8n node uses correct credential
- [ ] Test execution works in n8n

---

## 📊 EXPECTED BEHAVIOR

### When API Has Credits:
- ✅ n8n node executes successfully
- ✅ AI returns JSON response
- ✅ No error messages
- ✅ Workflow continues normally

### When API Has No Credits:
- ❌ 402 error: "Payment required"
- ❌ Node fails to execute
- ❌ Workflow stops at AI node

---

## 🔧 QUICK FIXES

### If Credits Are Low:
1. **Add credits:** https://platform.openai.com/account/billing
2. **Check usage:** https://platform.openai.com/usage
3. **Monitor spending:** Set up usage alerts

### If API Key Invalid:
1. **Get new key:** https://platform.openai.com/api-keys
2. **Update in n8n:** Credentials → OpenAI API
3. **Test again:** Execute node in n8n

---

## 📋 USEFUL LINKS

- **API Keys:** https://platform.openai.com/api-keys
- **Usage Dashboard:** https://platform.openai.com/usage
- **Billing:** https://platform.openai.com/account/billing
- **Documentation:** https://platform.openai.com/docs

---

**Version:** OpenAI Credits Check Guide  
**Created:** December 12, 2025  
**Status:** Ready to Use



