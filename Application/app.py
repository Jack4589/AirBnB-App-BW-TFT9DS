"""Example of a one file flask application that uses requests to access an API"""
from os import getenv
from datetime import datetime as dt
import requests
from flask import Flask, render_template

app = Flask(__name__)



# some routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/update")
def update():
   return redirect("/")


@app.route("/reset")
def reset():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
