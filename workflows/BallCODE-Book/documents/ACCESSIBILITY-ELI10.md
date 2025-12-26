# Accessibility - ELI10 (Explain Like I'm 10)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025

---

## 🎯 What is Accessibility?

**Simple Answer:** Making your website work for **everyone**, including people who can't see or have trouble seeing.

---

## 👀 The Problem (What We Found)

**In your `book1.html` file:**
- You have images (pictures)
- But the images don't have "alt text" (descriptions)

**What that means:**
- When someone who is **blind** visits your website
- Their computer reads the website out loud to them
- When it gets to an image, it says: "Image" (that's not helpful!)
- They have no idea what the picture shows

---

## ✅ The Fix (Super Simple)

**Add "alt text" to images**

**What is alt text?**
- It's like a **caption** that describes what the picture shows
- But it's hidden (you don't see it on the page)
- Screen readers (for blind people) can read it out loud

**Example:**
```html
<!-- BEFORE (Bad): -->
<img src="basketball-court.png">

<!-- AFTER (Good): -->
<img src="basketball-court.png" alt="Basketball court showing the center circle">
```

**Now when a blind person visits:**
- Their computer says: "Image: Basketball court showing the center circle"
- They understand what the picture shows! ✅

---

## 🎯 Why This Matters

**It's the law:**
- Websites must be accessible to everyone
- It's called the "Americans with Disabilities Act" (ADA)

**It's good for everyone:**
- Helps people with slow internet (images don't load? Alt text shows)
- Helps search engines (Google understands your images)
- Makes your website better overall

---

## 🔧 What We Need to Fix

**In `books/book1.html`:**
- Find all `<img>` tags
- Add `alt="description"` to each one

**Time:** 5 minutes (super quick!)

**Example fix:**
```html
<!-- If you have this: -->
<img src="../assets/images/book1-cover.png">

<!-- Change it to this: -->
<img src="../assets/images/book1-cover.png" alt="Book 1 cover showing basketball player doing foundation block move">
```

---

## ✅ Bottom Line

**Accessibility = Making your website work for everyone**

**The fix = Add descriptions to images (5 minutes)**

**Why = It's the right thing to do, and it's the law**

---

**That's it! Super simple. Just add descriptions to your images.** 🎯

