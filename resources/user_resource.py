from flask_restful import Resource, reqparse
from services.user_service import UserService
from flask_jwt_extended import jwt_required


class UserResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')

    @jwt_required()
    def get(self, user_id=None):
        if user_id:
            user = UserService.get_user_by_id(user_id)
            if user:
                return {'id': user.id, 'name': user.name, 'email': user.email}, 200
            return {'message': 'User not found'}, 404
        users = UserService.get_all_users()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users], 200
    
    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        user = UserService.create_user(args)
        return {'id': user.id, 'name': user.name, 'email': user.email}, 201

    @jwt_required()
    def put(self, user_id):
        args = self.parser.parse_args()
        user = UserService.get_user_by_id(user_id)
        if user:
            updated_user = UserService.update_user(user, args)
            return {'id': updated_user.id, 'name': updated_user.name, 'email': updated_user.email}, 200
        return {'message': 'User not found'}, 404
    
    @jwt_required()
    def delete(self, user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            UserService.delete_user(user)
            return {'message': 'User deleted'}, 200
        return {'message': 'User not found'}, 404