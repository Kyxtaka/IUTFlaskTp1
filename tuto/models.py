# import yaml, os.path
# Books = yaml.safe_load(
#     open(
#     os.path.join(
#     os.path.dirname(__file__),
#             "data.yml"
#         )
#     )
# )

# # Pour avoir un id
# i = 0
# for book in Books:
#     book['id'] = i
#     i += 1

# def get_sample():
#     return Books[0:10]

from .app import db
from flask_sqlalchemy import SQLAlchemy

class Author (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(100))

    def __repr__ (self ):
        return "<Author (%d) %s>" % (self.id , self.name)
    

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