from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.routes import api_router
from src.core.cache import cache_middleware
from src.core.rate_limit import check_rate_limit
from src.db.storage import engine
from src.models import db_models

# Create database tables
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stock Predictor API",
    version="1.0",
    description="A sentiment-based stock prediction API"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add caching middleware
@app.middleware("http")
async def cache_responses(request: Request, call_next):
    return await cache_middleware(request, call_next)

# Add rate limiting
@app.middleware("http")
async def rate_limit_requests(request: Request, call_next):
    await check_rate_limit(request)
    return await call_next(request)

# Include routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Stock Predictor API",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }