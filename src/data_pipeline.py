# src/data_pipeline.py
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_price_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """
    Returns a DataFrame with Date index and columns: Open, High, Low, Close, Adj Close, Volume
    """
    df = yf.download(ticker, period=period, interval=interval, progress=False)
    if df.empty:
        raise ValueError(f"No data returned for ticker {ticker}")
    df = df.reset_index()
    df.rename(columns={"Date": "date"}, inplace=True)
    return df

def fetch_recent_dates(days: int = 30):
    end = datetime.utcnow().date()
    start = end - timedelta(days=days)
    return start.isoformat(), end.isoformat()