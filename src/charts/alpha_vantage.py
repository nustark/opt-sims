import os
import requests


def query_ticker(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + \
        os.environ.get("ALPHAVANTAGE_API_KEY")
    r = requests.get(url)
    return r
