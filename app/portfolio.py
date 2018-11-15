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

def getShareAmount(stockList, amountList, valueList):
    shareAmount = {}
    for stock in stockList:
        amount = amountList[stock]
        value = valueList[stock]
        shareAmount[stock] = amount / value
    return shareAmount

def getWeekHistoryValue(stock):
    weekHistory = {}
    today = datetime.date.today()
    fiveDayAgo = today - datetime.timedelta(days=6)
    stockData = web.DataReader(stock, 'yahoo', fiveDayAgo, today)
    stockDict = dict(stockData['Close'])

    for key in stockDict:
        date = key.strftime('%Y-%m-%d')
        weekHistory[date] = stockDict[key]

    return weekHistory

def getHistoryPortfolio(stockList, shareAmount):
    historyPortfolio = {}
    for stock in stockList:
        stockWeekHistory = getWeekHistoryValue(stock)
        for key in stockWeekHistory:
            if key in historyPortfolio:
                historyPortfolio[key] += float(str(round(stockWeekHistory[key] * shareAmount[stock], 2)))
            else:
                historyPortfolio[key] = float(str(round(stockWeekHistory[key] * shareAmount[stock], 2)))

    return historyPortfolio
