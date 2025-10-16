from prophet import Prophet
import pandas as pd

class ProphetTrainer:
    def __init__(self):
        self.model = Prophet()

    def prepare_data(self, historical_data):
        df = pd.DataFrame(historical_data)
        df.rename(columns={'date': 'ds', 'close': 'y'}, inplace=True)
        return df

    def train_model(self, historical_data):
        df = self.prepare_data(historical_data)
        self.model.fit(df)

    def make_forecast(self, periods):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]