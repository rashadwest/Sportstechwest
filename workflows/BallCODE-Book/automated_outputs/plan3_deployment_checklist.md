# Plan 3: Website Deployment Checklist

**Status:** Episode 1 Page Ready - Deployment Checklist Created  
**Completion:** 60% (Phase 1 items ready)

---

## Pre-Deployment Checklist

### Domain & Hosting
- [ ] Confirm `ballcode.co` domain ownership
- [ ] Verify domain DNS settings
- [ ] Confirm hosting platform (GitHub Pages, Netlify, Vercel, etc.)
- [ ] Test hosting access/credentials

### File Preparation
- [x] Episode 1 HTML page created (`episode1_page.html`)
- [x] Page verified production-ready
- [ ] Test page locally in browser
- [ ] Verify all links work
- [ ] Check mobile responsiveness

---

## Deployment Steps

### Step 1: Choose Hosting Platform

**Option A: GitHub Pages (Recommended for simplicity)**
1. Create repository (if not exists)
2. Upload `episode1_page.html` to repository
3. Rename to `index.html` OR create `episode1` folder
4. Enable GitHub Pages in repository settings
5. Set source to main branch
6. Access at: `username.github.io/repo/episode1` or custom domain

**Option B: Netlify**
1. Sign up/login to Netlify
2. Drag and drop `episode1_page.html` OR connect Git repository
3. Netlify auto-deploys
4. Access at: `your-site.netlify.app/episode1` or custom domain

**Option C: Vercel**
1. Sign up/login to Vercel
2. Import project or upload files
3. Vercel auto-deploys
4. Access at: `your-site.vercel.app/episode1` or custom domain

### Step 2: Deploy Episode 1 Page

1. **Upload file to hosting:**
   - If using GitHub: Commit and push `episode1_page.html`
   - If using Netlify/Vercel: Upload via dashboard or connect Git

2. **Set URL structure:**
   - Target URL: `ballcode.co/episode1` (or subdomain)
   - If using custom domain: Configure DNS settings

3. **Test deployment:**
   - Visit URL in browser
   - Test on mobile device
   - Verify all content displays correctly

### Step 3: Add Navigation Menu

1. **Locate main website template/header**
2. **Add navigation code** (see `plan3_navigation_code.html`)
3. **Test navigation links**
4. **Verify mobile menu works**

### Step 4: Update Contact Information

1. **Locate contact section on website**
2. **Add contact info** (see `plan3_contact_info.html`)
3. **Test contact form/email links**
4. **Verify information is visible**

### Step 5: Fix Sign-Up Button

1. **Locate sign-up button on homepage**
2. **Update button link** (see `plan3_signup_button_fix.html`)
3. **Test button functionality**
4. **Verify no placeholder redirects**

### Step 6: Add Episode 1 Quick Access

1. **Locate homepage hero/banner section**
2. **Add "Try Episode 1" button** linking to `/episode1`
3. **Style button prominently**
4. **Test button on mobile**

---

## Post-Deployment Testing

### Functionality Tests
- [ ] Episode 1 page loads correctly
- [ ] All internal links work
- [ ] Navigation menu functional
- [ ] Contact information visible and correct
- [ ] Sign-up button works (no placeholder)
- [ ] Episode 1 link on homepage works

### Content Tests
- [ ] Story displays correctly (all 3 acts)
- [ ] Skill Pit-Stop section visible
- [ ] Exercise section visible
- [ ] No typos or formatting issues
- [ ] Images load (if any added)

### Mobile Tests
- [ ] Page responsive on phone (iPhone/Android)
- [ ] Text readable on mobile
- [ ] Buttons touch-friendly
- [ ] Navigation works on mobile
- [ ] No horizontal scrolling
- [ ] Layout looks good on tablet

### Performance Tests
- [ ] Page loads quickly (< 3 seconds)
- [ ] No broken links
- [ ] No console errors
- [ ] Images optimized (if any)

### Cross-Browser Tests
- [ ] Chrome
- [ ] Safari
- [ ] Firefox
- [ ] Edge

---

## Deployment Verification

### Final Checklist
- [ ] All tests passed
- [ ] No critical issues
- [ ] Mobile-friendly verified
- [ ] Professional appearance confirmed
- [ ] URL ready to share: `ballcode.co/episode1`

---

## Communication to Pilot School

**Message Template:**
```
We're excited to share that Episode 1: The Tip-off Trial is now available online!

Students can access the story and exercises directly from any device at:
[URL]

The page includes:
- Complete Episode 1 story (all 3 acts)
- Skill Pit-Stop mini-lesson
- Exercise links and resources
- Mobile-friendly design

We're also building an enhanced interactive version with full Unity story mode that will be ready in 1-2 weeks.
```

---

## Next Steps After Deployment

1. **Monitor usage** - Track page visits
2. **Collect feedback** - Ask pilot school for input
3. **Plan Phase 2** - Begin Unity WebGL build
4. **Iterate** - Make improvements based on feedback

---

**Status:** ✅ Deployment checklist complete  
**Ready for:** Deployment execution




