# 🧪 Test Webhook with curl - Correct Syntax

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** `curl: (26) Failed to open/read local data from file/application`  
**Fix:** Correct file path and curl syntax

---

## ✅ CORRECT CURL COMMAND

### **Option 1: With Image File**

```bash
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -F "screenshot=@/path/to/your/error-screenshot.png" \
  -F "context=Unity build failed with error message"
```

**Important:**
- Use `@` before file path (not `@file`)
- Use **absolute path** or **relative path from current directory**
- File must exist and be readable

### **Option 2: With Image URL**

```bash
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://picsum.photos/800/600",
    "context": "Test error screenshot"
  }'
```

**No file needed** - uses URL instead

### **Option 3: Test with Existing Image**

**Find an image file:**
```bash
# List image files in current directory
ls -la *.png *.jpg *.jpeg 2>/dev/null

# Or use a test image
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -F "screenshot=@./test-image.png" \
  -F "context=Test error"
```

---

## 🔍 TROUBLESHOOTING

### **Error: "Failed to open/read local data"**

**Causes:**
1. File doesn't exist at that path
2. File path is wrong
3. No read permissions
4. Missing `@` symbol

**Fix:**
```bash
# Check if file exists
ls -la /path/to/your/file.png

# Use absolute path
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -F "screenshot=@$(pwd)/error-screenshot.png" \
  -F "context=Test"

# Or use relative path from current directory
cd /path/to/images
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -F "screenshot=@error-screenshot.png" \
  -F "context=Test"
```

---

## ✅ QUICK TEST (No File Needed)

**Test with URL instead:**

```bash
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://picsum.photos/800/600",
    "context": "Testing workflow with placeholder image"
  }'
```

**This works immediately** - no file needed!

---

## 🎯 FIND YOUR N8N WEBHOOK URL

**If using local n8n:**
```bash
# Default local URL
http://localhost:5678/webhook/screenshot-fix
```

**If using n8n cloud or custom domain:**
```bash
# Replace with your actual URL
https://your-n8n-instance.com/webhook/screenshot-fix
```

**Check your workflow:**
- Open n8n workflow
- Click on "Screenshot Upload Webhook" node
- Copy the webhook URL shown

---

## 📋 COMPLETE TEST SCRIPT

**Create a test script:**

```bash
#!/bin/bash

# Set your webhook URL
WEBHOOK_URL="http://localhost:5678/webhook/screenshot-fix"

# Option 1: Test with URL (easiest)
echo "Testing with image URL..."
curl -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://picsum.photos/800/600",
    "context": "Test error screenshot",
    "source": "manual_test"
  }'

echo -e "\n\n"

# Option 2: Test with file (if file exists)
if [ -f "error-screenshot.png" ]; then
  echo "Testing with local file..."
  curl -X POST "$WEBHOOK_URL" \
    -F "screenshot=@error-screenshot.png" \
    -F "context=Test error from file" \
    -F "source=file_upload"
else
  echo "No error-screenshot.png found, skipping file test"
fi
```

**Save as `test-webhook.sh` and run:**
```bash
chmod +x test-webhook.sh
./test-webhook.sh
```

---

## ✅ SIMPLEST TEST (Copy-Paste Ready)

**Just run this:**

```bash
curl -X POST http://localhost:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl":"https://picsum.photos/800/600","context":"Test error"}'
```

**No file needed!** This will work immediately.

---

**Status:** ✅ Test Commands Ready  
**Action:** Use URL method (easiest) or fix file path


