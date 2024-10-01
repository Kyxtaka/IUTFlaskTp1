from .app import db
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms . validators import DataRequired

class Author (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(100))

    def __repr__ (self ):
        return "<Author (%d) %s>" % (self.id , self.name)
    
    
def get_author(id):
    return  Author.query.get_or_404(id)  

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    url = db.Column(db.String(500))
    image = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author",
        backref = db.backref("books", lazy="dynamic"))
    
    def __repr__ (self ):
            return "<Book (%d) %s>" % (self.id , self.title)

def get_sample():
    return Book.query.limit(10).all()