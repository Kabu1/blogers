import os
class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY ='qwerty1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
     #email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}