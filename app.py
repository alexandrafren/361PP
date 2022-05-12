from flask import Flask, render_template, request
from movies import movies, descriptions

app = Flask(__name__)

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
    return "Books will be here!"

@app.route('/profile')
def profile():
    return "Profile will be here!"

app.run(host='0.0.0.0', port=5000)