# Pilot Program & CES Launch - Setup Guide
## Complete Setup Instructions for @Thanos System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 21, 2025  
**Purpose:** Complete setup guide for pilot program acquisition system  
**Target:** 10 pilot programs by CES 2026 (January 7-10)

---

## Quick Start

### Step 1: Install Python Dependencies

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
pip install requests python-dotenv
```

### Step 2: Set Up Environment Variables

Create `.env` file in project root:

```bash
# HubSpot API
HUBSPOT_TOKEN=your_hubspot_token_here

# Mailchimp API
MAILCHIMP_API_KEY=your_mailchimp_api_key_here
MAILCHIMP_LIST_ID=your_mailchimp_list_id_here

# Google Analytics (optional)
GOOGLE_ANALYTICS_PROPERTY_ID=your_property_id_here

# Buffer API (optional, for social media)
BUFFER_ACCESS_TOKEN=your_buffer_token_here
```

### Step 3: Populate School Database

Edit `documents/school-contacts-database.json` and add 100+ target schools with:
- School name
- Contact name and email
- Grades served
- STEM programs
- Basketball programs
- Priority level

### Step 4: Import n8n Workflows

1. Go to n8n: `http://192.168.1.226:5678`
2. Import `n8n-school-outreach-automation-workflow.json`
3. Import `n8n-ces-launch-automation-workflow.json`
4. Configure credentials (Mailchimp, HubSpot, Buffer)

### Step 5: Test Tracking System

```bash
python scripts/pilot-tracking-system.py status
python scripts/pilot-tracking-system.py report
```

---

## Detailed Setup Instructions

### 1. School Database Setup

**File:** `documents/school-contacts-database.json`

**Required Fields for Each School:**
- `name`: School name
- `contact_name`: Primary contact name
- `email`: Contact email
- `phone`: Contact phone (optional)
- `grades`: Grade levels served (e.g., "3-8")
- `stem_programs`: Array of STEM programs
- `basketball_programs`: Boolean
- `priority`: "high", "medium", or "low"

**Example School Entry:**
```json
{
  "id": "school_001",
  "name": "Triangle Science & Math Academy",
  "contact_name": "Dr. Jane Smith",
  "email": "jane.smith@school.edu",
  "phone": "555-1234",
  "grades": "3-8",
  "stem_programs": ["Science", "Math", "Technology"],
  "basketball_programs": true,
  "priority": "high",
  "status": "not_contacted"
}
```

### 2. HubSpot Pipeline Setup

**Pipeline Stages:**
1. **Contact** - Initial contact made
2. **Qualified** - Responded, interested
3. **Call Scheduled** - Discovery call scheduled
4. **Pilot Committed** - Pilot agreement signed
5. **Onboarded** - Onboarding complete
6. **CES Launch** - Part of CES launch

**Custom Properties to Add:**
- `ballcode_school_id` (Text)
- `ballcode_status` (Text)
- `ballcode_priority` (Text)
- `ballcode_pilot_committed` (Boolean)
- `ballcode_ces_launch` (Boolean)

### 3. Mailchimp Setup

**List Setup:**
1. Create new list: "BallCODE Pilot Schools"
2. Add custom merge fields:
   - `SCHOOL` (Text)
   - `GRADES` (Text)
   - `STATUS` (Text)
3. Get List ID from Mailchimp dashboard
4. Add to `.env` as `MAILCHIMP_LIST_ID`

**Campaigns to Create:**
- Warm Contact Email
- Cold Outreach Email
- Follow-up 3 Day
- Follow-up 7 Day
- CES Launch Announcement
- CES Countdown 6 Days
- CES Countdown 3 Days
- New Year Messaging

### 4. n8n Workflow Configuration

**School Outreach Automation:**
1. Import `n8n-school-outreach-automation-workflow.json`
2. Configure webhook URL: `http://192.168.1.226:5678/webhook/school-outreach`
3. Set up credentials:
   - Mailchimp API
   - HubSpot API
4. Test with sample school data

