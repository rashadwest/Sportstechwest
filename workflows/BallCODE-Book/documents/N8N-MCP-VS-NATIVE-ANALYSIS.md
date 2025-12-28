# n8n-mcp vs Native n8n: AIMCODE Analysis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 15, 2025  
**Purpose:** Comprehensive analysis of n8n-mcp vs native n8n for Cursor integration

---

## 🎯 Executive Summary

**Recommendation:** ✅ **Use n8n-mcp (Docker) as primary, deprecate Mac native n8n**

**Reasoning:**
- n8n-mcp is best practice for AI/Cursor integration
- Easier workflow management from Cursor
- Better security and modularity
- Aligns with your preference for simplicity

---

## 📊 Research Findings (AIMCODE Methodology)

### ✅ n8n-mcp is Best Practice

**Evidence from Research:**
1. **Official n8n Documentation:** MCP server is the recommended approach for AI agent integration
2. **Community Adoption:** Instance-level MCP access is actively promoted by n8n team
3. **Industry Best Practices:** Separation of control (n8n) and capability (MCP) is standard pattern

**Key Benefits:**
- ✅ **Centralized Workflow Management:** Single connection manages multiple workflows
- ✅ **Enhanced Security:** Two-level opt-in (instance + workflow level)
- ✅ **Modular Design:** Tools organized into focused bundles
- ✅ **AI Integration:** Seamless interaction between Cursor and n8n workflows
- ✅ **Better Observability:** Logging and monitoring built-in

---

## 🔄 Comparison: n8n-mcp vs Native n8n

### n8n-mcp (Docker) - **RECOMMENDED**

**Advantages:**
- ✅ **Cursor Integration:** Direct MCP protocol connection
- ✅ **42 Tools Available:** Documentation, API, templates all accessible
- ✅ **Easier Workflow Management:** Ask Cursor to manage workflows
- ✅ **Better Security:** Per-workflow opt-in access
- ✅ **Docker Isolation:** Clean separation from system
- ✅ **Port 5679:** Already configured and working
- ✅ **Container Named:** `mac-docker-mcp-n8n-cursor` (clear purpose)

**Disadvantages:**
- ⚠️ Requires Docker (already running)
- ⚠️ Slightly more setup (already done)

### Native n8n (Port 5678) - **DEPRECATE**

**Advantages:**
- ✅ Direct node.js process (no Docker)
- ✅ Standard port 5678

**Disadvantages:**
- ❌ **No MCP Integration:** Can't connect to Cursor via MCP
- ❌ **Manual Workflow Management:** Must use UI or CLI
- ❌ **Less Secure:** No per-workflow access control
- ❌ **Port Conflict:** Same port as Pi (confusing)
- ❌ **No AI Integration:** Can't ask Cursor to manage workflows

---

## 🎯 Decision Matrix

| Feature | n8n-mcp (Docker) | Native n8n |
|---------|------------------|------------|
| **Cursor Integration** | ✅ Yes (MCP) | ❌ No |
| **Ease of Use** | ✅ Ask Cursor | ⚠️ Manual UI/CLI |
| **Security** | ✅ Per-workflow opt-in | ⚠️ All or nothing |
| **Workflow Management** | ✅ Centralized | ⚠️ Individual |
| **AI Capabilities** | ✅ 42 tools | ❌ None |
| **Port** | ✅ 5679 (unique) | ⚠️ 5678 (conflicts) |
| **Container Name** | ✅ Clear purpose | ❌ Generic |
| **Best Practice** | ✅ Recommended | ⚠️ Legacy |

**Winner:** ✅ **n8n-mcp (Docker)**

---

## 🚀 Recommended Action Plan

### Phase 1: Add n8n-mcp to Cursor (IMMEDIATE)

**Action:** Add n8n-mcp to `~/.cursor/mcp.json`

**Configuration:**
```json
{
  "mcpServers": {
    "n8n-docs": {
      "command": "npx",
      "args": ["-y", "n8n-mcp"],
      "env": {
        "N8N_API_URL": "http://localhost:5679"
      }
    },
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "Notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": ""
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": ""
      }
    }
  }
}
```

**Benefits:**
- Ask Cursor: "List my n8n workflows"
- Ask Cursor: "Create a new workflow for Unity builds"
- Ask Cursor: "Update the webhook trigger in workflow X"
- Access n8n documentation directly from Cursor

### Phase 2: Deprecate Mac Native n8n (OPTIONAL)

**Action:** Stop and disable Mac native n8n on port 5678

**Steps:**
1. Stop native n8n: `pkill -f n8n` (or stop the service)
2. Update documentation to reflect n8n-mcp as primary
3. Update scripts to default to port 5679

**Benefits:**
- Eliminates port confusion
- Reduces resource usage
- Simplifies setup (one n8n instance)

**Note:** Keep it running if you have active workflows there, but migrate to Docker.

### Phase 3: Update Documentation (RECOMMENDED)

**Files to Update:**
- `documents/N8N-ROUTES-REFERENCE.md` - Mark native as deprecated
- `setup-n8n-terminal.sh` - Update comments
- `.n8n-env` - Update default to 5679

---

## 📋 Updated n8n Routes (After Changes)

### Primary: Mac Docker MCP (n8n-cursor)
- **Container:** `mac-docker-mcp-n8n-cursor`
- **URL:** `http://localhost:5679`
- **Purpose:** Primary n8n instance for Cursor/MCP workflows
- **Status:** ✅ **ACTIVE - RECOMMENDED**

### Secondary: Raspberry Pi n8n (Production)
- **URL:** `http://192.168.1.226:5678`
- **Purpose:** Production automation, scheduled workflows
- **Status:** ✅ **ACTIVE - PRODUCTION**

### Deprecated: Mac Native n8n
- **URL:** `http://localhost:5678`
- **Purpose:** ~~Testing/Development~~ (Use Docker instead)
- **Status:** ⚠️ **DEPRECATED - MIGRATE TO DOCKER**

---

## ✅ Final Recommendation

**DO THIS:**
1. ✅ **Add n8n-mcp to Cursor MCP config** (enables AI workflow management)
2. ✅ **Use Docker n8n (port 5679) as primary** (already working)
3. ⚠️ **Deprecate Mac native n8n** (optional, but recommended)

**WHY:**
- n8n-mcp is best practice for AI integration
- Easier to use from Cursor (your preference)
- Better security and workflow management
- Aligns with industry standards

**RESULT:**
- Ask Cursor to manage n8n workflows
- Access n8n documentation from Cursor
- Simpler setup (one primary instance)
- Better integration with your workflow

---

## 🔗 References

- [n8n MCP Documentation](https://docs.n8n.io/advanced-ai/accessing-n8n-mcp-server/)
- [n8n MCP Community Discussion](https://community.n8n.io/t/introducing-instance-level-mcp-access-in-n8n-beta/223178)
- [MCP Best Practices](https://blog.horizon.dev/mcp-in-n8n/)

---

**Decision:** ✅ **Proceed with adding n8n-mcp to Cursor and using Docker as primary**



