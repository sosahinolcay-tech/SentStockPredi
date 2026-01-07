from fastapi import APIRouter
from pydantic import BaseModel
from src.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter()


class SentimentRequest(BaseModel):
    # Test client sends {"text": "..."}
    text: str | None = None
    # API can also accept a list of headlines
    headlines: list[str] | None = None


@router.post("")
@router.post("/")
async def get_sentiment(req: SentimentRequest):
    analyzer = SentimentAnalyzer()
    if req.text is not None:
        result = analyzer.analyze_sentiment([req.text])[0]
        return {"sentiment": result}

    headlines = req.headlines or []
    results = analyzer.analyze_sentiment(headlines)
    sentiment_results = [{"headline": h, "sentiment": s} for h, s in zip(headlines, results)]
    return {"sentiments": sentiment_results}