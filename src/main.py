
from app import app
# import os
# import pymongo
# from trade_engine.module1 import Option
# from datetime import datetime
# from pymongo import MongoClient
# from dotenv import load_dotenv, find_dotenv

# env_file = find_dotenv(".env")
# load_dotenv(env_file)

# option = Option(symbol='AAPL', expiration_date=datetime(
#     2024, 6, 21), strike_price=150.0, option_type='call', quantity=5)
# option.update_price(price=10.25, bid=10.0, ask=10.5)
# option.update_greeks(delta=0.6, gamma=0.02, theta=-0.05, vega=0.3)
# option.execute_order(order_type='buy')

# cluster = MongoClient(os.environ.get("MONGODB_ATLAS_URI"))
# db = cluster["optionz-db-dev"]
# collection = db["user"]
# collection.insert_one({
#     "_id": "99",
#     "display_name": "GM Thurman",
#     "username": "username",
#     "email": "email@example.com",
#     "password_hash": "password",
#     "cash_balance": 100000.00
# })

# collection2 = db["transaction"]
# collection2.insert_one({
#     "_id": "1",
#     "user_id": "99",
#     "symbol": "AAPL",
#     "type": "buy",
#     "quantity": 5,
#     "price": 150.0,
#     "timestamp": "2024-04-17T10:00:00Z"
# })

# collection = db["option"]
# collection.insert_one({
#     "_id": "1",
#     "symbol": "AAPL",
#     "expiration_date": "2024-06-21",
#     "strike_price": 150.0,
#     "option_type": "call",
#     "quantity": 5,
#     "price": 10.25,
#     "bid": 10.0,
#     "ask": 10.5,
#     "delta": 0.6,
#     "gamma": 0.02,
#     "theta": -0.05,
#     "vega": 0.3
# })


if __name__ == '__main__':
    app.run(debug=True)
