from models.book import Book
from utils.database import db


class BookService:
    @staticmethod
    def get_all_books():
        return Book.query.all()
    
    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)
    
    @staticmethod
    def create_book(data):
        new_book = Book(title=data['title'], author_id=data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return new_book
    
    @staticmethod
    def update_book(book, data):
        book.title = data['title']
        book.author_id = data['author_id']
        if 'user_id' in data:
            book.user_id = data['user_id']
        db.session.commit()
        return book
    
    @staticmethod
    def delete_book(book):
        db.session.delete(book)
        db.session.commit()