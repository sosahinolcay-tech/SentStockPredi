from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.prophet_trainer import ProphetTrainer

router = APIRouter()

class ForecastRequest(BaseModel):
    stock_symbol: str
    period: int  # Number of days to forecast

class ForecastResponse(BaseModel):
    stock_symbol: str
    forecast: list

@router.post("/forecast", response_model=ForecastResponse)
async def forecast(request: ForecastRequest):
    try:
        trainer = ProphetTrainer()
        forecast_data = trainer.forecast(request.stock_symbol, request.period)
        return ForecastResponse(stock_symbol=request.stock_symbol, forecast=forecast_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))