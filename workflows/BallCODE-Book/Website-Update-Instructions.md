# Website Update Instructions
## Add Story Types Section + "Start Now" Button

**Goal:** Add a section at the bottom of the homepage showing the 3 story types with a "Start Now" button  
**Approach:** Keep existing site design, add new section

---

## What to Add

### Section Location
- **Place:** Bottom of homepage (before footer)
- **Content:** 3 story type cards + "Start Now" button

### The 3 Story Types

1. **🏀 Love Basketball**
   - Action-packed, game footage
   - Perfect for students who play/watch basketball

2. **📊 Studies Basketball**
   - Analytical, data-driven
   - Perfect for students who love stats/analysis

3. **📖 Interested in Stories**
   - Narrative, character-driven
   - Perfect for students who love stories

---

## Implementation

### Option 1: Add to Existing Homepage

**Step 1:** Open your homepage HTML file

**Step 2:** Add this section before the closing `</body>` or before footer:

```html
<!-- Copy the HTML from Website-Story-Types-Section.html -->
```

**Step 3:** Add the CSS styles (either in `<style>` tag or external CSS file)

**Step 4:** Update links:
- `/episodes?style=basketball` → Your episodes page with basketball filter
- `/episodes?style=analytical` → Your episodes page with analytical filter
- `/episodes?style=story` → Your episodes page with story filter
- `/episodes` → Your episodes listing page

---

## HTML Structure

The section includes:
- **Header:** "Choose Your Learning Adventure"
- **Subtitle:** Explanation text
- **3 Story Type Cards:**
  - Icon (🏀, 📊, 📖)
  - Title
  - Description
  - Features list
  - Audience description
  - "Start Learning →" button
- **Start Now Section:**
  - Large "Start Now" button
  - Subtitle text

---

## Styling Notes

### Colors (Match Your Brand)
- Primary: `#667eea` (purple)
- Secondary: `#764ba2` (darker purple)
- Background: `#f8f9fa` (light gray)
- Text: `#666` (gray)

**Update these if your site uses different colors!**

### Layout
- Responsive grid (3 columns on desktop, 1 on mobile)
- Cards with hover effects
- Centered "Start Now" button
- Professional, clean design

---

## Customization Options

### If You Want to Match Your Exact Brand:

1. **Update Colors:**
   - Replace `#667eea` with your primary color
   - Replace `#764ba2` with your secondary color
   - Update background gradients

2. **Update Fonts:**
   - Match your site's font family
   - Adjust font sizes if needed

3. **Update Icons:**
   - Can use custom icons instead of emojis
   - Or use icon fonts (Font Awesome, etc.)

4. **Update Links:**
   - Point to your actual episode pages
   - Add filtering logic if needed

---

## Integration with Episodes Page

### Filtering by Story Type

When users click a story type, they should see:
- Episodes filtered by that style
- Or all episodes with that style highlighted
- Or a dedicated page for that story type

**Example URLs:**
- `/episodes?style=basketball`
- `/episodes?style=analytical`
- `/episodes?style=story`

### Implementation Options:

**Option A: URL Parameters**
- Use query strings to filter
- JavaScript reads parameter and filters episodes

**Option B: Separate Pages**
- `/episodes/basketball`
- `/episodes/analytical`
- `/episodes/story`

**Option C: Highlighting**
- Show all episodes
- Highlight episodes matching selected style
- Visual indicator for each style

---

## Testing Checklist

After adding the section:

- [ ] Section appears at bottom of homepage
- [ ] 3 story type cards display correctly
- [ ] Cards are responsive (mobile/tablet/desktop)
- [ ] Hover effects work
- [ ] "Start Now" button is prominent
- [ ] Links work correctly
- [ ] Colors match your brand
- [ ] Text is readable
- [ ] Icons display properly
- [ ] Mobile layout looks good

---

## Quick Implementation (5 Minutes)

1. **Copy HTML** from `Website-Story-Types-Section.html`
2. **Paste** before footer on homepage
3. **Copy CSS** from the same file
4. **Paste** in your stylesheet or `<style>` tag
5. **Update links** to point to your episodes page
6. **Test** on mobile and desktop

---

## Files Created

1. **`Website-Story-Types-Section.html`** - Complete HTML + CSS for the section
2. **`Website-Update-Instructions.md`** - This file (implementation guide)

---

## Next Steps

1. **Review the HTML/CSS** in `Website-Story-Types-Section.html`
2. **Customize colors/fonts** to match your brand
3. **Add to homepage** before footer
4. **Update links** to point to your episodes
5. **Test** on different devices
6. **Launch!**

---

**Status:** Ready to implement! The HTML/CSS is complete and ready to add to your site. 🚀



