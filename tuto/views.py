from .app import app
from flask import redirect, render_template, url_for
from .models import get_sample
from .models import *
from wtforms import PasswordField
from .models import User
from hashlib import sha256
from flask_login import login_user , current_user, AnonymousUserMixin
from flask import request
from flask_login import login_required

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class AuthorForm (FlaskForm):
    id = HiddenField ('id')
    name = StringField ('Nom', validators =[DataRequired()])
    
class BookForm(FlaskForm):
    id = HiddenField('id')
    price = StringField('Prix')
    title = StringField('Titre', validators=[DataRequired()])
    
class FavorisForm(FlaskForm):
    user = HiddenField('user')
    book = HiddenField('book')

"""
@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Hello World!",
        names=["Pierre","Paul","Corinne"])
    """
@app.route("/")
def home():
    return render_template(
        "home.html",
        title="My Books !",
        books=get_sample())
    
@app.route("/books")
def books_author():
    authors_list = db.session.query(Author).all()
    authors_list.sort(key=lambda author:author.name)
    return render_template(
        "books.html",
        title="All books by author",
        authors_list=authors_list, 
    )

@app.route("/rate", methods=['GET', 'POST'])
@login_required
def save_rate():
    book_id = request.form.get('book_id')
    username = request.form.get('username')
    rate = request.form.get('rating')
    # print(f"form value: {book_id}, {username}, {rate}")
    if book_id and username and rate:
        current_rate = None
        current_rate = Rate.query.get((book_id,username))
        if current_rate is None:
            new_rating = Rate(book_id=int(book_id), username=username, rate=int(rate))
            db.session.add(new_rating)
            db.session.commit()
        else: 
            current_rate.rate = rate
            db.session.commit()
        return redirect(url_for('detail', id=book_id))
    books = get_sample()
    book = books[int(book_id)-1]
    return redirect(url_for("detail", id=book_id))

@app.route("/add/author/")
@login_required
def add_author():
    f = AuthorForm(id = int(Author.max_author())+1)
    return render_template(
        "add-author.html",
        form=f,
        title = "Ajouter an author"
    )

@app.route("/ajout/author", methods=("POST",))
@login_required
def save_add():
    f = AuthorForm(id = int(Author.max_author())+1)
    if f.validate_on_submit():
        id = int(f.id.data)
        name = f.name.data
        db.session.add(Author(id=id, name=name))
        db.session.commit()
        return redirect(url_for('add_author'))
    return render_template ("add-author.html",
    form=f)
    

@app.route("/profil")
@login_required
def profil():
    favorites = getFavorites(current_user.username)
    fav_id = [favorite.book for favorite in favorites]
    books = get_all_books(fav_id)
    return render_template("profil.html", books=books, username=current_user.username)

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    is_fav = False
    if not isinstance(current_user, AnonymousUserMixin) : 
        #Si l'utilisateur authentifé, on récupère sa note
        current_rating = Rate.query.get((int(id), current_user.username))
        user_rate = current_rating.rate if current_rating else None
        #Si l'utilisateur est authentifé on regarde si le livre est dans ses fav
        if not Favoris.query.get((current_user.username, id)) is None:
            is_fav = True 
    else: #Sinon initialisation de user_rate a None, pour passer ce processus
        user_rate = None
    rates = Rate.get_by_book(int(id))
    rates_sum = sum([value.rate for value in rates],0)
    if len(rates) != 0:
        rate_avarage = rates_sum/len(rates)
    else:
        rate_avarage = "unrated"
    return render_template("detail.html",
                           b=book, 
                           rate_avarage=rate_avarage, 
                           rate_count=str(len(rates)), 
                           user_rate=user_rate,
                           is_fav=is_fav
                        )

@app.route("/edit/author/<int:id>")
@login_required
def edit_author(id):
    a = get_author(id)
    f = AuthorForm (id=a.id, name=a.name)
    return render_template(
        "edit-authors.html",
        author =a, form=f)
    

@app.route("/edit/book/<int:id>")
@login_required
def edit_book(id):
    b = get_book(id)
    f = BookForm(id=b.id, price=b.price, title=b.title)
    return render_template(
        "edit-books.html",
        book =b, form=f)

@app.route("/save/author/", methods=("POST",))
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('edit_author', id=a.id))
    a = get_author(int(f.id.data))
    return render_template ("edit-author.html",
    author=a, form=f)

@app.route("/save/fav/<int:id>")
@login_required
def save_fav(id):
    book = get_book(id)
    edit_fav(current_user.username, book.id)
    return redirect( url_for ("profil"))

@app.route("/save/book/", methods=("POST",))
def save_book():
    b = None
    f = BookForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        b = get_book(id)
        b.title = f.title.data
        b.price = f.price.data
        db.session.commit()
        return redirect(url_for('detail', id=b.id))
    b = get_book(int(f.id.data))
    return render_template("edit-books.html",book=b, form=f)
    
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    next = HiddenField()
    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

@app.route("/login/", methods =("GET","POST" ,))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data or url_for("home")
            return redirect(next)
    return render_template(
    "login.html",
    form=f)

from flask_login import logout_user
@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))