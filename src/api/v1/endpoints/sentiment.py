
from fastapi import APIRouter
from src.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter()


@router.post("/sentiment/")
async def get_sentiment(headlines: list[str]):
    analyzer = SentimentAnalyzer()
    results = analyzer.analyze_sentiment(headlines)
    # results is a list of dicts from transformers pipeline
    sentiment_results = []
    for headline, sentiment in zip(headlines, results):
        sentiment_results.append({"headline": headline, "sentiment": sentiment})
    return {"sentiments": sentiment_results}