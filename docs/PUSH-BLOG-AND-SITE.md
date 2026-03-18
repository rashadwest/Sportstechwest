# Push Blog Post or Site Changes — Simple Flow

**When you say "post it" or "push it":** Add → Commit → Push. No PR needed.

---

## Standard Flow (use every time)

```bash
cd /Users/rashadwest/Sportstechwest

# Add the files you changed (e.g. new blog post)
git add _posts/2026-03-17-Building-Entrepreneurs-as-a-VC-Scout.md
# Or: git add .   (to add everything)

# Commit
git commit -m "Add blog post: [title]"

# Push
git push origin main
```

Then wait 2–5 minutes for GitHub Pages to deploy.

---

## One-Time Fix (if push fails with large files)

If push fails with "Large files detected" or "exceeds GitHub's file size limit":

Your local history has files >100 MB. **Reset local to match origin**:

```bash
cd /Users/rashadwest/Sportstechwest
git fetch origin
git reset --hard origin/main
```

After this, local = origin. Standard flow works again. Keep `output/music/`, `output/video/`, `output/audio/` in `.gitignore` so large files never get committed.

---

## To Avoid Divergence

- **Pull before you push** (at start of session or before pushing):
  ```bash
  git pull origin main
  ```
- Or push soon after committing so local and remote stay in sync.

---

**Reference:** `docs/DEPLOY-NAVIGATION-CHANGES.md` for deployment verification.
