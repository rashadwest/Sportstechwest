# ⚙️ Orchestrator Workflow - Configuration Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Workflow:** AIMCODE (Demis) - Unity Build Orchestrator (12 nodes)  
**Status:** ✅ Loaded - Ready to Configure

---

## 📋 CONFIGURATION CHECKLIST

### **Step 1: Add Credentials to HTTP Request Nodes** ✅

You need to add credentials to **3 HTTP Request nodes**:

#### **1. Dispatch GitHub Build (AIMCODE L2)**
- **Node:** "Dispatch GitHub Build (AIMCODE L2)"
- **Credential Type:** GitHub Actions Token (httpHeaderAuth)
- **How to add:**
  1. Click on the node
  2. In the "Authentication" section, select "Header Auth"
  3. Choose or create: "GitHub Actions Token"
  4. Save the node

#### **2. Check Latest GitHub Run (AIMCODE L3)**
- **Node:** "Check Latest GitHub Run (AIMCODE L3)"
- **Credential Type:** GitHub Actions Token (httpHeaderAuth)
- **How to add:**
  1. Click on the node
  2. In the "Authentication" section, select "Header Auth"
  3. Choose: "GitHub Actions Token" (same as above)
  4. Save the node

#### **3. Check Latest Netlify Deploy (AIMCODE L3)**
- **Node:** "Check Latest Netlify Deploy (AIMCODE L3)"
- **Credential Type:** Netlify API Token (httpHeaderAuth)
- **How to add:**
  1. Click on the node
  2. In the "Authentication" section, select "Header Auth"
  3. Choose or create: "Netlify API Token"
  4. Save the node

---

### **Step 2: Verify Environment Variables** ✅

The workflow uses these environment variables (should already be set on Pi):

- `GITHUB_REPO_OWNER` - GitHub repository owner
- `GITHUB_REPO_NAME` - GitHub repository name
- `GITHUB_WORKFLOW_FILE` - GitHub Actions workflow file name
- `NETLIFY_SITE_ID` - Netlify site ID
- `NETLIFY_SITE_NAME` - Netlify site name (optional)
- `N8N_INSTANCE_ROLE` - Should be "prod" on Pi (prevents scheduled builds on dev)

**To verify:**
```bash
# On Pi, check environment variables
echo $GITHUB_REPO_OWNER
echo $GITHUB_REPO_NAME
echo $GITHUB_WORKFLOW_FILE
echo $NETLIFY_SITE_ID
echo $N8N_INSTANCE_ROLE
```

---

### **Step 3: Activate the Workflow** ✅

1. **In n8n UI:**
   - Find the workflow: "AIMCODE (Demis) - Unity Build Orchestrator"
   - Click the **toggle switch** in the top-right corner
   - It should turn green/blue and show "Active"

---

### **Step 4: Test the Workflow** ✅

Once activated, test the webhook:

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build after configuration",
    "branch": "main"
  }' | python3 -m json.tool
```

**Expected Response:**
- Status: "ok" or "skipped"
- Message with GitHub Actions and Netlify status
- GitHub and Netlify status information

---

## 🔑 CREDENTIAL SETUP

### **GitHub Actions Token**

**How to create:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Create token with `repo` scope
3. Copy the token

**In n8n:**
1. Go to Credentials → Add Credential
2. Select "Header Auth"
3. Name: "GitHub Actions Token"
4. Header Name: `Authorization`
5. Header Value: `Bearer YOUR_TOKEN` or `token YOUR_TOKEN`
6. Save

### **Netlify API Token**

**How to create:**
1. Go to Netlify → User settings → Applications → New access token
2. Create token with appropriate permissions
3. Copy the token

**In n8n:**
1. Go to Credentials → Add Credential
2. Select "Header Auth"
3. Name: "Netlify API Token"
4. Header Name: `Authorization`
5. Header Value: `Bearer YOUR_TOKEN`
6. Save

---

## ✅ VERIFICATION

After configuration, verify:

1. ✅ All 3 HTTP Request nodes have credentials (no red triangles)
2. ✅ Workflow is active (toggle switch is ON)
3. ✅ Webhook is accessible at: `http://192.168.1.226:5678/webhook/unity-build`
4. ✅ Test webhook returns success response

---

## 🚨 TROUBLESHOOTING

### **Red triangles still showing:**
- Credentials not saved properly
- Click each node and verify credentials are selected
- Make sure to click "Save" after selecting credentials

### **Webhook returns 404:**
- Workflow not activated
- Check toggle switch is ON

### **Build doesn't trigger:**
- Check GitHub Actions token has correct permissions
- Verify environment variables are set correctly
- Check GitHub repository name and owner are correct

---

**Status:** Ready to configure  
**Next:** Add credentials and activate

