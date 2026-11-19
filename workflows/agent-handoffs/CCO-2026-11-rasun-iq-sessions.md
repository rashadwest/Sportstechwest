# CCO: Conversation Context Object
## RaSun Video module + IQ sessions (bikeIQ, hikingIQ, walkingIQ, runningIQ), Nov 20 to Dec 3, 2026

**Purpose:** Hand this work to Cursor (or any agent) so it can finish the build and ship without re-deriving anything.
**Owner:** Rashad West (Sportstechwest)
**Last updated:** 2026-11-19 (Thanos review)
**Repo:** `rashadwest/Sportstechwest`
**Branch:** `claude/keen-volta-y1ux2u` (pushed, **not merged**, no PR yet)

> Agent instructions: read this whole file first. Treat "Verified facts" and "Research" as the source of truth. Do not reopen anything under "Decisions already made." Build the tasks in section 8 in order. If you change a script, package or the module, update this file in the same commit.

---

## 1. Timeline

1. **"RaSun voice in ElevenLabs sounds good. Make a mod to push a video every other day."** Built the RaSun Video module on top of the existing ElevenLabs voice script, YouTube uploader and STW/IQ dispatcher. First episode drafted from the Beasley post (still awaiting review, not scheduled).
2. **"New post starting tomorrow: bikeIQ, breathe every 5 pedals, same way as our walking ones."** Added the `iq-session` format (walkingIQ/mentalIQ structure). Built "bikeIQ: Breathe Every 5 Pedals" (1 hour), approved and queued for **Fri Nov 20**. Tested a full 60:00 render with stand-in voice and music.
3. **"Plan the next two weeks: Sat, Tue, Thu. Change the imagery each time."** Drafted six 1-hour sessions with unique art, pinned to dates, all **awaiting approval**.
4. **"Use AIMCODE/Thanos to make sure this is what I should do, then give me the CCO so Cursor can build it."** Ran the review below. Applied the content fixes (research lines in descriptions, removed a health-claim tag). Wrote this file.

---

## 2. Files

| File | What it is |
|---|---|
| `scripts/rasun-video.py` | The module: `new`, `schedule`, `approve`, `build`, `status`. `iq-session` builder lives here (`build_session`). |
| `scripts/voice-generate.py` | ElevenLabs TTS. `--preset rasun` reads `ELEVENLABS_VOICE_ID_RASUN`. |
| `scripts/stw-iq-dispatcher.py` | Scheduler. Generic `queue_upload` action with `build_if_missing`, `thumbnail_template`, `record_video_id_in`, and a run lock. |
| `scripts/youtube-upload.py` | Uploader (thumbnail MIME type now set from the file). |
| `scripts/make-iq-card.py` | Draws `visual.png` + `thumbnail.jpg` from the `card` block in `package.json` (6 themes, 6 motifs). |
| `scripts/make-bikeiq-card.py` | One-off card for the bikeIQ episode. |
| `stw-publish-schedule.json` | Job `rasun-every-other-day`: daily at 11:17, public, uploads only on dates in the queue. |
| `_data/rasun_queue.csv` | The publish calendar (`date,story`). |
| `video-packages/rasun/<slug>/` | One folder per episode: `script.txt`, `youtube.txt`, `package.json`, `visual.png`, `thumbnail.jpg`. Excluded from the Jekyll build. |
| `docs/RASUN-VIDEO-MODULE.md` | How the module works, setup, knobs. |
| `workflows/agent-handoffs/CCO-2026-11-rasun-iq-sessions.md` | This file. |

**Where it runs:** the n8n workflow (`workflows/n8n-stw-iq-dispatcher.json`) runs
`cd /Users/rashadwest/Sportstechwest && python3 ./scripts/stw-iq-dispatcher.py ... --grace-minutes 35` every 5 minutes.
It **does not git pull**. It runs whatever is checked out in that folder.

---

## 3. The plan at a glance

