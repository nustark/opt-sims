
from datetime import datetime


def calculate_option_profit(option_data, execution_price, execution_date):
    """
    Calculate the profit/loss for an option trade using a more sophisticated premium calculation.

    Args:
        option_data: OptionDataPost object containing trade details
        execution_price: Current price of the underlying asset
        execution_date: Date when calculating the profit/loss

    Returns:
        float: The calculated profit/loss amount

    TODO:
    - add more sophisticated premium calculation (black-scholes, etc.)
    - add more sophisticated risk-free rate calculation (actual risk-free rate, etc.)
    - add more sophisticated volatility calculation (actual volatility, etc.)
    - add more sophisticated price ratio calculation (actual price ratio, etc.)
    - add more sophisticated time value calculation (actual time value, etc.)
    """
    # Convert expiration_date to datetime
    expiration_date = datetime.strptime(
        option_data.expiration_date, "%Y-%m-%d")

    # Return 0 if option is expired
    if execution_date > expiration_date:
        return 0

    # Calculate time value component (theta)
    days_to_expiry = (expiration_date - execution_date).days
    # Normalize to percentage of year
    time_value = max(0, days_to_expiry / 365.0)

    # Calculate distance from strike (delta component)
    price_ratio = abs(execution_price -
                      option_data.strike_price) / option_data.strike_price

    # Base premium calculation incorporating:
    # - Time value (theta)
    # - Price distance from strike (delta)
    # - Asset price volatility factor (assumed 0.2 or 20%)
    # - Risk-free rate (assumed 0.03 or 3%)
    volatility = 0.20  # 20% volatility assumption
    risk_free_rate = 0.03  # 3% risk-free rate assumption

    premium = option_data.strike_price * option_data.quantity * (
        0.01  # Base premium
        + (time_value * 0.02)  # Time value adjustment
        + (price_ratio * 0.03)  # Delta adjustment
        + (volatility * 0.04)  # Volatility adjustment
        + (risk_free_rate * 0.01)  # Interest rate adjustment
    )

    # Determine if option is in the money
    is_call = option_data.option_type.lower() == "call"
    is_buy = option_data.action.lower() == "buy"
    in_the_money = (execution_price > option_data.strike_price) if is_call else (
        execution_price < option_data.strike_price)

    if not in_the_money:
        # Out of the money options
        return premium if not is_buy else -premium

    # Calculate intrinsic value
    price_diff = abs(execution_price - option_data.strike_price)
    intrinsic_value = price_diff * option_data.quantity

    # Calculate final profit based on action
    if is_buy:
        return intrinsic_value - premium
    else:
        return premium - intrinsic_value
