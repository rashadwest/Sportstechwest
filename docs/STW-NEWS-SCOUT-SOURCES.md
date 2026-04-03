# STW News Scout Sources + Scoring

This file documents the locked source + scoring model used by `scripts/stw-news-scout.py`.

## Config file

- `config/stw-news-scout-sources.json`

## Source feeds (daily scout)

- SportsPro
- SportBusiness
- Strava Press
- WHOOP Press
- FIFA News
- Nike News
- TechCrunch Sports tag

## Scoring weights

- `sourceAuthority`: `0.26`
- `recency`: `0.24`
- `brandStrength`: `0.20`
- `athleteRelevance`: `0.20`
- `headlineClarity`: `0.10`

## Boosters

- Keyword boosts (acquisition, partnership, AI, wearable, World Cup, NFL, etc.)
- Brand boosts (Strava, WHOOP, FIFA, Nike, Teamworks, Garmin, Peloton, etc.)

## Output files

- `output/stw-news-scout/daily-YYYY-MM-DD.jsonl`
- `output/stw-news-scout/latest-top.json`
- `output/stw-news-scout/weekly-shortlist-YYYY-MM-DD.md`

## Command

```bash
python3 scripts/stw-news-scout.py
```
