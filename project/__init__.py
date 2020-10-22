from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from flask_login import LoginManager
from project.config import configure_app
from .models import User
import os
import project

mongo = PyMongo()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    configure_app(app)

    mongo.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        userJson = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        return User(userJson)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app