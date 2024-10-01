from .app import app
from flask import render_template
from .models import get_author, get_sample
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms . validators import DataRequired
from flask import url_for , redirect
from .app import db
from . models import Author

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="My Books !",
        books=get_sample()
    )

@app.route("/names")
def shownames():
    return render_template(
        "base.html", 
        title="base.html", 
        names=["Pierer", "Paul", "Corinne"])

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)]
    return render_template("detail.html",b=book)

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template(
        "edit-author.html",
        author =a, form=f)
 
@app.route("/save/author/",methods =("POST",))
def save_author():
    f = AuthorForm()
    a = get_author(int(f.id.data))
    if f.validate_on_submit():
        _id = int(f.id.data)
        a.name = get_author(_id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('edit_author', id=_id))
    return render_template("edit-author.html",author=a, form=f)