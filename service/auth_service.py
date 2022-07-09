from constants import SECRET, ALGORITHM
import jwt
from flask_restx import abort
from dao.auth_dao import AuthDAO
from utils.tools import generate_tokens, get_hash


class AuthService:
    def __init__(self, auth_dao: AuthDAO):
        self.auth_dao = auth_dao

    def create_tokens(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            abort(401)

        user = self.auth_dao.get_by_email(email)
        if user is None:
            abort(401)

        password = get_hash(password)
        if password != user.password:
            abort(403)

        return generate_tokens(data)

    def update_token(self, data):
        refresh_token = data["refresh_token"]
        if not refresh_token:
            abort(401)

        try:
            jwt.decode(refresh_token=refresh_token, key=SECRET, algorithm=ALGORITHM)
        except Exception as e:
            return f"{e}"

        return generate_tokens(data)
