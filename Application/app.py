"""An App that recieves multiple input values and returns a single value"""
from flask import Flask, render_template, request
from .simple_model import *

app = Flask(__name__)



# App routess
# TODO Landing home page and app introduction
# @app.route("/")
# def home():
#     return render_template('home.html')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user_submit", methods=['POST'])
def recommended_price():
    """
    Returns recommended price given user-inputed parameters.
    """
    avail_365 = int(request.values['availability_365'])
    min_nights = int(request.values['minimum_nights'])
    user_input = [avail_365, min_nights]

    prediction = predict_price(user_input)
    return "It should be around {}".format(prediction)

   
if __name__ == "__main__":
    app.run(debug=True)
    
