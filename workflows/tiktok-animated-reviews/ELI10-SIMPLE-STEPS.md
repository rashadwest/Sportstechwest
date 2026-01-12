# ELI10: Everything You Need to Do (Super Simple!)

**Like explaining to a 10-year-old - super easy steps!**

---

## 🎯 What You're Building

You're making a robot that:
1. Takes a TikTok video
2. Adds your animated character talking
3. Uses your voice to say things
4. Makes a cool reaction video

**That's it!** The robot does everything else automatically.

---

## 📝 Step 1: Get Your Voice Key (5 minutes)

**What:** You need a special password to make your voice work

**How:**
1. Go to this website: https://elevenlabs.io
2. Click "Sign Up" (make an account - it's free!)
3. After you sign up, click on your name (top right)
4. Click "API Keys"
5. Copy the long password you see (it looks like: `sk-1234567890abcdef...`)

**Save it somewhere safe!** You'll need it later.

**Why:** This password lets the robot use your voice

---

## 🎤 Step 2: Record Your Voice (10 minutes)

**What:** Record yourself talking for 1-2 minutes

**How:**
1. Open QuickTime on your Mac (or use your phone)
2. Click "New Audio Recording"
3. Press the red record button
4. Talk for 1-2 minutes about anything (like explaining something you like)
5. Press stop
6. Save it as "my_voice.mp3"

**Then:**
1. Go to: `workflows/tiktok-animated-reviews/assets/voice_samples/`
2. Put your "my_voice.mp3" file there

**Why:** The robot needs to hear your voice so it can copy it

---

## 🎨 Step 3: Get Your Characters (1-2 hours)

**What:** You need 3 animated characters (like cartoon versions of you)

**Where to get them:**
- From your Instagram: https://www.instagram.com/p/DQxNseoEdnE/
- Or make them in an animation program
- Or use AI to create them

**What you need:**
1. **Youth character** - A younger version (for kids' videos)
2. **Adult character** - You (for grown-up videos)
3. **Robot character** - A robot (for robot videos)

**How to save them:**
1. Go to: `workflows/tiktok-animated-reviews/assets/characters/`
2. Make 3 folders: `youth`, `adult`, `robot`
3. Put each character file in its folder
4. Name them: `character.mp4` (or `.png` if it's pictures)

**Why:** The robot needs characters to show on screen

**Tip:** Start with just ONE character to test! You can add the others later.

---

## 🤖 Step 4: Let the Robot Set Everything Up (5 minutes)

**What:** Run a magic script that does all the boring setup

**How:**
1. Open Terminal (on your Mac)
2. Type this and press Enter:
   ```bash
   cd workflows/tiktok-animated-reviews
   python3 setup_wizard.py
   ```
3. Answer the questions it asks:
   - Paste your API key (from Step 1)
   - Tell it where your voice file is
   - Tell it where your characters are
4. The robot does everything else!

**Why:** This saves you from doing boring computer stuff

---

## ✅ Step 5: Test It! (5 minutes)

**What:** Make sure everything works

**How:**
1. Get a test TikTok video (any short video)
2. Write a test script (just a few sentences)
3. Run this command:
   ```bash
   python3 src/pipeline/review_pipeline.py \
     --tiktok-video test.mp4 \
     --script test.txt \
     --config config/my_config.json \
     --auto-select-character
   ```
4. Wait a few minutes
5. Check the output folder - you should see your video!

**Why:** Testing makes sure everything works before you use it for real

---

## 🎉 That's It!

**After these 5 steps, you're done!**

The robot will:
- ✅ Automatically pick the right character
- ✅ Use your voice
- ✅ Make the video
- ✅ Fix any problems that come up

**You just need to:**
- Give it a TikTok video
- Give it a script (what to say)
- Let it do its magic!

---

## 📋 Quick Checklist

**Do these in order:**

- [ ] **Step 1:** Get API key from elevenlabs.io (5 min)
- [ ] **Step 2:** Record your voice, save it (10 min)
- [ ] **Step 3:** Get at least one character, save it (30 min - 2 hrs)
- [ ] **Step 4:** Run `python3 setup_wizard.py` (5 min)
- [ ] **Step 5:** Test with a sample video (5 min)

**Total time: About 1-3 hours** (mostly getting characters)

---

## 🆘 If Something Goes Wrong

**The robot is smart!** It will:
- Tell you exactly what's wrong
- Try again if something fails
- Give you ideas on how to fix it

**Just read the messages it shows you!**

---

## 💡 Pro Tips

1. **Start simple:** Get ONE character first, test it, then add the others
2. **Use the wizard:** The setup wizard does most of the work for you
3. **Test early:** Test with a simple video first
4. **Read the messages:** The robot tells you what to do if something's wrong

---

## 🎯 What Happens After Setup

**Once everything is set up:**

1. You find a TikTok video you want to react to
2. You write a script (what you want to say)
3. You run one command
4. The robot:
   - Picks the right character (youth/robot/adult)
   - Uses your voice
   - Makes the video
   - Saves it for you

**That's it!** Super easy after setup.

---

## 📚 Need More Help?

- **Full guide:** `STEP-BY-STEP-ACTION-PLAN.md`
- **What you need:** `MANUAL-STEPS-ONLY.md`
- **Priority order:** `PRIORITY-ORDER.md`
- **System ready?:** `SYSTEM-READY.md`

---

**Remember:** The robot does almost everything automatically. You just need to give it:
1. Your voice key (password)
2. Your voice recording
3. Your characters

**Everything else is automatic!** 🚀

