# Netlify Account Setup & Code Transfer Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Complete step-by-step guide to create Netlify account and transfer code from developer's account

---

## 🎯 What You're Setting Up

**Netlify** = Website hosting service (where your game/website will live)  
**WebGL** = Technology Unity uses to build web games (NOT a service - it's built into Unity)

**Goal:** Get your own Netlify account so you can control your code instead of it being under someone else's name.

---

## 📋 STEP 1: Create Netlify Account

### Option A: Sign Up with Email (Recommended)

1. **Go to Netlify:** https://app.netlify.com/signup
2. **Choose "Sign up with email"**
3. **Enter your information:**
   - Email: [Your email address]
   - Password: [Create a strong password]
   - Full name: Rashad West
4. **Click "Sign up"**
5. **Check your email** for verification link
6. **Click verification link** in email
7. **You're in!** You'll see the Netlify dashboard

### Option B: Sign Up with GitHub (If you have GitHub account)

1. **Go to Netlify:** https://app.netlify.com/signup
2. **Click "Sign up with GitHub"**
3. **Authorize Netlify** to access your GitHub
4. **You're in!** Netlify will automatically connect to your GitHub

---

## 📋 STEP 2: Understand Your Netlify Dashboard

Once logged in, you'll see:

- **Sites** - List of all your websites/apps
- **Add new site** - Button to deploy new projects
- **Team** - If you're working with others
- **Settings** - Your account settings

---

## 📋 STEP 3: Get Information from Developer

Before transferring code, you need these details from your developer:

### Information Checklist:

**NETLIFY SITE INFO:**
- [ ] Current Netlify site name (e.g., `ballcode` or `ballcode-game`)
- [ ] Current Netlify URL (e.g., `https://ballcode.netlify.app`)
- [ ] Which GitHub repository is connected? (e.g., `JuddCMelvin/BallCode`)

**CODE ACCESS:**
- [ ] GitHub repository URL
- [ ] Do you have access to the GitHub repo? (If not, ask developer to add you as collaborator)
- [ ] OR: Can developer give you the code files directly?

**UNITY PROJECT:**
- [ ] Where is the Unity project? (file path or repository)
- [ ] Has a WebGL build been created? Where is it?

---

## 📋 STEP 4: Transfer Code to Your Account

### Method 1: Transfer via GitHub (Recommended - Best for ongoing work)

**If the code is in GitHub:**

1. **Get GitHub Access:**
   - Ask developer to add you as collaborator to the repository
   - OR: Fork the repository to your GitHub account
   - OR: Get the repository URL and clone it locally

2. **Connect to Your Netlify:**
   - In Netlify dashboard, click **"Add new site"**
   - Choose **"Import an existing project"**
   - Click **"Deploy with GitHub"**
   - Authorize Netlify to access your GitHub
   - Select the repository (e.g., `JuddCMelvin/BallCode` or your fork)
   - Click **"Connect"**

3. **Configure Build Settings:**
   - **Build command:** (Leave empty if it's a static site, or ask developer what command to use)
   - **Publish directory:** (Usually `/` for static sites, or ask developer)
   - Click **"Deploy site"**

4. **Your site is now on YOUR Netlify account!**

### Method 2: Manual Transfer (If no GitHub access)

**If you need to transfer files manually:**

1. **Get the code from developer:**
   - Ask developer to zip the project files
   - Download the zip file
   - Extract it to a folder on your computer

2. **Deploy to Your Netlify:**
   - In Netlify dashboard, click **"Add new site"**
   - Choose **"Deploy manually"**
   - Drag and drop the project folder (or zip file)
   - Netlify will upload and deploy

3. **Your site is now on YOUR Netlify account!**

### Method 3: Transfer Existing Site (If developer gives you access)

**If developer can transfer the site directly:**

1. **Ask developer to:**
   - Go to their Netlify dashboard
   - Site Settings → General → Transfer site ownership
   - Enter your Netlify email address
   - Confirm transfer

2. **You'll receive an email:**
   - Click "Accept transfer"
   - Site is now in your account!

---

## 📋 STEP 5: Update Domain (If Using Custom Domain)

**If you're using `ballcode.co` or another custom domain:**

1. **In Netlify Dashboard:**
   - Go to your site
   - Site Settings → Domain Management
   - Add custom domain: `ballcode.co`
   - Follow DNS instructions

2. **Update DNS Records:**
   - Netlify will give you DNS records to add
   - Add them to your domain registrar (where you bought the domain)
   - Wait for DNS to propagate (usually 5-30 minutes)

---

## 📋 STEP 6: Instructions to Give Developer

**Copy and send this to your developer:**

---

Hi [Developer Name],

I've created my own Netlify account and need to transfer the BallCODE project to my account. Can you help with one of these options?

**OPTION 1 (Preferred):** Transfer the site ownership
- Go to Netlify dashboard → Site Settings → General → Transfer site ownership
- Enter my email: [Your email address]
- I'll accept the transfer

**OPTION 2:** Add me to GitHub repository
- Add me as collaborator to the GitHub repo: [Repository name]
- My GitHub username: [Your GitHub username]
- I'll connect it to my Netlify account

**OPTION 3:** Give me the code files
- Zip the project files
- Send me the zip file or share via Google Drive/Dropbox
- I'll deploy it to my Netlify account

**Also need:**
- Current Netlify site name/URL
- Build settings (build command, publish directory)
- Any environment variables or configuration needed

Thanks!

---

## 📋 STEP 7: Verify Everything Works

After transfer, test:

1. **Site loads:** Visit your Netlify URL (e.g., `https://ballcode.netlify.app`)
2. **Deployments work:** Make a small change, push to GitHub, verify it deploys
3. **Domain works:** If using custom domain, verify it loads correctly
4. **Game loads:** If Unity WebGL game is deployed, test that it loads

---

## 🎮 About WebGL (Clarification)

**WebGL is NOT a service you sign up for.**

**WebGL** = A technology that Unity uses to build games that run in web browsers. It's built into Unity - you don't need a separate account.

**What you DO need:**
- ✅ **Netlify account** (to host the WebGL game)
- ✅ **Unity** (to build the WebGL game)
- ✅ **GitHub** (optional, but recommended for code management)

**The flow:**
1. Build game in Unity → Export as WebGL
2. Deploy WebGL build to Netlify
3. Game runs in browsers via WebGL technology

---

## 📋 Quick Reference: Netlify Commands

**If you install Netlify CLI (optional):**

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to your account
netlify login

# Deploy a site
netlify deploy --prod

# View your sites
netlify sites:list
```

**You don't need CLI for basic use** - the web dashboard works great!

---

## 🚨 Common Issues & Solutions

### Issue: "Site already exists"
**Solution:** The site name is taken. Choose a different name or use a custom domain.

### Issue: "Build failed"
**Solution:** Check build settings. Ask developer what build command/publish directory to use.

### Issue: "Can't access repository"
**Solution:** Ask developer to add you as collaborator on GitHub, or use manual deployment.

### Issue: "Domain not working"
**Solution:** Check DNS settings. Netlify will show you what records to add.

---

## ✅ Checklist: What You'll Have After Setup

- [ ] Netlify account created
- [ ] Logged into Netlify dashboard
- [ ] Code transferred to your account (or transfer in progress)
- [ ] Site deployed and accessible
- [ ] Custom domain configured (if applicable)
- [ ] Developer has instructions for transfer

---

## 🎯 Next Steps After Account Setup

1. **Test the site** - Make sure everything works
2. **Update book links** - If books link to game, update URLs if needed
3. **Set up auto-deploy** - Connect GitHub for automatic deployments
4. **Configure environment variables** - If needed for API keys, etc.
5. **Set up custom domain** - If using `ballcode.co` or similar

---

## 📞 Need Help?

**Netlify Support:**
- Documentation: https://docs.netlify.com
- Community: https://answers.netlify.com
- Support: https://www.netlify.com/support

**For Unity WebGL:**
- See `WEBGL-NETLIFY-DEPLOYMENT-GUIDE.md` for detailed deployment instructions

---

**Status:** Ready to use  
**Last Updated:** January 2025


