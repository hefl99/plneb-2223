from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

with open("Aula7/webpage/terms.json", encoding="utf-8") as file:
    db = json.load(file)

def sort(db):
    keys = list(db.keys())
    keys = [term.strip() for term in keys]
    keys = sorted(keys, key=str.casefold)
    return keys

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/terms")
def terms():
    keys = sort(db)
    return render_template("terms.html", designations=keys)

@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation = t, value= db.get(t,"None"))

@app.route("/terms/search", methods=["GET"])
def search():
    text = request.args.get("text")
    results = []
    if text:
        for designation, description in db.items():
            if re.search(text, str(designation), flags=re.I):
                results.append((designation, description))
            elif 'des' in description and isinstance(description['des'], list):
                for desc in description['des']:
                    if re.search(text, str(desc), flags=re.I):
                        results.append((designation, description))
                        
    return render_template("search.html", results=results)

@app.route("/term", methods=["POST"])
def addTerm():
    print(request.form)
    designation = request.form["new_desi"]
    description = request.form["new_desc"]
    if designation not in db:
        info_message = 'Term added correctly'
    else: 
        info_message = 'Term updated correctly'
    db[designation] = {"des":[description]}
    with open("Aula7/webpage/terms.json", "w") as new_json:
        json.dump(db, new_json, ensure_ascii = False, indent = 4)
    keys = sort(db)
    return render_template("terms.html", designations=keys, message = info_message)

@app.route("/term/<designation>", methods=["DELETE"])
def deleteTerm(designation):
    desc = db[designation]
    if designation in db:
        del db[designation]
        with open("Aula7/webpage/terms.json", "w") as new_json:
            json.dump(db, new_json, ensure_ascii = False, indent = 4)
    return {designation: {"desc": desc}}

@app.route("/table")
def table():
    return render_template("table.html", db = db)

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)