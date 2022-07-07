from dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_new_movies(self):
        return self.session.query(Movie).order_by(Movie.year.desc())

    def get_one_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def add_movie(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete_movie(self, mid):
        book = self.get_one_movie(mid)
        self.session.delete(book)
        self.session.commit()
