# SportsTechWest YouTube Growth Plan

**Channel:** [youtube.com/@SportsTechWest](https://www.youtube.com/@SportsTechWest)
**Written:** July 2026
**Goal:** Restart consistent publishing, unlock algorithmic distribution, and grow subscribers/views over the next 90 days using the pipeline that already exists in this repo.

---

## Where the channel is today (repo audit)

You already have more automation than most channels with 100k subs:

- **STW News Shorts pipeline** — daily scout (`scripts/stw-news-scout.py`), Sunday selector (`scripts/stw-news-weekly-selector.py`), queue CSV (`_data/stw_news_queue.csv`), Pi dispatcher (`scripts/stw-iq-dispatcher.py`), voice via ElevenLabs, upload via `scripts/youtube-upload.py`. Cadence design: 4 Shorts/week (Mon/Tue/Thu/Fri).
- **IQ ambient/long-form** — mentalIQ, bikeIQ, walkingIQ, workoutIQ, yogaIQ 1-hour videos with scheduled upload jobs.
- **Blog engine** — strong original analysis (2026 NBA Draft Front Office Equation + interactive simulator, Corner 3 decision tree, youth development, CLEAR framework) that is not yet on YouTube.
- **Brand kit** — STW News opener spec, visual guide, packaging standard.

### The three things holding growth at zero

1. **Everything uploads as `unlisted`.** Every job in `stw-publish-schedule.json` and the dispatcher default (`stw-iq-dispatcher.py:179`) is `unlisted`. Unlisted videos get **zero** Shorts-feed, search, or browse distribution — the algorithm literally cannot recommend them. This single setting caps the channel at hand-shared views no matter how much you publish.
2. **The queue is stale.** `_data/stw_news_queue.csv` ends at 2026-04-18. The 4x/week machine has been idle since mid-April. Consistency is the one input the Shorts algorithm rewards for small channels, and the streak is broken.
3. **No search-facing long-form.** Shorts grow reach; long-form grows subscribers and watch time. The channel's best differentiated content (front-office analytics, the draft simulator, youth development frameworks) currently lives only on the blog where nobody searching YouTube can find it.

Fix #1 is a one-line config change. Fix #2 is one Sunday session. Fix #3 is the 90-day project.

---

## Content strategy: three pillars

| Pillar | Format | Cadence | Job it does |
|--------|--------|---------|-------------|
| **STW News** | 60–75s Shorts | 4x/week (Mon/Tue/Thu/Fri) | Reach + searchable brand names (Strava, FIFA, Nike, WHOOP) pull cold viewers in |
| **STW Breakdowns** | 4–8 min long-form | 1x/week (Wednesday) | Converts viewers to subscribers; builds watch time and authority |
| **IQ ambient** | 1-hour audio/video | Steady library, not a schedule | Search + session time ("pre-game focus music", "1 hour affirmations for athletes") |

### Pillar 1 — STW News (restart, don't redesign)

The system works; it just stopped. Keep 4x/week exactly as designed in `docs/STW-NEWS-WEEKLY-POST-PLAN.md`, with these upgrades:

- **Publish `public`, not `unlisted`.** Change `privacy` in every enabled job in `stw-publish-schedule.json`. Keep `unlisted` only for 10s pipeline tests.
- **Title formula:** `[Brand people search] + [verb] + [stake]`. "Strava just bought Runna — here's what changes for your training" beats "STW News — Strava acquires Runna". Put brand names first; drop "STW News —" from the title (it's branding for you, noise for search). The opener graphic carries the show brand.
- **First 3 seconds = the headline, on screen and in voice.** No logo-only opener longer than ~1.5s before the hook lands.
- **Always end with a question** ("Would you pay for this?") to feed comments — comments are the cheapest ranking signal a small channel can earn.
- **Add `#shorts` + 2–3 topical hashtags** in the description via the metadata files in each story package.

### Pillar 2 — STW Breakdowns (the new addition)

One long-form video per week, Wednesday (the existing "buffer" day). Do not build a new pipeline — reuse the blog pipeline in reverse: every Breakdown is a blog post you already wrote or were going to write.

Launch backlog (already researched and written — just needs camera/screen-record + edit):

1. **"The Front Office Equation: How I'd Draft the 2026 Top 5"** — screen-record the interactive simulator (`Front_Office_NBA_Draft_Dashboard.html`), talk through it. Draft content spikes June–July; this is timely *right now*.
2. **"Why the Corner 3 Is a Decision Tree"** — from the Corner 3 analytics post + dashboard.
3. **"10 Tips for Youth Basketball Development"** — evergreen search traffic; parents/coaches search this year-round.
4. **"Championship Basketball Is Systematic Thinking"** — from the 2025-09 post.
5. **"Measurement ≠ Understanding" (Parts 1–2)** — from the two-part series.

Production standard (keep it cheap): talking head or voiceover + screen recording of your own dashboards, ~5 minutes, custom thumbnail (face or bold stat + ≤4 words), chapters in description. Your dashboards *are* the B-roll — nobody else has them, and that's the moat.

Each Breakdown also gets: 1–2 Shorts cut from its best 45 seconds (published on off-days or stacked with STW News), the blog post updated to embed the video, and a LinkedIn post.

### Pillar 3 — IQ ambient (flip it on, let it sit)

- Set the existing IQ videos to `public` with search-first titles: "1 Hour Pre-Game Focus | Mental Training for Athletes" style. These are library assets — ambient content compounds through search over months.
- Enable at most 1/week of new IQ uploads so they don't crowd the channel feed; consider a dedicated "IQ" playlist and channel-page section so they don't dilute the news/analytics identity.

---

## 90-day rollout

### Phase 1 — Restart (Weeks 1–2)

- [ ] Flip `privacy` to `public` for enabled jobs in `stw-publish-schedule.json`; change dispatcher default in `scripts/stw-iq-dispatcher.py` to `public` (or make it required per-job so nothing silently ships unlisted).
- [ ] Sunday session: run `stw-news-weekly-selector.py --write-queue --create-stubs`, refresh `_data/stw_news_queue.csv` with 4 fresh stories, build packages.
- [ ] Set the already-uploaded unlisted STW News videos to public **only if** the story is still fresh; otherwise leave them and move forward.
- [ ] Channel page hygiene (30 min, one-time): channel trailer (can be your best short), sections ordered News → Breakdowns → IQ, keyword-rich channel description, links to sportstechwest site.
- [ ] Create playlists: "STW News", "STW Breakdowns", "IQ — Mental Training".

### Phase 2 — Add long-form (Weeks 3–6)

- [ ] Ship Breakdown #1 (NBA Draft simulator walkthrough — do this first while draft season is hot).
- [ ] Ship one Breakdown per Wednesday thereafter from the backlog above.
- [ ] Cut 1 Short from each Breakdown; add end screens on Breakdowns pointing to the playlist + subscribe.
- [ ] Keep STW News at 4/week without missing a week — the streak is the strategy.

### Phase 3 — Double down on what works (Weeks 7–13)

- [ ] Wednesday analytics review (already in the weekly plan): for Shorts look at **swipe-away rate in the first 3s** and **viewed vs. swiped**; for long-form look at **CTR** (target ≥4%) and **average view duration** (target ≥40%).
- [ ] Whatever story category over-indexes (acquisitions? AI in officiating? wearables?), tilt the scout's `keyword_boosts` in `config/stw-news-scout-sources.json` toward it.
- [ ] Community tab: 2 posts/week (poll on the week's stories; behind-the-scenes of the Pi pipeline — builders love this).
- [ ] Pick the best-performing Breakdown and make a sequel/series from it.

---

## Distribution (off-YouTube, ~30 min/week)

- **LinkedIn Friday post** (already in the weekly plan) — keep it; your audience of coaches/founders/analysts lives there.
- **Blog ↔ YouTube loop:** every Breakdown embeds in its blog post; every blog post links the channel. The site already links `@SportsTechWest` in nav and footer.
- **Comment as the channel** on 3–5 videos/week in the sportstech niche (Huge Deal, sports business channels) — genuine takes, not links.

## Metrics & targets (90 days)

Track weekly in the Wednesday slot; judge trends, not single videos.

| Metric | Baseline | 90-day target |
|--------|----------|---------------|
| Publishing streak | 0 weeks | 12 consecutive weeks of 4 Shorts + 1 long-form |
| Shorts feed impressions | ~0 (unlisted) | Nonzero and trending up (algorithm learning) |
| Subscribers | current | +100–300 (realistic for a restart; long-form drives this) |
| Long-form CTR / AVD | n/a | ≥4% / ≥40% |
| One "outlier" video | n/a | 1 Short >10x channel median (then make 3 more like it) |

The honest note in `STW-NEWS-WEEKLY-POST-PLAN.md` still applies: small channels see single-digit views for weeks even when doing everything right. The plan optimizes finished weeks, not vanity metrics — but only if videos are **public**.

## Repo changes this plan implies

1. `stw-publish-schedule.json` — `privacy: "public"` on enabled jobs.
2. `scripts/stw-iq-dispatcher.py` — change the `unlisted` fallback default (lines 179, 209) or require explicit privacy per job.
3. `_data/stw_news_queue.csv` — fresh 4-story week.
4. New `shorts-packages/stw-news-2026-07/` (selector `--create-stubs` handles this).
5. Story metadata templates — add `#shorts` and hashtags to `youtube-test.txt` files; consider renaming to `youtube-meta.txt` now that they're production.

— Sportstechwest
