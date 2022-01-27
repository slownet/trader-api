import uvicorn
from fastapi import FastAPI

from trader_api.internal import ping
from trader_api.routers import stocks

app = FastAPI()

app.include_router(ping.router)
app.include_router(stocks.router)

if __name__ == "__main__":
    uvicorn.run(app)
