import os
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

tickers = [
    "ETN",
    "PWR",
    "POWL",
    "VRT",
    "EMR",
    "SPY",
    "DUK",
    "SO",
    "D",
    "NEE"
]

endDate = datetime.today()
startDate = endDate - timedelta(days = (10*365))

endDateString = endDate.strftime("%Y-%m-%d")
startDateString = startDate.strftime("%Y-%m-%d")

prices = yf.download(
    tickers,
    startDateString,
    endDateString,
    "1d" 
)["Close"]

returns = (prices/prices.shift(1))
logReturns = np.log(returns)

returns = returns.tail(-1)
logReturns = logReturns.tail(-1)

pricesFile = "data/tenYearPrices.csv"
returnsFile = "data/tenYearReturns.csv"
logReturnsFile = "data/tenYearLogReturns.csv"

prices.to_csv(pricesFile)
returns.to_csv(returnsFile)
logReturns.to_csv(logReturnsFile)
print(f"\nSaved file[s] in directory: {os.getcwd()}.")