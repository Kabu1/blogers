from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

# Initializing application
app = Flask(__name__)

# Initializing flask extensions
bootstrap.init_app(app)
db.init_app(app)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
