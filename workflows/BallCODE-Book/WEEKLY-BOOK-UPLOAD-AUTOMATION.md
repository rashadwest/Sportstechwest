# Weekly Book Upload Automation System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Automated process for adding new books to the website weekly  
**Status:** Ready to use  
**Last Updated:** November 22, 2025

---

## 🎯 Overview

This system automates the process of adding a new book to your website each week. It works with your current Gumroad payment setup and requires minimal manual steps.

---

## 📋 Pre-Upload Checklist

Before running the automation, ensure you have:

- [ ] **Complete Story Content** - Book written and finalized
- [ ] **Video File** - Recorded video of the book (MP4 format)
- [ ] **Thumbnail Image** - Title page/cover image (JPG/PNG, 400x400px minimum)
- [ ] **Gumroad Product** - Product created on Gumroad with:
  - [ ] Product name
  - [ ] Price set ($5)
  - [ ] Product URL obtained
  - [ ] Password delivery configured (if needed)
- [ ] **Book Metadata** - Title, description, what's included

---

## 🚀 Automation Steps

### Step 1: Prepare Book Files

**Location:** Create a folder for your new book
```
BallCODE-Book/
└── New-Books/
    └── Book-[Number]-[Title]/
        ├── video.mp4
        ├── thumbnail.jpg
        └── metadata.json
```

**Create metadata.json:**
```json
{
  "bookNumber": 2,
  "title": "The Code of Flow",
  "subtitle": "Learn if/then logic through basketball",
  "dribbleLevel": 2,
  "dribbleName": "Crossover Dribble",
  "price": 5,
  "gumroadUrl": "https://9768426137106.gumroad.com/l/YOUR-PRODUCT-ID",
  "description": "Learn sequences and basic blocks through Ava's adventure breaking the press. Discover why fundamentals matter in basketball and how to code the most simple sequences.",
  "includes": [
    "Interactive video book",
    "Game access password (instant delivery)",
    "Curriculum level #2 unlock"
  ],
  "gameInstructions": "After purchase, practice in the game: Ballcode mode → Curriculum → Play → #2"
}
```

---

### Step 2: Update Website HTML

**File:** `BallCode/index.html`

**Location:** Find the books section (around line 70-140)

**Action:** Add new book card after Book 1 (or replace "Coming Soon" for Book 2)

**Template:**
```html
<!-- Book [Number]: [Title] -->
<div class="books-card">
  <div class="books-card-thumbnail">
    <img src="/assets/images/book[Number]-title-page.png" alt="Book [Number]: [Title]" />
    <span class="books-card-badge">Available</span>
    <span class="books-card-play">▶</span>
  </div>
  <div class="books-card-content">
    <div class="books-card-title-wrapper">
      <img src="/assets/images/book[Number]-title-page.png" 
           alt="Book [Number]: [Title]" 
           class="books-card-title-image"
           onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
      <h3 class="books-card-title books-card-title-fallback" style="display: none;">Book [Number]: [Title]</h3>
    </div>
    <p class="books-card-text">[Description from metadata.json]</p>
    
    <div class="books-card-includes">
      <p class="books-card-includes-title">📚 What's Included:</p>
      <ul class="books-card-includes-list">
        <li>[Item 1 from metadata]</li>
        <li>[Item 2 from metadata]</li>
        <li>[Item 3 from metadata]</li>
      </ul>
    </div>
    
    <p class="books-card-price">$[Price]</p>
    <a href="[Gumroad URL from metadata]" target="_blank" class="books-card-button">Buy Book [Number] →</a>
    
    <details class="books-card-access-info">
      <summary class="books-card-access-summary">🎮 How to Access After Purchase</summary>
      <div class="books-card-access-details">
        <ol>
          <li>Get password instantly on thank you page</li>
          <li>Click "Access Game Now" (or go to ballcode.netlify.app)</li>
          <li>Sign up or log in to the game</li>
          <li>Navigate to: <strong>[Game instructions from metadata]</strong></li>
          <li>Enter your password to unlock the level</li>
        </ol>
      </div>
    </details>
  </div>
</div>
```

---

### Step 3: Add Image File

**Action:** Copy thumbnail image to website assets

**Location:** `BallCode/assets/images/`

**File Name:** `book[Number]-title-page.png` (or `.jpg`)

**Command:**
```bash
cp /path/to/your/thumbnail.jpg /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode/assets/images/book[Number]-title-page.png
```

---

### Step 4: Test the Book