| Date | Episode (slug) | Practice | Art | Status |
|---|---|---|---|---|
| Fri Nov 20 | `bikeiq-breathe-every-5-pedals` | In for 5 right-foot pedals, out for 5 | Navy, bike wheel with 5 in / 5 out marks | **Approved, queued** |
| Sat Nov 21 | `hikingiq-heel-toe-grounding` | Heel-toe steps: in over 3 steps, out over 4 | Forest, topo contours | Awaiting approval |
| Tue Nov 24 | `walkingiq-5-4-3-2-1-senses` | 5 see, 4 touch, 3 hear, 2 smell, 1 taste, in rounds | Teal, 5-4-3-2-1 dot rows | Awaiting approval |
| Thu Nov 26 | `runningiq-intention-and-gratitude` | Mantra "Light feet. Grateful heart." + gratitude for nature (Thanksgiving) | Sunrise over a road | Awaiting approval |
| Sat Nov 28 | `hikingiq-grounding-on-the-climb` | Same 3/4 heel-toe breath on uphill and downhill | Dusk, switchback mountain | Awaiting approval |
| Tue Dec 1 | `walkingiq-5-4-3-2-1-reset-walk` | 5-4-3-2-1 aimed at resetting after a hard day | Night, streetlights | Awaiting approval |
| Thu Dec 3 | `runningiq-one-word-mantra` | Pick one word, say it on every left foot | Ember, rings around "YOUR WORD" | Awaiting approval |

**Session format (all seven):** 60:00 total. One RaSun segment per paragraph, 5 seconds of quiet after each. `[ride|walk|hike|run|quiet N]` lines are music-only stretches, scaled together so the session lands exactly on 60:00. Music bed at 35%, looped and faded. Still card as the video (6 fps, `-tune stillimage`). About 3 to 5 minutes of speech per hour; the rest is guided practice time with music.

**Approve one:** `python3 scripts/rasun-video.py approve <slug>` (marks approved and queues it on its `planned_date`).

---

## 4. Verified facts

- **Render test:** full 60:00 bikeIQ build with stand-in voice and stand-in music: 1920x1080 H.264 at 6 fps, AAC, exactly 3600.0 s, 96 MB, about 7.5 min to encode in the cloud sandbox (Mac/Pi speed not measured). Segment timing: speech 5.0 min, 5 s gaps 115 s, ride blocks scaled x1.29.
- **Dispatcher tests (dry run + stand-in uploader):** queue lookup, build-if-missing, thumbnail pickup, YouTube ID written back to `package.json`, run lock blocks overlapping runs, existing jobs unchanged.
- **Not tested end to end:** real ElevenLabs RaSun voice, real YouTube upload, real music file. No ElevenLabs key or music in the sandbox.
- **Music file:** `output/music/background-manifestation-60min/track-a.mp3` (gitignored, lives on the Mac). Source and license are **not recorded anywhere in the repo**.
- **Breath math:**
  - bikeIQ: 5 right-foot strokes at about 80 rpm is about 3.75 s in and 3.75 s out, so about 8 breaths per minute, inside the under-10-per-minute slow-breathing range.
  - hikingIQ: 7 steps per breath at about 100 steps per minute is about 4.2 s per breath (about 14 per minute). That is a longer exhale synced to steps, **not** "slow breathing." The scripts only claim it helps you settle, which is fine.
- **Existing job:** `bikeiq-leisure` in `stw-publish-schedule.json` is `enabled: true`, daily at 06:23, with a fixed MP4 and no queue. If that MP4 exists on the Mac, the dispatcher re-uploads the same video every day.

---

## 5. Research (used in the YouTube descriptions, existence verified by search on 2026-11-19)

