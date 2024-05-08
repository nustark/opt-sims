
import sys
import os

# add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'src')))

from trade_engine.models import OptionData
from trade_engine.util_functions import calculate_option_profit
from pydantic import BaseModel, Field
from datetime import datetime
import unittest


class TestCalculateOptionProfit(unittest.TestCase):
    def test_call_option_buy_in_the_money(self):
        option_data = OptionData(
            symbol="GOOG",
            quantity=100,
            strike_price=120.0,
            expiration_date="2023-06-30",
            option_type="call",
            action="buy",
            user_id=1234
        )
        execution_price = 125.0
        execution_date = datetime(2023, 6, 15)
        expected_profit = (125.0 - 120.0) * 100 - 120.0 * 100 * 0.01
        self.assertAlmostEqual(calculate_option_profit(
            option_data, execution_price, execution_date), expected_profit)

    def test_call_option_sell_out_of_the_money(self):
        option_data = OptionData(
            symbol="AAPL",
            quantity=50,
            strike_price=180.0,
            expiration_date="2023-07-31",
            option_type="call",
            action="sell",
            user_id=5678
        )
        execution_price = 175.0
        execution_date = datetime(2023, 7, 15)
        expected_profit = 180.0 * 50 * 0.01
        # expected_profit = 180.0 * 50 * 1.01
        self.assertAlmostEqual(calculate_option_profit(
            option_data, execution_price, execution_date), expected_profit)

    def test_put_option_buy_out_of_the_money(self):
        option_data = OptionData(
            symbol="TSLA",
            quantity=200,
            strike_price=300.0,
            expiration_date="2023-08-31",
            option_type="put",
            action="buy",
            user_id=9012
        )
        execution_price = 310.0
        execution_date = datetime(2023, 8, 15)
        expected_profit = -300.0 * 200 * 0.01
        self.assertAlmostEqual(calculate_option_profit(
            option_data, execution_price, execution_date), expected_profit)

    def test_expired_option(self):
        option_data = OptionData(
            symbol="MSFT",
            quantity=75,
            strike_price=250.0,
            expiration_date="2023-05-31",
            option_type="call",
            action="buy",
            user_id=3456
        )
        execution_price = 260.0
        execution_date = datetime(2023, 6, 15)
        expected_profit = 0
        self.assertEqual(calculate_option_profit(
            option_data, execution_price, execution_date), expected_profit)


if __name__ == '__main__':
    unittest.main()
