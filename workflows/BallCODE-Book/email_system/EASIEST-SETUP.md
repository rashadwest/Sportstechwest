# 🎯 Easiest Setup - 3 Steps to Working Email System

## ✅ Step 1: Install (Copy & Paste)

```bash
cd email_system
pip3 install aiosmtpd click
```

**Time: 10 seconds**

---

## ✅ Step 2: Test It Works (Copy & Paste)

```bash
python3 quick_start.py
```

**Time: 30 seconds**

You should see:
- Server starting ✅
- Email sent ✅
- Email stored ✅

---

## ✅ Step 3: Use It (Copy & Paste)

### Terminal 1: Start Server
```bash
python3 main.py start
```
**Keep this running!**

### Terminal 2: Send Email
```bash
python3 main.py send --to test@ballcode.co --subject "Hello" --body "This works!"
```

### Terminal 2: Check Emails
```bash
python3 main.py list
python3 main.py read 1
```

---

## 🎉 Done!

**Total time: 2 minutes**

You now have:
- ✅ Free email system (no cost)
- ✅ Works locally (no internet needed)
- ✅ Works in Cursor (CLI commands)
- ✅ Ready for n8n (localhost:2525)

---

## 🔧 For n8n Integration

1. **Keep server running:** `python3 main.py start`

2. **In n8n:** Add "Send Email" node:
   - Host: `localhost`
   - Port: `2525`
   - From: `noreply@ballcode.co`
   - To: Your recipient
   - Subject: Your subject
   - Message: Your message

3. **Done!** n8n can now send emails through your local system.

---

## 📚 All Commands

```bash
# Start server
python3 main.py start

# Send email
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"

# List emails
python3 main.py list
python3 main.py list --unread

# Read email
python3 main.py read ID

# Search emails
python3 main.py search "query"

# Delete email
python3 main.py delete ID

# Statistics
python3 main.py stats
```

---

**That's it! Simple, free, and works immediately.** 🚀



