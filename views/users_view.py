from flask import request
from flask_restx import Namespace, Resource

from dao.model.user_model import user_schema
from implemented import user_service
from views.decorators import auth_required

user_ns = Namespace("users")


@user_ns.route("/")
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers["Authorization"]
        user = user_service.get_by_token(data)
        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        data = request.get_json()
        user_service.update_user_info(data)
        return "", 204


@user_ns.route("/password")
class UserPassword(Resource):
    @auth_required
    def put(self):
        data = request.get_json()
        user_service.update_user_password(data)
        return "", 204
