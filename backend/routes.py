from fastapi import APIRouter
from models import Ticker, DailyBar
from config import tickers_col, bars_col
from schemas import ticker_serial, list_tickers, daily_bar_serial, list_daily_bars
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.get('/ticker/{symbol}')
def get_ticker_by_symbol(symbol: str):
    ticker = ticker_serial(tickers_col.find_one({'symbol': symbol}))
    return ticker

@router.get('/tickers')
async def get_tickers():
    tickers = list_tickers(tickers_col.find())
    return tickers

@router.get('/daily_bar/{id}')
def get_daily_bar(id):
    daily_bar = daily_bar_serial(bars_col.find_one({'_id': ObjectId(id)}))
    return daily_bar

# @router.get('/bars/{symbol}')
# async def get_daily_bars(symbol):
#     daily_bars = list_daily_bars(bars_col.find({'symbol': symbol}))
#     return daily_bars

@router.get('/bars/{symbol}')
async def get_daily_bars_by_symbol(symbol: str, start: str | None = None, end: str | None = None):
    if start and end:
        start_date = datetime.fromisoformat(start).timestamp()*1000
        end_date = datetime.fromisoformat(end).timestamp()*1000
        daily_bars = list_daily_bars(bars_col.find({'$and': [{'symbol': symbol}, {'t': {'$gte': start_date}}, {'t': {'$lte': end_date}}]}))
    elif start and not end:
        start_date = datetime.fromisoformat(start).timestamp()*1000
        daily_bars = list_daily_bars(bars_col.find({'$and': [{'symbol': symbol}, {'t': {'$gte': start_date}}]}))
    elif end and not start:
        end_date = datetime.fromisoformat(end).timestamp()*1000
        daily_bars = list_daily_bars(bars_col.find({'$and': [{'symbol': symbol}, {'t': {'$lte': end_date}}]}))
    else:
        daily_bars = list_daily_bars(bars_col.find({'symbol': symbol}))
    return daily_bars