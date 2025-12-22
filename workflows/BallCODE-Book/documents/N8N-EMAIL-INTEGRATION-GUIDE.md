# n8n Email Integration Guide
## How to Send Emails Through BallCODE Local Email System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Complete guide to integrate n8n with local email system

---

## 🎯 Overview

This guide shows you how to configure n8n to send emails through your local BallCODE email system, eliminating the need for external email services.

---

## 📋 Prerequisites

1. **Local Email Server Running:**
   ```bash
   python3 -m email_system.cli start
   ```
   Server should be running on `localhost:2525`

2. **n8n Installed:**
   - n8n should be running (locally or on server)
   - Access to n8n workflow editor

---

## 🔧 Step 1: Start Local Email Server

**In Cursor Terminal:**
```bash
cd email_system
python3 -m email_system.cli start
```

**Expected Output:**
```
🚀 Starting SMTP server on localhost:2525
📧 Ready to receive emails!
💡 Configure n8n SMTP to: localhost:2525
```

**Keep this running** - The server needs to be running for n8n to send emails.

---

## 📧 Step 2: Configure n8n SMTP Node

### **Option A: Using "Send Email" Node**

1. **Add Node:**
   - In n8n workflow, click "+" to add node
   - Search for "Send Email" or "Email Send"
   - Add `n8n-nodes-base.emailSend` node

