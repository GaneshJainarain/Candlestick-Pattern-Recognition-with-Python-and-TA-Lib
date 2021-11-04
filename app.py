import os, csv
import talib
import yfinance as yf
import pandas as pd
from flask import Flask, render_template, request
from patterns import patterns

app = Flask(__name__)

@app.route("/")
def index():
    pattern = request.args.get('pattern', None)
    if pattern:
        #looping thrpugh all the files in this specific directory
        #the os.listdir method lists all the files in the said directory and now we can loop through them
        datafiles = os.listdir('datasets/daily')
        for filename in datafiles:
            #pandas dataframe
            df = pd.read_csv('datasets/daily/{}'.format(filename))
            #print(df)
            pattern_function = getattr(talib, pattern)
            try:
                result = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                #print(result)
                #Focusing on the last result/candlestick for newer data
                last = result.tail(1).values[0]
                print(last)
                if last !=0:
                    print("{} triggered {}".format(filename, pattern))

            except:
                pass


    return render_template('index.html', patterns=patterns)


@app.route('/snapshot')
def snapshot():
    with open('datasets/companies.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = company.split(',')[0]
            df = yf.download(symbol, start="2020-01-01", end="2020-08-01")
            df.to_csv('datasets/daily/{}.csv'.format(symbol))
    return {
        'code': 'success'
    }