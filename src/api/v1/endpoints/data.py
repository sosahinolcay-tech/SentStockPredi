from fastapi import APIRouter, HTTPException
from src.services.data_fetcher import fetch_historical_data

router = APIRouter()

@router.get("/historical")
async def get_historical_data_default(symbol: str = "AAPL", start_date: str = "2020-01-01", end_date: str = "2021-01-01"):
    """
    Default historical data endpoint used by tests.
    """
    try:
        data = fetch_historical_data(symbol, start_date, end_date)
        return {"symbol": symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/historical/{symbol}")
async def get_historical_data(symbol: str, start_date: str, end_date: str):
    try:
        data = fetch_historical_data(symbol, start_date, end_date)
        return {"symbol": symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))