"""An App that recieves multiple input values and returns a single value"""
from flask import Flask, render_template, request
from simple_model import model_lr

app = Flask(__name__)



# some routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user_submit")
def model():
    prediction = model_lr()
    return "It should be around {}".format(prediction)

   
if __name__ == "__main__":
    app.run(debug=True)
