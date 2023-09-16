from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from .constants import DB_NAME
from os import path

def create_app():
    app = Flask(__name__)
    # Configuring the db
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    from .views import views
    with app.app_context():
        create_database(app)
        
    app.register_blueprint(views, url_prefix="/")

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()