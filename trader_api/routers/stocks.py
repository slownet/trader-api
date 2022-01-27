import yfinance as yf
from fastapi import APIRouter
from fastapi import status

from models.stocks import StockInfo, SplitRatioRequestBody

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
    stock_info = StockInfo.from_yfinance(ticker_data.info)
    return {'result': stock_info}


@router.get('/{ticker}/owners')
def read_stocks_owners(ticker: str):
    """Returns a list of gamers who own such stock."""

    # TODO: add database requests.

    return {'result': []}


@router.post('/{ticker}/split', status_code=status.HTTP_200_OK)
def split_stock_count(ticker: str, split_ratio: SplitRatioRequestBody):
    """Splits the stock for everyone who ons at least one stock."""

    split_ratio = split_ratio.ratio

    return {'result': 'success'}
