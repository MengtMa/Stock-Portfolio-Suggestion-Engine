# The current values of the overall portfolio
import pandas as pd
import datetime as datetime
import pandas_datareader.data as web
import requests

def getCurrentValue(stockList):
    valueList = {}
    today = datetime.date.today()
    for stock in stockList:
        stockData = web.DataReader(stock, 'yahoo', today, today)
        value = stockData['Adj Close'][0]
        valueList[stock] = float(str(round(value, 2)))
    return valueList

def getCompanyName(stockList):
    nameList = {}
    for symbol in stockList:
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
        result = requests.get(url).json()
        for x in result['ResultSet']['Result']:
            if x['symbol'] == symbol:
                nameList[symbol] = x['name']
    return nameList

def getEachAmount(amount, portion, stockList):
    amountList = {}
    for stock in stockList:
        p = portion[stock]
        amountList[stock] = amount * p    
    return amountList
