# n8n Routes Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Complete reference for all n8n instances and their ports/routes

**Last Updated:** December 2025

---

## 🎯 n8n Instance Routes

### 1. Mac Native n8n
- **Process:** Node.js native installation
- **URL:** `http://localhost:5678`
- **Port:** `5678` (direct)
- **Type:** Native node process
- **Use Case:** Manual testing, one-off workflow edits, non-24/7 runs
- **Health Check:** `curl http://localhost:5678/healthz`
- **Status:** Development/testing

### 2. Raspberry Pi n8n (Production)
- **URL:** `http://192.168.1.226:5678`
- **Port:** `5678`
- **Type:** Docker container (on Pi)
- **Use Case:** Always-on automation, scheduled triggers, production workflows
- **Health Check:** `curl http://192.168.1.226:5678/healthz`
- **Status:** Production automation

---

## 📋 Quick Reference

| Instance | URL | Port | Type | Purpose |
|----------|-----|------|------|---------|
| **Mac Native** | `http://localhost:5678` | 5678 | Native | Primary n8n instance |
| **Raspberry Pi** | `http://192.168.1.226:5678` | 5678 | Docker | Production Automation |

---

## 🔧 Configuration Files

### Profile System
- **Local Profile:** `./setup-n8n-terminal.sh local` → Uses `localhost:5678` (Mac Native)
- **Pi Profile:** `./setup-n8n-terminal.sh pi` → Uses `192.168.1.226:5678` (Raspberry Pi)

### Environment Files
- `.n8n-env.local` → Template for Mac Native (port 5678)
- `.n8n-env.pi` → Template for Raspberry Pi (port 5678)
- `.n8n-env` → Active profile (copied from template)

---

## 🚀 Common Commands

### Check Status
```bash
# Mac Native
curl http://localhost:5678/healthz
ps aux | grep n8n | grep -v grep

# Raspberry Pi
curl http://192.168.1.226:5678/healthz
```

### Access in Browser
- Mac Native: `http://localhost:5678`
- Raspberry Pi: `http://192.168.1.226:5678`

---

## 📝 Notes

- **Port 5678** is the standard n8n port
- **Different machines** = No port conflicts (localhost vs IP address)
- **Profile system** keeps Mac and Pi configurations separate
- **Mac Native** is the primary n8n instance for workflow management

---

**Memory:** This document serves as the canonical reference for all n8n routes and should be consulted when configuring or troubleshooting n8n instances.

