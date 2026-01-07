from __future__ import annotations

from typing import List


class SentimentAnalyzer:
    """
    Sentiment analyzer with an offline-friendly fallback.

    - Primary: HuggingFace `transformers` pipeline (may require network for first model download)
    - Fallback: NLTK VADER (lightweight, good default for local tests)
    """

    def __init__(self):
        self._backend = None

        # Try transformers first (best results), but this can fail offline.
        try:
            from transformers import pipeline  # type: ignore

            self._backend = ("transformers", pipeline("sentiment-analysis"))
            return
        except Exception:
            pass

        # Fallback to VADER
        try:
            import nltk  # type: ignore
            from nltk.sentiment import SentimentIntensityAnalyzer  # type: ignore

            try:
                nltk.data.find("sentiment/vader_lexicon.zip")
            except LookupError:
                # Attempt download; if offline, we'll still handle gracefully below.
                try:
                    nltk.download("vader_lexicon", quiet=True)
                except Exception:
                    pass

            self._backend = ("vader", SentimentIntensityAnalyzer())
        except Exception:
            self._backend = ("noop", None)

    def analyze_sentiment(self, headlines: List[str]) -> List[dict]:
        backend, impl = self._backend

        if backend == "transformers":
            return impl(headlines)  # type: ignore[misc]

        if backend == "vader":
            out: List[dict] = []
            for h in headlines:
                scores = impl.polarity_scores(h)  # type: ignore[union-attr]
                compound = scores.get("compound", 0.0)
                label = "POSITIVE" if compound >= 0 else "NEGATIVE"
                out.append({"label": label, "score": abs(float(compound))})
            return out

        # Last-resort deterministic fallback
        return [{"label": "NEUTRAL", "score": 0.0} for _ in headlines]


def analyze_sentiment(headlines: List[str]) -> List[dict]:
    """Convenience wrapper used by tests."""
    return SentimentAnalyzer().analyze_sentiment(headlines)

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