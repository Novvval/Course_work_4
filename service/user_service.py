import hashlib

import jwt
from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET, ALGORITHM
from dao.user_dao import UserDAO
from tools import get_hash


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_by_token(self, token):
        token = token.split("Bearer ")[-1]
        user = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        email = user["email"]
        return self.user_dao.get_by_email(email)

    def get_by_id(self, uid):
        return self.user_dao.get_by_id(uid)

    def add_user(self, data):
        password = get_hash(data["password"])
        data["password"] = password
        return self.user_dao.add_user(data)

    def update_user_password(self, data):
        uid = data["id"]
        old_password = get_hash(data["password_1"])
        new_password = data["password_2"]
        user = self.get_by_id(uid)
        if old_password != user.password:
            abort(403)
        user.password = get_hash(new_password)
        return self.user_dao.update_user(user)

    def update_user_info(self, data):
        uid = data["id"]
        user = self.get_by_id(uid)
        if "email" in data:
            user.email = data["email"]
        if "name" in data:
            user.name = data["name"]
        if "surname" in data:
            user.surname = data["surname"]
        if "favorite_genre" in data:
            user.favorite_genre = data["favorite_genre"]
        return self.user_dao.update_user(user)
