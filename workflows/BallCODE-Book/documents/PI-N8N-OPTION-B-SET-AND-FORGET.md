# Pi n8n — Option B (Set-and-Forget)

**Goal:** Make Pi n8n start the same way every time (reboots/updates), keep the secure-cookie fix permanently, and have an easy backup/restore.

**Pi host:** `rw3hampton@192.168.1.226`

---

## ELI10 (what this does)

- **Docker Compose file = the recipe.** It’s a saved “how to start n8n” so we never guess again.
- **Pinned version = stability.** We choose one n8n version so upgrades don’t surprise us.
- **Restart policy = always comes back.** Pi reboots → n8n comes back automatically.
- **Backup = safety net.** Your real n8n data lives in `/home/rw3hampton/.n8n`.

---

## Step 0 — SSH into the Pi

From Mac Terminal:

```bash
ssh rw3hampton@192.168.1.226
```

---

## Step 1 — Confirm current n8n image (so we can pin it)

Run on the Pi:

```bash
docker inspect n8n --format '{{.Config.Image}}'
```

This prints something like `n8nio/n8n:1.x.y`.

---

## Step 2 — Create a dedicated compose folder

Run on the Pi:

```bash
mkdir -p ~/n8n && cd ~/n8n
```

---

## Step 3 — Create `docker-compose.yml` (pinned + secure-cookie fix)

Run on the Pi (copy/paste):

```bash
cat > ~/n8n/docker-compose.yml <<'EOF'
services:
  n8n:
    # PIN THIS VERSION (replace 1.x.y with your chosen version)
    image: n8nio/n8n:1.x.y
    container_name: n8n
    ports:
      - "5678:5678"
    environment:
      # Pi is accessed over HTTP on LAN; this prevents the secure-cookie warning banner
      N8N_SECURE_COOKIE: "false"
    volumes:
      # Your real n8n data (workflows, DB, settings) lives here
      - /home/rw3hampton/.n8n:/home/node/.n8n
    restart: unless-stopped
EOF
```

Now **edit the pinned version**:

- Replace `1.x.y` with the output you got from Step 1.

Quick edit command:

```bash
nano ~/n8n/docker-compose.yml
```

---

## Step 4 — Start n8n using compose

Run on the Pi:

```bash
cd ~/n8n
docker compose up -d
```

---

## Step 5 — Verify the secure-cookie fix is actually loaded

Run on the Pi:

```bash
docker exec -it n8n sh -lc 'echo "N8N_SECURE_COOKIE=$N8N_SECURE_COOKIE"'
```

Expected output:

- `N8N_SECURE_COOKIE=false`

---

## Step 6 — Browser “last-mile” (Mac / Brave)

If you ever still see the banner even after Step 5 shows `false`:

- Open a **Private window**, or
- Clear site data for: `http://192.168.1.226:5678`

---

## Backups (recommended)

### Create a backup of n8n data

Run on the Pi:

```bash
sudo tar -czf "/home/rw3hampton/n8n-backup-$(date +%F).tar.gz" -C /home/rw3hampton .n8n
ls -lh /home/rw3hampton/n8n-backup-*.tar.gz | tail -1
```

### Copy backup to your Mac (optional)

Run on your Mac:

```bash
scp rw3hampton@192.168.1.226:/home/rw3hampton/n8n-backup-*.tar.gz ~/Downloads/
```

### Restore from a backup (only if needed)

Run on the Pi:

```bash
# stop n8n first
cd ~/n8n
docker compose down

# restore folder
sudo tar -xzf /home/rw3hampton/n8n-backup-YYYY-MM-DD.tar.gz -C /home/rw3hampton
sudo chown -R rw3hampton:rw3hampton /home/rw3hampton/.n8n

# start n8n again
docker compose up -d
```

---

## Mac vs Pi (keep them separate)

- **Mac n8n**: manual testing, not 24/7.
- **Pi n8n**: always-on automation.

Pi should keep `N8N_SECURE_COOKIE=false` as long as you access it via **HTTP** on LAN.


