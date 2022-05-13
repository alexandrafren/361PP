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

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    author = db.Column(db.String(100), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    #reviews = db.relationship('BookReview', backref='book', lazy='dynamic')
""" 
class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique=True)
    book_reviews = db.relationship('BookReview', backref='reviewer', lazy='dynamic')

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id')) """

#b1 = Book(title="Feed", author="Mira Grant", description="The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.The truth will get out, even if it kills them.", release=2010)
# r1 = Reviewer(username="alixp")
#db.session.add(b1)
# db.session.add(r1)

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
    return(str(len(books_all)))
    #return render_template("books.html", template_books=books_all)

@app.route('/profile')
def profile():
    return "Profile will be here!"

app.run(host='0.0.0.0', port=5000)