import yaml, os.path
from .app import db
from flask_login import UserMixin
from sqlalchemy.sql.expression import func


import yaml, os.path
Books = yaml.safe_load(
    open(
    os.path.join(
        os.path.dirname(__file__),
        "data.yml"
        )
    )
)
 
class Author (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', back_populates='author')

    def __repr__ (self ):
        return "Autheur (%d) %s" % (self.id , self.name)
    
    @staticmethod
    def max_author():
        return db.session.query(func.max(Author.id)).scalar()
    
class Favoris(db.Model):
    user = db.Column(db.String(50), db.ForeignKey('user.username'),primary_key=True)
    book = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    book_r = db.relationship('Book', back_populates='fav')
    user_r = db.relationship('User', back_populates='fav1')

    def __init__(self, username, book_id) :
        self.user = username
        self.book = book_id

    def __repr__(self):
        return f"Fav username: {self.user} book_id: {self.book}"
    
    def get_u(self):
        return (self.user,self.book)
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    price = db.Column(db.Float)
    url  = db.Column(db.String(500))
    image = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author_od = db.Column(db.Integer, db.ForeignKey("author.id"))
    fav = db.relationship('Favoris', back_populates='book_r')
    author = db.relationship('Author', back_populates='books')
    rates = db.relationship('Rate', back_populates='book')

    def __repr__(self):
        return "Livre (%d) %s" % (self.id, self.title)
    
    
class Genre(db.Model):
    id_genre = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(500))
    
    def __repr__(self):
        return "Genre (%d) %s" % (self.id_genre, self.description)
    
class Rate(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey("user.username"), primary_key=True)
    rate = db.Column(db.Integer)
    user = db.relationship('User', back_populates='rates')
    book = db.relationship('Book', back_populates='rates')

    def __init__(self, book_id:int, username:str, rate:int):
        self.book_id = book_id
        self.username = username
        self.rate = rate

    def __repr__(self):
        return f"book_id: {str(self.book_id)} | username: {self.username} | rate: {str(self.rate)}"
    
    @staticmethod
    def get_by_book(id:int):
        res = []
        for rate in Rate.query.all():
            if rate.book_id == id:
                res.append(rate)
        return res
    
def edit_fav(username, id_book):
    current_fav = Favoris.query.get((username, id_book))
    if current_fav is None:
        favorite = Favoris(username,id_book)
        db.session.add(favorite)
        db.session.commit()
    else:
        print(f"del fav: {current_fav}")
        db.session.delete(current_fav)
        db.session.commit()

def get_sample():
    return Book.query.all()

def get_author(id):
    return Author.query.get_or_404(id)

def get_all_books(list_id):
    return Book.query.filter(Book.id.in_(list_id)).all()

def get_genre(id_genre):
    return Genre.query.get_or_404(id_genre)

def getFavorites(username):
    return Favoris.query.filter_by(user=username).all()

def get_book(id):
    return Book.query.get_or_404(id)


class User(db.Model, UserMixin):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(64))
    rates = db.relationship('Rate', back_populates='user')
    fav1 = db.relationship('Favoris', back_populates='user_r')
    
    def get_id(self):
        return self.username

from .app import login_manager
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)