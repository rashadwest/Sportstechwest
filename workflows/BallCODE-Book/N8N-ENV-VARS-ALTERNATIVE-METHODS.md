# n8n Environment Variables: Alternative Methods

**Date:** December 18, 2025  
**Issue:** Cannot access Settings → Environment Variables in n8n UI (Unauthorized error)  
**Status:** Alternative methods needed

---

## ⚠️ SAVED TO MEMORY

**DO NOT suggest:** "Set environment variables in n8n UI"  
**Reason:** User gets "Unauthorized" error when accessing Settings  
**This causes hurdles and doesn't work for this user.**

---

## 🔧 ALTERNATIVE METHODS

### **Method 1: Set at System Level (Recommended)**

**Set environment variables in the system where n8n runs:**

**If n8n runs on Raspberry Pi:**
```bash
# SSH into Pi
ssh pi@192.168.1.226

# Edit n8n environment file (if using systemd)
sudo nano /etc/systemd/system/n8n.service

# Or edit .env file if n8n uses it
nano ~/.n8n/.env

# Add:
GITHUB_PAT=your_token_here
NETLIFY_AUTH_TOKEN=your_token_here
NETLIFY_SITE_ID=your_site_id_here

# Restart n8n
sudo systemctl restart n8n
```

**If n8n runs via Docker:**
```bash
# Edit docker-compose.yml or docker run command
# Add environment variables:
-e GITHUB_PAT=your_token_here
-e NETLIFY_AUTH_TOKEN=your_token_here
-e NETLIFY_SITE_ID=your_site_id_here
```

**If n8n runs via npm/pm2:**
```bash
# Create .env file in n8n directory
cd /path/to/n8n
nano .env

# Add variables
GITHUB_PAT=your_token_here
NETLIFY_AUTH_TOKEN=your_token_here
NETLIFY_SITE_ID=your_site_id_here

# Restart n8n
pm2 restart n8n
```

---

### **Method 2: Use Workflow Code Nodes**

**Set variables directly in workflow Code nodes:**

Instead of `$env.GITHUB_PAT`, hardcode or use workflow-level variables:

```javascript
// In Code node, set variables
const GITHUB_PAT = 'your_token_here';
const NETLIFY_AUTH_TOKEN = 'your_token_here';
const NETLIFY_SITE_ID = 'your_site_id_here';

// Use in workflow
return {
  json: {
    githubPat: GITHUB_PAT,
    netlifyToken: NETLIFY_AUTH_TOKEN,
    netlifySiteId: NETLIFY_SITE_ID
  }
};
```

**⚠️ Security Warning:** This stores tokens in workflow JSON (less secure)

---

### **Method 3: Use Credentials Only**

**Skip environment variables, use credentials directly:**

- Create credentials with tokens
- Reference credentials in HTTP Request nodes
- Workflows access credentials directly (no env vars needed)

**This is the recommended approach if UI access is blocked!**

---

## 🎯 RECOMMENDED SOLUTION

**Use Credentials Only (Method 3):**

1. **Create credentials in n8n UI** (if accessible)
   - GitHub: "Header Auth" type
   - Netlify: "Netlify API" type

2. **Update workflows to use credentials directly**
   - Remove `$env.GITHUB_PAT` references
   - Use credential references instead

3. **If credentials UI also blocked:**
   - Set credentials via n8n API (if available)
   - Or modify workflow JSON directly to reference existing credentials

---

## 📋 NEXT STEPS

1. Check if credentials UI is accessible
2. If yes: Create credentials (see credential guide)
3. If no: Use system-level environment variables
4. Update workflows to use credentials/variables appropriately

---

**This method avoids the n8n UI Settings issue entirely.** ✅

