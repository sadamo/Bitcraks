import os
import time
import timestamp
import shutil
import pandas as pd

FETCH_URL = "https://poloniex.com/public?command=returnChartData&currencyPair=%s&start=%d&end=%d&period=%d"
#PAIR_LIST = ["BTC_ETH"]
DATA_DIR = "data"
COLUMNS = ["date","high","low","open","close","volume","quoteVolume","weightedAverage"]
CANDLESTICK_DICT = {
    '1': 300,
    '2': 900,
    '3': 1800,
    '4': 7200,
    '5': 14400,
    '6': 86400,
}

def get_data(pair, start_time, end_time, candle):

    datafile = os.path.join(DATA_DIR, pair+".csv")
    timefile = os.path.join(DATA_DIR, pair)

    newfile = True

    url = FETCH_URL % (pair, start_time, end_time, candle)

    df = pd.read_json(url)

    #import pdb;pdb.set_trace()

    if df["date"].iloc[-1] == 0:
        print("No data.")
        return

    end_time = df["date"].iloc[-1]
    ft = open(timefile,"w")
    ft.write("%s\n" % end_time)
    ft.close()
    outf = open(datafile, "a")
    if newfile:
        df.to_csv(outf, index=False, columns=COLUMNS)
    else:
        df.to_csv(outf, index=False, columns=COLUMNS, header=False)
    outf.close()
    print("Finish.")
    time.sleep(3)


def main():

    start_time = timestamp.dateToTimestampStart()
    end_time = timestamp.dateToTimestampEnd()
    print("Valores do Candlestick")
    print("""
    1 - 5 min
    2 - 15 min  
    3 - 30  
    4 - 2 hr
    5 - 4 hr  
    6 - 1 dia""")
    option = input("Candlestick: ")
    candle = CANDLESTICK_DICT.get(str(option))
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)

    os.mkdir(DATA_DIR)

    pair = "USDT_BTC"
    print(pair)
    get_data(pair, start_time, end_time, candle)
    time.sleep(6)

if __name__ == '__main__':
    main()