"""
Email Analytics and Advanced Search
Analytics, metrics, and advanced search capabilities
"""

import sqlite3
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from pathlib import Path

class EmailAnalytics:
    """Email analytics and advanced search"""
    
    def __init__(self, db_path: str = "emails.db"):
        self.db_path = Path(__file__).parent / db_path
    
    def get_email_volume(self, days: int = 30) -> Dict:
        """
        Get email volume statistics
        
        Args:
            days: Number of days to analyze
            
        Returns:
            Dictionary with volume statistics
        """
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        # Total emails
        cursor.execute("SELECT COUNT(*) FROM emails WHERE date_received >= ?", (cutoff_date,))
        total = cursor.fetchone()[0]
        
        # By day
        cursor.execute("""
            SELECT DATE(date_received) as day, COUNT(*) as count
            FROM emails
            WHERE date_received >= ?
            GROUP BY DATE(date_received)
            ORDER BY day DESC
        """, (cutoff_date,))
        daily = dict(cursor.fetchall())
        
        # By folder
        cursor.execute("""
            SELECT folder, COUNT(*) as count
            FROM emails
            WHERE date_received >= ?
            GROUP BY folder
        """, (cutoff_date,))
        by_folder = dict(cursor.fetchall())
        
        conn.close()
        
        return {
            "period_days": days,
            "total_emails": total,
            "daily_volume": daily,
            "by_folder": by_folder,
            "average_per_day": total / days if days > 0 else 0
        }
    
    def get_sender_stats(self, limit: int = 10) -> List[Dict]:
        """
        Get top senders statistics
        
        Args:
            limit: Number of top senders to return
            
        Returns:
            List of sender statistics
        """
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT from_address, COUNT(*) as count
            FROM emails
            GROUP BY from_address
            ORDER BY count DESC
            LIMIT ?
        """, (limit,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                "email": row[0],
                "count": row[1]
            })
        
        conn.close()
        return results
    
    def search_advanced(self, query: str, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Advanced search with filters
        
        Args:
            query: Search query
            filters: Optional filters (from, to, date_from, date_to, folder, read)
            
        Returns:
            List of matching emails
        """
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Build query
        conditions = []
        params = []
        
        # Text search
        if query:
            search_term = f"%{query}%"
            conditions.append("""
                (subject LIKE ? OR body LIKE ? OR from_address LIKE ? OR to_address LIKE ?)
            """)
            params.extend([search_term, search_term, search_term, search_term])
        
        # Filters
        if filters:
            if filters.get('from'):
                conditions.append("from_address LIKE ?")
                params.append(f"%{filters['from']}%")
            
            if filters.get('to'):
                conditions.append("to_address LIKE ?")
                params.append(f"%{filters['to']}%")
            
            if filters.get('folder'):
                conditions.append("folder = ?")
                params.append(filters['folder'])
            
            if filters.get('read') is not None:
                conditions.append("read = ?")
                params.append(1 if filters['read'] else 0)
            
            if filters.get('date_from'):
                conditions.append("date_received >= ?")
                params.append(filters['date_from'])
            
            if filters.get('date_to'):
                conditions.append("date_received <= ?")
                params.append(filters['date_to'])
        
        # Build SQL
        sql = "SELECT * FROM emails"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += " ORDER BY date_received DESC LIMIT 100"
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        emails = []
        for row in rows:
            emails.append(dict(row))
        
        conn.close()
        return emails
    
    def get_insights(self) -> Dict:
        """
        Generate email insights
        
        Returns:
            Dictionary with insights
        """
        volume = self.get_email_volume(days=30)
        top_senders = self.get_sender_stats(limit=5)
        
        insights = {
            "email_volume": volume,
            "top_senders": top_senders,
            "insights": []
        }
        
        # Generate insights
        if volume['average_per_day'] > 10:
            insights["insights"].append("High email volume - consider automation")
        
        if len(top_senders) > 0:
            top_sender = top_senders[0]
            insights["insights"].append(f"Top sender: {top_sender['email']} ({top_sender['count']} emails)")
        
        return insights


