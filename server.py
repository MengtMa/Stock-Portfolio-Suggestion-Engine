from flask import Flask, render_template, request
from app.portfolio import getCurrentValue, getCompanyName, getEachAmount
app = Flask(__name__)

@app.route("/")
def getInput():
    return render_template('home.html')

@app.route("/result", methods=['GET', 'POST'])
def getResult():
    if request.method == 'POST':
        amount = request.form.get('amount', None)
        strategy = request.form.getlist("strategy")
        stockList = ['ADBE', 'AAPL', 'MSFT', 'TSLA', 'NSRGY']
        portion = {'ADBE': 0.3, 'AAPL': 0.2, 'MSFT':0.2, 'TSLA': 0.1, 'NSRGY': 0.2}
        valueList = getCurrentValue(stockList)
        nameList = getCompanyName(stockList)
        amountList = getEachAmount(float(amount), portion, stockList)
        return render_template('result.html', stockList=stockList, valueList=valueList, nameList=nameList, amountList=amountList)

if __name__ == '__main__':
    app.run(debug = True)
