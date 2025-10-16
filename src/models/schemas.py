from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class StockDataBase(BaseModel):
    symbol: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockDataCreate(StockDataBase):
    pass

class StockData(StockDataBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class HeadlineBase(BaseModel):
    title: str
    source: str
    published_at: datetime
    url: HttpUrl

class HeadlineCreate(HeadlineBase):
    symbol: str

class Headline(HeadlineBase):
    id: int
    sentiment_score: Optional[float]
    created_at: datetime

    class Config:
        orm_mode = True

class PredictionBase(BaseModel):
    symbol: str
    date: datetime
    predicted_price: float
    confidence_lower: float
    confidence_upper: float
    model_version: str

class PredictionCreate(PredictionBase):
    pass

class Prediction(PredictionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SentimentAnalysisResult(BaseModel):
    headline: str
    score: float
    label: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    sentiment: float
    label: str

class ForecastRequest(BaseModel):
    symbol: str
    periods: int

class ForecastResponse(BaseModel):
    symbol: str
    forecast: List[float]
    dates: List[str]