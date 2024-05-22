import os
import requests


base_url = 'https://www.alphavantage.co/query?function='


def query_ticker(ticker):
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + \
    #     os.environ.get("ALPHAVANTAGE_API_KEY")
    url = base_url + 'TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + \
        os.environ.get("ALPHAVANTAGE_API_KEY")
    r = requests.get(url)
    return r


def query_ticker_by_date(ticker, date):
    pass
