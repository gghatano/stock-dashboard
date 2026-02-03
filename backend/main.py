from pathlib import Path

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.services.chart import create_line_chart
from backend.services.stock import get_market_data

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI(title="Stock Dashboard")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


def prepare_card_context(currency: str = "JPY"):
    """Prepare context data for card templates."""
    data = get_market_data()

    sp500_chart = create_line_chart(
        data.sp500.prices,
        currency=currency,
        exchange_rate=data.exchange_rate,
    )
    fang_chart = create_line_chart(
        data.fang.prices,
        currency=currency,
        exchange_rate=data.exchange_rate,
    )

    return {
        "sp500": {
            "name": data.sp500.name,
            "latest": data.sp500.latest,
            "previous": data.sp500.previous,
            "change": data.sp500.change,
            "change_pct": data.sp500.change_pct,
            "chart": sp500_chart,
        },
        "fang": {
            "name": data.fang.name,
            "latest": data.fang.latest,
            "previous": data.fang.previous,
            "change": data.fang.change,
            "change_pct": data.fang.change_pct,
            "chart": fang_chart,
        },
        "exchange_rate": data.exchange_rate,
        "is_fallback": data.is_fallback,
        "currency": currency,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/indices")
async def get_indices():
    """JSON API endpoint for index data."""
    data = get_market_data()
    return {
        "sp500": {
            "name": data.sp500.name,
            "prices": data.sp500.prices,
            "latest": data.sp500.latest,
            "previous": data.sp500.previous,
        },
        "fang": {
            "name": data.fang.name,
            "prices": data.fang.prices,
            "latest": data.fang.latest,
            "previous": data.fang.previous,
        },
        "exchangeRate": data.exchange_rate,
        "isFallback": data.is_fallback,
    }


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, currency: str = Query("JPY")):
    """Main page."""
    context = prepare_card_context(currency)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Stock Dashboard",
            **context,
        },
    )


@app.get("/partial/cards", response_class=HTMLResponse)
async def partial_cards(request: Request, currency: str = Query("JPY")):
    """Partial HTML for htmx card updates."""
    context = prepare_card_context(currency)
    return templates.TemplateResponse(
        request=request,
        name="partials/cards.html",
        context=context,
    )
