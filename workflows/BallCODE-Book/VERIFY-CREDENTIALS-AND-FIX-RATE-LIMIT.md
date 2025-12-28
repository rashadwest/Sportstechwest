# 🔍 Verify Credentials & Fix Rate Limit (429 Error)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** HTTP 429 - "Too many requests"  
**Solution:** Verify credentials + Add rate limit handling  
**Fix Time:** 5 minutes

---

## 🔍 STEP 1: Verify Your Credentials

### **Check Your API Key:**

1. **In n8n UI:**
   - Go to **Credentials** (left sidebar)
   - Find **"OpenAI API Key"** or **"Custom Auth account"**
   - Click to view/edit

2. **Verify Header Value:**
   - **Header Name:** Should be `Authorization`
   - **Header Value:** Should be `Bearer sk-proj-...` (your actual key)
   - **Important:** Must have space after "Bearer"

3. **Test Your API Key Directly:**

```bash
# Test if your API key works
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer sk-proj-YOUR-KEY-HERE" \
  -H "Content-Type: application/json"
```

**Expected Response:**
- ✅ **200 OK:** Key works, you'll see list of models
- ❌ **401 Unauthorized:** Key is wrong or expired
- ❌ **429 Too Many Requests:** Key works but rate limited

---

## 🔍 STEP 2: Check Which API Key You're Using

### **In Your HTTP Request Node:**

1. Click on **"OpenAI API Key"** node
2. Check **"Authentication"** section
3. See which credential is selected:
   - **"Custom Auth account"** (what you're using)
   - Or **"OpenAI API Key"** (if you created a new one)

### **Verify the Credential:**

1. Click the **pencil/edit icon** next to the credential dropdown
2. Check the **Header Value**:
   - Should start with `Bearer sk-proj-`
   - Should be your actual OpenAI API key
   - Should match the key in your OpenAI account

### **Get Your API Key from OpenAI:**

1. Go to: https://platform.openai.com/api-keys
2. Find your active API key
3. Copy it
4. In n8n credential, set Header Value to: `Bearer sk-proj-YOUR-KEY`

---

## ✅ STEP 3: Fix Rate Limit (429 Error)

### **Solution A: Add Delay Between Requests**

**Add Wait Node Before HTTP Request:**

1. **Add "Wait" node** before "Vision Analysis (HTTP Request)"
2. **Set wait time:** 2-3 seconds
3. This spaces out requests

**Or use Code Node:**

**Node Name:** `Rate Limit Delay`

**Code:**
```javascript
// Add delay to prevent rate limiting
const lastCall = $getWorkflowStaticData('global').lastApiCall || 0;
const now = Date.now();
const minDelay = 2000; // 2 seconds minimum between calls
const timeSinceLastCall = now - lastCall;

if (timeSinceLastCall < minDelay) {
  const waitTime = minDelay - timeSinceLastCall;
  // Return wait instruction
  return {
    json: {
      ...$json,
      waitTime: waitTime,
      needsWait: true
    }
  };
}

// Update last call time
$getWorkflowStaticData('global').lastApiCall = now;

return {
  json: {
    ...$json,
    needsWait: false,
    proceed: true
  }
};
```

**Add Wait Node:**
- If `needsWait === true`, wait for `waitTime` milliseconds
- Then proceed to HTTP Request

---

### **Solution B: Use Batching (As OpenAI Suggests)**

**Add to HTTP Request Node Options:**

1. In your HTTP Request node
2. Click **"Options"** section
3. Click **"Add option"**
4. Select **"Timeout"** or **"Retry"**

**Or add delay in JSON body:**

Actually, batching won't help here - you need to space out requests.

---

### **Solution C: Use Mock Responses for Testing**

**Best Solution for Testing:**

Replace HTTP Request nodes with Mock Code nodes:
- **No rate limits**
- **No costs**
- **Instant responses**

**See:** `MOCK-RESPONSES-READY-TO-USE.md` for ready code

---

## 🎯 QUICK FIX RIGHT NOW

### **Option 1: Wait 5 Minutes**

1. **Stop testing for 5 minutes**
2. **Let rate limit reset**
3. **Test again**

### **Option 2: Verify Credential and Add Delay**

1. **Check credential** (Step 1 above)
2. **Add Wait node** before HTTP Request (2-3 seconds)
3. **Test again**

### **Option 3: Use Mocks**

1. **Replace HTTP Request with Mock Code node**
2. **Test workflow** (no rate limits)
3. **Switch back to real API** when ready for production

---

## 🔍 VERIFY CREDENTIAL IS CORRECT

### **Test Your API Key:**

```bash
# Replace YOUR-KEY with your actual key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer sk-proj-YOUR-KEY" \
  -H "Content-Type: application/json"
```

**If it works:**
- ✅ Credential is correct
- ✅ Issue is just rate limiting
- ✅ Wait 5 minutes and try again

**If it fails with 401:**
- ❌ Credential is wrong
- ❌ Update the Header Value in n8n
- ❌ Make sure it's `Bearer sk-proj-...` (with space)

---

## 📋 CHECKLIST

**Verify Credentials:**
- [ ] Check credential Header Name = `Authorization`
- [ ] Check credential Header Value = `Bearer sk-proj-...`
- [ ] Test API key directly with curl
- [ ] Verify key works (200 OK response)

**Fix Rate Limit:**
- [ ] Add Wait node (2-3 seconds) before HTTP Request
- [ ] OR use Mock responses for testing
- [ ] OR wait 5 minutes between tests

---

## ✅ RECOMMENDED APPROACH

**For Testing:**
1. ✅ Use Mock Code nodes (no rate limits, no cost)
2. ✅ Test entire workflow flow
3. ✅ Verify all connections work

**For Production:**
1. ✅ Use real HTTP Request nodes
2. ✅ Add Wait node (2-3 seconds) before API calls
3. ✅ Handle 429 errors with retry logic

---

**Status:** Rate limit confirmed (429)  
**Next:** Verify credentials + Add delay OR use mocks  
**Time:** 5 minutes to fix


