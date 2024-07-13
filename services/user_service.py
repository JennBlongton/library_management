from models.user import User
from utils.database import db


class UserService:
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def create_user(data):
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def update_user(user, data):
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()