# API Deployment Guide - CES Launch
## Complete Setup for All APIs

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 24, 2025  
**Status:** Ready to Deploy

---

## 🎯 Quick Answer: Canva API Free Tier

**✅ YES - Canva has a free tier for developers!**

- **Developer Platform:** Free to sign up
- **API Access:** Free tier available
- **Limitations:** Some rate limits, but sufficient for launch
- **Get Started:** https://www.canva.dev/

---

## 📋 All APIs Status

### ✅ FREE APIs (All Available):

1. **HubSpot** - Free CRM with full API
2. **Mailchimp** - Free plan (500 contacts) with API
3. **Buffer** - Free plan (3 accounts) with API
4. **Canva** - Free developer tier with API ✅

### 💰 PAID APIs (You Have):

5. **Apollo** - Paid tier (you have this) ✅

---

## 🚀 Quick Start - Deploy All APIs Now

### Step 1: Create .env File

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
cp .env.example .env
```

### Step 2: Get API Keys

**Run the setup guide:**
```bash
python scripts/setup-all-apis.py
```

This will show you:
- Where to get each API key
- Step-by-step instructions
- What to add to .env file

### Step 3: Add Keys to .env

Edit `.env` file` and add your keys:
```bash
# HubSpot (Free)
HUBSPOT_TOKEN=your_token_here

# Mailchimp (Free)
MAILCHIMP_API_KEY=your_key-us1
MAILCHIMP_LIST_ID=your_list_id

# Buffer (Free)
BUFFER_API_KEY=your_token_here

# Apollo (Paid - You have this)
APOLLO_API_KEY=your_key_here

# Canva (Free developer tier)
CANVA_API_KEY=your_key_here
```

### Step 4: Test All APIs

```bash
python scripts/test-api-integrations.py
```

This will test:
- ✅ HubSpot
- ✅ Mailchimp
- ✅ Mailchimp List
- ✅ Buffer
- ✅ Apollo
- ✅ Canva

---

## 📋 Individual API Setup

### 1. HubSpot (Free) ✅

**Get Key:**
1. Go to: https://app.hubspot.com/settings/integrations/private-apps
2. Click "Create a private app"
3. Name: "BallCODE CES Launch"
4. Scopes: `crm.objects.contacts.read`, `crm.objects.contacts.write`
5. Copy "Access token"
6. Add to .env: `HUBSPOT_TOKEN=your_token`

**Test:**
```bash
python scripts/test-api-integrations.py
```

---

### 2. Mailchimp (Free) ✅

**Get API Key:**
1. Go to: https://us1.admin.mailchimp.com/account/api/
2. Click "Create A Key"
3. Copy API key (format: `xxxxxxxx-us1`)
4. Add to .env: `MAILCHIMP_API_KEY=your_key-us1`

**Get List ID:**
1. Go to Audience → All contacts
2. Click "Settings" → "Audience name and defaults"
3. Copy "Audience ID"
4. Add to .env: `MAILCHIMP_LIST_ID=your_list_id`

**Test:**
```bash
python scripts/test-api-integrations.py
```

---

### 3. Buffer (Free) ✅

**Get Key:**
1. Go to: https://buffer.com/developers/apps
2. Settings → Apps & Extras → Developer App
3. Create new app
4. Copy "Access Token"
5. Add to .env: `BUFFER_API_KEY=your_token`

**Test:**
```bash
python scripts/test-api-integrations.py
```

---

### 4. Apollo (Paid - You Have This) ✅

**Get Key:**
1. Go to: https://app.apollo.io/#/settings/integrations/api
2. Copy your API key
3. Add to .env: `APOLLO_API_KEY=your_key`

**Note:** You have paid tier (1,000+ calls/month)

**Test:**
```bash
python scripts/test-api-integrations.py
python scripts/apollo-school-research.py
```

---

### 5. Canva (Free Developer Tier) ✅

**Get Key:**
1. Go to: https://www.canva.dev/
2. Sign up for Developer Platform (free)
3. Create a new app
4. Get API key or OAuth token
5. Add to .env: `CANVA_API_KEY=your_key`
   OR: `CANVA_ACCESS_TOKEN=your_token`

**Note:** Free tier available for developers

**Test:**
```bash
python scripts/test-api-integrations.py
python scripts/canva-design-automation.py
```

---

## 🔧 Automation Scripts

### Setup All APIs:
```bash
python scripts/setup-all-apis.py
```

### Test All APIs:
```bash
python scripts/test-api-integrations.py
```

### Use Canva for Design:
```bash
python scripts/canva-design-automation.py
```

### Use Apollo for Research:
```bash
python scripts/apollo-school-research.py
```

---

## 📊 API Status Dashboard

After setup, run:
```bash
python scripts/test-api-integrations.py
```

**Expected Output:**
```
✅ HubSpot: API connection successful
✅ Mailchimp: API connection successful
✅ Mailchimp List: List accessible
✅ Buffer: API connection successful
✅ Apollo: API connection successful
✅ Canva: API key/token found
```

---

## 🔒 Security Notes

**✅ .env file is already in .gitignore**
- Never commit .env file
- .env.example is safe to commit (no real keys)
- All API keys stay local

---

## ✅ Next Steps

1. **Run setup guide:**
   ```bash
   python scripts/setup-all-apis.py
   ```

2. **Get API keys** (follow instructions in guide)

3. **Add to .env file**

4. **Test all APIs:**
   ```bash
   python scripts/test-api-integrations.py
   ```

5. **Start using APIs:**
   - Canva: Add headers to designs
   - Apollo: Research schools
   - HubSpot: Track contacts
   - Mailchimp: Send emails
   - Buffer: Schedule posts

---

**Status:** ✅ Ready to deploy - All APIs have free tiers!

---

**Copyright © 2025 Rashad West. All Rights Reserved.**


