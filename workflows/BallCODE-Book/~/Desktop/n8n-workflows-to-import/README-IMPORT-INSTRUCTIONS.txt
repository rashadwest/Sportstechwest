📥 n8n Workflows - Import Instructions

Import these workflows to Pi n8n: http://192.168.1.226:5678

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 WORKFLOWS TO IMPORT (Import in this order):

1. n8n-ballcode-full-integration-workflow.json
   → Phase 1 - Full Integration Workflow

2. n8n-screenshot-to-fix-workflow.json
   → Phase 1 - Screenshot to Fix Workflow

3. n8n-book-content-update-workflow.json
   → Phase 2 - Book Content Update Workflow

4. n8n-curriculum-sync-workflow.json
   → Phase 2 - Curriculum Schema Sync Workflow

5. n8n-game-exercise-integration-workflow.json
   → Phase 2 - Game Exercise Integration Workflow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 HOW TO IMPORT:

1. Open Pi n8n UI: http://192.168.1.226:5678

2. Click "Workflows" in left sidebar

3. Click "Import from File" button (top right)

4. Select one workflow file from this folder

5. Click "Import"

6. Repeat for all 5 workflows

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ AFTER IMPORTING - ACTIVATE WORKFLOWS:

For each imported workflow:

1. Open the workflow in n8n
2. Toggle "Inactive" → "Active" (top-right switch)
3. Switch should turn green/blue when active

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧪 TEST AFTER ACTIVATION:

# Test Book Content Update
curl -X POST "http://192.168.1.226:5678/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'

# Test Curriculum Sync
curl -X POST "http://192.168.1.226:5678/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

# Test Game Exercise Integration
curl -X POST "http://192.168.1.226:5678/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Done! All workflows are ready to import.



