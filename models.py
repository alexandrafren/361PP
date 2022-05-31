from __init__ import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    author = db.Column(db.String(100), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    seasons = db.Column(db.Integer, index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    platforms = db.Column(db.String(50), index=False, unique=False)
    image = db.Column(db.Text(5000))
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

class List(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index=True, unique=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique=True)
    password_hash = db.Column(db.String(128))
    #book_reviews = db.relationship('BookReview', backref='reviewer', lazy='dynamic')
    user_lists = db.relationship('List', backref="list", lazy='dynamic')

class BookListLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), index=True)