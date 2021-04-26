"""An App that recieves multiple input values and returns a single value"""
from flask import Flask, render_template, request


app = Flask(__name__)



# some routes
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user_submit")
def update():
   return redirect("/")

   
if __name__ == "__main__":
    app.run(debug=True)
