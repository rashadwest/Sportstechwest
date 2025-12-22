# Garvis Workflow Reference
## Technical Reference for Garvis System

**Copyright © 2025 Rashad West. All Rights Reserved.**

---

## Architecture

### Core Components

1. **Garvis Execution Engine** (`scripts/garvis-execution-engine.py`)
   - AI-driven task execution
   - AIMCODE methodology integration
   - Autonomous decision-making
   - Quality validation

2. **Garvis Command Interface** (`scripts/garvis-command.py`)
   - User-facing CLI
   - Job creation and tracking
   - Status reporting

3. **Garvis Orchestrator** (`n8n-garvis-orchestrator-workflow.json`)
   - Routes requests to systems
   - Coordinates multi-system updates
   - Aggregates results

4. **System Workflows:**
   - School Onboarding
   - Sales Automation
   - Website Auto-Update
   - Book Content Update
   - Curriculum Sync
   - Unity Build

---

## Execution Flow

```
User Input → Garvis Command → Execution Engine → 
AIMCODE Analysis → System Identification → 
Workflow Routing → Task Execution → 
Quality Validation → Completion Report
```

### Phase 1: CLEAR Framework
- Clarity: Understand objectives
- Logic: Plan systematic approach
- Examples: Use existing patterns
- Adaptation: Handle edge cases
- Results: Define success criteria

### Phase 2: Alpha Evolve (Hassabis)
- Layer 1: Foundation (identify systems)
- Layer 2: Application (map to workflows)
- Layer 3: Integration (coordinate updates)
- Layer 4: Mastery (quality & completion)

### Phase 3: Execution
- Execute workflows
- Monitor progress
- Handle errors
- Validate quality

### Phase 4: Completion
- Aggregate results
- Generate report
- Notify user

---

## Database Schema

### garvis_jobs Table

```sql
CREATE TABLE garvis_jobs (
    id INTEGER PRIMARY KEY,
    job_id TEXT UNIQUE NOT NULL,
    one_thing TEXT NOT NULL,
    tasks TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    result TEXT,
    error TEXT,
    confidence_score REAL,
    escalation_needed INTEGER DEFAULT 0,
    escalation_reason TEXT
);
```

### garvis_execution_log Table

```sql
CREATE TABLE garvis_execution_log (
    id INTEGER PRIMARY KEY,
    job_id TEXT NOT NULL,
    step TEXT NOT NULL,
    action TEXT NOT NULL,
    result TEXT,
    timestamp TIMESTAMP
);
```

---

## Webhook Endpoints

### Garvis Orchestrator
- **URL:** `POST /webhook/garvis`
- **Payload:**
  ```json
  {
    "job_id": "garvis-abc123",
    "one_thing": "Complete Book 2",
    "tasks": ["Write story", "Update curriculum"],
    "context": "Optional context"
  }
  ```

### School Onboarding
- **URL:** `POST /webhook/school-onboarding`
- **Payload:**
  ```json
  {
    "school_name": "ABC Elementary",
    "email": "contact@school.edu",
    "contact_name": "John Doe"
  }
  ```

### Sales Automation
- **URL:** `POST /webhook/sales-automation`
- **Payload:**
  ```json
  {
    "type": "inquiry",
    "email": "lead@example.com",
    "name": "Jane Smith"
  }
  ```

### Website Update
- **URL:** `POST /webhook/website-update`
- **Payload:**
  ```json
  {
    "type": "content",
    "changes": ["Update homepage", "Add new page"]
  }
  ```

---

## System Identification

Garvis identifies systems from keywords:

- **Book:** book, story, episode, content
- **Curriculum:** curriculum, schema, lesson
- **Game:** game, unity, build, exercise
- **Website:** website, deploy, netlify, page
- **Sales:** email, sales, onboard, school

---

## Workflow Mapping

Tasks are mapped to workflows:

- Book tasks → `book-content-update` workflow
- Curriculum tasks → `curriculum-sync` workflow
- Game tasks → `unity-build` workflow
- Website tasks → `website-auto-update` workflow
- School tasks → `school-onboarding` workflow
- Sales tasks → `sales-automation` workflow
- General tasks → `full-integration` workflow

---

## Quality Validation

### Checks Performed:

1. **Task Completion:** All tasks completed successfully
2. **Integration Tests:** Systems integrated correctly
3. **Deployment Verification:** Deployments successful
4. **Content Quality:** Content meets standards
5. **Code Quality:** Code syntax valid

### Confidence Scoring:

- Start: 1.0 (100%)
- Task failure: -0.2 per failed task
- Integration failure: -0.15
- Deployment failure: -0.1
- Escalate if confidence < 0.75 (75%)

---

## Escalation Protocol

### Escalation Triggers:

1. Unclear requirements
2. Blocking errors
3. Low confidence (< 75%) + cannot proceed

### Escalation Flow:

```
Issue Detected → Garvis Tries to Resolve → 
Still Blocked → Create Escalation → 
User Answers → Garvis Resumes → 
Completes Everything
```

### Escalation Storage:

- Database: `garvis_jobs.escalation_needed = 1`
- File: `GARVIS-ESCALATIONS.md`

---

## Error Handling

### Error Types:

1. **Workflow Errors:** Webhook failures, timeout
2. **System Errors:** Missing files, permissions
3. **Quality Errors:** Validation failures
4. **Integration Errors:** System sync issues

### Error Recovery:

- Retry failed workflows
- Fallback to direct execution
- Escalate if cannot recover
- Log all errors for analysis

---

## Performance Metrics

### Tracking:

- Job creation time
- Execution time per task
- Total completion time
- Success rate
- Escalation rate

### Optimization:

- Parallel workflow execution
- Caching common operations
- Batch similar tasks
- Pre-validate inputs

---

## Security

### Credentials:

- Stored in n8n environment variables
- Never in code or logs
- Rotated regularly

### Access Control:

- Webhook authentication
- Job ID validation
- System permission checks

---

## Integration Points

### n8n Workflows:

- All workflows accessible via webhooks
- Environment variables for configuration
- Credential management in n8n

### Python Scripts:

- Execution engine
- Command interface
- Quality checks
- Dashboard generation

### File System:

- Job tracking database
- Escalation files
- Completion reports
- Log files

---

## Development

### Adding New Capabilities:

1. Create workflow in n8n
2. Add webhook endpoint
3. Update system identification logic
4. Add workflow mapping
5. Test end-to-end

### Extending Execution Engine:

1. Add new task type handler
2. Implement execution logic
3. Add quality checks
4. Update documentation

---

## Monitoring

### Dashboard:

```bash
python scripts/garvis-dashboard.py
```

### Logs:

- Execution logs in database
- Escalation file for visibility
- Job status for tracking

### Metrics:

- SIAFI percentage
- Success rate
- Average completion time
- Escalation count

---

**This is the technical foundation of Garvis. For user guide, see GARVIS-SYSTEM-GUIDE.md**

