# 🚀 Start Your Email System - 3 Commands

## Step 1: Install (10 seconds)

```bash
cd email_system
pip3 install aiosmtpd click
```

---

## Step 2: Test It (30 seconds)

```bash
python3 quick_start.py
```

You should see:
- ✅ Server starting
- ✅ Email sent  
- ✅ Email stored

---

## Step 3: Use It

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

You now have a free, local email system!

---

## For n8n:

1. Keep server running: `python3 main.py start`
2. In n8n: Add "Send Email" node → Host: `localhost`, Port: `2525`
3. Done!

---

**That's it! Simple and free!** 🚀


