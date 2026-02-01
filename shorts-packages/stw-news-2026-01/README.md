# STW News — Jan 2026 (3 stories)

Quick sportstech current-events videos: **voiceover (ElevenLabs) + collage of official images/videos** as B-roll. Brand: **STW News** opener + Sportstechwest logo in corner.

---

## Workflow

1. **STW News opener** — Build once (black or deep blue + "STW News" + logo corner). Use for all three. See `branding-notes.md` and `brand-kit/STW-NEWS-VISUAL-GUIDE.md`.
2. **Gather B-roll** — Per story, use the URLs in each `edit-notes.md` (press images, app store, company YouTube, FIFA media). Download or screen-capture; keep attribution for description.
3. **Voice** — Paste each story’s **script-elevenlabs.txt** into ElevenLabs (no B-roll tags); generate MP3. Or use `scripts/voice-generate` with that file or the script section from `short.md` (strip `[B-ROLL: …]` lines first).
4. **Edit** — In your editor (CapCut, DaVinci Resolve, etc.): **opener (2–3 s)** → **B-roll in order** cut to the voiceover. Follow the timeline in `edit-notes.md` (each beat = suggested clip). Drop voice track first; collage images/video on top, cutting on script beats.
5. **Export** — 9:16 for Shorts or 16:9 for standard; add "Footage/Image: [source]" in description where needed.

---

## 10-second unlisted test (first story)

To check you’re on the same page before doing the full edit:

1. **STW News opener** — One image: black or deep blue + "STW News" + Sportstechwest logo (e.g. bottom-right). Save as `orreco-jennis/stw-news-opener.png` (or any path you’ll pass to the script).
2. **Voice (10s)** — In ElevenLabs, paste only: *"An Olympic champion's app just became core infrastructure for pro women's sports."* Generate and save as `orreco-jennis/voice-10s.mp3` (or trim the full script to ~10s and export).
3. **Build 10s MP4** — From repo root:
   ```bash
   chmod +x shorts-packages/stw-news-2026-01/orreco-jennis/build-10s-test.sh
   ./shorts-packages/stw-news-2026-01/orreco-jennis/build-10s-test.sh
   ```
   (Or pass paths: `./build-10s-test.sh /path/to/opener.png /path/to/voice-10s.mp3`.)
   Output: `output/video/stw-news-orreco-jennis-10s-test.mp4`.
4. **Upload unlisted**:
   ```bash
   python scripts/youtube-upload.py --mp4 output/video/stw-news-orreco-jennis-10s-test.mp4 --metadata-file shorts-packages/stw-news-2026-01/orreco-jennis/youtube-test.txt --privacy unlisted --confirm
   ```

If you prefer to **export the first 10s from your editor** (CapCut, Resolve, etc.), save that MP4 and run the same upload command with your file path.

---

## Stories (packages)

| Story | Folder | Script | ~Length |
|-------|--------|--------|---------|
| Orreco acquires Jennis | `orreco-jennis/` | `short.md` | ~75 s |
| Teamworks acquires Sportlogiq | `teamworks-sportlogiq/` | `short.md` | ~75 s |
| FIFA 2026 AI avatars for offside | `fifa-ai-avatars/` | `short.md` | ~75 s |

Each folder has:
- **short.md** — Spec, full voiceover script with [B-ROLL] beats inline.
- **script-elevenlabs.txt** — Script only (no B-roll tags); paste into ElevenLabs.
- **edit-notes.md** — Timeline: what image/video to show when; source URLs.

---

## Branding (all three)

- **Opener:** "STW News" (or "Sportstechwest News") as main text; Sportstechwest logo small, one corner (e.g. bottom-right). See `branding-notes.md`.
- **Description:** End with "— Sportstechwest" and attribute B-roll (e.g. "Image: Orreco" / "Footage: FIFA").

— Sportstechwest
