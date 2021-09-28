import requests
import pandas as pd

from twelvedata import TDClient
td = TDClient(apikey="ffe545e905814682a6078d6a3850b6a2")

ts = td.time_series(
    symbol="BTC",
    interval="5min"
).as_pandas()



def get_crypto_price(symbol, interval, days):
    api_key = 'YOUR API KEY'
    api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&exchange=Binance&interval={interval}&outputsize={days}&apikey={api_key}'
    raw = requests.get(api_url).json()
    df = pd.DataFrame(raw['values']).set_index('datetime')
    df = df.iloc[::-1]
    return df

btc = get_crypto_price('BTC/USD', '1day', 450)
btc