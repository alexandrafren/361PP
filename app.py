import os
from flask import Flask, render_template, request
from helpers.movies import movies, descriptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    seasons = db.Column(db.Integer, index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
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

class Reviewer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique=True)
    password_hash = db.Column(db.String(128))
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
    shows_all = Show.query.all()
    return render_template("tv/tvs.html", template_shows=shows_all)

@app.route('/tv/<int:tv_id>')
def specific_tv(tv_id):
    spec_show = Show.query.get(tv_id)
    return render_template("tv/tv.html", template_show=spec_show)

@app.route('/movies')
def movies():
    movies_all = Movie.query.all()
    return render_template("movie/movies.html", template_movies=movies_all)

@app.route('/movies/<int:movie_id>')
def specific_movie(movie_id):
    spec_movie = Movie.query.get(movie_id)
    return render_template("movie/movie.html", template_movie=spec_movie)

@app.route('/games')
def games():
    games_all = Game.query.all()
    return render_template("game/games.html", template_games=games_all)

@app.route('/games/<int:game_id>')
def specific_game(game_id):
    spec_game = Game.query.get(game_id)
    return render_template("game/game.html", template_game=spec_game)

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
    # pass all of users shows, movies, games and books AND lists
    user_lists = List.query.all()
    return render_template("profile.html", template_lists = user_lists)

app.run(host='0.0.0.0', port=5000)

