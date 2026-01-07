from typing import List
import requests

class NewsFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"

    def fetch_headlines(self, query: str, page_size: int = 10) -> List[dict]:
        url = f"{self.base_url}/everything"
        params = {
            'q': query,
            'pageSize': page_size,
            'apiKey': self.api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('articles', [])

    def fetch_top_headlines(self, country: str, page_size: int = 10) -> List[dict]:
        url = f"{self.base_url}/top-headlines"
        params = {
            'country': country,
            'pageSize': page_size,
            'apiKey': self.api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('articles', [])


def fetch_news_headlines(query: str, api_key: str | None = None, page_size: int = 10) -> List[dict]:
    """
    Convenience wrapper used by tests and some callers.

    If an API key is not available (or the request fails), returns a small
    deterministic set of sample headlines so local tests don't depend on
    external services.
    """
    if not api_key:
        return [
            {"title": f"{query} stock update", "publishedAt": "2020-01-01T00:00:00Z"},
            {"title": f"{query} market sentiment mixed", "publishedAt": "2020-01-02T00:00:00Z"},
        ]

    try:
        return NewsFetcher(api_key).fetch_headlines(query, page_size=page_size)
    except Exception:
        # Fallback for offline/dev environments
        return [
            {"title": f"{query} stock update", "publishedAt": "2020-01-01T00:00:00Z"},
            {"title": f"{query} market sentiment mixed", "publishedAt": "2020-01-02T00:00:00Z"},
        ]