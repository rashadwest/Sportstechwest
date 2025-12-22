# Quick Start Guide

## ✅ What Robot Has Done

- ✅ Dependencies installed
- ✅ All system files verified
- ✅ System tests passed
- ✅ Startup scripts created

## ⚠️ What Human Must Do

- ⚠️ External SMTP Delivery: Set environment variables: GMAIL_USERNAME, GMAIL_APP_PASSWORD (or SendGrid/Mailgun)
- ⚠️ Slack Notifications: Optional: Get Slack webhook URL and add to email_config.json
- ⚠️ Apollo Lead Enrichment: Optional: Get Apollo API key and add to email_config.json

## 🚀 Start Using

```bash
cd email_system
python3 main.py start
```

## 📧 Send Email

```bash
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"
```
