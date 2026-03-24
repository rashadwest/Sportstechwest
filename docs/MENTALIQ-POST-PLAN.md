# mentalIQ — 1-Hour Post Plan

**Status:** Ready to ship  
**Assets:**
- Video: `~/Desktop/Brain Videos/MentalIQ_brain.mp4`
- Audio: `~/Desktop/SportsTechWest_visualizeIQ/MentalIQ_1hour_focus.m4a`
- Music: `output/music/background-manifestation-60min/track-a.mp3` (if using same as GameIQ/WalkingIQ)

---

## 1. Assemble the Video

Combine brain loop + audio + music into final MP4.

**Inputs:**
| Input | Path |
|-------|------|
| Video | `/Users/rashadwest/Desktop/Brain Videos/MentalIQ_brain.mp4` |
| Audio | `/Users/rashadwest/Desktop/SportsTechWest_visualizeIQ/MentalIQ_1hour_focus.m4a` |
| Music | `output/music/background-manifestation-60min/track-a.mp3` (35% mix) |

**Output:** `output/video/mentalIQ-1hour-focus.mp4`

**ffmpeg pattern** (same as GameIQ/WalkingIQ):
- Loop brain video to fill 60 min
- Audio = MentalIQ_1hour_focus.m4a (primary)
- Music = track-a.mp3 at 35% under voice

---

## 2. YouTube Upload

**Title:**  
`1 Hour Mental Focus for Sports | mentalIQ | Sportstechwest`

**Description:**
```
mentalIQ — Mental focus for sports. One hour of breathing, cue words, and routines to train your mind the way you train your body.

Your body can only do what your mind lets it.

This session covers:
• What focus is and why it breaks down under pressure
• System 1: Breathing (box breathing)
• System 2: Cue words
• System 3: Routines
• How to put it together before, during, and after competition
• Common mistakes to avoid

Play during pre-game, warm-up, or anytime you need to reset and lock in. 5-second pauses between segments so you can practice as you listen.

More IQ Training: youtube.com/@SportsTechWest
— Sportstechwest
```

**Tags:**  
`mental focus`, `sports psychology`, `mental training`, `pre-game`, `athlete`, `focus`, `mentalIQ`, `sportstechwest`, `breathing`, `performance`

**Category:** Sports (or Education)

**Privacy:** Public

---

## 3. Thumbnail

**Suggested:**  
- mentalIQ branding + brain visual
- Text: "1 HOUR MENTAL FOCUS"
- Match other IQ thumbnails (WalkingIQ, GameIQ, etc.)

---

## 4. Pinned Comment (Optional)

```
mentalIQ = mental focus for sports. Use before competition, during warm-up, or when you need to reset. 5-second pauses between segments — use them to breathe and practice. Try it this week: one breath, one cue word, before your next big moment.
```

---

## 5. Social Posts

### LinkedIn
**Hook:**  
Your body can only do what your mind lets it.

**Body:**  
mentalIQ is live — 1 hour of mental focus training for sports. Breathing, cue words, routines. The same systems pros use, in a format you can play during pre-game or warm-up. 5-second pauses so you can practice as you listen. Drop a link in comments.

**CTA:** Link to YouTube video

---

### Instagram
**Caption:**  
mentalIQ — 1 hour of mental focus for sports. Breathing. Cue words. Routines. Your body can only do what your mind lets it. Link in bio. 🧠

**Reel/Carousel:**  
- Clip: first 15–30 sec of video (hook + opening)
- Or: MentalIQ_brain.mp4 loop as visual with audio snippet

---

### X / Twitter
**Tweet:**  
mentalIQ is live. 1 hour of mental focus for sports — breathing, cue words, routines. Your body can only do what your mind lets it. 5 sec between segments so you can practice as you listen. [link]

---

## 6. Checklist

- [ ] Assemble: Brain video + audio + music → `output/video/mentalIQ-1hour-focus.mp4`
- [ ] Thumbnail ready
- [ ] YouTube upload (title, description, tags)
- [ ] Pinned comment (if desired)
- [ ] LinkedIn post
- [ ] Instagram post / Reel
- [ ] X / Twitter post

---

## 7. Automation

**Full automated push:** See `docs/MENTALIQ-PUSH-AUTOMATION.md`

```bash
./scripts/ship-mentalIQ-push.sh
```

- Assemble + YouTube upload in one command
- n8n workflow: `workflows/n8n-mentalIQ-push.json` (import for one-click)
- Social posts JSON: `audio-scripts/mentalIQ-social-posts.json`

---

— Sportstechwest
