# STW News — Weekly post plan (4 Shorts + LinkedIn)

**Goal:** Ship **four STW News Shorts every week** (Mon/Tue/Thu/Fri), plus LinkedIn support so the feed is not only YouTube.

**Default publish days:** **Monday, Tuesday, Thursday, Friday** (keep the same time slot each day).

---

## Weekly rhythm (about 4–6 hours total, spread across the week)

| When | Task | Time |
|------|------|------|
| **Sunday** | Run scout selector and lock next week queue: `python3 scripts/stw-news-weekly-selector.py --write-queue --create-stubs` | 45–60 min |
| **Monday** | Publish queue story #1 (`_data/stw_news_queue.csv`) | 30–45 min |
| **Tuesday** | Publish queue story #2 | 30–45 min |
| **Wednesday** | Buffer/rebuild + check analytics + prep thumbnails | 30 min |
| **Thursday** | Publish queue story #3 | 30–45 min |
| **Friday** | Publish queue story #4 + LinkedIn cross-post | 45–60 min |

If you only have one block: do **Thursday build + Friday publish** back-to-back after story + voice exist.

---

## Minimum viable week (if you’re slammed)

1. Sunday queue has 4 stories.
2. Publish Mon/Tue/Thu/Fri from queue.
3. If one fails, Wednesday buffer catches up.
4. LinkedIn on Friday with the best-performing short.

Skip nothing except LinkedIn only if you must — the LinkedIn post costs almost no time and signals consistency off YouTube.

---

## Queue file (required for automation)

Update `_data/stw_news_queue.csv` each Sunday:

```csv
date,story
2026-04-06,strava-runna
2026-04-07,teamworks-sportlogiq
2026-04-09,fifa-ai-avatars
2026-04-10,orreco-jennis
```

One row = one publish day. Dispatcher job `stw-news-queue-4x-week` reads this file.

---

## Why views stay low (short version)

- Shorts discovery is **algorithmic**; small channels often see **single-digit views** until the pattern repeats for months.
- What still helps: **first 3 seconds** = clear headline; **title** = names people search (Strava, NFL, WHOOP); **same weekly slot** so subscribers know when to look.

This plan optimizes **shipping**, not vanity metrics. Volume of *finished* weeks matters more than perfect edits.

---

## Related

- Links + capture: `docs/STW-NEWS-LINKS-READY.md`
- Voice + packaging standard: `docs/STWWIN-PACKAGING.md`
- LinkedIn copy: `docs/LINKEDIN-POST-FRIDAY-2026-03-28-STW-NEWS.md`
- Pi runbook: `docs/STW-NEWS-PI-AUTOMATION-RUNBOOK.md`

— Sportstechwest