| Citation | Used for |
|---|---|
| Bramble, D. M., & Carrier, D. R. (1983). Running and breathing in mammals. *Science, 219*(4583), 251–256. doi:10.1126/science.6849136 | Breathing locks onto movement rhythm (bikeIQ, hikingIQ) |
| Zaccaro, A., et al. (2018). How breath-control can change your life: A systematic review on psycho-physiological correlates of slow breathing. *Frontiers in Human Neuroscience, 12*, 353. doi:10.3389/fnhum.2018.00353 | Slow breathing (under 10/min) linked to relaxation, less anxiety (bikeIQ, hikingIQ) |
| Emmons, R. A., & McCullough, M. E. (2003). Counting blessings versus burdens. *Journal of Personality and Social Psychology, 84*(2), 377–389. | Gratitude practice and well-being (runningIQ gratitude) |
| Blanchfield, A. W., Hardy, J., de Morree, H. M., Staiano, W., & Marcora, S. M. (2014). Talking yourself out of exhaustion: The effects of self-talk on endurance performance. *Medicine & Science in Sports & Exercise, 46*(5), 998–1007. doi:10.1249/MSS.0000000000000184 | Motivational self-talk: longer time to exhaustion, lower perceived effort (both runningIQ) |

5-4-3-2-1 is a practitioner grounding technique, not a studied treatment. The walkingIQ descriptions call it a focus tool and point people with ongoing anxiety to a professional.

Caveat: verified from abstracts and indexes, not full texts. Claims are kept general to match.

**Policy facts (verified 2026-11-19):**
- YouTube renamed "repetitious content" to **"inauthentic content"** on July 15, 2025. Mass-produced, template-driven videos with little variation can lose monetization at the **channel** level.
- The YouTube Data API has `status.containsSyntheticMedia` (added Oct 30, 2024). It is settable on `videos.insert`, so uploads can carry the "altered or synthetic content" disclosure.

---

## 6. Thanos review

**Verdict: Go.** It's the right move: it reuses the IQ format that already works for you and puts RaSun on a steady cadence. Fix 3 blockers before tomorrow and build 3 high-priority items this week.

### @AIMCODE: content quality

| Check | Status | Notes |
|---|---|---|
| **C** Clarity | Pass | One rule per episode (5 and 5 pedals, 3 in 4 out, 5-4-3-2-1, one mantra). |
| **L** Logic | Pass | Each hour runs learn, then practice, then load (climb, effort, stress), then quiet blocks, then cool-down. Week 2 builds on week 1 (Alpha Evolve layering). |
| **E** Examples | Pass | Concrete cues: right foot at the bottom, heel then toe, the shape of one leaf. |
| **A** Adaptation | Pass | Fallbacks built in (drop to 4 and 4, 2 in 3 out, change your word), a short game-day version of 5-4-3-2-1, safety lines in every intro. |
| **R** Results | Partial | Nothing is measured. Option for later: an end-of-session check-in ("rate your calm 1 to 10 now vs. the start") to mirror the Pressure Gap idea. |
| Peer-reviewed research | Pass (after fix) | "Why it works" line added to all 7 descriptions (section 5). |
| Health claims | Pass (after fix) | Removed the "anxiety relief" tag. 5-4-3-2-1 framed as a focus tool. |
| Zhang (story-first) | Pass | Every episode opens on a hook line, not theory. |
| Resnick (build something) | Pass | The viewer does the practice live, during long quiet blocks. |
| Jobs (simple) | Pass | One rule, one hour, one card. |

### @Garvis: technical

| Check | Status | Notes |
|---|---|---|
| Builder, scaling to 60:00, dispatcher, lock, ID write-back | Pass | Section 4 tests. |
| **Code reaches the machine** | **BLOCKER** | The Mac runs a local checkout with no pull. Merge to `main` and pull, or tomorrow's bikeIQ never runs. |
| **RaSun voice ID on the Mac** | **BLOCKER** | `ELEVENLABS_VOICE_ID_RASUN` must be in `.env`. |
| **Music license** | **BLOCKER** | Unknown source. A claimed track on 7 hour-long uploads means Content ID claims or blocks. |
| AI disclosure | High | RaSun is a synthetic, realistic voice. Set `containsSyntheticMedia` on upload (task C2). |
| Build at upload time | High | Each session voices about 50 segments plus an hour-long encode at 11:17. Prebuild nightly (task C4). |
| Duplicate daily upload | High | `bikeiq-leisure` re-uploads daily if its MP4 exists. Rashad to decide (task C5). |
| ElevenLabs credits | Check | About 3,000 to 5,000 characters per session, about 30,000 for all seven. Confirm the plan has room. |

