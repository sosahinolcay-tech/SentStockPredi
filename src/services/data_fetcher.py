from typing import List
import yfinance as yf

def fetch_historical_data(ticker: str, start: str, end: str) -> List[dict]:
    """
    Fetch historical stock data for a given ticker symbol between start and end dates.

    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple).
    :param start: Start date in 'YYYY-MM-DD' format.
    :param end: End date in 'YYYY-MM-DD' format.
    :return: List of historical stock data as dictionaries.
    """
    data = yf.download(ticker, start=start, end=end)
    historical_data = data.reset_index().to_dict(orient='records')
    return historical_data

def fetch_current_price(ticker: str) -> float:
    """
    Fetch the current stock price for a given ticker symbol.

    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple).
    :return: Current stock price.
    """
    stock = yf.Ticker(ticker)
    return stock.history(period='1d')['Close'].iloc[0]