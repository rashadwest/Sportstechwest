# ✅ Complete Email System - Ready to Use!

## 🎯 What You Have

A **completely free, local email system** that:
- ✅ Works in Cursor (CLI commands)
- ✅ Integrates with n8n (SMTP server)
- ✅ Stores emails locally (SQLite database)
- ✅ Zero cost (no paid services)
- ✅ Simple setup (< 2 minutes)

---

## 🚀 EASIEST WAY TO START (3 Steps)

### Step 1: Install Dependencies (10 seconds)

```bash
cd email_system
pip3 install aiosmtpd click
```

---

### Step 2: Test It Works (30 seconds)

```bash
python3 quick_start.py
```

**OR use the test script:**
```bash
./TEST-NOW.sh
```

You should see:
- ✅ Server starting
- ✅ Email sent
- ✅ Email stored in database

---

### Step 3: Start Using It

**Terminal 1 - Start Server:**
```bash
python3 main.py start
```
**Keep this running!**

**Terminal 2 - Send Email:**
```bash
python3 main.py send --to test@ballcode.co --subject "Hello" --body "This works!"
```

**Terminal 2 - List Emails:**
```bash
python3 main.py list
python3 main.py read 1
```

---

## 📧 All Available Commands

```bash
# Start email server
python3 main.py start

# Send email
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"

# List emails
python3 main.py list
python3 main.py list --unread
python3 main.py list --folder sent

# Read email
python3 main.py read <ID>

# Search emails
python3 main.py search "query"

# Delete email
python3 main.py delete <ID>

# Statistics
python3 main.py stats
```

---

## 🔧 n8n Integration

### 1. Keep Server Running
```bash
python3 main.py start
```

### 2. Configure n8n

In n8n workflow, add **"Send Email"** node:

**SMTP Settings:**
- **Host:** `localhost`
- **Port:** `2525`
- **User:** (leave empty)
- **Password:** (leave empty)
- **SSL/TLS:** Disabled

**Email Settings:**
- **From:** `noreply@ballcode.co`
- **To:** `={{ $json.email }}` (or recipient)
- **Subject:** `={{ $json.subject }}`
- **Message:** `={{ $json.message }}`

### 3. Test

Execute the n8n workflow. Email will be sent to your local server and stored in the database.

---

## 📁 File Structure

```
email_system/
├── main.py              # Main entry point (use this!)
├── quick_start.py       # Quick test script
├── cli.py               # CLI commands
├── server.py            # SMTP server
├── storage.py           # Email storage (SQLite)
├── sender.py            # Email sender
├── requirements.txt     # Dependencies
├── TEST-NOW.sh          # Test script
└── emails.db            # Email database (created automatically)
```

---

## 🎯 Quick Reference

**Start Server:**
```bash
python3 main.py start
```

**Send Email:**
```bash
python3 main.py send --to info@ballcode.co --subject "Test" --body "Hello!"
```

**Check Emails:**
```bash
python3 main.py list
```

**Read Email:**
```bash
python3 main.py read 1
```

---

## 🆘 Troubleshooting

### "Module not found" error
```bash
pip3 install aiosmtpd click
```

### "Port already in use"
```bash
# Use different port
python3 main.py start --port 2526
```

### "Connection refused" in n8n
- Make sure server is running: `python3 main.py start`
- Check port is 2525
- If n8n is on different machine, use machine IP instead of `localhost`

---

## ✅ Success Checklist

- [ ] Dependencies installed (`pip3 install aiosmtpd click`)
- [ ] Quick test passed (`python3 quick_start.py`)
- [ ] Server starts (`python3 main.py start`)
- [ ] Can send email (`python3 main.py send ...`)
- [ ] Can list emails (`python3 main.py list`)
- [ ] n8n configured (localhost:2525)

---

## 🎉 You're Done!

**Total setup time: < 2 minutes**

You now have a **free, local email system** that works with Cursor and n8n!

**Cost: $0/month | Setup: < 2 minutes | All Local & Free!** 🚀



