#!/usr/bin/env python3
"""
Email System API Server
REST API endpoints for email operations
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from storage import EmailStorage
    from sender import EmailSender
    from sales_pipeline import SalesPipeline
except ImportError:
    import storage
    import sender
    import sales_pipeline
    EmailStorage = storage.EmailStorage
    EmailSender = sender.EmailSender
    SalesPipeline = sales_pipeline.SalesPipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for web access

# Initialize components
storage = EmailStorage()
sender = EmailSender()
pipeline = SalesPipeline()

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "email-system"})

@app.route('/api/emails', methods=['GET'])
def list_emails():
    """List emails"""
    folder = request.args.get('folder', 'inbox')
    unread_only = request.args.get('unread', 'false').lower() == 'true'
    limit = int(request.args.get('limit', 50))
    
    emails = storage.list_emails(folder=folder, unread_only=unread_only, limit=limit)
    return jsonify({"emails": emails, "count": len(emails)})

@app.route('/api/emails/<int:email_id>', methods=['GET'])
def get_email(email_id):
    """Get single email"""
    email = storage.get_email(email_id)
    if email:
        return jsonify(email)
    return jsonify({"error": "Email not found"}), 404

@app.route('/api/emails', methods=['POST'])
def send_email():
    """Send email"""
    data = request.json
    
    success = sender.send(
        to_address=data.get('to'),
        subject=data.get('subject'),
        body=data.get('body'),
        from_address=data.get('from', 'noreply@ballcode.co'),
        html_body=data.get('html_body')
    )
    
    if success:
        return jsonify({"status": "sent", "message": "Email sent successfully"})
    return jsonify({"status": "failed", "message": "Failed to send email"}), 500

@app.route('/api/emails/<int:email_id>/read', methods=['POST'])
def mark_read(email_id):
    """Mark email as read"""
    storage.mark_read(email_id, read=True)
    return jsonify({"status": "updated"})

@app.route('/api/emails/<int:email_id>', methods=['DELETE'])
def delete_email(email_id):
    """Delete email"""
    storage.delete_email(email_id)
    return jsonify({"status": "deleted"})

@app.route('/api/search', methods=['GET'])
def search_emails():
    """Search emails"""
    query = request.args.get('q', '')
    folder = request.args.get('folder', 'inbox')
    
    if not query:
        return jsonify({"error": "Query parameter 'q' required"}), 400
    
    results = storage.search_emails(query=query, folder=folder)
    return jsonify({"results": results, "count": len(results)})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get email statistics"""
    import sqlite3
    
    conn = sqlite3.connect(storage.db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM emails")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM emails WHERE read = 0")
    unread = cursor.fetchone()[0]
    
    cursor.execute("SELECT folder, COUNT(*) FROM emails GROUP BY folder")
    folders = dict(cursor.fetchall())
    
    conn.close()
    
    return jsonify({
        "total": total,
        "unread": unread,
        "read": total - unread,
        "folders": folders
    })

@app.route('/api/leads', methods=['GET'])
def get_leads():
    """Get sales leads"""
    status = request.args.get('status')
    leads = pipeline.get_leads(status=status)
    return jsonify({"leads": leads, "count": len(leads)})

@app.route('/api/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint for receiving emails"""
    data = request.json
    
    # Process incoming email data
    # This would integrate with external email services
    
    return jsonify({"status": "received"})

if __name__ == '__main__':
    print("🚀 Starting Email System API Server...")
    print("📡 API available at: http://localhost:5000")
    print("📚 API Documentation:")
    print("   GET  /api/health - Health check")
    print("   GET  /api/emails - List emails")
    print("   POST /api/emails - Send email")
    print("   GET  /api/emails/<id> - Get email")
    print("   GET  /api/search?q=query - Search emails")
    print("   GET  /api/stats - Statistics")
    print("   GET  /api/leads - Sales leads")
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=False)



