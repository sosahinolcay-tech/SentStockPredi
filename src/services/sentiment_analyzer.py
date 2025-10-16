from typing import List
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze_sentiment(self, headlines: List[str]) -> List[dict]:
        results = self.sentiment_pipeline(headlines)
        return results

def main():
    # Example usage
    analyzer = SentimentAnalyzer()
    sample_headlines = [
        "Stock prices are expected to rise.",
        "The market is facing a downturn."
    ]
    sentiments = analyzer.analyze_sentiment(sample_headlines)
    print(sentiments)

if __name__ == "__main__":
    main()