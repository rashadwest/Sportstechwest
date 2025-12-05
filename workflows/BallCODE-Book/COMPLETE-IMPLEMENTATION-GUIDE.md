# Complete Website Implementation Guide - Step by Step

**Goal:** Update ballcode.co for pilot school package  
**Timeline:** This week (5 days)  
**Approach:** Step-by-step with specific instructions

---

## Phase 1: Quick Fixes (Day 1 - 1 Hour)

### Step 1: Fix Contact Information

**What You Need:**
- Access to edit ballcode.co
- Your email address
- Your phone number (optional)

**Instructions:**

1. **Find the Contact Section**
   - Log into your website admin/editor
   - Navigate to the contact page or section
   - Look for where contact info is displayed

2. **Add Your Email**
   - Add: `your-email@example.com` (use your actual email)
   - Make it clickable: `<a href="mailto:your-email@example.com">your-email@example.com</a>`
   - Place it prominently (top of page or dedicated contact section)

3. **Add Phone (Optional)**
   - Add: `(555) 123-4567` (use your actual phone)
   - Make it clickable: `<a href="tel:+15551234567">(555) 123-4567</a>`

4. **Add Response Time Info**
   - Add text: "Response time: Within 24 hours"
   - This sets expectations for pilot school

**Example HTML:**
```html
<div class="contact-info">
    <h2>Contact Us</h2>
    <p>Email: <a href="mailto:your-email@example.com">your-email@example.com</a></p>
    <p>Phone: <a href="tel:+15551234567">(555) 123-4567</a></p>
    <p><small>Response time: Within 24 hours</small></p>
</div>
```

**Checklist:**
- [ ] Email added and visible
- [ ] Email is clickable (mailto link)
- [ ] Phone added (if applicable)
- [ ] Response time info added
- [ ] Contact section is easy to find

---

### Step 2: Fix Sign-Up Button

**What You Need:**
- Access to edit homepage/button
- Destination URL (contact form, email, or pilot program page)

**Instructions:**

1. **Find the Sign-Up Button**
   - Look for button that says "SIGN UP FOR MORE INFO" or similar
   - Currently redirects to `ballcode.netlify.app`

2. **Choose New Destination**
   - **Option A:** Contact form (if you have one)
   - **Option B:** Email link: `mailto:your-email@example.com`
   - **Option C:** Pilot program page (if you create one)
   - **Option D:** Contact page

3. **Update the Link**
   - Change the button's href/URL
   - Test that it works

**Example HTML:**
```html
<!-- Option A: Link to Contact Form -->
<a href="/contact" class="sign-up-button">SIGN UP FOR MORE INFO</a>

<!-- Option B: Link to Email -->
<a href="mailto:your-email@example.com?subject=Pilot Program Inquiry" class="sign-up-button">SIGN UP FOR MORE INFO</a>

<!-- Option C: Link to Contact Page -->
<a href="/contact" class="sign-up-button">SIGN UP FOR MORE INFO</a>
```

**Checklist:**
- [ ] Button link updated
- [ ] Button works (no placeholder redirect)
- [ ] Destination page/form works
- [ ] Tested on multiple devices

---

### Step 3: Add Episode 1 Link to Homepage

**What You Need:**
- Access to edit homepage
- URL for Episode 1 page (will be `ballcode.co/episode1`)

**Instructions:**

1. **Find Homepage Hero Section**
   - Look for main banner/hero area
   - Usually at top of homepage

2. **Add Button/Link**
   - Add prominent button: "Try Episode 1" or "Access Episode 1"
   - Make it visually prominent
   - Link to: `ballcode.co/episode1` (or `/episode1`)

3. **Style the Button**
   - Make it stand out (different color, larger size)
   - Ensure it's clickable and clear

**Example HTML:**
```html
<!-- In Hero Section -->
<div class="hero">
    <h1>BallCODE - STEM Learning Through Basketball</h1>
    <p>Teaching coding, math, and AI through the game you love</p>
    <a href="/episode1" class="cta-button episode1-button">Try Episode 1 Free</a>
    <a href="/contact" class="cta-button secondary-button">SIGN UP FOR MORE INFO</a>
</div>
```

**Example CSS:**
```css
.episode1-button {
    background: #667eea;
    color: white;
    padding: 15px 30px;
    border-radius: 8px;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
    margin: 10px;
    font-size: 1.2em;
}

.episode1-button:hover {
    background: #764ba2;
}
```

**Checklist:**
- [ ] Button added to homepage
- [ ] Button is prominent and visible
- [ ] Link works (will work once Episode 1 page is created)
- [ ] Button is mobile-friendly
- [ ] Styled appropriately

---

## Phase 2: Episode 1 Page (Day 2-3 - 4-6 Hours)

### Step 4: Create Episode 1 Page

**What You Need:**
- `Simple-Website-Template.html` (provided)
- `Episode-1-For-Pilot-School.md` (content source)
- Access to add new page to ballcode.co

**Instructions:**

#### Part A: Customize the Template

1. **Open `Simple-Website-Template.html`**
   - Open in text editor (VS Code, Notepad++, etc.)

2. **Update Colors to Match Your Brand**
   - Find color codes in CSS section
   - Replace with your brand colors
   - Look for: `#667eea`, `#764ba2` (purple gradient)
   - Replace with your colors

**Find This:**
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
color: #667eea;
```

**Replace With Your Colors:**
```css
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
color: #YOUR_COLOR_1;
```

3. **Add Your Logo**
   - Find header section
   - Add logo image

**Find This:**
```html
<div class="header">
    <h1>BallCODE</h1>
    <p class="subtitle">STEM Learning Through Basketball</p>
</div>
```

**Add Logo:**
```html
<div class="header">
    <img src="/path/to/your-logo.png" alt="BallCODE Logo" class="logo">
    <h1>BallCODE</h1>
    <p class="subtitle">STEM Learning Through Basketball</p>
</div>
```

4. **Add Navigation Menu**
   - Add navigation links

**Add Before Header:**
```html
<nav class="main-nav">
    <a href="/">Home</a>
    <a href="/episode1">Episode 1</a>
    <a href="/teachers">For Teachers</a>
    <a href="/contact">Contact</a>
