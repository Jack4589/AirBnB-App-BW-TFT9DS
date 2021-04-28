"""An App that recieves multiple input values and returns a single value"""
from flask import Flask, render_template, request
import pandas as pd
from simple_model import *


def create_app():
    app = Flask(__name__)




    # App routess
    # TODO Landing home page and app introduction
    # @app.route("/")
    # def home():
    #     return render_template('home.html')


    @app.route("/", methods = ["GET"])
    def index():
        if request.method == "GET":
                return render_template('home.html')


    @app.route("/user_submit", methods=['POST'])
    def recommended_price():
        """
        Returns recommended price given user-inputed parameters.
        """
        availability_365 = int(request.values['availability_365'])
        minimum_nights = int(request.values['minimum_nights'])
        user_input = [availability_365, minimum_nights]

        prediction = predict_price(user_input)

        return "It should be around ${}".format(round(prediction[0], 0))

        
    return app

if __name__ == "__main__":
    create_app()
    app.run(debug=True)