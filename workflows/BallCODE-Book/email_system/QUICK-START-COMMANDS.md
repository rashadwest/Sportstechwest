# 🚀 Quick Start Commands

## Navigate to Email System

**From anywhere, run:**
```bash
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system
```

**Or from Desktop:**
```bash
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system
```

---

## Start Email Server

```bash
python3 main.py start
```

**Keep this terminal running!**

---

## Send Email (New Terminal)

Open a **new terminal** and run:
```bash
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system
python3 main.py send --to test@ballcode.co --subject "Hello" --body "This is a test!"
```

---

## Check Emails

```bash
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system
python3 main.py list
```

---

## All Commands

```bash
# Navigate to email system
cd ~/Sportstechwest/workflows/BallCODE-Book/email_system

# Start server
python3 main.py start

# Send email
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"

# List emails
python3 main.py list

# Read email
python3 main.py read 1

# Search emails
python3 main.py search "query"
```

---

**Full path:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/email_system`


