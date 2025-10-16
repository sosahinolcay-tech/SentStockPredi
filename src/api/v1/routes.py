from fastapi import APIRouter
from .endpoints import data, headlines, sentiment, forecast


api_router = APIRouter()
api_router.include_router(data.router, prefix="/data", tags=["data"])
api_router.include_router(headlines.router, prefix="/headlines", tags=["headlines"])
api_router.include_router(sentiment.router, prefix="/sentiment", tags=["sentiment"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecast"])