</nav>
```

**Add CSS for Navigation:**
```css
.main-nav {
    background: rgba(255, 255, 255, 0.95);
    padding: 15px 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.main-nav a {
    color: #333;
    text-decoration: none;
    margin: 0 20px;
    font-weight: 500;
}

.main-nav a:hover {
    color: #667eea;
}
```

5. **Update Footer with Contact Info**
   - Find footer section
   - Add your contact information

**Find This:**
```html
<div class="footer">
    <p><strong>BallCODE</strong> - Teaching STEM Through Basketball</p>
    <p>Episode 1: The Tip-off Trial</p>
    <p>For questions or support, contact your teacher or visit ballcode.co</p>
</div>
```

**Update To:**
```html
<div class="footer">
    <p><strong>BallCODE</strong> - Teaching STEM Through Basketball</p>
    <p>Episode 1: The Tip-off Trial</p>
    <p>Questions? <a href="mailto:your-email@example.com">your-email@example.com</a></p>
    <p><a href="/">Home</a> | <a href="/contact">Contact</a></p>
</div>
```

#### Part B: Add Story Content

1. **Copy Story Content**
   - Open `Episode-1-For-Pilot-School.md`
   - Copy Act I, Act II, Act III content

2. **Paste into HTML**
   - Find content sections in HTML
   - Replace placeholder text with actual story
   - Maintain proper HTML structure

**Structure:**
```html
<div class="content-section">
    <h2>Act I: Meet the Crew; Tip-off Chaos</h2>
    <p>The center circle of Data Court glowed...</p>
    <!-- Paste Act I content here -->
</div>

<div class="content-section">
    <h2>Act II: Shadow Press Scouts Force Turnovers</h2>
    <p>The shadows moved...</p>
    <!-- Paste Act II content here -->
</div>

<div class="content-section">
    <h2>Act III: Controlled Outlet → Fill Lanes → Safe Entry</h2>
    <p>The ball came off the rim...</p>
    <!-- Paste Act III content here -->
</div>
```

3. **Add Skill Pit-Stop Section**
   - Copy Skill Pit-Stop content from markdown
   - Paste into the skill-pit-stop div

4. **Add Exercise Links**
   - Add links to exercise PDFs or teacher page
   - Update button links

**Find This:**
```html
<a href="#" class="cta-button">Download Exercises (PDF)</a>
```

**Update To:**
```html
<a href="/teachers" class="cta-button">Download Exercises (PDF)</a>
<!-- OR -->
<a href="/path/to/exercises.pdf" class="cta-button" download>Download Exercises (PDF)</a>
```

#### Part C: Deploy the Page

**Option A: If Using WordPress**
1. Go to WordPress admin
2. Pages → Add New
3. Title: "Episode 1: The Tip-off Trial"
4. Switch to "Code" or "HTML" editor
5. Paste your HTML code
6. Publish
7. Set permalink: `episode1`

**Option B: If Using Static HTML**
1. Save HTML file as `episode1.html`
2. Upload to your web server
3. Place in root directory or `/story/` folder
4. Access at: `ballcode.co/episode1.html` or `ballcode.co/story/episode1.html`

**Option C: If Using Netlify/Vercel**
1. Add HTML file to your project
2. Deploy
3. Configure routing if needed

**Option D: If Using Other CMS**
- Follow your CMS's instructions for adding new pages
- Upload HTML or use page builder

**Checklist:**
- [ ] Template customized with your colors
- [ ] Logo added
- [ ] Navigation menu added
- [ ] Story content added (all 3 acts)
- [ ] Skill Pit-Stop added
- [ ] Exercise links added
- [ ] Footer updated with contact info
- [ ] Page deployed
- [ ] URL works: `ballcode.co/episode1`
- [ ] Tested on desktop
- [ ] Tested on mobile

---

## Phase 3: Navigation Menu (Day 2-3 - 1 Hour)

### Step 5: Add Navigation Menu to Main Site

**What You Need:**
- Access to edit site header/navigation
- List of pages to link to

**Instructions:**

1. **Find Header/Navigation Area**
   - Usually in site header
   - May be in theme settings

2. **Add Navigation Links**
   - Home → `/` or `/index.html`
   - Episode 1 → `/episode1`
   - For Teachers → `/teachers` (optional for now)
   - Contact → `/contact`

**Example HTML:**
```html
<nav class="site-nav">
    <div class="nav-container">
        <a href="/" class="logo">BallCODE</a>
        <ul class="nav-menu">
            <li><a href="/">Home</a></li>
            <li><a href="/episode1">Episode 1</a></li>
            <li><a href="/teachers">For Teachers</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </div>
</nav>
```

**Example CSS:**
```css
.site-nav {
    background: white;
    padding: 15px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
}

.nav-menu {
    list-style: none;
    display: flex;
    gap: 30px;
}

.nav-menu a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
}

.nav-menu a:hover {
    color: #667eea;
}
```

**For Mobile (Hamburger Menu):**
```html
<button class="mobile-menu-toggle">☰</button>
```

```css
.mobile-menu-toggle {
    display: none;
}

