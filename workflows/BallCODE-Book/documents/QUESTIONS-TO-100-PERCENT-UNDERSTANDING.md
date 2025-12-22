# Questions to Get to 100% Understanding
## Consolidated List for Complete BallCODE System Knowledge

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Purpose:** All questions needed to reach 100% understanding  
**Status:** 🎯 Ready for Answers

---

## 🚨 CRITICAL PRIORITY (Blocking Integration)

### Game System - Unity Code Structure

1. **BallCODEStarter.cs:**
   - Can you show me the complete BallCODEStarter.cs code?
   This should be in the github
   - How does it receive URL parameters in Unity WebGL builds?
   I thought we are now developing this framework. We are the new devs
   - What happens if URL parameters are missing or invalid?
   We have to develop a plan/system
   - How does it initialize the game mode?
   We are able to come up with this ideation using our gaming expert
   - What error handling exists?
   We have the github but we probably need to create something esle as well. 

2. **GameModeManager.cs:**
   - Can you show me the complete GameModeManager.cs code?
   This should be in github
   - How does it load exercises (from where? JSON, ScriptableObjects, hardcoded?)?
   I am not sure lets look into it and find out. 
   - What game modes exist (block coding, Python, story mode, etc.)?
   Tutorial, Coding, Math, Chess, Freeplay
   - How does it switch between game modes?
   You have to go to the main menu to switch
   - How does it handle exercise data structure?
   The data is not saved currently but I would love to save student data for research purposes with consent

3. **URL Parameter System:**
   - What is the EXACT URL parameter format?
   - Example: `ballcode.co/play?book=1&exercise=foundation-block&source=book` - is this correct?
   Currently the game is on the netlify account and not directly connected to the website. 
   - How does Unity WebGL receive these parameters (Application.absoluteURL, JavaScript bridge, etc.)?
   I am not sure this is for us to determine as I created a new account
   - What happens if parameters are malformed?
   We need to figure this out
   - What are all possible parameter values?
   We need to figure this out 

4. **Exercise System:**
**Everything here needs to be discovered by R&D through AIMCODE
   - What is the exercise data structure?
   - Where is exercise data stored (StreamingAssets, Resources, ScriptableObjects, JSON files)?
   - How is exercise completion detected?
   - What happens when user completes an exercise?
   - How is exercise progress tracked?

5. **Game-to-Book Return Flow:**
   - How does game communicate completion back to book/website?
   Book does not need to communicate with the website. The website is merely a funnal to go go to the book. 
   - What data is sent back (completion status, score, time, etc.)?
   This would be cool to put in the roadmap
   - What mechanism is used (JavaScript bridge, localStorage, API call, URL redirect)?
   We need to ask the experts on what would be best 
   - How does book/website receive this data?
   Data questions all need to be thought about on the roadmap with a dashboard concept. Save this to memory for all data questions
   - What happens if communication fails?
   We need to have a system that knows what happened and is logged for fixing using AIMCODE. 

---

### Integration Technical Details

6. **Data Flow:**
**Everything here needs to be discovered by R&D through AIMCODE
   - How does website pass data to game (URL parameters only, or other methods)?
   - How does game return data to website (exact mechanism)?
   - What data flows in each direction?
   - Are there any APIs or endpoints involved?
   - How is data formatted (JSON, query strings, etc.)?

7. **Progress Tracking:**
   - How is user progress tracked?
   I think it would be great to have a daily log but we can put this in the roadmap!
   - Where is progress stored (localStorage, database, cookies, etc.)?
   We need to figure this out with our experts
   - How is progress retrieved and displayed?
   We need to figure this out but for now it is just on the roadmap. 
   - What progress data is tracked (books completed, exercises completed, scores, etc.)?
   We want it on the roadmap that all will be tracked.
   - How does progress sync across systems?
   All in a comprehensive dashboard and this is on the roadmap

8. **Integration Points:**
**Everything here needs to be discovered by R&D through AIMCODE
   - What APIs/endpoints exist for integration?
   - How does website know game is complete?
   The website really does not need to know yet. It is merely a operator right now. It tells the user where to go and what to do. 
   - How does book know game is complete?
   The book will not know. They will just go to the next level. The book does not need to be smart like this. 
   - How does curriculum track progress?
   We need to look at what books were read and what game modes were completed. We may need to make it where they have to unlock the game mode by competeing the book. I think this would be a cool way to hold them accountable for reading in order to play the game. 
   - What triggers "next book" recommendation?
   WHen a book then game is completed if it is possible with our current configuration

