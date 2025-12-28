# Complete Documentation Checklist
## Everything You Can Document to Hold Cursor Accountable

**Purpose:** Comprehensive list of all evidence you can collect  
**Use:** Check off items as you document them

---

## 📋 QUICK REFERENCE: What to Document

### ✅ Codebase Evidence (Automated)
- [ ] File inventory
- [ ] Git history
- [ ] File types and counts
- [ ] Activity timeline
- [ ] Copyright notices

### ✅ Cursor Usage Evidence (Manual)
- [ ] `.cursorrules` file
- [ ] Cursor settings screenshots
- [ ] Cursor configuration files
- [ ] Documentation mentioning Cursor
- [ ] Cursor-generated code/comments

### ✅ Communication Evidence (Manual)
- [ ] All emails to/from Cursor
- [ ] Support tickets
- [ ] Response times
- [ ] Response content
- [ ] Non-responses

### ✅ Legal Documents (Manual)
- [ ] Terms of Service (with dates)
- [ ] Privacy Policy (with dates)
- [ ] Any agreements signed
- [ ] Policy changes over time

### ✅ Settings & Configuration (Manual)
- [ ] Privacy settings
- [ ] Data sharing settings
- [ ] Opt-out status
- [ ] Account settings
- [ ] Local configuration files

---

## 📁 CATEGORY 1: CODEBASE EVIDENCE

### 1.1 File Inventory

**What to Document:**
- Total file count
- Files by type (.md, .py, .cs, .js, .json, etc.)
- File sizes
- File locations
- File creation dates
- File modification dates

**How to Document:**
```bash
# Run the automated script
./collect-cursor-evidence.sh

# Or manually:
find . -type f ! -path "./.git/*" > file-list.txt
find . -name "*.md" | wc -l  # Count markdown files
find . -name "*.py" | wc -l  # Count Python files
find . -name "*.cs" | wc -l  # Count C# files
```

**Save As:**
- `CURSOR-EVIDENCE/file-list.txt`
- `CURSOR-EVIDENCE/file-type-breakdown.txt`
- `CURSOR-EVIDENCE/CODEBASE-INVENTORY-LEGAL.txt`

**Checklist:**
- [ ] Complete file list exported
- [ ] File type breakdown created
- [ ] File counts documented
- [ ] File sizes calculated (if relevant)

### 1.2 Git History

**What to Document:**
- All commit dates
- All commit messages
- All commit authors
- All commit hashes
- Files changed in each commit
- Activity timeline

**How to Document:**
```bash
# Complete git history
git log --all --format="%ai|%H|%an|%s" > git-history.txt

# Timeline by date
git log --all --format="%ai|%s" --date=iso | sort > timeline.txt

# First and last commits
git log --all --format="%ai" | tail -1  # First
git log --all --format="%ai" | head -1  # Last
```

**Save As:**
- `CURSOR-EVIDENCE/git-history.txt`
- `CURSOR-EVIDENCE/activity-timeline.txt`
- `CURSOR-EVIDENCE/commit-statistics.txt`

**Checklist:**
- [ ] Complete git history exported
- [ ] Activity timeline created
- [ ] First commit date documented
- [ ] Last commit date documented
- [ ] Total commit count recorded

### 1.3 Code Content

**What to Document:**
- Python scripts (list all)
- C# Unity scripts (list all)
- JavaScript files (list all)
- Configuration files (list all)
- Documentation files (list all)
- Key algorithms or proprietary code

**How to Document:**
```bash
# List all code files
find . -name "*.py" > python-files.txt
find . -name "*.cs" > csharp-files.txt
find . -name "*.js" > javascript-files.txt

# List key files
ls -la scripts/ > scripts-list.txt
ls -la Unity-Scripts/ > unity-scripts-list.txt
```

**Save As:**
- `CURSOR-EVIDENCE/code-files-inventory.txt`
- `CURSOR-EVIDENCE/python-scripts-list.txt`
- `CURSOR-EVIDENCE/csharp-scripts-list.txt`

**Checklist:**
- [ ] All Python files listed
- [ ] All C# files listed
- [ ] All JavaScript files listed
- [ ] Key files identified
- [ ] Proprietary code documented

### 1.4 Copyright & IP

**What to Document:**
- Copyright notices in files
- License information
- Proprietary content
- Trade secrets (if any)
- Original creation dates
- Author information

**How to Document:**
```bash
# Find copyright notices
grep -r -i "copyright" --include="*.md" --include="*.py" --include="*.cs" . > copyright-notices.txt

# Find license information
find . -name "LICENSE*" -o -name "COPYRIGHT*" > license-files.txt
```

