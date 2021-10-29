import talib
import yfinance as yf 

data = yf.download("SPY", start="2021-01-01", end="2021-10-22")

#print(data)

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning_Star'] = morning_star
data['Engulfing'] = engulfing

print(data)
print(morning_star[morning_star !=0])
engulfing_days = data[data['Engulfing'] !=0]
print(engulfing_days)