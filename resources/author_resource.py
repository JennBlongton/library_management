from flask_restful import Resource, reqparse
from services.author_service import AuthorService
from flask_jwt_extended import jwt_required


class AuthorResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name is required')

    @jwt_required()
    def get(self, author_id=None):
        if author_id:
            author = AuthorService.get_author_by_id(author_id)
            if author:
                return {'id': author.id, 'name': author.name}, 200
            return {'message': 'Author not found'}, 404
        authors = AuthorService.get_all_authors()
        return [{'id': author.id, 'name': author.name} for author in authors], 200
    
    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        author = AuthorService.create_author(args)
        return {'id': author.id, 'name': author.name}, 201
    
    @jwt_required()
    def put(self, author_id):
        args = self.parser.parse_args()
        author = AuthorService.get_author_by_id(author_id)
        if author:
            updated_author = AuthorService.create_author(author, args)
            return {'id': updated_author.id, 'name': updated_author.name}, 200
        return {'message': 'Author not found'}, 404
    
    @jwt_required()
    def delete(self, author_id):
        author = AuthorService.get_author_by_id(author_id)
        if author:
            AuthorService.delete_author(author)
            return {'message': 'Author Deleted'}, 200
        return {'message': 'Author not found'}, 404
