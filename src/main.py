
from module1 import Option
from datetime import datetime

option = Option(symbol='AAPL', expiration_date=datetime(
    2024, 6, 21), strike_price=150.0, option_type='call', quantity=5)
option.update_price(price=10.25, bid=10.0, ask=10.5)
option.update_greeks(delta=0.6, gamma=0.02, theta=-0.05, vega=0.3)
option.execute_order(order_type='buy')
