from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def getInput():
    return render_template('home.html')

@app.route("/result", methods=['GET', 'POST'])
def getResult():
    if request.method == 'POST':
        amount = request.form.get('amount', None)
        strategy = request.form.getlist("strategy")
        return render_template('result.html', amount=amount, strategy=strategy)

if __name__ == '__main__':
    app.run(debug = True)
