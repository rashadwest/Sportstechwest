# BallCODE Local Email System - AIMCODE Methodology
## Free, Local Email System Integrated with Cursor & n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Build a completely free, local email system that works inside Cursor and integrates with n8n

---

## 🎯 PHASE 1: CLEAR FRAMEWORK

### **C - Clarity: Objectives & Requirements**

**Clear Objectives:**
1. **Free Email System:** Zero cost, no paid services
2. **Local Hosting:** Runs on your machine, no external dependencies
3. **Cursor Integration:** Manage emails directly inside Cursor (no external email client)
4. **n8n Integration:** Send emails through n8n workflows
5. **Domain Support:** Use ballcode.co domain for email addresses
6. **Full Control:** Complete ownership of email data and system

**Requirements:**
- ✅ Must be free (no paid services)
- ✅ Must work locally (no cloud dependencies)
- ✅ Must integrate with Cursor (Python-based, CLI interface)
- ✅ Must integrate with n8n (SMTP/IMAP protocols)
- ✅ Must support custom domain (ballcode.co)
- ✅ Must be simple to set up and maintain

---

### **L - Logic: Systematic Approach**

**Logical Architecture:**
```
Layer 1: Email Protocol Foundation (SMTP/IMAP)
  ↓
Layer 2: Local Email Server (Python-based)
  ↓
Layer 3: Email Storage (Local file system or SQLite)
  ↓
Layer 4: Cursor Integration (CLI commands & Python API)
  ↓
Layer 5: n8n Integration (SMTP/IMAP endpoints)
  ↓
Layer 6: Domain Configuration (DNS setup guide)
```

**System Components:**
1. **SMTP Server:** Receives and sends emails (aiosmtpd)
2. **IMAP Server:** Email access protocol (optional, for email clients)
3. **Email Storage:** Local database or file system
4. **Cursor CLI:** Commands to manage emails from Cursor
5. **n8n Endpoints:** SMTP configuration for n8n workflows
6. **DNS Guide:** Instructions for ballcode.co MX records

---

### **E - Examples: Similar Systems**

**Reference Examples:**
- **Mail-in-a-Box:** Self-hosted email server (too complex for our needs)
- **hMailServer:** Windows email server (not Python-based)
- **aiosmtpd:** Python async SMTP server (perfect for our needs)
- **Postfix:** Linux email server (too complex)
- **Python smtpd:** Built-in Python SMTP server (synchronous, less efficient)

**Best Match:**
- **aiosmtpd** - Python async SMTP server library
- **SQLite** - Lightweight database for email storage
- **Python CLI** - Cursor-integrated command interface

---

### **A - Adaptation: Flexibility & Constraints**

**Flexibility:**
- Can start simple (SMTP only) and add IMAP later
- Can use file system storage initially, upgrade to database later
- Can add features incrementally (webhooks, API, etc.)

**Constraints:**
- Must be free (no paid services)
- Must work on macOS (your system)
- Must be Python-based (for Cursor integration)
- Must be simple to set up (one command if possible)

**Adaptations:**
- Start with SMTP server only (sending/receiving)
- Use SQLite for storage (simple, no setup needed)
- CLI interface first (can add GUI later)
- Local-only initially (can add remote access later)

---

### **R - Results: Measurable Outcomes**

**Success Criteria:**
- [ ] Can send emails from Cursor using CLI command
- [ ] Can receive emails to local server
- [ ] Can list/view emails from Cursor
- [ ] n8n can send emails through local SMTP server
- [ ] Email addresses work (e.g., info@ballcode.co)
- [ ] Zero cost (no paid services)
- [ ] Setup time < 30 minutes

**Metrics:**
- Setup time: < 30 minutes
- Email delivery time: < 5 seconds (local)
- Storage: Unlimited (local disk)
- Cost: $0/month

---

## 🧠 PHASE 2: ALPHA EVOLVE (Systematic Deep Learning)

### **Layer 1: Email Protocol Foundation**

**SMTP (Simple Mail Transfer Protocol):**
- **Purpose:** Send emails between servers
- **Port:** 25 (standard), 587 (submission), 465 (SSL)
- **How it works:** Client connects to server, sends email, server delivers
- **Our use:** Local SMTP server receives and stores emails

