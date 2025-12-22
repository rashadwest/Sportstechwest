# 🚀 Quick Installation Guide

## Step 1: Install Dependencies (30 seconds)

```bash
cd email_system
pip3 install -r requirements.txt
```

That's it! You're ready to go.

---

## Step 2: Test It Works (30 seconds)

```bash
python3 quick_start.py
```

You should see:
- ✅ Server starting
- ✅ Email sent
- ✅ Email stored in database

---

## Step 3: Start Using It

### Start the Email Server

```bash
python3 main.py start
```

Keep this running in a terminal.

### Send an Email (in another terminal)

```bash
python3 main.py send --to info@ballcode.co --subject "Hello" --body "This is a test!"
```

### List Emails

```bash
python3 main.py list
```

### Read an Email

```bash
python3 main.py read 1
```

---

## That's It! 🎉

You now have a free, local email system that works with Cursor and n8n!

**Total setup time: < 2 minutes**


