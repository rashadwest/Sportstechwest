# Check Unity Password in GitHub Secrets

**Date:** December 24, 2025  
**Issue:** Workflow failed - may be incorrect password

---

## 🔍 HOW TO CHECK/UPDATE PASSWORD

### **Step 1: Go to GitHub Secrets**

**I opened the page for you:**
```
https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
```

**On that page:**
- You'll see all your secrets listed
- Look for `UNITY_EMAIL` and `UNITY_PASSWORD`
- **Note:** You can't VIEW the password (for security), but you can UPDATE it

---

### **Step 2: Update UNITY_PASSWORD**

**If you think the password is wrong:**

1. **Find `UNITY_PASSWORD` in the list**
2. **Click the pencil icon** (edit) next to it
3. **Enter the correct password**
4. **Click "Update secret"**

**OR if it doesn't exist:**

1. **Click "New repository secret"**
2. **Name:** `UNITY_PASSWORD`
3. **Secret:** Your Unity account password
4. **Click "Add secret"**

---

## ✅ WHAT PASSWORD TO USE

**Use the SAME password you used for local activation:**

- The password you typed into the activation script
- Your Unity account password (the one you use to log into Unity Hub)
- Make sure there are no extra spaces
- Make sure it's the exact password

---

## 🔍 CHECK THE WORKFLOW LOGS

**I also opened the workflow run page for you.**

**To see the exact error:**
1. Click on the failed step (usually "Build Unity WebGL")
2. Scroll through the logs
3. Look for error messages like:
   - "Authentication failed"
   - "Invalid credentials"
   - "License activation failed"
   - "Password incorrect"

**This will tell us if it's a password issue or something else.**

---

## 📋 COMMON PASSWORD ISSUES

1. **Extra spaces:**
   - Wrong: ` mypassword ` (spaces before/after)
   - Right: `mypassword`

2. **Wrong password:**
   - Make sure it's the Unity account password
   - Not your GitHub password
   - Not your email password

3. **2FA enabled:**
   - If you have 2FA on Unity account, you might need an app-specific password
   - Check Unity account settings

4. **Password changed:**
   - If you changed your Unity password recently
   - Update it in GitHub Secrets

---

## 🎯 QUICK CHECKLIST

- [ ] Go to GitHub Secrets page (I opened it)
- [ ] Check if `UNITY_PASSWORD` exists
- [ ] Update it with the correct password
- [ ] Check workflow logs for exact error (I opened it)
- [ ] Re-run the workflow after updating

---

## ✅ AFTER UPDATING

**Once you update the password:**

1. **Trigger the workflow again:**
   - I can trigger it for you, OR
   - You can push a change, OR
   - Find the "Run workflow" button

2. **Watch it run:**
   - Should activate license successfully
   - Should build successfully
   - Should deploy successfully

---

## 🚀 SUMMARY

**What to do:**
1. ✅ Check GitHub Secrets (I opened it)
2. ✅ Update `UNITY_PASSWORD` if needed
3. ✅ Check workflow logs for exact error (I opened it)
4. ✅ Re-run workflow after fixing

**I opened both pages for you - check the password and the error logs!**


