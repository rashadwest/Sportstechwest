# 🔄 Restart n8n on Remote Raspberry Pi

**Status:** Environment variables set ✅  
**Next:** Restart n8n for changes to take effect  
**n8n URL:** http://192.168.1.226:5678

---

## 🚀 QUICK RESTART (Choose Your Method)

### Option 1: SSH and Restart (Recommended)

```bash
# SSH into Raspberry Pi
ssh pi@192.168.1.226

# Check if n8n is running as a service
sudo systemctl status n8n

# Restart n8n service
sudo systemctl restart n8n

# Verify it's running
sudo systemctl status n8n
```

### Option 2: If n8n is Running via PM2

```bash
# SSH into Raspberry Pi
ssh pi@192.168.1.226

# Restart n8n via PM2
pm2 restart n8n

# Or restart all PM2 processes
pm2 restart all
```

### Option 3: If n8n is Running via npm/npx

```bash
# SSH into Raspberry Pi
ssh pi@192.168.1.226

# Find n8n process
ps aux | grep n8n

# Kill the process (replace PID with actual process ID)
kill -9 <PID>

# Restart n8n (adjust command based on how you start it)
n8n start
# OR
npx n8n
```

### Option 4: If n8n is Running via Docker

```bash
# SSH into Raspberry Pi
ssh pi@192.168.1.226

# Restart n8n container
docker restart n8n

# Or if using docker-compose
cd /path/to/n8n
docker-compose restart
```

---

## ✅ VERIFY IT WORKED

**After restarting:**

1. **Check n8n is running:**
   ```bash
   curl http://192.168.1.226:5678/healthz
   ```
   Should return: `OK` or `{"status":"ok"}`

2. **Test in workflow:**
   - Go to n8n: http://192.168.1.226:5678
   - Execute "Get Git Variables" node
   - Should now show: `repoUrlSet: true, projectPathSet: true`

---

## 🐛 IF YOU DON'T KNOW HOW n8n IS RUNNING

**Find out how n8n is running:**

```bash
# SSH into Raspberry Pi
ssh pi@192.168.1.226

# Check if it's a systemd service
sudo systemctl status n8n

# Check if it's running via PM2
pm2 list

# Check if it's a Docker container
docker ps | grep n8n

# Check running processes
ps aux | grep n8n
```

**Then use the appropriate restart method above.**

---

## 📋 ENVIRONMENT VARIABLES SET

✅ `UNITY_REPO_URL` = `https://github.com/rashadwest/BallCode.git`  
✅ `UNITY_PROJECT_PATH` = `/Users/rashadwest/BTEBallCODE`  
✅ `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`

**After restart, these will be available in your workflow!**

---

**Status:** Variables set ✅  
**Action:** Restart n8n on Raspberry Pi  
**Then:** Test workflow again


