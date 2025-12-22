#!/usr/bin/env python3
"""
Recreate Unity Build Orchestrator workflow from scratch
Fix ALL potential bugs and validate end-to-end

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import os

def recreate_workflow():
    """Recreate the workflow with proper structure, fixing all known issues"""
    
    # Build the workflow from scratch with correct structure
    workflow = {
        "name": "AIMCODE (Demis) - Unity Build Orchestrator (13 nodes, MAC GUARDED)",
        "nodes": [],
        "connections": {},
        "settings": {
            "executionOrder": "v1",
            "timezone": "America/New_York"
        }
    }
    
    # Node 1: Scheduled Trigger
    workflow["nodes"].append({
        "parameters": {
            "rule": {
                "cronExpression": "0 * * * *"
            }
        },
        "id": "scheduled-trigger",
        "name": "Scheduled Trigger (Hourly) [DISABLED ON DEV]",
        "type": "n8n-nodes-base.scheduleTrigger",
        "typeVersion": 1.1,
        "position": [240, 240],
        "disabled": True
    })
    
    # Node 2: Webhook Trigger - NO OPTIONS
    workflow["nodes"].append({
        "parameters": {
            "httpMethod": "POST",
            "path": "unity-build",
            "responseMode": "responseNode"
        },
        "id": "webhook-trigger",
        "name": "Webhook Trigger (Manual/API)",
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 1,
        "position": [240, 420],
        "webhookId": "unity-build-webhook"
    })
    
    # Node 3: Normalize Input
    workflow["nodes"].append({
        "parameters": {
            "jsCode": "// L1 (Foundation): normalize trigger input\nconst input = $input.item.json;\nconst body = input.body || {};\n\nconst isWebhook = !!(body && (body.request || body.message || body.prompt || body.branch));\nconst triggerType = isWebhook ? 'webhook' : 'scheduled';\n\nconst request = String(body.request || body.message || body.prompt || 'Scheduled build');\nconst branch = String(body.branch || (body.ref ? String(body.ref).replace('refs/heads/', '') : 'main'));\n\nreturn {\n  json: {\n    request,\n    branch,\n    triggerType,\n    isWebhook,\n    timestamp: new Date().toISOString(),\n    proceed: true\n  }\n};"
        },
        "id": "normalize-input",
        "name": "Normalize Input (AIMCODE L1)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [520, 330]
    })
    
    # Node 4: Env Preflight
    workflow["nodes"].append({
        "parameters": {
            "jsCode": "// L1 (Foundation): env/credential preflight + DEV guardrails\n// Guardrail goal: prevent the Mac instance from accidentally running scheduled builds.\n//\n// Set on Mac:\n// - N8N_INSTANCE_ROLE=dev\n//\n// Set on Pi/prod:\n// - N8N_INSTANCE_ROLE=prod\n//\n// Override (if you really want scheduled builds on dev):\n// - ALLOW_SCHEDULED_BUILDS=1\n\nconst requiredEnv = [\n  'GITHUB_REPO_OWNER',\n  'GITHUB_REPO_NAME',\n  'GITHUB_WORKFLOW_FILE',\n  'NETLIFY_SITE_ID'\n];\n\nconst missing = requiredEnv.filter((k) => !($env[k] || '').toString().trim());\nif (missing.length) {\n  return {\n    json: {\n      ...$json,\n      proceed: false,\n      status: 'fail',\n      error: `Missing required env var(s): ${missing.join(', ')}`,\n    }\n  };\n}\n\nconst role = ($env.N8N_INSTANCE_ROLE || 'dev').toString().trim().toLowerCase();\nconst allowScheduled = ($env.ALLOW_SCHEDULED_BUILDS || '').toString().trim() === '1';\n\n// Block scheduled trigger on dev by default.\nif ($json.triggerType === 'scheduled' && role !== 'prod' && !allowScheduled) {\n  return {\n    json: {\n      ...$json,\n      proceed: false,\n      status: 'skipped',\n      skipReason: `Scheduled builds are blocked on ${role}. Set N8N_INSTANCE_ROLE=prod (recommended only on Pi) or set ALLOW_SCHEDULED_BUILDS=1 to override.`,\n      instanceRole: role,\n      allowScheduled\n    }\n  };\n}\n\nreturn {\n  json: {\n    ...$json,\n    proceed: true,\n    instanceRole: role,\n    allowScheduled\n  }\n};"
        },
        "id": "env-preflight",
        "name": "Env Preflight + Dev Guardrails (AIMCODE L1)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [760, 330]
    })
    
    # Node 5: Acquire Lock
    workflow["nodes"].append({
        "parameters": {
            "jsCode": "// L1 (Foundation): overlap prevention via workflow static data lock (TTL)\nconst MAX_LOCK_SECONDS = 55 * 60; // fits hourly schedule\nconst nowMs = Date.now();\n\nlet staticData;\ntry {\n  staticData = $getWorkflowStaticData('global');\n} catch (e) {\n  // If static data isn't available (manual test), proceed without lock\n  return { json: { ...$json, lock: { enabled: false, reason: 'staticData unavailable' }, proceed: true } };\n}\n\nconst lockUntilMs = Number(staticData.lockUntilMs || 0);\nconst lockOwner = String(staticData.lockOwner || '');\n\nif (lockUntilMs && nowMs < lockUntilMs) {\n  return {\n    json: {\n      ...$json,\n      proceed: false,\n      status: 'skipped',\n      skipReason: `Locked until ${new Date(lockUntilMs).toISOString()} (owner=${lockOwner})`,\n      lock: { enabled: true, acquired: false, lockUntilMs, lockOwner }\n    }\n  };\n}\n\nconst owner = `${$json.triggerType}:${$json.branch}:${$json.timestamp}`;\nstaticData.lockUntilMs = nowMs + MAX_LOCK_SECONDS * 1000;\nstaticData.lockOwner = owner;\nstaticData.lastAttemptAt = new Date(nowMs).toISOString();\n\nreturn {\n  json: {\n    ...$json,\n    proceed: true,\n    lock: { enabled: true, acquired: true, lockUntilMs: staticData.lockUntilMs, lockOwner: owner }\n  }\n};"
        },
        "id": "acquire-lock",
        "name": "Acquire Lock (AIMCODE L1)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [1000, 330]
    })
    
    # Node 6: Proceed? (IF node)
    workflow["nodes"].append({
        "parameters": {
            "conditions": {
                "boolean": [
                    {
                        "value1": "={{ $json.proceed }}",
                        "value2": True
                    }
                ]
            }
        },
        "id": "if-proceed",
        "name": "Proceed?",
        "type": "n8n-nodes-base.if",
        "typeVersion": 1,
        "position": [1240, 330]
    })
    
    # Node 7: Dispatch GitHub Build - Use options.headers (original format)
    workflow["nodes"].append({
        "parameters": {
            "method": "POST",
            "url": "https://api.github.com/repos/{{ $env.GITHUB_REPO_OWNER }}/{{ $env.GITHUB_REPO_NAME }}/dispatches",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": True,
            "sendBody": True,
            "bodyContentType": "json",
            "specifyBody": "json",
            "jsonBody": "={{ JSON.stringify({ event_type: 'unity-build', client_payload: { request: $json.request, triggerType: $json.triggerType, branch: $json.branch, timestamp: $json.timestamp, instanceRole: $json.instanceRole } }) }}",
            "options": {
                "headers": {
                    "Accept": "application/vnd.github.v3+json"
                }
            }
        },
        "id": "dispatch-build",
        "name": "Dispatch GitHub Build (AIMCODE L2)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.1,
        "position": [1480, 240],
        "credentials": {
            "httpHeaderAuth": {
                "id": "github-actions-token",
                "name": "GitHub Actions Token"
            }
        }
    })
    
    # Node 8: Wait
    workflow["nodes"].append({
        "parameters": {
            "amount": 3,
            "unit": "minutes"
        },
        "id": "wait",
        "name": "Wait (3 min)",
        "type": "n8n-nodes-base.wait",
        "typeVersion": 1,
        "position": [1700, 240]
    })
    
    # Node 9: Check GitHub Run - Use options.headers (original format)
    workflow["nodes"].append({
        "parameters": {
            "method": "GET",
            "url": "https://api.github.com/repos/{{ $env.GITHUB_REPO_OWNER }}/{{ $env.GITHUB_REPO_NAME }}/actions/workflows/{{ $env.GITHUB_WORKFLOW_FILE }}/runs?per_page=1",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": True,
            "options": {
                "headers": {
                    "Accept": "application/vnd.github.v3+json"
                }
            }
        },
        "id": "check-github-run",
        "name": "Check Latest GitHub Run (AIMCODE L3)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.1,
        "position": [1920, 240],
        "credentials": {
            "httpHeaderAuth": {
                "id": "github-actions-token",
                "name": "GitHub Actions Token"
            }
        }
    })
    
    # Node 10: Check Netlify - NO OPTIONS
    workflow["nodes"].append({
        "parameters": {
            "method": "GET",
            "url": "https://api.netlify.com/api/v1/sites/{{ $env.NETLIFY_SITE_ID }}/deploys?per_page=1",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": True
        },
        "id": "check-netlify",
        "name": "Check Latest Netlify Deploy (AIMCODE L3)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.1,
        "position": [2140, 240],
        "credentials": {
            "httpHeaderAuth": {
                "id": "netlify-api-token",
                "name": "Netlify API Token"
            }
        }
    })
    
    # Node 11: Finalize
    workflow["nodes"].append({
        "parameters": {
            "jsCode": "// L4 (Mastery): compile report + release lock (best-effort)\nlet staticData;\ntry {\n  staticData = $getWorkflowStaticData('global');\n} catch (e) {\n  staticData = null;\n}\n\nlet gh = { ok: null, status: 'unknown', conclusion: 'unknown', url: '' };\ntry {\n  const runs = $items('Check Latest GitHub Run (AIMCODE L3)')[0].json.workflow_runs || [];\n  const latest = runs[0] || {};\n  gh.status = latest.status || 'unknown';\n  gh.conclusion = latest.conclusion || 'unknown';\n  gh.url = latest.html_url || '';\n  gh.ok = (gh.status === 'completed' && gh.conclusion === 'success');\n} catch (e) {\n  gh = { ok: null, status: 'unavailable', conclusion: 'unavailable', url: '' };\n}\n\nlet nf = { ok: null, state: 'unknown', deployUrl: '' };\ntry {\n  const deploys = $items('Check Latest Netlify Deploy (AIMCODE L3)')[0].json;\n  const latest = Array.isArray(deploys) ? (deploys[0] || {}) : {};\n  nf.state = latest.state || 'unknown';\n  nf.deployUrl = latest.deploy_url || '';\n  nf.ok = (nf.state === 'ready' || nf.state === 'published');\n} catch (e) {\n  nf = { ok: null, state: 'unavailable', deployUrl: '' };\n}\n\nif (staticData && $json.lock?.enabled && $json.lock?.acquired) {\n  staticData.lockUntilMs = 0;\n  staticData.lockOwner = '';\n  staticData.lastDispatchAt = $json.timestamp;\n}\n\nconst siteUrl = 'https://' + ($env.NETLIFY_SITE_NAME || 'ballcode-game') + '.netlify.app';\nconst status = $json.status || ($json.proceed ? 'ok' : 'skipped');\nconst message = $json.error\n  ? `Preflight failed: ${$json.error}`\n  : ($json.skipReason ? `Skipped: ${$json.skipReason}` : `Build dispatched. GH=${gh.status}/${gh.conclusion} NF=${nf.state}`);\n\nreturn {\n  json: {\n    status,\n    request: $json.request,\n    triggerType: $json.triggerType,\n    isWebhook: $json.isWebhook,\n    branch: $json.branch,\n    timestamp: $json.timestamp,\n    instanceRole: $json.instanceRole,\n    github: gh,\n    netlify: nf,\n    siteUrl,\n    message\n  }\n};"
        },
        "id": "finalize",
        "name": "Finalize Report + Release Lock (AIMCODE L4)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [2360, 240]
    })
    
    # Node 12: Webhook Response? (IF node)
    workflow["nodes"].append({
        "parameters": {
            "conditions": {
                "boolean": [
                    {
                        "value1": "={{ $json.isWebhook }}",
                        "value2": True
                    }
                ]
            }
        },
        "id": "if-webhook",
        "name": "Webhook Response?",
        "type": "n8n-nodes-base.if",
        "typeVersion": 1,
        "position": [2580, 240]
    })
    
    # Node 13: Webhook Response - CRITICAL: NO OPTIONS AT ALL
    workflow["nodes"].append({
        "parameters": {
            "respondWith": "json",
            "responseBody": "={{ $json }}"
        },
        "id": "webhook-response",
        "name": "Webhook Response",
        "type": "n8n-nodes-base.respondToWebhook",
        "typeVersion": 1,
        "position": [2800, 240]
    })
    
    # Build connections
    workflow["connections"] = {
        "Scheduled Trigger (Hourly) [DISABLED ON DEV]": {
            "main": [[{"node": "Normalize Input (AIMCODE L1)", "type": "main", "index": 0}]]
        },
        "Webhook Trigger (Manual/API)": {
            "main": [[{"node": "Normalize Input (AIMCODE L1)", "type": "main", "index": 0}]]
        },
        "Normalize Input (AIMCODE L1)": {
            "main": [[{"node": "Env Preflight + Dev Guardrails (AIMCODE L1)", "type": "main", "index": 0}]]
        },
        "Env Preflight + Dev Guardrails (AIMCODE L1)": {
            "main": [[{"node": "Acquire Lock (AIMCODE L1)", "type": "main", "index": 0}]]
        },
        "Acquire Lock (AIMCODE L1)": {
            "main": [[{"node": "Proceed?", "type": "main", "index": 0}]]
        },
        "Proceed?": {
            "main": [
                [{"node": "Dispatch GitHub Build (AIMCODE L2)", "type": "main", "index": 0}],
                [{"node": "Finalize Report + Release Lock (AIMCODE L4)", "type": "main", "index": 0}]
            ]
        },
        "Dispatch GitHub Build (AIMCODE L2)": {
            "main": [[{"node": "Wait (3 min)", "type": "main", "index": 0}]]
        },
        "Wait (3 min)": {
            "main": [[{"node": "Check Latest GitHub Run (AIMCODE L3)", "type": "main", "index": 0}]]
        },
        "Check Latest GitHub Run (AIMCODE L3)": {
            "main": [[{"node": "Check Latest Netlify Deploy (AIMCODE L3)", "type": "main", "index": 0}]]
        },
        "Check Latest Netlify Deploy (AIMCODE L3)": {
            "main": [[{"node": "Finalize Report + Release Lock (AIMCODE L4)", "type": "main", "index": 0}]]
        },
        "Finalize Report + Release Lock (AIMCODE L4)": {
            "main": [[{"node": "Webhook Response?", "type": "main", "index": 0}]]
        },
        "Webhook Response?": {
            "main": [[{"node": "Webhook Response", "type": "main", "index": 0}]]
        }
    }
    
    return workflow

def validate_workflow(workflow):
    """Validate workflow structure and check for all known issues"""
    issues = []
    warnings = []
    
    # Check node count
    node_count = len(workflow.get("nodes", []))
    if node_count != 13:
        issues.append(f"Node count is {node_count}, expected 13")
    
    # Check each node
    for i, node in enumerate(workflow.get("nodes", []), 1):
        node_type = node.get("type", "")
        node_name = node.get("name", "Unknown")
        params = node.get("parameters", {})
        type_version = node.get("typeVersion", "")
        
        # Check for problematic options
        if "options" in params:
            opt_val = params["options"]
            if opt_val == {} or opt_val is None:
                issues.append(f"Node {i} ({node_name}): Has empty options object")
            elif "respondToWebhook" in node_type and type_version == 1:
                issues.append(f"Node {i} ({node_name}): respondToWebhook v1 should NOT have options")
            elif "webhook" in node_type.lower() and type_version == 1:
                issues.append(f"Node {i} ({node_name}): Webhook v1 should not have options")
        
        # Check respondToWebhook specifically
        if "respondToWebhook" in node_type:
            if type_version == 1:
                if "options" in params:
                    issues.append(f"Node {i} ({node_name}): respondToWebhook v1 MUST NOT have options")
                # Check allowed parameters
                allowed_params = ["respondWith", "responseBody", "responseCode", "responseHeaders"]
                for param in params:
                    if param not in allowed_params:
                        warnings.append(f"Node {i} ({node_name}): respondToWebhook has unexpected parameter: {param}")
    
    return issues, warnings

def main():
    print("🔧 Recreating Unity Build Orchestrator from scratch...")
    print()
    
    # Recreate workflow
    workflow = recreate_workflow()
    
    # Validate
    print("✅ Validating workflow structure...")
    issues, warnings = validate_workflow(workflow)
    
    if issues:
        print(f"❌ Found {len(issues)} critical issues:")
        for issue in issues:
            print(f"   - {issue}")
        return 1
    
    if warnings:
        print(f"⚠️  Found {len(warnings)} warnings:")
        for warning in warnings[:5]:
            print(f"   - {warning}")
    
    print(f"✅ Workflow is valid! ({len(workflow['nodes'])} nodes)")
    print()
    
    # Save to file
    output_file = "/tmp/orchestrator-recreated-clean.json"
    with open(output_file, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    print(f"✅ Recreated workflow saved to: {output_file}")
    print()
    print("📋 Summary:")
    print(f"   - Nodes: {len(workflow['nodes'])}")
    print(f"   - Connections: {len(workflow['connections'])}")
    print(f"   - Issues: {len(issues)}")
    print(f"   - Warnings: {len(warnings)}")
    print()
    print("✅ Ready for import!")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
