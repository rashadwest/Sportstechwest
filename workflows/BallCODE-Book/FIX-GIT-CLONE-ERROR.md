# Fix Git Clone Error

**Error:** `zsh: parse error near '\n'`

**Cause:** You have angle brackets around the URL: `<https://github.com/rashadwest/BTEBallCODE>`

---

## ✅ CORRECT COMMAND

```bash
git clone https://github.com/rashadwest/BTEBallCODE
```

**Remove the angle brackets!** The URL should be plain text.

---

## 📍 WHERE TO CLONE

**Recommended location:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows
git clone https://github.com/rashadwest/BTEBallCODE
```

**This will create:**
```
/Users/rashadwest/Sportstechwest/workflows/BTEBallCODE/
```

---

## 🔍 GET NETLIFY SITE ID (After Cloning)

**You don't need to clone to get Netlify Site ID!**

**Easier method:**
1. Go to: https://app.netlify.com
2. Select your site (ballcode-game or similar)
3. Go to: **Site settings** → **General**
4. Find **"Site ID"** (looks like: `abc123-def456-ghi789`)
5. Copy it

**That's it!** No git clone needed for Site ID.

---

## 🎯 WHY CLONE THE REPO?

**You only need to clone if:**
- Garvis needs to read Unity files locally
- You want to make code changes locally
- You want to test builds locally

**For just getting Site ID:** Use Netlify dashboard (no clone needed).

---

**Fix the git command and you're good!** ✅

