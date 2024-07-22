from flask_restful import Resource, reqparse
from models.user import User
from utils.database import db
from flask_jwt_extended import create_access_token
from utils.errors import InvalidUsage

class UserRegister(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
    

    def post(self):
        args = self.parser.parse_args()
        if User.query.filter_by(email=args['email']).first():
            raise InvalidUsage('Email already exists', status_code=400)
        user = User(name=args['name'], email=args['email'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User Registered successfully'}, 201
    

class UserLogin(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(email=args['email']).first()
        if user and user.check_password(args['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return InvalidUsage('Invalid Email or Password', status_code=401)