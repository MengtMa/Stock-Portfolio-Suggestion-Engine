# The current values of the overall portfolio
import pandas as pd
import datetime as datetime
import pandas_datareader.data as web
import requests

def getCurrentValue(portion):
    valueList = {}
    today = datetime.date.today()
    for key in portion:
        stockData = web.DataReader(key, 'yahoo', today, today)
        value = stockData['Adj Close'][0]
        valueList[key] = float(str(round(value, 2)))
    return valueList

def getCompanyName(portion):
    nameList = {}
    for key in portion:
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(key)
        result = requests.get(url).json()
        for x in result['ResultSet']['Result']:
            if x['symbol'] == key:
                nameList[key] = x['name']
    return nameList

def getEachAmount(amount, portion):
    amountList = {}
    for key, val in portion.items():
        amountList[key] = amount * val
    return amountList

def getShareAmount(amountList, valueList):
    shareAmount = {}
    for key,val in amountList.items():
        value = valueList[key]
        shareAmount[key] = val / value
    return shareAmount

def getWeekHistoryValue(stock):
    weekHistory = {}
    today = datetime.date.today()
    fiveDayAgo = today - datetime.timedelta(days=8)
    stockData = web.DataReader(stock, 'yahoo', fiveDayAgo, today)
    stockDict = dict(stockData['Close'])

    for key in stockDict:
        date = key.strftime('%Y-%m-%d')
        weekHistory[date] = stockDict[key]

    return weekHistory

def getHistoryPortfolio(shareAmount):
    historyPortfolio = {}
    stockList = shareAmount.keys()
    for stock in stockList:
        stockWeekHistory = getWeekHistoryValue(stock)
        for key in stockWeekHistory:
            if key in historyPortfolio:
                historyPortfolio[key] += float(str(round(stockWeekHistory[key] * shareAmount[stock], 2)))
            else:
                historyPortfolio[key] = float(str(round(stockWeekHistory[key] * shareAmount[stock], 2)))

    return historyPortfolio
