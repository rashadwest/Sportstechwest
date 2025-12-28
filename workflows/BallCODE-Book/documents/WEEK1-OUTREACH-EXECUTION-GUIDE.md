# Week 1 Outreach Execution Guide (Dec 23-27)
## Step-by-Step Guide for Initial Outreach Phase

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23-27, 2025  
**Target:** Contact 80+ schools, 3-5 pilot commitments  
**Status:** Ready for Execution

---

## 📅 Day-by-Day Execution Plan

### Day 1-2 (Dec 23-24): Initial Outreach - 30 Schools

#### Morning (9 AM):
1. **Generate Daily Report**
   ```bash
   python scripts/pilot-tracking-system.py report
   ```

2. **Prepare School List**
   - Review `documents/school-contacts-database.json`
   - Select 30 schools (mix of high/medium priority)
   - Verify contact information is complete

3. **Trigger Outreach Workflow**
   - Option A: Via n8n UI
     - Go to `http://192.168.1.226:5678`
     - Open "School Outreach Automation" workflow
     - Click "Execute Workflow"
     - Set parameters:
       - Status: "not_contacted"
       - Limit: 30
       - Template type: "cold_outreach" (or "warm_contact" for high priority)
   
   - Option B: Via Webhook
     ```bash
     curl -X POST http://192.168.1.226:5678/webhook/school-outreach \
       -H "Content-Type: application/json" \
       -d '{"status": "not_contacted", "limit": 30, "template_type": "cold_outreach"}'
     ```

#### During Day:
1. **Monitor Email Responses**
   - Check Mailchimp dashboard for opens/clicks
   - Check email inbox for responses
   - Update school statuses in database as responses come in

2. **Update Tracking System**
   - For each response, update `documents/school-contacts-database.json`:
     ```json
     {
       "status": "responded",
       "response_status": "responded",
       "date_contacted": "2025-12-23T10:00:00Z"
     }
     ```

3. **Schedule Discovery Calls**
   - For interested schools, schedule calls via Calendly
   - Update database:
     ```json
     {
       "call_scheduled": "2025-12-26T14:00:00Z",
       "status": "call_scheduled"
     }
     ```

#### Evening (6 PM):
1. **End-of-Day Report**
   ```bash
   python scripts/pilot-tracking-system.py report
   ```

2. **Update Daily Reports**
   - Edit `documents/pilot-ces-daily-reports.md`
   - Fill in today's metrics

3. **Plan Tomorrow**
   - Review responses
   - Plan follow-ups
   - Select next batch of schools

**Target:** 4-5 responses, 2-3 calls scheduled

---

### Day 3-4 (Dec 25-26): Follow-up + Scale Outreach - 25 Schools

#### Morning (9 AM):
1. **Check Follow-ups Needed**
   ```bash
   python scripts/pilot-tracking-system.py followup 3
   ```

2. **Send Follow-up Emails**
   - For schools contacted 3+ days ago with no response
   - Use "follow_up_3_day" template
   - Trigger via n8n or send manually

3. **Contact 25 New Schools**
   - Select next 25 schools from database
   - Trigger outreach workflow
   - Mix of warm/cold contacts

#### During Day:
1. **Conduct Discovery Calls**
   - Use discovery call script (see below)
   - Take notes during calls
   - Update database after each call

2. **Manage Pipeline**
   - Move responders to "Qualified" in HubSpot
   - Update school statuses
   - Schedule additional calls if needed

#### Evening (6 PM):
1. **End-of-Day Report**
   ```bash
   python scripts/pilot-tracking-system.py report
   ```

2. **Update Metrics**
   - Total responses: [COUNT]
   - Calls scheduled: [COUNT]
   - Calls conducted: [COUNT]

**Target:** 8-10 total responses, 5-6 calls scheduled

---

### Day 5-7 (Dec 27-29): Intensive Follow-up + Closing

#### Morning (9 AM):
1. **Multi-Touch Follow-up**
   - Send 7-day follow-ups to non-responders
   - Phone call attempts (if numbers available)
   - LinkedIn outreach (if applicable)

2. **Review Pipeline**
   - Check HubSpot for all "Qualified" schools
   - Prioritize schools for closing

