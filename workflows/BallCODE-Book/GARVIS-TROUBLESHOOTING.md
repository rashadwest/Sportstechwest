# Garvis Troubleshooting Guide
## Common Issues and Solutions

**Copyright © 2025 Rashad West. All Rights Reserved.**

---

## Issue: Job Not Starting

### Symptoms:
- Job created but status stays "pending"
- No execution log entries

### Solutions:

1. **Check n8n is running:**
   ```bash
   curl http://192.168.1.226:5678/healthz
   ```

2. **Check job in database:**
   ```bash
   python scripts/garvis-command.py --status <job_id>
   ```

3. **Manually trigger execution:**
   ```bash
   python scripts/garvis-command.py --execute <job_id>
   ```

4. **Check for errors:**
   - Review `garvis_jobs.db` for error messages
   - Check n8n workflow status

---

## Issue: Job Stuck in "in_progress"

### Symptoms:
- Job started but never completes
- Execution log shows it's running

### Solutions:

1. **Check for escalations:**
   ```bash
   python scripts/garvis-escalation.py --list
   ```

2. **Check workflow status:**
   - Verify n8n workflows are active
   - Check webhook endpoints are accessible

3. **Check execution log:**
   ```bash
   python scripts/garvis-command.py --status <job_id>
   ```
   Review the execution log for where it stopped

4. **Manual intervention:**
   - If truly stuck, you may need to manually complete
   - Update job status in database if needed

---

## Issue: Workflow Execution Fails

### Symptoms:
- Job completes but tasks show "failed"
- Error messages in job results

### Solutions:

1. **Check webhook endpoints:**
   ```bash
   curl -X POST http://192.168.1.226:5678/webhook/garvis \
     -H "Content-Type: application/json" \
     -d '{"test": true}'
   ```

2. **Verify n8n workflows are active:**
   - Check n8n UI for workflow status
   - Ensure workflows are not paused

3. **Check credentials:**
   - Verify n8n has required credentials
   - Check environment variables

4. **Review error details:**
   ```bash
   python scripts/garvis-command.py --status <job_id>
   ```
   Look at the error field for specific issues

---

## Issue: Quality Checks Failing

### Symptoms:
- Job completes but quality validation fails
- Confidence score below 75%

### Solutions:

1. **Review quality check results:**
   ```bash
   python scripts/garvis-quality-check.py --job-id <job_id>
   ```

2. **Check specific failures:**
   - Review which checks failed
   - Fix underlying issues
   - Re-run job if needed

3. **If confidence < 75%:**
   - Garvis will escalate automatically
   - Answer the escalation question
   - Garvis will resume

---

## Issue: Escalations Not Resolving

### Symptoms:
- Multiple escalations pending
- Garvis not resuming after answer

### Solutions:

1. **List escalations:**
   ```bash
   python scripts/garvis-escalation.py --list
   ```

2. **Resolve escalation:**
   ```bash
   python scripts/garvis-escalation.py --resolve <job_id> "Your answer"
   ```

3. **Manually resume job:**
   ```bash
   python scripts/garvis-command.py --execute <job_id>
   ```

4. **Check escalation file:**
   - Review `GARVIS-ESCALATIONS.md`
   - Ensure questions are clear

---

## Issue: Database Errors

### Symptoms:
- "Database locked" errors
- Jobs not saving

### Solutions:

1. **Close other connections:**
   - Ensure no other scripts are using database
   - Close any database viewers

2. **Check file permissions:**
   ```bash
   ls -la garvis_jobs.db
   ```
   Ensure file is writable

3. **Rebuild database if corrupted:**
   ```bash
   rm garvis_jobs.db
   python scripts/garvis-execution-engine.py
   ```
   (This will recreate the database)

---

## Issue: Import Errors

### Symptoms:
- "Cannot import garvis_execution_engine"
- Module not found errors

### Solutions:

1. **Check file exists:**
   ```bash
   ls scripts/garvis-execution-engine.py
   ```

