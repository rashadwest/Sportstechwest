---
tags: [time, youtube, sportstechwest]
area: Time
updated: 2026-07-05
---

# SportsTechWest YouTube — Dashboard

**Channel:** https://www.youtube.com/@SportsTechWest
**Status (2026-07-05):** ~2 weeks behind last post; queue stale since 2026-04-18. Restart mode.
**Rule:** Forward restart — no backfilling missed weeks. News expires.

Related: [[SportsTechWest YouTube - Growth Plan]] · [[SportsTechWest YouTube - Thanos Assessment 2026-07]]

## Restart checklist (this weekend, ~2 h)

- [x] Flip uploads to `public` (schedule JSON + dispatcher defaults) — done 2026-07-05
- [x] Disable daily bikeiq re-upload job (same MP4 daily = spam once public) — done 2026-07-05
- [x] Queue-empty warning added to dispatcher — done 2026-07-05
- [ ] Sunday reset: run scout + `python3 scripts/stw-news-weekly-selector.py --write-queue --create-stubs`, pick 4 fresh July stories
- [ ] Repoint schedule `story_dir`/`metadata_template` from `stw-news-2026-01` to the new July package folder
- [ ] Build voice + video for Mon/Tue stories minimum
- [ ] "We're back" post on LinkedIn / community tab

## Weekly rhythm (4–6 h/week)

- [ ] **Sun** — Selector run, lock queue for the week (45–60 min)
- [ ] **Mon** — Short #1 ships (verify upload happened)
- [ ] **Tue** — Short #2 ships
- [ ] **Wed** — Analytics check (Studio 28-day: views, swipe-away, CTR) + Breakdown production
- [ ] **Thu** — Short #3 ships
- [ ] **Fri** — Short #4 ships + LinkedIn cross-post
- [ ] Weekly Breakdown (long-form) shipped? (starting week of Jul 13)

## Streak tracker

| Week of | Shorts (x/4) | Breakdown | Notes |
|---------|--------------|-----------|-------|
| 2026-07-06 | | | Restart week |
| 2026-07-13 | | | + Breakdown #1: NBA Draft simulator walkthrough |

## Hardening backlog

- [ ] Dead-man switch: alert when a publish day passes with no upload (11 silent weeks proved the need)
- [ ] Write the real production runbook (`STW-MAC-AUTOMATION-RUNBOOK.md` is referenced but missing)
- [ ] Rename `youtube-test.txt` → `youtube-meta.txt` in new packages; add `#shorts` + hashtags
- [ ] Channel page: playlists (STW News / Breakdowns / IQ), trailer, keyword description
