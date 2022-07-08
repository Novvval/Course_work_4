from flask import Flask, render_template
from flask_restx import Api
from config import Config
from dao.model.director_model import Director
from dao.model.genre_model import Genre
from dao.model.movie_model import Movie
from dao.model.user_model import User
from setup_db import db
from views.auth_view import auth_ns
from views.movies_view import movie_ns
from views.genres_view import genre_ns
from views.directors_view import director_ns
from data import genres, directors, movies
from views.users_view import user_ns
from flask_cors import CORS


api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 4",
    doc="/docs",
)
cors = CORS()


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    register_extensions(app)

    @app.route('/')
    def index():
        return render_template("index.html")
    return app


def register_extensions(app):
    db.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
#     create_data(db)
#
#
# def create_data(db):
#     db.create_all()
#     for movie in movies:
#         movie["id"] = movie.pop('pk')
#         movie = Movie(**movie)
#         db.session.add(movie)
#     for genre in genres:
#         genre["id"] = genre.pop('pk')
#         genre = Genre(**genre)
#         db.session.add(genre)
#     for director in directors:
#         director["id"] = director.pop('pk')
#         director = Director(**director)
#         db.session.add(director)
#     db.session.commit()


config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=2500, debug=True)
