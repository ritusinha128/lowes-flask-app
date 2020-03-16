from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/dashboard.html')
def dash():
    return render_template('dashboard.html')

@app.route('/icons.html')
def icon():
    return render_template('icons.html')

@app.route('/map.html')
def map():
    return render_template('map.html')

@app.route('/customer_data.html')
def cust():
    return render_template("customer_data.html")

@app.route('/analyse.html')
def analyze():
    return render_template("analyse.html")

app.run('localhost:8000', debug=True)
