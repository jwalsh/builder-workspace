#!/usr/bin/env python3
"""
Redis connection wrapper for queue system
Created: 2025-01-10
Purpose: Provide a simplified Redis interface with fallback to in-memory storage
"""

import json
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
from collections import defaultdict

logger = logging.getLogger(__name__)


class RedisWrapper:
    """
    Redis wrapper with fallback to in-memory storage for development.
    This allows the queue system to work without Redis during initial testing.
    """
    
    def __init__(self, redis_url: str = "redis://localhost:6379", use_redis: bool = True):
        self.redis_url = redis_url
        self.use_redis = use_redis
        self.redis = None
        self.connected = False
        
        # In-memory fallback storage
        self.memory_store: Dict[str, Any] = {}
        self.sorted_sets: Dict[str, List[tuple]] = defaultdict(list)
        self.hashes: Dict[str, Dict[str, str]] = defaultdict(dict)
        
    async def connect(self) -> bool:
        """Attempt to connect to Redis, fall back to memory if unavailable"""
        if not self.use_redis:
            logger.info("Using in-memory storage (Redis disabled)")
            self.connected = True
            return True
            
        try:
            import aioredis
            self.redis = await aioredis.from_url(self.redis_url)
            await self.redis.ping()
            self.connected = True
            logger.info(f"Connected to Redis at {self.redis_url}")
            return True
        except ImportError:
            logger.warning("aioredis not installed, using in-memory storage")
            self.use_redis = False
            self.connected = True
            return True
        except Exception as e:
            logger.warning(f"Redis connection failed: {e}, using in-memory storage")
            self.use_redis = False
            self.connected = True
            return True
            
    async def disconnect(self):
        """Disconnect from Redis if connected"""
        if self.redis:
            await self.redis.close()
            self.redis = None
        self.connected = False
        
    async def zadd(self, key: str, mapping: Dict[str, float]) -> int:
        """Add members to sorted set"""
        if self.redis:
            return await self.redis.zadd(key, mapping)
        else:
            # In-memory implementation
            for member, score in mapping.items():
                self.sorted_sets[key].append((score, member))
            self.sorted_sets[key].sort(key=lambda x: x[0])
            return len(mapping)
            
    async def zpopmin(self, key: str, count: int = 1) -> List[tuple]:
        """Remove and return members with lowest scores"""
        if self.redis:
            return await self.redis.zpopmin(key, count)
        else:
            # In-memory implementation
            if key not in self.sorted_sets or not self.sorted_sets[key]:
                return []
            result = []
            for _ in range(min(count, len(self.sorted_sets[key]))):
                score, member = self.sorted_sets[key].pop(0)
                result.append((member, score))
            return result
            
    async def zcard(self, key: str) -> int:
        """Get number of members in sorted set"""
        if self.redis:
            return await self.redis.zcard(key)
        else:
            return len(self.sorted_sets.get(key, []))
            
    async def hset(self, key: str, field: str = None, value: str = None, mapping: Dict = None) -> int:
        """Set hash field values"""
        if self.redis:
            if mapping:
                return await self.redis.hset(key, mapping=mapping)
            else:
                return await self.redis.hset(key, field, value)
        else:
            # In-memory implementation
            if mapping:
                self.hashes[key].update(mapping)
                return len(mapping)
            else:
                self.hashes[key][field] = value
                return 1
                
    async def hget(self, key: str, field: str) -> Optional[str]:
        """Get hash field value"""
        if self.redis:
            result = await self.redis.hget(key, field)
            return result.decode() if result else None
        else:
            return self.hashes.get(key, {}).get(field)
            
    async def keys(self, pattern: str) -> List[str]:
        """Get keys matching pattern"""
        if self.redis:
            keys = await self.redis.keys(pattern)
            return [k.decode() for k in keys]
        else:
            # Simple pattern matching for in-memory
            import fnmatch
            all_keys = set()
            all_keys.update(self.memory_store.keys())
            all_keys.update(self.sorted_sets.keys())
            all_keys.update(self.hashes.keys())
            return [k for k in all_keys if fnmatch.fnmatch(k, pattern)]
            
    async def delete(self, *keys: str) -> int:
        """Delete keys"""
        if self.redis:
            return await self.redis.delete(*keys)
        else:
            count = 0
            for key in keys:
                if key in self.memory_store:
                    del self.memory_store[key]
                    count += 1
                if key in self.sorted_sets:
                    del self.sorted_sets[key]
                    count += 1
                if key in self.hashes:
                    del self.hashes[key]
                    count += 1
            return count
            
    def get_stats(self) -> Dict[str, Any]:
        """Get storage statistics"""
        if self.redis:
            return {"type": "redis", "connected": self.connected, "url": self.redis_url}
        else:
            return {
                "type": "memory",
                "connected": True,
                "keys": len(self.memory_store) + len(self.sorted_sets) + len(self.hashes),
                "sorted_sets": len(self.sorted_sets),
                "hashes": len(self.hashes)
            }