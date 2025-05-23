## opt-sims

### about

Opt-sims is a paper-trading platform built in Python and Flask that allows users to simulate the buying and selling of option contracts. This project aims to put together an application in Python/Flask as well as demonstrate a basic understanding of how options work.

### requirements

#### stack/technology

- react with vite (pwa plugin eventually)
- python
- flask
- mongodb
- pydantic (validations)
- marketdata.app (via requests for options chain)
- ~~alphavantage (via requests)~~
- oauth2 (auth)
- aws elastic beanstalk (or ec2, for cloud deployment)

#### structure

- market data layer (python - flask):
  - use marketdata.app api to search for ticker options chain data
  - refresh daily data for tracked tickers
  - cache ticket options data since only need once daily
- order and position management (python - flask):
  - schemas for orders, positions, trades
  - order validation logic
  - track positions and p&l
- database (mongodb):
  - schemas for orders, positions, trades
- ui (react with vite)

#### todos

- execute option, calculate profit, add to transaction table
  - redo optiondata model class to handle get/post flows differently (inherit from common base class)
- frontend ui
- ~~map users to transactions~~
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
  - the cost upfront will be $1.32 \* 100 = $132
  - if the MSFT rises above $455, say $460 before or on the expiration date, the investor can choose to exercise the option to buy the security at the pre-determined strike price of $455, then immediately proceed to resell it at the new price of $460, netting a profit of ($5 - $1.32) \* 100 = $368 (significantly higher returns than purchasing the underlying directly
  - if the stock fell to $400, the option would expire worthless and the investor would be out the premium of $132

### usage

#### development

##### running

1. navigate to "venv/bin"
2. run `source activate` (on unix)
3. run `pip install` here (if necessary)
4. `cd` to directory with python script and run, eg: `python main.py`
5. run `deactivate` when done

##### testing in Postman with session

1. copy value from `storage`->`cookies` in the browser
2. copy `Value`
3. manage cookies in postman and set name = `session` and value equal to `Value` from the browser

##### common bugs while running

- `test_utils.py` throws `ModuleNotFoundError: No module named 'trade_engine'`: make sure `sys.path.append...` comes before the 'trade-engine' module imports and save without formatting

### links

- https://www.investopedia.com/terms/o/option.asp