2. **Check Python path:**
   - Ensure you're in the project root
   - Or use full path to script

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Issue: Webhook Timeouts

### Symptoms:
- Workflows start but timeout
- Long-running tasks fail

### Solutions:

1. **Increase timeout:**
   - Update n8n workflow timeout settings
   - Or break into smaller tasks

2. **Check network:**
   - Verify n8n is accessible
   - Check firewall settings

3. **Use direct execution:**
   - For very long tasks, consider direct execution
   - Or split into multiple jobs

---

## Issue: Results Not Showing

### Symptoms:
- Job says "completed" but no results
- Result field is empty

### Solutions:

1. **Check job status:**
   ```bash
   python scripts/garvis-command.py --status <job_id>
   ```

2. **Check execution log:**
   - Review log entries for task results
   - Verify tasks actually completed

3. **Re-run if needed:**
   ```bash
   python scripts/garvis-command.py --execute <job_id>
   ```

---

## Issue: SIAFI Percentage Not Updating

### Symptoms:
- Dashboard shows old SIAFI percentage
- Metrics not reflecting recent jobs

### Solutions:

1. **Refresh dashboard:**
   ```bash
   python scripts/garvis-dashboard.py
   ```

2. **Check database:**
   - Verify jobs are being saved
   - Check job statuses are correct

3. **Recalculate:**
   - Dashboard recalculates on each run
   - If still wrong, check calculation logic

---

## Issue: Chat Integration Not Working

### Symptoms:
- Saying "Garvis:" doesn't trigger
- Chat doesn't recognize commands

### Solutions:

1. **Check .cursorrules:**
   - Verify Garvis trigger phrases are added
   - Ensure AI is configured to recognize them

2. **Use explicit format:**
   ```
   Garvis: [ONE thing] + [tasks]
   ```

3. **Use command line instead:**
   ```bash
   python scripts/garvis-command.py --one-thing "..." --tasks "..."
   ```

---

## Issue: File Watcher Not Working

### Symptoms:
- `GARVIS-REQUEST.md` changes not detected
- File-based requests not triggering

### Solutions:

1. **Manual trigger:**
   ```bash
   python scripts/garvis-command.py --file GARVIS-REQUEST.md
   ```

2. **Check file format:**
   - Ensure file follows template
   - Verify ONE Thing and Tasks are present

3. **File watcher (if implemented):**
   - Check if file watcher is running
   - Restart if needed

---

## General Troubleshooting Steps

### Step 1: Check Status
```bash
python scripts/garvis-command.py --status <job_id>
```

### Step 2: Check Escalations
```bash
python scripts/garvis-escalation.py --list
```

### Step 3: Check Dashboard
```bash
python scripts/garvis-dashboard.py
```

### Step 4: Check Logs
- Review execution log in database
- Check `GARVIS-ESCALATIONS.md`
- Review n8n workflow execution logs

### Step 5: Verify Systems
- n8n is running and accessible
- Workflows are active
- Credentials are configured
- Environment variables are set

---

## Getting Help

### If Garvis Escalates:
1. Read the escalation question carefully
2. Provide clear, specific answer
3. Garvis will resume automatically

### If Issues Persist:
1. Check this troubleshooting guide
2. Review execution logs
3. Check n8n workflow status
4. Verify all systems are operational

### Common Solutions:
- **Restart n8n:** Often fixes workflow issues
- **Re-run job:** Sometimes jobs just need retry
- **Check credentials:** Many issues are credential-related
- **Verify network:** Ensure n8n is accessible

---

## Prevention

### Best Practices to Avoid Issues:

1. **Be clear with requests:** Ambiguity causes escalations
2. **Check systems first:** Ensure n8n is running
3. **Monitor initially:** Watch first few jobs to learn patterns
4. **Keep credentials updated:** Expired credentials cause failures
5. **Regular maintenance:** Check dashboard regularly

---

**Most issues resolve themselves. Garvis is designed to handle errors gracefully and escalate only when truly needed.**


