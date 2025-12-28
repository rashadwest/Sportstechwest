# Memory: User Preference - Environment Variables in ~/.zshrc

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Type:** User Preference (Permanent Memory)

---

## 🎯 USER PREFERENCE

**User Request:**
> "set to memory i want to set all vaiables to ~/.zshrc from now on as long as it is safe"

**Preference:** All environment variables should be saved to `~/.zshrc` from now on, as long as it's safe.

---

## ✅ SAFE PRACTICES (MANDATORY)

**When adding variables to ~/.zshrc:**

1. **Always use safe script:** `scripts/safe-add-to-zshrc.sh`
   - Checks for duplicates
   - Creates backup (.bak file)
   - Asks before replacing existing variables
   - Adds timestamp comments

2. **Never:**
   - ❌ Add without checking for duplicates
   - ❌ Overwrite without asking
   - ❌ Add secrets without explicit user permission
   - ❌ Modify system-wide files (only user's ~/.zshrc)

3. **Always:**
   - ✅ Check if variable exists first
   - ✅ Create backup before modifying
   - ✅ Ask before replacing existing values
   - ✅ Add comments with timestamps
   - ✅ Use safe script for all additions

---

## 🔧 SCRIPT USAGE

**Safe script location:**
- `scripts/safe-add-to-zshrc.sh`

**Usage:**
```bash
./scripts/safe-add-to-zshrc.sh VARIABLE_NAME "value"
```

**Example:**
```bash
./scripts/safe-add-to-zshrc.sh NETLIFY_SITE_ID "39ebfb47-c716-4f38-8f8b-7bfba36f3dc7"
```

---

## 📋 AI ASSISTANT RULES

**For ALL future environment variable setups:**

1. **Always suggest ~/.zshrc** (not just export in current session)
2. **Always use safe script** (`safe-add-to-zshrc.sh`)
3. **Always check for duplicates** before adding
4. **Always create backup** before modifying
5. **Always ask before replacing** existing variables
6. **Never add secrets** without explicit user permission

---

## ✅ MEMORY STATUS

**This preference is saved and will be followed for:**
- ✅ All future environment variable setups
- ✅ All automation scripts
- ✅ All deployment configurations
- ✅ All development environment setups

---

**Status:** ✅ **PERMANENT MEMORY** - This preference will be followed for all future variable setups

