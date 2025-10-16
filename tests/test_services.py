from fastapi import FastAPI
from src.services.data_fetcher import fetch_historical_data
from src.services.news_fetcher import fetch_news_headlines
from src.services.sentiment_analyzer import analyze_sentiment
from src.services.prophet_trainer import train_prophet_model, predict_with_prophet

def test_fetch_historical_data():
    # Test fetching historical stock data
    data = fetch_historical_data("AAPL", "2020-01-01", "2021-01-01")
    assert data is not None
    assert len(data) > 0

def test_fetch_news_headlines():
    # Test fetching news headlines
    headlines = fetch_news_headlines("AAPL")
    assert headlines is not None
    assert len(headlines) > 0

def test_analyze_sentiment():
    # Test sentiment analysis
    headlines = ["Apple stock is soaring!", "Apple faces challenges ahead."]
    sentiments = analyze_sentiment(headlines)
    assert sentiments is not None
    assert len(sentiments) == len(headlines)

def test_train_prophet_model():
    # Test training the Prophet model
    historical_data = fetch_historical_data("AAPL", "2020-01-01", "2021-01-01")
    model = train_prophet_model(historical_data)
    assert model is not None

def test_predict_with_prophet():
    # Test making predictions with the Prophet model
    historical_data = fetch_historical_data("AAPL", "2020-01-01", "2021-01-01")
    model = train_prophet_model(historical_data)
    future = model.make_future_dataframe(periods=30)
    forecast = predict_with_prophet(model, future)
    assert forecast is not None
    assert len(forecast) == 30