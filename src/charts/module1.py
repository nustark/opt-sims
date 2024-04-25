import os
import requests

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=' + \
#     os.environ.get("ALPHAVANTAGE_API_KEY")
# r = requests.get(url)
# data = r.json()

# print(data)


def query_ticker(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + \
        os.environ.get("ALPHAVANTAGE_API_KEY")
    r = requests.get(url)
    data = r.json()
    return data
