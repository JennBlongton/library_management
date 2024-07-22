from flask_restful import Resource, reqparse
from services.book_service import BookService
from flask_jwt_extended import jwt_required


class BookResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help='Title is required')
        self.parser.add_argument('author_id', type=int, required=True, help='Author ID is required')
        self.parser.add_argument('user_id', type=str, required=False, help='User ID is optional')

    @jwt_required()
    def get(self, book_id=None):
        if book_id:
            book = BookService.get_book_by_id(book_id)
            if book:
                return {'id': book.id, 'title': book.title, 'author_id': book.author_id, 'user_id': book.user_id}, 200
            return {'message': 'Book not found'}, 404
        
        books = BookService.get_all_books()
        return [{'id': book.id, 'title': book.title, 'author_id': book.author_id, 'user_id': book.user_id} for book in books], 200
    
    @jwt_required()
    def post(self, book_id):
        args = self.parser.parse_args()
        book = BookService.create_book(args)
        return {'id': book.id, 'title': book.title, 'author_id': book.author_id, 'user_id': book.user_id}, 201
    
    @jwt_required()
    def put(self, book_id):
        args = self.parser.parse_args()
        book = BookService.get_book_by_id(book_id)
        if book:
            updated_book = BookService.update_book(book, args)
            return {'id': updated_book.id, 'title': updated_book.title, 'author_id': updated_book.author_id, 'user_id': updated_book.user_id}, 200
        return {'message': 'Book not found'}, 404
    
    @jwt_required()
    def delete(self, book_id):
        book = BookService.get_book_by_id(book_id)
        if book:
            BookService.delete_book(book)
            return {'message': 'Book deleted'}, 200
        return {'message': 'Book not found'}, 404