import os
from flask import Flask, render_template, request
from helpers.movies import movies, descriptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models - To Be Moved to Seperate Function
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    author = db.Column(db.String(100), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    rating = db.Column(db.String(5), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    rating = db.Column(db.String(5), index=True, unique=False)
    seasons = db.Column(db.Integer, index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    rating = db.Column(db.String(5), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    platforms = db.Column(db.String(50), index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

"""
class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
"""
class List(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index=True, unique=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique=True)
    #book_reviews = db.relationship('BookReview', backref='reviewer', lazy='dynamic')
    user_lists = db.relationship('List', backref="list", lazy='dynamic')

class BookListLink(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('list.id'), primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), index=True, unique=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/tv')
def tv():
    return "TV will be here!"

@app.route('/movies')
def movies_loader():
    return render_template("movies.html", template_movies=movies)

@app.route('/games')
def games():
    return "Games will be here!"

@app.route('/books')
def books():
    books_all = Book.query.all()
    return render_template("book/books.html", template_books=books_all)

@app.route('/books/<int:book_id>')
def specific_book(book_id):
    spec_book = Book.query.get(book_id)
    return render_template("book/book.html", template_book=spec_book)

@app.route('/profile')
def profile():
    return "Profile will be here!"

app.run(host='0.0.0.0', port=5000)

