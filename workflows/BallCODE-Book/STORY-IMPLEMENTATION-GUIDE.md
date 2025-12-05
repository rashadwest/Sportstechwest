# Story Implementation Guide
## How to Add New Episodes to ballcode.co

**Purpose:** Step-by-step guide for implementing new story episodes on the website  
**Template:** Use `STORY-IMPLEMENTATION-TEMPLATE.html` as the base  
**Goal:** Make adding new episodes quick and easy

---

## Quick Start

1. **Copy the template:** `STORY-IMPLEMENTATION-TEMPLATE.html`
2. **Rename it:** `episode[NUMBER].html` (e.g., `episode1.html`)
3. **Fill in placeholders:** Replace all `[PLACEHOLDER]` text
4. **Add content:** Insert story content from your markdown files
5. **Test:** Check on desktop and mobile
6. **Deploy:** Upload to website

---

## Content Requirements

### Before You Start

Make sure you have:
- ✅ Complete story (all 3 acts)
- ✅ Act titles for each act
- ✅ Skill Pit-Stop content
- ✅ Exercise content
- ✅ Episode number and title
- ✅ Learning focus/concept
- ✅ Target audience (usually Grades 3-8)
- ✅ Estimated reading duration

---

## Step-by-Step Implementation

### Step 1: Copy Template

```bash
cp STORY-IMPLEMENTATION-TEMPLATE.html episode[NUMBER].html
```

### Step 2: Update Page Metadata

**In `<head>` section:**
- Replace `[NUMBER]` with episode number (e.g., `1`)
- Replace `[TITLE]` with episode title (e.g., `The Tip-off Trial`)

**Example:**
```html
<title>BallCODE - Episode 1: The Tip-off Trial</title>
```

### Step 3: Update Header Section

**Replace placeholders:**
- `[NUMBER]` → Episode number
- `[TITLE]` → Episode title
- `[X]` → Reading duration (e.g., `15-20`)
- `[LEARNING_FOCUS]` → Main concept (e.g., `Understanding State in Code`)

**Example:**
```html
<h1>Episode 1: The Tip-off Trial</h1>
<span class="meta-item">Duration: 15-20 minutes</span>
<span class="meta-item">Focus: Understanding State in Code</span>
```

### Step 4: Add Act I Content

**Replace:**
- `[ACT_I_TITLE]` → Act I title (e.g., `Meet the Crew; Tip-off Chaos`)
- `<!-- ACT_I_CONTENT -->` → Full Act I story text

**Content Format:**
- Use `<p>` tags for paragraphs
- Use `<strong>` for emphasis
- Use `<em>` for italics
- Preserve line breaks where needed

**Example:**
```html
<h2>Act I: Meet the Crew; Tip-off Chaos</h2>
<div class="story-text">
    <p>The center circle of Data Court glowed with a soft blue light...</p>
    <p>"Remember," Coach Circuit's voice crackled...</p>
</div>
```

### Step 5: Add Act II Content

**Same process as Act I:**
- Replace `[ACT_II_TITLE]`
- Replace `<!-- ACT_II_CONTENT -->` with Act II story

### Step 6: Add Act III Content

**Same process:**
- Replace `[ACT_III_TITLE]`
- Replace `<!-- ACT_III_CONTENT -->` with Act III story

### Step 7: Add Skill Pit-Stop

**Replace:**
- `[SKILL_TITLE]` → Skill/concept title (e.g., `Understanding State in Code`)
- `<!-- SKILL_PIT_STOP_CONTENT -->` → Full Skill Pit-Stop content

**Example:**
```html
<h2>Skill Pit-Stop: Understanding State in Code</h2>
<div class="skill-content">
    <p><strong>What is State?</strong></p>
    <p>Think of state like a light switch...</p>
</div>
```

### Step 8: Add Exercises

**Replace:**
- `<!-- EXERCISE_CONTENT -->` → Exercise descriptions
- Update PDF link: `/teachers/episode-[NUMBER]-exercises.pdf`

**Example:**
```html
<div class="exercise-content">
    <h3>Exercise A: Label States in a Play</h3>
    <p>Read the basketball scenario and label each state change...</p>
</div>
<a href="/teachers/episode-1-exercises.pdf" class="cta-button">Download Exercises (PDF)</a>
```

---

## Content Formatting Guidelines

### Paragraphs
- Each paragraph should be in its own `<p>` tag
- Don't use `<br>` for spacing (use CSS margins instead)

### Emphasis
- Use `<strong>` for important terms/concepts
- Use `<em>` for emphasis within sentences

### Lists
- Use `<ul>` or `<ol>` for lists
- Use `<li>` for list items

### Code/Technical Terms
- Use `<code>` for code snippets or technical terms
- Use `<strong>` for state names (START, LIVE, DEAD, OUTCOME)

### Dialogue
- Keep dialogue in `<p>` tags
- Use quotation marks as written
- No special formatting needed

---

## Testing Checklist

Before deploying, test:

- [ ] All placeholders replaced
- [ ] Content displays correctly
- [ ] Navigation links work
- [ ] Mobile responsive (test on phone)
- [ ] All links work (exercises, contact, etc.)
- [ ] Page loads quickly
- [ ] No broken images
- [ ] Text is readable
- [ ] Footer information correct

---

## File Naming Convention

**Episode Pages:**
- Format: `episode[NUMBER].html`
- Examples: `episode1.html`, `episode2.html`, `episode12.html`

**Supporting Files:**
- CSS: `/assets/css/episode.css` (shared)
- PDFs: `/teachers/episode-[NUMBER]-exercises.pdf`

---

## URL Structure

**Target URLs:**
- Episode 1: `ballcode.co/episode1` or `ballcode.co/episodes/episode1`
- Episode 2: `ballcode.co/episode2` or `ballcode.co/episodes/episode2`
- etc.

**Update navigation:**
- Add episode link to main navigation menu
- Add to episodes index page (if exists)

---

## Common Issues & Solutions

### Issue: Content not displaying
**Solution:** Check that all HTML tags are properly closed

### Issue: Mobile layout broken
**Solution:** Verify CSS is linked correctly, check responsive breakpoints

### Issue: Links not working
**Solution:** Check file paths are correct (use relative paths)

### Issue: Styling looks wrong
**Solution:** Ensure CSS files are linked and paths are correct

---

## Content Source Files

**Where to get content:**
- Story content: `Episode-[NUMBER]-For-Pilot-School.md` or `Episode-[NUMBER]-Story-Draft.md`
- Skill Pit-Stop: `Episode-[NUMBER]-Skill-Pit-Stop.md`
- Exercises: `Episode-[NUMBER]-Exercises.md`

---

## Future Enhancements

**Potential additions (not required for MVP):**
- Video/audio player for recordings
- Interactive exercises
- Progress tracking
- Social sharing buttons
- Print-friendly CSS
- Reading time estimation

---

## Support

**Questions?**
- Review this guide
- Check `STORY-IMPLEMENTATION-TEMPLATE.html` for examples
- Refer to `Episode-1-For-Pilot-School.md` for content structure reference

---

**Status:** Template ready for use  
**Last Updated:** [Current Date]  
**Next Episode:** Use this guide for Episode 2, 3, etc.



