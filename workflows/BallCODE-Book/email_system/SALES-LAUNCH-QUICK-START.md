# 🚀 Sales Launch Quick Start Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Get your email system ready for product launch in 10 minutes

---

## ⚡ Quick Setup (10 Minutes)

### **Step 1: Start Email Server (1 min)**
```bash
cd email_system
python3 main.py start
```
**Keep this running!** (Leave terminal open)

---

### **Step 2: Configure External SMTP (5 min)**

**Get Gmail App Password:**
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password (for "Mail")
4. Copy the 16-character password

**Set Environment Variables:**
```bash
export GMAIL_USERNAME='your-email@gmail.com'
export GMAIL_APP_PASSWORD='your-16-char-password'
```

**Auto-Configure:**
```bash
python3 auto_setup_external_smtp.py
```

✅ **Done!** Emails will now deliver to Gmail.

---

### **Step 3: Test Email (1 min)**
```bash
python3 send_with_external_smpt.py
```

Check your Gmail inbox - email should arrive!

---

### **Step 4: Prepare Launch Template (3 min)**

**Edit Template:**
```bash
cd templates
nano product_announcement.txt
```

**Fill in your product info:**
- Product name
- Description
- Features
- Link

**Save and done!**

---

## 🎯 Launch Your Product

### **Option 1: Send via CLI (Simple)**

**Send to one person:**
```bash
python3 main.py send \
  --to customer@example.com \
  --subject "New BallCODE Product!" \
  --body "$(python3 -c "
from templates import TemplateEngine
engine = TemplateEngine()
print(engine.render('product_announcement', {
    'name': 'Customer Name',
    'product_name': 'BallCODE Book 1',
    'description': 'Learn coding through basketball!',
    'features': '- Interactive exercises\n- Basketball stories',
    'link': 'https://ballcode.co'
}))
")"
```

---

### **Option 2: Send via n8n (Automated)**

**Import Workflow:**
1. Open n8n
2. Import `n8n-email-automation-workflow.json`
3. Configure:
   - Customer list (CSV, database, or Apollo)
   - Email template
   - Schedule (if needed)

**Run Workflow:**
- Click "Execute Workflow"
- Watch emails send automatically!

---

### **Option 3: Send via Python Script (Custom)**

**Create script:**
```python
from sender import EmailSender
from templates import TemplateEngine

# Load template
engine = TemplateEngine()
body = engine.render("product_announcement", {
    "name": "John",
    "product_name": "BallCODE Book 1",
    "description": "Learn coding through basketball!",
    "features": "- Interactive exercises\n- Basketball stories",
    "link": "https://ballcode.co"
})

# Send email
sender = EmailSender()
sender.send(
    to_address="customer@example.com",
    subject="New BallCODE Product!",
    body=body
)
```

---

## 📊 Track Your Launch

### **View Dashboard:**
```bash
python3 dashboard.py
```
**Open:** `http://localhost:5000`

**See:**
- All sent emails
- All leads created
- Engagement stats
- Sales pipeline

---

### **Check Sales Pipeline:**
```python
from sales_pipeline import SalesPipeline

pipeline = SalesPipeline()
leads = pipeline.get_leads()

for lead in leads:
    print(f"{lead['name']} - {lead['status']} - {lead['company']}")
```

---

## 🎯 Launch Checklist

**Before Launch:**
- [ ] Email server running
- [ ] External SMTP configured
- [ ] Test email sent successfully
- [ ] Template prepared
- [ ] Customer list ready

**During Launch:**
- [ ] Send emails (via CLI, n8n, or script)
- [ ] Monitor dashboard
- [ ] Check for errors

**After Launch:**
- [ ] Review sent emails
- [ ] Check leads created
- [ ] Follow up with responders
- [ ] Analyze engagement

---

## 💡 Pro Tips

1. **Start Small:**
   - Test with 5-10 emails first
   - Verify everything works
   - Then scale up

2. **Personalize:**
   - Use customer names
   - Reference their company
   - Make it personal

3. **Track Everything:**
   - Monitor dashboard
   - Check pipeline
   - Follow up quickly

4. **Automate Follow-Ups:**
   - Set up n8n workflow
   - Auto-follow-up after 3 days
   - Never let leads go cold

---

## 🚀 You're Ready!

**Everything is set up and ready to go!**

Just:
1. Start email server
2. Send your launch emails
3. Track results
4. Follow up with leads

**Good luck with your launch!** 🎉


