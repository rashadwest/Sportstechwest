# SportsTechWest YouTube @Thanos Assessment
## Complete AIMCODE + Garvis + Launch Analysis

**Copyright © 2026 Rashad West. All Rights Reserved.**

**Date:** July 5, 2026
**Methodology:** @Thanos (AIMCODE + Garvis + Launch)
**Subject:** [youtube.com/@SportsTechWest](https://www.youtube.com/@SportsTechWest) + the publishing pipeline in this repo
**Reported status:** ~2 weeks behind last post
**Companion doc:** `docs/YOUTUBE-GROWTH-PLAN.md`

---

## 🎯 Executive Summary

**Overall Health Score:** 🟡 **62/100** (System is built; distribution and cadence are the failures)

### Component scores

| Component | Score | One-line verdict |
|-----------|-------|------------------|
| @AIMCODE (Content) | 🟡 72/100 | Strong system design and backlog; packaging not built for discovery |
| @Garvis (Automation) | 🟡 68/100 | Full pipeline exists end-to-end; it is stalled, not broken |
| @Launch (Execution) | 🔴 45/100 | Queue dead since April 18, ~2 weeks since last upload, everything ships `unlisted` |

### Critical findings (ranked by leverage)

1. 🔴 **`unlisted` on every automated upload.** Every enabled job in `stw-publish-schedule.json` and the dispatcher fallback (`scripts/stw-iq-dispatcher.py:179,209`) ships unlisted. Unlisted videos receive zero Shorts-feed, search, or browse impressions. Until this changes, publishing more content produces ~0 growth. **One-line fix, highest leverage in the entire system.**
2. 🔴 **The streak is broken.** `_data/stw_news_queue.csv` ends 2026-04-18. You report ~2 weeks since your last (manual) post. For a small channel, consistency is the input the algorithm rewards; the machine to guarantee it exists and is idle.
3. 🟡 **The catch-up trap.** Being 2 weeks behind creates pressure to backfill. Don't. News Shorts expire — a June story published in July reads stale. The correct move is a forward restart: fresh Sunday queue, next Monday go-live, zero backfill.
4. 🟡 **No subscriber engine.** 100% of planned output is Shorts + ambient audio. Shorts rent attention; long-form converts it. The channel's unfair advantage (interactive dashboards, front-office analytics, the draft simulator) has zero YouTube presence.
5. 🟡 **Ops docs drifted.** The Pi runbook says primary production moved to `docs/STW-MAC-AUTOMATION-RUNBOOK.md` — **that file does not exist in this repo.** `docs/STWWIN-PACKAGING.md` (referenced by the weekly plan) is also missing. Whatever the current production path is, it isn't written down here, which is exactly how a 4x/week system silently dies for 11 weeks.

### What could NOT be verified from this environment

Live channel metrics (subs, views, CTR, retention, exact last-upload date) — this session's network policy denies `youtube.com` and SocialBlade at the gateway (confirmed via proxy log: `CONNECT www.youtube.com:443 → 403`). This assessment covers the **system**; paste YouTube Studio numbers (last 28 days: views, watch time, subs, top 3 videos, Shorts swipe-away rate) into a follow-up session and the scores can be sharpened against reality.

---

## 🔬 @THANOS FRAMEWORK ANALYSIS

### @AIMCODE Component (Content Methodology) — 🟡 72/100

**Experts applied:**
- **@Chao Zhang** (story-first) — ✅ Applied in STW News scripts: each package leads with a hook line, not a logo
- **@Seth Godin** (Purple Cow / remarkable) — 🟡 Partially applied: the *dashboards* are the purple cow, and they're not on the channel
- **@MrBeast-school packaging** (title/thumbnail/first-3-seconds) — ❌ Not applied: titles lead with "STW News —" (your brand) instead of names viewers search (Strava, FIFA, Nike)
- **@Steve Jobs** (simplicity) — ✅ Applied: 75s single-story format, one headline per video

#### ✅ Complete
- ✅ **Show format defined** — STW News: opener + voiceover + B-roll collage, 60–75s, spec'd in `shorts-packages/stw-news-2026-01/README.md`
- ✅ **Brand kit** — `brand-kit/STW-NEWS-VISUAL-GUIDE.md`, opener spec, attribution standard
- ✅ **Story packaging standard** — per-story folder: `short.md` (script + B-roll beats), `script-elevenlabs.txt`, `edit-notes.md` (timeline + source URLs)
- ✅ **9 story packages built** (orreco-jennis, teamworks-sportlogiq, fifa-ai-avatars, strava-runna, playermaker, nike, aws, huupe...)
- ✅ **Long-form raw material** — blog backlog is genuinely differentiated: 2026 NBA Draft Front Office Equation + interactive simulator, Corner 3 decision tree, youth development, Measurement ≠ Understanding series

#### ⚠️ Gaps
- ⚠️ **Titles not search-first** — formula should be `[Brand] + [verb] + [stake]`; brand prefix belongs in the opener graphic, not the title
- ⚠️ **No long-form pillar** — nothing converts a Shorts viewer into a subscriber; the growth plan's "STW Breakdowns" (1x/week, blog-to-video) is designed but unshipped
- ⚠️ **Metadata still labeled "test"** — production uploads read metadata from `youtube-test.txt`; no `#shorts`/hashtags standard in descriptions
- ⚠️ **Story shelf-life unmanaged** — Jan 2026 packages are now unusable as "news"; no freshness rule in the selector

**Score: 72/100** — The methodology is real. The discovery layer (titles, long-form, hashtags) is the missing 28.

---

### @Garvis Component (Automation) — 🟡 68/100

**Experts applied:**
- **@Andy Grove** (operational excellence) — 🟡 Built but not monitored: no alert when the queue runs dry (it ran dry April 18 and nothing complained)
- **@Demis Hassabis** (systematic execution) — ✅ Applied: scout → score → select → queue → build → upload is a clean pipeline
- **@Elon Musk** (delete the part) — ⚠️ Needed: 5 of 7 scheduled jobs are `enabled: false`; dead config obscures live config

#### ✅ Complete
- ✅ **Daily scout** — `scripts/stw-news-scout.py`: RSS ingestion, recency + authority + keyword/brand-boost scoring, JSONL output
- ✅ **Sunday selector** — `scripts/stw-news-weekly-selector.py`: shortlist → `--write-queue --create-stubs` writes the week and scaffolds story folders
- ✅ **Dispatcher** — `scripts/stw-iq-dispatcher.py`: reads `stw-publish-schedule.json` + queue CSV, uploads on Mon/Tue/Thu/Fri slot (16:29)
- ✅ **Uploader** — `scripts/youtube-upload.py`: metadata files, thumbnails, privacy flags, `--confirm` safety
- ✅ **Voice** — ElevenLabs flow (`scripts/voice-generate`) with per-story clean scripts
- ✅ **Preflight** — `scripts/check-stw-iq-readiness.sh` exists per runbook

#### ⚠️ Gaps
- ⚠️ **Stalled input** — queue CSV last row 2026-04-18; automation with no queue = no output, silently
- ⚠️ **Privacy default** — dispatcher falls back to `unlisted` (`stw-iq-dispatcher.py:179`); schedule jobs all say `unlisted`; the pipeline is perfectly automated at shipping videos nobody can find
- ⚠️ **No dead-man switch** — nothing notifies you when a publish day passes with no upload; 11 weeks of silence proves it
- ⚠️ **Runbook drift** — Pi runbook archived in favor of a Mac runbook that isn't in the repo; `STWWIN-PACKAGING.md` referenced but missing; current production path undocumented
- ⚠️ **Hardcoded January paths** — schedule's `story_dir` and `metadata_template` point at `shorts-packages/stw-news-2026-01/`; a July restart needs these bumped (or made month-agnostic)
- ⚠️ **No analytics loop** — Wednesday review exists on paper only; nothing captures views/retention back into scout `keyword_boosts`

**Score: 68/100** — 90% of the machine exists. It's missing fuel (queue), a fire alarm (dead-man alert), and it's pointed at the wrong target (unlisted).

---

### @Launch Component (Execution) — 🔴 45/100

**Experts applied:**
- **@Grove** (cadence discipline) — 🔴 Broken: designed 4x/week; actual ≈ 0x/week for ~11 weeks (with some manual posts, last ~2 weeks ago)
- **@Godin** (ship the streak) — 🔴 The weekly plan's own words: "Volume of finished weeks matters more than perfect edits." Finished weeks since mid-April: ~0

#### ✅ Complete
- ✅ **Weekly operating plan** — `docs/STW-NEWS-WEEKLY-POST-PLAN.md`: realistic 4–6 h/week budget, minimum-viable-week fallback
- ✅ **Cross-platform hook** — LinkedIn Friday post templated; site nav/footer link the channel
- ✅ **Manual publishing muscle** — posts continued after automation stalled (last ~2 weeks ago), so the habit isn't dead

#### ⚠️ Gaps
- 🔴 **~2 weeks since last upload; ~11 weeks since the system last ran a full week**
- 🔴 **Distribution off** — unlisted = the launch never actually happened from the algorithm's perspective, regardless of effort spent
- ⚠️ **Channel-page packaging unverified** — trailer, sections, playlists, keyword description (couldn't inspect from this environment; treat as TODO until confirmed)
- ⚠️ **Blog ↔ YouTube loop one-directional** — site links channel; videos don't feed blog posts and blog posts don't embed videos

**Score: 45/100** — Execution is the bottleneck, and it's a scheduling/restart problem, not a capability problem.

---

## 🛤️ PATH BACK TO 100 (catch-up plan — forward restart, no backfill)

### This weekend (~2 hours total)
1. **[15 min] Flip distribution on.** In `stw-publish-schedule.json`: `"privacy": "public"` on both enabled jobs. In `stw-iq-dispatcher.py`: change the two `or "unlisted"` fallbacks to `or "public"` (or make privacy required per job). Keep `unlisted` only for 10s tests.
2. **[60–90 min] Sunday reset session.** Run the scout + `stw-news-weekly-selector.py --write-queue --create-stubs`; hand-pick the 4 freshest stories (July news only — skip anything from the gap); write `_data/stw_news_queue.csv` for Mon 7/6, Tue 7/7, Thu 7/9, Fri 7/10.
3. **[10 min] Repoint the schedule.** Update `story_dir`/`metadata_template` from `stw-news-2026-01` to the new July package dir.
4. **[15 min] Post one "we're back" community/LinkedIn note.** Costs nothing, restarts the public streak marker.

### Week of July 6 (back to full cadence immediately)
- Mon/Tue/Thu/Fri: 4 STW News Shorts ship **public** via dispatcher.
- Wed: pull YouTube Studio 28-day numbers (this also backfills the data this assessment couldn't reach) + verify channel page: playlists ("STW News", "STW Breakdowns", "IQ — Mental Training"), trailer, keyword description.

### Week of July 13 (add the subscriber engine)
- Ship **Breakdown #1**: screen-record the NBA Draft Front Office simulator walkthrough (asset already built: `Front_Office_NBA_Draft_Dashboard.html`; blog post already written). Draft-season search interest is still warm — this is the most perishable long-form asset in the backlog.
- Cut 1 Short from it. Embed the video back into the June 23 blog post.

### Hardening (by end of July)
- **Dead-man switch:** small cron/dispatcher check — if a publish day passes with no upload logged, send yourself an email/notification. This single alarm would have saved 11 weeks.
- **Queue-empty warning:** selector or preflight warns when `stw_news_queue.csv` has no future dates.
- **Write the real runbook:** replace the missing `STW-MAC-AUTOMATION-RUNBOOK.md` with whatever the actual current path is, or re-promote the Pi runbook.
- Rename `youtube-test.txt` → `youtube-meta.txt` in new packages; add `#shorts` + hashtags.

### 100% definition (12-week horizon)
- 12 consecutive finished weeks: 4 public Shorts + 1 Breakdown each week
- Dead-man switch live; zero silent gaps
- Analytics loop feeding scout keyword boosts
- 1 outlier video identified (>10x channel median) with 3 follow-ups shipped

---

## 📊 Score Summary

| Component | Now | After weekend fixes | After 12 clean weeks |
|-----------|-----|--------------------:|---------------------:|
| @AIMCODE | 72 | 78 (titles + hashtags) | 90 (long-form live) |
| @Garvis | 68 | 82 (queue + privacy + repoint) | 92 (dead-man + loop) |
| @Launch | 45 | 65 (streak restarted, public) | 90 (12/12 weeks) |
| **Overall** | **62** | **~75** | **~90** |

**Status:** 🟡 **ASSESSMENT COMPLETE — RESTART IS THE STRATEGY**
**Next:** Weekend checklist above; then paste Studio analytics for the data-driven follow-up pass.

---

**Copyright © 2026 Rashad West. All Rights Reserved.**
