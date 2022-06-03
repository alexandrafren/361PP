import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests as requests
import json
import string
from shareddb import db
from models import Book, Movie, Show, Game, Reviewer, BookListLink, MovieListLink, ShowListLink, GameListLink, BookReview, MovieReview, ShowReview, GameReview, List

app = Flask(__name__)
    
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

global current_user
current_user = None

# on start up - testing microservice integration!
"""
shows_all = Show.query.all()
for show in shows_all:
    translator = str.maketrans('', '', string.punctuation)
    title = show.title.translate(translator)
    product_dict = {"product": show.title + " show"}
    product_json = json.dumps(product_dict, indent=4)
    details = requests.get("http://127.0.0.1:5000/", json=product_json)
    show.image = details.json()['product_image']
    db.session.commit()
"""

#GET/SET METHODS
def get_current_user():
    return current_user

def get_current_lists():
    current_user = get_current_user()
    if current_user is not None:
        return List.query.filter(List.reviewer_id == current_user.id).all()
    else:
        return []

def set_current_user(user):
    global current_user
    current_user = user

def logged_in():
    if current_user == None:
        return False
    else:
        return True

def create_review(text, type, id):
    # helper method used to create new reviews
    if logged_in() and text != None:
        reviewer = get_current_user()
        if type == "Book": 
            newreview = BookReview(text=text, book_id=id, reviewer_id = reviewer.id, consumed = True ); reviewer.book_count += 1
        if type == "Game": 
            newreview = GameReview(text=text, game_id=id, reviewer_id = reviewer.id, consumed = True ); reviewer.game_count += 1
        if type == "Movie": 
            newreview = MovieReview(text=text, movie_id=id, reviewer_id = reviewer.id, consumed = True ); reviewer.movie_count += 1
        if type == "Show": 
            newreview = ShowReview(text=text, show_id=id, reviewer_id = reviewer.id, consumed = True ); reviewer.show_count += 1
    db.session.add(newreview)
    db.session.commit()

@app.route('/')
def home():
    # Home/Index Page, Shows 10 of each media item
    books = Book.query.limit(10).all()
    shows = Show.query.limit(10).all()
    movies = Movie.query.limit(10).all()
    games = Game.query.limit(10).all()
    return render_template("index.html", template_books=books, template_shows = shows, template_movies = movies, template_games = games)

@app.route('/shows')
def show():
    # Shows all TV Shows
    shows_all = Show.query.all()
    return render_template("show/shows.html", template_shows=shows_all)