#### During Day:
1. **Conduct Discovery Calls**
   - Focus on closing pilots
   - Use pilot agreement template (see below)
   - Send agreements to committed schools

2. **Close Pilots**
   - For schools ready to commit:
     - Send pilot agreement
     - Update database:
       ```json
       {
         "pilot_committed": true,
         "date_committed": "2025-12-27T15:00:00Z",
         "status": "pilot_committed"
       }
     ```
   - Log to HubSpot: Move to "Pilot Committed" stage

#### Evening (6 PM):
1. **Week 1 Summary**
   ```bash
   python scripts/pilot-tracking-system.py report
   python scripts/pilot-tracking-system.py commitments
   ```

2. **Update Weekly Summary**
   - Fill in Week 1 Summary in `documents/pilot-ces-daily-reports.md`

**Target:** 3-5 pilot commitments by end of Week 1

---

## 📞 Discovery Call Script

### Opening (2 min)
"Hi [Name], thanks for taking the time. I know you're busy, so I'll keep this brief - about 15 minutes.

I reached out because [School Name] has [specific program], and I think BallCODE could be a great fit for your students."

### Problem/Need (3 min)
"Are you seeing any challenges with:
- Student engagement in STEM subjects?
- Teaching coding concepts in an accessible way?
- Connecting coding to real-world applications?"

### Solution (5 min)
"BallCODE solves this by:
- Using basketball stories that students already love
- Teaching real coding skills (Blocks → Bridge → Python)
- Making concepts accessible through sports
- Providing teacher-ready implementation

The pilot is completely free and includes everything you need to get started."

### Value Proposition (3 min)
"What you get:
- Complete Episode 1 content
- Teacher resources and guides
- Student access to interactive games
- Ongoing support
- **Be part of our CES 2026 launch** (January 7-10)
- Opportunity to be featured in case studies"

### Close (2 min)
"Does this sound like something that could work for your students?

If yes, I can send you the pilot agreement today, and we can get started next week. The pilot is 2-4 weeks, completely free, and you can provide feedback to help us improve."

### Objection Handling

**"We don't have time for another program."**
- "I understand. The pilot is designed to be minimal prep - 15-20 minutes to get started, then students can work independently. Would a 2-week trial work?"

**"We don't have basketball programs."**
- "That's okay! The basketball stories are just the framework - students don't need to play basketball. The stories make coding concepts accessible. Would you like to see a sample?"

**"We already have coding programs."**
- "Great! BallCODE complements existing programs by teaching concepts through a different lens. It's story-driven and game-based, which can increase engagement. Would you be open to a pilot to see how it fits?"

---

## 📄 Pilot Agreement Template

**File:** `documents/pilot-agreement-template.md`

See separate file for complete template.

**Key Sections:**
- Pilot Program Overview
- What BallCODE Provides
- What School Provides
- Timeline (2-4 weeks)
- Feedback Requirements
- CES Launch Participation
- Agreement Terms

---

## 📊 Daily Metrics Tracking

**Track Daily:**
- Schools contacted today
- Responses received
- Calls scheduled
- Calls conducted
- Pilot agreements sent
- Pilot commitments secured

**Update:**
- `documents/school-contacts-database.json` - School statuses
- `documents/pilot-ces-daily-reports.md` - Daily metrics
- HubSpot - Pipeline stages
- Mailchimp - Email metrics

---

## 🎯 Success Criteria

**By End of Week 1 (Dec 27):**
- ✅ 80+ schools contacted
- ✅ 12-16 responses (15-20% response rate)
- ✅ 8-12 calls scheduled (10-15% call rate)
- ✅ 3-5 pilot commitments (14% conversion rate)
- ✅ All systems operational
- ✅ Tracking up to date

---

## 🔗 Key Resources

**Automation:**
- n8n workflow: `n8n-school-outreach-automation-workflow.json`
- Tracking script: `scripts/pilot-tracking-system.py`

**Templates:**
- Email templates: `documents/promotion-content/email-templates.json`
- Discovery call script: This document
- Pilot agreement: `documents/pilot-agreement-template.md`

**Tracking:**
- School database: `documents/school-contacts-database.json`
- Daily reports: `documents/pilot-ces-daily-reports.md`

---

**Version:** 1.0  
**Created:** December 21, 2025  
**Status:** Ready for Execution