**Save As:**
- `CURSOR-EVIDENCE/copyright-notices.txt`
- `CURSOR-EVIDENCE/license-information.txt`
- `CURSOR-EVIDENCE/IP-inventory.txt`

**Checklist:**
- [ ] Copyright notices found and documented
- [ ] License information collected
- [ ] Proprietary content identified
- [ ] Creation dates documented
- [ ] Author information recorded

---

## 📁 CATEGORY 2: CURSOR USAGE EVIDENCE

### 2.1 Cursor Configuration Files

**What to Document:**
- `.cursorrules` file (content, size, dates)
- `.cursor/` directory (if exists)
- Cursor settings files
- Cursor configuration files
- MCP (Model Context Protocol) configurations

**How to Document:**
```bash
# Copy .cursorrules
cp .cursorrules CURSOR-EVIDENCE/.cursorrules

# Check for .cursor directory
ls -la .cursor/ > cursor-directory-contents.txt 2>/dev/null || echo "No .cursor directory"

# Find all Cursor-related files
find . -name "*cursor*" -type f > cursor-files.txt
find . -name ".cursor*" -type f > cursor-dotfiles.txt
```

**Save As:**
- `CURSOR-EVIDENCE/.cursorrules` (copy)
- `CURSOR-EVIDENCE/cursor-configuration-files.txt`
- `CURSOR-EVIDENCE/cursor-directory-contents.txt`

**Checklist:**
- [ ] `.cursorrules` file copied
- [ ] `.cursorrules` line count documented
- [ ] `.cursorrules` creation date recorded
- [ ] `.cursorrules` modification date recorded
- [ ] Cursor directory contents listed (if exists)
- [ ] All Cursor config files found

### 2.2 Cursor Settings (Screenshots)

**What to Document:**
- Privacy settings (screenshot)
- Data sharing settings (screenshot)
- Telemetry settings (screenshot)
- Training data opt-out (screenshot, if exists)
- Account settings (screenshot)
- Any opt-in/opt-out toggles (screenshot)

**How to Document:**
1. Open Cursor
2. Go to Settings (Cmd/Ctrl + ,)
3. Navigate to each section
4. Take screenshots
5. Save with descriptive names

**Save As:**
- `CURSOR-EVIDENCE/settings-screenshots/privacy-settings-2025-12-09.png`
- `CURSOR-EVIDENCE/settings-screenshots/data-sharing-2025-12-09.png`
- `CURSOR-EVIDENCE/settings-screenshots/telemetry-2025-12-09.png`
- `CURSOR-EVIDENCE/settings-screenshots/account-settings-2025-12-09.png`

**Checklist:**
- [ ] Privacy settings screenshot taken
- [ ] Data sharing settings screenshot taken
- [ ] Telemetry settings screenshot taken
- [ ] Training data opt-out screenshot taken (if exists)
- [ ] Account settings screenshot taken
- [ ] All screenshots dated and named clearly

### 2.3 Cursor Local Configuration

**What to Document:**
- Cursor application settings files
- Cursor user preferences
- Cursor workspace settings
- Cursor extension configurations
- Cursor cache files (if relevant)

**How to Document:**
```bash
# macOS
ls -la ~/Library/Application\ Support/Cursor/ > cursor-app-config-macos.txt

# Windows
# ls -la %APPDATA%\Cursor\ > cursor-app-config-windows.txt

# Linux
# ls -la ~/.config/Cursor/ > cursor-app-config-linux.txt

# Search for settings files
find ~/Library/Application\ Support/Cursor/ -name "*.json" > cursor-settings-files.txt
```

**Save As:**
- `CURSOR-EVIDENCE/cursor-app-config-[OS].txt`
- `CURSOR-EVIDENCE/cursor-settings-files.txt`
- `CURSOR-EVIDENCE/cursor-preferences.txt`

**Checklist:**
- [ ] Cursor application directory located
- [ ] Settings files listed
- [ ] Preferences documented
- [ ] Configuration files copied (if safe to do so)

### 2.4 Cursor Mentions in Documentation

**What to Document:**
- All files mentioning "Cursor"
- Documentation about Cursor usage
- Guides referencing Cursor
- Integration documentation
- Any Cursor-related content

**How to Document:**
```bash
# Find all Cursor mentions
grep -r -i "cursor" --include="*.md" --include="*.txt" . > cursor-mentions.txt

# Count mentions
grep -r -i "cursor" --include="*.md" . | wc -l

# List files with Cursor mentions
grep -r -l -i "cursor" --include="*.md" . > files-mentioning-cursor.txt
```

