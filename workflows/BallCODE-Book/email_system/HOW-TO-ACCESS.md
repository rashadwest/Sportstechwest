# 📧 How to Access Your Email System

## 🚀 Quick Start (3 Steps)

### Step 1: Start the Email Server

**Open Terminal 1 (keep this running):**
```bash
cd email_system
python3 main.py start
```

You should see:
```
🚀 Starting SMTP server on localhost:2525
📧 Ready to receive emails!
💡 Configure n8n SMTP to: localhost:2525
```

**Keep this terminal open!** The server needs to keep running.

---

### Step 2: Send an Email (Terminal 2)

**Open a NEW terminal window:**
```bash
cd email_system
python3 main.py send --to test@ballcode.co --subject "Hello" --body "This is a test email!"
```

You should see:
```
✅ Email sent to test@ballcode.co
```

---

### Step 3: Check Your Emails

**In the same Terminal 2:**
```bash
# List all emails
python3 main.py list

# List unread emails
python3 main.py list --unread

# Read a specific email
python3 main.py read 1
```

---

## 📋 All Commands

### **Start Server**
```bash
cd email_system
python3 main.py start
```
**Keep this running!**

### **Send Email**
```bash
python3 main.py send --to EMAIL --subject "SUBJECT" --body "MESSAGE"
```

### **List Emails**
```bash
python3 main.py list              # All emails
python3 main.py list --unread     # Unread only
python3 main.py list --folder sent # Sent folder
```

### **Read Email**
```bash
python3 main.py read <ID>
```
Example: `python3 main.py read 1`

### **Search Emails**
```bash
python3 main.py search "query"
```

### **Delete Email**
```bash
python3 main.py delete <ID>
```

### **Statistics**
```bash
python3 main.py stats
```

---

## 🔧 First Time Setup

If you haven't installed dependencies yet:

```bash
cd email_system
pip3 install aiosmtpd click
```

Then test it works:
```bash
python3 quick_start.py
```

---

## 📧 Access Methods

### **Method 1: CLI Commands (Cursor Terminal)**
- Use `python3 main.py` commands
- Works directly in Cursor
- No external email client needed

### **Method 2: Python Code (in Cursor)**
```python
from email_system import EmailStorage, EmailSender

# Send email
sender = EmailSender(smtp_host='localhost', smtp_port=2525)
sender.send(to_address='info@ballcode.co', subject='Test', body='Hello!')

# List emails
storage = EmailStorage()
emails = storage.list_emails()
for email in emails:
    print(f"{email['subject']} from {email['from_address']}")
```

### **Method 3: n8n Integration**
- Start server: `python3 main.py start`
- In n8n: Add "Send Email" node
- Configure: Host `localhost`, Port `2525`
- Send emails through n8n workflows

---

## 🗂️ Where Emails Are Stored

**Database Location:**
```
email_system/emails.db
```

**View Database:**
```bash
cd email_system
sqlite3 emails.db "SELECT * FROM emails;"
```

---

## 🆘 Troubleshooting

### **"Module not found" error**
```bash
pip3 install aiosmtpd click
```

### **"Port already in use"**
```bash
# Use different port
python3 main.py start --port 2526
```

### **"Connection refused" in n8n**
- Make sure server is running: `python3 main.py start`
- Check port is 2525
- If n8n is on different machine, use machine IP instead of `localhost`

### **Can't find emails**
```bash
# Check database exists
ls -la email_system/emails.db

# List emails
python3 main.py list

# Check stats
python3 main.py stats
```

---

## ✅ Quick Checklist

- [ ] Dependencies installed (`pip3 install aiosmtpd click`)
- [ ] Server started (`python3 main.py start`)
- [ ] Test email sent (`python3 main.py send ...`)
- [ ] Emails listed (`python3 main.py list`)
- [ ] Email read (`python3 main.py read 1`)

---

## 🎯 Typical Workflow

1. **Start server** (Terminal 1 - keep running):
   ```bash
   python3 main.py start
   ```

2. **Send/receive emails** (Terminal 2 or n8n):
   ```bash
   python3 main.py send --to ... --subject ... --body ...
   ```

3. **Check emails** (Terminal 2):
   ```bash
   python3 main.py list
   python3 main.py read <ID>
   ```

---

**That's it! Your email system is accessible from Cursor terminal or n8n!** 🎉



