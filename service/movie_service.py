from flask_sqlalchemy import Pagination

from dao.model.director_model import Director
from dao.model.genre_model import Genre
from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def paginate(self, data, page, per_page):
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        items = data[start_index:end_index]
        return Pagination(None, page, per_page, len(data), items)

    def get_all_movies(self):
        return self.movie_dao.get_all_movies()

    def get_new_movies(self):
        return self.movie_dao.get_new_movies()

    def get_one_movie(self, mid):
        return self.movie_dao.get_one_movie(mid)

    def add_movie(self, data):
        return self.movie_dao.add_movie(data)

    def update_movie(self, data):
        mid = data["id"]
        movie = self.get_one_movie(mid)

        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]
        return self.movie_dao.update_movie(movie)

    def update_movie_partial(self, data):
        mid = data["id"]
        movie = self.get_one_movie(mid)
        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]
        if "genre_id" in data:
            movie.genre_id = data["genre_id"]
        if "director_id" in data:
            movie.director_id = data["director_id"]

        return self.movie_dao.update_movie(movie)

    def delete_movie(self, mid):
        return self.movie_dao.delete_movie(mid)


