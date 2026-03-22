# Blog Post: Teaching Is the Greatest Teacher — Gemini Image Prompts

**Save images to:** `assets/images/blog-img/`

---

## What to use

| Image | Where to use it | Format |
|-------|-----------------|--------|
| **teaching-greatest-teacher-hero.png** | Blog post front matter (thumbnail) + social preview | Set `thumbnail: "/assets/images/blog-img/teaching-greatest-teacher-hero.png"` in the YAML at top of post |
| **teaching-greatest-teacher-transformation.png** | After "From Drivers to Owner-Operators" or any transformation section | Paste the HTML block below into the post body |
| **teaching-greatest-teacher-operating-system.png** | After "The Same Operating System" section | Paste the HTML block below into the post body |

**Minimum:** Generate the hero image, save it, and ensure the post front matter has the thumbnail path. The post will work with just that.

---

## Copy-paste blocks

**1. Hero (front matter)** — Already in the post. If you change the filename, use:
```yaml
thumbnail: "/assets/images/blog-img/teaching-greatest-teacher-hero.png"
```

**2. Transformation image** — Paste in post body where you want it:
```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/teaching-greatest-teacher-transformation.png" alt="Individuals becoming entrepreneurs - transformation to ownership" class="img-fluid">
</div>
```

**3. Operating system image** — Paste in post body where you want it:
```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/teaching-greatest-teacher-operating-system.png" alt="Same operating system across industries - Sportstechwest, BallCODE, BTE Analytics" class="img-fluid">
</div>
```

---

## 1. Hero / Thumbnail (required)

**Filename:** `teaching-greatest-teacher-hero.png`  
**Dimensions:** 1200 x 630 px (for social/OG preview)  
**Used in:** Front matter `thumbnail`, blog listing, social share

**Gemini prompt:**
```
Professional blog hero image. Theme: helping individuals become entrepreneurs—get started and connect to funding. Visual metaphor showing transformation: employees becoming business owners. Include subtle elements: a laptop or tech icon (startups), handshake or connection symbol (funding/capital), upward arrow or growth (ownership). Clean, modern, minimal design. Blue and white color scheme. No text. Photorealistic or high-quality illustration style. 16:9 aspect ratio.
```

---

## 2. Optional: Transformation section

**Filename:** `teaching-greatest-teacher-transformation.png`  
**Dimensions:** 1200 x 630 px or 16:9

**Gemini prompt:**
```
Professional illustration. Theme: individuals becoming entrepreneurs. Show a progression or transformation—from employee to business owner. Person with keys, documents, or laptop starting their own venture. Clean, hopeful, entrepreneurial tone. Blue and neutral colors. No text. Modern flat illustration or photorealistic style. Conveys ownership and possibility.
```

---

## 3. Optional: Same Operating System section

**Filename:** `teaching-greatest-teacher-operating-system.png`  
**Dimensions:** 1200 x 630 px or 16:9

**Gemini prompt:**
```
Professional infographic-style image. Theme: one system across many industries. Show four connected nodes or icons: (1) athlete/sports, (2) tech/laptop, (3) analytics/chart, (4) business/ownership. All connected by a central hub or network. Clean, modern, minimal. Blue and white. Conveys "same operating system, different industries." No text. Abstract or icon-based design.
```

---

## Quick reference

| File | Required | Use |
|------|----------|-----|
| teaching-greatest-teacher-hero.png | Yes | Thumbnail, social preview |
| teaching-greatest-teacher-transformation.png | No | Inline in transformation/ownership section |
| teaching-greatest-teacher-operating-system.png | No | Inline in "The Same Operating System" |

**To add the hero only:** Generate `teaching-greatest-teacher-hero.png` and save to `assets/images/blog-img/`. Update the post front matter `thumbnail` to reference it.

---

## Markdown / HTML for blog post

**Hero** — Set in front matter: `thumbnail: "/assets/images/blog-img/teaching-greatest-teacher-hero.png"`

**Optional inline images** — Paste where you want them in the post:

### teaching-greatest-teacher-hero.png (if used inline)
```markdown
![Teaching Is the Greatest Teacher - Helping individuals become entrepreneurs](/assets/images/blog-img/teaching-greatest-teacher-hero.png)
```

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/teaching-greatest-teacher-hero.png" alt="Teaching Is the Greatest Teacher - Helping individuals become entrepreneurs" class="img-fluid">
</div>
```

### teaching-greatest-teacher-transformation.png
```markdown
![Individuals becoming entrepreneurs - transformation to ownership](/assets/images/blog-img/teaching-greatest-teacher-transformation.png)
```

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/teaching-greatest-teacher-transformation.png" alt="Individuals becoming entrepreneurs - transformation to ownership" class="img-fluid">
</div>
```

### teaching-greatest-teacher-operating-system.png
```markdown
![Same operating system across industries - Sportstechwest, BallCODE, BTE Analytics](/assets/images/blog-img/teaching-greatest-teacher-operating-system.png)
```

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/teaching-greatest-teacher-operating-system.png" alt="Same operating system across industries - Sportstechwest, BallCODE, BTE Analytics" class="img-fluid">
</div>
```
