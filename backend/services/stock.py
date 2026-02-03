from dataclasses import dataclass
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf


@dataclass
class IndexData:
    name: str
    prices: list[dict]
    latest: float
    previous: float
    change: float
    change_pct: float


@dataclass
class MarketData:
    sp500: IndexData
    fang: IndexData
    exchange_rate: float
    is_fallback: bool


def get_dummy_prices(base_price: float, days: int = 14) -> list[dict]:
    """Generate dummy price data for fallback."""
    import random

    prices = []
    price = base_price * 0.95
    for i in range(days):
        date = datetime.now() - timedelta(days=days - i - 1)
        price = price * (1 + random.uniform(-0.02, 0.025))
        prices.append({"date": date.strftime("%Y-%m-%d"), "close": round(price, 2)})
    return prices


def get_dummy_data() -> MarketData:
    """Return dummy data when API fails."""
    sp500_prices = get_dummy_prices(5800)
    fang_prices = get_dummy_prices(12000)

    return MarketData(
        sp500=IndexData(
            name="S&P500",
            prices=sp500_prices,
            latest=sp500_prices[-1]["close"],
            previous=sp500_prices[-2]["close"],
            change=round(sp500_prices[-1]["close"] - sp500_prices[-2]["close"], 2),
            change_pct=round(
                (sp500_prices[-1]["close"] - sp500_prices[-2]["close"])
                / sp500_prices[-2]["close"]
                * 100,
                2,
            ),
        ),
        fang=IndexData(
            name="FANG+",
            prices=fang_prices,
            latest=fang_prices[-1]["close"],
            previous=fang_prices[-2]["close"],
            change=round(fang_prices[-1]["close"] - fang_prices[-2]["close"], 2),
            change_pct=round(
                (fang_prices[-1]["close"] - fang_prices[-2]["close"])
                / fang_prices[-2]["close"]
                * 100,
                2,
            ),
        ),
        exchange_rate=150.23,
        is_fallback=True,
    )


def fetch_index_data(ticker: str, name: str) -> IndexData | None:
    """Fetch index data from yfinance."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")

        if hist.empty or len(hist) < 2:
            return None

        hist = hist.tail(14)
        prices = [
            {"date": idx.strftime("%Y-%m-%d"), "close": round(row["Close"], 2)}
            for idx, row in hist.iterrows()
        ]

        latest = prices[-1]["close"]
        previous = prices[-2]["close"]

        return IndexData(
            name=name,
            prices=prices,
            latest=latest,
            previous=previous,
            change=round(latest - previous, 2),
            change_pct=round((latest - previous) / previous * 100, 2),
        )
    except Exception:
        return None


def fetch_exchange_rate() -> float | None:
    """Fetch USD/JPY exchange rate."""
    try:
        usdjpy = yf.Ticker("USDJPY=X")
        hist = usdjpy.history(period="1d")
        if hist.empty:
            return None
        return round(hist["Close"].iloc[-1], 2)
    except Exception:
        return None


def get_market_data() -> MarketData:
    """Fetch all market data, with fallback to dummy data."""
    sp500 = fetch_index_data("^GSPC", "S&P500")
    fang = fetch_index_data("^NYFANG", "FANG+")
    exchange_rate = fetch_exchange_rate()

    if sp500 is None or fang is None or exchange_rate is None:
        return get_dummy_data()

    return MarketData(
        sp500=sp500,
        fang=fang,
        exchange_rate=exchange_rate,
        is_fallback=False,
    )
