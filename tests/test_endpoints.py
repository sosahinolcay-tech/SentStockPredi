from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_fetch_historical_data():
    response = client.get("/api/v1/data/historical")
    assert response.status_code == 200
    assert "data" in response.json()

def test_fetch_headlines():
    response = client.get("/api/v1/headlines")
    assert response.status_code == 200
    assert "headlines" in response.json()

def test_analyze_sentiment():
    response = client.post("/api/v1/sentiment", json={"text": "The stock market is doing great!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_train_forecast():
    response = client.post("/api/v1/forecast/train", json={"data": "historical_data_placeholder"})
    assert response.status_code == 200
    assert "forecast" in response.json()

def test_get_forecast():
    response = client.get("/api/v1/forecast")
    assert response.status_code == 200
    assert "forecast" in response.json()