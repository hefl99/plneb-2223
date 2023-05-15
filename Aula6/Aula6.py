from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"

@app.route("/home")
def home():
    return render_template("home.html", title="Welcome!!!")

app.run(host="localhost", port=4001, debug = True)