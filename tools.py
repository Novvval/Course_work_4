import calendar
import datetime
import hashlib
import jwt
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET, ALGORITHM


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")


def generate_tokens(data):
    try:
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
    except jwt.PyJWTError as e:
        return f"{e}"
    return tokens




