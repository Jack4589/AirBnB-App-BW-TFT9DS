"""Example of a one file flask application that uses requests to access an API"""
from os import getenv
from datetime import datetime as dt
import requests
from flask import Flask, redirect

app = Flask(__name__)



# some routes
@app.route("/")
def root():
    astro_data = Astros.query.all()[0]
    return 'TODO'


@app.route("/update")
def update():
   return redirect("/")


@app.route("/reset")
def reset():
    return redirect("/")

