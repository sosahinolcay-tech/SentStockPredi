from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "sqlite:///./stock_predictor.db"
    
    # API Keys
    NEWS_API_KEY: Optional[str] = None
    
    # Service configurations
    STOCK_DATA_SOURCE: str = "yfinance"
    NEWS_API_URL: str = "https://newsapi.org/v2"
    SENTIMENT_MODEL: str = "finbert"
    
    # Cache settings
    CACHE_TTL: int = 3600  # 1 hour
    CACHE_DIR: str = ".cache"
    
    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600  # 1 hour
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()