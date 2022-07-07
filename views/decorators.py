from flask import request
import jwt
from constants import SECRET, ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        try:
            data = request.headers["Authorization"]
        except Exception as e:
            return f"Authorization error: {e}", 401
        token = data.split("Bearer")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        except Exception as e:
            return f"JWT decode error: {e}"
        return func(*args, **kwargs)
    return wrapper
