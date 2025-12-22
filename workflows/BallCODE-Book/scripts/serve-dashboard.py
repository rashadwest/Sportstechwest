#!/usr/bin/env python3
"""
Simple HTTP server to serve the BallCODE dashboard
Run this to view the dashboard on localhost:8000

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import http.server
import socketserver
import os
from pathlib import Path

# Get project root
project_root = Path(__file__).parent.parent
os.chdir(project_root)

PORT = 8000

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Serve dashboard.html for root path
        if self.path == '/' or self.path == '/dashboard.html':
            self.path = '/dashboard.html'
        return super().do_GET()
    
    def do_POST(self):
        if self.path == '/refresh-dashboard':
            # Trigger dashboard update
            import subprocess
            try:
                result = subprocess.run(
                    ['python3', 'scripts/update-dashboard.py'],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(f'{{"status": "error", "message": "{str(e)}"}}'.encode())
        else:
            self.send_response(404)
            self.end_headers()

def main():
    """Start the dashboard server."""
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print(f"🚀 BallCODE Dashboard Server")
        print(f"   Serving on: http://localhost:{PORT}")
        print(f"   Dashboard: http://localhost:{PORT}/dashboard.html")
        print(f"   Press Ctrl+C to stop")
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == '__main__':
    main()


