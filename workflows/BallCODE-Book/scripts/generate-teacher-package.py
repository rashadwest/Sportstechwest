#!/usr/bin/env python3
"""
Generate Teacher Essentials Package
Creates complete teacher onboarding and resource package

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
TEACHER_DIR = PROJECT_ROOT / "documents" / "teacher-resources"
TEACHER_WEB_DIR = PROJECT_ROOT / "BallCode" / "teachers"

# Ensure directories exist
TEACHER_DIR.mkdir(parents=True, exist_ok=True)
TEACHER_WEB_DIR.mkdir(parents=True, exist_ok=True)

def generate_onboarding_guide():
    """Generate teacher onboarding guide."""
    content = f"""# BallCODE Teacher Onboarding Guide

**Version:** 1.0  
**Date:** {datetime.now().strftime('%B %d, %Y')}  
**Welcome to BallCODE!**

---

## 🎯 Welcome to BallCODE

Thank you for choosing BallCODE - where coding meets basketball! This guide will help you get started quickly and effectively.

---

## 📋 Quick Start (5 Minutes)

### Step 1: Access Your Account
1. You'll receive an email with your login credentials
2. Visit: [ballcode.co/teachers](https://ballcode.co/teachers)
3. Log in with your provided credentials

### Step 2: Set Up Your First Class
1. Click "Create Class" in your dashboard
2. Enter class name (e.g., "5th Grade Coding - Fall 2025")
3. Add student emails or share class code
4. Click "Create"

### Step 3: Assign First Episode
1. Go to "Episodes" in your dashboard
2. Click "Episode 1: The Simplest Move"
3. Click "Assign to Class"
4. Select your class
5. Set due date (optional)
6. Click "Assign"

### Step 4: Share with Students
1. Students will receive email invitations
2. Or share the class code: Students go to ballcode.co/join and enter code
3. Students can start Episode 1 immediately

**That's it! You're ready to go! 🚀**

---

## 📚 Understanding BallCODE

### What is BallCODE?
BallCODE is an educational system that teaches coding through basketball stories and interactive games.

### How It Works:
1. **Story First:** Students read an engaging basketball story
2. **Learn Concepts:** Coding concepts are woven into the narrative
3. **Practice:** Students play interactive games to practice
4. **Master:** Students master concepts through repetition

### The Learning Path:
- **Episode 1:** The Simplest Move (Variables & States)
- **Episode 2:** Coming Soon
- **Episode 3:** Coming Soon
- And more...

---

## 🎓 Episode 1: The Simplest Move

### Learning Objectives:
- Understand what variables are
- Learn about state management
- Practice with interactive exercises
- Apply concepts in game scenarios

### Curriculum Alignment:
- **CSTA Standards:** Variables and Data (1B-AP-10)
- **Common Core:** Mathematical Practices (MP.2, MP.4)
- **21st Century Skills:** Critical Thinking, Problem Solving

### Time Required:
- Story Reading: 10-15 minutes
- Exercise Practice: 5-10 minutes
- Total: 15-25 minutes per student

---

## 👥 Managing Your Class

### Adding Students:
1. Go to your class dashboard
2. Click "Add Students"
3. Enter student emails (one per line)
4. Click "Send Invitations"

### Monitoring Progress:
1. Go to your class dashboard
2. Click on a student's name
3. View their progress:
   - Story completion
   - Exercise attempts
   - Success rate
   - Time spent

### Providing Support:
- Students can ask questions in the built-in chat
- You'll receive notifications for student questions
- Respond directly in the dashboard

---

## 📊 Assessment & Grading

### What Gets Tracked:
- Story completion (did they read it?)
- Exercise completion (did they finish?)
- Exercise success (did they get it right?)
- Time spent (engagement level)

### Grading Options:
1. **Completion-Based:** Grade on completion only
2. **Performance-Based:** Grade on success rate
3. **Hybrid:** Combine completion and performance

### Recommended Approach:
- **Formative Assessment:** Use for practice and learning
- **Summative Assessment:** Use Episode completion as quiz grade
- **Portfolio:** Have students explain concepts in their own words

---

## 🎯 Best Practices

### Before Class:
1. **Preview Episode:** Read the story yourself first
2. **Test Exercise:** Try the exercise to understand it
3. **Prepare Questions:** Think about what students might ask
4. **Set Expectations:** Tell students what to expect

### During Class:
1. **Let Them Explore:** Give students time to read and play
2. **Be Available:** Answer questions as they come up
3. **Encourage Persistence:** Remind them it's okay to try multiple times
4. **Celebrate Success:** Acknowledge when students complete exercises

### After Class:
1. **Review Progress:** Check who completed and who didn't
2. **Follow Up:** Reach out to students who struggled
3. **Plan Next Steps:** Decide when to move to next episode

---

## 🆘 Troubleshooting

### Student Can't Access:
- **Check Email:** Make sure they received invitation
- **Check Class Code:** Verify they're using correct code
- **Check Browser:** Recommend Chrome or Firefox
- **Contact Support:** Email schools@ballcode.co

### Exercise Not Working:
- **Check Internet:** Ensure stable connection
- **Try Different Browser:** Sometimes browser issues
- **Clear Cache:** Have student clear browser cache
- **Contact Support:** Email schools@ballcode.co

### Student Struggling:
- **Encourage Persistence:** Remind them it's okay to try again
- **Review Story:** Have them re-read relevant parts
- **Provide Hints:** Give subtle guidance without giving answers
- **Pair Up:** Have them work with a partner

---

## 📞 Support Resources

### Getting Help:
- **Email:** schools@ballcode.co
- **Response Time:** Within 24 hours
- **Priority:** Teachers get priority support

### Documentation:
- **Teacher Dashboard:** ballcode.co/teachers
- **Student Guide:** ballcode.co/students
- **FAQ:** ballcode.co/faq

### Community:
- **Teacher Forum:** Coming soon
- **Best Practices:** Coming soon
- **Success Stories:** Coming soon

---

## 🚀 Next Steps

1. **Complete Quick Start** (5 minutes)
2. **Assign Episode 1** to your class
3. **Monitor Progress** in your dashboard
4. **Provide Support** as needed
5. **Celebrate Success** with your students!

---

## 📝 Quick Reference

### Important Links:
- Teacher Dashboard: ballcode.co/teachers
- Student Portal: ballcode.co/students
- Support Email: schools@ballcode.co

### Key Concepts:
- **Story First:** Always start with the story
- **Practice Makes Perfect:** Encourage multiple attempts
- **Learning Takes Time:** Be patient with students
- **Celebrate Progress:** Acknowledge every step forward

---

**Welcome to BallCODE! We're here to support you every step of the way.**

**Questions? Email: schools@ballcode.co**

---

*Generated: {datetime.now().strftime('%B %d, %Y')}*
"""
    
    file_path = TEACHER_DIR / "Teacher-Onboarding-Guide.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {file_path}")
    return file_path

def generate_quick_start():
    """Generate 5-minute quick start guide."""
    content = f"""# BallCODE Quick Start Guide (5 Minutes)

**Get your class started in 5 minutes!**

---

## ⚡ 5-Minute Setup

### 1. Log In (1 minute)
- Go to: ballcode.co/teachers
- Use your provided credentials
- Click "Log In"

### 2. Create Class (1 minute)
- Click "Create Class"
- Enter class name
- Click "Create"
- Copy the class code

### 3. Assign Episode 1 (1 minute)
- Click "Episodes"
- Click "Episode 1"
- Click "Assign to Class"
- Select your class
- Click "Assign"

### 4. Share with Students (2 minutes)
- Share class code with students
- Or add student emails
- Students can start immediately!

**Done! 🎉**

---

## 📱 Student Access

Students can join in two ways:

### Option 1: Class Code
1. Go to: ballcode.co/join
2. Enter class code
3. Start learning!

### Option 2: Email Invitation
1. Check email for invitation
2. Click "Join Class"
3. Start learning!

---

## 🎯 What Students Will Do

1. **Read Story** (10-15 min)
   - Engaging basketball narrative
   - Coding concepts woven in

2. **Play Exercise** (5-10 min)
   - Interactive practice
   - Immediate feedback

3. **Master Concept** (Repeat as needed)
   - Try multiple times
   - Learn through practice

---

## 📊 Monitor Progress

- Go to your class dashboard
- See who's completed
- See who needs help
- Provide support as needed

---

## 🆘 Need Help?

- Email: schools@ballcode.co
- Response: Within 24 hours

---

**That's it! You're ready to go! 🚀**

*Generated: {datetime.now().strftime('%B %d, %Y')}*
"""
    
    file_path = TEACHER_DIR / "Teacher-Quick-Start.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {file_path}")
    return file_path

def generate_first_day_lesson_plan():
    """Generate first day lesson plan."""
    content = f"""# First Day Lesson Plan: Episode 1

**Time:** 30-45 minutes  
**Grade Level:** 4th-8th grade  
**Subject:** Coding through Basketball

---

## 🎯 Learning Objectives

By the end of this lesson, students will:
- Understand what BallCODE is
- Access their BallCODE account
- Complete Episode 1: The Simplest Move
- Understand basic coding concepts (variables, states)

---

## 📋 Materials Needed

- Computer or tablet for each student
- Internet connection
- BallCODE accounts (set up before class)
- Projector/screen (optional, for demonstration)

---

## ⏱️ Lesson Timeline

### Introduction (5 minutes)
**What to Say:**
"Today we're starting something exciting - BallCODE! This is a new way to learn coding through basketball stories and games. You'll read stories about basketball players and learn coding at the same time. Let's get started!"

**Activity:**
- Show BallCODE website on projector
- Demonstrate how to log in
- Show what Episode 1 looks like

---

### Getting Started (5 minutes)
**What to Do:**
1. Have students go to ballcode.co/join
2. Enter class code (write on board)
3. Students create accounts or log in
4. Help any students who need assistance

**Check:**
- All students logged in?
- All students see Episode 1?
- Any technical issues?

---

### Reading the Story (10-15 minutes)
**What to Say:**
"Now you're going to read Episode 1: The Simplest Move. This is a story about a basketball player named Nova who learns an important lesson. As you read, pay attention to the coding concepts. You'll use them in the exercise later."

**Activity:**
- Students read story independently
- Walk around and check progress
- Answer questions as they come up

**Check:**
- Are students reading?
- Do they understand the story?
- Any questions about concepts?

---

### Playing the Exercise (10-15 minutes)
**What to Say:**
"Now you're going to play the exercise. This is where you practice what you learned in the story. Don't worry if you don't get it right the first time - you can try as many times as you need. The goal is to learn, not to be perfect."

**Activity:**
- Students play exercise
- Walk around and provide encouragement
- Help students who are stuck (but don't give answers)

**Check:**
- Are students engaged?
- Are they making progress?
- Who needs extra help?

---

### Wrap-Up (5 minutes)
**What to Say:**
"Great job today! You've completed your first episode of BallCODE. How did it go? What did you learn? What was challenging? What was fun?"

**Activity:**
- Quick discussion about experience
- Answer any final questions
- Remind them they can continue at home

**Check:**
- Did students enjoy it?
- Do they understand what's next?
- Any concerns or questions?

---

## 🎯 Assessment

### Formative (During Lesson):
- Are students engaged?
- Are they making progress?
- Do they understand concepts?

### Summative (After Lesson):
- Check dashboard for completion
- See who finished story
- See who completed exercise
- Follow up with students who didn't finish

---

## 🆘 Troubleshooting

### Student Can't Log In:
- Check class code
- Verify email invitation
- Contact support: schools@ballcode.co

### Exercise Not Working:
- Check internet connection
- Try different browser
- Clear browser cache

### Student Struggling:
- Encourage persistence
- Remind them to re-read story
- Provide hints (not answers)
- Pair with another student

---

## 📝 Notes

**What Went Well:**
- [Write notes here]

**What to Improve:**
- [Write notes here]

**Student Feedback:**
- [Write notes here]

**Next Steps:**
- [Write notes here]

---

## 🚀 Extension Activities

### For Fast Finishers:
- Have them explain concepts to a partner
- Have them write their own story using concepts
- Have them help other students

### For Struggling Students:
- Re-read story together
- Break down exercise into smaller steps
- Provide one-on-one support

---

**Good luck with your first BallCODE lesson! 🎉**

*Generated: {datetime.now().strftime('%B %d, %Y')}*
"""
    
    file_path = TEACHER_DIR / "First-Day-Lesson-Plan.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {file_path}")
    return file_path

def generate_teacher_resources_page():
    """Generate teacher resources HTML page."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teacher Resources - BallCODE</title>
    <link rel="stylesheet" href="/css/style.css">
    <style>
        .teacher-resources {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .resource-card {{
            background: white;
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .resource-card h2 {{
            color: #eb6123;
            margin-bottom: 1rem;
        }}
        .resource-card p {{
            color: #666;
            margin-bottom: 1rem;
        }}
        .resource-link {{
            display: inline-block;
            background: #eb6123;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 1rem;
        }}
        .resource-link:hover {{
            background: #d4551a;
        }}
    </style>
</head>
<body>
    <div class="teacher-resources">
        <h1>👨‍🏫 Teacher Resources</h1>
        <p>Everything you need to get started with BallCODE in your classroom.</p>
        
        <div class="resource-card">
            <h2>📚 Onboarding Guide</h2>
            <p>Complete guide to getting started with BallCODE, managing your class, and supporting your students.</p>
            <a href="/documents/teacher-resources/Teacher-Onboarding-Guide.md" class="resource-link">Download Guide</a>
        </div>
        
        <div class="resource-card">
            <h2>⚡ Quick Start (5 Minutes)</h2>
            <p>Get your class up and running in just 5 minutes with this quick start guide.</p>
            <a href="/documents/teacher-resources/Teacher-Quick-Start.md" class="resource-link">Download Quick Start</a>
        </div>
        
        <div class="resource-card">
            <h2>📅 First Day Lesson Plan</h2>
            <p>Ready-to-use lesson plan for your first BallCODE class. Includes timeline, activities, and assessment.</p>
            <a href="/documents/teacher-resources/First-Day-Lesson-Plan.md" class="resource-link">Download Lesson Plan</a>
        </div>
        
        <div class="resource-card">
            <h2>📞 Support</h2>
            <p>Need help? We're here for you!</p>
            <p><strong>Email:</strong> schools@ballcode.co</p>
            <p><strong>Response Time:</strong> Within 24 hours</p>
        </div>
    </div>
</body>
</html>
"""
    
    file_path = TEACHER_WEB_DIR / "index.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Created: {file_path}")
    return file_path

def main():
    """Generate teacher package."""
    print("=" * 60)
    print("📦 BallCODE Teacher Package Generator")
    print("=" * 60)
    print()
    
    print("📝 Generating teacher resources...")
    print()
    
    # Generate all resources
    generate_onboarding_guide()
    generate_quick_start()
    generate_first_day_lesson_plan()
    generate_teacher_resources_page()
    
    print()
    print("=" * 60)
    print("✅ Teacher Package Generated Successfully!")
    print("=" * 60)
    print()
    
    print("📋 Generated Files:")
    print(f"  1. Onboarding Guide: {TEACHER_DIR / 'Teacher-Onboarding-Guide.md'}")
    print(f"  2. Quick Start: {TEACHER_DIR / 'Teacher-Quick-Start.md'}")
    print(f"  3. First Day Lesson Plan: {TEACHER_DIR / 'First-Day-Lesson-Plan.md'}")
    print(f"  4. Teacher Resources Page: {TEACHER_WEB_DIR / 'index.html'}")
    print()
    
    print("🚀 Next Steps:")
    print("  1. Review generated resources")
    print("  2. Customize as needed for your school")
    print("  3. Share with teachers")
    print("  4. Link teacher resources page from main website")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


