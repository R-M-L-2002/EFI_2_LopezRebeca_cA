from models import User
from app import db

class UserRepository:
    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def add(self, user):
        db.session.add(user)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
