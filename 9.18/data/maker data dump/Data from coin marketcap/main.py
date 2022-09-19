import time
import requests
import json
import csv
from datetime import datetime
import pytz
import pandas as pd
import matplotlib.pyplot as plt
from random import seed, randint

DICT_COIN_ID = {'BTC': 1, 'ETH': 1027, 'USDT': 825, 'USDC': 3408, 'BNB': 1939, 'BUSD': 4687, 'XRP': 52, 'ADA': 2010,
                'SOL': 5426, 'DOT': 6636}

start_time_history = int(datetime(2013, 4, 28, 0, 0, tzinfo=pytz.utc).timestamp())  # 1367107200
end_time_history = int(time.time())  # now
duration_segment = 7776000  # 3 month

print(f"time_history_start in UTC: {time.asctime(time.gmtime(start_time_history))} ({start_time_history})")
print(f"time_history_end in UTC: {time.asctime(time.gmtime(end_time_history))} ({end_time_history})")

seed(1)
for coin in DICT_COIN_ID.keys():
    id_coin = DICT_COIN_ID[coin]
    quoteList = []
    for head_segment in range(start_time_history, end_time_history, duration_segment):
        head_segment -= randint(1, 10000)
        tail_segment = min(end_time_history, head_segment + duration_segment - 86400) + randint(1, 10000)
        request_link = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={id_coin}&convertId=2781&timeStart={head_segment}&timeEnd={tail_segment}"
        "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?id=825&range=1662566400~1663171199"
        print(request_link)
        response = requests.get(url=request_link)
        content = json.loads(response.content)
        quoteList = quoteList + content['data']['quotes']

    with open(f'{coin}.csv', 'w', encoding='utf8', newline='') as f:
        csv_write = csv.writer(f)
        csv_head = ["Date", "Price", "Volume"]
        csv_write.writerow(csv_head)

        for quote in quoteList:
            quote_date = quote["timeOpen"][:10]
            quote_price = "{:.2f}".format(quote["quote"]["close"])
            quote_volume = "{:.2f}".format(quote["quote"]["volume"])
            csv_write.writerow([quote_date, quote_price, quote_volume])

    series = pd.DataFrame()
    df = pd.read_csv("BTC.csv")
    series['Date'] = df['Date'].tolist()
    series['Price'] = df['Price'].tolist()
    series['Volume'] = df['Volume'].tolist()

    plt.cla()
    ax = plt.gca()
    series.plot(kind='line', x='Date', y='Price', ax=ax)
    plt.savefig(f'{coin}_price.png')

    plt.cla()
    ax = plt.gca()
    series.plot(kind='line', x='Date', y='Volume', ax=ax)
    plt.savefig(f'{coin}_volume.png')
