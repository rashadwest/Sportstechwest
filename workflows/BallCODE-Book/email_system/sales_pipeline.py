"""
Sales Pipeline System
Automated sales pipeline and funnel for products/services
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
try:
    from .storage import EmailStorage
    from .apollo_integration import ApolloIntegration
    from .slack_notifier import SlackNotifier
except ImportError:
    from storage import EmailStorage
    from apollo_integration import ApolloIntegration
    from slack_notifier import SlackNotifier

class SalesPipeline:
    """Sales pipeline and funnel system"""
    
    def __init__(self, config_file: str = "email_config.json"):
        self.config_file = Path(__file__).parent / config_file
        self.storage = EmailStorage()
        self.apollo = ApolloIntegration(config_file)
        self.slack = SlackNotifier(config_file)
        self.pipeline_db = Path(__file__).parent / "sales_pipeline.db"
        self._init_pipeline_db()
    
    def _init_pipeline_db(self):
        """Initialize sales pipeline database"""
        import sqlite3
        
        conn = sqlite3.connect(self.pipeline_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                name TEXT,
                company TEXT,
                title TEXT,
                status TEXT DEFAULT 'new',
                source TEXT,
                apollo_id TEXT,
                email_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP,
                notes TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pipeline_stages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER,
                stage TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lead_id) REFERENCES leads(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def process_new_email(self, email_id: int):
        """
        Process new email and create sales lead if applicable
        
        Args:
            email_id: Email ID from storage
        """
        email = self.storage.get_email(email_id)
        
        if not email:
            return None
        
        # Check if email is from potential lead (not from us)
        from_address = email.get("from_address", "")
        if "ballcode.co" in from_address.lower():
            return None  # Skip internal emails
        
        # Enrich with Apollo
        lead_data = self.apollo.create_lead_from_email(email)
        
        if not lead_data:
            # Create basic lead from email
            email_addr = from_address.split("<")[-1].split(">")[0].strip()
            lead_data = {
                "name": from_address.split("<")[0].strip() or "Unknown",
                "email": email_addr,
                "company": "",
                "title": "",
                "status": "new",
                "source": "email",
                "email_id": email_id,
                "email_subject": email.get("subject", ""),
                "email_body": email.get("body", "")[:500]
            }
        
        # Save lead
        lead_id = self._save_lead(lead_data)
        
        # Notify Slack
        self.slack.notify_sales_lead(lead_data)
        
        # Add to pipeline stage
        self._add_to_pipeline(lead_id, "new")
        
        return lead_id
    
    def _save_lead(self, lead_data: Dict) -> int:
        """Save lead to database"""
        import sqlite3
        
        conn = sqlite3.connect(self.pipeline_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO leads 
            (email, name, company, title, status, source, apollo_id, email_id, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lead_data.get("email", ""),
            lead_data.get("name", ""),
            lead_data.get("company", ""),
            lead_data.get("title", ""),
            lead_data.get("status", "new"),
            lead_data.get("source", "email"),
            lead_data.get("apollo_id", ""),
            lead_data.get("email_id"),
            json.dumps(lead_data)
        ))
        
        lead_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return lead_id
    
    def _add_to_pipeline(self, lead_id: int, stage: str):
        """Add lead to pipeline stage"""
        import sqlite3
        
        conn = sqlite3.connect(self.pipeline_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO pipeline_stages (lead_id, stage)
            VALUES (?, ?)
        """, (lead_id, stage))
        
        conn.commit()
        conn.close()
    
    def get_leads(self, status: Optional[str] = None) -> List[Dict]:
        """Get leads from pipeline"""
        import sqlite3
        
        conn = sqlite3.connect(self.pipeline_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if status:
            cursor.execute("SELECT * FROM leads WHERE status = ? ORDER BY created_at DESC", (status,))
        else:
            cursor.execute("SELECT * FROM leads ORDER BY created_at DESC")
        
        rows = cursor.fetchall()
        leads = [dict(row) for row in rows]
        conn.close()
        
        return leads
    
    def update_lead_status(self, lead_id: int, new_status: str):
        """Update lead status in pipeline"""
        import sqlite3
        
        conn = sqlite3.connect(self.pipeline_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE leads 
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_status, lead_id))
        
        self._add_to_pipeline(lead_id, new_status)
        
        conn.commit()
        conn.close()