@app.route('/shows/<int:show_id>')
def specific_show(show_id):
    # Returns a specific TV show and its reviews
    spec_show = Show.query.get(show_id)
    revs = ShowReview.query.filter(ShowReview.show_id == show_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("show/show.html", template_show=spec_show, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/movies')
def movies():
    # Shows all Movies
    movies_all = Movie.query.all()
    return render_template("movie/movies.html", template_movies=movies_all)

@app.route('/movies/<int:movie_id>')
def specific_movie(movie_id):
    # Returns a specific movie and its reviews 
    spec_movie = Movie.query.get(movie_id)
    revs = MovieReview.query.filter(MovieReview.movie_id == movie_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("movie/movie.html", template_movie=spec_movie, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/games')
def games():
    # Shows all games
    games_all = Game.query.all()
    return render_template("game/games.html", template_games=games_all)

@app.route('/games/<int:game_id>')
def specific_game(game_id):
    # Returns a specific game and its reviews 
    spec_game = Game.query.get(game_id)
    revs = GameReview.query.filter(GameReview.game_id == game_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("game/game.html", template_game=spec_game, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/books')
def books():
    # Shows all books
    books_all = Book.query.all()
    return render_template("book/books.html", template_books=books_all)

@app.route('/books/<int:book_id>')
def specific_book(book_id):
    # Returns a specific book and its reviews 
    spec_book = Book.query.get(book_id)
    revs = BookReview.query.filter(BookReview.book_id == book_id)
    for i, elem in enumerate(revs):
        revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("book/book.html", template_book=spec_book, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/profile')
def profile():
    # pass all of users shows, movies, games and books AND lists
    cur_user = get_current_user()
    if cur_user is None: return redirect(url_for('login'))
    # return all reviews and enumerate through them to replace the reviewer with a name and not just an ID number
    book_reviews = BookReview.query.filter(BookReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(book_reviews): book_reviews[i].book = Book.query.get(elem.book_id)
    movie_reviews = MovieReview.query.filter(MovieReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(movie_reviews): movie_reviews[i].movie = Movie.query.get(elem.movie_id)
    game_reviews = GameReview.query.filter(GameReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(game_reviews): game_reviews[i].game = Game.query.get(elem.game_id)
    show_reviews = ShowReview.query.filter(ShowReview.reviewer_id == current_user.id).all()
    for i, elem in enumerate(show_reviews): show_reviews[i].show = Show.query.get(elem.show_id)
    return render_template("profile.html", template_lists = get_current_lists(), cur_user=current_user, 
        template_book_reviews=book_reviews, template_movie_reviews=movie_reviews, template_game_reviews=game_reviews, template_show_reviews=show_reviews)

@app.route('/newlist', methods=['POST'])
def new_list():
    # creates a new list and commits to the DB
    title = request.form.get('listname')
    if logged_in() and title != None: reviewer = get_current_user()
    newlist = List(title=title, reviewer_id = reviewer.id)
    db.session.add(newlist)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/newbookreview', methods=['POST'])
def new_book_review():
    # creates a new book review and commits to the DB
    text = request.form.get('review')
    book_id = request.form.get('book_id')
    create_review(text, "Book", book_id)
    spec_book = Book.query.get(book_id)
    revs = BookReview.query.filter(BookReview.book_id == book_id)
    for i, elem in enumerate(revs): revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("book/book.html", template_book=spec_book, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/newgamereview', methods=['POST'])
def new_game_review():
    # creates a new game review and commits to the DB
    text = request.form.get('review')
    game_id = request.form.get('game_id')
    create_review(text, "Game", game_id)
    spec_game = Game.query.get(game_id)
    revs = GameReview.query.filter(GameReview.game_id == game_id)
    for i, elem in enumerate(revs): revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("game/game.html", template_game=spec_game, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/newmoviereview', methods=['POST'])
def new_movie_review():
    # creates a new movie review and commits to the DB
    text = request.form.get('review')
    movie_id = request.form.get('movie_id')
    create_review(text, "Movie", movie_id)
    spec_movie = Movie.query.get(movie_id)
    revs = MovieReview.query.filter(MovieReview.movie_id == movie_id)
    for i, elem in enumerate(revs): revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("movie/movie.html", template_movie=spec_movie, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/newshowreview', methods=['POST'])
def new_show_review():
    # creates a new show review and commits to the DB
    text = request.form.get('review')
    show_id = request.form.get('show_id')
    create_review(text, "Show", show_id)
    spec_show = Show.query.get(show_id)
    revs = ShowReview.query.filter(ShowReview.show_id == show_id)
    for i, elem in enumerate(revs): revs[i].user = Reviewer.query.get(elem.reviewer_id).username
    return render_template("show/show.html", template_show=spec_show, template_lists = get_current_lists(), template_reviews = revs)

@app.route('/lists/<int:list_id>')
def specific_list(list_id):
    # pass all of users shows, movies, games and books for a specific list
    spec_list = List.query.get(list_id)
    bookitems = BookListLink.query.filter(BookListLink.list_id == list_id).all()
    showitems = ShowListLink.query.filter(ShowListLink.list_id == list_id).all()
    movieitems = MovieListLink.query.filter(MovieListLink.list_id == list_id).all()
    gameitems = GameListLink.query.filter(GameListLink.list_id == list_id).all()
    for i, elem in enumerate(bookitems): bookitems[i] = Book.query.get(elem.book_id)
    for i, elem in enumerate(showitems): showitems[i] = Show.query.get(elem.show_id)
    for i, elem in enumerate(movieitems): movieitems[i] = Movie.query.get(elem.movie_id)
    for i, elem in enumerate(gameitems): gameitems[i] = Game.query.get(elem.game_id)
    return render_template("list.html", template_list = spec_list, template_books = bookitems, 
        template_shows = showitems, template_movies = movieitems, template_games=gameitems)

@app.route('/addbooktolist/<int:new_list_id>/<int:new_book_id>')
def add_book_to_list(new_list_id, new_book_id):
    # adds a book to a user list
    db.session.add(BookListLink(list_id=new_list_id, book_id=new_book_id))
    db.session.commit()
    spec_book = Book.query.get(new_book_id)
    return render_template("book/book.html", template_book=spec_book, template_lists = get_current_lists())

@app.route('/addgametolist/<int:new_list_id>/<int:new_game_id>')
def add_game_to_list(new_list_id, new_game_id):
    # adds a game to a user list
    db.session.add(GameListLink(list_id=new_list_id, game_id=new_game_id))
    db.session.commit()
    spec_game = Game.query.get(new_game_id)
    return render_template("game/game.html", template_game=spec_game, template_lists = get_current_lists())

@app.route('/addmovietolist/<int:new_list_id>/<int:new_movie_id>')
def add_movie_to_list(new_list_id, new_movie_id):
    # adds a move to a user list 
    db.session.add(MovieListLink(list_id=new_list_id, movie_id=new_movie_id))
    db.session.commit()
    spec_movie = Movie.query.get(new_movie_id)
    return render_template("movie/movie.html", template_movie=spec_movie, template_lists = get_current_lists())

@app.route('/addshowtolist/<int:new_list_id>/<int:new_show_id>')
def add_show_to_list(new_list_id, new_show_id):
    # adds a show to a user list 
    db.session.add(ShowListLink(list_id=new_list_id, show_id=new_show_id))
    db.session.commit()
    spec_show = Show.query.get(new_show_id)
    return render_template("show/show.html", template_show=spec_show, template_lists = get_current_lists())

@app.route('/login')
def login():
    # loads the login form for a user
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    # logs a user in, returns error if incorrect
    username = request.form.get('username')
    password = request.form.get('password')
    reviewer = Reviewer.query.filter_by(username=username).first()
    if not reviewer or not check_password_hash(reviewer.password_hash, password):
        flash('Please check your login details and try again.')
        return render_template('login.html')
    set_current_user(reviewer)
    return redirect(url_for('profile'))

@app.route('/signup')
def signup():
    # loads the sign up for for a user
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # validate and add user to the database
    username = request.form.get('username')
    password = request.form.get('password')
    reviewer = Reviewer.query.filter_by(username=username).first()
    if reviewer:
        flash('Email address already in use')
        return redirect(url_for('signup'))
    new_reviewer = Reviewer(username=username, password_hash=generate_password_hash(password, method='sha256'), book_count = 0, game_count = 0, movie_count = 0, show_count = 0)
    db.session.add(new_reviewer)
    db.session.commit()
    return redirect(url_for('login'))

app.run(host='0.0.0.0', port=5001)