---

## ⚠️ HIGH PRIORITY (Important for Quality)

### Game Modes & Systems

9. **Block Coding Mode:**
   - How does the block coding system work?
   A robot moves block to block with commands with a goal of mimicing the video of the player given. This is the current model
   The only difference is when it comes to math that is all about the formula given that you are executing using the number system and a algerba equation and chess that is a strategy game 1 vs 1. 
   - What blocks are available for each book/exercise?
   The tutorial is where we are starting because we have a full development. You can check the code to see but we have exercises for each dribble
   - How are blocks executed in the game?
   You have to give the robot a command by clicking on the block and then selecting the dribble, action before shot, or shot for tutorial. 
   For freeplay action for shot is selected first, and then you have to select dribbles and when the shot is taken
   FOr coding it is about coding everything after you place the robot and then the block code is used for the robot to move throughout the game (think scratch game developed by MIT)
   The turn based game and math are mostly moving like the turtorial but math only has certain actions you can do because you have to equal the amount you are looking to accomplish
   - What feedback does user receive?
   We need to work through this because it is mostly "nice shot!" type of feedback right now
   - How is block code validated?
   It is said by us what the robot is going to do before he does it. 

10. **Python Mode:**
**Everything here needs to be discovered by R&D through AIMCODE. We have not talked about this at all it was just a thought to make this more practical for serious programmers or people who want to be deve. 
    - Is Python mode implemented?
    - How does Python code execution work?
    - What Python runtime is used?
    - How is Python code validated?
    - What feedback does user receive?

11. **Game Modes:**
    - What game modes exist (list all)?
    Coding, Tutorial, Chess, Math, Freeplay
    - How do modes differ from each other?
    Tutorial - tells you how to play 
    Coding - lets you use block code to move robot
    Chess - The ability to play against someone else
    Freeplay - Unlimited moves similar to freeplay just to play around
    Math - Just like tutorial but you are doing math
    - How does user switch between modes?
    You have to go to the home screen to select a specific mode. 
    - What modes are available for each book?
    WE need to make the books for each mode not the other way around. 

12. **Exercise Structure:**
**Everything here needs to be discovered by R&D through AIMCODE
    - What is the complete exercise data structure?
    - What fields/properties does each exercise have?
    - How are exercises organized (by book, by concept, by difficulty)?
    It just goes by dribble in the tutorial so we have not really developed this system all the way out. I do have a doc I can share for what I was thinking. 
    - How are exercises loaded into the game?
    We need to look at the github and figure out how this is. 

---

### User Experience

13. **User Journey:**
    - What does user see at each step of the journey?
    They go to the website, select a book, finish the book and then go to the coding excercise and then they are done for the day. If they want they can go to the website and just do a game coding excercise or just play the game. Does this make sense?
    - Can you provide screenshots or mockups of each step?
    See the screenshots that were shared and use the mechanism you used last time to figure out what each thing is doing and how it works. 
    - What feedback does user receive at each step?
    We need to add some of this to it. Right now only the tutorial gives step by step feedback. The only other feedback is nice shot or missed shot. 
    - How does user know what to do next?
    It should instruct them we need to add these features. 
    - What happens in edge cases (user skips steps, errors occur, etc.)?
    We need to have guardrails so that they do not do this. To protect the integraty of the game and to make it a good user experience. 

14. **Book-to-Game Transition:**
    - What does user see when clicking "Try the Exercise" button?
    We need to figure this out as I think it would be cool to see how the book and the exercise work and what they will be learning
    - How seamless is the transition?
    It should be simple. Everything should be withiin the fully integrated model. Lets make sure we know that this is ELI10 wih the functionality 
    - Does game load in same window or new window?
    It is in a new window for now. We can eventually make them the same. Put this on the roadmap and make it seamless. 
    - What loading states exist?
    Really just when loading the game initially. 
    - What happens if game fails to load?
    I have not seen this but we need to create a safety net. 

