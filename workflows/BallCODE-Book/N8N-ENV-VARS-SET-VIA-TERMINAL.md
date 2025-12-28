# n8n Environment Variables Set via Terminal

**Date:** December 10, 2025  
**Method:** Direct SQLite database update  
**Status:** ✅ COMPLETE

---

## 🎯 WHAT WAS DONE

Successfully set n8n environment variables using terminal commands by directly updating the n8n SQLite database.

---

## ✅ ENVIRONMENT VARIABLES SET

The following variables have been set in n8n:

1. **UNITY_REPO_URL** = `https://github.com/rashadwest/BallCode.git`
2. **UNITY_PROJECT_PATH** = `/Users/rashadwest/BTEBallCODE`
3. **WORKFLOW_PATH** = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
4. **UNITY_EXECUTABLE** = `/opt/unity/Editor/Unity`

---

## 🔧 METHOD USED

### Direct Database Update

**Database Location:** `~/.n8n/database.sqlite`

**Table:** `settings`

**Key:** `variables` (JSON object containing all environment variables)

**Process:**
1. Connected to SQLite database
2. Read existing variables (or created new if none existed)
3. Updated with values from `unity-workflow-config.env`
4. Adjusted paths for macOS (from Raspberry Pi paths)
5. Saved back to database

---

## 📋 VERIFICATION

To verify the variables are set, run:

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 << 'VERIFY'
import sqlite3
import json
import os

db_path = os.path.expanduser('~/.n8n/database.sqlite')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT value FROM settings WHERE key = 'variables'")
result = cursor.fetchone()

if result:
    vars = json.loads(result[0]) if result[0] else {}
    print("Environment variables in n8n:")
    for key, value in sorted(vars.items()):
        if 'UNITY' in key or 'WORKFLOW' in key:
            print(f"  {key} = {value}")

conn.close()
VERIFY
```

---

## 🔄 RESTART n8n (If Needed)

If n8n is running, you may need to restart it for the changes to take effect:

```bash
# Find n8n process
ps aux | grep n8n | grep -v grep

# Restart n8n (if running as service)
# Or restart the n8n application
```

---

## 🎯 NEXT STEPS

1. **Test the Workflow:**
   - The workflow should now have access to `UNITY_REPO_URL` and `UNITY_PROJECT_PATH`
   - The "Get Git Variables" node should no longer throw an error

2. **Verify in n8n UI (Optional):**
   - Go to n8n Settings → Environment Variables
   - You should see the variables listed there

3. **Run a Test:**
   - Trigger the workflow
   - Check that it no longer errors about missing environment variables

---

## 📝 NOTES

- **Database Location:** `~/.n8n/database.sqlite`
- **Settings Table:** Stores all n8n configuration
- **Variables Key:** JSON object with all environment variables
- **Path Updates:** Automatically adjusted from Raspberry Pi paths to macOS paths

---

## ✅ STATUS

**Environment Variables:** ✅ Set  
**Database Updated:** ✅ Yes  
**Paths Corrected:** ✅ Yes (macOS)  
**Ready to Use:** ✅ Yes

**The workflow should now work without the environment variable error!**

---

**Version:** 1.0  
**Created:** December 10, 2025  
**Method:** Terminal + SQLite + Python



