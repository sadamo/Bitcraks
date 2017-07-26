import numpy as np

dataset = [1, 5, 7, 2, 6, 7, 8, 2, 5, 2, 6, 8, 2, 6, 13]


def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a


def computeMACD(x, slow=26, fast=12):
    '''
    macd line = 12ema - 26ema
    signal line = 9ema of the macd line
    histogram = macd line - signal line
    '''
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    return emaslow, emafast, emafast - emaslow

nslow = 26
nfast = 12
nsignal = 9

# emaslow, emafast, macd = computeMACD(dataset)
# signal = ExpMovingAverage(macd, nsignal)

# histogram = macd - signal

# print movingaverage(dataset, 3)
# print ExpMovingAverage(dataset, 3)
