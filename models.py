from __init__ import db

# User Model
class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique=True)
    password_hash = db.Column(db.String(128))
    user_lists = db.relationship('List', backref="list", lazy='dynamic')
    book_count = db.Column(db.Integer, index=False, unique=False)
    movie_count = db.Column(db.Integer, index=False, unique=False)
    game_count = db.Column(db.Integer, index=False, unique=False)
    show_count = db.Column(db.Integer, index=False, unique=False)

# Media Items
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    author = db.Column(db.String(100), index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    seasons = db.Column(db.Integer, index=True, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    image = db.Column(db.Text(5000))

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique=True)
    description = db.Column(db.String(1000), index=False, unique=False)
    release = db.Column(db.Integer, index=False, unique=False)
    platforms = db.Column(db.String(50), index=False, unique=False)
    image = db.Column(db.Text(5000))

# Review Models
class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
    consumed = db.Column(db.Boolean)

class MovieReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
    consumed = db.Column(db.Boolean)

class ShowReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
    consumed = db.Column(db.Boolean)

class GameReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), index=False, unique=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
    consumed = db.Column(db.Boolean)
    
# Lists and List Helper Models
class List(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index=True, unique=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

class BookListLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), index=True)

class MovieListLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), index=True)

class ShowListLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), index=True)

class GameListLink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)  
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), index=True)