**Checklist:**
- [ ] Book card displays correctly on homepage
- [ ] Image loads (or fallback shows)
- [ ] "Buy Book" button links to correct Gumroad URL
- [ ] Price displays correctly
- [ ] Description is accurate
- [ ] "What's Included" list is complete
- [ ] Game access instructions are clear

---

### Step 5: Deploy to Website

**If using Git/Netlify:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode
git add .
git commit -m "Add Book [Number]: [Title]"
git push
```

**If using manual upload:**
- Upload updated `index.html` to your hosting
- Upload new image file to `/assets/images/`

---

## 🔄 Weekly Automation Workflow

### Monday: Content Preparation
- [ ] Write/complete book story
- [ ] Record video
- [ ] Create thumbnail image
- [ ] Set up Gumroad product

### Tuesday: Website Integration
- [ ] Create metadata.json
- [ ] Update index.html with new book card
- [ ] Add image file to assets
- [ ] Test locally

### Wednesday: Deployment & Testing
- [ ] Deploy to website
- [ ] Test purchase flow end-to-end
- [ ] Verify Gumroad integration
- [ ] Check mobile responsiveness

### Thursday: Marketing Prep
- [ ] Create social media posts
- [ ] Update email list (if applicable)
- [ ] Prepare launch announcement

### Friday: Launch
- [ ] Make book live
- [ ] Announce launch
- [ ] Monitor first purchases

---

## 📝 Quick Reference: Book Card Template

**Copy this template and fill in the [BRACKETS]:**

```html
<div class="books-card">
  <div class="books-card-thumbnail">
    <img src="/assets/images/book[NUMBER]-title-page.png" alt="Book [NUMBER]: [TITLE]" />
    <span class="books-card-badge">Available</span>
    <span class="books-card-play">▶</span>
  </div>
  <div class="books-card-content">
    <div class="books-card-title-wrapper">
      <img src="/assets/images/book[NUMBER]-title-page.png" 
           alt="Book [NUMBER]: [TITLE]" 
           class="books-card-title-image"
           onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
      <h3 class="books-card-title books-card-title-fallback" style="display: none;">Book [NUMBER]: [TITLE]</h3>
    </div>
    <p class="books-card-text">[DESCRIPTION]</p>
    
    <div class="books-card-includes">
      <p class="books-card-includes-title">📚 What's Included:</p>
      <ul class="books-card-includes-list">
        <li>[ITEM 1]</li>
        <li>[ITEM 2]</li>
        <li>[ITEM 3]</li>
      </ul>
    </div>
    
    <p class="books-card-price">$[PRICE]</p>
    <a href="[GUMROAD URL]" target="_blank" class="books-card-button">Buy Book [NUMBER] →</a>
    
    <details class="books-card-access-info">
      <summary class="books-card-access-summary">🎮 How to Access After Purchase</summary>
      <div class="books-card-access-details">
        <ol>
          <li>Get password instantly on thank you page</li>
          <li>Click "Access Game Now" (or go to ballcode.netlify.app)</li>
          <li>Sign up or log in to the game</li>
          <li>Navigate to: <strong>[GAME INSTRUCTIONS]</strong></li>
          <li>Enter your password to unlock the level</li>
        </ol>
      </div>
    </details>
  </div>
</div>
```

---

## ✅ Success Criteria

A book is successfully uploaded when:

- [ ] Book card appears on homepage
- [ ] Image displays correctly
- [ ] "Buy Book" button links to working Gumroad product
- [ ] Price is correct
- [ ] Description is accurate
- [ ] Purchase flow works end-to-end
- [ ] Game access instructions are clear
- [ ] Mobile responsive

---

## 🐛 Troubleshooting

### Image Not Showing
- Check file path: `/assets/images/book[NUMBER]-title-page.png`
- Verify file exists in correct location
- Check file name matches exactly (case-sensitive)
- Fallback gradient should show if image missing

### Gumroad Link Not Working
- Verify Gumroad product is published (not draft)
- Check URL is correct (copy from Gumroad product page)
- Test link in new tab before deploying

### Book Card Not Appearing
- Check HTML is inside `<div class="books-grid">` section
- Verify no syntax errors (missing closing tags)
- Check browser console for JavaScript errors

---

## 📊 Weekly Tracking

**Week of [DATE]:**
- Book Number: _______
- Title: _______
- Status: [ ] Content Ready | [ ] Video Ready | [ ] Gumroad Ready | [ ] Website Ready | [ ] Live
- Launch Date: _______
- Notes: _______

---

**Remember:** This automation works with your current Gumroad setup. Each week, follow these steps to add a new book. The process should take 30-60 minutes once content is ready.


