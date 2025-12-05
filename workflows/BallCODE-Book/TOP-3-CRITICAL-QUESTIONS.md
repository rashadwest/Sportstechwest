# Top 3 Critical Questions: Netlify & Unity Development

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** The 3 essential questions you need answered to continue development with Netlify and Unity integration.

---

## 🎯 QUESTION 1: Unity Project Access

**What you need to know:**
- **Where is the Unity project located?**
  - Local file path? (e.g., `/Users/rashadwest/UnityProjects/BallCODE`)
  - Git repository URL?
  - Cloud storage location?
- **How can you access it?**
  - Direct file access?
  - Git repository access?
  - Shared folder/cloud access?

**Why this matters:**
- Can't modify Unity scripts without project access
- Can't create WebGL builds without project
- Can't test integration without project

**Action:** Get Unity project location and access method from your developer.

---

## 🌐 QUESTION 2: Netlify Account Access

**What you need to know:**
- **Netlify site name/URL:**
  - Site name (e.g., `ballcode` or `ballcode.netlify.app`)
  - Site URL (e.g., `https://ballcode.netlify.app`)
- **Access method:**
  - Netlify access token (preferred)
    - How to create: Netlify → User Settings → Applications → New access token
  - OR: Login credentials (if comfortable sharing)

**Why this matters:**
- Can't deploy changes without access
- Can't view deployment status
- Can't configure build settings
- Can't upload Unity WebGL build files

**Action:** Get Netlify access token or login credentials.

---

## 🎮 QUESTION 3: Unity WebGL Build Capability

**What you need to know:**
- **Can you create a Unity WebGL build?**
  - If yes: What Unity version? (e.g., 2021.3.15f1)
  - If no: Can your developer create one?
- **Where should the WebGL build be deployed on Netlify?**
  - Subfolder? (e.g., `/game/` or `/play/`)
  - Subdomain? (e.g., `play.ballcode.co`)
  - Root path? (e.g., `ballcode.co/game`)

**Why this matters:**
- Determines deployment structure
- Affects how website integrates with game
- Determines URL routing and file organization
- Needed to test end-to-end flow

**Action:** Confirm Unity version, WebGL build capability, and preferred deployment location.

---

## 📋 QUICK CHECKLIST

**Send these 3 questions to your developer:**

1. **Unity Project:** Where is it located and how can I access it?
2. **Netlify Access:** What's the site name/URL and can you create an access token?
3. **WebGL Build:** Can you create a Unity WebGL build? What Unity version? Where should it be deployed?

---

## 🚀 ONCE YOU HAVE ANSWERS

**Share the answers with me and I'll:**
- ✅ Provide Unity WebGL build instructions (if needed)
- ✅ Configure Netlify deployment settings
- ✅ Create integration code (website → game)
- ✅ Set up file structure for deployment
- ✅ Provide testing checklist

---

**These 3 questions unlock everything else. Get these answered first!**


