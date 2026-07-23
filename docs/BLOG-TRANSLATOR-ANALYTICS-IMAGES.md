# Blog: The Translation Gap — Image Generation Brief

**Save images to:** `assets/images/blog-img/`  
**Article:** `_posts/2026-07-21-I-Have-Called-Myself-a-Translator-for-Years.md`  
**Do not generate assets in this task unless Rashad requests it.** This file is the prompt package only.

---

## What to use

| Image | Where to use it | Format |
|-------|-----------------|--------|
| **translator-analytics-hero.png** | Front matter `thumbnail` + social/OG preview | Required |
| **translator-analytics-bridge.png** | Optional inline after “What a Translator Actually Does” | Optional |
| **translator-analytics-ballcode.png** | Optional inline after “BallCODE Extends the Same Mission” | Optional |

**Minimum to unblock `validate-post`:** Generate the hero, save it as `assets/images/blog-img/translator-analytics-hero.png`, keep front matter:

```yaml
thumbnail: "/assets/images/blog-img/translator-analytics-hero.png"
```

---

## Overlay recommendation

**Primary (3 words):** `THE TRANSLATION GAP`  
**Optional supporting line:** `Data → Understanding → Action`  
Keep overlay sparse. Prefer adding text in Canva/Glif after generation if the model struggles with clean typography.

---

## 1. Hero / Thumbnail (required)

**Filename:** `translator-analytics-hero.png`  
**Dimensions:** 1200 × 630 px (16:9 social/OG)  
**Used in:** Front matter thumbnail, blog listing, LinkedIn/X share

**Alt text:**  
`College basketball assistant coach and college-aged player reviewing one simplified analytics insight on a tablet beside a practice court.`

**Generation prompt:**
```
Modern editorial sports photography, 1200x630 landscape. A younger college basketball assistant coach sits courtside or beside a practice gym floor with a college-aged basketball player. The coach holds a tablet showing a clean, abstract basketball-performance visualization—simple court diagram, one highlighted possession path or efficiency callout, no dense dashboard clutter. The coach points to one relevant insight. The athlete leans in, engaged, natural body language. Calm teaching conversation, not technological spectacle. Realistic gym lighting, soft shadows, shallow depth of field. Neutral practice-gym environment with no visible university logos, team names, jersey numbers that look real, or readable wall text. No identifiable real athletes or coaches. No futuristic AR overlays, holograms, or sci-fi UI. Photorealistic, quiet confidence, professional sports-media style. Leave subtle negative space near top or side for optional text overlay reading THE TRANSLATION GAP. No text burned into the image unless overlay is requested separately.
```

**Negative prompt / avoid:**  
Copied composition from any LinkedIn screenshot; real NBA/NCAA branding; celebrity likenesses; unreadable wall posters; neon cyber UI; crowded multi-chart dashboards; stock-photo “handshake over laptop” corporate vibe.

---

## 2. Optional: Analyst-to-coach bridge

**Filename:** `translator-analytics-bridge.png`  
**Dimensions:** 1200 × 630 px or 16:9  
**Paste block if used:**

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/translator-analytics-bridge.png" alt="Analyst and coach reviewing the same basketball insight in different language on film and a simple chart" class="img-fluid">
</div>
```

**Generation prompt:**
```
Editorial sports photography or high-quality photorealistic illustration, 16:9. Two colleagues in a quiet film-room or practice-office setting: one analyst and one assistant coach. A laptop or monitor shows a simple chart; a second screen or tablet shows a short basketball film still with one possession circled. They are mid-conversation, gesturing toward the same insight expressed two ways—measurement and basketball meaning. Calm, collaborative, realistic lighting. No logos, no identifiable real people, no dense dashboards, no futuristic overlays. Convey translation between analytics and coaching without corporate cliché.
```

---

## 3. Optional: BallCODE learning bridge

**Filename:** `translator-analytics-ballcode.png`  
**Dimensions:** 1200 × 630 px or 16:9  
**Paste block if used:**

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/translator-analytics-ballcode.png" alt="Young learners using basketball concepts on a screen as a bridge into coding and analytics ideas" class="img-fluid">
</div>
```

**Generation prompt:**
```
Warm, modern educational sports-tech scene, 16:9. Two or three non-identifiable young learners (teenagers or preteens, diverse, faces not celebrity-like) around a laptop or classroom screen. On screen: a simple basketball court graphic next to block-style or clean code-like if/then cards—suggesting basketball as a bridge into logic and analytics. Adult facilitator optional, back partly turned, no recognizable identity. Bright but calm classroom or gym-adjacent learning space. No real school branding, no BallCODE logo required, no product-ad layout. Photorealistic or polished editorial illustration. Emphasize learning and understanding, not marketing.
```

**Privacy:** Do not use real youth photos. Keep faces generic or partially turned if photorealistic.

---

## Quick reference

| Step | Action |
|------|--------|
| 1 | Generate hero with the prompt above |
| 2 | Save as `assets/images/blog-img/translator-analytics-hero.png` |
| 3 | Optional: add overlay `THE TRANSLATION GAP` in Glif/Canva |
| 4 | Re-run `npm run validate-post _posts/2026-07-21-I-Have-Called-Myself-a-Translator-for-Years.md` |
| 5 | Optional inline images only after hero exists |

---

## STWwin packaging note

- One focal idea per visual: conversation + understanding  
- Thumbnail text ≤ 5 words (`THE TRANSLATION GAP` = 3)  
- Promise matches article thesis: data → understanding → action
