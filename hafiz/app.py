import functools
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

migrate = Migrate()
db = SQLAlchemy()
marshmallow = Marshmallow()

def get_database_url():
    DB_NAME = os.environ.get('DB_NAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_USER = os.environ.get('DB_USER')

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    print(DATABASE_URL)
    return DATABASE_URL


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    with app.app_context():
        from .views import reciter_data_bp, surah_bp, ayah_variation_bp, word_variation_bp
        app.register_blueprint(reciter_data_bp)
        app.register_blueprint(surah_bp)
        app.register_blueprint(ayah_variation_bp)
        app.register_blueprint(word_variation_bp)
        return app


def get_app_context():
    """
    Function either gets the current flask app or creates a new one.
    :return: (Flask)  A flask application instance
    """
    from flask import current_app

    if current_app:
        return current_app
    else:
        return create_app()


def with_app_context(fn):
    """
    Decorator to wrap a given function in a flask application context.
    """

    # intended for use with zappa event handler functions, making them more analagous to views

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        app = get_app_context()

        with app.app_context():
            return fn(*args, **kwargs)

    return wrapper
