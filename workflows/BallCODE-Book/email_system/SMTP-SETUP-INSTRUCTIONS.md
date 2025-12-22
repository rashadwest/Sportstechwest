# External SMTP Setup Instructions

## 🤖 Automated Setup (When Credentials Available)

**If you set environment variables, run:**
```bash
python3 auto_setup_external_smtp.py
```

The system will automatically detect and configure SMTP!

---

## 📋 Manual Setup Options

### Option 1: Gmail SMTP (Recommended - Unlimited, Free)

**Steps:**
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password (for "Mail")
4. Set environment variables:
   ```bash
   export GMAIL_USERNAME='your-email@gmail.com'
   export GMAIL_APP_PASSWORD='your-16-char-app-password'
   ```
5. Run: `python3 auto_setup_external_smtp.py`

**Result:** Unlimited emails, free, reliable

---

### Option 2: SendGrid (100 emails/day free)

**Steps:**
1. Sign up at sendgrid.com (free account)
2. Create API key in Settings → API Keys
3. Set environment variables:
   ```bash
   export SENDGRID_API_KEY='your-api-key'
   export SENDGRID_FROM_EMAIL='noreply@ballcode.co'
   ```
4. Run: `python3 auto_setup_external_smtp.py`

**Result:** 100 emails/day free

---

### Option 3: Mailgun (5,000 emails/month free)

**Steps:**
1. Sign up at mailgun.com (free account)
2. Get SMTP credentials from dashboard
3. Set environment variables:
   ```bash
   export MAILGUN_API_KEY='your-api-key'
   export MAILGUN_SMTP_USERNAME='your-smtp-username'
   export MAILGUN_FROM_EMAIL='noreply@ballcode.co'
   ```
4. Run: `python3 auto_setup_external_smtp.py`

**Result:** 5,000 emails/month free

---

## ✅ After Setup

Once configured, emails will automatically use external SMTP for delivery!

**Test:**
```bash
python3 send_test_email.py
```

---

**Robot will auto-configure when credentials are available!** 🤖
