from fastapi import Request, Response
from fastapi.responses import JSONResponse
from diskcache import Cache
import hashlib
import json
from src.core.config import settings
import os

cache = Cache(directory=settings.CACHE_DIR)

def get_cache_key(request: Request) -> str:
    """Generate a cache key from the request"""
    # Include path and query parameters in the key
    key_parts = [
        request.url.path,
        str(sorted(request.query_params.items())),
    ]
    key_string = "|".join(key_parts)
    return hashlib.md5(key_string.encode()).hexdigest()

async def cache_middleware(request: Request, call_next):
    """Middleware to cache responses"""
    # Don't cache non-GET requests
    if request.method != "GET":
        return await call_next(request)

    cache_key = get_cache_key(request)
    
    # Try to get from cache
    cached_response = cache.get(cache_key)
    if cached_response is not None:
        return JSONResponse(content=cached_response)
    
    # Get fresh response
    response = await call_next(request)
    
    # Cache the response if it's successful
    if response.status_code == 200:
        try:
            response_body = [chunk async for chunk in response.body_iterator]
            response.body = b"".join(response_body)
            
            # Parse and cache the response content
            content = json.loads(response.body)
            cache.set(cache_key, content, expire=settings.CACHE_TTL)
            
            return Response(
                content=response.body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )
        except Exception:
            # If caching fails, return original response
            return response
    
    return response