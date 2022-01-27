import yfinance as yf
from fastapi import APIRouter

router = APIRouter(
    prefix='/stocks',
)


@router.get('/{ticker}')
def read_stocks_ticker(ticker: str):
    return {'result': f'Your ticker sir: {ticker}'}


@router.get('/{ticker}/info')
def read_stocks_ticker(ticker: str):
    """Returns a stock information."""
    ticker_data = yf.Ticker(ticker)
    return {'result': ticker_data.info}


@router.get('/{ticker}/owners')
def read_stocks_owners(ticker: str):
    """Returns a list of gamers who own such stock."""

    # TODO: add database requests.

    return {'result': []}
