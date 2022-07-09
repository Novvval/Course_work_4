from dao.auth_dao import AuthDAO
from dao.movie_dao import MovieDAO
from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.user_dao import UserDAO
from service.auth_service import AuthService
from service.user_service import UserService
from setup_db import db
from service.movie_service import MovieService
from service.genre_service import GenreService
from service.directors_service import DirectorService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

auth_dao = AuthDAO(db.session)
auth_service = AuthService(auth_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
