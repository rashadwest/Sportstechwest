# 🚀 n8n CLI Terminal Editing Setup

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Status:** ✅ Complete  
**Method:** n8n CLI (export → edit → import)

---

## ⚡ Quick Start

### 1. List All Workflows

```bash
./n8n-list-workflows.sh
```

This shows all workflows with their IDs, names, and node counts.

### 2. Edit a Workflow

```bash
# Edit with default editor (nano)
./n8n-edit-workflow.sh WORKFLOW_ID

# Edit with vim
./n8n-edit-workflow.sh WORKFLOW_ID vim

# Edit with VS Code
./n8n-edit-workflow.sh WORKFLOW_ID code
```

**What it does:**
1. Exports workflow from n8n
2. Creates backup
3. Opens in your editor
4. Validates JSON
5. Imports back to n8n

---

## 🛠️ Available Tools

### n8n CLI Commands

**Export workflow:**
```bash
n8n export:workflow --id=WORKFLOW_ID --output=workflow.json --pretty
```

**Import workflow:**
```bash
n8n import:workflow --input=workflow.json
```

**Export all workflows:**
```bash
n8n export:workflow --all --output=backups/ --separate --pretty
```

### Helper Scripts

**List workflows:**
```bash
./n8n-list-workflows.sh
```

**Edit workflow:**
```bash
./n8n-edit-workflow.sh WORKFLOW_ID [editor]
```

---

## 📋 Complete Workflow

### Edit Workflow in Terminal

```bash
# 1. List workflows to find ID
./n8n-list-workflows.sh

# 2. Edit workflow
./n8n-edit-workflow.sh abc123 vim

# 3. Make changes in editor
# 4. Save and exit
# 5. Script validates and imports automatically
```

### Manual Export/Edit/Import

```bash
# Export
n8n export:workflow --id=WORKFLOW_ID --output=workflow.json --pretty

# Edit
vim workflow.json  # or your preferred editor

# Validate
python3 -m json.tool workflow.json > /dev/null

# Import
n8n import:workflow --input=workflow.json
```

---

## 🎯 Two Methods Available

### Method 1: n8n CLI (This Setup)
- ✅ Direct n8n CLI integration
- ✅ Export → Edit → Import
- ✅ Works with any editor
- ✅ Automatic backup

### Method 2: API-Based (Previous Setup)
- ✅ REST API integration
- ✅ `deploy-n8n-workflow.sh`
- ✅ `n8n-workflow-editor.sh`
- ✅ Works remotely

**Both methods work! Use whichever you prefer.**

---

## 🔧 Configuration

### Set Default Editor

```bash
# In your ~/.zshrc or ~/.bashrc
export EDITOR=vim  # or nano, code, etc.
```

### Environment Variables

The scripts use:
- `$EDITOR` - Default editor (falls back to `nano`)
- `$VISUAL` - Alternative editor variable

---

## ✅ Verification

**Test the setup:**
```bash
# 1. Check n8n CLI
n8n --version

# 2. List workflows
./n8n-list-workflows.sh

# 3. Test edit (use a test workflow ID)
./n8n-edit-workflow.sh TEST_ID
```

---

## 📖 Related Documentation

- **`N8N-CURSOR-EDITING-SYSTEM.md`** - API-based editing system
- **`N8N-TERMINAL-QUICK-START.md`** - Quick reference
- **`N8N_WORKFLOW_DEVELOPMENT_GUIDE.md`** - Best practices

---

**Status:** ✅ Ready to Use  
**Next:** Run `./n8n-list-workflows.sh` to see your workflows!




