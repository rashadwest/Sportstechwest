# How to Deploy Changes to Your Live Website
## Getting Your Changes from Local Files to ballcode.co

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Important:** I've been editing files in your local workspace. These changes need to be pushed to GitHub and deployed to appear on your live site.

---

## 🔍 What I've Changed

**Files Modified:**
1. `BallCode/index.html` - Added Books section between FAQ and Contact
2. `BallCode/css/style.css` - Added Books section styling (blue/orange theme)

**What Was Added:**
- Books section with Book 1 (Gumroad link) and Book 2 (Coming Soon)
- Styling that matches your blue/orange template
- Responsive design for mobile

---

## 🚀 How to Deploy (3 Steps)

### Step 1: Check Your Git Status
**In Terminal, run:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
git status
```

This shows which files have been changed.

---

### Step 2: Commit and Push to GitHub

**Option A: If you have a Git repository set up:**
```bash
# Add the changed files
git add BallCode/index.html BallCode/css/style.css

# Commit with a message
git commit -m "Add Books section between FAQ and Contact"

# Push to GitHub
git push
```

**Option B: If you don't have Git set up yet:**
- You'll need to create a GitHub repository first
- Or upload files directly to your hosting platform

---

### Step 3: Deploy to Your Live Site

**This depends on where ballcode.co is hosted:**

#### If Hosted on Netlify:
- If connected to GitHub: Changes auto-deploy when you push
- If manual upload: Go to Netlify dashboard → Deploy → Upload files

#### If Hosted on GitHub Pages:
- Push to GitHub → Changes appear automatically (if Pages is enabled)

#### If Hosted on Vercel:
- If connected to GitHub: Changes auto-deploy when you push
- If manual: Upload via Vercel dashboard

#### If Hosted on Custom Server:
- Upload files via FTP or your hosting control panel

---

## ❓ Questions to Answer

**To help you deploy, I need to know:**

1. **Do you have a GitHub repository for the website?**
   - If yes: What's the repository URL?
   - If no: Do you want me to help set one up?

2. **Where is ballcode.co currently hosted?**
   - Netlify? (I see references to ballcode.netlify.app)
   - GitHub Pages?
   - Vercel?
   - Custom server?
   - Other?

3. **How do you currently update the website?**
   - Git push?
   - FTP upload?
   - WordPress admin?
   - Other method?

---

## 🎯 Quick Check: Is Your Site on Netlify?

I see references to `ballcode.netlify.app` in your code. If your site is on Netlify:

1. **Check if Netlify is connected to GitHub:**
   - Go to Netlify dashboard
   - Check if your site is connected to a Git repository
   - If yes: Just push to GitHub and it auto-deploys
   - If no: You can upload files manually or connect it

2. **Manual Upload to Netlify:**
   - Go to Netlify dashboard
   - Click "Deploy" → "Deploy manually"
   - Drag and drop your `BallCode` folder
   - Netlify will deploy it

---

## 📋 What Files Need to Be Deployed

**Files I've Modified:**
- `BallCode/index.html` (added Books section)
- `BallCode/css/style.css` (added Books styling)

**Files You Need to Add:**
- `BallCode/assets/images/book1-title-page.jpg` (your Book 1 thumbnail image)

---

## ✅ Quick Test Before Deploying

**Before deploying, test locally:**
1. Open `BallCode/index.html` in your browser
2. Check that the Books section appears between FAQ and Contact
3. Verify the styling looks good
4. Check that the Gumroad link works

---

## 🆘 If You Need Help

**Tell me:**
1. Where is ballcode.co hosted? (Netlify, GitHub Pages, etc.)
2. Do you have a GitHub repository?
3. How do you currently update the site?

**Then I can give you exact step-by-step instructions for your setup!**

---

**Status:** Changes are ready locally, waiting for deployment  
**Next Action:** Determine your hosting/deployment method, then push/deploy


