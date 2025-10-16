# src/sentiment_analysis.py
from typing import List, Tuple
import logging

# Try FinBERT (transformers) first; fall back to VADER if not available
try:
    from transformers import pipeline
    _hf_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert", device=-1)
    USE_FINBERT = True
except Exception as e:
    USE_FINBERT = False

if not USE_FINBERT:
    import nltk
    nltk.download('vader_lexicon', quiet=True)
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    _vader = SentimentIntensityAnalyzer()

def analyze_headlines(headlines: List[str]) -> List[Tuple[str, float]]:
    """
    Returns list of (headline, sentiment_score) where score is roughly on -1..1 (negative..positive)
    Uses FinBERT if available, otherwise VADER.
    """
    results = []
    if USE_FINBERT:
        # ProsusAI/finbert outputs labels: positive/negative/neutral with scores.
        for h in headlines:
            try:
                res = _hf_pipeline(h[:512])[0]  # truncate long text
                label = res.get("label", "").lower()
                score = float(res.get("score", 0.0))
                # map to -1..1
                if label.startswith("neg"):
                    mapped = -score
                elif label.startswith("pos"):
                    mapped = score
                else:
                    mapped = 0.0
                results.append((h, mapped))
            except Exception as e:
                logging.exception("FinBERT failed on headline; falling back to 0.0")
                results.append((h, 0.0))
    else:
        for h in headlines:
            vs = _vader.polarity_scores(h)
            results.append((h, vs["compound"]))
    return results

# small helper to compute avg sentiment
def average_sentiment(scores_list):
    if not scores_list:
        return 0.0
    vals = [s for (_, s) in scores_list]
    return sum(vals) / len(vals)