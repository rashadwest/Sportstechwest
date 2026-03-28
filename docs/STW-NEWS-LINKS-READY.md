# STW News — strava-runna (links + capture)

**Article:** https://support.strava.com/hc/en-us/articles/35941891603725-Strava-is-Acquiring-Runna  
**Company:** https://www.strava.com/

**Capture (from repo root):**

```bash
python scripts/capture-article-screenshot.py --story strava-runna
python scripts/capture-article-screenshot.py --url "https://www.strava.com/" --out output/stw-news/strava-runna-company.png
```

**Voice (once):** `output/audio/stw-news-strava-runna.mp3` — `python scripts/voice-generate.py --in shorts-packages/stw-news-2026-01/strava-runna/script-elevenlabs.txt --out output/audio/stw-news-strava-runna.mp3 --preset stw-news`

**Build:** `./scripts/build-stw-news-video.sh strava-runna` → `output/video/stw-news-strava-runna-ready.mp4`

— Sportstechwest
