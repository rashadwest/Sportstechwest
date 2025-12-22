# ⚡ Quick Test Command - Copy-Paste Ready

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** File path issue with curl  
**Solution:** Use URL method (no file needed)

---

## ✅ SIMPLEST TEST (No File Needed)

**For Pi n8n (Production):**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://picsum.photos/800/600","context":"Test error screenshot"}'
```

**For Local n8n (Testing):**
```bash
curl -X POST "http://localhost:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://picsum.photos/800/600","context":"Test error screenshot"}'
```

**One-liner (Pi):**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl":"https://picsum.photos/800/600","context":"Test error"}'
```

---

## ✅ WITH REAL ERROR SCREENSHOT URL

**If you have a real error screenshot hosted online:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://your-image-host.com/error.png","context":"Unity build failed with compilation error"}'
```

---

## ✅ WITH FILE UPLOAD (If File Exists)

**Only if you have a local file:**
```bash
# Check if file exists first
ls -la error-screenshot.png

# Then upload (use absolute path or be in same directory)
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -F "screenshot=@$(pwd)/error-screenshot.png" \
  -F "context=Test error from file"
```

**Common file path issues:**
- ❌ `@file` → Wrong (no file named "file")
- ❌ `@./file.png` → Wrong if file doesn't exist
- ✅ `@/full/path/to/file.png` → Correct (absolute path)
- ✅ `@error.png` → Correct (if in current directory)

---

## 🎯 RECOMMENDED: Use URL Method

**Why:**
- ✅ No file path issues
- ✅ Works immediately
- ✅ Can use any public image URL
- ✅ No file permissions needed

**Just copy-paste the first command above!**

---

**Status:** ✅ Ready to Test  
**Action:** Use URL method (easiest)