15. **Game-to-Book Return:**
    - What does user see when exercise completes?
    Nice shot! or Missed shot 
    - How does user return to book?
    They have to go back to the website now. The book reads to you and you read along with the pictures so they should finish most of the time. 
    - What feedback is shown on book page after completion?
    We need to think about this and we should make this optional as duolingo is fun because everything is moslty within the book or game and that makes it good. 
    - How is progress displayed?
    We should have a dashboard eventually but right now lets focus on building out our system. 
    - What happens if return flow fails?
    We need to create safeguards and guardrails so it wont and if it does we have them redirected. 

---

## 📊 MEDIUM PRIORITY (Nice to Know)

### n8n & Automation

16. **Current Build Process:**
    - What currently happens after each hourly build?
    We need to have a quick test of what was built to make sure that it worked. 
    - What automated testing exists (if any)?
    Nothing that I am aware of as of now
    - How are bugs currently detected?
    I have weekly audits and ask for end to end tests 
    - What guardrails currently exist?
    We do not have any that I know of outside of the rules
    - What monitoring/logging exists?
    We are currently not logging much at all but we have a database setup that we can use 

17. **Build System:**
    - How does Unity build process work?
    Unity build needs rules, parameters, and guides along with using our rules. We need to make sure it is looking at it from a gamers perspecitive and makign sure that the process is building it for an optimal user experience. 
    - What happens during build?
    We are putting in new levels or editing UI/UX to make the game better. 
    - What could go wrong during build?
    If you dont know what you are doing you could build something that is not good.Lets make sure we save each build so we can always go back or revert back
    - How are build errors handled?
    They are logged and then we have a clear system on how to handle them being developed with robot. 
    - What build artifacts are created?
    This is a question for our AI.

---

### Curriculum Integration

18. **Curriculum System:**
    - How does curriculum track learning objectives?
    - How does curriculum recommend next book?
    - What curriculum data structure exists?
    - How does curriculum integrate with game?
    - How does curriculum integrate with books?

19. **Progression Logic:**
    - What determines book unlock?
    - What determines exercise unlock?
    - How is prerequisite tracking handled?
    - What happens if user skips prerequisites?

---

## 🔍 DETAILED TECHNICAL QUESTIONS

### Unity-Specific

20. **Unity Architecture:**
**Everything here needs to be discovered by R&D through AIMCODE
    - What Unity version is being used?
    - What is the scene structure?
    - What Unity systems are in place (UI, Input, Audio, etc.)?
    - What third-party packages/plugins are used?
    - What is the project folder structure?

21. **WebGL-Specific:**
**Everything here needs to be discovered by R&D through AIMCODE
    - How does Unity WebGL handle URL parameters?
    - What JavaScript interop is used?
    - How does WebGL communicate with browser?
    - What WebGL limitations affect the game?
    - How is WebGL build optimized?

22. **Code Structure:**
**Everything here needs to be discovered by R&D through AIMCODE
    - What is the overall code architecture?
    - What design patterns are used (Singleton, Observer, etc.)?
    - How is code organized (folders, namespaces)?
    - What dependencies exist between scripts?
    - What is the initialization order?

---

### Integration-Specific

23. **Website Integration:**
**Everything here needs to be discovered by R&D through AIMCODE
    - How does website generate game URLs?
    - What JavaScript is used on website?
    - How does website handle game completion?
    - What website APIs exist?
    - How does website track user sessions?

24. **Book Integration:**
**Everything here needs to be discovered by R&D through AIMCODE
    - How does book page generate game link?
    - What data does book pass to game?
    - How does book receive completion data?
    - What book APIs exist?
    - How does book display progress?

---

## 🎯 BUILD-MEASURE-LEARN QUESTIONS

25. **Daily Build Priorities:**
    - What should we build each day this week?
    New levels mostly copying the current levels and adding or changing the video and the blocks to go with a particular move of a player. I can give you the moves or you can just say which move it is you are using and with what hands and I can find a move of a player doing that. 
    - What is the priority order?
    I think Chess is the hardest so leave that to last. 
    Coding and Math new level should be priority. Math is really easy because it does not need videos so maybe a bunch of math levles first along with the UI/UX. 
    Then we go to coding and chess. 
    - What dependencies exist between tasks?
    Use AIMCODE to think this through 
    - What can be built in parallel?
    Give me suggestions

26. **Progress Metrics:**
    - What metrics matter most for progress?
    Daily streaks and if they are learning and their progress. 
    - How should we measure daily progress?
    Rather the game is improving for sales to schools because it is functional and the kids like using it. 
    - What indicates we're on track for playable game?
    If I can play each level with a kid and we are progressing within the game. We need to figure out other elements of it. 
    - What are the success criteria for each day?
    Have we gotten better from the previous day?

