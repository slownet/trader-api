from fastapi import FastAPI

from .internal import ping
from .routers import stocks

app = FastAPI()

app.include_router(ping.router)
app.include_router(stocks.router)
