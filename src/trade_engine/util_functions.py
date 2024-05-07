
from datetime import datetime


# uses simple option premium calculation (real-world would account for more volatility; eg: black-scholes, etc.)
def calculate_option_profit(option_data, execution_price, execution_date):
    # convert expiration_date to datetime object
    expiration_date = datetime.strptime(
        option_data.expiration_date, "%Y-%m-%d")

    # check if the option is expired
    if execution_date > expiration_date:
        # expires worthless
        return 0

    # calculate the option premium, assumes 1% premium for simplicity
    premium = option_data.strike_price * \
        option_data.quantity * 0.01

    if option_data.option_type.lower() == "call":
        if option_data.action.lower() == "buy":
            # buying a call option
            if execution_price > option_data.strike_price:
                # option is in the money
                profit = (execution_price - option_data.strike_price) * \
                    option_data.quantity - premium
            else:
                # option is out of the money
                profit = -premium
        else:
            # selling a call option
            if execution_price > option_data.strike_price:
                # option is in the money
                profit = premium - \
                    (execution_price - option_data.strike_price) * \
                    option_data.quantity
            else:
                # option is out of the money
                profit = premium
    else:
        if option_data.action.lower() == "buy":
            # buying a put option
            if execution_price < option_data.strike_price:
                # option is in the money
                profit = (option_data.strike_price - execution_price) * \
                    option_data.quantity - premium
            else:
                # option is out of the money
                profit = -premium
        else:
            # selling a put option
            if execution_price < option_data.strike_price:
                # option is in the money
                profit = premium - (option_data.strike_price -
                                    execution_price) * option_data.quantity
            else:
                # option is out of the money
                profit = premium

    return profit
