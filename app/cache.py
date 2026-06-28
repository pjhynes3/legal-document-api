from typing import Any, Optional

# Simple in-memory cache simulation
_cache_store = {}


def cache_get(key: str) -> Optional[Any]:
    """Retrieve value from cache by key"""
    return _cache_store.get(key)


def cache_set(key: str, value: Any, ttl_seconds: int = 300) -> None:
    """Store value in cache with optional TTL"""
    # In real implementation, TTL would be handled
    _cache_store[key] = value


def cache_delete(key: str) -> None:
    """Remove key from cache"""
    _cache_store.pop(key, None)


def cache_clear() -> None:
    """Clear entire cache"""
    _cache_store.clear()