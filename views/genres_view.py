from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound

from implemented import genre_service
from dao.model.genre_model import genres_schema, genre_schema
from views.decorators import auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        genres = genre_service.get_all_genres()
        if page is not None:
            genres = genre_service.paginate(genres, int(page), per_page=5)
        return genres_schema.dump(genres.items), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        try:
            genre = genre_service.get_one_genre(gid)
        except NoResultFound as e:
            return f"{e}", 400

        return genre_schema.dump(genre), 200
