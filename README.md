
## opt-sims

### requirements
#### stack/technology
- python
- flask
- mongodb
- pydantic (validations)
- alphavantage (via requests)
- oauth2 (auth)

#### todos
- map users to transactions
- use more accurate formula to calculate option premium (assuming simplified 1% for now but it doesn't account for volatility, other market factors; black-scholes)
- sell option call/puts (query db for available options for security) 
- ~~split `database.py` into different files for each collection~~

#### functional
- users can view historical and timeline data for an underlying security
- users should be able to buy or sell a call or put option for an underlying security (ignoring stocks for now)
- users can make orders of different types: market orders, limit order, stop order
- users can view their current balance, positions and the relevant order information (ticker symbol, strike price, expiry, etc.)
- users can backtest trading strategies using historical market data

#### non-functional
- trades will be simulated and starting cash will be initiated once
- system will determine gain/loss for contract(s) as the underlying securities move in price

### concepts
#### options general
- call options: written contract that gives the holder the right to buy an underlying security at a pre-determined strike price on or before a pre-determined expiration date
- puts: written contract that gives the holder the right to sell an underlying security at a pre-determined strike price on or before a pre-determined expiration date
- typical contract consists of 100 shares
- example: MSFT is trading at $404/share as of writing:
    - an investor is bullish on this security and purchases 1 contract of a call option for MSFT with a strike price of $455 for one in the future at $1.32/contract
    - the cost upfront will be $1.32 * 100 = $132
    - if the MSFT rises above $455, say $460 before or on the expiration date, the investor can choose to exercise the option to buy the security at the pre-determined strike price of $455, then immediately proceed to resell it at the new price of $460, netting a profit of ($5 - $1.32) * 100 = $368 (significantly higher returns than purchasing the underlying directly
    - if the stock fell to $400, the option would expire worthless and the investor would be out the premium of $132

### usage
#### development
1. navigate to "venv/bin"
2. run `source activate` (on unix)
3. run `pip install` here (if necessary)
4. `cd` to directory with python script and run, eg: `python main.py`
6. run `deactivate` when done