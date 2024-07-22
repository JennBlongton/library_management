from flask import Flask
from flask_restful import Api
from resources.book_resource import BookResource
from resources.author_resource import AuthorResource
from resources.user_resource import UserResource
from resources.auth_resource import UserRegister, UserLogin
from utils.database import db
from flask_jwt_extended import JWTManager
from utils.errors import ErrorHandling, InvalidUsage


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    # Add Resources
    api.add_resource(BookResource, '/books', '/books/<int:book_id>')
    api.add_resource(AuthorResource, '/authors', '/authors/<int:author_id>')
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    # Error handling
    app.register_error_handler(InvalidUsage, ErrorHandling.handle_invalid_usage)
    
    return app


if __name__=='__main__':
    app = create_app()
    app.run(debug=True)