@media (max-width: 768px) {
    .mobile-menu-toggle {
        display: block;
    }
    
    .nav-menu {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        padding: 20px;
    }
    
    .nav-menu.active {
        display: flex;
    }
}
```

**Checklist:**
- [ ] Navigation menu added
- [ ] All links work
- [ ] Mobile-responsive (hamburger menu)
- [ ] Styled appropriately
- [ ] Consistent across pages

---

## Phase 4: Testing & Polish (Day 4 - 2 Hours)

### Step 6: Test Everything

**Testing Checklist:**

**Functionality:**
- [ ] Episode 1 page loads
- [ ] All links work
- [ ] Contact info visible
- [ ] Sign-up button works
- [ ] Navigation works
- [ ] Homepage Episode 1 link works

**Content:**
- [ ] Story displays correctly
- [ ] No typos
- [ ] Formatting is correct
- [ ] Images load (if any)

**Mobile:**
- [ ] Test on phone
- [ ] Test on tablet
- [ ] Text is readable
- [ ] Buttons are touch-friendly
- [ ] Navigation works on mobile
- [ ] No horizontal scrolling

**Performance:**
- [ ] Page loads quickly (< 3 seconds)
- [ ] No broken links
- [ ] No console errors

**Cross-Browser:**
- [ ] Chrome
- [ ] Safari
- [ ] Firefox
- [ ] Edge

---

### Step 7: Final Polish

**Last Checks:**
- [ ] All contact info correct
- [ ] All links tested
- [ ] Professional appearance
- [ ] Consistent branding
- [ ] Mobile-friendly
- [ ] Fast loading

---

## Phase 5: Launch & Package (Day 5 - 1 Hour)

### Step 8: Prepare for Pilot School

**Final Steps:**
1. **Verify URLs**
   - Episode 1: `ballcode.co/episode1`
   - Contact: `ballcode.co/contact`
   - Home: `ballcode.co`

2. **Update Package Documents**
   - Add website URLs to email template
   - Update progress update document
   - Include URLs in onboarding guide

3. **Send Package**
   - Use email template
   - Include all documents
   - Include website URLs
   - Follow up

---

## Platform-Specific Instructions

### If Using WordPress

**Adding New Page:**
1. Dashboard → Pages → Add New
2. Title: "Episode 1: The Tip-off Trial"
3. Use "Custom HTML" block or "Code" editor
4. Paste HTML code
5. Publish
6. Settings → Permalinks → Set to: `episode1`

**Adding Navigation:**
1. Appearance → Menus
2. Create new menu or edit existing
3. Add pages/links
4. Assign to menu location

**Adding Contact Info:**
1. Edit contact page or widget
2. Add email/phone
3. Save

---

### If Using Static HTML

**Adding New Page:**
1. Create `episode1.html` file
2. Copy template HTML
3. Customize
4. Upload to server
5. Access at: `ballcode.co/episode1.html`

**Adding Navigation:**
1. Edit header in all HTML files
2. Add navigation HTML
3. Update all pages consistently

**Adding Contact Info:**
1. Edit contact page HTML
2. Add email/phone
3. Upload

---

### If Using Netlify

**Adding New Page:**
1. Add `episode1.html` to project
2. Push to Git
3. Netlify auto-deploys
4. Access at: `ballcode.co/episode1.html`

**Custom Routing:**
- Create `_redirects` file:
```
/episode1 /episode1.html 200
```

---

### If Using Wix/Squarespace

**Adding New Page:**
1. Pages → Add New Page
2. Title: "Episode 1"
3. Use "Embed Code" or "HTML" block
4. Paste HTML (may need to adjust)
5. Publish

**Adding Navigation:**
1. Edit site navigation
2. Add new page link
3. Save

---

## Troubleshooting

### Episode 1 Page Not Loading

**Check:**
- File uploaded correctly
- URL is correct
- Permissions set correctly
- Server configuration

**Fix:**
- Verify file path
- Check server logs
- Test URL directly

---

### Links Not Working

**Check:**
- Link URLs are correct
- Links use correct format (`/episode1` not `episode1.html`)
- No typos in URLs

**Fix:**
- Use absolute paths if needed
- Test each link
- Verify URLs

---

### Mobile Issues

**Check:**
- Viewport meta tag present
- CSS is responsive
- Font sizes appropriate
- Touch targets large enough

**Fix:**
- Add viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Test on actual device
- Adjust CSS for mobile

---

## Support Resources

### Files You Have
1. ✅ `Simple-Website-Template.html` - Template
2. ✅ `Episode-1-For-Pilot-School.md` - Content
3. ✅ `Episode-1-Teacher-Guide.md` - Teacher resources
4. ✅ `Pilot-School-Onboarding-Guide.md` - Onboarding

### Need More Help?
- Review template file
- Check content files
- Test incrementally
- Get feedback

---

## Quick Reference

### Critical URLs
- Episode 1: `ballcode.co/episode1`
- Contact: `ballcode.co/contact`
- Home: `ballcode.co`

### Key Files
- Template: `Simple-Website-Template.html`
- Content: `Episode-1-For-Pilot-School.md`

### Priority Order
1. Fix contact info (15 min)
2. Fix sign-up button (15 min)
3. Create Episode 1 page (4-6 hours)
4. Add navigation (1 hour)
5. Test everything (2 hours)

---

**You've got this! Follow the steps one at a time, and you'll have everything ready for the pilot school package! 🚀**




