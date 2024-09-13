import pandas as pd


def exponential_smoothing(series, alpha=0.2):
    result = [series[0]]  # First value is the same as series
    for i in range(1, len(series)):
        result.append(alpha * series[i] + (1 - alpha) * result[i-1])
    return result