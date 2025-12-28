# 🤖 Human vs Robot Tasks - Email System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Project:** BallCODE Email System  
**Purpose:** Clear separation of human-required tasks vs automated tasks

---

## ✅ SYSTEM STATUS: READY TO GO

**The email system is fully built and ready to use!**

---

## 👤 HUMAN TASKS (MUST DO)

### **1. Start the Email Server** ⚠️ REQUIRED
- **Action:** Run `python3 main.py start` in terminal
- **When:** Every time you want to use the email system
- **Why:** Server must be running to receive/send emails
- **Frequency:** Once per session (keep terminal open)

**Command:**
```bash
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system
python3 main.py start
```

---

### **2. Add Credentials (Optional - Only If You Want Features)**

#### **A. Slack Webhook URL** (Optional)
- **Action:** Get webhook URL from Slack, edit `email_config.json`
- **When:** Only if you want Slack notifications
- **Why:** Enables Slack notifications (no email client needed)
- **Location:** `email_system/email_config.json`

**How:**
1. Get Slack webhook URL from Slack workspace
2. Edit `email_config.json`:
   ```json
   "slack": {
     "webhook_url": "YOUR_WEBHOOK_URL",
     "enabled": true
   }
   ```

#### **B. Apollo API Key** (Optional)
- **Action:** Get API key from Apollo.io, edit `email_config.json`
- **When:** Only if you want lead enrichment
- **Why:** Enables automatic lead enrichment from emails
- **Location:** `email_system/email_config.json`

**How:**
1. Get Apollo API key from Apollo.io account
2. Edit `email_config.json`:
   ```json
   "apollo": {
     "api_key": "YOUR_API_KEY",
     "enabled": true
   }
   ```

---

### **3. Send Emails** (When You Want To)
- **Action:** Run `python3 main.py send` command
- **When:** Whenever you want to send an email
- **Why:** You control what emails to send
- **Frequency:** As needed

**Command:**
```bash
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"
```

---

## 🤖 ROBOT TASKS (AUTOMATED)

### **✅ Already Done by Robot:**
- ✅ Installed all dependencies (aiosmtpd, click, requests)
- ✅ Created configuration files (`email_config.json`)
- ✅ Built email server (SMTP on localhost:2525)
- ✅ Built email storage (SQLite database)
- ✅ Built email sender (send emails via CLI or n8n)
- ✅ Built Slack integration (ready - just needs webhook URL)
- ✅ Built Apollo integration (ready - just needs API key)
- ✅ Built sales pipeline (automatic lead creation)
- ✅ Fixed all import issues
- ✅ Created all documentation

### **✅ Automatic When Server Running:**
- ✅ Receives emails automatically (stores in database)
- ✅ Creates sales leads automatically (from incoming emails)
- ✅ Sends Slack notifications (if webhook configured)
- ✅ Enriches leads with Apollo (if API key configured)
- ✅ Tracks leads in sales pipeline (automatic)

### **✅ Robot Can Do:**
- ✅ List emails (`python3 main.py list`)
- ✅ Read emails (`python3 main.py read <ID>`)
- ✅ Search emails (`python3 main.py search "query"`)
- ✅ Delete emails (`python3 main.py delete <ID>`)
- ✅ Show statistics (`python3 main.py stats`)
- ✅ Process sales pipeline (automatic)
- ✅ Send emails via n8n (automatic when configured)

---

## 📋 QUICK REFERENCE

### **Human Must Do:**
1. ⚠️ **Start server:** `python3 main.py start` (keep running)
2. 📝 **Send emails:** `python3 main.py send ...` (when you want)
3. 🔑 **Add credentials:** Edit `email_config.json` (optional)

### **Robot Does Automatically:**
- ✅ Receives emails
- ✅ Stores emails in database
- ✅ Creates sales leads
- ✅ Sends Slack notifications (if configured)
- ✅ Enriches with Apollo (if configured)
- ✅ Tracks in sales pipeline

---

## 🎯 MINIMUM HUMAN EFFORT

**To use the system, you only need to:**

1. **Start server once:** `python3 main.py start`
2. **Send emails when needed:** `python3 main.py send ...`

**That's it!** Everything else is automated.

**Optional enhancements:**
- Add Slack webhook for notifications
- Add Apollo API key for lead enrichment

---

## ✅ SYSTEM READINESS CHECKLIST

- [x] **Dependencies installed** (robot did it)
- [x] **Configuration created** (robot did it)
- [x] **All code built** (robot did it)
- [x] **Import issues fixed** (robot did it)
- [ ] **Server started** (human must do - `python3 main.py start`)
- [ ] **Credentials added** (human optional - Slack/Apollo)

---

## 🚀 READY TO GO!

**The system is ready. You just need to:**
1. Start the server: `python3 main.py start`
2. Start using it!

**Everything else is automated!** 🎉

---

**Saved to memory for email project reference.**



