from flask import request
from flask_restx import Resource, Namespace
from flask_sqlalchemy import BaseQuery

from implemented import movie_service
from dao.model.movie_model import movies_schema, movie_schema
from views.decorators import auth_required, admin_required

movie_ns = Namespace("movies")


@movie_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        movies = movie_service.get_all_movies()
        if status == "new":
            movies = movie_service.get_new_movies()
        if page is not None:
            movies = movie_service.paginate(movies, int(page), per_page=5).items

        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        data = request.get_json()

        movie_service.add_movie(data)
        return "", 201


@movie_ns.route('/<int:mid>')
class GenreView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one_movie(mid)
        return movie_schema.dump(movie), 200
