# 🧪 How to Test Screenshot-to-Fix Webhook

**Date:** December 17, 2025  
**Webhook:** `/webhook/screenshot-fix`

---

## ✅ Quick Test (Terminal)

### Option 1: Use the Test Script

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
bash TEST-SCREENSHOT-FIX-WEBHOOK.sh
```

**With your own image:**
```bash
bash TEST-SCREENSHOT-FIX-WEBHOOK.sh 'https://your-image-url.com/image.png' 'Error description'
```

### Option 2: Use curl Directly

```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://via.placeholder.com/800x600.png", "context": "Test"}'
```

**With your own image:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://your-actual-screenshot-url.com/image.png", "context": "Error description"}'
```

---

## ⚠️ Important Notes

### 1. Use Real Image URLs

**❌ Don't use:**
- `https://example.com/test.png` (not a real image)
- Placeholder URLs that don't exist

**✅ Use:**
- `https://via.placeholder.com/800x600.png` (real placeholder service)
- `https://picsum.photos/800/600` (random images)
- Your actual screenshot URLs

### 2. Image Requirements

- Must be publicly accessible (no authentication)
- Must be a valid image format (PNG, JPG, etc.)
- Must be downloadable by OpenAI's servers

### 3. Check Results

After triggering the webhook:

1. **Open n8n:** `http://192.168.1.226:5678`
2. **Click:** "Executions" tab
3. **Find:** Most recent execution
4. **Check:** Status (Success ✅ or Error ❌)
5. **If Error:** Click on it to see error details

---

## 📋 Example Payloads

### Test with Placeholder Image
```json
{
  "screenshotUrl": "https://via.placeholder.com/800x600.png",
  "context": "Testing workflow with placeholder image"
}
```

### Test with Random Image
```json
{
  "screenshotUrl": "https://picsum.photos/800/600",
  "context": "Testing with random image"
}
```

### Production Use
```json
{
  "screenshotUrl": "https://your-actual-screenshot-url.com/image.png",
  "context": "Error: Unity build failed on line 42"
}
```

---

## 🔧 Troubleshooting

### Error: `invalid_image_url`

**Cause:** Image URL is not accessible or not a real image

**Fix:**
- Use a real, publicly accessible image URL
- Test the URL in a browser first
- Ensure the image is downloadable

### Error: `Credential not found`

**Cause:** OpenAI credential not set

**Fix:**
- Go to n8n Credentials
- Add OpenAI API credential
- Assign to "Message a model" node

### Error: `Model not found`

**Cause:** GPT-5.2-PRO not available

**Fix:**
- Change model to GPT-4 or GPT-4-turbo
- Update "Message a model" node

---

## ✅ Success Indicators

**When the workflow succeeds:**
- ✅ Webhook returns 200 OK
- ✅ Execution shows "Success" in n8n
- ✅ "Message a model" node is GREEN
- ✅ Response contains fix suggestions

**Check Executions tab to confirm!**

---

**The workflow is ready - just use real image URLs!** 🚀

