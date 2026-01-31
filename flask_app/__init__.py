from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .utils import time_ago



db = SQLAlchemy()           # Create database object
login_manager = LoginManager()     # Create login manager object
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    
    app.config['SECRET_KEY'] = 'mysecretkey'   # Secret key for forms (CSRF protection)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database setup (SQLite file)
    app.jinja_env.filters['timeago'] = time_ago
    
    db.init_app(app)               # Initialize extensions
    login_manager.init_app(app)
    migrate.init_app(app, db)


    
    login_manager.login_view = 'login'  # Redirect to login if not authenticated
    


    return app
