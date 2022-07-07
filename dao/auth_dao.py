from dao.model.user_model import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).first()
        return user
