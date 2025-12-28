# 🔧 Local n8n .env File Setup Guide

**Your Setup:** Local n8n (not cloud, not remote Pi)  
**Method:** `.env` file in n8n project directory  
**Status:** Ready to configure

---

## 🎯 QUICK SETUP (Automated)

### Run the Setup Script:

```bash
cd ~/Desktop
./setup-n8n-env-file.sh
```

**This will:**
1. Find your n8n directory
2. Create/update `.env` file
3. Add required variables
4. Show you where it was created

---

## 📋 MANUAL SETUP (If You Prefer)

### Step 1: Find Your n8n Directory

**This is where you run `n8n start`**

Common locations:
- `~/.n8n` (default n8n directory)
- `~/n8n` (if you created it)
- Current directory where you run `n8n start`

**To find it:**
```bash
# Check where n8n is running
ps aux | grep n8n

# Or check common locations
ls -la ~/.n8n
ls -la ~/n8n
```

### Step 2: Create .env File

**In your n8n directory, create `.env` file:**

```bash
cd ~/.n8n  # or wherever your n8n directory is
nano .env  # or use your preferred editor
```

### Step 3: Add Environment Variables

**Paste this into the `.env` file:**

```bash
# Unity Automation Environment Variables
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

**Save the file** (Ctrl+X, then Y, then Enter in nano)

### Step 4: Restart n8n

**If running in terminal:**
```bash
# Stop n8n (Ctrl+C in the terminal where it's running)
# Then restart:
n8n start
```

**If running as a service:**
```bash
n8n stop
n8n start
```

### Step 5: Test Variables

**In n8n workflow:**
1. Add a **Code** node
2. In the code editor, type:
   ```javascript
   {{ $env.UNITY_REPO_URL }}
   ```
3. Execute the node
4. Should show: `https://github.com/rashadwest/BallCode.git`

**Or test in any node's Expression field:**
- Type: `{{ $env.UNITY_REPO_URL }}`
- Should resolve to the URL

---

## 🔒 SECURITY NOTES

**Important:**
- ✅ **DO NOT** commit `.env` to Git
- ✅ Add `.env` to `.gitignore`
- ✅ Keep `.env` file secure
- ✅ Don't share `.env` file

**Add to .gitignore:**
```bash
echo ".env" >> .gitignore
```

---

## ✅ VERIFY IT WORKED

**After restarting n8n:**

1. **Test in workflow:**
   - Execute "Get Git Variables" node
   - Should show: `repoUrlSet: true, projectPathSet: true`

2. **Check .env file:**
   ```bash
   cat ~/.n8n/.env
   # Should show your variables
   ```

3. **Test in Code node:**
   ```javascript
   const repoUrl = $env.UNITY_REPO_URL;
   console.log('Repo URL:', repoUrl);
   return { json: { repoUrl: repoUrl } };
   ```

---

## 🐛 TROUBLESHOOTING

### Variables Not Working?

**Check:**
1. **.env file location** - Must be in n8n project directory
2. **File name** - Must be exactly `.env` (not `.env.txt`)
3. **n8n restarted** - Variables only load on startup
4. **Syntax** - No spaces around `=` sign
5. **No quotes needed** - Just `VARIABLE=value`

### Can't Find n8n Directory?

**Find where n8n is running:**
```bash
# Check running processes
ps aux | grep n8n

# Check where n8n was installed
which n8n

# Check n8n config
n8n --version
```

### Variables Still Not Working?

**Try:**
1. **Check .env file exists:**
   ```bash
   ls -la ~/.n8n/.env
   ```

2. **Check file contents:**
   ```bash
   cat ~/.n8n/.env
   ```

3. **Restart n8n completely:**
   ```bash
   # Kill all n8n processes
   pkill -f n8n
   # Then restart
   n8n start
   ```

---

## 📋 COMPLETE .env FILE EXAMPLE

**Your complete `.env` file should look like:**

```bash
# n8n Configuration
N8N_PORT=5678
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=rashad
N8N_BASIC_AUTH_PASSWORD=yourpassword

# Unity Automation Environment Variables
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

---

## ✅ DONE!

**After setup:**
1. ✅ `.env` file created with variables
2. ✅ n8n restarted
3. ✅ Variables accessible in workflows
4. ✅ "Get Git Variables" node should work

**Test your workflow now!**

---

**Status:** Ready to set up  
**Action:** Run `./setup-n8n-env-file.sh` or create `.env` manually  
**Time:** 2 minutes



