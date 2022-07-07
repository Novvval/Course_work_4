from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class AuthViewRegister(Resource):
    def post(self):
        data = request.get_json()
        user_service.add_user(data)
        return "", 201


@auth_ns.route("/login")
class AuthViewLogin(Resource):
    def post(self):
        data = request.get_json()
        return auth_service.create_tokens(data), 201

    def put(self):
        data = request.get_json()
        return auth_service.update(data), 204
