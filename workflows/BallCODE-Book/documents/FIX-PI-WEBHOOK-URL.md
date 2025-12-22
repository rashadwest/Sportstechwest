# 🔧 Fix Pi n8n Webhook URL (localhost → Pi IP)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Issue:** n8n showing `localhost:5678` webhook URLs instead of `192.168.1.226:5678`  
**Solution:** Configure n8n environment variables on Pi

---

## 🎯 THE PROBLEM

Even though you're connected to Pi n8n at `http://192.168.1.226:5678`, the webhook URLs show:
- ❌ `http://localhost:5678/webhook-test/screenshot-fix`
- ✅ Should be: `http://192.168.1.226:5678/webhook-test/screenshot-fix`

---

## ✅ THE FIX

### Step 1: SSH into Raspberry Pi

```bash
ssh rw3hampton@192.168.1.226
```

### Step 2: Find n8n Installation Directory

```bash
# Check where n8n is running
ps aux | grep n8n

# Check common locations
ls -la ~/.n8n
ls -la ~/n8n
ls -la /opt/n8n
ls -la /usr/local/lib/node_modules/n8n
```

### Step 3: Find n8n Service/Process Configuration

**If using systemd:**
```bash
sudo systemctl status n8n
sudo systemctl cat n8n
```

**If using PM2:**
```bash
pm2 list
pm2 show n8n
pm2 env n8n
```

**If using Docker:**
```bash
docker ps | grep n8n
docker inspect <container-name>
```

### Step 4: Set Environment Variables

**For systemd service:**
```bash
# Create override directory
sudo mkdir -p /etc/systemd/system/n8n.service.d

# Create override file
sudo nano /etc/systemd/system/n8n.service.d/override.conf
```

**Add this content:**
```ini
[Service]
Environment="WEBHOOK_URL=http://192.168.1.226:5678/"
Environment="N8N_HOST=192.168.1.226"
Environment="N8N_PROTOCOL=http"
Environment="N8N_PORT=5678"
```

**Save and reload:**
```bash
sudo systemctl daemon-reload
sudo systemctl restart n8n
```

**For PM2:**
```bash
# Edit PM2 ecosystem file or use PM2 env
pm2 set N8N_HOST 192.168.1.226
pm2 set N8N_PROTOCOL http
pm2 set WEBHOOK_URL http://192.168.1.226:5678/
pm2 restart n8n
```

**For Docker:**
```bash
# Add to docker-compose.yml or docker run command:
-e WEBHOOK_URL=http://192.168.1.226:5678/
-e N8N_HOST=192.168.1.226
-e N8N_PROTOCOL=http
```

**For .env file (if n8n uses one):**
```bash
# Find .env file
find ~ -name ".env" -path "*n8n*" 2>/dev/null

# Edit .env file
nano ~/.n8n/.env  # or wherever it is
```

**Add these lines:**
```bash
WEBHOOK_URL=http://192.168.1.226:5678/
N8N_HOST=192.168.1.226
N8N_PROTOCOL=http
N8N_PORT=5678
```

### Step 5: Restart n8n

**systemd:**
```bash
sudo systemctl restart n8n
sudo systemctl status n8n
```

**PM2:**
```bash
pm2 restart n8n
pm2 logs n8n
```

**Docker:**
```bash
docker restart <container-name>
```

### Step 6: Verify

1. **Refresh n8n UI:** `http://192.168.1.226:5678`
2. **Open any workflow with webhook**
3. **Check webhook URL** - should now show `192.168.1.226:5678` instead of `localhost:5678`

---

## 🔍 QUICK DIAGNOSTIC

**Check current n8n environment:**
```bash
# SSH to Pi
ssh rw3hampton@192.168.1.226

# Check n8n process environment
ps aux | grep n8n | grep -v grep

# Check if environment variables are set
sudo systemctl show n8n | grep -i webhook
sudo systemctl show n8n | grep -i host
```

---

## 📝 ALTERNATIVE: Manual URL Override

If you can't change the environment variables, you can manually use the correct URL:

**Test URL:**
```
http://192.168.1.226:5678/webhook-test/screenshot-fix
```

**Production URL:**
```
http://192.168.1.226:5678/webhook/screenshot-fix
```

The webhook will work even if n8n shows `localhost` - just use the Pi IP in your requests.

---

## ✅ SUCCESS CRITERIA

After fixing:
- ✅ Webhook URLs show `192.168.1.226:5678` instead of `localhost:5678`
- ✅ All webhook requests use Pi IP
- ✅ Workflows execute on Pi instance

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** 🔧 Configuration Fix Guide


