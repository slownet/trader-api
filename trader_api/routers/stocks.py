from fastapi import APIRouter

router = APIRouter(
    prefix='/stocks',
)


@router.get('/{ticker}')
def read_stocks_ticker(ticker: str):
    return {'result': f'Your ticker sir: {ticker}'}
