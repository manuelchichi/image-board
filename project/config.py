# /config.py

import os

config = {
    "development": "project.config.DevelopmentConfig",
    "testing": "project.config.TestingConfig",
    "production": "project.config.ProductionConfig",
    "default": "project.config.DevelopmentConfig"
}

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    MONGO_URI = 'mongodb://localhost:27017/image-board-dev'
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/image-board-test'
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    MONGO_URI = 'mongodb://localhost:27017/image-board'


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])
    app.config.from_pyfile("config.cfg", silent=True)
    app.secret_key = '1231qsaa566a4s6d4a6sa'