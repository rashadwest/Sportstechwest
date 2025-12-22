# AIMCODE Analysis: Environment Variables Solution

**Date:** December 18, 2025  
**Methodology:** AIMCODE (5-Layer Approach)  
**Goal:** Find best solution for setting n8n environment variables

---

## 🔍 ANALYZE (Layer 1: Foundation)

### **Problem:**
- Cannot access n8n UI Settings → Environment Variables (Unauthorized error)
- Unity Build Orchestrator needs these env vars:
  - `GITHUB_REPO_OWNER` = "rashadwest"
  - `GITHUB_REPO_NAME` = "BTEBallCODE"
  - `GITHUB_WORKFLOW_FILE` = "unity-webgl-build.yml"
  - `NETLIFY_SITE_ID` = "[site ID]"

### **Options Available:**

#### **Option A: System-Level Environment Variables**
- **Where:** Set on Raspberry Pi where n8n runs
- **How:** Edit systemd service file or .env file
- **Access:** Requires SSH to Pi (192.168.1.226)
- **Persistence:** Permanent, survives restarts
- **Security:** Tokens stored in system, not in workflow code

#### **Option B: Hardcode in Workflow JSON**
- **Where:** Modify workflow Code nodes directly
- **How:** Replace `$env.VARIABLE` with hardcoded values
- **Access:** Edit workflow JSON file locally
- **Persistence:** Permanent in workflow file
- **Security:** Tokens visible in workflow JSON (less secure)

---

## 💡 IDEATE (Layer 2: Application)

### **Option A Analysis:**

**Pros:**
- ✅ Most secure (tokens not in code)
- ✅ Standard practice (how n8n is designed to work)
- ✅ Persistent across restarts
- ✅ Can be updated without modifying workflows
- ✅ Works with existing workflow code (uses `$env.VARIABLE`)

**Cons:**
- ⚠️ Requires SSH access to Pi
- ⚠️ Requires Pi system access
- ⚠️ Need to know how n8n is installed (systemd, docker, npm)

**Feasibility:** HIGH (if Pi access available)

---

### **Option B Analysis:**

**Pros:**
- ✅ No Pi access needed
- ✅ Quick to implement
- ✅ Can be done immediately
- ✅ Works if Pi access is blocked

**Cons:**
- ❌ Less secure (values in workflow JSON)
- ❌ Need to modify workflow code
- ❌ Harder to update (must edit workflow)
- ❌ Values visible in workflow export
- ❌ Not standard practice

**Feasibility:** HIGH (but not ideal)

---

## 🎯 MODEL (Layer 3: Integration)

### **Decision Matrix:**

| Criteria | Option A (System) | Option B (Hardcode) | Winner |
|----------|------------------|---------------------|--------|
| Security | ✅ High | ❌ Low | A |
| Best Practice | ✅ Yes | ❌ No | A |
| Maintainability | ✅ Easy | ❌ Hard | A |
| Implementation Speed | ⚠️ Medium | ✅ Fast | B |
| Long-term | ✅ Better | ❌ Worse | A |

### **Recommendation: Option A (System-Level)**

**Why:**
1. **Security:** Tokens not in code (better security)
2. **Best Practice:** How n8n is designed to work
3. **Maintainability:** Easy to update without touching workflows
4. **Future-proof:** Works with all workflows automatically

**Fallback:** If Pi access unavailable, use Option B

---

## ⚡ OPTIMIZE (Layer 4: Mastery)

### **Optimal Implementation Plan:**

1. **Check Pi Access:**
   - Test SSH connection
   - Identify n8n installation method
   - Determine service file location

2. **Set Variables:**
   - Add to systemd service (if systemd)
   - Or add to .env file (if npm/docker)
   - Use secure method

3. **Verify:**
   - Restart n8n service
   - Test workflow execution
   - Confirm variables accessible

4. **Document:**
   - Record method used
   - Document variable locations
   - Create update procedure

---

## 🚀 DEPLOY (Layer 5: Execution)

### **Implementation Steps:**

**Step 1: Detect n8n Installation Method**
- Check if systemd service exists
- Check if docker container
- Check if npm/pm2

**Step 2: Set Variables (Based on Method)**
- Systemd: Edit `/etc/systemd/system/n8n.service`
- Docker: Edit docker-compose.yml or add env vars
- npm/pm2: Edit `.env` file or pm2 config

**Step 3: Apply Changes**
- Reload systemd daemon (if systemd)
- Restart n8n service
- Verify variables accessible

**Step 4: Test**
- Run verification script
- Test workflow execution
- Confirm success

---

## ✅ FINAL RECOMMENDATION

**Best Solution: Option A (System-Level Environment Variables)**

**Implementation:**
- Use robot script to:
  1. Detect n8n installation method
  2. Set variables appropriately
  3. Restart n8n
  4. Verify success

**If Option A fails:**
- Fallback to Option B (hardcode in workflow)

---

**Next: Create robot script to implement Option A** 🤖

