from flask_sqlalchemy import Pagination

from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def paginate(self, data, page, per_page):
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        items = data[start_index:end_index]
        return Pagination(None, page, per_page, len(data), items)

    def get_all_genres(self):
        return self.genre_dao.get_all_genres()

    def get_one_genre(self, gid):
        return self.genre_dao.get_one_genre(gid)
