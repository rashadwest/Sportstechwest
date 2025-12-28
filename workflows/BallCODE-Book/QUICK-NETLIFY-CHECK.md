# Quick Netlify Access Check

**Date:** December 18, 2025  
**Quick Reference:** How to check Netlify access

---

## 🚀 QUICK COMMAND

**From the BallCODE-Book directory:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
export NETLIFY_TOKEN='your-token-here'
./check-netlify-access.sh
```

---

## 📋 STEP-BY-STEP

1. **Navigate to correct directory:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   ```

2. **Get your Netlify token:**
   - Go to: https://app.netlify.com/user/applications
   - Create or copy your access token

3. **Set token and run:**
   ```bash
   export NETLIFY_TOKEN='your-token-here'
   ./check-netlify-access.sh
   ```

---

## 🔍 ALTERNATIVE: Manual API Check

**If script doesn't work, use curl directly:**

```bash
curl -H "Authorization: Bearer YOUR_NETLIFY_TOKEN" \
  https://api.netlify.com/api/v1/sites
```

**Replace `YOUR_NETLIFY_TOKEN` with your actual token.**

---

## 📍 CURRENT DIRECTORY

**You're in:** `BTEBallCODE`  
**Script is in:** `BallCODE-Book`

**Navigate to script location:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

---

**Navigate to BallCODE-Book directory first!** ✅


