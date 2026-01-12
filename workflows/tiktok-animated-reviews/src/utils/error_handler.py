"""
Error Handler - JAEDS Framework
Self-healing automation with error classification and retry logic

Based on research:
- Self-healing test automation frameworks (reinforcement learning)
- Dynamic workflow adaptation
- Risk-aware adaptive automation
"""

import time
import logging
from enum import Enum
from typing import Dict, Optional, Callable, Any
from functools import wraps

logger = logging.getLogger(__name__)


class ErrorType(Enum):
    """Error classification for autonomous decision-making."""
    TRANSIENT = "transient"  # Network, rate limits, temporary - retry
    TIMEOUT = "timeout"  # Timeout errors - retry
    VALIDATION = "validation"  # Invalid input, format errors - don't retry
    PERMANENT = "permanent"  # Permission, not found - don't retry
    QUOTA = "quota"  # API quota exceeded - retry later
    UNKNOWN = "unknown"  # Unknown error - retry once


class ErrorHandler:
    """
    Self-healing error handler with intelligent retry logic.
    
    JAEDS Principles:
    - Jobs: Simple, elegant error handling
    - Alpha Evolve: Adaptive retry strategies
    - Demis: Research-backed error classification
    - Superhero CV: Best practices from automation research
    """
    
    def __init__(self, max_retries: int = 3, base_backoff: int = 2):
        """Initialize error handler."""
        self.max_retries = max_retries
        self.base_backoff = base_backoff
        self.error_history = []
    
    def classify_error(self, error: Exception, context: Optional[Dict] = None) -> ErrorType:
        """
        Classify error type for autonomous decision-making.
        
        Based on research: Error classification enables intelligent retry strategies.
        """
        error_str = str(error).lower()
        error_type = type(error).__name__
        
        # Transient errors (network, temporary)
        transient_keywords = [
            'connection', 'network', 'timeout', 'temporary', 'unavailable',
            'rate limit', 'too many requests', '429', '503', '502'
        ]
        if any(keyword in error_str for keyword in transient_keywords):
            return ErrorType.TRANSIENT
        
        # Timeout errors
        if 'timeout' in error_str or error_type == 'TimeoutError':
            return ErrorType.TIMEOUT
        
        # Quota errors
        quota_keywords = ['quota', 'limit exceeded', 'usage limit', '402']
        if any(keyword in error_str for keyword in quota_keywords):
            return ErrorType.QUOTA
        
        # Validation errors (don't retry)
        validation_keywords = [
            'invalid', 'missing', 'not found', 'format', 'syntax',
            '404', '400', 'bad request'
        ]
        if any(keyword in error_str for keyword in validation_keywords):
            return ErrorType.VALIDATION
        
        # Permanent errors (don't retry)
        permanent_keywords = [
            'permission', 'forbidden', 'unauthorized', '403', '401',
            'not implemented', 'not supported'
        ]
        if any(keyword in error_str for keyword in permanent_keywords):
            return ErrorType.PERMANENT
        
        return ErrorType.UNKNOWN
    
    def should_retry(self, error_type: ErrorType, attempt: int) -> bool:
        """
        Determine if error should be retried.
        
        Based on research: Intelligent retry decisions reduce wasted attempts.
        """
        if attempt >= self.max_retries:
            return False
        
        # Always retry transient, timeout, and quota errors
        if error_type in [ErrorType.TRANSIENT, ErrorType.TIMEOUT, ErrorType.QUOTA]:
            return True
        
        # Never retry validation and permanent errors
        if error_type in [ErrorType.VALIDATION, ErrorType.PERMANENT]:
            return False
        
        # Retry unknown errors once
        if error_type == ErrorType.UNKNOWN:
            return attempt < 2
        
        return False
    
    def calculate_backoff(self, attempt: int, error_type: ErrorType) -> float:
        """
        Calculate exponential backoff time.
        
        Based on research: Exponential backoff prevents overwhelming services.
        """
        if error_type == ErrorType.QUOTA:
            # Longer backoff for quota errors
            return min(self.base_backoff ** (attempt + 1), 300)  # Max 5 minutes
        
        # Standard exponential backoff
        return min(self.base_backoff ** attempt, 60)  # Max 1 minute
    
    def handle_with_retry(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute function with automatic retry and error handling.
        
        Self-healing: Automatically recovers from transient errors.
        """
        last_error = None
        
        for attempt in range(1, self.max_retries + 1):
            try:
                result = func(*args, **kwargs)
                
                if attempt > 1:
                    logger.info(f"✅ Function succeeded on attempt {attempt}")
                
                return {
                    "success": True,
                    "result": result,
                    "attempts": attempt,
                    "error": None
                }
                
            except Exception as e:
                last_error = e
                error_type = self.classify_error(e)
                
                # Log error
                logger.warning(
                    f"⚠️  Attempt {attempt}/{self.max_retries} failed: {error_type.value} - {str(e)}"
                )
                
                # Decide if we should retry
                if not self.should_retry(error_type, attempt):
                    logger.error(f"❌ Error classified as {error_type.value} - not retrying")
                    break
                
                # Calculate backoff and wait
                if attempt < self.max_retries:
                    backoff = self.calculate_backoff(attempt, error_type)
                    logger.info(f"⏳ Retrying in {backoff:.1f}s...")
                    time.sleep(backoff)
        
        # All attempts failed
        return {
            "success": False,
            "result": None,
            "attempts": self.max_retries,
            "error": str(last_error),
            "error_type": self.classify_error(last_error).value if last_error else None
        }


def retry_on_error(max_retries: int = 3, base_backoff: int = 2):
    """
    Decorator for automatic retry on errors.
    
    Usage:
        @retry_on_error(max_retries=3)
        def my_function():
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            handler = ErrorHandler(max_retries=max_retries, base_backoff=base_backoff)
            result = handler.handle_with_retry(func, *args, **kwargs)
            
            if not result["success"]:
                raise Exception(result["error"])
            
            return result["result"]
        
        return wrapper
    return decorator

