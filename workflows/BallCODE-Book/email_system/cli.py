"""
Email CLI
Command-line interface for managing emails from Cursor
"""

import click
from typing import Optional
import sys
import os

# Handle imports - try relative first, then absolute
try:
    from .storage import EmailStorage
    from .sender import EmailSender
    from .server import EmailServer
except ImportError:
    # If relative imports fail, use absolute imports
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    from storage import EmailStorage
    from sender import EmailSender
    from server import EmailServer


@click.group()
@click.option('--db-path', default='emails.db', help='Path to email database')
@click.pass_context
def cli(ctx, db_path):
    """BallCODE Local Email System - Manage emails from Cursor"""
    ctx.ensure_object(dict)
    ctx.obj['db_path'] = db_path


@cli.command()
@click.option('--host', default='localhost', help='SMTP server host')
@click.option('--port', default=2525, help='SMTP server port')
@click.pass_context
def start(ctx, host, port):
    """Start the local SMTP server"""
    db_path = ctx.obj['db_path']
    server = EmailServer(host=host, port=port, db_path=db_path)
    
    try:
        server.run_forever()
    except KeyboardInterrupt:
        server.stop()


@cli.command()
@click.option('--to', required=True, help='Recipient email address')
@click.option('--subject', required=True, help='Email subject')
@click.option('--body', required=True, help='Email body')
@click.option('--from', 'from_address', default='noreply@ballcode.co', help='Sender email address')
@click.option('--html', help='HTML body (optional)')
@click.option('--smtp-host', default='localhost', help='SMTP server host')
@click.option('--smtp-port', default=2525, help='SMTP server port')
@click.pass_context
def send(ctx, to, subject, body, from_address, html, smtp_host, smtp_port):
    """Send an email"""
    db_path = ctx.obj['db_path']
    sender = EmailSender(smtp_host=smtp_host, smtp_port=smtp_port, db_path=db_path)
    
    success = sender.send(
        to_address=to,
        subject=subject,
        body=body,
        from_address=from_address,
        html_body=html
    )
    
    sys.exit(0 if success else 1)


@cli.command()
@click.option('--folder', default='inbox', help='Email folder')
@click.option('--unread', is_flag=True, help='Show only unread emails')
@click.option('--limit', default=50, help='Maximum number of emails')
@click.pass_context
def list(ctx, folder, unread, limit):
    """List emails"""
    db_path = ctx.obj['db_path']
    storage = EmailStorage(db_path=db_path)
    
    emails = storage.list_emails(folder=folder, unread_only=unread, limit=limit)
    
    if not emails:
        click.echo("📭 No emails found")
        return
    
    click.echo(f"\n📧 Found {len(emails)} email(s):\n")
    
    for email in emails:
        status = "📬" if not email['read'] else "📭"
        click.echo(f"{status} [{email['id']}] {email['subject']}")
        click.echo(f"   From: {email['from_address']}")
        click.echo(f"   To: {email['to_address']}")
        click.echo(f"   Date: {email['date_received']}")
        click.echo()


@cli.command()
@click.argument('email_id', type=int)
@click.pass_context
def read(ctx, email_id):
    """Read an email by ID"""
    db_path = ctx.obj['db_path']
    storage = EmailStorage(db_path=db_path)
    
    email = storage.get_email(email_id)
    
    if not email:
        click.echo(f"❌ Email {email_id} not found")
        sys.exit(1)
    
    # Mark as read
    storage.mark_read(email_id, read=True)
    
    click.echo(f"\n📧 Email #{email_id}\n")
    click.echo(f"From: {email['from_address']}")
    click.echo(f"To: {email['to_address']}")
    click.echo(f"Subject: {email['subject']}")
    click.echo(f"Date: {email['date_received']}")
    click.echo(f"\n{'='*60}\n")
    
    if email['html_body']:
        click.echo(email['html_body'])
    else:
        click.echo(email['body'])


@cli.command()
@click.argument('query')
@click.option('--folder', default='inbox', help='Email folder to search')
@click.pass_context
def search(ctx, query, folder):
    """Search emails"""
    db_path = ctx.obj['db_path']
    storage = EmailStorage(db_path=db_path)
    
    emails = storage.search_emails(query=query, folder=folder)
    
    if not emails:
        click.echo(f"📭 No emails found matching '{query}'")
        return
    
    click.echo(f"\n🔍 Found {len(emails)} email(s) matching '{query}':\n")
    
    for email in emails:
        status = "📬" if not email['read'] else "📭"
        click.echo(f"{status} [{email['id']}] {email['subject']}")
        click.echo(f"   From: {email['from_address']}")
        click.echo(f"   Date: {email['date_received']}")
        click.echo()


@cli.command()
@click.argument('email_id', type=int)
@click.pass_context
def delete(ctx, email_id):
    """Delete an email by ID"""
    db_path = ctx.obj['db_path']
    storage = EmailStorage(db_path=db_path)
    
    email = storage.get_email(email_id)
    
    if not email:
        click.echo(f"❌ Email {email_id} not found")
        sys.exit(1)
    
    storage.delete_email(email_id)
    click.echo(f"✅ Email {email_id} deleted")


@cli.command()
@click.pass_context
def stats(ctx):
    """Show email statistics"""
    db_path = ctx.obj['db_path']
    storage = EmailStorage(db_path=db_path)
    
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Total emails
    cursor.execute("SELECT COUNT(*) FROM emails")
    total = cursor.fetchone()[0]
    
    # Unread emails
    cursor.execute("SELECT COUNT(*) FROM emails WHERE read = 0")
    unread = cursor.fetchone()[0]
    
    # By folder
    cursor.execute("SELECT folder, COUNT(*) FROM emails GROUP BY folder")
    folders = cursor.fetchall()
    
    conn.close()
    
    click.echo("\n📊 Email Statistics\n")
    click.echo(f"Total emails: {total}")
    click.echo(f"Unread: {unread}")
    click.echo(f"Read: {total - unread}")
    click.echo("\nBy folder:")
    for folder, count in folders:
        click.echo(f"  {folder}: {count}")


if __name__ == '__main__':
    cli()

