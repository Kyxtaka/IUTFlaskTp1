from .app import app
from flask import render_template

@app.route("/")
def home():
    return "<h1> HELLO WORKS </h1>"

@app.route("/names")
def shownames():
    return render_template(
        "base.html", 
        title="base.html", 
        names=["Pierer", "Paul", "Corinne"]
    )