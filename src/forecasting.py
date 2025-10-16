# src/forecasting.py
import pandas as pd
import joblib
from prophet import Prophet
from typing import Optional
import os

MODEL_STORE = os.path.join(os.path.dirname(__file__), "..", "models")

def prepare_prophet_df(price_df: pd.DataFrame, sentiment_series: Optional[pd.Series]=None) -> pd.DataFrame:
    """
    price_df expected to have 'date' and 'Close' columns
    returns df with columns ds, y, and optionally sentiment regressor column
    """
    df = price_df.copy()
    df = df[['date', 'Close']].rename(columns={'date': 'ds', 'Close': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.sort_values('ds')
    if sentiment_series is not None:
        # align by index length; simplest: expand sentiment_series to length of df using forward fill / average
        if isinstance(sentiment_series, pd.Series) and len(sentiment_series) == len(df):
            df['sentiment'] = sentiment_series.values
        else:
            # fallback: constant average
            avg = float(sentiment_series.mean()) if hasattr(sentiment_series, "mean") else float(sentiment_series)
            df['sentiment'] = avg
    return df

def train_prophet(df_prophet: pd.DataFrame, add_regressor: bool = True) -> Prophet:
    model = Prophet()
    if add_regressor and 'sentiment' in df_prophet.columns:
        model.add_regressor('sentiment')
    model.fit(df_prophet)
    return model

def predict_prophet(model: Prophet, periods: int = 30, freq: str = 'D', last_sentiment: Optional[float] = None):
    future = model.make_future_dataframe(periods=periods, freq=freq)
    if 'sentiment' in model.train_component_cols:
        # supply sentiment regressor for future: use last_sentiment or 0
        last_val = last_sentiment if last_sentiment is not None else 0.0
        future['sentiment'] = last_val
    forecast = model.predict(future)
    return forecast

def save_model(model: Prophet, name: str):
    os.makedirs(MODEL_STORE, exist_ok=True)
    path = os.path.join(MODEL_STORE, f"{name}.joblib")
    joblib.dump(model, path)
    return path

def load_model(name: str):
    path = os.path.join(MODEL_STORE, f"{name}.joblib")
    if not os.path.exists(path):
        return None
    return joblib.load(path)