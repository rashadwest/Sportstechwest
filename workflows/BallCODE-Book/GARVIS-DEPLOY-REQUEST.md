# Garvis Deployment Request

**ONE Thing:** Deploy all website and game updates to Netlify seamlessly via Garvis automation

**Tasks:**
1. Deploy Website to Netlify - Push website changes to GitHub (rashadwest/BallCode), Trigger Netlify deployment via API, Verify website deployment status, Report completion
2. Deploy Game Updates - Push Book 1, 2, 3 levels to Unity repository (rashadwest/BTEBallCODE), Trigger Unity build via GitHub Actions, Monitor build and Netlify deployment, Verify game deployment status, Report completion
3. Verify Both Deployments - Check website is live with updates, Check game is live with new levels, Generate deployment report, Notify on completion

---

## 🔧 GARVIS EXECUTION PLAN

### **Phase 1: Website Deployment**

**System:** Website (rashadwest/BallCode)  
**Method:** GitHub Push → Netlify API Trigger

**Steps:**
1. Verify website changes are committed
2. Push to GitHub: `rashadwest/BallCode` (main branch)
3. Trigger Netlify deployment via API:
   - Endpoint: `https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys`
   - Method: POST
   - Headers: Authorization Bearer token
   - Body: `{"branch": "main"}`
4. Monitor deployment status
5. Report completion

---

### **Phase 2: Game Deployment**

**System:** Game (rashadwest/BTEBallCODE)  
**Method:** GitHub Push → Unity Build Orchestrator → GitHub Actions → Netlify

**Steps:**
1. Push Book 1, 2, 3 level files to Unity repository
2. Trigger Unity Build Orchestrator via n8n:
   - Webhook: `http://192.168.1.226:5678/webhook/unity-build`
   - Method: POST
   - Body: `{"request": "Build with Book 1, 2, 3 levels", "branch": "main"}`
3. Monitor GitHub Actions build
4. Monitor Netlify deployment
5. Verify game is live with new levels
6. Report completion

---

### **Phase 3: Verification & Reporting**

**Steps:**
1. Check website deployment status
2. Check game deployment status
3. Verify both sites are live
4. Generate deployment report
5. Notify completion

---

## 🚀 EXECUTE VIA GARVIS

**Command:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/garvis-command.py --file GARVIS-DEPLOY-REQUEST.md
```

**Or via webhook:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/garvis \
  -H "Content-Type: application/json" \
  -d @- << EOF
{
  "one_thing": "Deploy all website and game updates to Netlify seamlessly",
  "tasks": [
    "Deploy website to Netlify",
    "Deploy game updates with Book 1, 2, 3 levels",
    "Verify both deployments"
  ],
  "systems": ["website", "game"],
  "priority": "high"
}
EOF
```

---

## ✅ SUCCESS CRITERIA

- [ ] Website deployed to Netlify with all UI/UX improvements
- [ ] Game deployed to Netlify with Book 1, 2, 3 levels
- [ ] Both sites verified live and working
- [ ] Deployment report generated
- [ ] Completion notification sent

---

## 📊 EXPECTED RESULTS

**Website:**
- URL: ballcode.co (or Netlify subdomain)
- Status: Live with all recent commits
- Features: UI/UX improvements, blog enhancements

**Game:**
- URL: ballcode.netlify.app (or custom domain)
- Status: Live with Book 1, 2, 3 levels
- Features: All level files integrated

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** Ready for Garvis Execution