**Save As:**
- `CURSOR-EVIDENCE/cursor-mentions.txt`
- `CURSOR-EVIDENCE/files-mentioning-cursor.txt`
- `CURSOR-EVIDENCE/cursor-documentation-list.txt`

**Checklist:**
- [ ] All Cursor mentions found
- [ ] Files with Cursor mentions listed
- [ ] Cursor documentation identified
- [ ] Integration guides documented

### 2.5 Cursor-Generated Content

**What to Document:**
- Code generated by Cursor (if identifiable)
- Comments added by Cursor
- Documentation created with Cursor
- Any AI-generated markers
- Cursor suggestions accepted

**How to Document:**
- Review git history for patterns
- Look for Cursor-style comments
- Check for AI-generated patterns
- Document any identifiable Cursor output

**Save As:**
- `CURSOR-EVIDENCE/cursor-generated-content.txt`
- `CURSOR-EVIDENCE/cursor-suggestions-log.txt`

**Checklist:**
- [ ] Cursor-generated code identified (if possible)
- [ ] Cursor comments documented
- [ ] AI-generated patterns noted
- [ ] Cursor usage patterns documented

---

## 📁 CATEGORY 3: COMMUNICATION EVIDENCE

### 3.1 Email Communications

**What to Document:**
- All emails sent to Cursor
- All emails received from Cursor
- Email dates and times
- Email subjects
- Email content (full text)
- Email attachments
- Response times

**How to Document:**
1. Export emails from your email client
2. Save as PDF or text files
3. Organize by date
4. Create a log

**Save As:**
- `CURSOR-EVIDENCE/communications/email-2025-12-09-initial-request.txt`
- `CURSOR-EVIDENCE/communications/email-2025-12-09-response.txt`
- `CURSOR-EVIDENCE/communications/email-log.csv`

**Email Log Template:**
```csv
Date,Time,From,To,Subject,Response_Time_Days,Status,File
2025-12-09,10:00,me@email.com,legal@cursor.com,Data Request,0,Pending,email-2025-12-09-initial.txt
```

**Checklist:**
- [ ] All emails to Cursor saved
- [ ] All emails from Cursor saved
- [ ] Email dates documented
- [ ] Response times calculated
- [ ] Email log created

### 3.2 Support Tickets

**What to Document:**
- Ticket numbers
- Ticket dates
- Ticket subjects
- Ticket content
- Responses received
- Resolution status
- Response times

**How to Document:**
- Screenshot support tickets
- Export ticket history
- Create ticket log

**Save As:**
- `CURSOR-EVIDENCE/communications/support-ticket-[#].txt`
- `CURSOR-EVIDENCE/communications/support-ticket-log.csv`

**Checklist:**
- [ ] All support tickets documented
- [ ] Ticket numbers recorded
- [ ] Ticket content saved
- [ ] Responses documented
- [ ] Response times calculated

### 3.3 Response Tracking

**What to Document:**
- Response received: Yes/No
- Response date
- Response time (days)
- Response content
- Response quality (complete/incomplete)
- Follow-up needed: Yes/No

**How to Document:**
Create a tracking spreadsheet or document

**Save As:**
- `CURSOR-EVIDENCE/communications/response-tracking.csv`
- `CURSOR-EVIDENCE/communications/response-analysis.txt`

**Template:**
```csv
Request_Date,Request_Type,Response_Received,Response_Date,Days_To_Respond,Complete,Follow_Up_Needed
2025-12-09,GDPR Request,No,,,No,Yes
```

**Checklist:**
- [ ] Response tracking log created
- [ ] Response times documented
- [ ] Response completeness assessed
- [ ] Follow-up needs identified

---

## 📁 CATEGORY 4: LEGAL DOCUMENTS

### 4.1 Terms of Service

**What to Document:**
- Current Terms of Service
- Terms of Service version/date
- Terms of Service URL
- Key clauses about data usage
- Key clauses about training data
- Changes over time (if you have old versions)

**How to Document:**
1. Visit Cursor website
2. Download Terms of Service
3. Save with date
4. Highlight key sections
5. Create summary

**Save As:**
- `CURSOR-EVIDENCE/legal-documents/cursor-terms-of-service-2025-12-09.pdf`
- `CURSOR-EVIDENCE/legal-documents/terms-summary.txt`
- `CURSOR-EVIDENCE/legal-documents/terms-key-clauses.txt`

