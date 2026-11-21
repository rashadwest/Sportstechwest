# YouTube Build Review: RaSun IQ Sessions (Nov 2026)

**Date:** 2026-11-21
**Reviewed:** PR #5, branch `claude/keen-volta-y1ux2u` (RaSun Video module, 9 IQ sessions Nov 20 to Dec 8)
**Question:** Is this build helping the YouTube strategy, and is it sustainable?
**Data limits:** No YouTube Studio numbers in this review (the channel is managed directly in Studio; nothing in the repo or this environment can read it). This reviews the system.

---

## Verdict

**It helps, a lot. It is not sustainable yet.** For the first time since April the channel has a real cadence: 9 finished hour-long sessions, 3 a week through Dec 8, with research-backed descriptions, chapters, AI disclosure, distinct art and a nightly prebuild. Production is solved.

What is not solved is the last step and the bigger picture:

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | Going public is manual. Every episode was uploaded as a private draft, so the dispatcher skips it on its date (it already has a video ID). Nothing goes public unless someone flips it in Studio. This is the July "unlisted" problem in a new form. | Blocker | **Fixed in this branch:** `scripts/rasun-schedule-publish.py` |
| 2 | The build is not on `main`. PR #5 is open; `main` still has the old schedule. The Mac runs whatever branch is checked out, so the next `git checkout main` silently stops RaSun. | Blocker | Merge PR #5, then this branch |
| 3 | No discovery engine. Hour-long, mostly-music videos are found slowly through search. Shorts (task C6) were deferred until "after week-1 metrics," but small channels get almost no metrics without Shorts. | High | Pull C6 forward |
| 4 | Channel identity drift. STW News (sportstech) has been dead since April; its job still runs Mon/Tue/Thu/Fri and finds an empty queue. The channel is becoming 100% breathing sessions, while the writing that defines Sports Tech West (Translator, Practicing Isn't Pressure, the NBA draft model) has no video. | High | Decision for Rashad (below) |
| 5 | Policy ceiling. 3 hour-long, AI-voiced, template-built videos a week sits near YouTube's "inauthentic content" line. The build already mitigates it well (distinct scripts, art, research, disclosure). | Medium | Do not raise IQ volume; add variety instead |
| 6 | Music source not written down anywhere in the repo. If one Content ID claim lands, you will want the license in hand. | Low | One line in `docs/RASUN-VIDEO-MODULE.md` |

---

## 1. Auto-publish (fixed)

`scripts/rasun-schedule-publish.py` sets YouTube's scheduled publish on each approved, already-uploaded episode in `_data/rasun_queue.csv`. The video stays private (your listen window) and goes public at 06:07 on its date by itself. To stop one, set it back to private in Studio.

```bash
python3 scripts/rasun-schedule-publish.py --dry-run          # see the plan
python3 scripts/rasun-schedule-publish.py                    # schedule them
python3 scripts/rasun-schedule-publish.py --publish-overdue  # also publish past-date drafts now
```

- First real run opens the browser once to allow the `youtube` scope (the upload token only has `youtube.upload`). It keeps its own token at `secrets/youtube-token-manage.json`, so uploads are unaffected. The same consent also unlocks playlists (task C7).
- It reads each video's current status first and keeps the AI-disclosure flag and other settings.
- Tested against the real queue (dry run) and with a fake YouTube client covering schedule, publish-overdue, already-public, missing video and re-run.

Dry run today: bikeIQ (Nov 20) shows **overdue** (still private if you have not published it in Studio); the other 8 schedule cleanly.

## 3. Discovery: pull Shorts forward

Every session already opens on a hook line plus one instruction ("In for five pedals. Out for five."). That is a 45-second vertical Short with no new writing. Ship one Short per session, ideally the day before the hour-long version, linking to it. This is the cheapest way to get the channel in front of people who are not already searching for "1 hour breathing walk."

## 4. Channel identity: the decision

The RaSun module already has a **blog-breakdown format** (3-minute narration over the post's art), and a Beasley breakdown is drafted and waiting. Recommendation:

- **Weekly mix:** 3 IQ sessions + 1 blog breakdown. The breakdown reuses writing you already do, so it adds about 15 minutes of review, not a new workload.
- **Retire STW News for now.** It died because daily scouting and editing is a second job. Set `stw-news-queue-4x-week` to `"enabled": false` so it stops running against an empty queue, and bring it back only if you want news again.
- **Before approving the Beasley breakdown:** its script closes with "I'm RaSun." The brand rule says the spoken close is "I'm Rashad West." (Not changed here; the CCO says spoken text changes need you.)

If you would rather the channel lean fully into training/mindset, that is a valid choice too, but then say so in the channel description and banner so subscribers know what they signed up for.

## Sustainable weekly routine (about 45 minutes, Sunday)

1. Listen to the coming week's private drafts (skim the intro and one practice block each).
2. `python3 scripts/rasun-schedule-publish.py` to lock their publish times.
3. Review and approve one blog breakdown.
4. Wednesday: 10 minutes in Studio (views, average view duration, subscribers per video, traffic sources).

## Measure on Nov 28 (one week after the first sessions)

For each session: views, average view duration, subscribers gained, and the top traffic source (search vs. browse vs. external). Compare against the Shorts once they exist. If one lane (biking, walking, running, hiking) clearly wins, give it the extra slot rather than adding a fourth IQ video.