### @Launch: distribution

| Check | Status | Notes |
|---|---|---|
| Titles, descriptions, tags, thumbnails | Pass | Under 100 characters, keyword-first, unique thumbnail per episode. |
| Inauthentic-content risk | Medium | 7 hour-long, mostly-music videos from one template in 14 days. Mitigated by distinct scripts, narration with real instruction, distinct art and research lines. Chapters (task C3) add more visible substance. Don't scale past this cadence until week-2 metrics are in. |
| Discovery | Gap | The IQ framework calls for a **3-minute version** next to every hour. Shorts cut from each session would be the discovery engine (task C6, phase 2). |
| Publish time | Decision | 11:17 is late for Saturday hikes and morning runs. Consider 05:47 or the evening before (Rashad decides). |
| Playlist | Gap | Put all IQ sessions in one playlist (task C7, phase 2). |
| Measure | Plan | One week after Nov 21: views, average view duration, subs per video. Compare IQ sessions to blog breakdowns. |

---

## 7. Decisions already made (do not reopen)

- **Format:** walkingIQ/mentalIQ structure, 1 hour, 5 s after every segment, music at 35%, still card.
- **Voice:** RaSun (ElevenLabs), ending "Sportstechwest. I'm RaSun."
- **Lane:** RaSun queue (`_data/rasun_queue.csv`), job `rasun-every-other-day`, **public**.
- **Calendar:** Fri Nov 20 bikeIQ, then Sat/Tue/Thu from Nov 21 to Dec 3, as in section 3. Week 2 = second takes on the same three ideas, with new art.
- **Approval gate:** nothing uploads unless `approved: true`. Rashad approves each one.
- **hikingIQ breath:** "3 breaths in, 4 out" is implemented as **one inhale over 3 heel-to-toe steps, one exhale over 4**. Change only if Rashad says so.
- **bikeIQ count:** one pedal = right foot at the bottom (one revolution).
- **runningIQ:** Rashad's prompt cut off at "over and over again through the…". Implemented as "through the run."
- **Nov 26 episode** closes with "Happy Thanksgiving from Sportstechwest."
- **Art:** generated typographic cards, no stock or photos, one theme and motif per episode.
- **Style:** no em dashes in scripts or descriptions.

---

## 8. Cursor build tasks (in order)

### C1. Ship to the machine (blocker, before Nov 20 11:17 local time)
1. Open a PR `claude/keen-volta-y1ux2u` into `main`. Wait for CI (`blog-validate.yml`, `site-health.yml`, `jekyll.yml`) and merge (Rashad merges).
2. On the Mac: `cd /Users/rashadwest/Sportstechwest && git checkout main && git pull`.
3. Add `ELEVENLABS_VOICE_ID_RASUN=<RaSun voice ID>` to `.env`.
4. Prebuild tomorrow's video and listen to the first 2 minutes:
   ```bash
   python3 scripts/rasun-video.py build --slug bikeiq-breathe-every-5-pedals
   ```
5. Run `python3 scripts/stw-iq-dispatcher.py --run-now rasun-every-other-day --dry-run` and check `output/stw-iq-dispatcher.log` shows the bikeIQ upload command.

**Done when:** `output/video/rasun-bikeiq-breathe-every-5-pedals.mp4` exists on the Mac, is 60:00, and the voice and music sound right.

### C2. AI disclosure on upload (high)
- `scripts/youtube-upload.py`: add `--synthetic-media` flag; when set, put `"containsSyntheticMedia": true` in `body["status"]`.
- `scripts/stw-iq-dispatcher.py`: if a job (or resolved queue job) has `"contains_synthetic_media": true`, pass `--synthetic-media`.
- `stw-publish-schedule.json`: add `"contains_synthetic_media": true` to `rasun-every-other-day`.
- **Done when:** a dry run shows `--synthetic-media` in the RUN line, and a real upload shows the "Altered or synthetic content" label in YouTube Studio.

