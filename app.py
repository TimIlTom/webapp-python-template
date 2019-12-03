from flask import Flask, Response
import json

from Account import accounts
#from Account import Account


app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/jquery-3.4.1.min.js')
def js():
    return app.send_static_file('jquery-3.4.1.min.js')

@app.route("/data")
def data():
    json_string = json.dumps([account.__dict__ for account in accounts])
    return Response(json_string, mimetype='application/json')