**Checklist:**
- [ ] Current Terms of Service downloaded
- [ ] Terms date/version recorded
- [ ] Key clauses highlighted
- [ ] Data usage clauses documented
- [ ] Training data clauses documented
- [ ] Summary created

### 4.2 Privacy Policy

**What to Document:**
- Current Privacy Policy
- Privacy Policy version/date
- Privacy Policy URL
- Data collection policies
- Data usage policies
- Training data policies
- Opt-out mechanisms
- Changes over time (if you have old versions)

**How to Document:**
1. Visit Cursor website
2. Download Privacy Policy
3. Save with date
4. Highlight key sections
5. Create summary

**Save As:**
- `CURSOR-EVIDENCE/legal-documents/cursor-privacy-policy-2025-12-09.pdf`
- `CURSOR-EVIDENCE/legal-documents/privacy-summary.txt`
- `CURSOR-EVIDENCE/legal-documents/privacy-key-sections.txt`

**Checklist:**
- [ ] Current Privacy Policy downloaded
- [ ] Privacy Policy date/version recorded
- [ ] Data collection policies documented
- [ ] Data usage policies documented
- [ ] Training data policies documented
- [ ] Opt-out mechanisms documented
- [ ] Summary created

### 4.3 Agreements & Contracts

**What to Document:**
- Any agreements you signed
- Any contracts with Cursor
- Any NDAs (if applicable)
- Any data processing agreements
- Agreement dates
- Agreement terms

**How to Document:**
- Locate any signed agreements
- Copy or screenshot
- Save with dates
- Create summary

**Save As:**
- `CURSOR-EVIDENCE/legal-documents/agreement-[name]-[date].pdf`
- `CURSOR-EVIDENCE/legal-documents/agreements-summary.txt`

**Checklist:**
- [ ] All agreements located
- [ ] Agreements saved
- [ ] Agreement dates recorded
- [ ] Key terms documented
- [ ] Summary created

### 4.4 Policy Changes

**What to Document:**
- Terms of Service changes
- Privacy Policy changes
- When changes occurred
- What changed
- How you were notified

**How to Document:**
- Compare current vs. old versions (if you have them)
- Check Wayback Machine (archive.org)
- Document any change notifications
- Create change log

**Save As:**
- `CURSOR-EVIDENCE/legal-documents/policy-changes-log.txt`
- `CURSOR-EVIDENCE/legal-documents/terms-comparison.txt`

**Checklist:**
- [ ] Policy versions compared (if possible)
- [ ] Changes documented
- [ ] Change dates recorded
- [ ] Notifications documented

---

## 📁 CATEGORY 5: SETTINGS & CONFIGURATION

### 5.1 Application Settings

**What to Document:**
- All privacy settings
- All data sharing settings
- All telemetry settings
- All opt-out options
- Current state of each setting
- Settings location/path

**How to Document:**
- Take screenshots (see Category 2.2)
- Export settings files (if possible)
- Create settings inventory
- Document current state

**Save As:**
- `CURSOR-EVIDENCE/settings/application-settings-inventory.txt`
- `CURSOR-EVIDENCE/settings/current-settings-state.txt`

**Checklist:**
- [ ] All settings screenshotted
- [ ] Settings inventory created
- [ ] Current state documented
- [ ] Settings locations recorded

### 5.2 Account Settings

**What to Document:**
- Account type (free/paid)
- Account creation date
- Account settings
- Privacy preferences
- Data sharing preferences
- Opt-out status

**How to Document:**
- Screenshot account page
- Document account details
- Record preferences

**Save As:**
- `CURSOR-EVIDENCE/settings/account-settings.txt`
- `CURSOR-EVIDENCE/settings/account-details.txt`

**Checklist:**
- [ ] Account settings documented
- [ ] Account type recorded
- [ ] Account creation date recorded
- [ ] Preferences documented

### 5.3 Workspace Settings

**What to Document:**
- Workspace-specific settings
- Project settings
- Local configuration
- `.cursorrules` settings (already covered)

**How to Document:**
- Check workspace config files
- Document workspace settings
- Record project-specific configs

**Save As:**
- `CURSOR-EVIDENCE/settings/workspace-settings.txt`
- `CURSOR-EVIDENCE/settings/project-config.txt`

**Checklist:**
- [ ] Workspace settings documented
- [ ] Project settings recorded
- [ ] Local configs documented

---

## 📁 CATEGORY 6: TIMELINE & ACTIVITY

### 6.1 Usage Timeline

