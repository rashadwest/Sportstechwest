# 📧 Email Setup Action Plan - FREE Option
## Set Up info@ballcode.co and schools@ballcode.co

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Status:** 🎯 Ready to Execute  
**Cost:** **FREE** (Zoho Mail Free Plan)

---

## 🎯 QUICK SUMMARY

**What We're Doing:**
- Setting up FREE email for `ballcode.co` domain
- Creating `info@ballcode.co` and `schools@ballcode.co`
- Using **Zoho Mail Free** (completely free, 5 users max)

**Time Required:** 30-45 minutes  
**Cost:** $0/month

---

## ✅ PRE-SETUP CHECKLIST

Before starting, you need:

- [ ] **GoDaddy Account Access**
  - Log into your GoDaddy account
  - Confirm you own `ballcode.co`
  - Find "DNS Management" or "Domain Settings"

- [ ] **Email Addresses to Create**
  - `info@ballcode.co` (main contact)
  - `schools@ballcode.co` (school inquiries)

- [ ] **30-45 Minutes** (one-time setup)

---

## 📋 STEP-BY-STEP PLAN

### **STEP 1: Get DNS Access from GoDaddy** (5-10 minutes)

**Action Items:**

1. **Log into GoDaddy:**
   - Go to: https://www.godaddy.com
   - Sign in to your account

2. **Find Domain Management:**
   - Click "My Products" or "Domains"
   - Find `ballcode.co` in your domain list
   - Click on `ballcode.co`

3. **Access DNS Settings:**
   - Look for "DNS" or "DNS Management" tab
   - Click on it
   - You should see current DNS records (A, CNAME, etc.)

4. **Verify Access:**
   - Can you see DNS records?
   - Can you add/edit records?
   - If yes → Proceed to Step 2
   - If no → Contact GoDaddy support to enable DNS access

**✅ Checkpoint:** You can see and edit DNS records for ballcode.co

---

### **STEP 2: Sign Up for Zoho Mail Free** (10 minutes)

**Action Items:**

1. **Go to Zoho Mail:**
   - Visit: https://www.zoho.com/mail/
   - Click "Sign Up Now" or "Get Started Free"

2. **Choose Free Plan:**
   - Select "Mail Free" plan
   - Click "Get Started" or "Sign Up"

3. **Enter Domain:**
   - When asked for domain, enter: `ballcode.co`
   - Click "Add Domain" or "Continue"

4. **Create Zoho Account:**
   - Enter your personal email (for Zoho account)
   - Create password
   - Verify email (check your personal email for verification link)

5. **Verify Domain Ownership:**
   - Zoho will ask you to verify you own `ballcode.co`
   - They'll provide a TXT record to add to DNS
   - **Don't add it yet** - we'll do this in Step 3

**✅ Checkpoint:** You have a Zoho Mail account with `ballcode.co` added (pending verification)

---

### **STEP 3: Add Verification TXT Record** (5 minutes)

**Action Items:**

1. **Get TXT Record from Zoho:**
   - In Zoho Mail dashboard, find "Domain Verification"
   - Copy the TXT record value (looks like: `zoho-verification=xxxxx`)

2. **Add TXT Record to GoDaddy DNS:**
   - Go back to GoDaddy DNS settings (from Step 1)
   - Click "Add" or "Add Record"
   - Select record type: **TXT**
   - **Name/Host:** `@` or leave blank (depends on GoDaddy interface)
   - **Value:** Paste the TXT record from Zoho
   - **TTL:** 3600 (or default)
   - Click "Save"

3. **Wait for Verification:**
   - Go back to Zoho Mail dashboard
   - Click "Verify" or "Check Verification"
   - Wait 5-15 minutes (DNS propagation)
   - Zoho will confirm when verified

**✅ Checkpoint:** Domain verified in Zoho Mail

---

### **STEP 4: Add MX Records to GoDaddy** (5 minutes)

**Action Items:**

1. **Get MX Records from Zoho:**
   - In Zoho Mail dashboard, go to "MX Records" or "Email Setup"
   - Zoho will provide MX records (usually 2 records)
   - Example MX records from Zoho:
     ```
     Priority: 10, Host: @, Value: mx.zoho.com
     Priority: 20, Host: @, Value: mx2.zoho.com
     ```

2. **Add MX Records to GoDaddy:**
   - Go to GoDaddy DNS settings
   - Find existing MX records (if any) - **DELETE THEM FIRST**
   - Click "Add" or "Add Record"
   - Select record type: **MX**
   - **Priority:** Enter priority number (e.g., 10)
   - **Name/Host:** `@` or leave blank
   - **Value/Points To:** Enter MX server (e.g., `mx.zoho.com`)
   - **TTL:** 3600 (or default)
   - Click "Save"
   - **Repeat for each MX record** (usually 2 records)

3. **Verify MX Records:**
   - Wait 15-30 minutes for DNS propagation
   - Zoho Mail dashboard should show "MX Records Configured" or similar

**✅ Checkpoint:** MX records added and verified

---

### **STEP 5: Create Email Addresses** (5 minutes)

**Action Items:**

1. **Go to Zoho Mail Users:**
   - In Zoho Mail dashboard, find "Users" or "Email Accounts"
   - Click "Add User" or "Create Email"

