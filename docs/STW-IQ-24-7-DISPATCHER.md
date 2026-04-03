# STW + IQ 24/7 Dispatcher (Mac + launchd or Pi + n8n)

## What this gives you
- A single always-on n8n workflow that runs every 5 minutes
- A dispatcher script that decides *which* STW News / IQ jobs are due
- Idempotency: it won’t re-upload the same job more than once per day

On Mac, the same dispatcher is run by launchd every 5 minutes. See:
- `docs/STW-MAC-AUTOMATION-RUNBOOK.md`
- `scripts/install-mac-launchd.sh`

Uploads only happen when `enabled: true` in `stw-publish-schedule.json`.
For STW News 4x weekly, dispatcher now supports queue-driven uploads via `action: "stw_news_queue_upload"`.

## 1) Ensure Pi n8n is always running
Use your existing Pi/n8n “set-and-forget” docker-compose method so the n8n server survives reboots:
- `workflows/BallCODE-Book/PI-N8N-OPTION-B-SET-AND-FORGET.md`

## 2) Deploy/Update files on the Pi
Make sure the Pi has:
- `scripts/stw-iq-dispatcher.py`
- `stw-publish-schedule.json`
- `workflows/n8n-stw-iq-dispatcher.json`

## 3) Import the workflow into n8n
In n8n UI:
1. Import `workflows/n8n-stw-iq-dispatcher.json`
2. Keep the workflow enabled (it is `active: true` in the JSON)

## 4) Configure your “go out at different times”
Edit `stw-publish-schedule.json`:
- Set `enabled: true` for the jobs you want
- Adjust `schedule.time` (daily, HH:MM)
- Adjust `privacy` (`unlisted` / `public`)
- For queue-driven STW News:
  - `queue_csv`: `_data/stw_news_queue.csv`
  - `video_template`: `output/video/stw-news-{story}-ready.mp4`
  - `metadata_template`: `shorts-packages/stw-news-2026-01/{story}/youtube-test.txt`

## 5) Test safely (recommended)
1. Run the workflow manually once (Manual Trigger)
2. Check logs:
   - `output/stw-iq-dispatcher.log`
   - `output/stw-iq-scheduler-state.json`

## 6) Turn on real publishing
After the titles/descriptions/times look correct:
- Switch `privacy` to `public` (if desired)
- Enable each job (`enabled: true`)

## 7) 4x weekly STW News queue cycle

1. Run daily scout:
   - `python3 scripts/stw-news-scout.py`
2. On Sunday, generate shortlist + queue:
   - `python3 scripts/stw-news-weekly-selector.py --write-queue --create-stubs`
3. Dispatcher picks up Monday/Tuesday/Thursday/Friday rows automatically.

