# STW News Pi Automation Runbook (4x weekly)

> Archived as fallback. Primary production path is now Mac automation:
> `docs/STW-MAC-AUTOMATION-RUNBOOK.md`.

## Goal

Ship 4 STW News Shorts every week (Mon/Tue/Thu/Fri) with daily Pi scouting and Sunday queue generation.

## Scripts

- Scout daily: `scripts/stw-news-scout.py`
- Sunday selector + queue writer: `scripts/stw-news-weekly-selector.py`
- Dispatcher uploader: `scripts/stw-iq-dispatcher.py`
- Preflight checker: `scripts/check-stw-iq-readiness.sh`

## Weekly flow

1. Daily scout runs and scores candidate stories.
2. Sunday selector builds shortlist and writes next week queue.
3. Selector optionally creates missing story stubs in `shorts-packages/stw-news-2026-01/<slug>/`.
4. Dispatcher uploads due queue stories on Mon/Tue/Thu/Fri.

## Pi scheduling (cron)

Run `crontab -e` on Pi and add:

```cron
# Optional (recommended): set once for portability
# STW_REPO_ROOT=/Users/rashadwest/Sportstechwest

# Daily scout (UTC/local depending on Pi timezone)
10 8 * * * cd /Users/rashadwest/Sportstechwest && python3 scripts/stw-news-scout.py >> output/stw-news-scout/cron.log 2>&1
10 14 * * * cd /Users/rashadwest/Sportstechwest && python3 scripts/stw-news-scout.py >> output/stw-news-scout/cron.log 2>&1

# Sunday shortlist + queue + stubs
30 9 * * 0 cd /Users/rashadwest/Sportstechwest && python3 scripts/stw-news-weekly-selector.py --write-queue --create-stubs >> output/stw-news-scout/cron.log 2>&1

# Dispatcher (already used in n8n, optional cron fallback)
8,23,38,53 * * * * cd /Users/rashadwest/Sportstechwest && python3 scripts/stw-iq-dispatcher.py --config stw-publish-schedule.json --state output/stw-iq-scheduler-state.json --grace-minutes 35 >> output/stw-iq-dispatcher.log 2>&1
```

## Dispatcher queue job

`stw-publish-schedule.json` includes:

- `action: "stw_news_queue_upload"`
- `queue_csv: "_data/stw_news_queue.csv"`
- `video_template: "output/video/stw-news-{story}-ready.mp4"`
- `metadata_template: "shorts-packages/stw-news-2026-01/{story}/youtube-test.txt"`

## Sunday checklist

1. Run selector dry run:
   ```bash
   python3 scripts/stw-news-weekly-selector.py
   ```
2. Review `output/stw-news-scout/weekly-shortlist-YYYY-MM-DD.md`.
3. Run with queue + stubs:
   ```bash
   python3 scripts/stw-news-weekly-selector.py --write-queue --create-stubs
   ```
4. Confirm `_data/stw_news_queue.csv` has four rows for Mon/Tue/Thu/Fri.
5. Run preflight (must be clean before Monday window):
   ```bash
   ./scripts/check-stw-iq-readiness.sh
   ```

## KPIs (weekly)

- 4/4 queue slots populated by Sunday.
- 4/4 Shorts published on schedule.
- Median first-24h views trend.
- Avg retention trend (focus on first 3 seconds).

## Failure handling

- Missing queue story for a day: dispatcher skips job without marking run.
- Missing MP4/metadata: dispatcher logs skip and retries next trigger.
- API/billing issues: keep queue; rerun dispatcher after fix.
