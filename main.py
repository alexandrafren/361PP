import os
from flask import Flask, render_template, request, redirect, url_for, flash
from __init__ import db, create_app
from helpers.movies import movies, descriptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests as requests
import json
import string
from models import Book, Movie, Show, Game, Reviewer, BookListLink, BookReview, List

main = create_app()
global current_user
current_user = None

# on start up - testing microservice integration!
"""
shows_all = Show.query.all()
for show in shows_all:
    translator = str.maketrans('', '', string.punctuation)
    title = show.title.translate(translator)
    product_dict = {"product": show.title + " tv show"}
    product_json = json.dumps(product_dict, indent=4)
    details = requests.get("http://127.0.0.1:5000/", json=product_json)
    show.image = details.json()['product_image']
    db.session.commit()
"""

#GET METHODS
def get_current_user():
    # UPDATE THIS ONCE AUTHENTICATION IS IMPLEMENTED
    return current_user

def get_current_lists():
    current_user = get_current_user()
    if current_user is not None:
        return List.query.filter(List.reviewer_id == current_user.id).all()
    else:
        return None

def set_current_user(user):
    # UPDATE THIS ONCE AUTHENTICATION IS IMPLEMENTED
    global current_user
    current_user = user

def logged_in():
    if current_user == None:
        return False
    else:
        return True

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/tv')
def tv():
    shows_all = Show.query.all()
    return render_template("tv/tvs.html", template_shows=shows_all)

@main.route('/tv/<int:tv_id>')
def specific_tv(tv_id):
    spec_show = Show.query.get(tv_id)
    return render_template("tv/tv.html", template_show=spec_show, template_lists = get_current_lists())

@main.route('/movies')
def movies():
    movies_all = Movie.query.all()
    return render_template("movie/movies.html", template_movies=movies_all)

@main.route('/movies/<int:movie_id>')
def specific_movie(movie_id):
    spec_movie = Movie.query.get(movie_id)
    return render_template("movie/movie.html", template_movie=spec_movie, template_lists = get_current_lists())

@main.route('/games')
def games():
    games_all = Game.query.all()
    return render_template("game/games.html", template_games=games_all)

@main.route('/games/<int:game_id>')
def specific_game(game_id):
    spec_game = Game.query.get(game_id)
    return render_template("game/game.html", template_game=spec_game, template_lists = get_current_lists())

@main.route('/books')
def books():
    books_all = Book.query.all()
    return render_template("book/books.html", template_books=books_all)

@main.route('/books/<int:book_id>')
def specific_book(book_id):
    spec_book = Book.query.get(book_id)
    revs = BookReview.query.filter(BookReview.book_id == book_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("book/book.html", template_book=spec_book, template_lists = get_current_lists(), template_reviews = revs)

@main.route('/profile')
def profile():
    # pass all of users shows, movies, games and books AND lists
    current_user = get_current_user()
    if current_user is None:
        return redirect(url_for('login'))
    rec_reviews = BookReview.query.filter(BookReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(rec_reviews):
        rec_reviews[i].book = Book.query.get(elem.book_id)
    return render_template("profile.html", template_lists = get_current_lists(), cur_user=current_user, template_reviews=rec_reviews)

@main.route('/newlist', methods=['POST'])
def new_list():
    title = request.form.get('listname')
    if logged_in() and title != None:
        reviewer = get_current_user()
    newlist = List(title=title, reviewer_id = reviewer.id)
    db.session.add(newlist)
    db.session.commit()
    return redirect(url_for('profile'))

@main.route('/newreview', methods=['POST'])
def new_list():
    title = request.form.get('listname')
    if logged_in() and title != None:
        reviewer = get_current_user()
    newlist = List(title=title, reviewer_id = reviewer.id)
    db.session.add(newlist)
    db.session.commit()
    return redirect(url_for('profile'))

@main.route('/lists/<int:list_id>')
def specific_list(list_id):
    # pass all of users shows, movies, games and books AND lists
    spec_list = List.query.get(list_id)
    items = BookListLink.query.filter(BookListLink.list_id == list_id).all()
    for i, elem in enumerate(items):
        items[i] = Book.query.get(elem.book_id)
    return render_template("list.html", template_list = spec_list, template_items = items)

@main.route('/addbooktolist/<int:new_list_id>/<int:new_book_id>')
def add_to_list(new_list_id, new_book_id):
    db.session.add(BookListLink(list_id=new_list_id, book_id=new_book_id))
    db.session.commit()
    spec_book = Book.query.get(new_book_id)
    return render_template("book/book.html", template_book=spec_book, template_lists = get_current_lists())

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    reviewer = Reviewer.query.filter_by(username=username).first()
    if not reviewer or not check_password_hash(reviewer.password_hash, password):
        flash('Please check your login details and try again.')
        return render_template('login.html')
    set_current_user(reviewer)
    return redirect(url_for('profile'))

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/signup', methods=['POST'])
def signup_post():
    # validate and add user to the database
    username = request.form.get('username')
    password = request.form.get('password')
    reviewer = Reviewer.query.filter_by(username=username).first()
    if reviewer:
        flash('Email address already in use')
        return redirect(url_for('signup'))
    new_reviewer = Reviewer(username=username, password_hash=generate_password_hash(password, method='sha256'))
    db.session.add(new_reviewer)
    db.session.commit()
    return redirect(url_for('login'))

@main.route('/logout')
def logout():
    return 'Logout'

main.run(host='0.0.0.0', port=5001)

