# STW News — Weekly post plan (one Short + one LinkedIn)

**Goal:** Ship **one STW News Short every week** on a fixed day, plus **one LinkedIn line** the same week so the feed isn’t only YouTube.

**Default publish day:** **Friday** (adjust once; keep the same slot every week).

---

## Weekly rhythm (about 2–3 hours total, spread across the week)

| When | Task | Time |
|------|------|------|
| **Monday** | Pick **one** story (slug) under `shorts-packages/stw-news-2026-01/<slug>/` or add a new folder with `article-url.txt` + `company-url.txt`. Prefer big names (Strava, NFL, WHOOP, FIFA) for search. | 20–30 min |
| **Tuesday** | Finalize `script-elevenlabs.txt` (already drafted for packaged stories). Trim to ~60s spoken. | 15–20 min |
| **Wednesday** | **Voice once:** `python scripts/voice-generate.py --in .../script-elevenlabs.txt --out output/audio/stw-news-<story>.mp3 --preset stw-news` | 15 min |
| **Thursday** | **Capture** article + company screenshots; **build** video: `./scripts/build-stw-news-video.sh <story>`. Watch once; fix only visuals if needed (no re-voice). | 45–60 min |
| **Friday** | **Upload** Short (title + description + tags from `youtube-test.txt`). **Thumbnail** per `brand-kit/STW-NEWS-THUMBNAIL-SPEC.md`. **LinkedIn:** paste from `docs/LINKEDIN-POST-FRIDAY-2026-03-28-STW-NEWS.md` (swap `[LINK]` for the new Short or channel). | 30–45 min |

If you only have one block: do **Thursday build + Friday publish** back-to-back after story + voice exist.

---

## Minimum viable week (if you’re slammed)

1. **Story** already chosen (e.g. `strava-runna`).
2. **Voice** Wednesday.
3. **Build + upload** Friday morning.
4. **LinkedIn** Friday afternoon (2 sentences + link).

Skip nothing except LinkedIn only if you must — the LinkedIn post costs almost no time and signals consistency off YouTube.

---

## Queue file (optional)

If you use `_data/stw_news_queue.csv`, add one row per publish day:

```csv
date,story
2026-04-04,strava-runna
```

One row = one Friday. If the file doesn’t exist yet, create it or track the date in your calendar instead.

---

## Why views stay low (short version)

- Shorts discovery is **algorithmic**; small channels often see **single-digit views** until the pattern repeats for months.
- What still helps: **first 3 seconds** = clear headline; **title** = names people search (Strava, NFL, WHOOP); **same weekly slot** so subscribers know when to look.

This plan optimizes **shipping**, not vanity metrics. Volume of *finished* weeks matters more than perfect edits.

---

## Related

- Links + capture: `docs/STW-NEWS-LINKS-READY.md`
- Voice once rule: `.cursor/rules/stw-news-voice-once.mdc`
- LinkedIn copy: `docs/LINKEDIN-POST-FRIDAY-2026-03-28-STW-NEWS.md`

— Sportstechwest
