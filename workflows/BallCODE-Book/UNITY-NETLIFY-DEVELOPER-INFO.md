# Information Needed from Developer: Unity & Netlify App

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Clear checklist of what information you need from your developer to work with the Unity game and Netlify website deployment.

---

## 🎮 UNITY PROJECT INFORMATION

### **Critical Information Needed:**

#### 1. **Unity Project Location & Access**
- [ ] **Where is the Unity project stored?**
  - Local file path? (e.g., `/Users/rashadwest/UnityProjects/BallCODE`)
  - Git repository? (What's the URL?)
  - Cloud storage? (Google Drive, Dropbox, etc.)
- [ ] **How can I access it?**
  - Direct file access (if local)
  - Git repository access (preferred)
  - Cloud storage access
  - Shared folder

#### 2. **Unity Version & Configuration**
- [ ] **What Unity version is the project using?**
  - Version number (e.g., 2021.3.15f1, 2022.1.0f1)
  - Where to check: Unity Editor → Help → About Unity
- [ ] **What build target is configured?**
  - WebGL (for website integration)
  - Standalone (for desktop)
  - Mobile (iOS/Android)
- [ ] **Any special build settings?**
  - Compression settings
  - Memory settings
  - Player settings

#### 3. **Unity WebGL Build Information**
- [ ] **Has a WebGL build been created?**
  - If yes: Where are the build files located?
  - If no: Can the developer create one?
- [ ] **WebGL Build Settings:**
  - Build output folder location
  - Compression format (Gzip, Brotli, etc.)
  - Template used (if custom)
  - Data URL or separate files?
- [ ] **Build Instructions:**
  - Step-by-step process to create WebGL build
  - Any special configurations needed
  - Estimated build time

#### 4. **Unity Project Structure**
- [ ] **Key folders/files:**
  - Where are scripts located? (`Assets/Scripts/`)
  - Where are scenes located? (`Assets/Scenes/`)
  - Where are assets located? (`Assets/`)
- [ ] **Important scripts to know about:**
  - Game manager scripts
  - Story mode scripts
  - URL parameter handling (if exists)
- [ ] **Dependencies:**
  - Required Unity packages
  - External plugins/assets
  - Version requirements

---

## 🌐 NETLIFY DEPLOYMENT INFORMATION

### **Critical Information Needed:**

#### 1. **Netlify Account & Access**
- [ ] **Netlify Account Details:**
  - Account email/username
  - Site name (e.g., `ballcode` or `ballcode.netlify.app`)
  - Site URL (e.g., `https://ballcode.netlify.app`)
- [ ] **Access Method:**
  - Netlify access token (preferred - more secure)
  - OR: Login credentials (if comfortable sharing)
  - How to create token: Netlify → User Settings → Applications → New access token

#### 2. **Netlify Site Configuration**
- [ ] **Current Build Settings:**
  - Build command (if any)
  - Publish directory (usually `/` for static sites)
  - Base directory (if site is in subfolder)
- [ ] **Deployment Settings:**
  - Which branch deploys? (usually `main` or `master`)
  - Auto-deploy enabled? (Yes/No)
  - Deploy previews enabled? (Yes/No)
- [ ] **Site Configuration File:**
  - Does `netlify.toml` exist?
  - What are the current settings?
  - Any redirect rules configured?

#### 3. **GitHub Integration**
- [ ] **Repository Connection:**
  - Which GitHub repository is connected? (e.g., `JuddCMelvin/BallCode`)
  - Is it connected via GitHub integration?
  - Branch that triggers deployment?
- [ ] **Deployment Workflow:**
  - How are changes deployed? (Auto on push, manual, etc.)
  - Build logs location
  - How to trigger manual deploy

#### 4. **Domain Configuration**
- [ ] **Custom Domain:**
  - Is `ballcode.co` connected to Netlify?
  - DNS settings (where managed - Netlify or external?)
  - SSL certificate status
- [ ] **Subdomains:**
  - Any subdomains configured? (e.g., `play.ballcode.co`)
  - Where are they pointing?

---

## 🔗 UNITY + NETLIFY INTEGRATION

### **Information Needed for Integration:**

#### 1. **WebGL Build Deployment**
- [ ] **Where should Unity WebGL build be deployed?**
  - Subfolder? (e.g., `/game/` or `/play/`)
  - Subdomain? (e.g., `play.ballcode.co`)
  - Same domain? (e.g., `ballcode.co/game`)
- [ ] **File Structure:**
  - How should build files be organized?
  - Where should `index.html` be located?
  - Asset folder structure?

#### 2. **URL Parameters & Communication**
- [ ] **Does Unity game accept URL parameters?**
  - Example: `ballcode.co/game?episode=1&mode=story`
  - How are parameters passed to Unity?
  - What parameters are supported?
- [ ] **Website → Game Communication:**
  - How does website launch the game?
  - JavaScript integration needed?
  - PostMessage API usage?

#### 3. **Asset Loading**
- [ ] **How are assets loaded?**
  - All assets in build folder?
  - External CDN?
  - Streaming assets?
- [ ] **File Size Considerations:**
  - Total build size?
  - Any large files that need special handling?
  - Compression strategy?

---

## 📋 QUICK CHECKLIST FOR DEVELOPER

### **Send This to Your Developer:**

**UNITY:**
- [ ] Unity project location (path or repository)
- [ ] Unity version number
- [ ] WebGL build location (if exists) OR instructions to create one
- [ ] Build settings and configuration
- [ ] Project structure overview

**NETLIFY:**
- [ ] Netlify site name and URL
- [ ] Netlify access token OR login credentials
- [ ] Current build/deploy settings
- [ ] GitHub repository connection
- [ ] Domain configuration (if custom domain)

**INTEGRATION:**
- [ ] Where Unity game should be deployed (path/subdomain)
- [ ] URL parameter handling (if any)
- [ ] Website → game communication method

---

## 💬 MESSAGE TEMPLATE FOR DEVELOPER

**Copy and send this to your developer:**

---

Hi [Developer Name],

I need some information about our Unity game and Netlify deployment setup to help with integration and updates. Can you provide:

**UNITY PROJECT:**
1. Where is the Unity project located? (file path, Git repo, or cloud storage)
2. What Unity version are we using?
3. Do we have a WebGL build? If yes, where is it? If no, can you create one?
4. What are the WebGL build settings?

**NETLIFY:**
1. What's our Netlify site name/URL?
2. Can you create a Netlify access token? (Netlify → User Settings → Applications → New access token)
3. What are the current build/deploy settings?
4. Which GitHub repository is connected?

**INTEGRATION:**
1. Where should the Unity WebGL game be deployed? (subfolder like `/game/` or subdomain?)
2. Does the Unity game handle URL parameters? (e.g., `?episode=1`)

This will help me provide the right code and instructions for website-game integration.

Thanks!

---

## 🎯 PRIORITY ORDER

### **HIGH PRIORITY** (Need First):
1. ✅ Unity project location/access
2. ✅ Unity version
3. ✅ Netlify site name and access
4. ✅ WebGL build location or ability to create one

### **MEDIUM PRIORITY** (Nice to Have):
5. ⚠️ Detailed build settings
6. ⚠️ Integration details (URL parameters, etc.)
7. ⚠️ Domain configuration

### **LOW PRIORITY** (Can Wait):
8. ⚠️ Advanced deployment configurations
9. ⚠️ Performance optimization settings

---

## 📝 WHAT YOU'LL DO WITH THIS INFO

Once you have this information:

1. **Share with me (AI assistant):**
   - I'll use it to provide correct code
   - I'll create integration instructions
   - I'll help with deployment setup

2. **I'll provide:**
   - Unity WebGL build instructions (if needed)
   - Netlify deployment configuration
   - Integration code (website → game)
   - Testing checklist

3. **Developer can then:**
   - Implement the integration
   - Deploy the game
   - Test the full flow

---

## 🔒 SECURITY NOTES

**For Developer:**
- Use access tokens instead of passwords when possible
- Tokens can be revoked later if needed
- Only share what's necessary for the task
- Test credentials are fine for development

**What I'll Do:**
- ✅ Use info to provide correct code/instructions
- ✅ Help with deployment configuration
- ✅ Troubleshoot integration issues
- ❌ Will NOT: Access systems directly without permission
- ❌ Will NOT: Make changes without approval

---

## 🚀 NEXT STEPS

1. **You → Developer:** Send the message template above
2. **Developer → You:** Provides the information
3. **You → Me:** Share the developer's responses
4. **Me → You:** Provide code, instructions, and configuration
5. **You → Developer:** Share code/instructions for implementation

---

**Ready to get started? Send the message template to your developer!**