### C3. Chapters in descriptions (high)
- Script syntax: a line `## Chapter title` starts a chapter at the next segment. Today `#` lines are comments, so `## ` must be checked first in `parse_session`.
- In `build_session`, while laying out the timeline, record each chapter's start time and write `video-packages/rasun/<slug>/chapters.txt` (`0:00 Intro`, `4:35 Learn the count`, ...). YouTube rules: the first chapter at 0:00, at least 3 chapters, each at least 10 s.
- In the dispatcher's `resolve_queue_job`, if `chapters.txt` exists next to `youtube.txt`, append it to the description under a "Chapters" heading.
- Add `## ` markers to all 7 scripts, following the bullet list already in each `youtube.txt` (warm-up, build, climb, cruise, cool-down, and so on). Don't change the spoken text.
- **Done when:** a test build writes a valid `chapters.txt` and the dispatcher dry run shows chapters in the description.

### C4. Nightly prebuild (high)
- Add a scheduled run (new n8n workflow next to `n8n-stw-iq-dispatcher.json`, or launchd) at **02:13** local time:
  ```bash
  cd /Users/rashadwest/Sportstechwest && python3 scripts/rasun-video.py build --upcoming 2 >> output/rasun-prebuild.log 2>&1
  ```
- It only builds approved, queued episodes for today to today+2. `build_if_missing` in the dispatcher stays as the fallback.
- **Done when:** the MP4 for the next queued date exists before 11:17 without a manual build.

### C5. Duplicate bikeIQ job (Rashad decides first)
- If Rashad agrees, set `"enabled": false` on `bikeiq-leisure` in `stw-publish-schedule.json`. Don't change anything else in that job.

### C6. 3-minute / Shorts versions (phase 2, after week-1 metrics)
- `rasun-video.py short --slug <slug>`: 1080x1920, 45 to 60 s, the hook segment plus the core instruction segments with 1 s gaps, a vertical version of the card (add a vertical layout to `make-iq-card.py`), music at 35%.
- Queue Shorts as their own job (a separate queue CSV) so they don't take the hour-long slots.

### C7. Playlist (phase 2)
- Adding to a playlist needs the `https://www.googleapis.com/auth/youtube` scope (the current token only has `youtube.upload`), so Rashad will need to re-consent once.
- Add an optional `--playlist-id` to `youtube-upload.py` (`playlistItems.insert` after upload), plus a `playlist_id` on the job.

**General rules for Cursor:** keep `[ride|walk|hike|run|quiet N]` and the 5 s gap behaviour; don't touch scripts' spoken text without Rashad; keep the approval gate; no em dashes; update this CCO in the same commit as any change.

---

## 9. Rashad's decisions needed

1. **Approve episodes** (each one: `rasun-video.py approve <slug>`, or tell Claude/Cursor). Nov 21 hikingIQ first, since it's due Saturday.
2. **Music license:** where `track-a.mp3` came from and whether it's cleared for YouTube. If unsure, swap in a YouTube Audio Library track and set `music` in each `package.json`.
3. **Upload time:** keep 11:17, or move to 05:47 / the evening before.
4. **`bikeiq-leisure`:** disable the daily re-upload?
5. **AI disclosure:** recommended on (task C2).

## 10. Reuse ideas

- **Shorts:** each hook line plus one instruction makes a 45-second vertical clip (C6).
- **Blog:** "Breathe on rhythm" post tying the IQ sessions to the research in section 5, linking each video.
- **BallCODE / curriculum:** breath math (pedals per minute to breaths per minute) is a ready-made rate lesson.
- **Teams:** the 5-4-3-2-1 short version ("one thing you see, one you hear, next play") as a timeout or free-throw routine.
