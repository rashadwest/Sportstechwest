# BallCODE Local Email System

**Free, local email system integrated with Cursor and n8n**

## 🎯 Features

- ✅ **Completely Free** - No paid services required
- ✅ **Local Hosting** - Runs on your machine
- ✅ **Cursor Integration** - Manage emails from Cursor CLI
- ✅ **n8n Integration** - Send emails through n8n workflows
- ✅ **SQLite Storage** - Simple, local email database
- ✅ **SMTP Server** - Receive emails locally

## 🚀 Quick Start

### Installation

```bash
cd email_system
pip install -r requirements.txt
```

### Start SMTP Server

```bash
python -m email_system.cli start
```

Server will run on `localhost:2525`

### Send Email

```bash
python -m email_system.cli send --to info@ballcode.co --subject "Test" --body "Hello from Cursor!"
```

### List Emails

```bash
python -m email_system.cli list
python -m email_system.cli list --unread
```

### Read Email

```bash
python -m email_system.cli read <email_id>
```

### Search Emails

```bash
python -m email_system.cli search "test"
```

### Delete Email

```bash
python -m email_system.cli delete <email_id>
```

### Statistics

```bash
python -m email_system.cli stats
```

## 🔧 n8n Integration

### Configure n8n SMTP Node

1. **Add "Send Email" node** to your n8n workflow
2. **Configure SMTP:**
   - **Host:** `localhost` (or your machine IP)
   - **Port:** `2525`
   - **User:** (leave empty for local server)
   - **Password:** (leave empty for local server)
   - **SSL/TLS:** Disabled (for local testing)

3. **Set Email Fields:**
   - **From:** `noreply@ballcode.co` (or your email)
   - **To:** Recipient email
   - **Subject:** Email subject
   - **Message:** Email body

4. **Test:** Send test email from n8n workflow

### Example n8n Workflow

```json
{
  "nodes": [
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "host": "localhost",
        "port": 2525,
        "fromEmail": "noreply@ballcode.co",
        "toEmail": "={{ $json.email }}",
        "subject": "={{ $json.subject }}",
        "message": "={{ $json.message }}",
        "emailType": "text"
      }
    }
  ]
}
```

## 📧 Using from Python (in Cursor)

```python
from email_system import EmailStorage, EmailSender, EmailServer

# Send email
sender = EmailSender(smtp_host='localhost', smtp_port=2525)
sender.send(
    to_address='info@ballcode.co',
    subject='Test Email',
    body='Hello from Python!'
)

# List emails
storage = EmailStorage()
emails = storage.list_emails(unread_only=True)
for email in emails:
    print(f"{email['subject']} from {email['from_address']}")

# Read email
email = storage.get_email(email_id=1)
print(email['body'])

# Search emails
results = storage.search_emails('test')
```

## 🗂️ Email Storage

Emails are stored in SQLite database (`emails.db` by default).

**Database Schema:**
- `emails` table: Stores email data
- `attachments` table: Stores email attachments (future feature)

**Folders:**
- `inbox` - Received emails
- `sent` - Sent emails
- (Can add more folders later)

## 🔒 Security Notes

- **Local Only:** This system is designed for local use
- **No Authentication:** Local server doesn't require authentication (for simplicity)
- **Production Use:** For production, add authentication and SSL/TLS
- **Domain Setup:** For real domain emails, configure DNS MX records

## 📚 Documentation

See `BALLCODE-LOCAL-EMAIL-SYSTEM-AIMCODE.md` for complete AIMCODE methodology documentation.

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Use different port
python -m email_system.cli start --port 2526
```

### Database Locked
- Close any other connections to `emails.db`
- Restart the server

### Emails Not Receiving
- Check server is running: `python -m email_system.cli start`
- Check port is correct in n8n configuration
- Check firewall settings

## 🎯 Next Steps

1. **Start Server:** `python -m email_system.cli start`
2. **Configure n8n:** Add SMTP node with localhost:2525
3. **Test:** Send test email from n8n
4. **Use:** Manage emails from Cursor CLI

---

**Cost: $0/month | Setup Time: < 5 minutes | All Local & Free!**


