from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from app.extensions.jwt_ext import jwt
from app.models import db
from app.schemas import ma
from app.api import api_v1
from flask_cors import CORS
from app import settings
from app.utils.before_request import request_intercept
from app.extensions.error_ext import handle_exception


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.DevConfig)

    api = Api()
    migrate = Migrate()
    cors = CORS(resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    with app.app_context():
        cors.init_app(app)
        # db
        db.init_app(app)
        # api
        api.init_app(app)
        # ma
        ma.init_app(app)
        # cors
        # migrate
        migrate.init_app(app, db)
        jwt.init_app(app)
        # socketio.init_app(app)
        # return socketio ，Error: A valid Flask application was not obtained from 'flaskchat-backend.app:create_app()'
    app.before_request(request_intercept)
    api.register_blueprint(api_v1)
    app.errorhandler(Exception)(handle_exception)

    return app
