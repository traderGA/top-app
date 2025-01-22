from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
database_url=os.getenv("DATABASE_URL")
client = MongoClient(database_url)

db = client.testdb

tickers_col = db.tickers

bars_col = db.daily_bars