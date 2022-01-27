# Trader API

A trader bot underlying API written with FastAPI.


### Requirements

Trader API requirements are stored inside `pyproject.toml`. To create new virtual environment with all requirements installed you should use the following command:

`poetry install`

### How to run

In order to run the API server run the following command.

`uvicorn trader_api.main:app --reload`

### Docs

A swagger documentation is available under `/docs` endpoint.

### Alternative API docs

There is and alternative form for the API docs under `/redoc` endpoint.