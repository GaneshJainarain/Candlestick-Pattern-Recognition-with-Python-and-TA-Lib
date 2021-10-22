import talib
import yfinance as yf 

data = yf.download("SPY", start="2021-01-01", end="2021-10-21")

print(data)