**IMAP (Internet Message Access Protocol):**
- **Purpose:** Access emails from server
- **Port:** 143 (standard), 993 (SSL)
- **How it works:** Client connects to server, reads emails, manages folders
- **Our use:** Optional - for email client access (can add later)

**Email Structure:**
- **Headers:** From, To, Subject, Date, etc.
- **Body:** Text or HTML content
- **Attachments:** Files attached to email

**Key Concepts:**
- **MX Records:** DNS records that tell where to send emails for a domain
- **SPF/DKIM/DMARC:** Email authentication (can add later)
- **Local vs Remote:** We're building local (no internet required for basic operation)

---

### **Layer 2: Local Email Server Architecture**

**Components:**
1. **SMTP Server (aiosmtpd):**
   - Listens on port 25 (or custom port)
   - Receives incoming emails
   - Stores emails in database/file system

2. **Email Storage:**
   - SQLite database (emails table)
   - Stores: from, to, subject, body, date, attachments

3. **Email Sender:**
   - Python smtplib to send emails
   - Can send through local server or external SMTP

**Data Flow:**
```
Incoming Email → SMTP Server → Parse Email → Store in Database
Outgoing Email → Python Script → SMTP Server → Send Email
```

---

### **Layer 3: Email Storage System**

**SQLite Database Schema:**
```sql
CREATE TABLE emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id TEXT UNIQUE,
    from_address TEXT,
    to_address TEXT,
    subject TEXT,
    body TEXT,
    html_body TEXT,
    date_received TIMESTAMP,
    date_sent TIMESTAMP,
    read BOOLEAN DEFAULT 0,
    folder TEXT DEFAULT 'inbox',
    raw_email TEXT
);

CREATE TABLE attachments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_id INTEGER,
    filename TEXT,
    content_type TEXT,
    file_path TEXT,
    FOREIGN KEY (email_id) REFERENCES emails(id)
);
```

**File System Storage (Alternative):**
- Store emails as .eml files
- Organize by date/folder
- Simpler but less queryable

---

### **Layer 4: Cursor Integration**

**CLI Commands:**
```bash
# Send email
python email_system.py send --to info@ballcode.co --subject "Test" --body "Hello"

# List emails
python email_system.py list
python email_system.py list --unread

# Read email
python email_system.py read <email_id>

# Search emails
python email_system.py search --query "test"

# Delete email
python email_system.py delete <email_id>
```

**Python API:**
```python
from email_system import EmailSystem

email = EmailSystem()
email.send(to="info@ballcode.co", subject="Test", body="Hello")
emails = email.list_unread()
email.read(email_id=1)
```

---

### **Layer 5: n8n Integration**

**SMTP Configuration for n8n:**
- **Host:** localhost (or your machine IP)
- **Port:** 25 (or custom port)
- **Username:** (optional, for authentication)
- **Password:** (optional, for authentication)
- **SSL/TLS:** Optional (can add later)

**n8n Workflow:**
- Use "Send Email" node
- Configure SMTP connection to local server
- Send emails through local system

**IMAP Integration (Optional):**
- n8n can read emails using IMAP node
- Monitor inbox for new emails
- Trigger workflows based on email content

---

### **Layer 6: Domain Configuration**

**DNS Setup (ballcode.co):**
- **MX Record:** Points to your server IP (or localhost for testing)
- **A Record:** Points to your server IP (if sending from domain)
- **SPF Record:** (Optional) Authorizes your server to send emails
- **DKIM Record:** (Optional) Email signing for authentication

**For Local Testing:**
- Use localhost (no DNS needed)
- Test with email addresses like test@localhost
- Can add domain later when ready

---

## 📚 PHASE 3: PhD-LEVEL PEER-REVIEWED RESEARCH

### **Email Protocol Research**

**SMTP Protocol (RFC 5321):**
- **Source:** RFC 5321 - Simple Mail Transfer Protocol
- **Key Points:**
  - SMTP is the standard for email transmission
  - Uses TCP port 25 (standard) or 587 (submission)
  - Protocol is text-based and command-driven
  - Supports authentication (SMTP AUTH)

