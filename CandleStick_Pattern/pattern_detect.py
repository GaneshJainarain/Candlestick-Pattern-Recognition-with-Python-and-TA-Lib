import talib
import yfinance as yf 

data = yf.download("SPY", start="2021-01-01", end="2021-10-22")

#print(data)

num = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

print(num[num !=0])