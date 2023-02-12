from flask import Flask, render_template

app = Flask(__name__)

def welcome():
    return "Welcome to my Flask application!"

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")