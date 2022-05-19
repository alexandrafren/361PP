import os
from flask import Flask, render_template, request
from helpers.movies import movies, descriptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests as requests
import json

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
    image = db.Column(db.Text(5000))
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

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

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
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), index=True)



# on start up - testing microservice integration!

current_user = Reviewer.query.get(1)
current_lists = items = List.query.filter(List.reviewer_id == current_user.id).all()

product_dict = {"product": "feed newsflesh paperback"}
product_json = json.dumps(product_dict, indent=4)
details = requests.get("http://127.0.0.1:5000/", json=product_json)
b1 = Book.query.filter(Book.title=="Feed").first()
b1.image = details.json()['product_image']
db.session.commit()
print()

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
    return render_template("tv/tv.html", template_show=spec_show, template_lists = current_lists)

@app.route('/movies')
def movies():
    movies_all = Movie.query.all()
    return render_template("movie/movies.html", template_movies=movies_all)

@app.route('/movies/<int:movie_id>')
def specific_movie(movie_id):
    spec_movie = Movie.query.get(movie_id)
    return render_template("movie/movie.html", template_movie=spec_movie, template_lists = current_lists)

@app.route('/games')
def games():
    games_all = Game.query.all()
    return render_template("game/games.html", template_games=games_all)

@app.route('/games/<int:game_id>')
def specific_game(game_id):
    spec_game = Game.query.get(game_id)
    return render_template("game/game.html", template_game=spec_game, template_lists = current_lists)

@app.route('/books')
def books():
    books_all = Book.query.all()
    return render_template("book/books.html", template_books=books_all)

@app.route('/books/<int:book_id>')
def specific_book(book_id):
    spec_book = Book.query.get(book_id)
    revs = BookReview.query.filter(BookReview.book_id == book_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("book/book.html", template_book=spec_book, template_lists = current_lists, template_reviews = revs)

@app.route('/profile')
def profile():
    # pass all of users shows, movies, games and books AND lists
    rec_reviews = BookReview.query.filter(BookReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(rec_reviews):
        rec_reviews[i].book = Book.query.get(elem.book_id)
    return render_template("profile.html", template_lists = current_lists, cur_user=current_user, template_reviews=rec_reviews)

@app.route('/lists/<int:list_id>')
def specific_list(list_id):
    # pass all of users shows, movies, games and books AND lists
    spec_list = List.query.get(list_id)
    items = BookListLink.query.filter(BookListLink.list_id == list_id).all()
    for i, elem in enumerate(items):
        items[i] = Book.query.get(elem.book_id)
    return render_template("list.html", template_list = spec_list, template_items = items)

@app.route('/addbooktolist/<int:new_list_id>/<int:new_book_id>')
def add_to_list(new_list_id, new_book_id):
    db.session.add(BookListLink(list_id=new_list_id, book_id=new_book_id))
    db.session.commit()
    spec_book = Book.query.get(new_book_id)
    return render_template("book/book.html", template_book=spec_book, template_lists = current_lists)

app.run(host='0.0.0.0', port=5001)

