# The current values of the overall portfolio
import datetime as datetime
import requests

result = {}


def fetchDataFrom3rdParty(portion):
    keys = []
    for key in portion:
        keys.append(key)
    keys = ','.join(keys)
    url = 'https://api.iextrading.com/1.0/stock/market/batch?symbols=%s&types=quote,chart&range=1m' % keys
    data = requests.get(url).json()
    for key in portion:
        global result
        result[key] = data[key]


def getCurrentValue(portion):
    print(portion)
    fetchDataFrom3rdParty(portion)
    valueList = {}
    today = datetime.date.today()
    for key in portion:
        value = result[key]["quote"]["latestPrice"]
        valueList[key] = float(str(round(value, 2)))
    return valueList


def getCompanyName(portion):
    nameList = {}
    for key in portion:
        nameList[key] = result[key]['quote']['companyName']
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
    stockDict = result[stock]['chart'][-5:]
    for item in stockDict:
        weekHistory[item['date']] = item['close']
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
