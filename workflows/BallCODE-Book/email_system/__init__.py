"""
BallCODE Local Email System
Free, local email system integrated with Cursor and n8n
"""

__version__ = "1.0.0"

try:
    from .server import EmailServer
    from .storage import EmailStorage
    from .sender import EmailSender
    __all__ = ['EmailServer', 'EmailStorage', 'EmailSender']
except ImportError:
    # If relative imports fail, try absolute
    from server import EmailServer
    from storage import EmailStorage
    from sender import EmailSender
    __all__ = ['EmailServer', 'EmailStorage', 'EmailSender']

