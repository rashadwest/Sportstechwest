# Roboflow - Accessing Your Existing Project & Finding Training

**Your Project:** BTE Basketball Detection  
**Current Issue:** Can't see project content or training options

---

## Accessing Your Existing Project

### Step 1: Find Your Project

**In the Left Sidebar:**
- Look for "BTE Basketball De..." at the top (below the Roboflow logo)
- This is your workspace/project selector
- Click on it to see project options

**OR**

**In the Main Area:**
- If you see the "Projects" overview page with "+ New Project" button
- Look for a list of projects below or in a sidebar
- Your "BTE Basketball Detection" project should be listed there
- Click on it to open

---

## Step 2: Navigate to Your Project Dashboard

### Once You Click Your Project:

You should see your **Project Dashboard** with these tabs at the top:

1. **Overview** - Project stats, dataset info
2. **Upload** - Upload new images/videos
3. **Annotate** - Label your images (draw bounding boxes, keypoints)
4. **Train** - Train your model (THIS IS WHAT YOU'RE LOOKING FOR!)
5. **Deploy** - Deploy trained model
6. **Settings** - Project settings

---

## Finding the Train Tab

### The Train Tab Location:

1. **Click on your project** ("BTE Basketball Detection")
2. **Look at the top tabs** in the project dashboard
3. **Find "Train" tab** - it should be there

### Why You Might Not See It:

**The "Train" tab only appears if:**
- ✅ You have uploaded images to your project
- ✅ You have labeled at least some images
- ❌ If you have no labeled data, the Train tab won't be visible/active

---

## Checking Your Project Status

### What to Check:

1. **Go to "Overview" Tab:**
   - How many images do you have?
   - How many are labeled?
   - What's your dataset status?

2. **Go to "Upload" Tab:**
   - Do you have images uploaded?
   - If empty, you need to upload images first

3. **Go to "Annotate" Tab:**
   - Do you have labeled images?
   - If empty or no labels, you need to label images first
   - Training requires labeled data

---

## Common Scenarios

### Scenario 1: Project Exists But No Data

**Symptoms:**
- Project exists
- No images uploaded
- Train tab not visible

**Solution:**
1. Go to "Upload" tab
2. Upload basketball images/videos
3. Go to "Annotate" tab
4. Label your images
5. Train tab will appear after labeling

---

### Scenario 2: Project Has Images But No Labels

**Symptoms:**
- Images uploaded
- Train tab not visible or grayed out
- No annotations/labels

**Solution:**
1. Go to "Annotate" tab
2. Click on an image
3. Draw bounding boxes and label them
4. Label at least 10-20 images
5. Train tab will become active

---

### Scenario 3: Train Tab Exists But Can't Start Training

**Symptoms:**
- Train tab is visible
- But can't click "Start Training" or button is disabled

**Solution:**
- You need more labeled images (minimum 50-100 recommended)
- Check "Overview" tab to see how many labeled images you have
- Label more images, then try again

---

## Step-by-Step: Getting to Training

### If You're on the Projects Overview Page:

1. **Find Your Project:**
   - Look for "BTE Basketball Detection" in project list
   - OR click the project selector in left sidebar
   - Click on your project name

2. **You'll See Project Dashboard:**
   - Tabs at top: Overview, Upload, Annotate, Train, Deploy

3. **Check Your Data:**
   - Click "Overview" - see how many images/labels you have
   - Click "Upload" - see if you have images
   - Click "Annotate" - see if you have labels

4. **If No Data:**
   - Upload images first (Upload tab)
   - Then label them (Annotate tab)
   - Then Train tab will work

5. **If You Have Labeled Data:**
   - Click "Train" tab
   - Configure training settings
   - Click "Start Training"

---

## Quick Navigation Guide

### From Projects Overview to Training:

```
Projects Page → Click "BTE Basketball Detection" → Project Dashboard → Train Tab
```

### If Train Tab Not Visible:

```
Projects Page → Your Project → Upload Tab → Add Images → Annotate Tab → Label Images → Train Tab Appears
```

---

## What to Do Right Now

### Step 1: Access Your Project

**Option A: Click Project in List**
- If you see project list, click "BTE Basketball Detection"

**Option B: Use Sidebar Selector**
- Click "BTE Basketball De..." in left sidebar
- Select your project

**Option C: Direct URL**
- Your URL shows: `app.roboflow.com/bte-basketball-detection-v1`
- This IS your project URL
- You might already be in it, just need to navigate to Train tab

---

### Step 2: Check Your Tabs

Once in your project, look for tabs at the top:
- Overview
- Upload
- **Annotate** ← Label images here
- **Train** ← Train model here (if you have labeled data)
- Deploy
- Settings

---

### Step 3: If Train Tab Not Visible

1. **Check "Overview" Tab:**
   - How many labeled images do you have?
   - If 0, you need to label images first

2. **Go to "Annotate" Tab:**
   - Label at least 10-20 images
   - Draw bounding boxes and label them
   - Save annotations

3. **Train Tab Will Appear:**
   - After labeling, refresh or navigate
   - Train tab should now be visible/active

---

## Direct Access Methods

### Method 1: URL Navigation

Your current URL: `https://app.roboflow.com/bte-basketball-detection-v1`

This IS your project! You might just need to:
- Scroll to see tabs
- Click on "Train" tab at the top
- If Train tab not there, check if you have labeled data

---

### Method 2: Sidebar Navigation

1. In left sidebar, you're already in "BTE Basketball De..." workspace
2. The main area should show your project
3. Look for tabs at the top of the main content area
4. Click "Train" tab

---

### Method 3: Breadcrumb Navigation

- Look for breadcrumbs at top: "Projects > BTE Basketball Detection"
- Click on project name
- See all tabs

---

## Troubleshooting

### "I'm in my project but don't see Train tab"

**Check:**
1. Do you have images uploaded? (Check "Upload" tab)
2. Do you have labeled images? (Check "Annotate" tab)
3. How many labeled images? (Check "Overview" tab)

**Solution:**
- If no images: Upload images first
- If no labels: Label images first (at least 10-20)
- Train tab appears after you have labeled data

---

### "Train tab is there but grayed out/disabled"

**Reason:**
- Not enough labeled images (need minimum 50-100 recommended)
- Or training already in progress

**Solution:**
- Label more images
- Check if training is already running
- Wait for current training to finish

---

### "I can't find my project at all"

**Solution:**
1. Check left sidebar - click workspace selector
2. Look for "BTE Basketball Detection" in dropdown
3. Or use direct URL: `app.roboflow.com/bte-basketball-detection-v1`
4. Or go to Projects page and look for your project in list

---

## Quick Checklist

- [ ] I can see my project "BTE Basketball Detection"
- [ ] I'm in the project dashboard (see tabs at top)
- [ ] I can see "Overview" tab
- [ ] I can see "Upload" tab
- [ ] I can see "Annotate" tab
- [ ] I can see "Train" tab (if you have labeled data)
- [ ] If Train tab not visible, I need to label images first

---

## Next Steps Based on Your Status

### If You Have No Images:
1. Go to "Upload" tab
2. Upload basketball images/videos
3. Then go to "Annotate" tab
4. Label images
5. Then "Train" tab will appear

### If You Have Images But No Labels:
1. Go to "Annotate" tab
2. Click on an image
3. Draw bounding boxes and label
4. Label at least 10-20 images
5. "Train" tab will become active

### If You Have Labeled Images:
1. Go to "Train" tab (should be visible)
2. Configure training settings
3. Click "Start Training"

---

**The key: Training requires labeled data. If you don't see the Train tab, check if you have labeled images in the "Annotate" tab first!**




