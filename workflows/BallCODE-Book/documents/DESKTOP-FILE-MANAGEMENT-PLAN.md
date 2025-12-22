# Desktop File Management Plan

**Date:** December 12, 2025  
**Goal:** Organize desktop files, prevent duplicates, minimize file creation

---

## 🎯 RULES FOR DESKTOP FILES

### 1. **ONLY Essential JSON Files to Desktop**
- ✅ **ONLY** copy the n8n workflow JSON file that needs to be uploaded to n8n
- ✅ **File name:** `n8n-unity-automation-workflow-FINAL-WORKING.json` (or current working version)
- ❌ **DO NOT** copy documentation files to desktop
- ❌ **DO NOT** create multiple versions on desktop
- ❌ **DO NOT** copy status reports, research docs, or summaries to desktop

### 2. **Check Before Copying**
- ✅ Check if file already exists on desktop before copying
- ✅ If exists, ask user if they want to replace it
- ✅ Use same filename to avoid duplicates

### 3. **Documentation in Chat**
- ✅ Put new documentation in chat (markdown format)
- ✅ User can open in chat if needed
- ❌ **DO NOT** create documentation files unless explicitly requested
- ❌ **DO NOT** create status reports as files

### 4. **Desktop Organization**
- ✅ Keep desktop clean - only essential upload files
- ✅ Use consistent filename: `n8n-unity-automation-workflow-FINAL-WORKING.json`
- ✅ Replace old version instead of creating new ones

---

## 📋 CURRENT DESKTOP FILE STATUS

### What Should Be on Desktop:
- ✅ `n8n-unity-automation-workflow-FINAL-WORKING.json` (if needs upload)

### What Should NOT Be on Desktop:
- ❌ Documentation files (`.md` files)
- ❌ Status reports
- ❌ Research documents
- ❌ Multiple workflow versions
- ❌ Backup files

---

## 🔧 IMPLEMENTATION

### When to Copy to Desktop:
**ONLY** when:
1. Workflow JSON file has been updated
2. File needs to be uploaded to n8n
3. User explicitly requests it

### Process:
```bash
# 1. Check if file exists
if [ -f ~/Desktop/n8n-unity-automation-workflow-FINAL-WORKING.json ]; then
  # Ask user if they want to replace
  # Or just replace silently (same filename = no duplicate)
fi

# 2. Copy only the essential file
cp n8n-unity-automation-workflow-FINAL-WORKING.json ~/Desktop/

# 3. DO NOT copy any other files
```

### Documentation Approach:
Instead of creating files, put in chat:
```markdown
## Status Report

[Content here - user can read in chat or copy if needed]
```

---

## 📝 UPDATED WORKFLOW

### Before (Old Way):
1. Update workflow JSON
2. Copy JSON to desktop
3. Create status report file
4. Create research document file
5. Create summary file
6. Desktop gets cluttered

### After (New Way):
1. Update workflow JSON
2. Copy ONLY JSON to desktop (if needs upload)
3. Put status/research/summary in chat
4. Desktop stays clean

---

## ✅ CHECKLIST

Before copying to desktop:
- [ ] Is this the essential JSON file that needs upload?
- [ ] Does file already exist on desktop? (replace, don't duplicate)
- [ ] Is this documentation? (put in chat instead)
- [ ] Is this a status report? (put in chat instead)

---

## 🎯 GOAL

**Desktop should have:**
- ✅ Only the current workflow JSON file (when needed for upload)
- ✅ Nothing else

**Chat should have:**
- ✅ All documentation
- ✅ Status reports
- ✅ Research findings
- ✅ Summaries

**Project directory should have:**
- ✅ All source files
- ✅ All documentation files
- ✅ All workflow versions (for version control)

---

**Status:** Plan ready for implementation
