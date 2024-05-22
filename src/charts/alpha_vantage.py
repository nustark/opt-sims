import os
import requests


base_url = 'https://www.alphavantage.co/query?function='


def query_ticker(ticker):
    url = base_url + 'TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + \
        os.environ.get("ALPHAVANTAGE_API_KEY")
    r = requests.get(url)
    return r


def query_ticker_by_date(ticker, date):
    # hardcoded date for now
    date = '2024-01-02'
    data = query_ticker(ticker).json()
    # just assume open date for now
    return data['Time Series (Daily)'][date]['1. open']
