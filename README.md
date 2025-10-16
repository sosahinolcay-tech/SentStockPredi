# Stock Predictor Backend

This project is a backend application for a stock predictor that utilizes FastAPI to provide a RESTful API. The application fetches historical stock data, processes news headlines, computes sentiment, and trains a forecasting model using Prophet.

## Features

- Fetch historical stock data using `yfinance`.
- Retrieve and process news headlines.
- Analyze sentiment from headlines using FinBERT or VADER.
- Train and predict stock prices using the Prophet model.
- REST API built with FastAPI for easy integration.

## Project Structure

```
stock-predictor-backend
├── src
│   ├── main.py                # Entry point for the FastAPI application
│   ├── api
│   │   └── v1
│   │       ├── __init__.py    # Marks the directory as a Python package
│   │       ├── routes.py       # Defines API routes
│   │       └── endpoints
│   │           ├── data.py     # Functions for fetching historical stock data
│   │           ├── headlines.py # Handles fetching and processing news headlines
│   │           ├── sentiment.py # Functions for analyzing sentiment
│   │           └── forecast.py  # Functions for training and predicting with Prophet
│   ├── core
│   │   ├── config.py           # Configuration settings
│   │   └── logger.py           # Logging setup
│   ├── services
│   │   ├── data_fetcher.py     # Fetches stock price data
│   │   ├── news_fetcher.py     # Fetches news articles
│   │   ├── sentiment_analyzer.py # Analyzes sentiment
│   │   └── prophet_trainer.py   # Prepares data for Prophet and trains the model
│   ├── models
│   │   ├── schemas.py          # Pydantic models for request and response
│   │   └── db_models.py        # Database models (if applicable)
│   ├── db
│   │   └── storage.py          # Database storage and retrieval
│   └── utils
│       └── helpers.py          # Utility functions
├── tests
│   ├── test_endpoints.py       # Unit tests for API endpoints
│   └── test_services.py        # Unit tests for service functions
├── notebooks
│   └── exploratory.ipynb       # Jupyter notebook for exploratory data analysis
├── requirements.txt            # Project dependencies
├── Dockerfile                  # Docker image instructions
├── .env.example                # Example environment variables
├── pyproject.toml             # Project dependencies and configurations
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-predictor-backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by copying `.env.example` to `.env` and modifying as needed.

5. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:8000`. Use tools like Postman or curl to interact with the endpoints.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.