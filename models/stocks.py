from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class StockInfo:
    current_price: float
    fifty_day_average: float
    recommendation_key: str

    @staticmethod
    def from_yfinance(yfin_data: Dict[str, Any]):
        """Generates StockInfo object by yfinance information."""

        stock_info = StockInfo(
            current_price=yfin_data['regularMarketPrice'],
            fifty_day_average=yfin_data['fiftyDayAverage'],
            recommendation_key=yfin_data['recommendationKey'],
        )

        return stock_info


@dataclass
class SplitRatioRequestBody:
    ratio: float
