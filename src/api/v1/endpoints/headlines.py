
from fastapi import APIRouter
from src.services.news_fetcher import NewsFetcher
import os

router = APIRouter()


@router.get("/headlines")
async def get_headlines(stock_symbol: str, page_size: int = 10):
    api_key = os.getenv("NEWS_API_KEY", "")
    news_fetcher = NewsFetcher(api_key)
    headlines = news_fetcher.fetch_headlines(stock_symbol, page_size)
    return {"headlines": headlines}