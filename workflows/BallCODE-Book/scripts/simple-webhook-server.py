#!/usr/bin/env python3
"""
Simple Webhook Server - Alternative to n8n
Purpose: Receive GitHub webhooks and trigger Unity builds
Cost: FREE (runs on your Mac or Pi)
"""

from flask import Flask, request, jsonify
import subprocess
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuration
BUILD_SCRIPT = os.path.join(os.path.dirname(__file__), "custom-unity-build-orchestrator.py")
PORT = int(os.getenv("WEBHOOK_PORT", "5000"))
HOST = os.getenv("WEBHOOK_HOST", "0.0.0.0")  # 0.0.0.0 = listen on all interfaces

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "build_script": BUILD_SCRIPT,
        "script_exists": os.path.exists(BUILD_SCRIPT)
    })

@app.route('/webhook/build', methods=['POST'])
def webhook_build():
    """Receive webhook and trigger build"""
    try:
        # Get webhook data
        data = request.get_json() or {}
        event_type = request.headers.get('X-GitHub-Event', 'manual')
        
        # Log webhook
        print(f"[{datetime.now()}] Webhook received: {event_type}")
        
        # Trigger build
        if not os.path.exists(BUILD_SCRIPT):
            return jsonify({
                "error": "Build script not found",
                "path": BUILD_SCRIPT
            }), 500
        
        # Run build in background (non-blocking)
        process = subprocess.Popen(
            ["python3", BUILD_SCRIPT],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(BUILD_SCRIPT)
        )
        
        return jsonify({
            "status": "build_triggered",
            "build_id": process.pid,
            "event": event_type,
            "timestamp": datetime.now().isoformat()
        }), 202  # 202 Accepted (async)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/webhook/github', methods=['POST'])
def webhook_github():
    """GitHub webhook endpoint"""
    return webhook_build()

@app.route('/build/trigger', methods=['POST', 'GET'])
def trigger_build():
    """Manual build trigger endpoint"""
    return webhook_build()

@app.route('/build/status', methods=['GET'])
def build_status():
    """Get build status (simple - checks if build is running)"""
    # Check if build script exists
    if not os.path.exists(BUILD_SCRIPT):
        return jsonify({
            "status": "error",
            "message": "Build script not found"
        }), 500
    
    # Simple status check (could be enhanced to read status files)
    return jsonify({
        "status": "ready",
        "build_script": BUILD_SCRIPT,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Simple Webhook Server - Unity Build Trigger")
    print("=" * 60)
    print(f"Build Script: {BUILD_SCRIPT}")
    print(f"Script Exists: {os.path.exists(BUILD_SCRIPT)}")
    print(f"Listening on: http://{HOST}:{PORT}")
    print("=" * 60)
    print("\nEndpoints:")
    print(f"  POST http://localhost:{PORT}/webhook/build - Trigger build")
    print(f"  POST http://localhost:{PORT}/webhook/github - GitHub webhook")
    print(f"  GET  http://localhost:{PORT}/build/trigger - Manual trigger")
    print(f"  GET  http://localhost:{PORT}/build/status - Check status")
    print(f"  GET  http://localhost:{PORT}/health - Health check")
    print("\nStarting server...")
    print("=" * 60)
    
    app.run(host=HOST, port=PORT, debug=False)


