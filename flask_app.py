
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session
import requests
from datetime import date

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = b'dfgsdgvdcrevd4893r34tqyof'

@app.route('/')
def homepage():
    return render_template('index.html',current_date=str(date.today()))

@app.route('/currency')
def currency_form():
    return render_template('form.html')

@app.route('/result', methods = ['GET'])
def currency_result():
    result = requests.get("http://data.fixer.io/api/latest?access_key=88e986137779229d0ead7334b6a91252")
    jsondata = result.json()
    eur_thb = jsondata['rates']['THB']
    eur = request.args.get('amount')
    thb = round(float(eur)*float(eur_thb),2)
    return render_template('result.html',amount_eur=eur,amount_thb=thb)
