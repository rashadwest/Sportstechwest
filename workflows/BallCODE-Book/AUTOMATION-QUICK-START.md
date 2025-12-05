# Automation Quick Start Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**One-command book upload system** - Everything automated!

---

## 🚀 Quick Start: Upload Book 2 (When Ready)

**Just run this one command:**

```bash
python3 automate-book-upload.py \
  2 \
  "The Code of Flow" \
  "Learn if/then logic through Ava's one-on-one challenge. Discover how to make smart decisions based on what you see—just like coding uses conditional logic." \
  "https://9768426137106.gumroad.com/l/YOUR-PRODUCT-ID" \
  "/path/to/book2-thumbnail.png" \
  5
```

**Then deploy:**
```bash
cd BallCode && ../automate-deployment.sh "Add Book 2: The Code of Flow"
```

**Done!** ✅

---

## 📋 What Each Script Does

### 1. `automate-book-upload.py` - Upload Book
- Updates website HTML automatically
- Copies thumbnail image
- Replaces "Coming Soon" with actual book
- Prepares git commit

### 2. `test-book-section.sh` - Test Everything
- Validates books section
- Checks images
- Verifies links
- Tests HTML structure

### 3. `automate-deployment.sh` - Deploy to Live
- Commits changes
- Pushes to GitHub
- Triggers auto-deployment

---

## 🎯 Complete Workflow

```bash
# Step 1: Upload book
python3 automate-book-upload.py [book-number] [title] [description] [gumroad-url] [thumbnail] [price]

# Step 2: Test
./test-book-section.sh

# Step 3: Deploy
cd BallCode && ../automate-deployment.sh "Your commit message"
```

---

## ✅ Current Status (From Test)

- ✅ Books section: Working
- ✅ Book 1: Complete with Gumroad link
- ⚠️ Book 2: Waiting for content (still "Coming Soon")
- ✅ Images: Present
- ✅ HTML: Valid

---

**Everything is automated and ready!** Just provide book details and run the scripts. 🤖


