# Roboflow Training Guide - Getting Started

**Platform:** Roboflow (app.roboflow.com)  
**Project:** BTE Basketball Detection  
**Goal:** Train a computer vision model for basketball detection

---

## Understanding the Roboflow Workflow

### The Process (In Order):
1. **Create Project** → 2. **Upload Data** → 3. **Label Data** → 4. **Train Model** → 5. **Deploy**

You're currently at **Step 1** - you need to create a project first before you can train.

---

## Step 1: Create a New Project

### What You See Now:
- The Projects tab shows an introductory page
- "+ New Project" button is visible
- No existing projects listed (because you haven't created one yet)

### What to Do:

1. **Click the "+ New Project" button** (large purple button in center)

2. **Fill in Project Details:**
   - **Project Name:** e.g., "Basketball Player Detection" or "Basketball State Detection"
   - **Project Type:** Choose based on what you want to detect:
     - **Object Detection** - Detect players, ball, court elements (bounding boxes)
     - **Keypoint Detection** - Detect body parts, joints (like the example shown)
     - **Classification** - Classify images into categories
     - **Instance Segmentation** - Detect and segment objects
   
   - **Workspace:** Should already be set to "BTE Basketball De..." (your current workspace)

3. **Click "Create Project"**

---

## Step 2: Upload Your Data

### After Creating Project:

1. **You'll see the project dashboard**
   - This is where your project lives

2. **Upload Images:**
   - Click "Upload" or drag and drop images
   - Upload basketball footage/images
   - Roboflow accepts: JPG, PNG, video files

3. **Organize Your Dataset:**
   - Images will appear in your project
   - You can organize into folders if needed

---

## Step 3: Label Your Data

### This is Where You Annotate:

1. **Go to "Annotate" Tab** (in your project)
   - This is where you label your images

2. **For Object Detection:**
   - Draw bounding boxes around objects
   - Label each box (e.g., "player", "ball", "court")
   - Repeat for all images

3. **For Keypoint Detection:**
   - Mark keypoints on players (joints, body parts)
   - Label each keypoint
   - Connect keypoints if needed

4. **Label Multiple Images:**
   - Go through your dataset
   - Label consistently
   - More labels = better model

---

## Step 4: Train Your Model (This is What You're Looking For!)

### Training Appears After You Have Labeled Data:

1. **Go to "Train" Tab** (in your project)
   - This tab appears AFTER you've labeled some images
   - You need at least some labeled data to train

2. **Configure Training:**
   - **Model Type:** Choose (YOLOv8, YOLOv5, etc.)
   - **Training Steps:** Set number of epochs
   - **Batch Size:** Adjust if needed
   - **Image Size:** Set resolution

3. **Start Training:**
   - Click "Start Training" button
   - Roboflow will train your model
   - This takes time (minutes to hours depending on dataset)

4. **Monitor Training:**
   - Watch training progress
   - See metrics (loss, accuracy)
   - Wait for completion

---

## Why You Don't See Training Yet

### The Issue:
- **Training tab only appears AFTER you:**
  1. Create a project ✅ (you're here)
  2. Upload images ⚠️ (need to do this)
  3. Label at least some images ⚠️ (need to do this)
  4. Then training becomes available ✅

### Current Status:
- ✅ You're in Roboflow
- ✅ You're in the Projects tab
- ⚠️ You haven't created a project yet
- ⚠️ No data uploaded
- ⚠️ No labels created
- ❌ Training not available (because no labeled data)

---

## Quick Start Guide

### Right Now (5 Minutes):

1. **Click "+ New Project"**
   - Large purple button in center

2. **Create Project:**
   - Name: "Basketball Detection" (or your choice)
   - Type: "Object Detection" (most common for basketball)
   - Click "Create"

3. **You'll Now See Your Project Dashboard**

### Next Steps (After Project Created):

4. **Upload Images:**
   - Click "Upload" in your project
   - Add basketball images/videos
   - Wait for upload to complete

5. **Start Labeling:**
   - Go to "Annotate" tab
   - Draw bounding boxes on first few images
   - Label them (e.g., "player", "ball")

6. **Train Model:**
   - After labeling some images, "Train" tab appears
   - Click "Train" tab
   - Configure settings
   - Click "Start Training"

---

## Project Dashboard Navigation

### After Creating Project, You'll See:

**Top Tabs:**
- **Overview** - Project stats and info
- **Upload** - Upload new images
- **Annotate** - Label your images (THIS IS KEY!)
- **Train** - Train your model (appears after labeling)
- **Deploy** - Deploy trained model
- **Settings** - Project settings

**The "Train" Tab:**
- Only appears after you've labeled some data
- This is where you configure and start training
- You'll see training options and "Start Training" button

---

## Common Questions

### Q: Why is the Projects tab empty?
**A:** You haven't created a project yet. Click "+ New Project" to start.

### Q: Where is the training button?
**A:** Training appears in the "Train" tab AFTER you:
1. Create a project
2. Upload images
3. Label at least some images

### Q: How many images do I need?
**A:** 
- Minimum: 50-100 labeled images
- Recommended: 200+ labeled images
- More = better model performance

### Q: How long does training take?
**A:**
- Small dataset (50-100 images): 10-30 minutes
- Medium dataset (200-500 images): 30-60 minutes
- Large dataset (1000+ images): 1-3 hours

### Q: What if I don't have images yet?
**A:** You can:
- Use Roboflow's public datasets
- Upload basketball videos (Roboflow can extract frames)
- Start with a few images and add more later

---

## Step-by-Step: From Empty to Training

### Step 1: Create Project (2 minutes)
1. Click "+ New Project"
2. Enter project name
3. Select project type (Object Detection recommended)
4. Click "Create"

### Step 2: Upload Data (10-30 minutes)
1. In your project, click "Upload"
2. Drag and drop images OR click to browse
3. Wait for upload
4. Images appear in your project

### Step 3: Label Data (1-3 hours, depending on dataset)
1. Click "Annotate" tab
2. Click on an image
3. Draw bounding boxes around objects
4. Label each box
5. Save and move to next image
6. Repeat for all images (or at least 50-100 to start)

### Step 4: Train Model (Now Available!)
1. Click "Train" tab (now visible!)
2. Configure training settings
3. Click "Start Training"
4. Wait for training to complete
5. Review results

---

## Tips for Success

### For Basketball Detection:

1. **Start Small:**
   - Upload 50-100 images first
   - Label them
   - Train a quick model
   - See if it works
   - Then add more data

2. **Label Consistently:**
   - Use same labels throughout
   - Be precise with bounding boxes
   - Label all relevant objects

3. **Use Good Images:**
   - Clear, well-lit basketball footage
   - Various angles and situations
   - Different players/teams

4. **Iterate:**
   - Train model
   - Test on new images
   - Find what it misses
   - Add more labeled data
   - Retrain

---

## What You Should Do Right Now

### Immediate Action (Next 5 Minutes):

1. ✅ **Click "+ New Project" button**
2. ✅ **Create your project:**
   - Name: "Basketball Detection" (or your choice)
   - Type: "Object Detection"
   - Click "Create"
3. ✅ **You'll now see your project dashboard**

### Then (Next 30 Minutes):

4. ✅ **Upload some images:**
   - Click "Upload" in your project
   - Add basketball images/videos
5. ✅ **Start labeling:**
   - Click "Annotate" tab
   - Label at least 10-20 images to start
6. ✅ **Training will appear:**
   - After labeling, "Train" tab becomes available
   - Click it to start training

---

## Troubleshooting

### "Train Tab Not Showing"
**Solution:** You need to label at least some images first. Go to "Annotate" tab and label a few images, then "Train" tab will appear.

### "No Images to Label"
**Solution:** Go to "Upload" tab and add images to your project first.

### "Training Takes Too Long"
**Solution:** This is normal. Training can take 30 minutes to several hours depending on your dataset size. Be patient, it's working!

### "Model Not Accurate"
**Solution:** 
- Add more labeled images
- Label more consistently
- Use better quality images
- Retrain with more data

---

## Next Steps

1. **Create your project** (click "+ New Project")
2. **Upload basketball images**
3. **Label your images** (this unlocks training)
4. **Train your model** (now you'll see the Train tab!)
5. **Test and iterate**

---

**The key is: Training appears AFTER you create a project, upload data, and label it. Start with "+ New Project" and work through the steps! 🚀**




