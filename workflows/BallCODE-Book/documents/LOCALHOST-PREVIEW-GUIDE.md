# Localhost Preview Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025

---

## 🌐 Your Website is Now Running on Localhost!

**URL:** http://localhost:8000

---

## 📋 What You Can See

### **Homepage:**
- http://localhost:8000/
- Main BallCODE website

### **Book 1:**
- http://localhost:8000/books/book1.html
- Book 1 page (where visual assets will be added)

### **Book 2:**
- http://localhost:8000/books/book2.html

### **Book 3:**
- http://localhost:8000/books/book3.html

---

## 🎯 What to Look For

### **Current State (Before Visual Assets):**
- ✅ Website structure
- ✅ Mobile responsiveness
- ✅ All content working
- ⚠️ Missing visual assets (3 images)

### **After Adding Visual Assets:**
- ✅ Court Map image
- ✅ Shadow Press Scouts character
- ✅ State Diagram visualization
- ✅ More engaging and professional look

---

## 🔧 How to Stop the Server

**When you're done previewing:**

```bash
# Find and kill the server
lsof -ti:8000 | xargs kill -9
```

Or just close the terminal window.

---

## 📸 Visual Assets Preview

**Once you generate the 3 images:**
1. Save them to: `BallCode/assets/images/`
2. Run: `python3 scripts/add-visuals-to-book1.py`
3. Refresh: http://localhost:8000/books/book1.html
4. See the images appear! 🎉

---

**Your website is ready to preview!** 🚀

