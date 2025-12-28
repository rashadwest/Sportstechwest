# ✅ Automated Email System - Complete Setup

## 🚀 One Command Setup

**Run this single command:**
```bash
cd email_system
python3 automated_setup.py
```

**That's it!** The system will:
- ✅ Install all dependencies automatically
- ✅ Create configuration files
- ✅ Only prompt you for credentials (Slack webhook, Apollo API key - both optional)
- ✅ Test the system
- ✅ Set up everything ready to use

---

## 📋 What Gets Set Up Automatically

1. **Dependencies** - Installs aiosmtpd, click, requests
2. **Configuration** - Creates email_config.json with defaults
3. **Email System** - Sets up SMTP server, storage, sender
4. **Slack Integration** - Ready (just needs webhook URL)
5. **Apollo Integration** - Ready (just needs API key)
6. **Sales Pipeline** - Automatically enabled

---

## 🔑 Credentials (Only When Needed)

The setup will only ask for:

1. **Slack Webhook URL** (optional)
   - Press Enter to skip
   - Can add later in `email_config.json`

2. **Apollo API Key** (optional)
   - Press Enter to skip
   - Can add later in `email_config.json`

**Everything else is automated!**

---

## 🎯 After Setup

### Start Email Server
```bash
python3 main.py start
```

### Send Email
```bash
python3 main.py send --to EMAIL --subject "SUBJECT" --body "BODY"
```

### Check Emails
```bash
python3 main.py list
```

### View Sales Pipeline
```bash
python3 -c "from sales_pipeline import SalesPipeline; p = SalesPipeline(); print(p.get_leads())"
```

---

## 📧 Sales Pipeline Features

**Automatic Lead Creation:**
- New emails automatically create leads
- Enriched with Apollo data (if API key provided)
- Notifications sent to Slack (if webhook provided)
- Stored in sales_pipeline.db

**Pipeline Stages:**
- new → contacted → qualified → proposal → closed

**No Email Client Needed:**
- All notifications go to Slack
- Sales pipeline tracks everything
- Apollo integration enriches leads

---

## 🔧 Adding Credentials Later

Edit `email_config.json`:
```json
{
  "slack": {
    "webhook_url": "YOUR_WEBHOOK_URL",
    "enabled": true
  },
  "apollo": {
    "api_key": "YOUR_API_KEY",
    "enabled": true
  }
}
```

---

## ✅ Success Checklist

- [x] Automated setup script created
- [x] Minimal prompts (only credentials)
- [x] Slack integration ready
- [x] Apollo integration ready
- [x] Sales pipeline automated
- [x] All dependencies auto-installed
- [x] Configuration auto-created

---

**Run `python3 automated_setup.py` and you're done!** 🎉



