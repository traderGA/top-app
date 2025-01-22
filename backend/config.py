from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.testdb

tickers_col = db.tickers

bars_col = db.daily_bars