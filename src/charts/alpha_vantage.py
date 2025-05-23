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
    # date = '2024-02-02'
    date_str = date.strftime("%Y-%m-%d")
    data = query_ticker(ticker).json()
    # just assume open date for now
    return data['Time Series (Daily)'][date_str]['1. open']
