"""An App that recieves multiple input values and returns a single value"""
from flask import Flask, render_template, request
from simple_model import *

app = Flask(__name__)



# some routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user_submit", methods=['POST'])
def recommended_price():
    """
    Returns recommended price given user-inputed parameters.
    """
    user_input = request.values['feature_checkbox']
    prediction = model_lr(user_input)
    return "It should be around {}".format(prediction)

   
if __name__ == "__main__":
    app.run(debug=True)
