from fastapi import HTTPException, Request
from datetime import datetime, timedelta
from collections import defaultdict
from src.core.config import settings

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        
    def is_rate_limited(self, request: Request) -> bool:
        now = datetime.utcnow()
        client_ip = request.client.host
        
        # Remove old requests
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if now - req_time < timedelta(seconds=settings.RATE_LIMIT_WINDOW)
        ]
        
        # Check if too many requests
        if len(self.requests[client_ip]) >= settings.RATE_LIMIT_REQUESTS:
            return True
            
        # Add new request
        self.requests[client_ip].append(now)
        return False

rate_limiter = RateLimiter()

async def check_rate_limit(request: Request):
    if rate_limiter.is_rate_limited(request):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )