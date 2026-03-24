# mentalIQ — Full Push Automation

**One command:** Assemble + YouTube upload. Optional: n8n workflow for scheduled or one-click push.

---

## Schedule for today (one-time)

### Option A — Delay in minutes (no `at`; works when `at` fails)

If you see `at: cannot open lockfile ... Operation not permitted`, use this instead:

```bash
chmod +x scripts/schedule-mentalIQ-push-today.sh

# Push in 90 minutes (example)
./scripts/schedule-mentalIQ-push-today.sh --delay-minutes 90
```

Output goes to `output/mentalIQ-scheduled-push.log`. Tail with `tail -f output/mentalIQ-scheduled-push.log`.

### Option B — macOS `at` (specific clock time)

```bash
./scripts/schedule-mentalIQ-push-today.sh 6pm
./scripts/schedule-mentalIQ-push-today.sh 21:00
```

Requires the `at` daemon (one-time):

```bash
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist
```

- **List:** `atq` — **Cancel:** `atrm <jobid>`

**Note:** Pasting comment lines that start with `#` into zsh can cause `zsh: number expected` or `command not found: #`. Run only the `./scripts/...` lines, not the comments.

---

## Quick Start (run now)

```bash
# From repo root
./scripts/ship-mentalIQ-push.sh
```

This will:
1. Assemble the 60-min video (brain loop + audio + music)
2. Upload to YouTube (public)

**Flags:**
- `--skip-assemble` — Use existing MP4 (video already built)
- `--no-upload` — Only assemble, don't upload

---

## Prerequisites

### 1. YouTube API (one-time)

1. **Google Cloud Console**
   - Create project or use existing
   - Enable **YouTube Data API v3**
   - Create OAuth 2.0 credentials (Desktop app)
   - Download `client_secrets.json`

2. **Place secrets**
   ```
   secrets/
   ├── client_secrets.json   # or client_secret.json
   └── youtube-token.json    # auto-created after first auth
   ```

3. **Python deps**
   ```bash
   pip install -r requirements-youtube.txt
   ```

4. **First run** — Browser opens for OAuth. Approve once. Token cached.

---

## Files

| File | Purpose |
|------|---------|
| `scripts/ship-mentalIQ-assemble.sh` | Assemble video (brain + audio + music → MP4) |
| `scripts/ship-mentalIQ-push.sh` | Full push: assemble + YouTube upload |
| `scripts/youtube-upload.py` | YouTube upload via Google API |
| `audio-scripts/youtube-mentalIQ-1hour-focus.txt` | YouTube metadata (title, description, tags) |
| `workflows/n8n-mentalIQ-push.json` | n8n workflow for one-click push |

---

## n8n Workflow (optional)

**Import:** `workflows/n8n-mentalIQ-push.json` into n8n

**Trigger:** Manual (click Run) or add Schedule Trigger for recurring

**Note:** Update the `command` path in the Execute Command node if your repo path differs from `/Users/rashadwest/Sportstechwest`.

---

## Social Posts (after upload)

Copy from `docs/MENTALIQ-POST-PLAN.md` — LinkedIn, Instagram, X. Or add Buffer/LinkedIn/Twitter nodes to the n8n workflow with your credentials.

---

— Sportstechwest
