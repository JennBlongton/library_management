from utils.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    borrowed_books = db.relationship('Book', backref='user', lazy=True)


    def __repr__(self) -> str:
        return f'<User {self.name}'