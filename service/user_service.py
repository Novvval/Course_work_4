import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user_dao import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_by_email(self, email):
        return self.user_dao.get_by_email(email)

    def get_by_id(self, uid):
        return self.user_dao.get_by_id(uid)

    def add_user(self, data):
        password = self.get_hash(data["password"])
        data["password"] = password
        return self.user_dao.add_user(data)

    def update_user_password(self, data):
        uid = data["id"]
        new_password = data["password_2"]
        user = self.get_by_id(uid)
        user.password = self.get_hash(new_password)
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

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")