**CES Launch Automation:**
1. Import `n8n-ces-launch-automation-workflow.json`
2. Configure schedule trigger for January 7, 2026 at 9:00 AM
3. Set up credentials:
   - Mailchimp API
   - HubSpot API
   - Buffer API (optional)
4. Test workflow manually

### 5. Tracking System Usage

**Generate Daily Report:**
```bash
python scripts/pilot-tracking-system.py report
```

**Check Current Status:**
```bash
python scripts/pilot-tracking-system.py status
```

**Get Follow-up List:**
```bash
python scripts/pilot-tracking-system.py followup 3
```

**List Pilot Commitments:**
```bash
python scripts/pilot-tracking-system.py commitments
```

### 6. Google Analytics Setup

**Events to Track:**
- `pilot_signup_form_submit`
- `pilot_agreement_signed`
- `discovery_call_scheduled`
- `ces_launch_email_click`

**Goals to Create:**
- Pilot Program Sign-up
- Discovery Call Scheduled
- Pilot Agreement Signed

---

## Daily Workflow

### Morning (9 AM):
1. Run tracking report: `python scripts/pilot-tracking-system.py report`
2. Review daily metrics
3. Check follow-ups needed: `python scripts/pilot-tracking-system.py followup 3`
4. Plan day's outreach

### During Day:
1. Trigger outreach workflow via webhook or n8n UI
2. Monitor email responses
3. Update school statuses in database
4. Schedule discovery calls
5. Send pilot agreements

### Evening (6 PM):
1. Update tracking system
2. Generate end-of-day report
3. Plan next day's activities
4. Review metrics and adjust strategy

---

## API Integration Details

### HubSpot API Integration

**Endpoints Used:**
- `POST /crm/v3/objects/contacts` - Create contact
- `PATCH /crm/v3/objects/deals/{dealId}` - Update deal stage
- `GET /crm/v3/objects/deals` - List deals

**Required Scopes:**
- `contacts`
- `deals`

### Mailchimp API Integration

**Endpoints Used:**
- `POST /3.0/lists/{listId}/members` - Add subscriber
- `POST /3.0/campaigns` - Create campaign
- `POST /3.0/campaigns/{campaignId}/actions/send` - Send campaign

**Required Permissions:**
- Read/Write access to lists
- Campaign creation and sending

### n8n Webhook Integration

**Webhook URLs:**
- School Outreach: `http://192.168.1.226:5678/webhook/school-outreach`
- CES Launch: Scheduled trigger (no webhook needed)

**Webhook Payload Example:**
```json
{
  "status": "not_contacted",
  "limit": 30,
  "template_type": "cold_outreach"
}
```

---

## Troubleshooting

### Issue: Tracking system can't find database
**Solution:** Ensure `documents/school-contacts-database.json` exists and is valid JSON

### Issue: HubSpot API errors
**Solution:** 
- Verify token is valid
- Check custom properties exist
- Verify API scopes

### Issue: Mailchimp API errors
**Solution:**
- Verify API key is valid
- Check list ID is correct
- Verify merge fields exist

### Issue: n8n workflow not executing
**Solution:**
- Check n8n is running: `http://192.168.1.226:5678`
- Verify credentials are configured
- Check workflow is activated
- Review execution logs

---

## Success Metrics Dashboard

**Key Metrics to Monitor Daily:**
- Schools contacted (target: 80+ Week 1, 150+ Week 2)
- Response rate (target: 15-20%)
- Call scheduled rate (target: 10-15%)
- Pilot commitment rate (target: 14% = 10/70)
- Total pilot commitments (target: 10 by Jan 5)

**CES Launch Metrics:**
- New inquiries (target: 100+)
- Sign-ups (target: 50+)
- Pilot commitments (target: 20+)
- Total schools in pipeline (target: 100+)

---

## Next Steps

1. ✅ Complete foundation setup (this guide)
2. ⏳ Populate school database with 100+ schools
3. ⏳ Configure HubSpot pipeline
4. ⏳ Set up Mailchimp campaigns
5. ⏳ Import and test n8n workflows
6. ⏳ Begin Week 1 outreach (Dec 23)

---

**Version:** 1.0  
**Created:** December 21, 2025  
**Status:** Ready for Implementation

