"""
Garvis API Cache Module
In-memory caching for API responses to reduce calls

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import time
from typing import Dict, Optional, Any

class APICache:
    """In-memory API response cache with TTL"""
    
    def __init__(self, default_ttl: int = 60):
        self.cache: Dict[str, tuple] = {}  # key -> (value, timestamp)
        self.default_ttl = default_ttl
    
    def get(self, key: str, ttl: Optional[int] = None) -> Optional[Any]:
        """Get cached value if not expired"""
        if key not in self.cache:
            return None
        
        value, timestamp = self.cache[key]
        cache_ttl = ttl or self.default_ttl
        
        if time.time() - timestamp < cache_ttl:
            return value
        else:
            # Expired, remove from cache
            del self.cache[key]
            return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Cache value with timestamp"""
        self.cache[key] = (value, time.time())
    
    def clear(self, key: Optional[str] = None):
        """Clear cache entry or all cache"""
        if key:
            if key in self.cache:
                del self.cache[key]
        else:
            self.cache.clear()
    
    def is_cached(self, key: str, ttl: Optional[int] = None) -> bool:
        """Check if key is cached and not expired"""
        return self.get(key, ttl) is not None
    
    def get_stats(self) -> Dict:
        """Get cache statistics"""
        return {
            "size": len(self.cache),
            "keys": list(self.cache.keys())
        }


