Portfolio Project for OSU CS361

Python, Flask, SQLite


Microservice referenced by teammate: https://github.com/alexandrafren/random-microservice 

Reference Code:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login


Seed Data:
Stored: https://docs.google.com/spreadsheets/d/14FEp7v6DWOT7JIexWhf3h1lxYZcCd9g9fUHPelFLQLc/edit#gid=0 
Video Games: https://en.wikipedia.org/wiki/List_of_zombie_video_games
Books: https://en.wikipedia.org/wiki/List_of_zombie_novels
Movies: https://en.wikipedia.org/wiki/List_of_zombie_films
Shows: https://en.wikipedia.org/wiki/Category:Zombies_in_television

Icon:
Apple Zombie Emoji: https://emojipedia.org/apple/ios-11.1/zombie/ 

To seed DB:
from app import app, db
from models import Book, Movie, Show, Game, Reviewer, BookListLink, MovieListLink, ShowListLink, GameListLink, BookReview, MovieReview, ShowReview, GameReview, List
app.app_context().push()
db.create_all()
copy/paste seed data from create_objects()
db.session.commit()
