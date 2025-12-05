# Episode 1 Page Implementation Guide

**Goal:** Add Episode 1 story page to ballcode.co  
**URL:** `ballcode.co/episode1` or `ballcode.co/story/episode-1`  
**Timeline:** 1-2 days

---

## What You Need

### Content (Ready)
- ✅ Complete Episode 1 story (from `Episode-1-For-Pilot-School.md`)
- ✅ Skill Pit-Stop content
- ✅ Exercise information

### Template (Ready)
- ✅ `Simple-Website-Template.html` - Base template provided

### Design
- Match your existing ballcode.co branding
- Use your color scheme
- Use your fonts
- Match your style

---

## Implementation Steps

### Step 1: Customize the Template

**File:** `Simple-Website-Template.html`

**What to Change:**
1. **Colors** - Match your brand colors
   - Current: Purple gradient (#667eea, #764ba2)
   - Update to match ballcode.co colors

2. **Fonts** - Match your site fonts
   - Current: System fonts
   - Update if you use custom fonts

3. **Logo/Branding** - Add your logo
   - Add BallCODE logo to header
   - Match your brand style

4. **Navigation** - Add navigation menu
   - Link back to homepage
   - Link to other sections
   - Match your site navigation

5. **Footer** - Update footer
   - Add your contact info
   - Add social links (if applicable)
   - Match your site footer

---

### Step 2: Add Content

**Copy from:** `Episode-1-For-Pilot-School.md`

**Add to HTML:**
- Act I content
- Act II content
- Act III content
- Skill Pit-Stop section
- Exercise information

**Format:**
- Use proper HTML structure
- Add appropriate headings
- Format paragraphs correctly
- Add styling classes

---

### Step 3: Add Links

**Links to Add:**
1. **Teacher Guide** - Link to PDF or teacher page
2. **Exercises** - Link to exercise PDFs or page
3. **Onboarding Guide** - Link to guide PDF or page
4. **Contact** - Link to contact page/email
5. **Home** - Link back to homepage

**Implementation:**
- Add buttons/links in appropriate sections
- Make them prominent and easy to find
- Test all links work

---

### Step 4: Mobile Optimization

**Check:**
- ✅ Responsive design (works on mobile)
- ✅ Text is readable on small screens
- ✅ Buttons are touch-friendly
- ✅ Images scale properly
- ✅ Navigation works on mobile

**Test:**
- Test on actual phone
- Test on tablet
- Test on desktop
- Fix any layout issues

---

### Step 5: Deploy

**Options:**

**Option A: Add to Existing Site**
- If using CMS (WordPress, etc.): Add as new page
- If static HTML: Add new HTML file
- Update navigation to include Episode 1 link

**Option B: Subdomain/Subdirectory**
- `ballcode.co/episode1` (recommended)
- `ballcode.co/story/episode-1`
- `episode1.ballcode.co` (if subdomain)

**Implementation:**
- Upload HTML file
- Configure URL routing
- Test URL works
- Update navigation

---

### Step 6: Test

**Checklist:**
- [ ] Page loads correctly
- [ ] Story displays properly
- [ ] All links work
- [ ] Mobile-responsive
- [ ] Fast loading (< 3 seconds)
- [ ] Professional appearance
- [ ] Accessible from homepage
- [ ] Navigation works
- [ ] Contact links work

---

## Quick Implementation (If Using Template)

### Minimal Changes Needed

1. **Update Colors** (5 minutes)
   ```css
   /* Change these colors to match your brand */
   background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
   color: #667eea; /* Change to your brand color */
   ```

2. **Add Logo** (10 minutes)
   ```html
   <img src="your-logo.png" alt="BallCODE" class="logo">
   ```

3. **Update Footer** (5 minutes)
   ```html
   <p>Contact: your-email@example.com</p>
   ```

4. **Add Navigation** (15 minutes)
   ```html
   <nav>
       <a href="/">Home</a>
       <a href="/episode1">Episode 1</a>
       <a href="/teachers">For Teachers</a>
       <a href="/contact">Contact</a>
   </nav>
   ```

**Total Time:** ~35 minutes for basic customization

---

## Advanced Customization

### If You Want More Features

1. **Add Print Styles**
   - CSS for printing
   - Hide navigation when printing
   - Optimize for PDF

2. **Add Share Buttons**
   - Social media sharing
   - Email sharing
   - Copy link

3. **Add Progress Tracking**
   - Track reading progress
   - Save position (localStorage)
   - Resume reading

4. **Add Audio Narration**
   - Audio player
   - Sync with text
   - Play/pause controls

**Note:** These are nice-to-have, not required for pilot school

---

## Integration with Existing Site

### If ballcode.co Uses:

**WordPress:**
- Create new page
- Use HTML block or custom template
- Add to navigation menu

**Static HTML:**
- Add new HTML file
- Update navigation in all pages
- Link from homepage

**CMS (Other):**
- Follow CMS-specific instructions
- Add new page/content
- Update navigation

**React/Next.js:**
- Create new route/page
- Use template as component
- Add to navigation

---

## Content Structure

### Page Sections (In Order)

1. **Header**
   - Logo
   - Navigation
   - Title: "Episode 1: The Tip-off Trial"

2. **Episode Info**
   - Target audience
   - Duration
   - Learning focus

3. **Act I**
   - Story content
   - Proper formatting

4. **Act II**
   - Story content
   - Proper formatting

5. **Act III**
   - Story content
   - Proper formatting

6. **Skill Pit-Stop**
   - Educational content
   - Highlighted section

7. **Exercises**
   - Exercise information
   - Download links

8. **Footer**
   - Contact info
   - Links
   - Copyright

---

## Testing Before Launch

### Functionality Tests

- [ ] Page loads without errors
- [ ] All text displays correctly
- [ ] Links work properly
- [ ] Navigation works
- [ ] Mobile-responsive
- [ ] Fast loading

### Content Tests

- [ ] Story is complete
- [ ] No typos or errors
- [ ] Formatting is correct
- [ ] Images display (if any)
- [ ] Professional appearance

### User Experience Tests

- [ ] Easy to read
- [ ] Easy to navigate
- [ ] Clear call-to-actions
- [ ] Contact information visible
- [ ] Mobile-friendly

---

## Launch Checklist

### Before Going Live

- [ ] Content reviewed and approved
- [ ] Design matches brand
- [ ] All links tested
- [ ] Mobile tested
- [ ] Fast loading verified
- [ ] Navigation updated
- [ ] Homepage link added
- [ ] Contact info correct

### After Launch

- [ ] Test URL works
- [ ] Share with team for review
- [ ] Add to pilot school package
- [ ] Monitor for issues
- [ ] Collect feedback

---

## Support Resources

### Files You Have

1. ✅ `Simple-Website-Template.html` - Base template
2. ✅ `Episode-1-For-Pilot-School.md` - Story content
3. ✅ `Episode-1-Teacher-Guide.md` - Teacher resources
4. ✅ `Pilot-School-Onboarding-Guide.md` - Onboarding guide

### Need Help?

- Review template file
- Check content files
- Test on multiple devices
- Get feedback before launch

---

## Quick Start (30 Minutes)

If you just want to get something live quickly:

1. **Use the template as-is** (5 min)
2. **Add your contact info** (5 min)
3. **Add navigation link** (5 min)
4. **Deploy to ballcode.co** (10 min)
5. **Test and verify** (5 min)

**Total:** 30 minutes to get Episode 1 page live!

---

**Bottom Line:** You have everything you need. The template is ready, content is ready. Just customize colors/branding, add navigation, and deploy!