**IMAP Protocol (RFC 3501):**
- **Source:** RFC 3501 - Internet Message Access Protocol
- **Key Points:**
  - IMAP allows email clients to access emails on server
  - Supports multiple folders, flags, and search
  - More complex than POP3 but more powerful

**Email Architecture Research:**
- **Source:** "Email Architecture and Protocols" - Academic papers on email system design
- **Key Concepts:**
  - Email systems use store-and-forward architecture
  - Local servers can operate independently
  - DNS MX records route emails to correct server

### **Python Email Libraries Research**

**aiosmtpd:**
- **Source:** Python aiosmtpd library documentation
- **Key Features:**
  - Async SMTP server implementation
  - Built on asyncio for performance
  - Easy to customize and extend
  - Active development and maintenance

**Python smtplib:**
- **Source:** Python standard library documentation
- **Key Features:**
  - Built-in SMTP client
  - Can send emails through any SMTP server
  - Simple and reliable

**Email Parsing:**
- **Source:** Python email library (standard library)
- **Key Features:**
  - Parse email headers and body
  - Handle attachments
  - Support MIME types

---

## 🎓 PHASE 4: EXPERT CONSULTATION (AIMCODE Advisory Board)

### **Steve Jobs - Simplicity Principle**
**Question:** "Would Jobs make this simple and beautiful?"

**Application:**
- ✅ Simple setup (one command: `python email_system.py start`)
- ✅ Clean CLI interface (intuitive commands)
- ✅ Minimal dependencies (only essential libraries)
- ✅ "It just works" - no complex configuration

### **Demis Hassabis - Systems Thinking**
**Question:** "Would Hassabis ensure systematic progression?"

**Application:**
- ✅ Layer-by-layer architecture (protocol → server → storage → integration)
- ✅ Each layer builds on previous
- ✅ Systematic testing at each layer
- ✅ Deep understanding before moving forward

---

## 🚀 IMPLEMENTATION PLAN

### **Step 1: Core SMTP Server**
- Install aiosmtpd
- Create basic SMTP server
- Test receiving emails

### **Step 2: Email Storage**
- Set up SQLite database
- Store received emails
- Query emails from database

### **Step 3: Email Sending**
- Implement email sending (smtplib)
- Test sending emails

### **Step 4: Cursor CLI**
- Create CLI commands
- Integrate with Cursor
- Test all commands

### **Step 5: n8n Integration**
- Configure n8n SMTP node
- Test sending from n8n
- Document integration

### **Step 6: Domain Setup (Optional)**
- DNS configuration guide
- Domain email setup
- Testing with real domain

---

## 📋 TECHNICAL STACK

**Core Technologies:**
- **Python 3.8+** - Programming language
- **aiosmtpd** - Async SMTP server
- **SQLite** - Email storage database
- **Python email library** - Email parsing
- **smtplib** - Email sending
- **Click** - CLI framework (optional)

**Dependencies:**
```python
aiosmtpd>=1.4.0
sqlite3 (built-in)
email (built-in)
smtplib (built-in)
click>=8.0.0  # For CLI
```

---

## 🎯 SUCCESS METRICS

**Functional Requirements:**
- [ ] Can receive emails on local SMTP server
- [ ] Can send emails from Python script
- [ ] Can list/view emails from Cursor
- [ ] n8n can send emails through local server
- [ ] Emails stored in SQLite database
- [ ] CLI commands work from Cursor

**Performance Requirements:**
- Email delivery: < 5 seconds (local)
- Database queries: < 1 second
- Server startup: < 2 seconds

**Cost Requirements:**
- Total cost: $0/month
- No paid services required
- All open-source software

---

## 🔄 NEXT STEPS

1. **Build Core System** - SMTP server + storage
2. **Add CLI Interface** - Cursor commands
3. **Integrate n8n** - SMTP configuration
4. **Test & Document** - Verify everything works
5. **Deploy & Use** - Start using in production

---

**Ready to build!** Let's start with the core SMTP server implementation.


