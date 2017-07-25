import time
import datetime


def timeConvert(start_time):

    utc_time = datetime.utcfromtimestamp(start_time)
#   return utc_time.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")
    return utc_time.strftime("%Y-%m-%d %H:%M:%S")

def dateToTimestampStart():

    data = raw_input("Data inicial - Ex: 01-12-2017: ")
    timestamp = time.mktime(time.strptime(data, '%d-%m-%Y'))
    return int(timestamp)


def dateToTimestampEnd():

    data =raw_input("Data final - Ex: 01-12-2017: ")
    timestamp = time.mktime(time.strptime(data, '%d-%m-%Y'))
    return int(timestamp)
