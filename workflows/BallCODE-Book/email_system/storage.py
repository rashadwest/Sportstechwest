"""
Email Storage System
SQLite database for storing emails locally
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Optional
from email.utils import parsedate_to_datetime
import email
from email.header import decode_header


class EmailStorage:
    """Manages email storage in SQLite database"""
    
    def __init__(self, db_path: str = "emails.db"):
        """
        Initialize email storage
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Create database tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Emails table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id TEXT UNIQUE,
                from_address TEXT,
                to_address TEXT,
                subject TEXT,
                body TEXT,
                html_body TEXT,
                date_received TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                date_sent TIMESTAMP,
                read BOOLEAN DEFAULT 0,
                folder TEXT DEFAULT 'inbox',
                raw_email TEXT
            )
        """)
        
        # Attachments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attachments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_id INTEGER,
                filename TEXT,
                content_type TEXT,
                file_path TEXT,
                FOREIGN KEY (email_id) REFERENCES emails(id)
            )
        """)
        
        # Create indexes for faster queries
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_from ON emails(from_address)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_to ON emails(to_address)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_date ON emails(date_received)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_read ON emails(read)
        """)
        
        conn.commit()
        conn.close()
    
    def save_email(self, raw_email: bytes, folder: str = 'inbox') -> int:
        """
        Save email to database
        
        Args:
            raw_email: Raw email bytes
            folder: Folder to store email in (default: 'inbox')
            
        Returns:
            Email ID
        """
        # Parse email
        msg = email.message_from_bytes(raw_email)
        
        # Extract headers
        message_id = msg.get('Message-ID', '')
        from_address = msg.get('From', '')
        to_address = msg.get('To', '')
        subject = self._decode_header(msg.get('Subject', ''))
        
        # Extract date
        date_str = msg.get('Date', '')
        date_received = None
        if date_str:
            try:
                date_received = parsedate_to_datetime(date_str)
            except:
                date_received = datetime.now()
        else:
            date_received = datetime.now()
        
        # Extract body
        body = ''
        html_body = ''
        
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = self._get_text_content(part)
                elif content_type == 'text/html':
                    html_body = self._get_text_content(part)
        else:
            content_type = msg.get_content_type()
            if content_type == 'text/plain':
                body = self._get_text_content(msg)
            elif content_type == 'text/html':
                html_body = self._get_text_content(msg)
        
        # Save to database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR IGNORE INTO emails 
            (message_id, from_address, to_address, subject, body, html_body, 
             date_received, folder, raw_email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            message_id,
            from_address,
            to_address,
            subject,
            body,
            html_body,
            date_received,
            folder,
            raw_email.decode('utf-8', errors='ignore')
        ))
        
        email_id = cursor.lastrowid
        
        # If email already exists (by message_id), get its ID
        if email_id == 0:
            cursor.execute("SELECT id FROM emails WHERE message_id = ?", (message_id,))
            result = cursor.fetchone()
            if result:
                email_id = result[0]
        
        conn.commit()
        conn.close()
        
        return email_id
    
    def _decode_header(self, header: str) -> str:
        """Decode email header (handles encoded headers)"""
        if not header:
            return ''
        
        decoded_parts = decode_header(header)
        decoded_string = ''
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                if encoding:
                    decoded_string += part.decode(encoding)
                else:
                    decoded_string += part.decode('utf-8', errors='ignore')
            else:
                decoded_string += part
        return decoded_string
    
    def _get_text_content(self, part) -> str:
        """Extract text content from email part"""
        try:
            payload = part.get_payload(decode=True)
            if payload:
                charset = part.get_content_charset() or 'utf-8'
                return payload.decode(charset, errors='ignore')
        except:
            pass
        return ''
    
    def list_emails(self, folder: str = 'inbox', unread_only: bool = False, 
                   limit: int = 50) -> List[Dict]:
        """
        List emails from database
        
        Args:
            folder: Folder to list emails from
            unread_only: Only return unread emails
            limit: Maximum number of emails to return
            
        Returns:
            List of email dictionaries
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = "SELECT * FROM emails WHERE folder = ?"
        params = [folder]
        
        if unread_only:
            query += " AND read = 0"
        
        query += " ORDER BY date_received DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        emails = []
        for row in rows:
            emails.append({
                'id': row['id'],
                'message_id': row['message_id'],
                'from_address': row['from_address'],
                'to_address': row['to_address'],
                'subject': row['subject'],
                'body': row['body'],
                'html_body': row['html_body'],
                'date_received': row['date_received'],
                'date_sent': row['date_sent'],
                'read': bool(row['read']),
                'folder': row['folder']
            })
        
        conn.close()
        return emails
    
    def get_email(self, email_id: int) -> Optional[Dict]:
        """
        Get single email by ID
        
        Args:
            email_id: Email ID
            
        Returns:
            Email dictionary or None
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM emails WHERE id = ?", (email_id,))
        row = cursor.fetchone()
        
        if row:
            email_dict = {
                'id': row['id'],
                'message_id': row['message_id'],
                'from_address': row['from_address'],
                'to_address': row['to_address'],
                'subject': row['subject'],
                'body': row['body'],
                'html_body': row['html_body'],
                'date_received': row['date_received'],
                'date_sent': row['date_sent'],
                'read': bool(row['read']),
                'folder': row['folder'],
                'raw_email': row['raw_email']
            }
            conn.close()
            return email_dict
        
        conn.close()
        return None
    
    def mark_read(self, email_id: int, read: bool = True):
        """
        Mark email as read/unread
        
        Args:
            email_id: Email ID
            read: True to mark as read, False to mark as unread
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE emails SET read = ? WHERE id = ?", (1 if read else 0, email_id))
        conn.commit()
        conn.close()
    
    def delete_email(self, email_id: int):
        """
        Delete email from database
        
        Args:
            email_id: Email ID
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Delete attachments first
        cursor.execute("DELETE FROM attachments WHERE email_id = ?", (email_id,))
        
        # Delete email
        cursor.execute("DELETE FROM emails WHERE id = ?", (email_id,))
        
        conn.commit()
        conn.close()
    
    def search_emails(self, query: str, folder: str = 'inbox') -> List[Dict]:
        """
        Search emails by query (searches subject, body, from, to)
        
        Args:
            query: Search query
            folder: Folder to search in
            
        Returns:
            List of matching emails
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        search_term = f"%{query}%"
        cursor.execute("""
            SELECT * FROM emails 
            WHERE folder = ? 
            AND (
                subject LIKE ? OR 
                body LIKE ? OR 
                from_address LIKE ? OR 
                to_address LIKE ?
            )
            ORDER BY date_received DESC
        """, (folder, search_term, search_term, search_term, search_term))
        
        rows = cursor.fetchall()
        
        emails = []
        for row in rows:
            emails.append({
                'id': row['id'],
                'message_id': row['message_id'],
                'from_address': row['from_address'],
                'to_address': row['to_address'],
                'subject': row['subject'],
                'body': row['body'],
                'html_body': row['html_body'],
                'date_received': row['date_received'],
                'date_sent': row['date_sent'],
                'read': bool(row['read']),
                'folder': row['folder']
            })
        
        conn.close()
        return emails


