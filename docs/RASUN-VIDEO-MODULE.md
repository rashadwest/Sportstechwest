# RaSun Video module

Turns Sportstechwest blog posts into RaSun-narrated YouTube videos and publishes one **every other day**. It runs on the same machine and dispatcher as STW News and the IQ jobs (Pi + n8n, or Mac + launchd).

```
_posts/<post>.md
   │  rasun-video.py new        drafts the script (with Claude) + YouTube title, description and tags
   ▼
video-packages/rasun/<slug>/    script.txt · youtube.txt · package.json · (optional) visual.* / thumbnail.*
   │  you review → "approved": true
   │  rasun-video.py schedule   gives it the next every-other-day date
   ▼
_data/rasun_queue.csv           date,story
   │  stw-iq-dispatcher.py      job "rasun-every-other-day", runs daily at 11:17
   │    ├─ builds it if needed: RaSun voice (ElevenLabs) + 1080p render (ffmpeg)
   │    └─ uploads to YouTube (public), then saves the video ID in package.json
   ▼
YouTube
```

The dispatcher job runs every day, but it only uploads on days that have a row in the queue. The queue is what makes it every other day.

## One-time setup (on the Pi or Mac that runs the dispatcher)

1. Add the RaSun voice ID to `.env` (ElevenLabs → Voices → RaSun → copy the voice ID):
   ```
   ELEVENLABS_API_KEY=...
   ELEVENLABS_VOICE_ID_RASUN=...
   ```
2. Optional: to have Claude draft scripts, add your Claude API key and install the SDK:
   ```
   ANTHROPIC_API_KEY=...
   ```
   ```bash
   pip install -r requirements-youtube.txt
   ```
   Without a key, `new` still works but writes a rough outline you will need to rewrite.
3. YouTube upload already works if the IQ/STW News uploads work (`secrets/client_secrets.json` + `secrets/youtube-token.json`).
4. Pull this repo on that machine. The dispatcher picks up the new job from `stw-publish-schedule.json`.

## Weekly routine (about 15 minutes for 3–4 videos)

```bash
python3 scripts/rasun-video.py new --post _posts/2026-11-09-Practicing-Is-Not-Pressure-Beasley-vs-Stephenson.md
```

- Read `video-packages/rasun/<slug>/script.txt` out loud once and fix anything RaSun would trip on.
- Check `youtube.txt` (line 1 is the title, then the description, then the `TAGS:` line).
- Optional: drop in `visual.png`/`visual.jpg`/`visual.mp4` to replace the post's hero image, and `thumbnail.jpg` for a custom thumbnail.
- Set `"approved": true` in `package.json`.

```bash
python3 scripts/rasun-video.py schedule
```

```bash
python3 scripts/rasun-video.py status
```

Commit and push `video-packages/` and `_data/rasun_queue.csv`, then pull on the Pi. The dispatcher does the rest.

To hear and watch a video before its date:

```bash
python3 scripts/rasun-video.py build --slug <slug>
```

It writes `output/audio/rasun-<slug>.mp3` and `output/video/rasun-<slug>.mp4`. If you edit `script.txt` later, the next build re-voices it automatically.

## IQ sessions (bikeIQ, walkingIQ style)

A package with `"format": "iq-session"` in `package.json` builds as a long guided session instead of a blog breakdown. It uses the same pattern as the walking and mentalIQ videos:

- One spoken segment per paragraph in `script.txt`, voiced separately in RaSun's voice, with **5 seconds of quiet after each**.
- A line `[ride 90]` under a segment swaps that 5-second gap for about 90 seconds of music-only time. The builder stretches or shrinks all ride blocks together so the session lands exactly on `duration_seconds` (3600 = 60:00).
- Lines starting with `#` are notes and are never read aloud.
- Music bed: `music` at `music_volume` (default `output/music/background-manifestation-60min/track-a.mp3` at 35%), looped and faded. If the file is missing, it renders voice only and warns.
- Visual: `visual.png`/`visual.mp4` in the package folder (an MP4 loops for the hour). Thumbnail: `thumbnail.jpg`.
- Segments are cached by their text, so editing one line re-voices only that line.

Example: `video-packages/rasun/bikeiq-breathe-every-5-pedals/` (breathe in for 5 pedals, out for 5 pedals; 1 hour).

To start a new one, copy that folder, rewrite `script.txt`, `youtube.txt` and the card, set `"approved": true`, then run `rasun-video.py schedule`.

## Knobs

| What | Where |
|---|---|
| Upload time | `stw-publish-schedule.json` → `rasun-every-other-day` → `schedule.time` |
| Public / unlisted | same job → `privacy` |
| Pause RaSun only | same job → `"enabled": false` |
| Gap between videos | `rasun-video.py schedule --gap 3` (default 2) |
| Start date | `rasun-video.py schedule --start 2026-11-21` |
| Script length / voice rules | `RASUN_SYSTEM` and `TARGET_WORDS` in `scripts/rasun-video.py` |
| Voice settings | `scripts/voice-generate.py` (`--preset rasun`) |

## Files

- `scripts/rasun-video.py`: the module (`new`, `schedule`, `build`, `status`)
- `scripts/voice-generate.py`: `--preset rasun` reads `ELEVENLABS_VOICE_ID_RASUN`
- `scripts/stw-iq-dispatcher.py`: generic `queue_upload` action with `build_if_missing`, `thumbnail_template` and `record_video_id_in`
- `_data/rasun_queue.csv`: the publish calendar
- `video-packages/rasun/`: one folder per episode (excluded from the Jekyll build)
- Logs: `output/stw-iq-dispatcher.log`
