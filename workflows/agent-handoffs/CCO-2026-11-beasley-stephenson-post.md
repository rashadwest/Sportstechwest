# CCO: Conversation Context Object
## Beasley vs. Stephenson blog post ("Practicing Isn't Pressure")

**Purpose:** Hand this conversation to another agent (Claude, Cursor, Garvis, n8n, etc.) so it can continue the work or reuse the post's research without re-deriving anything.
**Owner:** Rashad West (Sportstechwest)
**Last updated:** 2026-11-16 (voice pass + ship)
**Repo:** `rashadwest/Sportstechwest`
**Branch:** `claude/determined-tesla-0r6btx` (merged to `main` via PR; live on the site)

> Agent instructions: read this whole file first. Treat the "Verified facts" and "Research" sections as the source of truth for this topic. Do not re-add anything listed under "Decisions already made" as open questions. If you change the post, update this file in the same commit.

---

## 1. What happened in the conversation (timeline)

1. **"What happened to the Beasley Lance blog post?"** A search of every branch, all git history, PRs and issues found **no such post was ever committed**. "Beasley" only appears in BallCODE data CSVs. Conclusion: any earlier draft was never pushed (likely local / another tool).
2. **"Give me a good article to push."** Identified the topic as the **Michael Beasley vs. Lance Stephenson MMA fight (May 23, 2026)**. Wrote a new post, built a hero image, validated, committed, pushed.
3. **"Use AIMCODE/Thanos to make sure we are doing this all right."** Ran the Thanos review (AIMCODE + Garvis + Launch, per `workflows/BallCODE-Book/documents/AT-COMMANDS-QUICK-REFERENCE.md`). Added 6 peer-reviewed citations, a pressure/choking section, a measurable "Pressure Gap" drill, brand-color hero, inline image with alt text, and a social launch kit. Committed and pushed.
4. **"Was this ever pushed? Create a CCO."** Confirmed pushed to the branch (not live). Created this file.
5. **"Let's push it. Make it a consistent thing. Spell/grammar check, my voice."** Voice and proofreading pass on the post (short standalone lines, first-person experience as player/trainer/translator, ties to Rashad's film coaching loop). Made the CCO a standard step: `README.md` (process + Thanos post workflow) and `CCO-TEMPLATE.md` in this folder. Opened a PR into `main` and merged it.

---

## 2. Files

| File | What it is |
|---|---|
| `_posts/2026-11-09-Practicing-Is-Not-Pressure-Beasley-vs-Stephenson.md` | The post (~1,800 words, category Insights) |
| `assets/images/blog-img/beasley-stephenson-practice-pressure-hero.jpg` | 1200x630 typographic hero / OG image, brand blue #0C72B3 + orange #eb6123, no player photos |
| `workflows/blog-launch/2026-11-09-beasley-stephenson-launch-kit.md` | Thanos scorecard + LinkedIn, X thread, Instagram carousel, newsletter copy, posting plan |
| `workflows/agent-handoffs/CCO-2026-11-beasley-stephenson-post.md` | This file |

**Live URL after merge:** https://sportstechwest.com/blog/practicing-is-not-pressure-beasley-vs-stephenson/
(`workflows/` is excluded from the published site in `_config.yml`.)

---

## 3. The post at a glance

**Title:** Practicing Isn't Pressure: What Beasley vs. Stephenson Taught Me About Live Reps
**Thesis:** Practice reps and pressure reps are different data. Beasley's quote is a player development philosophy, and sport science backs it.

**Structure:**
1. Two Hoopers Walk Into a Cage (the fight, the quotes)
2. Lesson 1: Practice reps and live reps are different data (representative learning design; practice-vs-game table)
3. Lesson 2: Pressure changes how skill works (choking; training with anxiety)
4. Lesson 3: Athleticism transfers, skill does not (skill transfer; youth sport sampling)
5. Lesson 4: The name of the promotion was the point (attention economy; athlete brand)
6. Epilogue: Teammates again (June 20 BIG3 ejections)
7. Try It This Week: Measure your Pressure Gap
8. What I am taking from it (4 takeaways)
9. Research + News sources

**Signature idea, reusable anywhere:**
**Pressure Gap = Practice % − Pressure %**
Example: 16/20 FTs fresh (80%) vs. 12/20 tired with a consequence per miss (60%) = 20-point gap. Track weekly; a shrinking gap means practice is starting to look like the game.

**Internal links used:** `/blog/Measurement-Does-Not-Mean-Understanding-Part-1/`, `/blog/Where-Does-the-Value-Actually-Live-Part-2/`

---

## 4. Verified facts (source of truth)

- **Event:** Brand Risk Promotions 14 (Adin Ross's influencer fight series), co-main event, UFC Apex, Las Vegas, **May 23, 2026**.
- **Result:** Lance Stephenson def. Michael Beasley, **rear-naked choke, Round 1**. Beasley ended up on his back and tried a guillotine; Stephenson escaped, took his back, finished.
- **Finish time: sources conflict.** BrandRisk recap about 26 s; Yardbarker 1:04/65 s; Tapology and Bleacher Report 1:26. The post says "anywhere from under 30 seconds to 1:26." Do not state a single time.
- **Beasley quote:** "Practicing getting choked and getting choked ain't the same!" (Yahoo Sports live blog). Ballislife's version ends "...ain't no joke. I'll box." Beasley said he wants a boxing rematch.
- **Stephenson quote (clean version used):** "You can beat me in 1v1, but you wanna fight me?" (Ballislife on X).
- **Background:** Both were on Miami 305, 2025 BIG3 champions, and on the 2026 roster. Beasley was the No. 2 pick in the 2008 NBA Draft.
- **Epilogue:** June 20, 2026 BIG3 opener, Miami 305 vs. LA Riot. Beasley tangled with Dwight Howard; Stephenson threw a punch after a hard foul. Both ejected, Miami 305 forfeited, short of players (LA won 39-30 per BIG3). Commissioner Clyde Drexler suspended both on staggered weeks: fighting "of any kind will not be tolerated." The opponent's first name is reported inconsistently (Jordan vs. Jamal Crawford), so the post avoids naming him.

**News sources:** [Tapology event](https://www.tapology.com/fightcenter/events/143561-brandrisk-promotions-14), [Tapology bout](https://www.tapology.com/fightcenter/bouts/1136143-brandrisk-promotions-14-michael-beasley-vs-lance-stephenson), [Bloody Elbow](https://bloodyelbow.com/2026/05/24/michael-beasley-vs-lance-stephenson-fight-result-brand-risk-promotions-mma-fight-ends-in-shock-submission/), [Yahoo Sports](https://sports.yahoo.com/articles/brand-risk-14-live-blog-070440618.html), [ClutchPoints](https://clutchpoints.com/nba/lance-stephenson-choking-out-michael-beasley-in-mma-fight-is-craziest-thing-youll-see-today), [Ballislife on X](https://x.com/Ballislife/status/2058512397984211428), [Larry Brown Sports](https://larrybrownsports.com/basketball/lance-stephenson-michael-beasley-suspended-big3/759023), [BIG3 on X](https://x.com/thebig3/status/2068462888789193082)

Caveat: full articles could not be fetched from the sandbox; facts come from search-result summaries cross-checked across sources.

---

## 5. Research (peer-reviewed, existence verified)

| Citation | Used for |
|---|---|
| Pinder, Davids, Renshaw & Araújo (2011). Representative learning design and functionality of research and practice in sport. *J. Sport & Exercise Psychology, 33*(1), 146–155. doi:10.1123/jsep.33.1.146 | Practice transfers only if it keeps competition's key information and pressures |
| Beilock & Carr (2001). On the fragility of skilled performance: What governs choking under pressure? *J. Experimental Psychology: General, 130*(4), 701–725. | Choking: step-by-step monitoring breaks down automatic skills |
| Oudejans & Pijpers (2009). Training with anxiety has a positive effect on expert perceptual-motor performance under pressure. *Quarterly J. Experimental Psychology, 62*(8), 1631–1647. | Training under pressure improves performance under pressure |
| Rosalie & Müller (2012). A model for the transfer of perceptual-motor skill learning in human behaviors. *Research Quarterly for Exercise and Sport, 83*(3), 413–421. | Transfer depends on task similarity |
| Côté, Lidor & Hackfort (2009). ISSP position stand: To sample or to specialize? *Int. J. Sport and Exercise Psychology, 7*(1), 7–17. | Multi-sport sampling as a base |
| Arai, Ko & Ross (2014). Branding athletes. *Sport Management Review, 17*(2), 97–106. doi:10.1016/j.smr.2013.04.003 | Athlete brand is more than performance |

Caveat: verified from abstracts and citing papers, not full texts. Claims in the post are kept general to match.

---

## 6. Decisions already made (do not reopen)

- Topic = Beasley vs. Stephenson MMA fight, framed as player development + sport science + attention economy.
- First-person voice as Rashad (coach / data / "translator").
- **No em dashes** (Rashad's style).
- Stephenson's quote is used without the slur that preceded it.
- Finish time is given as a range, not one number.
- Hero image is typographic only (no player photos, no rights issues), brand colors.
- Voice: short standalone lines, measured not hype, "I watched it as a translator," references Rashad's real roles (player receiving information in live competition, trainer of young athletes) and his film loop (observation, cue, behavior to test, follow-up measurement). No invented anecdotes.
- Date in front matter: 2026-11-09 (must stay after the latest post date for `scripts/validate-post.js`).

---

## 7. Status and checks

| Check | Status |
|---|---|
| `node scripts/validate-post.js` | Pass |
| Markdown render (kramdown GFM) | Pass, 0 warnings |
| Images exist, alt text | Pass |
| Full Jekyll build | Not run locally (sandbox Ruby env issues). Runs in CI on PR (`blog-validate.yml`) and on merge to main (`jekyll.yml`). |
| Pushed | Yes, branch `claude/determined-tesla-0r6btx` |
| Proofread + voice pass | Done (manual read; no spell-check tool available in the sandbox) |
| Live | Merged to `main`; GitHub Pages deploys via `jekyll.yml` |

---

## 8. Next steps for any agent picking this up

1. Confirm the live URL loads with the image after the `jekyll.yml` deploy finishes.
2. Run the posting plan in the launch kit (LinkedIn → X → X thread → Instagram → newsletter). Do not post before the page is live.
3. One week after launch: pull views/clicks per channel, record what worked (BML).

## 9. Reuse ideas

- **BallCODE / curriculum:** the Pressure Gap is a ready-made math lesson (percentages, subtraction, tracking change over time).
- **BTE / analytics content:** practice-vs-game table → a "context gap" series on any stat measured in drills vs. games.
- **Video / short-form:** Beasley quote → 3 science points → Pressure Gap drill (about 45 seconds).
- **Follow-up post:** a reader Pressure Gap challenge with collected results.