2. **Create info@ballcode.co:**
   - Email: `info`
   - Domain: `ballcode.co` (should be pre-filled)
   - Password: Create a strong password
   - Display Name: "BallCODE Info" (optional)
   - Click "Create" or "Add"

3. **Create schools@ballcode.co:**
   - Click "Add User" again
   - Email: `schools`
   - Domain: `ballcode.co`
   - Password: Create a strong password
   - Display Name: "BallCODE Schools" (optional)
   - Click "Create" or "Add"

4. **Verify Creation:**
   - Both addresses should appear in your user list
   - Status should show "Active"

**✅ Checkpoint:** Both email addresses created and active

---

### **STEP 6: Test Email** (5 minutes)

**Action Items:**

1. **Access Zoho Mail Webmail:**
   - Go to: https://mail.zoho.com
   - Sign in with: `info@ballcode.co`
   - Use the password you created

2. **Send Test Email:**
   - Compose new email
   - To: `schools@ballcode.co`
   - Subject: "Test Email"
   - Body: "This is a test"
   - Send

3. **Check schools@ballcode.co:**
   - Sign out
   - Sign in with: `schools@ballcode.co`
   - Check inbox for test email
   - If received → ✅ Email is working!

4. **Test from External Email:**
   - Send email from your personal email (Gmail, etc.)
   - To: `info@ballcode.co`
   - Check Zoho Mail inbox
   - If received → ✅ External emails working!

**✅ Checkpoint:** Emails sending and receiving correctly

---

## 🎉 COMPLETION CHECKLIST

Once all steps are complete, verify:

- [ ] Domain verified in Zoho Mail
- [ ] MX records added to GoDaddy DNS
- [ ] `info@ballcode.co` created and active
- [ ] `schools@ballcode.co` created and active
- [ ] Can send emails from both addresses
- [ ] Can receive emails at both addresses
- [ ] External emails (from Gmail, etc.) can reach your addresses

---

## 📧 ACCESSING YOUR EMAIL

**Webmail:**
- URL: https://mail.zoho.com
- Sign in with: `info@ballcode.co` or `schools@ballcode.co`
- Use password you created

**Mobile App:**
- Download "Zoho Mail" app (iOS/Android)
- Sign in with your email address

**Email Client (Optional):**
- Can configure in Outlook, Apple Mail, etc.
- IMAP settings provided by Zoho

---

## 🆘 TROUBLESHOOTING

### **Problem: Can't Access DNS in GoDaddy**
**Solution:**
- Contact GoDaddy support
- Ask them to enable DNS management for ballcode.co
- Or ask them to add the MX records for you

### **Problem: Domain Verification Failing**
**Solution:**
- Double-check TXT record is exactly as Zoho provided
- Wait longer (up to 24 hours for DNS propagation)
- Contact Zoho support if still failing

### **Problem: MX Records Not Working**
**Solution:**
- Verify MX records are exactly as Zoho provided
- Make sure you deleted old MX records first
- Wait 30-60 minutes for DNS propagation
- Use online MX checker: https://mxtoolbox.com

### **Problem: Can't Receive External Emails**
**Solution:**
- Check MX records are correct
- Wait for DNS propagation (can take up to 48 hours)
- Check spam folder
- Verify email address is spelled correctly

---

## 💡 ZOHO MAIL FREE LIMITATIONS

**What You Get (Free):**
- ✅ 5 email accounts max
- ✅ 5GB storage per account
- ✅ Webmail access
- ✅ Mobile apps
- ✅ Basic spam filtering
- ✅ Professional email addresses

**What You Don't Get (Free):**
- ❌ Email forwarding (can't forward to Gmail)
- ❌ Custom email signatures (basic only)
- ❌ Advanced features (available in paid plans)

**For BallCODE, Free Plan is Perfect:**
- You only need 2 email addresses (info@ and schools@)
- 5GB storage is plenty for business emails
- All essential features included

---

## 📞 NEXT STEPS AFTER SETUP

Once email is working:

1. **Update Website:**
   - Email links already point to `info@ballcode.co` and `schools@ballcode.co`
   - No website changes needed!

2. **Set Up Email Signatures:**
   - Create professional signatures in Zoho Mail
   - Include BallCODE branding

3. **Monitor Emails:**
   - Check both inboxes regularly
   - Set up email notifications on your phone

4. **Share Access (If Needed):**
   - Can add team members (up to 5 total on free plan)
   - Each person gets their own login

---

## 🎯 QUICK REFERENCE

**Zoho Mail Free:**
- URL: https://www.zoho.com/mail/
- Cost: FREE
- Max Users: 5
- Storage: 5GB per user

**GoDaddy DNS:**
- URL: https://www.godaddy.com
- Login → My Products → Domains → ballcode.co → DNS

**Email Addresses:**
- `info@ballcode.co` (main contact)
- `schools@ballcode.co` (school inquiries)

**Webmail Access:**
- URL: https://mail.zoho.com

---

## ✅ READY TO START?

**Your Action Items:**
1. Log into GoDaddy and verify DNS access
2. Sign up for Zoho Mail Free
3. Follow steps 1-6 above
4. Test email functionality

**Estimated Time:** 30-45 minutes total

**Questions?** Refer back to this guide or contact support if you get stuck!

---

**Status:** 🎯 Ready to Execute - Follow steps above to set up FREE email for ballcode.co


