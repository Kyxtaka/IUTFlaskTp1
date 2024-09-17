from .app import app
from flask import render_template
from .models import get_sample

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

@app.route("/samples")
def showsamples():
    return render_template(
        "home.html", 
        title="home.html",
    )

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)]
    return render_template(
        "detail.html",
        book=book)