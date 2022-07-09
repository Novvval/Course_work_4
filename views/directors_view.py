from flask import request
from flask_restx import Resource, Namespace
from implemented import director_service
from dao.model.director_model import directors_schema, director_schema
from views.decorators import auth_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        directors = director_service.get_all_directors()
        if page is not None:
            directors = director_service.paginate(directors, int(page), per_page=5).items
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
@director_ns.doc(params={'did': 'Director id'})
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one_director(did)
        return director_schema.dump(director), 200
