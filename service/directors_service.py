from flask_sqlalchemy import Pagination

from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def paginate(self, data, page, per_page):
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        items = data[start_index:end_index]
        return Pagination(None, page, per_page, len(data), items)

    def get_all_directors(self):
        return self.director_dao.get_all_directors()

    def get_one_director(self, did):
        return self.director_dao.get_one_director(did)
