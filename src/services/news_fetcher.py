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