import os
import time
import timestamp
import pandas as pd

FETCH_URL = "https://poloniex.com/public?command=returnChartData&currencyPair=%s&start=%d&end=%d&period=300"
#PAIR_LIST = ["BTC_ETH"]
DATA_DIR = "data"
COLUMNS = ["date","high","low","open","close","volume","quoteVolume","weightedAverage"]

def get_data(pair):
    datafile = os.path.join(DATA_DIR, pair+".csv")
    timefile = os.path.join(DATA_DIR, pair)

    newfile = True
    start_time = 1420070400
    end_time = 1500940800
    url = FETCH_URL % (pair, start_time, end_time)

    start = timestamp.timeConvert(start_time)
    end = timestamp.timeConvert(end_time)

    print("Get %s from %s to %s" % (pair, start, end))

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
    time.sleep(30)



def main():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    df = pd.read_json("https://poloniex.com/public?command=return24hVolume")
    pairs = [pair for pair in df.columns if pair.startswith('USDT_BTC')]
    print(pairs)

    for pair in pairs:
        get_data(pair)
        time.sleep(2)

if __name__ == '__main__':
    main()