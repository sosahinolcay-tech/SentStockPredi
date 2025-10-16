from fastapi import APIRouter, HTTPException
from src.services.data_fetcher import fetch_historical_data

router = APIRouter()

@router.get("/historical/{symbol}")
async def get_historical_data(symbol: str, start_date: str, end_date: str):
    try:
        data = fetch_historical_data(symbol, start_date, end_date)
        return {"symbol": symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))