**What to Document:**
- When you started using Cursor
- When you created repository
- When you added `.cursorrules`
- Key development dates
- Major code additions
- Activity peaks

**How to Document:**
- Review git history
- Check file creation dates
- Create timeline document

**Save As:**
- `CURSOR-EVIDENCE/timeline/usage-timeline.txt`
- `CURSOR-EVIDENCE/timeline/activity-timeline.txt`

**Checklist:**
- [ ] Usage start date documented
- [ ] Key dates identified
- [ ] Timeline created
- [ ] Activity peaks noted

### 6.2 Development Activity

**What to Document:**
- Development periods
- Active development dates
- Code addition dates
- Documentation creation dates
- Peak activity periods

**How to Document:**
- Analyze git history
- Identify activity patterns
- Document peak periods

**Save As:**
- `CURSOR-EVIDENCE/timeline/development-activity.txt`
- `CURSOR-EVIDENCE/timeline/activity-analysis.txt`

**Checklist:**
- [ ] Development periods documented
- [ ] Activity patterns identified
- [ ] Peak periods noted
- [ ] Analysis created

---

## 📁 CATEGORY 7: EVIDENCE INTEGRITY

### 7.1 Checksums & Verification

**What to Document:**
- File checksums (SHA-256)
- File integrity verification
- Evidence chain of custody
- Timestamps

**How to Document:**
```bash
# Create checksums
find CURSOR-EVIDENCE -type f -exec shasum -a 256 {} \; > checksums.txt
```

**Save As:**
- `CURSOR-EVIDENCE/checksums.txt`
- `CURSOR-EVIDENCE/integrity-verification.txt`

**Checklist:**
- [ ] Checksums created
- [ ] Integrity verified
- [ ] Timestamps documented

### 7.2 Evidence Log

**What to Document:**
- What evidence was collected
- When it was collected
- How it was collected
- Who collected it
- Where it's stored

**How to Document:**
- Create evidence log
- Document collection process
- Record dates and methods

**Save As:**
- `CURSOR-EVIDENCE/evidence-log.txt`
- `CURSOR-EVIDENCE/collection-process.txt`

**Checklist:**
- [ ] Evidence log created
- [ ] Collection process documented
- [ ] Dates recorded
- [ ] Methods documented

---

## 📊 MASTER CHECKLIST

### Automated Collection (Run Script)
- [ ] Run `./collect-cursor-evidence.sh`
- [ ] Review generated evidence
- [ ] Verify all files created

### Manual Collection - Codebase
- [ ] File inventory complete
- [ ] Git history exported
- [ ] Code files listed
- [ ] Copyright notices found

### Manual Collection - Cursor Usage
- [ ] `.cursorrules` copied
- [ ] Settings screenshots taken
- [ ] Configuration files documented
- [ ] Cursor mentions found

### Manual Collection - Communication
- [ ] Emails saved
- [ ] Support tickets documented
- [ ] Response tracking created
- [ ] Communication log complete

### Manual Collection - Legal Documents
- [ ] Terms of Service downloaded
- [ ] Privacy Policy downloaded
- [ ] Agreements located
- [ ] Policy changes documented

### Manual Collection - Settings
- [ ] Application settings documented
- [ ] Account settings documented
- [ ] Workspace settings documented
- [ ] Current state recorded

### Manual Collection - Timeline
- [ ] Usage timeline created
- [ ] Activity timeline created
- [ ] Development periods documented

### Evidence Integrity
- [ ] Checksums created
- [ ] Evidence log complete
- [ ] Collection process documented

---

## 🎯 PRIORITY ORDER

### High Priority (Do First)
1. ✅ Run automated script
2. ✅ Document `.cursorrules`
3. ✅ Screenshot settings
4. ✅ Download legal documents
5. ✅ Create communication log

### Medium Priority (Do This Week)
1. ✅ Complete file inventory
2. ✅ Document all communications
3. ✅ Review legal documents
4. ✅ Create timeline
5. ✅ Document settings

### Lower Priority (Do If Time)
1. ✅ Deep code analysis
2. ✅ Policy change tracking
3. ✅ Advanced configuration review
4. ✅ Detailed timeline analysis

---

## 📝 NOTES TEMPLATE

**Create:** `CURSOR-EVIDENCE/NOTES.txt`

Use this to record:
- Any issues encountered
- Additional findings
- Questions to research
- Next steps
- Important observations

---

**Remember:** Document everything. You can't have too much evidence. Better to over-document than under-document.

**Last Updated:** 2025-12-09




