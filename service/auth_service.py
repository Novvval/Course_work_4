import calendar
import datetime
import hashlib
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET, ALGORITHM
import jwt
from flask_restx import abort
from dao.auth_dao import AuthDAO


class AuthService:
    def __init__(self, auth_dao: AuthDAO):
        self.auth_dao = auth_dao

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def create_tokens(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            abort(401)

        user = self.auth_dao.get_by_email(email)
        if user is None:
            abort(401)

        password = self.get_hash(password)
        if password != user.password:
            abort(403)

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens

    def update(self, data):
        refresh_token = data["refresh_token"]
        if refresh_token is None:
            abort(401)

        try:
            jwt.decode(refresh_token=refresh_token, key=SECRET, algorithm=ALGORITHM)
        except Exception:
            abort(403)

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens