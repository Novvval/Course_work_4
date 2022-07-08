from dao.model.director_model import Director
from dao.model.genre_model import Genre
from dao.model.movie_model import Movie
from data import movies, genres, directors
from setup_db import db


def create_data(db):
    db.create_all()
    for movie in movies:
        movie["id"] = movie.pop('pk')
        movie = Movie(**movie)
        db.session.add(movie)
    for genre in genres:
        genre["id"] = genre.pop('pk')
        genre = Genre(**genre)
        db.session.add(genre)
    for director in directors:
        director["id"] = director.pop('pk')
        director = Director(**director)
        db.session.add(director)
    db.session.commit()


create_data(db)