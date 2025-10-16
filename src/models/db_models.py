from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(DateTime, index=True)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Float)

class NewsHeadline(Base):
    __tablename__ = 'news_headlines'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    published_at = Column(DateTime)
    source = Column(String)

class SentimentAnalysis(Base):
    __tablename__ = 'sentiment_analysis'

    id = Column(Integer, primary_key=True, index=True)
    headline_id = Column(Integer)
    sentiment_score = Column(Float)
    sentiment_label = Column(String)