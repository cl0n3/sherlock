#!/usr/bin/python

from flask import Flask


app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/accounts")l
def accounts():
    accounts = facade.get_accounts();

app.run(host='0.0.0.0', port=5000)
