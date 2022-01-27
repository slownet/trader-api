from dataclasses import dataclass
from typing import Dict, Any

from bs4 import BeautifulSoup
from requests_html import HTMLSession


@dataclass
class StockInfo:
    ticker: str
    current_price: float
    fifty_day_average: float
    recommendation_key: str

    __add_to_dict__ = ['is_tradable']

    @staticmethod
    def from_yfinance(yfin_data: Dict[str, Any]):
        """Generates StockInfo object by yfinance information."""

        stock_info = StockInfo(
            ticker=yfin_data['symbol'],
            current_price=yfin_data['regularMarketPrice'],
            fifty_day_average=yfin_data['fiftyDayAverage'],
            recommendation_key=yfin_data['recommendationKey'],
        )

        return stock_info

    @property
    def is_tradable(self) -> bool:
        """Checks whether the market is open for the ticker."""

        url = f'https://finance.yahoo.com/quote/{self.ticker}'
        session = HTMLSession()
        r = session.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        header_text = soup.find_all("div", {"id": "quote-market-notice"})[0].text

        return 'Market open.' in header_text


@dataclass
class SplitRatioRequestBody:
    ratio: float
