import yfinance as yf
import pandas as pd

data = yf.download('EURUSD=X', start='2022-10-4', end='2022-12-2', interval='15m')
data.iloc[-1:,:]
data.Open.iloc