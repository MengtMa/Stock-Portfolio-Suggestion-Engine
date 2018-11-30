from flask import Flask, render_template, request
from app.portfolio import getCurrentValue, getCompanyName, getEachAmount, getShareAmount, getHistoryPortfolio
from app.strategySelect import getPortionList
app = Flask(__name__)

@app.route("/")
def getInput():
    return render_template('home.html')

@app.route("/result", methods=['GET', 'POST'])
def getResult():
    if request.method == 'POST':
        amount = request.form.get('amount', None)
        strategy = request.form.getlist("strategy")
        portion = getPortionList(strategy)
        print('getPortionList')
        valueList = getCurrentValue(portion)
        print("getcurrentvalue")
        nameList = getCompanyName(portion)
        amountList = getEachAmount(float(amount), portion)
        shareAmount = getShareAmount(amountList, valueList)
        print("getShareAmount")
        historyPortfolio = getHistoryPortfolio(shareAmount)
        print("getHistoryPortfolio")
        return render_template('result.html', valueList=valueList, nameList=nameList, amountList=amountList, historyPortfolio=historyPortfolio)

if __name__ == '__main__':
    app.run(debug = True)
