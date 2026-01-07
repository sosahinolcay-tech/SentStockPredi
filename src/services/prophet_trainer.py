from __future__ import annotations

import pandas as pd
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from prophet import Prophet  # pragma: no cover


class ProphetTrainer:
    def __init__(self):
        # Import lazily so importing the API doesn't hard-crash in environments
        # where Prophet (or its compiled deps) aren't available.
        from prophet import Prophet as _Prophet  # type: ignore

        self.model = _Prophet()

    def prepare_data(self, historical_data):
        """
        Accepts either:
        - yfinance-style rows with 'Date' and 'Close'
        - internal rows with 'date' and 'close'
        """
        # yfinance sometimes yields tuple keys like ('Close', 'AAPL') when MultiIndex columns are present.
        normalized = []
        for r in historical_data:
            nr = {}
            for k, v in r.items():
                if isinstance(k, tuple) and k:
                    k0 = k[0]
                    k = k0 if isinstance(k0, str) else str(k0)
                nr[str(k)] = v
            normalized.append(nr)

        df = pd.DataFrame(normalized)
        rename_map = {}
        if "Date" in df.columns:
            rename_map["Date"] = "ds"
        if "date" in df.columns:
            rename_map["date"] = "ds"
        if "Close" in df.columns:
            rename_map["Close"] = "y"
        if "close" in df.columns:
            rename_map["close"] = "y"

        df = df.rename(columns=rename_map)
        if "ds" not in df.columns or "y" not in df.columns:
            raise ValueError("historical_data must include date and close price columns")
        df["ds"] = pd.to_datetime(df["ds"])
        df["y"] = pd.to_numeric(df["y"])
        return df[["ds", "y"]]

    def train_model(self, historical_data):
        df = self.prepare_data(historical_data)
        self.model.fit(df)

    def make_forecast(self, periods: int):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    def forecast(self, stock_symbol: str, period: int):
        """
        End-to-end helper used by the API.
        Imports fetcher lazily to avoid circular imports.
        """
        from datetime import date, timedelta
        from src.services.data_fetcher import fetch_historical_data

        end = date.today()
        start = end - timedelta(days=365)
        historical = fetch_historical_data(stock_symbol, start.isoformat(), end.isoformat())
        self.train_model(historical)
        fc = self.make_forecast(period)
        # JSON-friendly output
        return [
            {
                "ds": str(row["ds"].date()) if hasattr(row["ds"], "date") else str(row["ds"]),
                "yhat": float(row["yhat"]),
                "yhat_lower": float(row["yhat_lower"]),
                "yhat_upper": float(row["yhat_upper"]),
            }
            for _, row in fc.tail(period).iterrows()
        ]


def train_prophet_model(historical_data):
    """Convenience wrapper used by tests."""
    trainer = ProphetTrainer()
    trainer.train_model(historical_data)
    return trainer.model


def predict_with_prophet(model: Any, future: pd.DataFrame):
    """Convenience wrapper used by tests."""
    forecast = model.predict(future)
    # tests expect exactly `periods` rows; keep only the future part
    return forecast.tail(len(future) - len(model.history))