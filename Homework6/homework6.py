from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/elefants")
def elefant():
    return render_template("elefants.html")

@app.route("/engineering")
def engineering():
    return render_template("engineering.html")

@app.route("/mares")
def mare():
    return render_template("mares.html")

app.run(host="localhost", port=4000, debug = True)