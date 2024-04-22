class Option:
    def __init__(self, symbol, expiration_date, strike_price, option_type, quantity):
        self.symbol = symbol
        self.expiration_date = expiration_date
        self.strike_price = strike_price
        self.option_type = option_type  # call/put
        self.quantity = quantity  # num of option contracts

        self.price = None

        # self.bid = None
        # self.ask = None
        # self.delta = None
        # self.gamma = None
        # self.theta = None
        # self.vega = None

    def update_price(self, price, bid, ask):
        """
        Update option price, bid, and ask.
        """
        self.price = price
        self.bid = bid
        self.ask = ask

    def update_greeks(self, delta, gamma, theta, vega):
        """
        Update option Greeks.
        """
        self.delta = delta
        self.gamma = gamma
        self.theta = theta
        self.vega = vega

    def execute_order(self, order_type, price=None):
        if order_type == 'buy':
            print(
                f"Buying {self.quantity} {self.option_type} option contracts of {self.symbol}...")
            # Update user's portfolio, cash balance, etc.
        elif order_type == 'sell':
            print(
                f"Selling {self.quantity} {self.option_type} option contracts of {self.symbol}...")
            # Update user's portfolio, cash balance, etc.
        else:
            print("Invalid order type.")


# option = Option(symbol='AAPL', expiration_date=datetime(
#     2024, 6, 21), strike_price=150.0, option_type='call', quantity=5)
# option.update_price(price=10.25, bid=10.0, ask=10.5)
# option.update_greeks(delta=0.6, gamma=0.02, theta=-0.05, vega=0.3)
# option.execute_order(order_type='buy')
