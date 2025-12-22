# BallCode Automation Commands Reference

**Purpose:** Quick reference for all BallCode build automation commands  
**Usage:** When user asks for commands, provide these with `--commands` flag

---

## 🚀 SETUP & AUTOMATION

### One-Time Setup
```bash
cd ~/Desktop
bash setup-automated-build.sh
```

### Manual Build (Run Anytime)
```bash
bash ~/Desktop/build-ballcode-background.sh
```

### Send Build Request (Direct curl)
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d @/Users/rashadwest/Desktop/build-request-ballcode-game.json
```

### Send Build Request (Background)
```bash
nohup curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d @/Users/rashadwest/Desktop/build-request-ballcode-game.json \
  > build-output.log 2>&1 &
```

---

## 📊 MONITORING & STATUS

### Check Recent Logs
```bash
ls -lt ~/Desktop/build-logs/ | head -5
```

### Watch Live Logs
```bash
tail -f ~/Desktop/build-logs/build-request-*.log
```

### View Latest Log
```bash
tail -20 ~/Desktop/build-logs/build-request-*.log | tail -20
```

### Check Automation Status
```bash
launchctl list | grep ballcode
```

### Check LaunchAgent Status
```bash
launchctl list com.rashadwest.ballcode-build
```

---

## ⚙️ AUTOMATION CONTROL

### Stop Automation
```bash
launchctl unload ~/Library/LaunchAgents/com.rashadwest.ballcode-build.plist
```

### Start Automation
```bash
launchctl load ~/Library/LaunchAgents/com.rashadwest.ballcode-build.plist
```

### Restart Automation
```bash
launchctl unload ~/Library/LaunchAgents/com.rashadwest.ballcode-build.plist && \
launchctl load ~/Library/LaunchAgents/com.rashadwest.ballcode-build.plist
```

---

## 🔧 TROUBLESHOOTING

### Test Network Connectivity
```bash
curl http://192.168.1.226:5678/webhook/unity-dev
```

### Check Build File Exists
```bash
ls -la ~/Desktop/build-request-ballcode-game.json
```

### Validate Build File JSON
```bash
python3 -m json.tool ~/Desktop/build-request-ballcode-game.json
```

### Remove Stale Lock File
```bash
rm ~/Desktop/.build-request.lock
```

### Check Script Permissions
```bash
ls -la ~/Desktop/build-ballcode-background.sh
chmod +x ~/Desktop/build-ballcode-background.sh
```

### Remove Quarantine (if needed)
```bash
xattr -d com.apple.quarantine ~/Desktop/build-ballcode-background.sh
xattr -d com.apple.quarantine ~/Desktop/setup-automated-build.sh
```

---

## 🌐 WORKFLOW & DEPLOYMENT

### View Workflow in Browser
```
http://192.168.1.226:5678/workflow/Kr8ZUpAiJl2nvf4E
```

### Game URL
```
https://ballcode-game.netlify.app
```

### Webhook URL
```
http://192.168.1.226:5678/webhook/unity-dev
```

---

## 📝 FILE LOCATIONS

### Scripts
- Main script: `~/Desktop/build-ballcode-background.sh`
- Setup script: `~/Desktop/setup-automated-build.sh`
- Build request: `~/Desktop/build-request-ballcode-game.json`

### Logs
- Log directory: `~/Desktop/build-logs/`
- LaunchAgent logs: `~/Desktop/build-logs/launchd-output.log`
- LaunchAgent errors: `~/Desktop/build-logs/launchd-error.log`

### Configuration
- LaunchAgent: `~/Library/LaunchAgents/com.rashadwest.ballcode-build.plist`
- Lock file: `~/Desktop/.build-request.lock`

---

## 🎯 QUICK REFERENCE

### Most Common Commands
```bash
# Run build now
bash ~/Desktop/build-ballcode-background.sh

# Check if it worked
tail -20 ~/Desktop/build-logs/build-request-*.log

# Check automation is running
launchctl list | grep ballcode
```

---

## ⚠️ IMPORTANT NOTES

1. **Always use `bash` command** - Don't use `./` on macOS
   - ✅ `bash script.sh`
   - ❌ `./script.sh` (may get "Operation not permitted")

2. **Use absolute paths** in curl commands
   - ✅ `/Users/rashadwest/Desktop/file.json`
   - ❌ `~/Desktop/file.json` (doesn't work in curl)

3. **Background execution** - Use `nohup` or `&` for background
   - `nohup command &` - runs in background, logs to nohup.out
   - `command &` - runs in background, output to terminal

---

**Last Updated:** December 11, 2025  
**Status:** Production Ready ✅