27. **Learning & Application:**
    - How should we capture learnings each day?
    We should log it. 
    - How should we apply learnings to next day?
    We should log what we learned and apply our lessons
    - What patterns should we look for?
    How well they are learning and retaining information and how we can make it better
    - How do we know if approach is working?
    I will have users testing it if we can get out the content in the way I think we can. 

---

## 🎓 EXPERT CONSULTATION QUESTIONS

### For Working with Experts

28. **User Experience (Jobs + Zhang):**
    - Does the integration "just work" from user perspective?
    Yes
    - Does the journey feel story-driven or system-driven?
    story driven would be dope expecially so it does not feel like school
    - What would make it simpler and more beautiful?
    The ability to make it where it feels like a game at all times and if we make the UI/UX better 
    - What would make concepts emerge more naturally from narrative?
    I have to write from the perspective of being a kid and what they like or think about so getting in that frame of mind and you giving me outlines that puts me in that mindset. 

29. **Building Experience (Resnick):**
    - Is building experience central to integration?
    Yes, I want the kids to build on their learning and enjoy it. 
    - Does game enable hands-on creation?
    I think it will. Right now it is rigid and I want it to eventually become more flexible. 
    - What would make building more engaging?
    We can make a game where you can buil the court each block at a time. We can maybe call it the "building" game. Save this to memory and lets create a plan around this. Make sure we lock this in and put it on the roadmap. It is a top priority because I think it gives students the ability to become architecture types. 
    - How can we ensure students create, not just consume?
    They are learning both from the books and the game things that they retain and have fun doign it. 

30. **Multiple Entry Points (Reggio):**
**Everything here needs to be discovered by R&D through AIMCODE. I want you to use the data we gather to make an informed decision on these questions. 
    - Can users access content from multiple places?
    - Are there multiple pathways through content?
    - What would make it more accessible?
    - How can we provide more entry points?

31. **Systematic Progression (Hassabis):**
**Everything here needs to be discovered by R&D through AIMCODE
    - Is progression truly systematic?
    Yes, it is but we need to make the coding even more so in order to easily create replical builds and also the students systematic learning through princples. 
    - Does each layer build on previous?
    Yes, I think you can help us improve on this more and more and I want you to think about how this can be improved throughout the process. 
    - What would make progression clearer?
    THe ability to get more detailed. Pivots, pre dribble actions like jabs and pump fakes, along with adding in the defender movement in all modes. 
    - How can we ensure deep understanding?
    We can track it and tell them what they learned each day (Put this on the roadmap)

---

## 📋 ANSWER FORMAT

For each question, please provide:

1. **Direct Answer:** Clear, specific answer
2. **Code Examples:** If applicable, show code
3. **Screenshots/Mockups:** If applicable, visual examples
4. **Documentation:** Point to existing docs if they exist
5. **Expert Input:** If question requires expert consultation, note that

---

## 🎯 PRIORITY ORDER FOR ANSWERS

### Answer These First (Critical - Blocking):
- Questions 1-8 (Game System + Integration Technical)

### Answer These Second (High - Important):
- Questions 9-15 (Game Modes + User Experience)

### Answer These Third (Medium - Nice to Know):
- Questions 16-19 (n8n + Curriculum)

### Answer These Fourth (Detailed - Deep Dive):
- Questions 20-24 (Technical Details)

### Answer These Last (Process - Ongoing):
- Questions 25-31 (Build-Measure-Learn + Experts)

---

## ✅ SUCCESS CRITERIA

After answering these questions, I should have:
- ✅ Complete understanding of Unity game system
- ✅ Complete understanding of integration mechanisms
- ✅ Complete understanding of user experience
- ✅ Complete understanding of build process
- ✅ Complete understanding of daily priorities
- ✅ 100% understanding of BallCODE fully integrated model

---

**Status:** 🎯 Ready for Your Answers  
**Total Questions:** 31  
**Critical Priority:** 8 questions  
**High Priority:** 7 questions  
**Medium Priority:** 4 questions  
**Detailed Technical:** 5 questions  
**Process/Expert:** 7 questions

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Purpose:** Get to 100% understanding


