from fastapi import APIRouter
from src.services.news_fetcher import fetch_news_headlines
import os

router = APIRouter()


@router.get("")
@router.get("/")
async def get_headlines(stock_symbol: str = "AAPL", page_size: int = 10):
    api_key = os.getenv("NEWS_API_KEY", "")
    headlines = fetch_news_headlines(stock_symbol, api_key=api_key, page_size=page_size)
    return {"headlines": headlines}