2. **Configure SMTP Settings:**
   - **Host:** `localhost` (or your machine IP if n8n is on different machine)
   - **Port:** `2525`
   - **User:** (leave empty - local server doesn't require auth)
   - **Password:** (leave empty)
   - **SSL/TLS:** Disabled (for local server)

3. **Configure Email Fields:**
   - **From Email:** `noreply@ballcode.co` (or your email address)
   - **To Email:** `={{ $json.email }}` (or recipient email)
   - **Subject:** `={{ $json.subject }}` (or email subject)
   - **Message:** `={{ $json.message }}` (or email body)
   - **Email Type:** `text` or `html`

4. **Test:**
   - Click "Execute Node" to test
   - Check email server terminal for confirmation
   - List emails: `python3 -m email_system.cli list`

---

### **Option B: Using Code Node (Advanced)**

If you need more control, use a Code node with Python:

```python
import smtplib
from email.mime.text import MIMEText

# Get data from previous node
to_email = $json.email
subject = $json.subject
body = $json.message

# Create message
msg = MIMEText(body)
msg['From'] = 'noreply@ballcode.co'
msg['To'] = to_email
msg['Subject'] = subject

# Send via local SMTP
server = smtplib.SMTP('localhost', 2525)
server.send_message(msg)
server.quit()

return {'success': True, 'sent_to': to_email}
```

---

## 🔄 Step 3: Create n8n Workflow

### **Simple Email Sending Workflow**

**Workflow Structure:**
```
Trigger (Manual/Webhook/Schedule)
  ↓
Process Data (Code/Set Node)
  ↓
Send Email (Email Send Node)
  ↓
Log Success (Code/Slack Node)
```

**Example Workflow JSON:**
```json
{
  "name": "Send Email via Local Server",
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [250, 300]
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [450, 300],
      "parameters": {
        "host": "localhost",
        "port": 2525,
        "fromEmail": "noreply@ballcode.co",
        "toEmail": "info@ballcode.co",
        "subject": "Test Email from n8n",
        "message": "This email was sent through the local email system!",
        "emailType": "text"
      }
    }
  ],
  "connections": {
    "Manual Trigger": {
      "main": [[{"node": "Send Email", "type": "main", "index": 0}]]
    }
  }
}
```

---

## 📊 Step 4: Dynamic Email Sending

**Send emails based on workflow data:**

```json
{
  "name": "Send Email",
  "type": "n8n-nodes-base.emailSend",
  "parameters": {
    "host": "localhost",
    "port": 2525,
    "fromEmail": "noreply@ballcode.co",
    "toEmail": "={{ $json.recipient_email }}",
    "subject": "={{ $json.email_subject }}",
    "message": "={{ $json.email_body }}",
    "emailType": "html"
  }
}
```

**Data Flow:**
- Previous node provides: `recipient_email`, `email_subject`, `email_body`
- Email Send node uses expressions to get values
- Email is sent to local SMTP server

---

## 🎯 Step 5: Email Templates

**Create reusable email templates:**

### **Template 1: Simple Text Email**
```json
{
  "toEmail": "={{ $json.email }}",
  "subject": "Welcome to BallCODE!",
  "message": "Hello {{ $json.name }},\n\nWelcome to BallCODE! We're excited to have you.\n\nBest regards,\nBallCODE Team"
}
```

### **Template 2: HTML Email**
```json
{
  "toEmail": "={{ $json.email }}",
  "subject": "Welcome to BallCODE!",
  "message": "<h1>Welcome to BallCODE!</h1><p>Hello {{ $json.name }},</p><p>We're excited to have you join us!</p><p>Best regards,<br>BallCODE Team</p>",
  "emailType": "html"
}
```

---

## 🔍 Step 6: Verify Emails Sent

**Check emails in Cursor:**
```bash
# List all emails
python3 -m email_system.cli list

# List unread emails
python3 -m email_system.cli list --unread

# Read specific email
python3 -m email_system.cli read <email_id>

# Search emails
python3 -m email_system.cli search "n8n"
```

---

## 🚨 Troubleshooting

### **Issue: Email Not Sending**

**Check:**
1. ✅ Email server is running (`python3 -m email_system.cli start`)
2. ✅ n8n SMTP host is `localhost` (or correct IP)
3. ✅ n8n SMTP port is `2525`
4. ✅ No firewall blocking port 2525

**Solution:**
- Check n8n execution logs
- Check email server terminal for errors
- Test email server directly: `python3 -m email_system.cli send --to test@test.com --subject "Test" --body "Test"`

---

### **Issue: Connection Refused**

**Error:** `Connection refused` or `Cannot connect to SMTP server`

**Solution:**
- Make sure email server is running
- Check if port 2525 is available: `lsof -i :2525`
- If n8n is on different machine, use machine IP instead of `localhost`

---

### **Issue: Emails Not Appearing**

**Check:**
1. ✅ Email was actually sent (check n8n execution logs)
2. ✅ Email server received email (check server terminal)
3. ✅ Database is accessible: `ls -la emails.db`

**Solution:**
- List emails: `python3 -m email_system.cli list`
- Check database: `sqlite3 emails.db "SELECT COUNT(*) FROM emails;"`

---

## 📋 Best Practices

### **1. Error Handling**
Add error handling in n8n workflow:

```json
{
  "name": "Handle Email Errors",
  "type": "n8n-nodes-base.if",
  "parameters": {
    "conditions": {
      "boolean": [
        {
          "value1": "={{ $json.success }}",
          "value2": true
        }
      ]
    }
  }
}
```

### **2. Email Logging**
Log all sent emails:

```json
{
  "name": "Log Email Sent",
  "type": "n8n-nodes-base.code",
  "parameters": {
    "jsCode": "return [{json: {email_sent: true, timestamp: new Date().toISOString()}}];"
  }
}
```

### **3. Rate Limiting**
Add delays between emails if sending many:

```json
{
  "name": "Wait",
  "type": "n8n-nodes-base.wait",
  "parameters": {
    "amount": 1,
    "unit": "seconds"
  }
}
```

---

## 🎯 Example Workflows

### **Workflow 1: Send Welcome Email**

**Trigger:** New user signup  
**Action:** Send welcome email

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Send Welcome Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "host": "localhost",
        "port": 2525,
        "fromEmail": "noreply@ballcode.co",
        "toEmail": "={{ $json.user_email }}",
        "subject": "Welcome to BallCODE!",
        "message": "Hello {{ $json.user_name }},\n\nWelcome to BallCODE!",
        "emailType": "text"
      }
    }
  ]
}
```

---

### **Workflow 2: Send Notification Email**

**Trigger:** Event occurs  
**Action:** Send notification

```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger"
    },
    {
      "name": "Send Notification",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "host": "localhost",
        "port": 2525,
        "fromEmail": "noreply@ballcode.co",
        "toEmail": "info@ballcode.co",
        "subject": "Daily Report",
        "message": "={{ $json.report }}",
        "emailType": "html"
      }
    }
  ]
}
```

---

## ✅ Success Checklist

- [ ] Email server is running (`python3 -m email_system.cli start`)
- [ ] n8n workflow created with Email Send node
- [ ] SMTP configured: `localhost:2525`
- [ ] Test email sent successfully
- [ ] Email appears in database (`python3 -m email_system.cli list`)
- [ ] Workflow executes without errors

---

## 🚀 Next Steps

1. **Start Email Server:** Keep it running in background
2. **Create n8n Workflows:** Build your email automation workflows
3. **Test:** Send test emails and verify they're stored
4. **Monitor:** Check email statistics: `python3 -m email_system.cli stats`

---

**You now have a completely free email system integrated with n8n!** 🎉


