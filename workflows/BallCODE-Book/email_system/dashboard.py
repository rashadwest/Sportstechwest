#!/usr/bin/env python3
"""
Email System Dashboard
Simple web dashboard for email system
"""

from flask import Flask, render_template_string, jsonify, request
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from storage import EmailStorage
    from analytics import EmailAnalytics
    from sales_pipeline import SalesPipeline
except ImportError:
    import storage
    import analytics
    import sales_pipeline
    EmailStorage = storage.EmailStorage
    EmailAnalytics = analytics.EmailAnalytics
    SalesPipeline = sales_pipeline.SalesPipeline

app = Flask(__name__)

storage = EmailStorage()
analytics = EmailAnalytics()
pipeline = SalesPipeline()

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>BallCODE Email System Dashboard</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #1a3d5c; }
        h2 { color: #4a90e2; margin-top: 0; }
        .stat { display: inline-block; margin: 10px 20px 10px 0; }
        .stat-value { font-size: 32px; font-weight: bold; color: #1a3d5c; }
        .stat-label { color: #666; font-size: 14px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #f8f9fa; color: #1a3d5c; }
        .badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
        .badge-success { background: #d4edda; color: #155724; }
        .badge-warning { background: #fff3cd; color: #856404; }
        .badge-info { background: #d1ecf1; color: #0c5460; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📧 BallCODE Email System Dashboard</h1>
        
        <div class="card">
            <h2>📊 Statistics</h2>
            <div id="stats">
                <div class="stat">
                    <div class="stat-value" id="total-emails">-</div>
                    <div class="stat-label">Total Emails</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="unread-emails">-</div>
                    <div class="stat-label">Unread</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="leads-count">-</div>
                    <div class="stat-label">Sales Leads</div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>📬 Recent Emails</h2>
            <div id="recent-emails">Loading...</div>
        </div>
        
        <div class="card">
            <h2>🎯 Sales Leads</h2>
            <div id="leads">Loading...</div>
        </div>
    </div>
    
    <script>
        async function loadStats() {
            const response = await fetch('/api/stats');
            const data = await response.json();
            document.getElementById('total-emails').textContent = data.total || 0;
            document.getElementById('unread-emails').textContent = data.unread || 0;
        }
        
        async function loadLeads() {
            const response = await fetch('/api/leads');
            const data = await response.json();
            document.getElementById('leads-count').textContent = data.count || 0;
            
            let html = '<table><tr><th>Name</th><th>Email</th><th>Company</th><th>Status</th></tr>';
            data.leads.slice(0, 10).forEach(lead => {
                html += `<tr>
                    <td>${lead.name || 'Unknown'}</td>
                    <td>${lead.email || ''}</td>
                    <td>${lead.company || ''}</td>
                    <td><span class="badge badge-info">${lead.status || 'new'}</span></td>
                </tr>`;
            });
            html += '</table>';
            document.getElementById('leads').innerHTML = html;
        }
        
        async function loadEmails() {
            const response = await fetch('/api/emails?limit=10');
            const data = await response.json();
            
            let html = '<table><tr><th>From</th><th>Subject</th><th>Date</th><th>Status</th></tr>';
            data.emails.forEach(email => {
                const status = email.read ? '<span class="badge badge-success">Read</span>' : '<span class="badge badge-warning">Unread</span>';
                html += `<tr>
                    <td>${email.from_address || ''}</td>
                    <td>${email.subject || 'No Subject'}</td>
                    <td>${email.date_received || ''}</td>
                    <td>${status}</td>
                </tr>`;
            });
            html += '</table>';
            document.getElementById('recent-emails').innerHTML = html;
        }
        
        async function loadAll() {
            await loadStats();
            await loadEmails();
            await loadLeads();
        }
        
        loadAll();
        setInterval(loadAll, 30000); // Refresh every 30 seconds
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """Dashboard home page"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/stats')
def api_stats():
    """API endpoint for statistics"""
    import sqlite3
    
    conn = sqlite3.connect(storage.db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM emails")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM emails WHERE read = 0")
    unread = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        "total": total,
        "unread": unread,
        "read": total - unread
    })

@app.route('/api/emails')
def api_emails():
    """API endpoint for emails"""
    limit = int(request.args.get('limit', 10))
    emails = storage.list_emails(limit=limit)
    return jsonify({"emails": emails})

@app.route('/api/leads')
def api_leads():
    """API endpoint for leads"""
    leads = pipeline.get_leads()
    return jsonify({"leads": leads, "count": len(leads)})

if __name__ == '__main__':
    print("🚀 Starting Email System Dashboard...")
    print("🌐 Dashboard available at: http://localhost:8080")
    print()
    
    app.run(host='0.0.0.0', port=8080, debug=False)

